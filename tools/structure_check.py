#!/usr/bin/env python3
"""比对中文译文与上游 ADOC 原文的结构一致性。

比对维度：
- 标题层级计数（`==` ↔ `##`，`===` ↔ `###`，`====` ↔ `####`，`=====` ↔ `#####`）
- 正文段落数（排除仅含链接、联系方式、属性的行）
- 列表项数
- 链接目标集合（中文侧每个链接必须在上游有对应目标）

用法：
    python tools/structure_check.py <中文.md> [上游adoc目录]

上游目录缺省时，从中文文件头 `- 原文：[...](https://www.freebsd.org/status/report-.../)`
推导为 `en/report-...`。标题、段落、列表任一不匹配即以非零退出码结束。
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

RE_ADOC_ATTR = re.compile(r"^:([A-Za-z0-9_-]+):\s*(.*)$")
RE_ADOC_INCLUDE = re.compile(r"^include::([^\[\s]+)(\[[^\]]*\])?")
RE_ADOC_HEADING = re.compile(r"^(=+)\s+(\S.*)$")
RE_MD_HEADING = re.compile(r"^(#{1,6})\s+(\S.*)$")
RE_ADOC_LIST = re.compile(r"^\s*(?:\*+|-|\.+|\d+\.)\s+")
RE_MD_LIST = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
RE_ADOC_DELIM = re.compile(r"^([-./=+*]{4,})\s*$")
RE_CODE_FENCE_MD = re.compile(r"^(```|~~~)")
RE_ADOC_LINK = re.compile(r"link:([^\[\s]+)\[([^\]]*)\]")
RE_ADOC_XREF = re.compile(r"<<([^,>]+)(?:,([^>]*))?>>")
RE_ADOC_URL = re.compile(r"(?<!link:)(?<![\w\"'=])(https?://[^\s\[\]<>]+)")
RE_ADOC_MAILTO = re.compile(r"(?:mailto:)?([\w.+-]+@[\w.-]+\.[A-Za-z]{2,})")
RE_ADOC_PACKAGE = re.compile(r"package:([^\s\[]+)\[")
RE_ADOC_ATTR_LINK = re.compile(r"\{([A-Za-z0-9_-]+)\}\[([^\]]*)\]")
RE_MD_LINK = re.compile(r"\[[^\]]*\]\(((?:[^()\s]|\([^()]*\))+)\)")
RE_MD_AUTOLINK = re.compile(r"<(https?://[^>]+)>")
RE_META = re.compile(r"^-\s*(?:原文|版本|最后作者)：")
RE_ONLY_LINK_MD = re.compile(r"^\*{0,2}链接\*{0,2}：|^\*\*联系方式\*\*：|^\[[^\]]*\]\([^)]*\)$")
RE_ONLY_LINK_ADOC = re.compile(r"^(?:link:|URL:|\*\*Links\*\*|Links:|Contact:|<\S+@\S+>)")
RE_ADOC_COMMENT = re.compile(r"^//")


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


DEFAULT_ATTRS = {
    "handbook": "https://docs.freebsd.org/en/books/handbook/",
    "fdp-primer": "https://docs.freebsd.org/en/books/fdp-primer/",
}


def load_attrs(index_path: Path) -> dict[str, str]:
    attrs: dict[str, str] = dict(DEFAULT_ATTRS)
    for line in read_lines(index_path):
        m = RE_ADOC_ATTR.match(line)
        if m:
            attrs[m.group(1)] = m.group(2).strip()
    return attrs


def substitute(text: str, attrs: dict[str, str]) -> str:
    for name, value in attrs.items():
        text = text.replace("{" + name + "}", value)
    return text


def resolve_include(entry_dir: Path, target: str) -> Path | None:
    candidates = [entry_dir / target, entry_dir / Path(target).name, entry_dir.parent / Path(target).name]
    for cand in candidates:
        if cand.exists():
            return cand
    return None


def expand_adoc(path: Path, entry_dir: Path, attrs: dict[str, str], seen: set[Path]) -> list[str]:
    if path in seen or not path.exists():
        return []
    seen.add(path)
    out: list[str] = []
    lines = read_lines(path)
    skip_stack: list[bool] = []
    in_comment = False
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("////"):
            in_comment = not in_comment
            continue
        if in_comment:
            continue
        if stripped.startswith("ifdef::"):
            skip_stack.append(False)
            continue
        if stripped.startswith("ifndef::"):
            skip_stack.append(True)
            continue
        if stripped.startswith("endif::"):
            if skip_stack:
                skip_stack.pop()
            continue
        if any(skip_stack):
            continue
        m = RE_ADOC_INCLUDE.match(stripped)
        if m:
            target = substitute(m.group(1), attrs).strip("/")
            sub = resolve_include(entry_dir, target)
            if sub is not None:
                out.extend(expand_adoc(sub, entry_dir, attrs, seen))
            continue
        if line.startswith(("include::", "//")):
            continue
        out.append(substitute(line, attrs))
    return out


def norm_target(url: str) -> str:
    url = url.strip().rstrip(".,:;")
    if url.startswith("mailto:"):
        return "mail:" + url[len("mailto:"):].lower()
    if url.startswith("{"):
        return "unresolved:" + url
    if "#" in url:
        return "anchor:" + url.split("#", 1)[1]
    if url.startswith(("http://", "https://")):
        rest = url.split("://", 1)[1]
        host, _, path = rest.partition("/")
        if host == "www.freshports.org":
            return "pkg:" + path.strip("/")
        if host == "cgit.freebsd.org" and path.startswith("ports/tree/"):
            return "pkg:" + path[len("ports/tree/"):].strip("/")
        if host in ("www.freebsd.org", "freebsd.org") or host.endswith(".freebsd.org"):
            return "path:" + path.strip("/")
        return "url:" + url.rstrip("/")
    if url.startswith("#"):
        return "anchor:" + url[1:]
    tail = "/".join(p for p in url.split("/") if p and p not in (".", ".."))
    return "path:" + tail


def adoc_links(lines: list[str]) -> set[str]:
    keys: set[str] = set()
    for line in lines:
        for url, _text in RE_ADOC_LINK.findall(line):
            keys.add(norm_target(url))
        for anchor, _text in RE_ADOC_XREF.findall(line):
            keys.add("anchor:" + anchor.strip())
        for url in RE_ADOC_URL.findall(line):
            keys.add(norm_target(url))
        for addr in RE_ADOC_MAILTO.findall(line):
            keys.add("mail:" + addr.lower())
        for pkg in RE_ADOC_PACKAGE.findall(line):
            keys.add("pkg:" + pkg.strip("/"))
        for name, _text in RE_ADOC_ATTR_LINK.findall(line):
            if name not in DEFAULT_ATTRS:
                keys.add("unresolved:{" + name + "}")
    return keys


def analyze_adoc(entry_dir: Path) -> dict:
    attrs = load_attrs(entry_dir / "_index.adoc")
    lines = expand_adoc(entry_dir / "_index.adoc", entry_dir, attrs, set())
    headings: Counter = Counter()
    paragraphs = 0
    list_items = 0
    in_code = False
    in_para = False
    in_front = False
    in_list = False
    for idx, raw in enumerate(lines):
        line = raw.strip()
        if idx == 0 and line == "---":
            in_front = True
            continue
        if in_front:
            if line == "---":
                in_front = False
            continue
        m = RE_ADOC_DELIM.match(line)
        if m:
            in_code = not in_code
            in_para = False
            in_list = False
            continue
        if in_code:
            continue
        if not line:
            in_para = False
            in_list = False
            continue
        if line in ("+", "'''") or line.startswith(("|", "!", "[", ":", "////")):
            in_para = False
            continue
        m = RE_ADOC_HEADING.match(line)
        if m:
            headings[len(m.group(1)) - 1] += 1
            in_para = False
            in_list = False
            continue
        if RE_ADOC_LIST.match(line):
            list_items += 1
            in_para = False
            in_list = True
            continue
        if RE_ONLY_LINK_ADOC.match(line):
            in_para = False
            continue
        if in_list and raw.startswith((" ", "\t")):
            continue
        in_list = False
        if not in_para:
            paragraphs += 1
            in_para = True
    headings.pop(0, None)
    return {
        "headings": headings,
        "paragraphs": paragraphs,
        "list_items": list_items,
        "links": adoc_links(lines),
    }


def analyze_md(path: Path) -> dict:
    lines = read_lines(path)
    headings: Counter = Counter()
    paragraphs = 0
    list_items = 0
    links: set[str] = set()
    in_code = False
    in_para = False
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if RE_CODE_FENCE_MD.match(stripped):
            in_code = not in_code
            in_para = False
            continue
        if in_code:
            continue
        if not stripped:
            in_para = False
            continue
        m = RE_MD_HEADING.match(stripped)
        if m:
            headings[len(m.group(1)) - 1] += 1
            in_para = False
            continue
        if RE_META.match(stripped):
            continue
        for target in RE_MD_LINK.findall(stripped):
            links.add(norm_target(target))
        for target in RE_MD_AUTOLINK.findall(stripped):
            links.add(norm_target(target))
        if RE_MD_LIST.match(stripped):
            list_items += 1
            in_para = False
            continue
        if RE_ONLY_LINK_MD.match(stripped):
            in_para = False
            continue
        if not in_para:
            paragraphs += 1
            in_para = True
    headings.pop(0, None)
    return {"headings": headings, "paragraphs": paragraphs, "list_items": list_items, "links": links}


def load_allowlist() -> set[str]:
    path = Path(__file__).resolve().parent / "structure_allowlist.txt"
    if not path.exists():
        return set()
    entries: set[str] = set()
    for line in read_lines(path):
        line = line.strip()
        if line and not line.startswith("#"):
            entries.add(line)
    return entries


def derive_en_dir(zh_path: Path) -> Path:
    text = zh_path.read_text(encoding="utf-8")
    m = re.search(r"- 原文：\[[^\]]*\]\((https://www\.freebsd\.org/status/([^/]+)/)", text)
    if not m:
        raise SystemExit("无法从文件头推导上游目录，请显式传入 adoc 目录")
    return zh_path.parent.parent / "en" / m.group(2)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    zh_path = Path(sys.argv[1])
    en_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else derive_en_dir(zh_path)
    if not zh_path.exists() or not en_dir.exists():
        print(f"错误：文件或目录不存在（zh={zh_path}, en={en_dir}）", file=sys.stderr)
        return 2

    zh = analyze_md(zh_path)
    en = analyze_adoc(en_dir)

    # AGENTS.md 要求统一保留 `## 引言`，上游 adoc 的引言不成节，故中文侧减 1 后比对
    md_text = zh_path.read_text(encoding="utf-8")
    if re.search(r"^## 引言\s*$", md_text, re.M) and zh["headings"].get(1, 0) > 0:
        zh["headings"][1] -= 1

    ok = True
    print(f"== 结构比对：{zh_path} vs {en_dir} ==")
    for depth, label in ((1, "二级标题"), (2, "三级标题"), (3, "四级标题"), (4, "五级标题")):
        a, b = en["headings"].get(depth, 0), zh["headings"].get(depth, 0)
        match = a == b
        ok &= match
        print(f"  [{'一致' if match else '偏差'}] {label}: 上游 {a} / 中文 {b}")
    for dim, label in (("paragraphs", "正文段落"), ("list_items", "列表项")):
        a, b = en[dim], zh[dim]
        if dim == "paragraphs":
            tolerance = max(2, round(a * 0.03))
            match = abs(a - b) <= tolerance
            note = f"（容差 ±{tolerance}，允许中文为可读性拆分长段）"
        else:
            match = a == b
            note = ""
        ok &= match
        print(f"  [{'一致' if match else '偏差'}] {label}: 上游 {a} / 中文 {b}{note}")

    allowlist = load_allowlist()
    missing = sorted(
        k for k in zh["links"]
        if k not in en["links"]
        and not k.startswith("unresolved:")
        and k not in allowlist
        and not any(adoc_key.startswith(k + "/") for adoc_key in en["links"])
    )
    excused = sorted(k for k in zh["links"] if k in allowlist)
    unresolved = sorted(k for k in en["links"] if k.startswith("unresolved:"))
    print(f"  [{'一致' if not missing else '偏差'}] 链接目标: 中文 {len(zh['links'])} 个，缺失对应 {len(missing)} 个")
    for key in missing[:20]:
        print(f"      - {key}")
    if excused:
        print(f"  [提示] 已登记例外 {len(excused)} 个（见 tools/structure_allowlist.txt）")
    if unresolved:
        print(f"  [提示] 上游含未解析属性链接 {len(unresolved)} 个（不计入偏差）")
    ok &= not missing
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
