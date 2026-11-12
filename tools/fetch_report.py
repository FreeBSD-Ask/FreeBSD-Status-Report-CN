#!/usr/bin/env python3
"""从 GitHub freebsd/freebsd-doc main 分支拉取指定状态报告的 ADOC 原文快照。

用法：
    python tools/fetch_report.py [--report report-2026-07-2026-09]
                                 [--out en/report-2026-07-2026-09]
                                 [--ref main]
                                 [--repo freebsd/freebsd-doc]

通过 GitHub Contents API 列出 website/content/en/status/<report>/ 下全部
.adoc 文件并下载到 --out 目录。校验下载文件数与清单一致，失败即非零退出。
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

API_BASE = "https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"
UA = "FreeBSD-Status-Report-CN-tools"


def fetch_json(url: str) -> object:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", default="report-2026-07-2026-09")
    parser.add_argument("--out", default="en/report-2026-07-2026-09")
    parser.add_argument("--ref", default="main")
    parser.add_argument("--repo", default="freebsd/freebsd-doc")
    args = parser.parse_args()

    remote_path = f"website/content/en/status/{args.report}"
    url = API_BASE.format(repo=args.repo, path=remote_path, ref=args.ref)
    try:
        listing = fetch_json(url)
    except Exception as exc:  # noqa: BLE001
        print(f"错误：列出目录失败（{url}）：{exc}", file=sys.stderr)
        return 1
    if not isinstance(listing, list):
        print(f"错误：API 返回非目录内容", file=sys.stderr)
        return 1

    adocs = [item for item in listing if item.get("name", "").endswith(".adoc")]
    if not adocs:
        print("错误：目录内无 .adoc 文件", file=sys.stderr)
        return 1

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    failures = 0
    for item in adocs:
        name = item["name"]
        try:
            data = fetch_bytes(item["download_url"])
        except Exception as exc:  # noqa: BLE001
            print(f"错误：下载 {name} 失败：{exc}", file=sys.stderr)
            failures += 1
            continue
        (out_dir / name).write_bytes(data)
        print(f"已下载 {name}（{len(data)} 字节）")

    expected = len(adocs)
    got = sum(1 for item in adocs if (out_dir / item["name"]).exists())
    if failures or got != expected:
        print(f"校验失败：预期 {expected} 个文件，实际成功 {got} 个", file=sys.stderr)
        return 1
    print(f"完成：{expected} 个 .adoc 已保存至 {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
