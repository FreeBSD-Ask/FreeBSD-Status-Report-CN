#!/usr/bin/env python3
"""对象盘点：按“对象”而非“句子”比对译文与上游原文。

比对五类对象：
  1. 链接目标（非邮件）
  2. 邮箱地址
  3. man 页引用（name(section)）
  4. 行间代码 token 与代码块内的代码行
  5. 版本号、百分比、ISO 日期、提交哈希、评审编号（D####）

用法：
    python tools/object_check.py <中文.md> [上游adoc目录]

上游目录缺省时，从文件头 `- 原文：[...](https://www.freebsd.org/status/report-.../)` 推导。
任一对象类别存在“上游有、中文无”即以非零退出码结束。
"""

from __future__ import annotations

import importlib.util
import re
import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("structure_check", _HERE / "structure_check.py")
sc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sc)

RE_FENCE_ZH = re.compile(r"^```")
RE_INLINE_CODE_ZH = re.compile(r"`([^`\n]+)`")
RE_LINK_DEST = re.compile(r"\]\([^)]*\)")
RE_URL = re.compile(r"https?://[^\s)\]>]+")

RE_MAN = re.compile(r"\b[A-Za-z][A-Za-z0-9_.+-]*\(\d\)")
RE_ADOC_MAN_MACRO = re.compile(r"man:([A-Za-z0-9_.+-]+)\[(\d)\]")
RE_EMAIL = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")

RE_VERSION = re.compile(r"\b\d+\.\d+(?:\.\d+)+\b")
RE_PERCENT = re.compile(r"\b\d+(?:\.\d+)?%")
RE_ISO_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
RE_COMMIT = re.compile(r"\b(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b")
RE_REVIEW = re.compile(r"\bD\d{4,6}\b")

RE_BARE_COMMAND = re.compile(r"^[a-z][a-z0-9_-]*$")


def strip_noise(text: str) -> str:
    """去掉链接目标与裸 URL，保留可见文字。"""
    return RE_URL.sub(" ", RE_LINK_DEST.sub("]()", text))


def norm_code_token(token: str) -> str:
    token = token.strip().strip("+")
    return token.replace("\\{", "{").replace("\\}", "}").replace("\\_", "_")


def useful_code_token(token: str) -> bool:
    if len(token) < 2:
        return False
    # 裸命令按项目规范不加反引号；路径与 IP 按规范用加粗，均不参与代码 token 比对
    if RE_BARE_COMMAND.match(token):
        return False
    if token.startswith("/"):
        return False
    return True


def code_lines(text: str, fence_pattern: re.Pattern, is_adoc: bool) -> list[str]:
    out: list[str] = []
    in_code = False
    for raw in text.splitlines():
        line = raw.rstrip()
        if is_adoc:
            if sc.RE_ADOC_DELIM.match(line.strip()):
                in_code = not in_code
                continue
        elif fence_pattern.match(line.strip()):
            in_code = not in_code
            continue
        if not in_code:
            continue
        stripped = line.strip()
        if not stripped:
            continue
        # 注释需要翻译，不参与逐字比对
        if stripped.startswith(("#", "//")):
            continue
        out.append(stripped)
    return out


def normalize_zh_dates(text: str) -> str:
    """把“YYYY 年 M 月 D 日”统一为 ISO 形式，便于与上游日期比对。"""
    return re.sub(
        r"(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日",
        lambda m: f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}",
        text,
    )


def numbers(text: str) -> Counter:
    return Counter(
        RE_VERSION.findall(text)
        + RE_PERCENT.findall(text)
        + RE_ISO_DATE.findall(text)
        + RE_COMMIT.findall(text)
        + RE_REVIEW.findall(text)
    )


def zh_objects(text: str) -> dict:
    emails = set(m.lower() for m in RE_EMAIL.findall(text))
    visible = strip_noise(text)
    inline_code: Counter = Counter()
    for line in text.splitlines():
        for token in RE_INLINE_CODE_ZH.findall(line):
            token = norm_code_token(token)
            if useful_code_token(token):
                inline_code[token] += 1
    return {
        "emails": emails,
        "man": set(RE_MAN.findall(visible)),
        "inline_code": inline_code,
        "code_lines": set(code_lines(text, RE_FENCE_ZH, is_adoc=False)),
        "numbers": numbers(normalize_zh_dates(visible)),
    }


