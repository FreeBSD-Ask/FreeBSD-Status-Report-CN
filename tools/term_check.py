#!/usr/bin/env python3
"""按 tools/glossary.yml 检查中文译文的术语一致性。

检查两类问题：
  1. wrong 变体命中（level: forbid 失败退出；level: warn 仅提示）；
  2. man 页引用格式（man: true 的术语在正文须写作 **term**，标题与
     链接文本内除外，代码块内除外）。

用法：
    python tools/term_check.py <文件.md> [更多文件.md ...]

存在 forbid 级命中时以非零退出码结束。
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

GLOSSARY = Path(__file__).resolve().parent / "glossary.yml"

RE_FENCE = re.compile(r"^```")
RE_HEADING = re.compile(r"^#{1,6}\s")


@dataclass
class Term:
    term: str
    keep: bool = False
    man: bool = False
    level: str = "forbid"
    wrong: list[str] = field(default_factory=list)
    note: str = ""


def parse_glossary(path: Path) -> list[Term]:
    """解析 glossary.yml 的受控子集（缩进规整，无嵌套映射）。"""
    terms: list[Term] = []
    current: Term | None = None
    in_wrong = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        stripped = line.strip()
        if stripped.startswith("- term:"):
            if current:
                terms.append(current)
            in_wrong = False
            current = Term(term=stripped.split(":", 1)[1].strip())
        elif current is None:
            continue
        elif stripped.startswith("- ") and in_wrong:
            current.wrong.append(stripped[2:].strip())
        elif stripped.startswith("keep:"):
            in_wrong = False
            current.keep = stripped.split(":", 1)[1].strip() == "true"
        elif stripped.startswith("man:"):
            in_wrong = False
            current.man = stripped.split(":", 1)[1].strip() == "true"
        elif stripped.startswith("level:"):
            in_wrong = False
            current.level = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("note:"):
            in_wrong = False
            current.note = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("wrong:"):
            in_wrong = True
    if current:
        terms.append(current)
    return terms


def check_man_format(path: Path, lines: list[str], term: str) -> list[tuple[int, str]]:
    """正文出现 man 引用但未加粗（且不在链接文本内）→ 违规。"""
    hits: list[tuple[int, str]] = []
    pattern = re.compile(r"\*\*" + re.escape(term) + r"\*\*")
    bare = re.compile(r"(?<!\*)\b" + re.escape(term) + r"\b(?!\*)")
    for lineno, line in enumerate(lines, start=1):
        if RE_HEADING.match(line) or RE_FENCE.match(line):
            continue
        if pattern.search(line):
            continue
        m = bare.search(line)
        if not m:
            continue
        # 位于链接文本 [term](...) 或行间代码内则豁免
        prefix = line[: m.start()]
        if prefix.rstrip().endswith("["):
            continue
        if line[max(0, m.start() - 1): m.end() + 1].count("`"):
            continue
        hits.append((lineno, line.strip()))
    return hits


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    terms = parse_glossary(GLOSSARY)
    if not terms:
        print("错误：glossary.yml 解析结果为空", file=sys.stderr)
        return 2

    forbid_hits = 0
    warn_hits = 0
    for arg in sys.argv[1:]:
        path = Path(arg)
        lines = path.read_text(encoding="utf-8").splitlines()
        # 剔除代码块内容后按行扫描 wrong 变体
        in_code = False
        for lineno, line in enumerate(lines, start=1):
            if RE_FENCE.match(line.strip()):
                in_code = not in_code
                continue
            if in_code:
                continue
            for t in terms:
                for wrong in t.wrong:
                    if wrong in line:
                        where = f"{path}:{lineno}"
                        if t.level == "forbid":
                            forbid_hits += 1
                            print(f"{where}: [forbid] “{wrong}”应为“{t.term}”")
                        else:
                            warn_hits += 1
                            print(f"{where}: [warn] “{wrong}”（应为“{t.term}”）")
        for t in terms:
            if t.man:
                for lineno, text in check_man_format(path, lines, t.term):
                    forbid_hits += 1
                    print(f"{path}:{lineno}: [forbid] man 页引用未加粗：{text}")
    if forbid_hits or warn_hits:
        print(f"共 forbid {forbid_hits} 处，warn {warn_hits} 处", file=sys.stderr)
        return 1 if forbid_hits else 0
    print("术语检查通过：无命中")
    return 0


if __name__ == "__main__":
    sys.exit(main())
