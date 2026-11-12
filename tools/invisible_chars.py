#!/usr/bin/env python3
"""检测中文 Markdown 文件中的 AI 不可见字符。

判定逻辑与 AGENTS.md“AI 不可见字符”一节一致：
零宽字符、BOM、双向标记、Tag 块、变体选择符、软连字符、
不换行空格等；排除 Markdown 嵌套列表的合法缩进 Tab（U+0009）。

用法：
    python tools/invisible_chars.py [目录]

默认扫描当前目录下全部 .md 文件，排除 en/、.github/、node_modules/、
script/、.trae/。发现可疑字符时打印 文件:行:列 与码点说明，
并以非零退出码结束。
"""

from __future__ import annotations

import sys
import unicodedata
from pathlib import Path

# 合法码点：Tab（嵌套列表缩进）、换行、回车
LEGAL = {0x0009, 0x000A, 0x000D}

# 可疑码点区间（闭区间）
SUSPECT_RANGES: tuple[tuple[int, int, str], ...] = (
    (0x00AD, 0x00AD, "软连字符"),
    (0x00A0, 0x00A0, "不换行空格"),
    (0x180E, 0x180E, "蒙古语元音分隔符"),
    (0x200B, 0x200D, "零宽字符"),
    (0x200E, 0x200F, "双向标记"),
    (0x202A, 0x202E, "双向格式化"),
    (0x2060, 0x2064, "不可见连接符"),
    (0x2066, 0x2069, "双向隔离符"),
    (0xFE00, 0xFE0F, "变体选择符"),
    (0xFEFF, 0xFEFF, "BOM / 零宽不换行空格"),
    (0xE0000, 0xE007F, "Tag 块（疑似 LLM 水印）"),
    (0xE0100, 0xE01EF, "变体选择符补充区"),
)

# 排除的目录（相对扫描根）
EXCLUDE_DIRS = {"en", ".github", "node_modules", "script", ".trae", ".git"}


def classify(cp: int) -> str | None:
    if cp in LEGAL:
        return None
    for lo, hi, label in SUSPECT_RANGES:
        if lo <= cp <= hi:
            return label
    # 其余 C0/C1 控制字符同样可疑
    if cp < 0x20 or 0x7F <= cp <= 0x9F:
        return "控制字符"
    return None


def scan_file(path: Path) -> list[tuple[int, int, int, str]]:
    findings: list[tuple[int, int, int, str]] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for lineno, line in enumerate(text.splitlines(), start=1):
        for colno, ch in enumerate(line, start=1):
            label = classify(ord(ch))
            if label:
                findings.append((lineno, colno, ord(ch), label))
    return findings


def iter_md_files(root: Path) -> list[Path]:
    files = []
    for p in sorted(root.rglob("*.md")):
        rel_parts = p.relative_to(root).parts
        if any(part in EXCLUDE_DIRS for part in rel_parts[:-1]):
            continue
        files.append(p)
    return files


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not root.exists():
        print(f"错误：目录不存在：{root}", file=sys.stderr)
        return 2
    total = 0
    for path in iter_md_files(root):
        for lineno, colno, cp, label in scan_file(path):
            total += 1
            name = unicodedata.name(chr(cp), "UNKNOWN")
            print(f"{path}:{lineno}:{colno}: U+{cp:04X} {label}（{name}）")
    if total:
        print(f"共发现 {total} 处不可见/可疑字符", file=sys.stderr)
        return 1
    print("未发现不可见/可疑字符")
    return 0


if __name__ == "__main__":
    sys.exit(main())
