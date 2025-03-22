# 2013 EuroBSDcon 开发者峰会特别篇

- 原文链接：<https://www.freebsd.org/status/report-2013-09-devsummit.html>


这份特别的状态报告总结了 2013 年 EuroBSDcon 开发者峰会各工作组的讨论内容。FreeBSD 项目在各种活动中组织开发者峰会，通常在主要的 BSD 会议上，以便开发者们能够面对面地讨论问题。

## [桌面](https://www.freebsd.org/status/report-2013-09-devsummit.html#Desktop)

| 链接                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [总结](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=DesktopWG-Summary.pdf) |

联系人：Kris Moore <[kmoore@FreeBSD.org](mailto:kmoore@FreeBSD.org)>

在桌面工作组中，Kris Moore 总结了过去几个月 PC-BSD 领域的变化。基于新发布的 9.2-RELEASE 版本的构建正在进行中，基于 10-STABLE 的未来构建也将很快推出。计划是跟踪 10-STABLE 分支，直到其变成 11-STABLE。Kris 还描述了他们已切换到的滚动发布模型。该方法利用 freebsd-update(8) 提供基于内核和用户空间工具的滚动更新，与此同时，pkg(8) 被用于桌面应用程序的包管理。还报告称，PC-BSD 团队已经改善了他们工具的 ZFS 集成，包括安装程序。即将发布的 PC-BSD 版本的另一个亮点是，它们将包括 Gleb Kurtsou 的 PEFS，提供基于 PAM 的认证来加密用户主目录。

接下来，报告和讨论了当前进行中的项目。最近，Port sysutils/pcbsd-utils 和 sysutils/pcbsd-utils-qt4 已添加到 ports 中，其中包含所有 PC-BSD 开发的工具和实用程序，前者是命令行版本，后者是具有 GUI 支持的版本。PC-BSD 开发者们还在开发一个 Life-preserver ZFS 命令行和 GUI 工具，仍在积极开发中。此工具的目的是利用 ZFS 的快照和复制功能作为备份解决方案。

最后，总结了 PC-BSD 10 的计划。PC-BSD 使用的 PBI 包格式正在修订，将更新为使用 pkg(8) 仓库构建 PBI，并为服务器 PBI 提供更好的集成。作为此项工作的部分，将调查是否有可能在不实际安装的情况下运行 PBI。pc-sysinstall 将具有文本界面。起初将是基础版本，但以后将提供一个命令行接口，通过 pc-sysinstall 后端进行安装。

---

## [开发者峰会专题](https://www.freebsd.org/status/report-2013-09-devsummit.html#Developer-Summit-Track)