def en_objects(entry_dir: Path) -> dict:
    attrs = sc.load_attrs(entry_dir / "_index.adoc")
    lines = sc.expand_adoc(entry_dir / "_index.adoc", entry_dir, attrs, set())
    raw_text = "\n".join(lines)
    emails = set(m.lower() for m in RE_EMAIL.findall(raw_text))
    converted = RE_ADOC_MAN_MACRO.sub(r"\1(\2)", raw_text)
    visible = strip_noise(converted)
    inline_code: Counter = Counter()
    in_code = False
    for line in converted.splitlines():
        if sc.RE_ADOC_DELIM.match(line.strip()):
            in_code = not in_code
            continue
        if in_code:
            continue
        for token in RE_INLINE_CODE_ZH.findall(line):
            token = norm_code_token(token)
            if useful_code_token(token):
                inline_code[token] += 1
    return {
        "emails": emails,
        "man": set(RE_MAN.findall(visible)),
        "inline_code": inline_code,
        "code_lines": set(code_lines(raw_text, RE_FENCE_ZH, is_adoc=True)),
        "numbers": numbers(visible),
    }


def missing_counter(en: Counter, zh: Counter) -> list[str]:
    out: list[str] = []
    for key, count in en.items():
        gap = count - zh.get(key, 0)
        if gap > 0:
            out.extend([key] * gap)
    return sorted(out)


def missing_set(en: set, zh: set) -> list[str]:
    return sorted(en - zh)


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

    zh = zh_objects(zh_path.read_text(encoding="utf-8"))
    en = en_objects(en_dir)

    ok = True
    print(f"== 对象盘点：{zh_path} vs {en_dir} ==")

    zh_doc = sc.analyze_md(zh_path)
    en_doc = sc.analyze_adoc(en_dir)
    allow = sc.load_allowlist()
    empty = ("path:", "pkg:", "url:", "frag:")
    zh_links = {k for k in zh_doc["links"] if k not in empty and not k.startswith("mail:")}
    en_links = {
        k for k in en_doc["links"]
        if k not in empty and not k.startswith(("mail:", "unresolved:")) and k not in allow
    }
    miss_links = sorted(en_links - zh_links)
    print(f"  [{'通过' if not miss_links else '失败'}] 链接：上游 {len(en_links)} 个唯一目标，中文缺 {len(miss_links)} 个")
    for item in miss_links[:20]:
        print(f"      - {item}")
    ok &= not miss_links

    for label, key, unit in (("邮箱", "emails", "个"), ("man 页引用", "man", "处")):
        miss = missing_set(en[key], zh[key])
        print(f"  [{'通过' if not miss else '失败'}] {label}：上游 {len(en[key])} {unit}，中文缺 {len(miss)} {unit}")
        for item in miss[:20]:
            print(f"      - {item}")
        ok &= not miss

    miss_code = missing_counter(en["inline_code"], zh["inline_code"])
    print(f"  [{'通过' if not miss_code else '失败'}] 行间代码：上游 {sum(en['inline_code'].values())} 处，中文缺 {len(miss_code)} 处")
    for item in miss_code[:20]:
        print(f"      - {item}")
    ok &= not miss_code

    miss_lines = missing_set(en["code_lines"], zh["code_lines"])
    print(f"  [{'通过' if not miss_lines else '失败'}] 代码行：上游 {len(en['code_lines'])} 行，中文缺 {len(miss_lines)} 行")
    for item in miss_lines[:20]:
        print(f"      - {item}")
    ok &= not miss_lines

    miss_num = missing_counter(en["numbers"], zh["numbers"])
    print(f"  [{'通过' if not miss_num else '失败'}] 数字对象：上游 {sum(en['numbers'].values())} 处，中文缺 {len(miss_num)} 处")
    for item in miss_num[:30]:
        print(f"      - {item}")
    ok &= not miss_num

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
