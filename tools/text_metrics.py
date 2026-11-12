#!/usr/bin/env python3
"""统计中文译文的文本质量指标（依据 .trae 规格“量化验收指标”）。

指标与阈值：
  - 平均句长 ≤ 45 字
  - 单句超过 80 字占比 ≤ 2%（含 ≥3 个顿号的技术枚举句除外）
  - 单句“的”数量 ≤ 3
  - “被”字句密度 ≤ 3 处/千字
  - “进行/作出/加以”密度 ≤ 1 处/千字
  - “使得”密度 ≤ 1 处/千字

统计范围：正文（剔除代码块、行间代码、链接 URL、标题、
链接区块 URL、“原文/版本/最后作者”元信息行）。

用法：
    python tools/text_metrics.py <文件.md> [更多文件.md ...]

任一指标超阈值时以非零退出码结束，并列出违规句供人工判定。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LIMIT_AVG_SENT = 45
LIMIT_LONG_RATIO = 0.02
LIMIT_LONG_LEN = 80
LIMIT_DE = 3
LIMIT_BEI_PER_K = 3.0
LIMIT_VERB_PER_K = 1.0  # 进行 / 作出 / 加以
LIMIT_SHIDe_PER_K = 1.0  # 使得

RE_FENCE = re.compile(r"^```")
RE_HEADING = re.compile(r"^#{1,6}\s")
RE_LIST = re.compile(r"^\s*(?:[-*+]|\d+[.、])\s")
RE_LINK_BLOCK_URL = re.compile(r"^(?:\[.*\]\([^)]*\)|<https?://\S+>|\*\*链接\*\*：.*)$")
RE_META = re.compile(r"^-\s*(?:原文|版本|最后作者)：")
RE_INLINE_CODE = re.compile(r"`[^`]*`")
RE_MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
RE_BOLD = re.compile(r"\*\*([^*]*)\*\*")
RE_MAILTO = re.compile(r"<[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+>")


def extract_prose(text: str) -> str:
    """提取正文：剔除代码块、标题与元信息；列表项保留其文字部分一并统计。"""
    lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if RE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if RE_HEADING.match(line) or RE_META.match(line):
            continue
        # 列表项去掉标记后保留文字，避免列表内的长句与措辞逃过统计
        m = RE_LIST.match(line)
        if m:
            line = line[m.end():]
        # 链接区块：只保留加粗标签行中的中文（如 **链接**：），剔除 URL
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith(")"):
            continue
        if stripped.startswith("<"):
            continue
        lines.append(line)
    return "\n".join(lines)


def clean_segment(seg: str) -> str:
    seg = RE_INLINE_CODE.sub("", seg)
    seg = RE_MD_LINK.sub(r"\1", seg)
    seg = RE_BOLD.sub(r"\1", seg)
    seg = RE_MAILTO.sub("", seg)
    seg = re.sub(r"https?://\S+", "", seg)
    return seg


def split_sentences(prose: str) -> list[str]:
    sentences: list[str] = []
    for para in prose.split("\n"):
        seg = clean_segment(para)
        if not seg.strip():
            continue
        parts = re.split(r"(?<=[。！？；])", seg)
        for part in parts:
            part = part.strip()
            if part:
                sentences.append(part)
    return sentences


def char_len(s: str) -> int:
    return len(re.sub(r"\s", "", s))


def is_technical_enum(s: str) -> bool:
    """含 3 个及以上顿号的句子视为技术枚举。"""
    return s.count("、") >= 3


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    failed = False
    for arg in sys.argv[1:]:
        path = Path(arg)
        text = path.read_text(encoding="utf-8")
        prose = extract_prose(text)
        sentences = split_sentences(prose)
        total_chars = sum(char_len(s) for s in sentences)
        if not sentences or not total_chars:
            print(f"{path}: 未提取到正文", file=sys.stderr)
            failed = True
            continue

        lengths = [char_len(s) for s in sentences]
        avg = sum(lengths) / len(lengths)
        longs = [
            s for s in sentences
            if char_len(s) > LIMIT_LONG_LEN and not is_technical_enum(s)
        ]
        long_ratio = len(longs) / len(sentences)
        de_violations = [
            (s, s.count("的")) for s in sentences if s.count("的") > LIMIT_DE
        ]
        bei_per_k = prose.count("被") / total_chars * 1000
        verb_per_k = (
            sum(prose.count(w) for w in ("进行", "作出", "加以")) / total_chars * 1000
        )
        shide_per_k = prose.count("使得") / total_chars * 1000

        checks = [
            ("平均句长", avg, LIMIT_AVG_SENT, f"{avg:.1f} ≤ {LIMIT_AVG_SENT}"),
            ("长句占比", long_ratio, LIMIT_LONG_RATIO, f"{long_ratio:.2%} ≤ {LIMIT_LONG_RATIO:.0%}"),
            ("“被”密度/千字", bei_per_k, LIMIT_BEI_PER_K, f"{bei_per_k:.2f} ≤ {LIMIT_BEI_PER_K}"),
            ("“进行/作出/加以”密度/千字", verb_per_k, LIMIT_VERB_PER_K, f"{verb_per_k:.2f} ≤ {LIMIT_VERB_PER_K}"),
            ("“使得”密度/千字", shide_per_k, LIMIT_SHIDe_PER_K, f"{shide_per_k:.2f} ≤ {LIMIT_SHIDe_PER_K}"),
        ]

        print(f"== {path} ==")
        print(f"  句数 {len(sentences)}，字数 {total_chars}")
        for name, value, limit, desc in checks:
            ok = value <= limit
            failed |= not ok
            print(f"  [{'通过' if ok else '超限'}] {name}: {desc}")
        if longs:
            over = long_ratio > LIMIT_LONG_RATIO
            failed |= over
            label = "超限" if over else "提示"
            print(f"  [{label}] 单句超过 {LIMIT_LONG_LEN} 字（{len(longs)} 句，占比未超阈值时仅供参考）：")
            for s in longs:
                print(f"    - （{char_len(s)} 字）{s}")
        if de_violations:
            failed = True
            print(f"  [超限] 单句“的”超过 {LIMIT_DE} 个（{len(de_violations)} 句）：")
            for s, n in de_violations:
                print(f"    - （{n} 个）{s}")
        print()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
