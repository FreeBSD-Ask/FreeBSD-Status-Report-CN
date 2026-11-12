#!/usr/bin/env python3
"""质量工具自测：用最小样例验证 tools/ 下的检查器确实能发现问题。

每个用例在临时目录生成一对最小的 adoc / Markdown 文件，运行对应工具，
断言退出码与关键提示。任何用例不符合预期即以非零状态退出。

用法：
    python tools/selftest.py
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

INDEX = """= Test Report
:reports-path: content/en/status/report-test-case
:author: Test Person <author@example.org>

== Projects

include::entry.adoc[]
"""

ENTRY = """=== Test Entry

Contact: Test Person <test@example.org>

Version 1.2.3 was released on 2026-07-20, covering 42% of cases (D12345, commit abc1234).

See link:https://example.org/doc[the document] and package:devel/example[] and man:example[8].
Prepared by {author}.

Inline tokens: `--flag`.
"""

ZH = """# 测试报告

- 原文：[Test](https://www.freebsd.org/status/report-test-case/)
- 版本：2026 年 7 月 20 日
- 最后作者：Test Person

## 项目

### 测试条目

**联系方式**：Test Person <[test@example.org](mailto:test@example.org)>

2026 年 7 月 20 日发布 1.2.3 版，覆盖 42% 的情形（D12345，提交 abc1234）。

参见[文档](https://example.org/doc)、[devel/example](https://cgit.freebsd.org/ports/tree/devel/example/) 与 **example(8)**。
由 Test Person <[author@example.org](mailto:author@example.org)> 编写。

行间 token：`--flag`。
"""


def write_case(base: Path, zh_text: str, index_text: str = INDEX, entry_text: str = ENTRY) -> Path:
    en = base / "en"
    en.mkdir(parents=True)
    (en / "_index.adoc").write_text(index_text, encoding="utf-8", newline="\n")
    (en / "entry.adoc").write_text(entry_text, encoding="utf-8", newline="\n")
    zh = base / "zh.md"
    zh.write_text(zh_text, encoding="utf-8", newline="\n")
    return zh


def run(tool: str, zh: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(TOOLS / tool), str(zh), str(zh.parent / "en")],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def main() -> int:
    cases = [
        ("clean", ZH, "object_check.py", 0, ""),
        ("clean-structure", ZH, "structure_check.py", 0, ""),
        ("missing-link", ZH.replace("[devel/example](https://cgit.freebsd.org/ports/tree/devel/example/)", "devel/example"), "object_check.py", 1, "链接"),
        ("missing-email", ZH.replace("<[test@example.org](mailto:test@example.org)>", "Test Person"), "object_check.py", 1, "邮箱"),
        ("missing-attr-email", ZH.replace("由 Test Person <[author@example.org](mailto:author@example.org)> 编写。", "由 Test Person 编写。"), "object_check.py", 1, "邮箱"),
        ("missing-man", ZH.replace("**example(8)**", "手册页"), "object_check.py", 1, "man"),
        ("missing-number", ZH.replace("1.2.3 版", "1.2 版"), "object_check.py", 1, "数字"),
        ("missing-code", ZH.replace("`--flag`", "命令行标志"), "object_check.py", 1, "行间代码"),
        ("missing-include", ZH, "structure_check.py", 1, "无法解析 include"),
    ]

    failed = 0
    for name, zh_text, tool, expect_code, expect_text in cases:
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            index = INDEX
            if name == "missing-include":
                index = INDEX.replace("include::entry.adoc[]", "include::absent.adoc[]")
            zh = write_case(base, zh_text, index_text=index)
            proc = run(tool, zh)
            ok = proc.returncode == expect_code and expect_text in (proc.stdout + proc.stderr)
            print(f"[{'PASS' if ok else 'FAIL'}] {name}（{tool}，退出码 {proc.returncode}）")
            if not ok:
                failed += 1
                print((proc.stdout + proc.stderr)[-1200:])

    print(f"\n{len(cases) - failed}/{len(cases)} 用例通过")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
