# 贡献指南

本仓库是 FreeBSD 季度状态报告的中文译本，基于 GitBook 组织与发布。所有译文以 FreeBSD 官方英文版为准，原文来源与许可见 [README](README.md)。

本文件面向人类贡献者，说明如何准备环境、翻译、校验与提交。译文规范、术语表与排版细则的权威来源是 [AGENTS.md](AGENTS.md)：两者冲突时以 [AGENTS.md](AGENTS.md) 为准，并请在 Issue 中指出冲突。

## 可以贡献什么

- 新增报告的翻译：上游发布新季度报告后补齐对应章节。
- 既有译文的校对：修正误译、漏译、欧化汉语与格式偏差。
- 工程与文档改进：CI、校验脚本、索引与说明文件。

不接受改写原文事实、增补原文没有的信息，以及为求通顺而调整数字、版本号、日期与专有名词的改动。

## 环境准备

需要 Git、Node.js 22 或更高版本、Python 3.10 或更高版本。可选安装 GitHub CLI（`gh`）用于发起拉取请求。

```sh
git clone https://github.com/<你的用户名>/FreeBSD-Status-Report-CN.git
cd FreeBSD-Status-Report-CN
git remote add upstream https://github.com/FreeBSD-Ask/FreeBSD-Status-Report-CN.git
npm install -g markdownlint-cli2@0.24.1 autocorrect-node
```

校验脚本只依赖 Python 标准库，无需 `pip install`。

## 仓库结构与数据流

- `SUMMARY.md` 是全书目录的唯一数据源，GitBook 据此生成侧边栏；第一行 `# Table of contents` 不得改动。
- `mu-lu.md` 由 CI 从 `SUMMARY.md` 自动生成，不要手工编辑。
- `CHANGELOG.md` 记录校对与同步进度，新条目追加在文件顶部。
- `en/` 存放从上游拉取的英文原文快照，`script/` 存放一次性临时脚本，两者均不纳入版本控制。
- `tools/` 存放可复用的质量校验脚本与术语表，属于仓库资产，请勿删除。

各年份目录下按季度或月份分文件：`2001/1-3.md`、`2010/Q2.md`、`2026/2026-Q3.md`。文件名不得包含空格、中文或英文冒号。

## 获取英文原文

上游报告位于 `freebsd/freebsd-doc` 仓库的 `website/content/en/status/` 目录，2021 年起为 AsciiDoc 格式，2020 年及以前为 XML 格式。

```sh
python tools/fetch_report.py --report report-2026-07-2026-09
```

脚本按 GitHub Contents API 列出目录并下载全部 `.adoc` 文件至 `en/report-2026-07-2026-09/`，文件数与清单不一致时以非零状态退出。报告目录通常含 `_index.adoc`（总装）、`intro.adoc`（引言）与各条目文件；条目数应以 `_index.adoc` 的 `include::` 数量与引言自述数字双向核对。

若 `en/` 中缺少某期报告，可用相应页面（形如 `https://www.freebsd.org/status/report-YYYY-MM-YYYY-MM/`）核对链接与页脚，但正文仍以 `en/` 中的原文快照为准。

## 元信息与命名

每份译文文件以一级标题开头，随后是三行元信息：

```markdown
# FreeBSD 2026 年第三季度状态报告

- 原文：[FreeBSD Status Report Third Quarter 2026](https://www.freebsd.org/status/report-2026-07-2026-09/)
- 版本：2026 年 11 月 1 日
- 最后作者：Lorenzo Salvadore
```

- `原文` 统一写作“原文”，链接使用上游页面地址；2021 年及以后以 `/` 结尾，2020 年及以前保留 `.html`。
- `版本` 取页面页脚 `Last modified on : <日期> by <作者>` 中的日期，转换为 `YYYY 年 M 月 D 日`；页脚缺失时回退到上游报告目录最后一次提交的日期与提交者。
- `最后作者` 取同一处署名；署名为团队时保留团队名。
- 一级标题由 CI 依据 `SUMMARY.md` 同步，不要手工修改。

## 翻译流程

1. 通读整节英文，登记术语与专名，再动笔；不要逐句硬译后拼装。
2. 一次性完成整节初译，不在中途反复回改。
3. 按“三审三校”逐轮处理：一审准确性、二审汉语表达、三审术语一致性；一校事实核验、二校交叉复核、三校规范终校。每轮只看新问题，不复查上一轮已处理的结论。
4. 逐处修改，一次一处，禁止批量替换与脚本改写译文；每处修改要能说明原文依据与规则依据。
5. 修改后回读上下文，确认未引入新错误。

译文须同时满足准确、完整、清晰、流畅、明白五项要求，篇幅较长的句子按语义拆分，单句“的”不超过三个，“被”字句、“进行/作出/加以”与“使得”按密度阈值控制。具体清单与阈值见 [AGENTS.md](AGENTS.md)。

## 本地校验

提交前请在仓库根目录依次执行以下命令，全部通过再推送。

```sh
markdownlint-cli2 "**/*.md" "!en/**" "!.github/**" "!node_modules/**" "!script/**" "!.trae/**" --config .github/.markdownlint.json
autocorrect --lint 20*/*.md *.md
python tools/invisible_chars.py .
python tools/structure_check.py 2026/2026-Q3.md
python tools/term_check.py 2026/2026-Q3.md
python tools/text_metrics.py 2026/2026-Q3.md
```

- markdownlint 须为 0 报错，报错逐处手工修正，不要用 `--fix` 批量接受。
- autocorrect 读取根目录 `.autocorrectrc`，规则与项目标点规范一致，出现命中须逐条判断，确属错误才改。
- `invisible_chars.py` 检测零宽字符、BOM、双向标记等不可见字符，合法的列表缩进 Tab 不报。
- `structure_check.py` 比对标题层级、段落数、列表项数与链接数；`term_check.py` 按 `tools/glossary.yml` 检查术语；`text_metrics.py` 统计句长与用词密度。三项均以非零状态表示未通过。

## 提交与拉取请求

1. 从 `main` 建立分支，分支名说明用途，例如 `update-2026-q3-report`、`fix-2015-q4-typo`。
2. 提交信息准确描述改动性质，例如 `新增 2026 Q3 状态报告译文`、`同步上游修订：2026 Q2`。一次提交只做一类改动，译文、工具、治理文件分别提交。
3. 推送到自己的仓库后，向 `FreeBSD-Ask/FreeBSD-Status-Report-CN` 的 `main` 分支发起拉取请求，并按模板填写自查清单。
4. 新报告需在 `SUMMARY.md` 对应年份小节按时间倒序插入条目，并在 `CHANGELOG.md` 顶部追加一行，日期格式为 `YYYY.M.D`。
5. CI 会在拉取请求与推送时执行 lint 与文档质量检查，任一失败即阻止合并；自动修复任务只在手动触发时运行，并会另开分支提交改动。

## 许可

译文遵循 [BSD 2-Clause 许可证](LICENSE)。上游状态报告允许在标注来源并给予署名后全文或部分转载；提交贡献即表示同意以同一许可证发布。