| 链接                                                        |
| ----------------------------------------------------------- |
| [讲座播放列表](http://goo.gl/2EF30C) |

联系人：Gábor Pálí <[pgj@FreeBSD.org](mailto:pgj@FreeBSD.org)>

自 2011 年起，FreeBSD 开发者峰会专题已成为 BSDCan 和 EuroBSDcon 会议的重要组成部分。它为开发者和社区成员提供了一个机会，展示他们的最新项目，集思广益解决难题，培训与会者使用新工具，观察 FreeBSD 开发过程并讨论如何改进，分享他们的公司如何使用 FreeBSD，或协调活动。在欧洲实例中，还可以听到谷歌编程之夏学生的报告。

在 2013 年 EuroBSDcon 会议上，我们有以下主题的讲座：ARM 超页、SDIO 堆栈、移植 GlusterFS、无人值守加密内核崩溃转储、为压缩服务添加 Capsicum 支持、智能下载管理服务、LLDB、数据包转发改进、多路径 TCP 支持、基于 FreeBSD 的网络仿真环境，最后是将 Mirage 操作系统（用 OCaml 函数式语言编写）移植到 FreeBSD。讲座录音（带幻灯片和演示的音频）播放列表可以在上述 URL 部分找到。

## [DNS](https://www.freebsd.org/status/report-2013-09-devsummit.html#DNS)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=20130928-eurobsdcon-dns-summary.pdf)      |

联系人：Erwin Lansing <[erwin@FreeBSD.org](mailto:erwin@FreeBSD.org)>

FreeBSD 10 将不再包含 BIND，而是基于 unbound(8) 和 LDNS，这两个工具已被导入到基本系统中，同时还替代了简单的 host(1) 工具。LDNS 还附带了 drill(1)，需要一个简单的包装器使其与 dig(1) 命令行界面兼容。OpenSSH 可以使用 LDNS 来检查 SSH 指纹，这也意味着默认启用了 DNSSEC 验证。请注意，unbound(8) 将被隐藏，它仅作为本地解析器使用。对于其他用途，用户需要在 Ports 中安装其版本。

对于下一个主要版本 FreeBSD 11，将有更多时间来寻找 BIND 的替代方案，因此在工作组中也讨论了理想的 DNS 实现要求。基于讨论结果，我们希望拥有一个缓存的、验证的解析器库，该库通过 Capsicum 隔离，支持每个用户的策略并与 Casper 守护进程集成，采用 BSD 许可，低占用，快速且线程安全。最重要的一点是，我们希望标准化面向应用层的 API，以便能够向用户报告与 DNSSEC 操作相关的事件。为此，已经有许多提案，如 Hoffman 提出的 get-api，或为 libval 提出的 draft-hayatnagarkar-dns-ext-validator-api，但目前该标准正在 IETF 成员的推动下进行标准化。我们希望联系这些人，确保 FreeBSD 11 成为标准的参考实现。



## [文档](https://www.freebsd.org/status/report-2013-09-devsummit.html#Documentation)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=DocWGSummaryReport.pdf)      |

联系人：Benedict Reuschling <[bcr@FreeBSD.org](mailto:bcr@FreeBSD.org)>

今年我们尝试了一些新方法，因此我们不再做大量讨论，而是集中精力实际工作，并与参与工作组的成员一起解决 PR 问题。结果发现这种方式并不那么奏效，因为我们有很多事情需要讨论，但最终一些问题还是得到了修复。

有一个巨大的需求是创建一个新网页：它需要更加现代化，以跟上近期的趋势。网页应该提供动态内容，如博客列表、Twitter 动态等。目前的问题是，网站缺少许多基本功能，例如搜索功能无法正常工作。Isabelle Long 一直在努力将 DuckDuckGo 搜索引擎集成到网站中，并希望很快提交必要的更改。还有其他问题，例如，网站没有链接到 FreeBSD 论坛，而 FreeBSD 论坛已经成为用户的另一种支持选项。

然后，FreeBSD 基金会的代表加入了我们的工作组，向我们展示了他们正在进行的工作。他们展示了他们为自己网站设计的提案。他们的建议是使 FreeBSD 基金会网站的外观与 FreeBSD 项目网站相似，以便这两个页面在视觉上可以连接。根据他们展示的华丽设计，我们认为这可能需要大量的基础设施工作，才能使我们的网站与基金会的相似。因此，我们决定组建一个由项目成员组成的新团队，专注于新网站的设计，以确保新设计能够满足各方的期望，如管理、安全性、功能性等。

另一个讨论话题是 FreeBSD 手册的印刷版工作。我们曾承诺在 BSDCan 大会前完成这项工作，但显然我们未能按时完成。Dru Lavigne 对整个手册进行了审查，并确定了许多需要解决的问题（如过时内容、无关章节等），以便为印刷版准备更好的内容。我们需要更多的内容和审阅者，因此如果你在查看手册时发现某个章节过时，请联系文档团队。你不必立即提交补丁，只需提供几句或一段话来改进或添加对特定系统功能的描述。文档团队将负责将这些内容加入手册或相关文档中。

我们还讨论了为手册的特定章节和部分指定维护者的想法，类似于 Ports 中实施的政策，这样用户和相关的 PR 可以直接转发给他们，维护者负责保持这些区域的文档更新。我们的目标是减少文档团队的整体工作量。

最后，在供应商小组中提到，我们希望重构目前的文档翻译工作流程。当前我们使用标准编辑器逐句翻译，这个过程非常繁琐。此外，大多数翻译团队都很小，因此他们很难赶上英文文档的更新，导致翻译内容很快过时。我们与 Gavin Atkinson 简要讨论了是否能从文档树中移除那些非常过时的文档，例如仍反映 FreeBSD 5.x 版本的文档。总的来说，主要目标是建立一个帮助跟踪翻译的系统，就像 PC-BSD 开发者正在做的那样：我们知道 Kris Moore 编写了一些脚本，扩展了像 Pootle 这样的标准工具来提高效率。能够看到哪些句子已经翻译，哪些还未翻译，哪些可以重用，将是一个巨大的进步。这些系统的另一个好处是，它们可以为普通贡献者提供一个界面，贡献的翻译可以由文档开发者进行审核和提交。

## [嵌入式平台](https://www.freebsd.org/status/report-2013-09-devsummit.html#Embedded-Platforms)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=Embedded-devsummit-201309.pdf)      |
| [笔记](https://wiki.freebsd.org/201309DevSummit/Embedded)      |
| [剑桥笔记](https://wiki.freebsd.org/201308DevSummit/Embedded)      |

联系人：Warner Losh <[imp@FreeBSD.org](mailto:imp@FreeBSD.org)>  
联系人：Brooks Davis <[brooks@FreeBSD.org](mailto:brooks@FreeBSD.org)>

嵌入式平台的讨论开始于一个月前的剑桥，在那里，BrilliantService 公司展示了他们为头戴式增强现实显示器开发的 Viking 操作系统。接下来，我们讨论了开发板启动和与之相关的内核最小化问题。随后，围绕系统镜像创建以及如何使一些嵌入式平台成为一级平台展开了长时间的讨论。最后，我们讨论了电源管理。

关于嵌入式平台（特别是树莓派）的一级架构状态讨论确定了实现这一目标所需的一些因素。除了驱动程序改进和稳定化工作外，我们还需要将镜像作为当前发布构建过程的部分或从中派生出来。我们还需要构建软件包（Stacey Son 正在致力于使 ARM 和 MIPS64 的软件包能够构建）。此外，我们还需要某种形式的二进制更新。最初，这可能通过 freebsd-update(8) 来完成，但从长远来看，这可能过于缓慢，无法实际应用。该话题的进一步讨论是 EuroBSDCon 开发者峰会的一个主要议题。

电源管理的讨论范围很广，最终得出结论，我们确实需要更好的电源管理基础设施，但我们不完全清楚其具体形式。我们确实需要某种方式来表示电源管理总线/设备树，这些与我们设备基础设施中的传统附件模型不同。我们还需要更智能的调度，以便能够做一些事情，比如将所有中断引导到某些核心，从而使它们可以完全关闭。

在马耳他，我们讨论的第一个话题是尽力为外部工具链支持设定更好的目标和使用场景，以便在 FreeBSD 11 发布时，任何支持的架构都可以通过外部工具链进行构建。我们讨论了为没有本地工具链支持的架构在基于 QEMU 的软件包构建基础设施中工作的不同方法。到了 FreeBSD 11，我们还希望确保所有内容都文档化清晰，以便用户知道在给定平台上支持和不支持的内容。

接下来，我们就 Alfred Perlstein 最近做的自动调优更改进行了长时间的讨论。对于内存大于一 GB 的机器，这些更改非常好，但对于几乎没有内存的机器则效果不佳，因此 Adrian Chadd 自愿修复这一问题（详情请参见幻灯片）。

我们讨论了很多关于 FreeBSD 11 中 ARM 移植的内容，并为该领域设定了一些目标。以下是一些亮点：我们希望能够在任何 armv6 平台上启动一个内核——目前有一些技术障碍。我们希望在 11 版本中继续支持 armv4 和 armv5，直到有特别的理由不再支持它们。由于我们正在转向 Clang，外部工具链问题可能是最大的任务之一。此外，armv6 将增加硬件浮点支持，我们希望能够实现对称多处理（SMP）。我们还广泛讨论了发布工程中的一些任务：我们需要为流行的开发板（如 Raspberry Pi 和 BeagleBoard）提供镜像。在 10.1 版本发布时，我们希望在这方面取得一些进展。我们希望为 ARM 和 MIPS 构建软件包，并为 freebsd-update(8) 设置基础设施。还简要提到，目前 ARM 上没有良好的 GPU 支持，这一问题存在于 FreeBSD 端。我们需要制定一个尽可能少有缺点的策略，可能的方案是采用 Android ABI，并允许将 Android 的二进制文件直接使用。这方面存在不少挑战。

此外，我们还讨论了 MIPS 和各种 FDT 问题。后者的关键问题是我们需要更好的时钟和电源支持，并且这些功能与设备树中的分离领域相关，必须单独处理。此外，不同版本之间的 GPIO 和 pinmux 不一致，我们需要解决这个问题。我们还讨论了 Arm64，在这一领域有很多工作要做。关键是要找出（在 FreeBSD 基金会的帮助下）谁对 Arm64 感兴趣，并与他们合作。由于基金会拥有与最大消费者相关的联系人和 NDA，因此它们可能处于推动这一工作的最佳位置。与 Semihalf 公司和峰会上的 ARM 代表 Andrew Wafaa 一起，我们得出结论，Arm64 的支持离我们目前在内核中支持的功能并不遥远。事实证明，这主要是关于如何组织源代码树和一些类似的细微问题。



## [网络](https://www.freebsd.org/status/report-2013-09-devsummit.html#Networking)

| 链接 |
| ----- |
| [笔记](https://wiki.freebsd.org/201309DevSummit/Networking)      |

联系人：Lawrence Stewart <[lstewart@FreeBSD.org](mailto:lstewart@FreeBSD.org)>  
联系人：Gleb Smirnoff <[glebius@FreeBSD.org](mailto:glebius@FreeBSD.org)>

André Oppermann 汇报了他目前在网络堆栈与驱动程序之间接口的工作。他计划发布一份关于堆栈 - 驱动边界的正式文档，并将 ifnet 结构分成由堆栈和驱动各自拥有的部分。所有驱动程序将根据这一新秩序进行调整，相关的反馈征求将发布到相应的邮件列表。此更改正在项目的 projects/ifq Subversion 分支中实施，由 FreeBSD 基金会赞助的 Ed Maste 监督。André 即将完成他的 TCP-AO 工作，并正在将 IPsec 代码迁移到基于 pfil(9) 的内核模块中。Gleb Smirnoff 提出了实现轻量级引用计数以避免悬挂指针的问题，Alexander Chernikov 开始讨论路由性能。

网络堆栈工作组的另一个亮点是关于测试的讨论，大家一致认为开发人员应该与能够测试不同工作负载性能的公司进行沟通。Olivier Cochard-Labbé（来自 Orange）和 Alexander Chernikov（来自 Yandex）已经表示对这一工作的兴趣，而奈飞的员工（Lawrence Stewart、Adrian Chadd 和 Scott Long）确认他们可以访问一个以 TCP 为主的生产工作负载。相关地，还提到奈飞希望定期在加利福尼亚州洛斯加图斯举办专注于网络的开发者峰会。

## [ Port 与软件包](https://www.freebsd.org/status/report-2013-09-devsummit.html#Ports-and-Packages)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=20130928-eurobsdcon-ports-summary.pdf)      |
| [笔记](https://wiki.freebsd.org/201309DevSummit/Ports)      |

联系人：Erwin Lansing <[erwin@FreeBSD.org](mailto:erwin@FreeBSD.org)>

我们有一场由 Allan Jude 主讲的完整报告，简要介绍了他们为 PC-BSD CDN（内容分发网络）所做的工作。例如，它使用 rsync(1) 的 --delay-update 标志来使更新操作更具原子性，使用了许多 ZFS 功能（如复制、快照管理），并实现了自动镜像选择。这是一次相当有趣的演讲，并介绍了一些我们可以借鉴并应用于 FreeBSD 软件包分发网络的有趣想法。接下来是 Jeremy Le Hen 的演讲，他谈到了堆栈保护（SSP）。在 FreeBSD 10.x 的 amd64 和 i386 平台上，SSP 将默认启用，但可以通过 SSP_UNSAFE 开关关闭。相反，它在 9.x 版本中默认没有启用，但可以通过另一个开关 WITH_SSP_PORT 启用。这将在 amd64 上生效，对 i386 没有影响。

Baptiste Daroussin 介绍了最近提交的分阶段安装。其他所有软件包系统都已经实现了这一功能，现在我们也实现了。它带来了许多改进，比如我们可以在软件包实际安装到文件系统之前，更早地捕获打包列表错误。如果一个 Port 在构建和打包时需要 root 权限，可以使用 NEED_ROOT 开关。此外，它还简化了构建工厂中使用的大多数逻辑，因为许多检查可以通过这种方式自动化，从而捕捉到损坏的 plist 并帮助消除特殊的后安装脚本。它为我们未来想要添加的一些新功能奠定了基础，例如实现子软件包。拥有子软件包使得我们可以先构建软件包，将文件放入不同的小软件包中，然后单独安装它们。与所有其他选项相比，它默认是关闭的，Port 将逐个转换为这种格式——不过，最终我们可能会说，未转换为支持分阶段的 Port 将被删除。实际上，这将帮助我们找出树中哪些 Port 不再被使用。

接下来，我们讨论了接下来的工作。我们已经讨论了软件包集至少三年，现在似乎我们终于能够实现它了。我们将尝试创建一个安全分支，并恢复 Ports 安全团队，与安全官员 Dag-Erling Smørgrav 合作。我们计划为该分支提供季度发布和每周安全更新。这是一个持续的计划，已经进行了三年，因为我们需要许多事情发生后才能继续推进，比如远离 CVS，推出新样式的二进制软件包，部署新的构建集群。我们终于得到了所有这些，实际上现在可以使用 pkg-test 设置来实现它。所以，我们希望能在 11 月初开始第一个季度发布。

我们就删除对旧版二进制软件包的支持进行了长时间的讨论，现在我们有了 pkg(8)。保持与 pkg_install(1) 的兼容性阻碍了新特性的引入，例如上面提到的子软件包。我们无法真正添加这些新特性，因为旧工具不支持它们，并且我们不能期望 Port 同时支持两种不同的软件包格式。我们不想让用户感到太多惊讶，但事实证明有一条简单的迁移路径。pkg(8) 的一个优势是它可以与各种第三方应用程序互操作，例如 puppet 和 chef。这仍然是一个 POLA（用户期望行为）违背，所以我们需要小心实际过渡的方式。我们应该给予用户很多警告，特别是在大型安装中，其中有自定义脚本来处理 Port 和软件包。切换的日期定在了六个月后，也就是 2014 年 4 月，这与 8.3-RELEASE 的生命周期结束日期非常吻合，8.3-RELEASE 是最后一个不包含 pkg(8) 的发布版本。所以，我们希望在明年的 BSDCan 上庆祝从 pkg_install(1) 切换过来的时刻。

最后，我们讨论了与软件包命名相关的问题。问题在于某些 Port 有相同的名称，并依赖于此，因此我们目前使用 LATEST_LINK 来解决这种行为。我们应该教育人们更好地利用 PKGNAMESUFFIX 来确保所有受影响的 Port 都有唯一的名称。为了鼓励这一点，我们应该设置自动化检查，以警告人们拥有相同名称的软件包。PKGNAME 必须在所有类别中唯一，因此当使用 pkg-add(8) 时，系统必须知道选择哪个软件包进行安装。这将改善选项的处理，增加软件包 flavor 并实现子软件包。

## [安全](https://www.freebsd.org/status/report-2013-09-devsummit.html#Security)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=201309+DevSummit+Security+Report.pdf)      |
| [笔记](https://wiki.freebsd.org/201309DevSummit/Security)      |

联系人：Dag-Erling Smørgrav <[des@FreeBSD.org](mailto:des@FreeBSD.org)>

在安全工作组中，我们的议程上有四项内容。首先，我们讨论了当前的 `/dev/random` 状况。有一些已知的熵收集漏洞已经被修复，例如从网络栈中提供大量零数据。我们有一个可插拔的随机生成器框架，并为其提供了一些插件，Yarrow 是其中之一，RDRAND 和 Padlock 是另外两个，我们还有一个阻塞的插件和一个崩溃的插件，以及一些编码示例等等。对于 10，我们将回溯并移除 RDRAND 和 Padlock 后端，而是将其输出传递给 Yarrow，而不是直接交付给 `/dev/random`。仍然可以通过内联汇编或在用户空间使用 OpenSSL 来直接访问硬件随机数生成器，即 RDRAND、Padlock 等，但我们不再信任它们。除此之外，我们还希望在启动过程中尽早收集更多熵，因为我们希望摆脱 initrandom 脚本，这个脚本将大部分静态数据输入到 `/dev/random`，并假装它是熵，实际上它并不是。Pawel Jakub Dawidek 提供了一个补丁，这个补丁已经在浮动，并做了一些分析，最终我们得到了相关的数据。该补丁将每个设备连接到 /dev/random 所需的时间作为输入，结果发现从每个设备中可以获得大约 4 位有效的熵。我们还应该让安装程序在新安装的系统上填充 `/entropy` 文件，这样在系统第一次启动时就能有熵源。此外，还有一个问题（尤其是在虚拟化和克隆中，这些做法变得越来越常见）是确保克隆足够快地分叉。例如，我们讨论了让安装程序生成 SSH 密钥。但问题在于，如果你安装一个虚拟机并生成了 SSH 密钥，然后将其克隆，所有实例都会拥有相同的密钥。所以，当单个虚拟机启动时，如果在启动过程中没有足够的熵收集，那么密钥就会基于安装过程中安装程序提供的熵来生成，这几乎是同样糟糕的。设备附加补丁可以帮助解决这个问题。

接下来的议题是软件包签名。我们为 10 提供了一个短期解决方案，直到开发出更专业的解决方案。在这个设计中，软件包构建者没有密钥，而是在完成后将哈希值提交给签名服务器，签名服务器返回签名。我们将把指纹与基本系统一起放在 /etc/pkg/fingerprints 中。如果需要撤销密钥或分发新密钥，我们只需要发布一个新的 FreeBSD 安全公告（这本来就应该做的），并通过 freebsd-update(8) 分发更新，将密钥从受信目录移到撤销目录，并将新密钥添加到受信目录中。启动时，pkg(8) 会查看这些目录，加载它找到的所有密钥，并接受签名至少由一个有效密钥且没有撤销密钥的包。

软件包签名之后是 Sofian Brabez 介绍的缓解措施。他已经准备好将 stackgap 优化和 mmap() 随机化包含在 10 中，但默认情况下是关闭的。Stackgap 随机化在栈顶部添加随机的空白空间，这样攻击者就不能仅仅假设应用程序的实际栈布局，防止缓冲区溢出攻击。Stackgap 随机化的问题是像 Varnish 这样的程序，拥有许多线程，因此必须使用非常小的栈空间来避免栈空间不足，这会导致栈空间不足。因为 stackgap 随机化会增加栈的大小。mmap() 随机化则在连续的映射之间插入一个随机间隙，目的是相同的。现在，栈保护（SSP）可以默认启用了。问题在于，如果默认启用，许多 Port 会出错。这是因为 GCC 在链接过程中会包含一个额外的目标文件，用于检查 canary 字，这显然干扰了某些 Port 的构建方式。现在，libc 是一个链接脚本，而不仅仅是一个 .so 文件，因此链接器将始终知道如何处理这个问题。我们还讨论了 ldbase 随机化，但尚未实现。它通过运行时链接器随机化库的加载位置。

议程上的最后一项是 VuXML 和 portaudit。我们在 VuXML 上有一些不足之处，其中之一是 portaudit 工具基于字符串匹配，这种方式不可靠，特别是当我们有重命名的 Port 或多个相同软件的不同版本时。此外，实际数据中也存在许多错误，尤其是一个常见的错误是将 `>` 错写为 `>=`。另外，审计工具没有验证基本系统的版本。我们有针对安全公告的 VuXML 条目，但由于这个原因它们没有被使用。一个原因是内核补丁级别不一定反映用户空间的补丁级别，因为 freebsd-update(8) 只在实际更新影响到内核时才更新内核补丁级别。因此，我们将开始在 Port 中包含 CPE 信息。CPE（公共平台枚举）是 NIST 的标准，用于唯一标识软件包、版本、变种，甚至是 Port 修订版。使用 CPE 的意义在于它是唯一的，并且不与 Port 名称相关联，因此我们可以有多个 Port 使用相同的 CPE，而不会产生问题。我们将把它作为注释存储在 pkg(8) 软件包中。NIST 发布的 CPE 可以直接推送到 VuXML 中，我们不再需要自己做匹配。CPE 的规范包含了一个匹配算法，并附带参考实现。FreeBSD 10 将安装一个脚本在 /libexec 下，用于打印用户空间的补丁级别，freebsd-update(8) 会更新这个脚本，这样也能验证用户空间的补丁级别。

## [工具链和构建系统](https://www.freebsd.org/status/report-2013-09-devsummit.html#Toolchain-and-Build-Systems)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=toolchain-and-build-eurobsdcon2013.pdf)      |
| [笔记](https://wiki.freebsd.org/201309DevSummit/ToolchainAndBuild)      |
| [剑桥笔记](https://wiki.freebsd.org/201308DevSummit/ToolchainAndBuild)      |
| [路线图](https://wiki.freebsd.org/GPLinBase)      |

联系人：Brooks Davis <[brooks@FreeBSD.org](mailto:brooks@FreeBSD.org)>

关于工具链和构建系统的讨论始于一个月前在剑桥的会议。在那里，主要的议题是源代码分析、替换 GCC 的进展以及如何打包基本系统的讨论。关于这些以及其他话题的笔记可以在会议页面的 Wiki 上找到。

源代码分析有多个方向。我们讨论了在源代码树中添加注释，以支持各种高级分析工具。大家普遍认为，如果这些注释过时，可能会带来一些负面影响，但只要这些注释经过验证，它们是有用的。大多数提议的注释都需要某种 LLVM 支持，因此我们讨论了将 LLVM 分析集成到构建框架中的过程。我们还讨论了将各种分析工具作为 Tinderbox 框架的一部分来运行的想法。

在替换 GCC 的背景下，我们讨论了 David Chisnall 停止在 Clang 是默认编译器的系统上构建 GCC 和 libstdc++ 的计划（这一变化已经实施）。此外，我们计划在 11 版本之前将所有现有平台迁移到 Clang 或外部 GCC。外部工具链支持目前与 Clang 配合正常工作，但与 GCC 不兼容。

最后，Baptiste Daroussin 讨论了他关于将基本系统打包为软件包的提议，以取代当前的 tar 归档分发方式。待完成这项工作，就可以执行 freebsd-update(8) 执行的任务，包括升级和检测更改的文件，并以更友好的操作方式进行。使用 pkg(8) 替代 freebsd-update(8) 目前还不是一个通用的解决方案，因为包签名和增量支持是使其可行所必需的。

在马耳他会议上，我们讨论了两个主要议题：基本系统中非许可性（GPL 许可）软件的总体状态，以及外部工具链支持的详细讨论。我们还决定，未来的会议应讨论如何使增量构建更具实用性，并且应在未来的会议中专门召开工作组讨论内核构建系统。

会议的一半时间用于详细讲解 GPLinBase Wiki 页面（请参见链接）。有一些领域需要适量的工作，而 binutils 替换则需要较多的工作。实际上，我们相信我们在 ELF 工具链项目或 LLVM 中已经拥有大部分所需的组件，但识别这些组件并与基本系统和 Port 进行测试还需要一些时间。

接着，我们讨论了 Warner Losh 在为外部工具链基础设施添加对 GCC 支持和向 GCC 上游提交补丁的工作进展。幸运的是，我们对基本系统中 GCC 的大多数更改是 x86 现代化，这在新版本中已不再需要。实际上，我们有大约 2000 行的更改应该合并，还有几百行应添加到交叉工具链 Port 中。除了创建一个现代化的交叉 GCC 外，外部工具链支持也需要工作，因为 Clang 和 GCC 对 -B 和可能的 --sysroot 的支持存在差异。关于外部工具链支持的进一步讨论发生在嵌入式会话中。

## [USB](https://www.freebsd.org/status/report-2013-09-devsummit.html#USB)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=DevSummitUSB2013Status.pdf)      |
| [笔记](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=DevSummitUSB2013.pdf)      |

联系人：Hans-Petter Selasky <[hselasky@FreeBSD.org](mailto:hselasky@FreeBSD.org)>

在 USB 工作组中，Hans-Petter Selasky 总结了 FreeBSD 在过去一年中 USB 堆栈的变化。他提到没有出现严重的问题，同时 USB 驱动程序在设备和控制器方面都有所改进。他还指出，许多系统已经开始在 FreeBSD 内核之外使用 USB 堆栈，例如 DragonFly BSD。Hans-Petter 简要回顾了改进 USB 支持的一些想法：他希望将更多的 Linux USB 串行 Port 和以太网设备驱动程序导入到用户空间，并通过他的 webcamd(8) 守护进程进行访问；将 NDIS（以太网和无线）USB 封装移到用户空间；并通过基于 Cuse4BSD 的守护进程在字符设备级别实现 Linux USB 文件系统的仿真，也是在用户空间中。

总结之后，我们讨论了如何解决 USB 无线和以太网设备中遇到的分离问题，这是由 Adrian Chadd 提出的。此外，还讨论了一些 DWC OTG 问题，例如实现 DMA 支持的需求，并将其暴露给更多的设备速度测试，不仅仅是以太网和内存棒。



## [厂商讨论](https://www.freebsd.org/status/report-2013-09-devsummit.html#Vendor-Discussions)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=20130928-eurobsdcon-vendor-summary.pdf)      |

联系人：Erwin Lansing <[erwin@FreeBSD.org](mailto:erwin@FreeBSD.org)>

首先，Justin Gibbs 代表 FreeBSD 基金会做了一回状态更新。一个主要变化是，之前我们只有一名兼职员工，Deb Goodkin，现在我们有两名全职技术人员参与一些当前项目，例如 Kostik Belousov，他仍在努力改善我们的 X.org 支持。他们还帮助改进不同团队之间的持续性，比如发布工程团队和安全团队。我们还雇用了 Glen Barber 作为系统管理员，他与 FreeBSD 集群管理员一起监督项目的机器，并且也在帮助发布工程。Ed Maste 被聘为兼职项目经理，负责监督基金会赞助项目的进展。我们希望能让更多的人参与其中，尤其是在行政和市场营销方面。

我们还听取了 Daichi Goto 关于他在日本的公司 BSD Consulting, Inc. 的演讲。他曾为一家公司提供咨询，试图用 FreeBSD 解决问题，但公司不允许他这么做，因为他们无法获得 FreeBSD 的商业支持。因此，他成立了自己的公司，专门为此提供支持，其中包括硬件认证。

围绕我们文档和网站的现状进行了讨论，特别是在日本，许多人并不精通英语。在接下来的时间里，我们进行了长时间但富有成效的讨论，关于一些小型项目的推进，例如将更多的 Infiniband 相关的 bug 修复纳入到发布版本中。总的来说，除了安全修复，回溯大修和发布的 erratas 也很有用。然后我们讨论了 nanobsd 支持，使其对潜在用户更为显眼和可访问。接着，我们谈论了如何推广 ARM 和 MIPS 平台至一级架构，提供更多的翻译文档和推荐信，吸引新用户并与他们联系：如何撰写问题报告，如何调试内核等。与此相关，还提到了 PR 筛选，目标是对每个新提交的 bug 报告在几天内给出回复。像往常一样，Java 也在讨论之中，似乎他们正在重新考虑将 OpenJDK 作为默认版本，定于 1.8。



## [虚拟化](https://www.freebsd.org/status/report-2013-09-devsummit.html#Virtualization)

| 链接 |
| ----- |
| [摘要](https://wiki.freebsd.org/201309DevSummit?action=AttachFile&do=get&target=eurobsdcon_summary.pdf)      |
| [笔记](https://wiki.freebsd.org/201309DevSummit/Virtualization)      |

联系人：Peter Grehan <[grehan@FreeBSD.org](mailto:grehan@FreeBSD.org)>

在虚拟化工作组中，Peter Grehan 提供了一个状态报告。在 FreeBSD 10 中，过去两年间进行了大量工作，我们正在逐步将 Xen、PHVM、Hyper-V 驱动程序以及 bhyve(4) 客户支持集成到 10.0-RELEASE 中。我们简要讨论了 Neel 长期在进行的 bhyve(4) 内存过度提交工作，但我们希望它也能进入 10 版本。这项工作提供了与 FreeBSD 虚拟内存子系统的更好集成，使我们能够将客户内存分页到交换空间。我们还讨论了 bhyve(4) 未来的工作方向：我们希望逐步摆脱用户空间启动加载程序，使用 Intel 提供的 BSD 许可的 UEFI 代码作为启动 ROM；我们希望在某个时候支持更多的 Windows 客户，并获得挂起和恢复客户的能力，最终实现支持实时迁移。

## [ZFS](https://www.freebsd.org/status/report-2013-09-devsummit.html#ZFS)

| 链接 |
| ----- |

联系人：Martin Matuška <[mm@FreeBSD.org](mailto:mm@FreeBSD.org)>  
联系人：Matthew Ahrens <[mahrens@delphix.com](mailto:mahrens@delphix.com)>

首先，Justin Gibbs 对来自硬件供应商的新技术——磁道叠加介质（Shingled Media）进行了概述。我们讨论了与此相关的一些性能问题，并提出了一些简单的想法，旨在确保系统可以充分利用这一技术，或者在不删除数据而仅覆盖数据时避免性能下降。最后我们得出结论，可能很难做得比这更好。

接着，我们报告了 ZFS 在 FreeBSD 和 Illumos 之外其他平台的情况。在 Linux 上，ZFS 基本上可以正常工作，并且正在积极开发，已经集成到内核中。在 Mac OS X 上，ZFS 还很不成熟，但有很多工作正在进行中。在 Oracle Solaris 上，ZFS 仍在开发中，但我们可能永远无法看到他们的源代码。

我们讨论了创建一个通用的跨平台 ZFS 代码库，供所有平台拉取代码。其目的是所有平台都能从这个代码库中获取平台无关的代码，从而使得将更改同步到所有平台变得更容易。这个代码库不包括像 ZPL 这样的内容，因为 ZPL 需要与每个平台特定的 VFS 层对接，但这样可以减少 FreeBSD 和 Linux 中 Solaris 移植层的杂乱，同时在 Illumos 中添加一点移植层。我们讨论了如何分阶段进行这项工作，并决定从一开始就尝试包括 Linux 开发人员，而不是仅仅做 Illumos 和 FreeBSD，然后再附加 Linux 层。

接下来，我们讨论了测试覆盖率和现有的测试工具。Spectra Logic 已经完成了 STF 测试套件的移植工作，现在可以在 FreeBSD 上使用，因此我们讨论了如何让它们更广泛地使用，并可能将它们纳入主源代码树。最终，这些测试将成为独立代码库的一部分，但可能需要一段时间才能实现。

最后，我们还讨论了 zfsd，这是 FMA 的替代工具。FMA 是 Solaris 中的技术，用于处理热备份和设备替换等问题。zfsd 是在 FreeBSD 上实现的替代工具，由 Spectra Logic 实现。我们讨论了将 zfsd 纳入主代码库时遇到的一些问题，因为它使用了一些微妙的物理路径处理，尚不完全通用。
