# FreeBSD 2022 年第二季度状态报告

- 原文：[FreeBSD Quarterly Status Report Second Quarter 2022](https://www.freebsd.org/status/report-2022-04-2022-06/)

这是 2022 年第二季度的季度报告，共包含 26 份报告。

本季度，季度团队成功地更快地发布了报告，并且希望错误不多。不过，如果你发现任何问题，请及时反馈，以便我们进行修正，同时在我们的工具中增加了一些自动检查，从而在后续的发布过程中尽可能保持高效。

我们还想提醒各位，如果因任何原因你需要更多时间提交季度报告，团队会等待你，但请提前告知，以便我们知晓仍有报告未提交。

非常感谢所有选择通过季度报告与 FreeBSD 社区分享自己工作的同仁。

Lorenzo Salvadore

代表季度报告团队

## FreeBSD 团队报告

以下内容来自各官方及半官方团队，可在 [管理页面](https://www.freebsd.org/administration/) 查阅。

### FreeBSD 核心团队

联系人：FreeBSD 核心团队 [core@FreeBSD.org](mailto:core@FreeBSD.org)

FreeBSD 核心团队是 FreeBSD 的管理机构。

第十二届 FreeBSD 核心团队由活跃开发者选举产生。第十二届 FreeBSD 核心团队成员如下：

- Baptiste Daroussin (bapt, 连任)
- Benedict Reuschling (bcr)
- Ed Maste (emaste, 连任)
- Greg Lehey (grog)
- John Baldwin (jhb)
- 許立文 (lwhsu)
- Emmanuel Vadot (manu)
- Tobias C. Berner (tcberner)
- Mateusz Piotrowski (0mp)

6 月 10 日，第十一届 FreeBSD 离任核心团队与第十二届 FreeBSD 新核心团队进行了交接会议，于 [6 月 18 日公布](https://lists.freebsd.org/archives/freebsd-announce/2022-June/000034.html)新核心团队。

现任核心团队秘书 Muhammad Moinur Rahman (bofh) 将在新秘书任命并完成任务交接后卸任。

本季度，Kornel Dulęba (kd) 和 Dmitry Salychev (dsl) 的 src 提交权限已获批准。

### FreeBSD 基金会

链接：

[FreeBSD 基金会](https://www.freebsdfoundation.org/)

[技术路线图](https://freebsdfoundation.org/blog/technology-roadmap/)

[捐赠](https://www.FreeBSDFoundation.org/donate/)

[基金会合作计划](https://www.freebsdfoundation.org/FreeBSD-foundation-partnership-program/)

[FreeBSD 期刊](https://www.FreeBSDFoundation.org/journal/)

[基金会新闻与事件](https://www.FreeBSDFoundation.org/news-and-events/)

联系人：Deb Goodkin [deb@FreeBSDFoundation.org](mailto:deb@FreeBSDFoundation.org)

FreeBSD 基金会是一家 501(c)(3) 非盈利组织，致力于支持和推广 FreeBSD 项目及社区。个人和企业的捐赠用于资助软件开发项目、会议及开发者峰会，也用于提供 FreeBSD 基础设施硬件、改善安全、质量保证和发布工程工作，同时提供法律支持。

#### 筹款工作

感谢所有捐赠者的支持。基金会 100% 依赖捐赠，帮助 FreeBSD 项目持续发展。本年度目标筹款至少 1,400,000 美元，支出预算约 2,000,000 美元，目前已筹得不到 200,000 美元，因此筹款工作需加大力度。

基金会在五大领域支持 FreeBSD：

1. **软件开发**：六名软件开发人员实现新特性、支持一级平台、审核补丁、修复问题。
2. **FreeBSD 宣传**：在会议、线上/线下演讲、教程、指南等活动中推广 FreeBSD。
3. **硬件支持**：购买和维护 FreeBSD 基础设施。
4. **活动组织**：线上和线下活动，促进社区协作。
5. **法律支持**：提供法律援助，保护 FreeBSD 商标。

大额商业捐赠者可参与合作计划：[合作计划详情](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)

#### 改进操作系统

2022 年第二季度，由基金会赞助的提交记录：

- src 树：243 次提交，占总提交 10.6%
- ports 树：62 次提交，占总提交 0.7%
- doc 树：12 次提交，占总提交 4.5%

赞助工作示例：

- 更新基本系统中的 OpenSSH
- 支持 LLDB 多进程调试
- 改进无线状态
- makefs 的 ZFS 支持

##### 改进 FreeBSD Wireguard

改进 FreeBSD 内核模块 Wireguard 的支持，适配 OCF，增加新加密算法和 API。

##### FreeBSD 上的 OpenStack

目标是移植 OpenStack 组件，使 FreeBSD 可作为 OpenStack 主机。

##### Bhyve 问题支持

新合同让 John Baldwin 专注于 Bhyve 相关问题，尤其是安全问题。

##### 探索改进手册

赞助 Pau Amma 完成小型项目，探索如何改进 FreeBSD 手册，已发放问卷并将分享结果。

#### 持续集成与质量保证

基金会提供全职人员和资金，改进持续集成、自动化测试和整体质量保证工作。

#### FreeBSD 基础设施支持

基金会提供硬件及支持。例如，新上线澳大利亚镜像，修复两台 PowerPC 软件包构建器。

#### FreeBSD 宣传与教育

基金会通过会议、线上内容、视频教程、指南等方式推广 FreeBSD，帮助用户更易采用和贡献项目。

活动示例：

- 参加 All Things Open 会议（2022 年 10 月 30 日 - 11 月 2 日，Raleigh, NC）
- Scale 19x 工作坊（2022 年 7 月 28-30 日，洛杉矶）
- EuroBSDcon 2022 银牌赞助（9 月 15-18 日，维也纳）
- 组织 2022 年 6 月 FreeBSD 开发者峰会（视频在 [FreeBSD YouTube 频道](https://www.youtube.com/c/FreeBSDProject)）

教程和指南示例：

- [WiFi 与蓝牙网络基础](https://freebsdfoundation.org/freebsd-project/resources/networking-basics-wifi-and-bluetooth/)
- [FreeBSD 音频设置](https://freebsdfoundation.org/freebsd-project/resources/audio-on-freebsd/)
- [在 VirtualBox 上安装 FreeBSD（Mac/Windows）视频指南](https://freebsdfoundation.org/freebsd/how-to-guides/installing-freebsd-with-virtualbox-video-guide/)
- [FreeBSD 系统介绍视频指南](https://freebsdfoundation.org/freebsd-project/resources/an-introduction-to-the-freebsd-operating-system-video/)
- [在 FreeBSD 上安装桌面环境视频指南](https://freebsdfoundation.org/freebsd-project/resources/installing-a-desktop-environment-on-freebsd-video-guide/)
- [安装 FreeBSD Port 视频指南](https://freebsdfoundation.org/freebsd-project/resources/installing-a-port-on-freebsd-video-guide/)

基金会还出版免费版 FreeBSD 期刊：[https://www.FreeBSDfoundation.org/journal/](https://www.FreeBSDFoundation.org/journal/)

#### 法律 / FreeBSD 知识产权

基金会持有并保护 FreeBSD 商标，并为核心团队提供法律支持。

更多信息请访问 [https://www.FreeBSDFoundation.org](https://www.FreeBSDFoundation.org/)。

### FreeBSD 发布工程团队

链接：

[FreeBSD 13.1-RELEASE 时间表](https://www.freebsd.org/releases/13.1R/schedule/)

[FreeBSD 13.1-RELEASE 公告](https://www.freebsd.org/releases/13.1R/announce/)

[FreeBSD 发布版本](https://download.freebsd.org/releases/ISO-IMAGES/)

[FreeBSD 开发快照](https://download.freebsd.org/snapshots/ISO-IMAGES/)

联系人：FreeBSD 发布工程团队 [re@FreeBSD.org](mailto:re@FreeBSD.org)

FreeBSD 发布工程团队负责制定和发布官方 FreeBSD 项目的发行计划，宣布代码冻结，维护各分支等工作。

2022 年第二季度，该团队完成了 13.1-RELEASE 版本周期工作，这是 stable/13 分支的第二个发布版本。发布周期中共进行了三次 BETA 构建和六次 RC（发布候选）构建，由于最后阶段发现一些问题，最终发布日期从 2022 年 4 月 21 日推迟至 5 月 16 日。

感谢所有 FreeBSD 开发者和贡献者在 13.1-RELEASE 测试中提供的问题反馈，并认真对待版本周期中的提议修改。

此外，本季度还发布了 **main**、**stable/13** 和 **stable/12** 分支的多个开发快照版本。

赞助：Rubicon Communications, LLC ("Netgate")

赞助：FreeBSD 基金会

### 集群管理团队

链接：

[集群管理团队成员](https://www.freebsd.org/administration/#t-clusteradm)

联系人：集群管理团队 [clusteradm@FreeBSD.org](mailto:clusteradm@FreeBSD.org)

FreeBSD 集群管理团队负责管理项目依赖的机器，用于同步分布式工作和通讯。本季度主要工作包括：

- 在澳大利亚悉尼安装新镜像，由 IX Australia 托管
- 修复 CI 集群硬件故障
- 建立新的内部监控系统
- 定期进行集群范围的软件升级
- 定期维护 FreeBSD.org 用户账户

进行中的工作：

- 与 PowerPC 团队合作改进软件包构建器、通用和参考机器
- 硬件更新计划及修复各站点的各种故障
- 改进软件包构建基础设施
- 审查 service jail 和管理员操作
- 与文档工程团队合作改进 [https://www.freebsd.org](https://www.freebsd.org/) 和 [https://docs.freebsd.org](https://docs.freebsd.org/) 的部署
- 改进网站服务架构
- 改进集群备份计划
- 改进日志分析系统

正在寻找欧洲额外的完整镜像站点（五台服务器），详细需求见 [generic mirrored layout](https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout)。单台镜像服务器（见 [tiny mirror](https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror)）也欢迎提供，尤其是在欧洲。

### 持续集成（CI）

链接：

[FreeBSD Jenkins 实例](https://ci.freebsd.org/)

[FreeBSD CI 构建产物存档](https://artifact.ci.freebsd.org/)

[FreeBSD Jenkins wiki](https://wiki.freebsd.org/Jenkins)

[托管 CI wiki](https://wiki.freebsd.org/HostedCI)

[第三方软件 CI](https://wiki.freebsd.org/3rdPartySoftwareCI)

[相关 freebsd-testing@ 工单](https://preview.tinyurl.com/y9maauwg)

[FreeBSD CI 仓库](https://github.com/freebsd/freebsd-ci)

[dev-ci 邮件列表](https://lists.freebsd.org/subscription/dev-ci)

联系人：Jenkins 管理员 [jenkins-admin@FreeBSD.org](mailto:jenkins-admin@FreeBSD.org)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

联系人：[freebsd-testing 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-testing)

联系人：IRC #freebsd-ci 频道（EFNet）

FreeBSD CI 团队维护项目的持续集成系统，检查提交代码能否成功构建，并对新构建结果进行各种测试和分析。构建产物存档在 [artifact server](https://artifact.ci.freebsd.org/) 以便进一步测试和调试。CI 团队成员会检查失败的构建和不稳定的测试，并与相关专家合作修复代码或调整测试基础设施。

2022 年第二季度主要完成的任务：

- 修复 CI 集群的硬件故障问题

进行中的任务：

- 设计和实现 pre-commit CI 构建和测试（支持 [workflow 工作组](https://gitlab.com/bsdimp/freebsd-workflow)）
- 设计和实现 CI 集群构建发布产物（如发布工程操作）
- 测试和合并 [FreeBSD-ci 仓库](https://github.com/freebsd/freebsd-ci/pulls) 的 pull request
- 简化贡献者和开发者的 CI/测试环境设置
- 设置 CI 阶段环境并运行实验性作业
- 组织 freebsd-ci 仓库脚本以准备合并至 src 仓库
- 更新 wiki 文档

待办或排队任务：

- 收集和整理 [CI 任务与想法](https://hackmd.io/@FreeBSD-CI/freebsd-ci-todo)
- 设置测试 VM 的公共网络访问
- 使用裸机硬件运行测试套件
- 针对 -CURRENT 构建 drm ports 测试
- 计划运行 ztest 测试
- 增加更多外部工具链相关作业
- 提高硬件实验室成熟度并增加测试硬件
- 帮助更多软件在其 CI 流程中获得 FreeBSD 支持（Wiki 页面：[3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI)、[HostedCI](https://wiki.freebsd.org/HostedCI)）
- 与托管 CI 提供商合作，提升 FreeBSD 支持

更多进行中信息，请参见 [freebsd-testing@ 相关工单](https://preview.tinyurl.com/y9maauwg)。

赞助：FreeBSD 基金会

### FreeBSD Ports

链接：

[关于 FreeBSD Ports](https://www.freebsd.org/ports/)

[Ports 贡献指南](https://docs.freebsd.org/en/articles/contributing/#ports-contributing)

[FreeBSD Ports 监控](http://portsmon.freebsd.org/)

[Ports 管理团队](https://www.freebsd.org/portmgr/)

[Ports Tarball](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/)

联系人：René Ladan [portmgr-secretary@FreeBSD.org](mailto:portmgr-secretary@FreeBSD.org)

联系人：FreeBSD Ports 管理团队 [portmgr@FreeBSD.org](mailto:portmgr@FreeBSD.org)

Ports 管理团队负责把控 Ports 的整体方向、构建包以及人员事务。以下为上季度的情况：

Ports 数量略高于三万。上季度，“main”分支有 151 位提交者提交了 9,137 次修改，“2022Q2”分支有 61 位提交者提交了 589 次修改。截止报告撰写时，共有 2,700 个打开的 ports PR，其中 682 个尚未分配。与上季度相比，提交活动略有下降，PR 数量保持不变。注意：Freshports 似乎存在严重的过度统计问题，本季度的 ports 计数采用了不同方法，因此不可与上季度直接比较。

上季度，portmgr 欢迎 salvadore@ 回归，同时因缺乏活跃度告别了七位 ports 提交者。

在每两周一次的会议中，portmgr 讨论了以下主题：

- ca\_root\_nss 的未来
- 基本系统提供某些 .pc 文件的可行性
- 处理基本系统小版本升级时内核模块 ports 不兼容问题的方法

经过开发者讨论，portmgr 决定允许所有文档和源码提交者修复 Ports 中与功能无关的文档错误。

2022 年第二季度 Ports Tree 的主要变化包括：

- pkg 更新到 1.18.3 版本，Firefox 更新到 102.0，Chromium 更新到 103.0.50060.53
- 默认版本更新：GCC 更新到 11（powerpcspe 保持 8 版本），Lazarus 更新到 2.2.2，Python 更新到 3.9，Ruby 更新到 3.0
- 添加了两个新的 USES：gstreamer（支持基于 GStreamer 插件的 ports）和 pytest（用于 pytest 测试）

## 项目

涉及内核、用户空间、Ports 和外部项目的跨类别项目。

### 更新 Linux 兼容层

联系人：Dmitry Chagin [dchagin@FreeBSD.org](mailto:dchagin@FreeBSD.org)

联系人：Edward Tomasz Napierala [trasz@FreeBSD.org](mailto:trasz@FreeBSD.org)

目标是提升 FreeBSD 执行未经修改的 Linux 二进制文件的能力。可在 [Linux app status Wiki 页面](https://wiki.freebsd.org/LinuxApps) 查询具体 Linux 应用支持状态。

Y2k38 Linux 项目实现大部分完成，所有 '\*\_time64()' 系统调用已提交。

arm64 Linux 仿真层已达到 amd64 仿真层状态：实现了 vDSO、机器相关 futex、信号传递。

线程亲和性系统调用修改为 Linux 语义。

共修复 50 多个 bug，glibc-2.35 测试套件报告失败测试少于 80 个。

所有 Linux 仿真层更改已合并至 stable/13 分支。

对 libsysdecode 和 kdump 添加了初步支持 Linux 系统调用追踪工作，仍在增加更多追踪支持。

赞助：EPSRC（Edward 的工作）

### 在 FreeBSD riscv64 上的 Go

链接：

[golang 首页](https://github.com/golang/go)

[FreeBSD riscv64 github 仓库](https://github.com/MikaelUrankar/go/tree/freebsd_riscv64)

[FreeBSD riscv64 golang 问题](https://github.com/golang/go/issues/53466)

联系人：Mikaël Urankar [mikael@FreeBSD.org](mailto:mikael@FreeBSD.org)

联系人：Dmitri Goutnik [dmgk@FreeBSD.org](mailto:dmgk@FreeBSD.org)

Go 在 FreeBSD riscv64 的移植已完成，可构建并通过所有 run.bash 测试，包括 cgo（在 QEMU 和 Unmatched 上测试）。相关 pull request 已提交上游，并加入 proposals 项目活跃列，将在每周提案评审会议中审核。

### 微软 Hyper-V 和 Azure 上的 FreeBSD

链接：

[Azure 上 FreeBSD 文章](https://wiki.freebsd.org/MicrosoftAzure)

[Hyper-V 上 FreeBSD 文章](https://wiki.freebsd.org/HyperV)

联系人：微软 FreeBSD 集成服务团队 [bsdic@microsoft.com](mailto:bsdic@microsoft.com)

联系人：[freebsd-cloud 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-cloud)

联系人：FreeBSD Azure 发布工程团队 [releng-azure@FreeBSD.org](mailto:releng-azure@FreeBSD.org)

联系人：Wei Hu [whu@FreeBSD.org](mailto:whu@FreeBSD.org)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

[13.1-RELEASE Azure Marketplace 镜像](https://azuremarketplace.microsoft.com/marketplace/apps/thefreebsdfoundation.freebsd-13_1) 已发布。

进行中任务：

- 自动化镜像构建和发布流程
- 构建并发布基于 ZFS 的 Azure Marketplace 镜像

  - 受益于 [makefs(8)(https://man.freebsd.org/cgi/man.cgi?query=makefs&sektion=8&format=html) 和 [release(7)(https://man.freebsd.org/cgi/man.cgi?query=release&sektion=7&format=html) ZFS 支持的合并

    - [D23334](https://reviews.freebsd.org/D23334)
    - [D34426](https://reviews.freebsd.org/D34426)
    - [D35248](https://reviews.freebsd.org/D35248)
- 构建并发布 Hyper-V gen2 VM 镜像到 Azure Marketplace

  - 被 [264267 号 Bug](https://bugs.freebsd.org/264267) 阻塞

以上任务由 FreeBSD 基金会赞助，微软提供资源。

Wei Hu 与微软同事正在进行微软赞助的任务：

- 修复 Azure 上 Hyper-V gen2 VM 的启动问题

  - [264267 号 Bug](https://bugs.freebsd.org/264267)
- 将对 Hyper-V 虚拟机的移植支持到 aarch64

开放任务：

- 更新 FreeBSD 相关文档于 [Microsoft Docs](https://docs.microsoft.com/)
- 支持 FreeBSD 在 [Azure Pipelines](https://azure.microsoft.com/services/devops/pipelines/)
- 更新 [Azure agent port](https://www.freshports.org/sysutils/azure-agent) 至最新版本
- 回溯 [Azure agent 本地修改](https://github.com/Azure/WALinuxAgent/pull/1892)

赞助：微软（Wei Hu 及其他微软工作相关），FreeBSD 基金会（其他任务）

## 用户空间

影响基本系统及其程序的更改。

### LLDB 多进程调试支持的持续工作

链接：

[Moritz Systems 项目说明](https://www.moritz.systems/blog/multiprocess-support-for-lldb/) URL: [https://www.moritz.systems/blog/multiprocess-support-for-lldb/](https://www.moritz.systems/blog/multiprocess-support-for-lldb/)

[进展报告 1](https://www.moritz.systems/blog/implementing-non-stop-protocol-compatibility-in-lldb/) URL: [https://www.moritz.systems/blog/implementing-non-stop-protocol-compatibility-in-lldb/](https://www.moritz.systems/blog/implementing-non-stop-protocol-compatibility-in-lldb/)

联系人：Kamil Rytarowski [kamil@moritz.systems](mailto:kamil@moritz.systems)

联系人：Michał Górny [mgorny@moritz.systems](mailto:mgorny@moritz.systems)

根据上游所述，“LLDB 是下一代高性能调试器。它由一组可重用组件构建，充分利用 LLVM 项目中的现有库，例如 Clang 表达式解析器和 LLVM 反汇编器。”

FreeBSD 在基本系统中内置 LLDB。之前的赞助项目改进了 LLDB，使其成为基本系统中可靠的调试器，尽管与当代 GNU GDB 版本相比仍有一些限制。该项目始于 2022 年 4 月，旨在实现同时调试多个进程的完整支持。

在项目开始时，LLDB 对多进程调试的支持非常有限。客户端通过维护与不同服务器实例的多个连接，支持同时调试多个独立进程。得益于早期工作，服务器能够处理 `fork(2)` 和 `vfork(2)` 调用，并可以选择分离新 fork 出来的子进程并继续跟踪父进程，或分离父进程并跟踪子进程（相当于 GDB 的 `follow-fork-mode` 设置）。

项目完成后，LLDB 将能够同时跟踪任意数量的 fork 进程（相当于 GDB 的 `detach-on-fork off`）。将实现对 GDB 远程串行协议多进程扩展的完整支持，并对 non-stop 扩展提供部分支持，使多个进程能够独立恢复和停止。

赞助方：FreeBSD 基金会

### makefs(8) 的 ZFS 支持

链接：

[邮件列表帖子](https://lists.freebsd.org/archives/freebsd-hackers/2022-May/001128.html) URL: [https://lists.freebsd.org/archives/freebsd-hackers/2022-May/001128.html](https://lists.freebsd.org/archives/freebsd-hackers/2022-May/001128.html)

[makefs(8) 代码审查](https://reviews.freebsd.org/D35248) URL: [https://reviews.freebsd.org/D35248](https://reviews.freebsd.org/D35248)

[release(7) 代码审查](https://reviews.freebsd.org/D34426) URL: [https://reviews.freebsd.org/D34426](https://reviews.freebsd.org/D34426)

联系人：Mark Johnston [markj@FreeBSD.org](mailto:markj@FreeBSD.org)

makefs(8) 是一款源自 NetBSD 的工具，用于在用户空间中创建文件系统镜像。它是构建虚拟机（VM）镜像工具链中的有用组件，因为它不需要任何特殊权限，不同于格式化字符设备、挂载新文件系统并复制文件的方式。此外，makefs 可以创建可复现的镜像，并旨在最小化资源消耗。目前，FreeBSD 的 makefs 可以构建 UFS、cd9660 和 msdos（FAT）文件系统镜像。

最近的工作使 makefs 可以创建 ZFS 镜像，从而简化了基于 ZFS 的 VM 镜像构建。makefs 的 ZFS 支持包括创建多个数据集的能力，每个数据集映射到输入文件层次结构中的一个目录。然而，许多 ZFS 功能尚不支持，该实现仅提供生成可复现根池所需的功能。

后续工作使 release(7) 框架能够使用这一新的 makefs 扩展创建基于 ZFS 的 VM 和云镜像。

赞助方：FreeBSD 基金会

### 更新基本系统中的 OpenSSH

链接：

[OpenSSH](https://www.openssh.com/) URL: [https://www.openssh.com/](https://www.openssh.com/)

[OpenSSH 8.9 发布说明](https://www.openssh.com/txt/release-8.9) URL: [https://www.openssh.com/txt/release-8.9](https://www.openssh.com/txt/release-8.9)

[OpenSSH 9.0 发布说明](https://www.openssh.com/txt/release-9.0) URL: [https://www.openssh.com/txt/release-9.0](https://www.openssh.com/txt/release-9.0)

联系人：Ed Maste [emaste@freebsd.org](mailto:emaste@freebsd.org)

OpenSSH 是一套远程登录和文件传输工具，在 FreeBSD 基本系统中已从 8.8p1 版本更新至 9.0p1。

尚未合并到 stable/13 和 stable/12 分支，预计将在七月完成。

**注意**：OpenSSH 9.0p1 默认将 scp(1) 从传统的 scp/rcp 协议切换为 SFTP 协议。可使用参数 `-O` 恢复使用旧协议。

赞助方：FreeBSD 基金会

### pf 状态更新

联系人：Kristof Provost [kp@FreeBSD.org](mailto:kp@FreeBSD.org)

联系人：Reid Linnemann [rlinnemann@netgate.com](mailto:rlinnemann@netgate.com)

#### 以太网

pf 最近增加了对以太网层过滤的支持。详见 2021 年第 2 季度 pf\_ethernet 报告。

此后，以太网层过滤功能已扩展，包括：

- 锚点支持
- 能够查看第 3 层头部，以匹配源/目的 IP(v4/v6) 地址
- IP 地址匹配的表格支持
- 直接派发到 dummynet
- 将以太网层数据包直接传递到 dummynet，而不是标记数据包并依赖第 3 层处理 dummynet

#### Dummynet

pf 最近开始能够使用 dummynet 进行数据包调度。该支持已扩展和改进，现在认为已可用于生产环境。

一个显著的修复是 reply-to/route-to 流量现在也受到 dummynet 调度。

#### 最后匹配时间戳

pf 现在跟踪规则的最后匹配时间。类似于 ipfw 规则时间戳，这些时间戳在内部为系统“实时时钟”的 uint32\_t 快照（单位为秒）。时间戳为 CPU 本地，每次规则或状态匹配时更新。

赞助方：Rubicon Communications, LLC (“Netgate”)

## 内核

内核子系统/功能、驱动支持、文件系统等更新。

### 更新 FreeBSD ENA 驱动

链接：

[ENA README](https://github.com/amzn/amzn-drivers/blob/master/kernel/fbsd/ena/README.rst) URL: [https://github.com/amzn/amzn-drivers/blob/master/kernel/fbsd/ena/README.rst](https://github.com/amzn/amzn-drivers/blob/master/kernel/fbsd/ena/README.rst)

联系人：Michal Krawczyk [mk@semihalf.com](mailto:mk@semihalf.com)

联系人：Dawid Gorecki [dgr@semihalf.com](mailto:dgr@semihalf.com)

联系人：Marcin Wojtas [mw@FreeBSD.org](mailto:mw@FreeBSD.org)

ENA（Elastic Network Adapter）是 Amazon Web Services (AWS) 虚拟化环境中的智能网卡。ENA 驱动支持多个发送和接收队列，并且可处理高达 100 Gb/s 的网络流量，具体取决于使用的实例类型。

自上次更新以来完成的工作：

- ENA 驱动 v2.5.0 上游更新，包括：

  - 改进复位例程处理
  - 延长定时器服务生命周期以检测更多硬件故障
  - 修复 Tx 请求 ID 验证逻辑
  - 修复 Tx IPv6 L4 校验和卸载处理
  - 为驱动增加 NUMA 感知
- 对即将发布的 ENA 驱动版本 (v2.6.0) 的内部审查，包括：

  - 进一步改进复位处理
  - 代码清理和样式修复
  - 日志改进
  - 修复 ENI 指标获取

正在进行的工作：

- 即将发布 ENA 驱动版本 (v2.6.0) 的测试

赞助方：亚马逊

### 新的蓝牙配置守护进程：blued

链接：

[blued git](https://git.lysator.liu.se/kempe/blued) URL: [https://git.lysator.liu.se/kempe/blued](https://git.lysator.liu.se/kempe/blued)

联系人：

邮箱：[kempe@lysator.liu.se](mailto:kempe@lysator.liu.se)

IRC：[kempe@libera.chat](mailto:kempe@libera.chat)

#### 简介

blued 工具提供了 IPC 接口，使非特权用户能够以用户友好的方式连接和使用 Bluetooth 设备，并支持安全简易配对（公钥加密，如果设备支持，还可防止中间人攻击）。

#### 什么是 blued？

blued 由三个部分组成：库、守护进程和命令行工具。库抽象了蓝牙的细节，守护进程管理蓝牙设备，命令行工具允许用户列出或扫描蓝牙设备、与设备配对或取消配对。命令行工具通过 UNIX 套接字与守护进程通信。

与 bthidd 和 hcsecd 不同，blued 支持安全简易配对并提供 IPC。要使 HID 设备工作，仍需 bthidd。提供了一个脚本，用于配对蓝牙设备并适当配置 bthidd，使其可以自动工作并在无需用户干预的情况下重新连接。

待配对稳定且 Bug 修复，计划将 bthidd 与 blued 集成，以便 HID 设备在配对后无需外部脚本即可自动生效。长期目标是提供图形界面，列出设备并提供一键连接的简单设置。

#### 安装和使用 blued v0.1

需要在 **/etc/src** 安装可选的 `src` 组件。

首先，确保 [已加载可用的 Bluetooth 驱动程序，如 FreeBSD 手册所述](https://docs.freebsd.org/en/books/handbook/advanced-networking/#network-bluetooth)。

测试 blued 时，获取 [blued v0.1 源代码](https://git.lysator.liu.se/kempe/blued/-/releases/v0.1)，然后编译，使用 **kernel\_patches** 中的补丁打补丁 FreeBSD 内核，并按 **README** 中说明重新编译 `hci` 模块。

我主要在 FreeBSD 12.3 上测试了 blued，但在测试 13.1 时补丁也能干净应用。目前没有提供 Port，但可以直接从构建目录运行软件，或执行“make install”安装所有所需文件。blued 和 bluecontrol 都使用 capsicum，并且 blued 可以配置以降低 root 权限。

更多信息请参阅 **README** 的 `Running blued` 部分。

#### 参与贡献

##### 测试

我只用自己的鼠标测试过此软件，样本量仅一款蓝牙设备。我预期会有问题，非常期待其他人的反馈！

遇到问题时，请提供 `/var/log/debug.log` 和 `/var/log/messages` 的输出，以及尝试配对时的 `hcidump -x` 流量转储，有助于排查问题。

##### 贡献代码

如果想参与代码并提交补丁，欢迎 [访问 Lysator 的仓库](https://git.lysator.liu.se/kempe/blued)。

### OpenVPN DCO

链接：

[D34340](https://reviews.freebsd.org/D34340) URL: [D34340](https://reviews.freebsd.org/D34340)

[OpenVPN wiki](https://community.openvpn.net/openvpn/wiki/DataChannelOffload) URL: [OpenVPN wiki](https://community.openvpn.net/openvpn/wiki/DataChannelOffload)

联系人：Kristof Provost [kp@FreeBSD.org](mailto:kp@FreeBSD.org)

OpenVPN DCO（数据通道卸载）将 OpenVPN 数据包处理移入内核。

传统上，OpenVPN 使用 tun(4) 接口收发数据包。在此设置下，接收到的数据包由内核接收，传递给 OpenVPN 应用解密，然后再回到内核进行网络栈处理。这需要多次内核与用户空间切换，自然会带来性能开销。

新的 if\_ovpn OpenVPN DCO 卸载驱动在内核中完成加密/解密，提高了性能。

初步性能测试显示吞吐量从约 660Mbit/s 提升至约 2Gbit/s。

用户空间的 OpenVPN 代码也需要修改以使用新的 if\_ovpn 卸载驱动，预计会在未来 OpenVPN 2.6.0 发布中实现。

赞助方：Rubicon Communications, LLC (“Netgate”)

### 无线动态

链接：

[Intel iwlwifi 状态 FreeBSD wiki 页面](https://wiki.freebsd.org/WiFi/Iwlwifi) URL: [https://wiki.freebsd.org/WiFi/Iwlwifi](https://wiki.freebsd.org/WiFi/Iwlwifi)

[Realtek rtw88 状态 FreeBSD wiki 页面](https://wiki.freebsd.org/WiFi/Rtw88) URL: [https://wiki.freebsd.org/WiFi/Rtw88](https://wiki.freebsd.org/WiFi/Rtw88)

[Realtek rtw89 状态 FreeBSD wiki 页面](https://wiki.freebsd.org/WiFi/Rtw89) URL: [https://wiki.freebsd.org/WiFi/Rtw89](https://wiki.freebsd.org/WiFi/Rtw89)

联系人：Bjoern A. Zeeb [bz@FreeBSD.org](mailto:bz@FreeBSD.org)

该项目旨在为 FreeBSD 引入对新芯片组的支持，目前使用 LinuxKPI 兼容代码，依赖原生 net80211 和内核代码。此外，项目还致力于支持更新的无线标准。第二季度，共有 40 次提交进入 FreeBSD CURRENT。随着更多用户尝试多驱动支持，支持时间也增加。

在 13.1-RELEASE 中首次引入了早期版本的 Intel iwlwifi 衍生无线驱动。随后在 CURRENT 和 stable/13 中更新了 iwlwifi 驱动和固件。与上游 Intel Linux 驱动共享的文件变更少于 400 行。近期解决了老芯片组的长期问题，使 iwm(4) 支持的网卡在近三个月后再次能与 iwlwifi(4) 配合使用。项目年末的主要目标是达到现代速度。

4 月 1 日，利用主要由 iwlwifi 工作构建的 LinuxKPI 基础设施，将 Realtek rtw88(4) 驱动提交了到 CURRENT。由于 DMA 问题，随后几周开发了一个工作绕过方案并合入源码树，使用户无需再补丁内核。该驱动仍需在物理内存超过 4GB 的机器上设置 loader.conf 可调参数。此参数能让驱动在 6 月合入到 stable/13，并随后在 CURRENT 和 stable/13 中进一步更新。随着基于 rtw88 芯片组的 USB 部分准备纳入 Linux，FreeBSD 对 USB 部分的支持工作已启动，但仍需更多时间。

近几个月，Realtek rtw89 已能编译，但仍在持续开发中，需要实现稳定运行和关联后才能在 CURRENT 中启用。

感谢所有用户的测试与反馈，耐心等待下一次更新、修复或回复。非常高兴与大家合作！请继续发送 Bug 报告，但感谢应归于 FreeBSD 基金会，使这些工作得以实现。

有关开发的最新状态，请关注 freebsd-wireless 邮件列表并查看 wiki 页面。

赞助方：FreeBSD 基金会

### 共享页地址随机化

链接：

[D35392](https://reviews.freebsd.org/D35392) [D35393](https://reviews.freebsd.org/D35393) [D35349](https://reviews.freebsd.org/D35349)

联系人：Kornel Duleba [mindal@semihalf.com](mailto:mindal@semihalf.com)

联系人：Marcin Wojtas [mw@FreeBSD.org](mailto:mw@FreeBSD.org)

共享页是 R/X 页，由映像激活器映射到每个进程中。它存储信号跳板以及其他元数据，例如实现用户空间计时器所需的信息。此前它映射在进程虚拟地址空间的顶部。经过所述更改后，其地址将被随机化。计划默认对 64 位二进制启用此功能，覆盖所有架构。目前正在审核补丁，等待批准。

赞助方：Stormshield

## 架构

更新平台特定功能，并引入对新硬件平台的支持。

### NXP DPAA2 支持

链接：

[变更历史](https://github.com/mcusim/freebsd-src/commits/lx2160acex7-dev)

[源码树](https://github.com/mcusim/freebsd-src/tree/lx2160acex7-dev/sys/dev/dpaa2)

联系人：Dmitry Salychev [dsl@FreeBSD.org](mailto:dsl@FreeBSD.org)

联系人：Bjoern A. Zeeb [bz@FreeBSD.org](mailto:bz@FreeBSD.org)

部分 NXP SoC（LX2160A、LS1088A）配备了 [DPAA2](https://www.nxp.com/design/qoriq-developer-resources/second-generation-data-path-acceleration-architecture-dpaa2:DPAA2)，第二代数据路径加速架构。它支持动态配置并连接数据包处理“对象”（DPNI 用于网络接口，DPMAC 用于媒体访问控制器等），形成片上网络。

在上个季度，驱动在 [SolidRun Honeycomb LX2](https://solidrun.atlassian.net/wiki/spaces/developer/pages/197494288/HoneyComb+LX2+ClearFog+CX+LX2+Quick+Start+Guide)（ACPI 测试平台）上已经足够稳定，Traverse Technologies 也提供了 [Ten64 FreeBSD 预览](https://forum.traverse.com.au/t/freebsd-preview-for-ten64/173)（用于 FDT 测试平台）。

该驱动仍在开发中，但接近首次版本审核，以便大家都能使用。

正在进行的工作（WIP）：

- FDT MDIO 支持。FreeBSD 目前不支持 SPF 部件。
- 驱动资源释放，以正确卸载 dpaa2.ko。
- [Bug 修复](https://github.com/mcusim/freebsd-src/issues) 与改进。

待办事项：

- DPIO 和 DPNI 的 CPU 亲和性设置。
- 基于缓存内存的软件门户。
- 瓶颈缓解。
- 硬件支持的其他部件（DPSW、DCE 等）。

赞助方：Bare Enthusiasm :)

赞助方：Traverse Technologies（提供 Ten64 硬件用于测试）

### arm64 及更高平台的中等大小超级页

联系人：Eliot H. Solomon [ehs3@rice.edu](mailto:ehs3@rice.edu)

联系人：Alan L. Cox [alc@rice.edu](mailto:alc@rice.edu)

64 位 ARM 架构的页表描述符格式包含一个称为 Contiguous 的标志。该标志告诉 MMU 可以使用单个 TLB 条目缓存一组对齐且物理连续的 16 个页表条目，这些条目具有相同权限和属性。

Contiguous 标志，以及 RISC-V 架构中类似的 Svnapot 扩展，可使用 64 KiB 的超级页。这些中等大小的超级页可以为较小的内存对象带来类似于传统 2 MiB 超级页的地址转换加速效果。

本项目旨在为 FreeBSD 引入中等大小超级页支持。目前，我们已修改 arm64 pmap 代码，通过检测物理连续的页表条目并使用 Contiguous 标志提升它们，自动利用 64 KiB 超级页。下一步，我们正在修改内核的超级页预留模块，以支持除现有 2 MiB 预留外的 64 KiB 预留。增加中等大小预留将允许虚拟内存系统显式分配符合超级页提升要求的内存，而不是仅靠机会发生。

目标是以通用方式实现，使得可以指定多个任意 2 的幂次方的预留大小，从而方便在其他架构（如 Ryzen 的 PTE 合并）上利用硬件特性，将 4 KiB 页表条目组透明合并为中等大小超级页。

赞助方：莱斯大学计算机科学系

## 文档

文档树、手册页或新外部书籍/文档的显著更新。

### 文档工程团队

链接：[FreeBSD 文档项目](https://www.freebsd.org/docproj/)

链接：[新贡献者文档工程指南](https://docs.freebsd.org/en/books/fdp-primer/)

链接：[文档工程团队](https://www.freebsd.org/administration/#t-doceng)

联系人：文档工程团队 [doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)

文档工程团队负责处理 FreeBSD 文档项目的一些元项目问题；详情请参阅 [FreeBSD 文档工程团队章程](https://www.freebsd.org/internal/doceng/)。

上季度，Graham Perrin (grahamperrin@) 和 Pau Amma (pauamma@) 获得了文档提交权限。

当前待处理和讨论的事项：

- 使用项目 GeoDNS 基础设施镜像网站和文档门户。
- 文档中商标的处理方式。
- 移除网站和文档门户的过期翻译。

#### FreeBSD Weblate 翻译

链接：[在 Weblate 翻译 FreeBSD](https://wiki.freebsd.org/Doc/Translation/Weblate)

链接：[FreeBSD Weblate 实例](https://translate-dev.freebsd.org/)

##### 2022 年第二季度状态

- 12 种语言
- 152 名注册用户（新增 9 名用户）

##### 支持语言

- 中文（简体）(zh-cn)
- 中文（繁体）(zh-tw)
- 荷兰语 (nl)
- 法语 (fr)
- 德语 (de)
- 印度尼西亚语 (id)
- 意大利语 (it)
- 挪威语 (nb-no)
- 波斯语 (fa-ir)
- 葡萄牙语 (pt-br)
- 西班牙语 (es)
- 土耳其语 (tr)

感谢所有参与翻译或校对文档的贡献者。请在本地用户组中推广此工作，我们始终需要更多志愿者。

#### FreeBSD 网站改版 - WebApps 工作组

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

该工作组负责创建新的 FreeBSD 文档门户，并重新设计 FreeBSD 主网站及其组件。FreeBSD 开发者可在 FreeBSD Slack 频道 #wg-www21 跟进并加入工作组。工作分为四个阶段：

1. 文档门户重设计
   创建新的响应式设计，并提供全局搜索。（**已完成**）
2. 网页手册页重设计
   使用 mandoc 生成 HTML 页面的脚本。（**进行中**）
3. Ports 页面网页重设计
   Ports 脚本用于创建应用门户。（**进行中**）
4. FreeBSD 主网站重设计
   新设计，响应式并支持暗色主题。（**未开始**）

## Ports

涉及 FreeBSD Ports 的更改，无论是影响大部分 Ports 树的全面更改，还是单个 Port 的更新。

### FreeBSD 上的 KDE

链接：

[KDE FreeBSD](https://freebsd.kde.org/)

[KDE FreeBSD 社区](https://community.kde.org/FreeBSD)

联系人：Adriaan de Groot [kde@FreeBSD.org](mailto:kde@FreeBSD.org)

FreeBSD 上的 KDE 项目将 KDE 社区的软件及其依赖和相关软件打包到 FreeBSD Ports 中。软件包括完整桌面环境 KDE Plasma（支持 X11 和 Wayland）以及可在任何 FreeBSD 机器上使用的数百款应用。

KDE 团队 (kde@) 也属于 desktop@ 和 x11@，构建软件栈，使 FreeBSD 成为美观、可日常使用的图形桌面系统。以下内容主要涉及 KDE 相关 Ports，同时也包括对整个桌面栈有意义的项目。

#### KDE 栈

KDE Gear 每季度发布一次，KDE Plasma 每月更新，KDE Frameworks 每月发布新版本。这些（大型）更新会在上游发布后不久落地，不单独列出。

- **astro/kstars** 最新版本 3.5.9。
- **deskutils/grantleetheme** 因安装结构有特殊变更，被记录在 UPDATING 中。
- **deskutils/kalendar** 加入 KDE Gear 发布。
- **devel/okteta** 更新二进制、八进制和十六进制数据查看与编辑器。
- **finance/kraft** 对新 KDE Frameworks 需要特定构建修复。
- 增补 **games/gcompris-qt**，支持更多图像格式。
- **graphics/digikam** 构建时不再需要 SQL 服务器。
- **graphics/krita** 更新至 5.0.5，可能是最后一个 5.0 版本。
- 最近 **math/labplot** 版本新增大量功能，适合数据绘图使用。
- 更新 **net-im/ruqola**，为 Qt 风格 Rocket chat 应用。
- **www/falkon** 加入 KDE Gear 发布。

#### 相关应用

- **archivers/quazip** 更新。
- **deskutils/semantik** 更新。
- **devel/py-qt5-pyqt** 更新，现在 Port 会拉取 DBus，Qt 桌面应用普遍需要。
- **devel/qcoro** 解决在某些 FreeBSD 版本上的构建问题。
- **devel/qtcreator** 每次新版本均更新。
- **devel/qt5** 更新 Port 基础设施，避免卸载时出现错误。
- **graphics/ksnip** 及相关库更新至最新版本。
- Matrix 客户端 Nheko (**net-im/nheko**) 和 Neochat (**net-im/neochat**) 随发布和库更新而更新。
- **x11/rsibreak** 更新，帮助长时间写季度报告时防止伤害。

#### 其他

- **devel/appstream** 更新以支持更多应用信息。
- **devel/cmake** 偏好使用通用 python3 而非版本化 python3，当用户安装多个 python3 Port 和 lang/python3 时。
- **devel/dbus** 更新。
- **graphics/poppler** 多次更新。
- **graphics/ImageMagick**（6 和 7）多次更新。
- **multimedia/gstreamer** 更新。

### GCC：更新 GCC\_DEFAULT 及其他改进

链接：

[GCC 项目](https://gcc.gnu.org/)

[GCC 11 发行系列](https://gcc.gnu.org/gcc-11/)

联系人：

[toolchain@FreeBSD.org](mailto:toolchain@FreeBSD.org)

Gerald Pfeifer [gerald@pfeifer.com](mailto:gerald@pfeifer.com)

Lorenzo Salvadore [salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)

Piotr Kubaj [pkubaj@FreeBSD.org](mailto:pkubaj@FreeBSD.org)

- salvadore@ 在 `Mk/bsd.default-versions.mk` 中将 GCC\_DEFAULT 从 10 升级到 11，并根据 antoine@ 的实验运行报告提交并修复了一些 bug，感谢所有协助此任务的人。GCC\_DEFAULT 从 GCC 10 升级到 GCC 11 已由 gerald@ 提交，并赶上了下一个季度分支。[https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=258378](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=258378)
- pkubaj@ 对 GCC 11 及更新版本的 GCC 自举过程启用了链接时间优化 (LTO\_BOOTSTRAP) 选项（默认启用）。启用 LTO\_BOOTSTRAP 构建需要大量内存和时间，具体资源需求取决于配置（例如从 Ports 构建或使用 poudriere，架构类型等）。例如，有用户报告需要 5 GiB tmpfs，而在 [PR 265254](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=265254#c2) 中估计约 130 GB 内存需求，原因是生成了大量进程（参见 [https://gcc.gnu.org/bugzilla/show\_bug.cgi?id=106328](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=106328)）。如果资源不足，可考虑禁用 LTO\_BOOTSTRAP，使用 STANDARD\_BOOTSTRAP 或完全禁用 BOOTSTRAP。
- pkubaj@ 还新增了 lang/gcc12 和 lang/gcc13-devel Ports，并将 lang/gcc9 更新至 9.5。
- 以下三个更改仍需协助与 upstream GCC 协作（需要源代码经验，而非 Ports）：

  - upstream lang/gcc11/patch-gets-no-more
  - upstream lang/gcc11/patch-arm-unwind-cxx-support
  - [https://bugs.freebsd.org/bugzilla/show\_bug.cgi?id=256874](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=256874)

### Valgrind：13.1 / 14.0 的多项 Bug 修复和更新

链接：

[Valgrind 主页](https://www.valgrind.org/)

[Valgrind 新闻](https://www.valgrind.org/docs/manual/dist.news.html)

联系人：Paul Floyd [pjfloyd@wanadoo.fr](mailto:pjfloyd@wanadoo.fr)

在过去几个月中，FreeBSD 上的 Valgrind 修复了大量 Bug，尤其是 i386 版本已基本赶上 amd64 版本。

devel/valgrind-devel Port 已更新至 3.20.0.g20220612,1，包含以下改动。如果你经常使用 Valgrind，请切换到 valgrind-devel。

自 Valgrind 3.19.0（devel/valgrind Port 提供版本）以来的改动包括：

- 当 Valgrind 保存系统调用的进位标志时，如果信号到达，修复错误的信号恢复
- 修复读取 lld 9 版及之后生成的 PT\_LOAD DWARF 调试信息，RW 段被拆分为两部分，主要影响共享库 (.so 文件)
- 在 i386 上正确管理线程 GDT，原先限制应用最多创建 8192 个线程
- 使 'brk' 的第一页在寻址时无效
- 分析并清理回归测试套件，特别是调整 i386 内存泄漏测试，避免检测到 ECX 中残留指针导致的可能泄漏
- 使 core dump 可被 lldb 读取
- 改善 C 分配函数设置 errno 的行为
- 修复 Valgrind 与 llvm-devel (15.0.0) 的构建

针对 FreeBSD 13.1 / 14.0：

- syscall 包装器：funlinkat、copy\_file\_range、swapoff、shm\_open2
- 为 fcntl 添加 K\_INFO 支持
- 支持新的 auxv 条目
- 添加 DRD 和 Helgrind 的默认抑制

已提供 vgdb 调用器初始版本——能让 vgdb 使用 ptrace 强制 Valgrind 轮询 gdb 命令，但 Ports 版本尚不可用。

剩余问题不多，预计 FreeBSD 14.0 及更新版本 llvm 仍需支持。其他包括：

- 部分错误信息获取正确源信息存在小问题
- 更好的 core dump（低优先级）
- Helgrind 的 TLS（线程局部存储）处理（难以实现）

### FreeBSD 上的 Pantheon 桌面

链接：

[elementary OS](https://elementary.io)

[开发仓库](https://codeberg.org/olivierd/freebsd-ports-elementary)

联系人：Olivier Duchateau [duchateau.olivier@gmail.com](mailto:duchateau.olivier@gmail.com)

Pantheon 桌面环境面向 elementary OS 设计，基于 GNOME 技术（如 Mutter、GNOME Shell、GTK 3 和 4），使用 Vala 编写。

目标是为用户提供一个新的桌面环境。部分功能支持不完整，但可实现完整会话。

仓库包含 Mk/Uses 框架 `elementary.mk`、官方应用以及依赖 `x11-toolkits/granite` 的精选 Ports（共 56 个新 Ports）。

已提交多个补丁，特别是：

- `x11-toolkits/granite7`
- `devel/libgee` 更新至 0.20.5 [bug #262893](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=262893)
- `sysutils/bamf` 更新至 0.5.6 [bug #264203](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=264203)

#### 待办任务

- 增加用户设置支持（当前非常 Ubuntu 中心化）
- 完成 wingpanel-indicator-power（电源管理）移植

### Intel igt-gpu-tools 完整 Port

链接：

[FreeBSD Wiki 项目页面](https://wiki.freebsd.org/SummerOfCode2022Projects/ImprovingTheLinuxKPICompatibilityLayerForTheFreeBSDGraphicsStack/)

[状态报告](https://cdaemon.com/tags/gsoc2022/)

联系人：Jake Freeland [jfree@freebsd.org](mailto:jfree@freebsd.org)

Intel 的 igt-gpu-tools 是 Linux 上 DRM 驱动通用测试套件。套件分为针对 kms、内存管理和命令提交的测试和工具，提供低级报告用于跟踪内核变更和高效调试现代 DRM 驱动。

将该项目移植到 FreeBSD 可提升 LinuxKPI 驱动的稳定性，并通过适当的 kms 驱动测试套件提升 FreeBSD 桌面体验与 Linux 代码同步。

项目于 2022 年 6 月 13 日在 FreeBSD Google Summer of Code 项目下正式启动。适配代码可编译，已移除非 FreeBSD 兼容片段，计划以 POSIX 方式重实现这些片段。

主要不兼容代码包括：debugfs、libkmod、libprocps、Linux 性能事件、Linux userfaultfd。如愿意协助将 libkmod 或 libprocps 移植到 Ports 树，请联系作者。

当 FreeBSD 兼容代码完成后，将在 FreeBSD 14.0-CURRENT 上使用多种显卡运行修改后的 igt 测试，如测试通过，项目差异将提交到 Ports 树。

赞助：FreeBSD 谷歌编程之夏
