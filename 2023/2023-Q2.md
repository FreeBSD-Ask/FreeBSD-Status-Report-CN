# FreeBSD 2023 年第二季度状态报告

- 原文：[FreeBSD Status Report Second Quarter 2023](https://www.freebsd.org/status/report-2023-04-2023-06/)

这是 2023 年第二份状态报告，共有 37 份报告。

如你所见，我们的报告数量比上季度有所增加。这是个好消息，也彰显了 FreeBSD 社区的活跃程度，以及大家始终致力于提供高质量软件的努力。

特别请注意，夏季已到，不要错过我们谷歌编程之夏学生分享的精彩项目。

祝阅读愉快。

Lorenzo Salvadore

代表状态团队敬上。

## FreeBSD 团队报告

可在 [管理页面](https://www.freebsd.org/administration/) 查阅来自各官方及半官方团队的条目。

### FreeBSD 核心团队

联系方式：FreeBSD 核心团队 [[core@FreeBSD.org](mailto:core@FreeBSD.org)

FreeBSD 核心团队是 FreeBSD 的管理机构。

#### 2023 年 5 月 开发峰会

核心团队在 5 月 17–18 日的 FreeBSD 开发者峰会上展示了动态更新。可在 [https://wiki.freebsd.org/DevSummit/202305](https://wiki.freebsd.org/DevSummit/202305) 查看演示文稿。

#### FreeBSD 14

核心团队正在与其他团队协作，确保 FreeBSD 14.0-RELEASE 拥有最高质量标准。

核心团队对 [14 版本不再支持](https://www.freebsd.org/platforms/) riscv64sf（64 位 RISC-V 软浮点）表示无异议。

#### 同 FreeBSD 基金会的会议

核心团队与 FreeBSD 基金会持续定期会面，讨论 FreeBSD 的管理、开发及后续发展。核心团队与基金会董事会及员工举行了两次会议，讨论基金会如何协助核心团队及整个项目。

#### Matrix 即时通讯方案

在 2023 年 5 月 开发峰会的核心团队动态中，其中一个主要议题是提出新的项目沟通解决方案。

目前，由集群管理员设置了测试实例 `matrix-dev.FreeBSD.org`。所有开发者可使用 Kerberos 凭证访问该实例，一些公开聊天室可通过 Matrix 的联合功能加入。请注意，此实例仅用于测试和评估，不保证备份或可用性。

核心团队仍在讨论该服务的范围和管理方式，并收集社区反馈。

#### 行为准则委员会

行为准则委员会（conduct@）目前由核心团队管理。

#### 提交权限

核心团队批准了 Christos Margiolis (christos@) 的 src 提交权限。

### FreeBSD 基金会

链接：

[FreeBSD 基金会](https://www.freebsdfoundation.org/) URL: [https://www.freebsdfoundation.org](https://www.freebsdfoundation.org/)

[技术路线图](https://freebsdfoundation.org/blog/technology-roadmap/) URL: [https://freebsdfoundation.org/blog/technology-roadmap/](https://freebsdfoundation.org/blog/technology-roadmap/)

[捐赠](https://www.freebsdfoundation.org/donate/) URL: [https://www.freebsdfoundation.org/donate/](https://www.freebsdfoundation.org/donate/)

[基金会合作计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/) URL: [https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)

[FreeBSD 期刊](https://www.freebsdfoundation.org/journal/) URL: [https://www.freebsdfoundation.org/journal/](https://www.freebsdfoundation.org/journal/)

[基金会新闻与活动](https://www.freebsdfoundation.org/news-and-events/) URL: [https://www.freebsdfoundation.org/news-and-events/](https://www.freebsdfoundation.org/news-and-events/)

联系方式：Deb Goodkin [deb@FreeBSDFoundation.org](mailto:deb@FreeBSDFoundation.org)

FreeBSD 基金会是一家 501(c)(3) 非营利组织，致力于支持和推广全球的 FreeBSD 项目与社区。来自个人和企业的捐赠用于资助和管理软件开发项目、会议及开发者峰会。我们还为 FreeBSD 贡献者提供差旅补助，购买并支持硬件以改善和维护 FreeBSD 基础设施，并提供资源以提升安全性、质量保证和发布工程工作。我们发布宣传材料以推广、教育和宣传 FreeBSD 项目，促进商业供应商与 FreeBSD 开发者之间的合作，并代表 FreeBSD 项目执行合同、许可协议及其他需要具备合法主体的法律事务。

#### FreeBSD 生日快乐，三十岁了

二十三年来，我们始终自豪地支持这个非凡的操作系统及其充满活力的社区，并期待在将来的日子里继续提供支持。在本次进展中，我们将概述基金会在多个领域对 FreeBSD 的贡献。内容涵盖项目开发举措，其中一些已有详细报告。此外，我们还将展示对 FreeBSD 的推广工作、促进社区参与的努力，以及拓展合作伙伴关系的进展。最后，我们将探讨为争取更多资金而开展的持续工作，从而能够投入更多资源来填补项目中的空白。

#### 筹款工作

本季度，我们在与商业 FreeBSD 用户的互动方面取得了重大进展。为了增强与现有及潜在商业用户的合作关系，我们聘请了 Greg Wallace 担任合作与研究总监。他的主要目标是扩大与商业用户的合作。从就任以来，Greg 就全力以赴，在一个季度内会见了众多公司。这些交流提供了宝贵的洞见，让我们了解 FreeBSD 的实际应用情况、用户面临的挑战以及项目可以改进的领域。通过了解这些方面，我们可以更明智地决定资金分配，并认识到 FreeBSD 的独特优势。此外，该职位还负责开展研究，以探索目标市场、探索 FreeBSD 的新机会，并确保我们的声音在相关讨论中被听到。关于 Greg 的目标和成就的更多细节，可参见下面的状态更新。

基金会对所有为支持我们工作的捐赠者表示衷心感谢。除了众多个人捐赠外，我们很高兴收到了 NetApp 和黑莓的大额捐赠。此外，我们还获得了 Tarsnap、iXsystems 和 LPI 对 FreeBSD 开发者峰会的赞助。这些赞助大大帮助了抵消开支，并使我们能够为参会者提供可承受的注册费用。

今年我们的预算约为 2,230,000 美元，其中包括对 FreeBSD 推广和软件开发的增加支出。超过一半的预算用于直接改善 FreeBSD 和保持其安全性的工作。

通过设立专职负责合作伙伴的岗位，我们能够有效强调投资我们工作的意义，并向公司展示项目的长期可持续性。

您的支持在我们的使命中起着关键作用，我们对您对 FreeBSD 社区的承诺深表感谢。请考虑为我们 2023 年的筹款活动捐赠！[https://www.freebsdfoundation.org/donate/](https://www.freebsdfoundation.org/donate/)

对于重要的商业捐赠者，我们有 [FreeBSD 基金会合作计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)，该计划成立于 2017 年。

#### 合作伙伴计划

大家好，我是 Greg Wallace。今年四月初，我加入基金会，担任合作与研究总监。[这篇博客介绍了我和这个职位](https://freebsdfoundation.org/blog/freebsd-foundation-welcomes-new-team-members/)。在合作方面，我专注于与使用 FreeBSD 的公司建立联系。我已经会见了几家公司，了解它们如何使用 FreeBSD。其中一些会谈产生了潜在合作的讨论。我会继续了解有趣的 FreeBSD 用户公司，并主动联系它们。

我的目标是与每一家使用 FreeBSD 的公司取得联系，倾听它们的故事。如果你属于此类公司且我们尚未联系，请在 [我的日程](https://calendly.com/greg-freebsdfound/30min) 上安排通话。

本季度其他合作相关活动包括：

- 我制作了 [这些幻灯片](https://docs.google.com/presentation/d/1tDCpbfxbqIucmJF6H15vK-ETrQsCMOVtxoqLem_V0Z0/edit?usp=sharing)，介绍了与基金会合作如何推动 FreeBSD 的发展。如果你对改进这些幻灯片有建议，或希望我向你的组织进行展示，请[发邮件给我](mailto:greg@freebsdfoundation.org)或[安排通话](https://calendly.com/greg-freebsdfound/30min)。欢迎随意分享此演示文稿，无论是部分还是全部内容。
- 我与基金会同事合作，为向行业分析师的演示制作了多份行业特定的使用案例幻灯片。
- 我还在寻求包括以下机构的资助机会：
  - NSF 安全与可信赖网络空间（SaTC）
  - 主权科技基金（Sovereign Tech Fund）
  - NGI

在研究方面，我的总体目标是确保社区的所有专业知识能够在全球关于计算性能、安全性和能源效率的讨论中得到体现。作为一个社区，我们有很多内容可以贡献。

到目前为止，我一直在跟踪并参与以下讨论：

- [欧洲开放论坛](https://openforumeurope.org/open-source/)
- [CHIPS 研究与开发](https://www.nist.gov/chips/research-and-development-program)

如果你有研究想法或希望在该领域合作，请[发邮件给我](mailto:greg@freebsdfoundation.org)或[安排通话](https://calendly.com/greg-freebsdfound/30min)。

#### 改进操作系统

在 2023 年第二季度，共有 339 个 src、155 个 Ports 和 20 个 doc 树提交标注 FreeBSD 基金会为赞助方。其中部分及其他基金会赞助的工作在单独报告条目中有所描述：

- [持续集成](https://www.freebsd.org/status/report-2023-04-2023-06/#_continuous_integration)
- [作为一级 cloud-init 平台的 FreeBSD](https://www.freebsd.org/status/report-2023-04-2023-06/#_freebsd_as_a_tier_1_cloud_init_platform)
- [基本系统中的 OpenSSL 3](https://www.freebsd.org/status/report-2023-04-2023-06/#_openssl_3_in_base)
- [FreeBSD 上的 OpenStack](https://www.freebsd.org/status/report-2023-04-2023-06/#_openstack_on_freebsd)
- [使用 ktrace(1) 的安全沙箱](https://www.freebsd.org/status/report-2023-04-2023-06/#_security_sandboxing_using_ktrace1)
- [amd64 SIMD 增强](https://www.freebsd.org/status/report-2023-04-2023-06/#_simd_enhancements_for_amd64)

以下是其他基金会赞助工作的示例：

- 修复 [fsck_ffs(8)(https://man.freebsd.org/cgi/man.cgi?query=fsck_ffs&sektion=8&format=html) 的 Bug
- 修复 [killpg(2)(https://man.freebsd.org/cgi/man.cgi?query=killpg&sektion=2&format=html) 的 Bug
- 改进 hwpmc
- 改进 vmm
- LLVM 16 与 OpenSSL 3.0 的 Ports 修复与解决方案
- 将 Port kinst 移植到 RISC-V 及相关 DTrace 工作
- 更新 libfido2 到版本 1.9.0
- 各类 LinuxKPI 802.11 改进
- 各类 RISC-V 改进
- 从版本 4.9.3 更新并导入 tcpdump 至版本 4.99.4

可在 [基金会项目页面](https://freebsdfoundation.org/our-work/projects/) 查看当前及以往基金会承包工作的状态。

基金会技术团队成员于 5 月 17–18 日在加拿大渥太华举行的开发者峰会上进行了展示，包括主持谷歌编程之夏、[FreeBSD 基金会](https://wiki.freebsd.org/DevSummit/202305?action=AttachFile&do=view&target=FreeBSD_Foundation_Devsummit_Spring_2023_Day_2.pdf) [技术评审](https://wiki.freebsd.org/DevSummit/202305?action=AttachFile&do=view&target=FreeBSD_Foundation_Devsummit_Spring_2023_Day_2_part1.pdf) 和 [工作流](https://docs.google.com/presentation/d/e/2PACX-1vSnEW5Z0ttQOAeqEEY8KHkfiRGeFUm4i8XrYsfY8TNYD%E2%80%94%E2%80%8Byx1P6MUu2_u-mCcpe6PMMITjeDIgT31CC/pub) 工作组会议。Pierre Pronchery 介绍了 [BSD 驱动程序协调](https://www.bsdcan.org/events/bsdcan_2023/schedule/speaker/89-pierre-pronchery/)，En-Wei Wu 讨论了与基金会合同完成的 [wtap 工作](https://www.bsdcan.org/events/bsdcan_2023/schedule/session/139-add-operating-modes-to-wtap4/)。

#### 持续集成与质量保证

基金会提供全职员工并资助项目，以改进 FreeBSD 项目的持续集成、自动化测试及整体质量保证工作。关于持续集成的工作，可在专门报告条目中阅读更多内容。

#### 宣传工作

我们的大部分工作都致力于 FreeBSD 项目的推广。这可能包括突出展示有趣的 FreeBSD 工作、制作文献和视频教程、参加活动或进行演讲。我们制作的文献旨在教授人们 FreeBSD 基础知识，并帮助他们更轻松地采纳或贡献 FreeBSD。除了参加和演讲外，我们还鼓励并协助社区成员举办自己的 FreeBSD 活动、做演讲或管理 FreeBSD 展台。

FreeBSD 基金会在全球范围内赞助许多会议、活动和峰会。这些活动可能与 BSD 相关、开源相关，或是面向弱势群体的技术活动。我们支持以 FreeBSD 为中心的活动，以提供知识分享、项目协作和促进开发者与商业用户合作的平台，从而维持健康的生态系统。我们支持非 FreeBSD 活动，以宣传和提高 FreeBSD 的认知度，增加其在不同应用中的使用，并招募更多贡献者加入项目。我们很高兴大部分活动能够回归线下参与。除了参加和策划活动，我们还在持续开展新的培训计划，并更新我们的 [使用指南](https://freebsdfoundation.org/freebsd-project/resources/)，以方便更多人尝试 FreeBSD。

以下是我们在推广和教育方面的一些工作：

- 协助组织并参加了 2023 年 5 月 17-18 日在加拿大安大略渥太华举办的 [开发者峰会](https://wiki.freebsd.org/DevSummit/202305)
- 在 2023 年 5 月 17-20 日举办的 [BSDCan](https://www.bsdcan.org/2023/) 中设立展台并赞助手提袋
  - 可在 [博客](https://freebsdfoundation.org/our-work/latest-updates/) 查看行程报告
- 在 BSDCan 庆祝项目 30 周年，提供蛋糕及特刊 [FreeBSD 期刊 30 周年纪念版](https://freebsdfoundation.org/past-issues/freebsd-30th-anniversary-special-edition/)
- 在 2023 年 7 月 13-16 日于美国俄勒冈州波特兰的 [FOSSY](https://sfconservancy.org/fossy/) 安排 FreeBSD 研讨会与讲座
- 确认对 2023 年 9 月 14-17 日在葡萄牙科英布拉举行的 [EuroBSDCon 2023](https://2023.eurobsdcon.org/) 的银级赞助
- 确认对 2023 年 10 月 15-17 日在美国北卡罗来纳州罗利举行的 [All Things Open](https://2023.allthingsopen.org/) 展位支持
- 开始规划 FreeBSD 秋季厂商峰会
- 欢迎两位 [新团队成员](https://freebsdfoundation.org/blog/freebsd-foundation-welcomes-new-team-members/)：Greg Wallace 和 Pierre Pronchery
- 发布 [4 月](https://freebsdfoundation.org/news-and-events/newsletter/freebsd-foundation-update-april-2023/) 和 [6 月](https://freebsdfoundation.org/news-and-events/newsletter/12518/) 通讯
- 通过特别视频和博客文章庆祝 [FreeBSD 日](https://freebsdfoundation.org/national-freebsd-day/) 及项目 30 周年纪念，活动日期为 6 月 19 日及当周
- 其他博客文章：
  - [EuroBSDCon 2023 差旅补助申请开启](https://freebsdfoundation.org/blog/eurobsdcon-2023-travel-grant-application-now-open/) - 注意：申请截止日期为 2023 年 8 月 2 日
  - [AsiaBSDcon 行程报告](https://freebsdfoundation.org/blog/asiabsdcon-2023-trip-report/)
- FreeBSD 新闻报道：

  - [信息世界：FreeBSD 30 周年快乐！](https://freebsdfoundation.org/news-and-events/latest-news/infoworld-happy-30th-freebsd/)

我们通过发布专业制作的 FreeBSD 期刊，帮助全球了解 FreeBSD。正如之前提到的，FreeBSD 期刊现免费发行。了解更多信息及访问最新期刊，请访问 [https://www.freebsdfoundation.org/journal/](https://www.freebsdfoundation.org/journal/)。

更多关于我们参加的活动及即将举办的活动信息，可访问 [https://www.FreeBSDfoundation.org/news-and-events/](https://www.freebsdfoundation.org/news-and-events/)。

#### 法律/FreeBSD 知识产权

基金会持有 FreeBSD 商标，并负责保护其权益。我们还为核心团队提供法律支持，以调查出现的问题。

访问 [https://www.freebsdfoundation.org](https://www.freebsdfoundation.org/) 了解更多关于我们如何支持 FreeBSD 及如何提供帮助的信息。

### FreeBSD 发布工程团队

链接：

[FreeBSD 13.2-RELEASE 时间表](https://www.freebsd.org/releases/13.2R/schedule/) URL: [https://www.freebsd.org/releases/13.2R/schedule/](https://www.freebsd.org/releases/13.2R/schedule/)

[FreeBSD 14.0-RELEASE 时间表](https://www.freebsd.org/releases/14.0R/schedule/) URL: [https://www.freebsd.org/releases/14.0R/schedule/](https://www.freebsd.org/releases/14.0R/schedule/)

[FreeBSD 发行版](https://download.freebsd.org/releases/ISO-IMAGES/) URL: [https://download.freebsd.org/releases/ISO-IMAGES/](https://download.freebsd.org/releases/ISO-IMAGES/)

[FreeBSD 开发快照](https://download.freebsd.org/snapshots/ISO-IMAGES/) URL: [https://download.freebsd.org/snapshots/ISO-IMAGES/](https://download.freebsd.org/snapshots/ISO-IMAGES/)

联系方式：FreeBSD 发布工程团队 [re@FreeBSD.org](mailto:re@FreeBSD.org)

FreeBSD 发布工程团队负责制定和公布官方项目版本的发布计划、宣布代码冻结、维护相应分支等工作。

在 2023 年第二季度，团队继续推进 13.2-RELEASE 工作。13.2 周期严格遵循预定计划，最终在四月中旬完成了三次额外 RC 构建及 RELEASE 构建和公告。

在与项目管理内各团队协调后，发布工程团队重新审视了即将到来的 14.0-RELEASE 原始计划，主要因部分工作尚在进行中。更新后的计划经过讨论和微调，以应对部分问题，并最终在 FreeBSD 项目网站上发布。新计划将 14.0-RELEASE 目标定于 2023 年 10 月。

团队继续为 `main`、`stable/13` 和 `stable/12` 分支提供每周开发快照构建。注意，今后将不再针对 `stable/12` 提供快照构建。

赞助方：Tarsnap

赞助方：FreeBSD 基金会

### 集群管理团队

链接：

[集群管理团队成员](https://www.freebsd.org/administration/#t-clusteradm) URL: [https://www.freebsd.org/administration/#t-clusteradm](https://www.freebsd.org/administration/#t-clusteradm)

联系方式：集群管理团队 [clusteradm@FreeBSD.org](mailto:clusteradm@FreeBSD.org)

FreeBSD 集群管理团队成员负责管理项目依赖的机器，用于同步其分布式工作和通信。

本季度，团队完成了以下工作：

- 定期支持 FreeBSD.org 用户账户。
- 定期维护（含替换）所有物理主机和镜像的磁盘及部件。
- 启用 FreeBSD 项目管理镜像对 [https://www.FreeBSD.org](https://www.freebsd.org/) 和 [https://docs.FreeBSD.org](https://docs.freebsd.org/) 的镜像同步。
- 集群刷新，将所有主机和 jail 升级至 14-CURRENT、13-STABLE 和 12-STABLE 的最新版本。

#### 正在进行的工作

- 主要站点的大规模网络升级
  - 新的 [Juniper](https://www.juniper.net/) 交换机已到达主站点以替换旧设备。感谢 Juniper 的捐赠。
- 更换主站点及部分镜像的旧服务器
  - 除了损坏的 CI 服务器外，还有几台旧服务器存在损坏磁盘和故障电源问题。此任务与 FreeBSD 基金会及捐助方/赞助方合作完成。
- 安装新的 CI（持续集成）机器，这些机器由包构建器重新利用。
- 审查运行在 FreeBSD 集群中的服务的备份配置。

#### FreeBSD 官方镜像概览

当前镜像位置包括：澳大利亚、巴西、德国、日本（两个完整镜像站）、马来西亚、南非、中国台湾、英国（完整镜像站）、美国—加利福尼亚、新泽西（主站）、华盛顿。

硬件及网络连接由以下机构慷慨提供：

- [Bytemark Hosting](https://www.bytemark.co.uk/)
- [BroadBand Tower, Inc 云与 SDN 实验室](https://www.bbtower.co.jp/en/corporate/)
- [國立陽明交通大學資訊工程學系](https://www.cs.nycu.edu.tw/)
- [Equinix](https://deploy.equinix.com/)
- [澳大利亚互联网协会](https://internet.asn.au/)
- [互联网系统联盟](https://www.isc.org/)
- [INX-ZA](https://www.inx.net.za/)
- [KDDI Web Communications Inc](https://www.kddi-webcommunications.co.jp/english/)
- [马来西亚研究与教育网络](https://www.mohe.gov.my/en/services/research/myren)
- [Metapeer](https://www.metapeer.com/)
- [NIC.br](https://nic.br/)
- [Your.Org](https://your.org/)
- [365 Data Centers](https://365datacenters.com/)

法兰克福单服务器镜像是欧洲主要镜像站，在带宽和使用量上居首。

我们仍在欧洲寻找额外完整镜像站（五台服务器），以替换英国完整镜像站的旧服务器。

在全球互联网交换点（澳大利亚、巴西、南非）设立单镜像的模式效果良好；如果你了解或就职于相关机构并能赞助单镜像服务器，请联系我们。美国（西海岸）和欧洲（任意地点）为优选地点。

请参阅 [通用镜像布局](https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout) 获取完整镜像站规格，以及 [tiny-mirror](https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror) 获取单镜像站信息。


### 持续集成

链接：

[FreeBSD Jenkins 实例](https://ci.freebsd.org/) URL: [https://ci.FreeBSD.org](https://ci.freebsd.org/)

[FreeBSD CI 构建产物归档](https://artifact.ci.freebsd.org/) URL: [https://artifact.ci.FreeBSD.org](https://artifact.ci.freebsd.org/)

[FreeBSD Jenkins wiki](https://wiki.freebsd.org/Jenkins) URL: [https://wiki.FreeBSD.org/Jenkins](https://wiki.freebsd.org/Jenkins)

[托管 CI wiki](https://wiki.freebsd.org/HostedCI) URL: [https://wiki.FreeBSD.org/HostedCI](https://wiki.freebsd.org/HostedCI)

[第三方软件 CI](https://wiki.freebsd.org/3rdPartySoftwareCI) URL: [https://wiki.FreeBSD.org/3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI)

[与 freebsd-testing@ 相关的工单](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals) URL: [https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=*open*&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)

[FreeBSD CI 仓库](https://github.com/freebsd/freebsd-ci) URL: [https://github.com/freebsd/freebsd-ci](https://github.com/freebsd/freebsd-ci)

[dev-ci 邮件列表](https://lists.freebsd.org/subscription/dev-ci) URL: [https://lists.FreeBSD.org/subscription/dev-ci](https://lists.freebsd.org/subscription/dev-ci)

联系方式：Jenkins 管理员 [jenkins-admin@FreeBSD.org](mailto:jenkins-admin@FreeBSD.org)

联系方式：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

联系方式：[freebsd-testing 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-testing)

联系方式：EFNet IRC #freebsd-ci 频道

在 2023 年第二季度，我们与项目贡献者和开发者合作，满足其测试需求。同时，我们也与外部项目和公司合作，通过在 FreeBSD 上进行更多测试来提升他们的产品质量。

已完成的重要任务：

- 新增 [FreeBSD-stable-13-amd64-gcc12_build](https://ci.freebsd.org/job/FreeBSD-stable-13-amd64-gcc12_build/) 作业。
- main 和 stable/13 分支的构建环境已更新到 13.2-RELEASE，stable/12 分支更新为 12.4-RELEASE。
- 使用 gcc12 的 *-build 作业已将失败报告发送至 [dev-ci 邮件列表](https://lists.freebsd.org/subscription/dev-ci)。
- 在 [BSDCan 2023 开发者峰会](https://wiki.freebsd.org/DevSummit/202305) 上展示 Testing/CI 状态更新。

正在进行的任务：

- 设计并实现 pre-commit CI 构建和测试（支持 [workflow 工作组](https://gitlab.com/bsdimp/freebsd-workflow)）
- 设计并实现使用 CI 集群构建发行产物（如发布工程操作）
- 简化贡献者和开发者的 CI/测试环境配置
- 设置 CI 阶段环境并运行实验性作业
- 整理 freebsd-ci 仓库脚本，为合并到 src 仓库做准备
- 改进硬件测试实验室并增加测试硬件
- 合并 [D38815](https://reviews.freebsd.org/D38815)
- 合并 [D36257](https://reviews.freebsd.org/D36257)

开放或排队任务：

- 收集并整理 [CI 任务和想法](https://hackmd.io/@FreeBSD-CI/freebsd-ci-todo)
- 为运行测试的虚拟机提供公共网络访问
- 使用裸机硬件运行测试套件
- 为 -CURRENT 构建 drm ports 测试
- 计划运行 ztest 测试
- 帮助更多软件在其 CI 流程中支持 FreeBSD（Wiki 页面：[3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI)、[HostedCI](https://wiki.freebsd.org/HostedCI)）
- 与托管 CI 提供商合作，提升 FreeBSD 支持

更多 WIP 信息请参见 [freebsd-testing@ 相关工单](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)，欢迎加入我们的工作！

赞助方：FreeBSD 基金会

### Ports

链接：

[关于 FreeBSD Ports](https://www.freebsd.org/ports/) URL: [https://www.FreeBSD.org/ports/](https://www.freebsd.org/ports/)

[Ports 贡献指南](https://docs.freebsd.org/en/articles/contributing/#ports-contributing) URL: [https://docs.freebsd.org/en/articles/contributing/#ports-contributing](https://docs.freebsd.org/en/articles/contributing/#ports-contributing)

[FreeBSD Ports 监控](http://portsmon.freebsd.org/) URL: [http://portsmon.freebsd.org/](http://portsmon.freebsd.org/)

[Ports 管理团队](https://www.freebsd.org/portmgr/) URL: [https://www.freebsd.org/portmgr/](https://www.freebsd.org/portmgr/)

[Ports 压缩包](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/) URL: [http://ftp.freebsd.org/pub/FreeBSD/ports/ports/](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/)

联系方式：René Ladan [portmgr-secretary@FreeBSD.org](mailto:portmgr-secretary@FreeBSD.org)

联系方式：FreeBSD Ports 管理团队 [portmgr@FreeBSD.org](mailto:portmgr@FreeBSD.org)

Ports 管理团队负责把控 Ports 的整体方向、构建包以及人员事务。本季度工作情况如下：

当前 Ports 中共有 34,400 余款 port。现有 3,019 个开放的 ports PR，其中 746 个尚未分配。本季度 `main` 分支由 151 名提交者完成 10,439 次提交，`2023Q2` 分支由 55 名提交者完成 745 次提交。与上一季度相比，ports 数量略有增加，开放 PR 数量略有减少，ports 提交数量有所增加。

本季度，我们欢迎 Tom Judge（tj@）回归，同时告别 Steve Wills（swills@），Steve 也曾是 portmgr 成员。作为 portmgr 潜水者项目的一部分，我们欢迎 Ronald Klop（ronald@）、Renato Botelho（garga@）和 Matthias Andree（mandree@）加入。

Portmgr 已恢复在源码中引入子包的工作，但仍有多项内容需要完善。

在软件方面，pkg 更新至 1.19.2，Firefox 更新至 114.0.2，Chromium 更新至 114.0.5735.198，KDE Gear 更新至 23.04.2。本季度，antoine@ 进行了 23 次 exp-run 来测试包更新，调整 CPU_MAXSIZE 至 1024，修复 devel/cmake-core 在 armv7 上的失败，并为 USES=meson 添加 `--auto-features=enabled`。最后，Ports Tree 已更新以支持 FreeBSD-CURRENT 上的 LLVM 16 和 OpenSSL 3。


### 项目

这些项目跨越多个类别，从内核和用户空间到 Ports 和第三方项目。


### Cirrus-CI

链接：
[FreeBSD Cirrus-CI 仓库](https://cirrus-ci.com/github/freebsd/) URL: [https://cirrus-ci.com/github/freebsd/](https://cirrus-ci.com/github/freebsd/)

[FreeBSD src CI](https://cirrus-ci.com/github/freebsd/freebsd-src) URL: [https://cirrus-ci.com/github/freebsd/freebsd-src](https://cirrus-ci.com/github/freebsd/freebsd-src)

[FreeBSD doc CI](https://cirrus-ci.com/github/freebsd/freebsd-doc) URL: [https://cirrus-ci.com/github/freebsd/freebsd-doc](https://cirrus-ci.com/github/freebsd/freebsd-doc)


联系方式：Brooks Davis [brooks@FreeBSD.org](mailto:brooks@FreeBSD.org)

联系方式：Ed Maste [emaste@FreeBSD.org](mailto:emaste@FreeBSD.org)

联系方式：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

Cirrus-CI 是一项托管的持续集成服务，为开源项目提供 Linux、Windows、macOS 和 FreeBSD 上的 CI 服务。它补充了我们的 Jenkins CI 基础设施，支持包括 GitHub RP 和 FreeBSD fork 测试在内的其他用例。我们在 2019 年将 Cirrus-CI 配置添加到 FreeBSD src 源码，在 2020 年添加到 doc。许多托管在 GitHub 的 FreeBSD 项目（如 drm-kmod、kyua、pkg 和 poudriere）也使用 Cirrus-CI。

Cirrus-CI 配置持续进行维护更新（迁移至最新 FreeBSD 发行镜像）。在 src tree 中，我们增加了一些额外检查，确保在需要时更新生成的文件（`make sysent` 和 `make makeman`），并检查缺失目录。我们还增加了使用 Clang/LLVM 16 工具链包进行构建的作业，与基本系统中 Clang 版本保持一致。GCC 作业现在默认在 GitHub 镜像上运行，适用于所有提交。

赞助方：美国国防高级研究计划局

赞助方：FreeBSD 基金会

### FreeBSD 内核中的 BATMAN 支持

链接：

[Wiki 页面](https://wiki.freebsd.org/SummerOfCode2023Projects/CallingTheBatmanFreeNetworksOnFreeBSD) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/CallingTheBatmanFreeNetworksOnFreeBSD](https://wiki.freebsd.org/SummerOfCode2023Projects/CallingTheBatmanFreeNetworksOnFreeBSD)

[源代码（RP)(https://github.com/obiwac/freebsd-gsoc/pull/1) URL: [https://github.com/obiwac/freebsd-gsoc/pull/1](https://github.com/obiwac/freebsd-gsoc/pull/1)

联系方式：Aymeric Wibo [obiwac@FreeBSD.org](mailto:obiwac@FreeBSD.org)

BATMAN（Better Approach to Mobile Ad-hoc Networking，即连网络优化方案）是 Freifunk 项目开发并使用的路由协议，用于（主要是无线）多跳自组网络。Freifunk 是一项由德国发起的城市级开放 WiFi 网络计划，基于网络中立性原则。BATMAN 的目标是完全去中心化协议；网络中的任何节点都无需了解或关心整个网络的拓扑结构。

该协议在 Linux 上通过内核模块 `batman-adv` 提供支持，本项目旨在将其引入 FreeBSD，包括内核模块本身，以及创建 BATMAN 网络所需的用户空间网络库和工具。

目前，接口创建及交互（Linux 和 FreeBSD 用户空间均支持）已可工作，数据包传输功能部分可用，但尚不完整。batadv 接口的支持已加入 [ifconfig(8)(https://man.freebsd.org/cgi/man.cgi?query=ifconfig&sektion=8&format=html)。

导师：[Mahdi Mokhtari](mailto:mmokhi@FreeBSD.org)

赞助方：2023 谷歌编程之夏

### 使 LinuxBoot 支持 FreeBSD

联系方式：Warner Losh [imp@bsdimp.com](mailto:imp@bsdimp.com)

链接：

[LinuxBoot 项目](https://www.linuxboot.org/) URL: [https://www.linuxboot.org/](https://www.linuxboot.org/)

[BSDCan 2023 kboot 演讲幻灯片](https://docs.google.com/presentation/d/1N5Jp6XzYWv9Z9RhhETC-e6tFkqRHvp-ldRDW_9h2JCw/edit?usp=sharing) URL: [https://docs.google.com/presentation/d/1N5Jp6XzYWv9Z9RhhETC-e6tFkqRHvp-ldRDW_9h2JCw/edit?usp=sharing](https://docs.google.com/presentation/d/1N5Jp6XzYWv9Z9RhhETC-e6tFkqRHvp-ldRDW_9h2JCw/edit?usp=sharing)

LinuxBoot 是一项旨在创建清洁、稳健、可审计且可重复的启动固件的项目。最初作为谷歌的一个特定项目，它已经发展为支持所有使用 Linux 启动最终操作系统的启动环境。许多平台现在支持该环境，有时甚至是唯一可用的启动环境。此外，一些嵌入式设备的 LinuxBoot 环境是硬编码的，难以更改，因此能够从 Linux 启动 FreeBSD 是非常有价值的。

旧的 Sony PlayStation 3 平台使用名为 `kboot` 的引导加载器从其 Linux 内核启动 FreeBSD（所有这些都早于 LinuxBoot 项目）。该代码已被大幅增补，并通过可替换的每架构插件变得通用。正常的 FreeBSD **/boot/loader** 被构建为 Linux 二进制文件，用于读取 FreeBSD 内核、模块和可调参数，将它们放入内存，就像运行在预启动环境中一样，然后使用 [kexec_load(2)(https://man.freebsd.org/cgi/man.cgi?query=kexec_load&sektion=2&format=html) 将映像加载到 Linux 内核并执行特殊重启。对于支持 UEFI 的系统，它会将 UEFI 内存表和指向 UEFI 运行时服务的指针传递给新内核。

它支持从主机文件系统、主机块设备上的任意 [loader(8)(https://man.freebsd.org/cgi/man.cgi?query=loader&sektion=8&format=html) 支持的文件系统（包括跨多个设备的 pool）、内存盘映像以及通过网络下载的文件加载数据。可任意混合使用。例如，配置覆盖可以从主机文件系统加载，而内核从专用存储（如 NVME）或 RAM 磁盘映像加载。它支持通过 stdin/stdout 运行的主机控制台，并支持显式指定路径，例如 `/dev/nvme0ns1:/boot/loader/gerbil.conf`。还支持 ZFS 启动环境，包括一次性启动功能。

现在 FreeBSD/aarch64 可以在 LinuxBoot 环境中从 Linux 启动，功能与 [loader.efi(8)(https://man.freebsd.org/cgi/man.cgi?query=loader.efi&sektion=8&format=html) 相当。为 GICv3 提供了内存布局工作补丁 ([D40902](https://reviews.freebsd.org/D40902))。

FreeBSD/amd64 支持正在进行中，约完成 80%。由于 amd64 是较早的平台，它对引导加载器提供内核所需数据的要求更多。在 BIOS 环境中，内核无法从长模式获取这些数据，因此必须由引导加载器提供。尽管 UEFI 和 ACPI 提供了获取方式，但许多数据仍需引导加载器提供。内核初始化时可能会 panic，因为尚未发现和实现所有前提条件。

PowerPC 可以构建，但其状态未知。尝试获取合适的 PlayStation 3 对作者来说过于耗时。

#### 需要帮助

1. 编写 [loader.kboot(8)(https://man.freebsd.org/cgi/man.cgi?query=loader.kboot&sektion=8&format=html) 文档，包括使用方法、镜像创建方式及当前可行的用例。
2. 完成 amd64 支持。
3. 统一 kboot 与 efi 的 elf 架构特定元数据代码，解决编译时差异和构建基础设施问题。
4. 增加 riscv64 支持。
5. PowerPC 测试（自重构开始后未测试）。
6. 编写脚本，将 EDK-II 镜像（例如从 QEMU）重新打包为带 FreeBSD Linux 内核的 linux-boot 镜像，用于 CI 测试。
7. 在 coreboot LinuxBoot 上测试。

赞助方：奈飞

### 改进内核模块 LLDB

链接：

[谷歌编程之夏 Wiki 项目](https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement](https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement)

[项目代码库](https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel) URL: [https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel](https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel)

联系方式：Sheng-Yi Hong [aokblast@FreeBSD.org](mailto:aokblast@FreeBSD.org)

FreeBSD 项目使用 LLVM 作为工具链，LLVM 自带 LLDB 调试器。用户空间调试功能已完善，但内核空间仍需改进，其中之一是 LLDB 内核模块调试功能——解析内核核心转储提供的已加载模块数据并加载模块对象。目标是为 LLDB 实现此插件，目前作为谷歌编程之夏项目进行中。

当前仍在进行调试和开发中。

赞助方：2023 谷歌编程之夏

## 用户空间

对基本系统及其程序的变更。

### 基本系统中的 OpenSSL 3

链接：

[OpenSSL 下载](https://www.openssl.org/source/) URL: [https://www.openssl.org/source/](https://www.openssl.org/source/)

[OpenSSL 3.0 发布](https://www.openssl.org/blog/blog/2021/09/07/OpenSSL3.Final/) URL: [https://www.openssl.org/blog/blog/2021/09/07/OpenSSL3.Final/](https://www.openssl.org/blog/blog/2021/09/07/OpenSSL3.Final/)

[openssl-fipsinstall](https://www.openssl.org/docs/man3.0/man1/openssl-fipsinstall.html) URL: [https://www.openssl.org/docs/man3.0/man1/openssl-fipsinstall.html](https://www.openssl.org/docs/man3.0/man1/openssl-fipsinstall.html)

联系方式：Pierre Pronchery [pierre@freebsdfoundation.org](mailto:pierre@freebsdfoundation.org)

Pierre 负责将 OpenSSL 3 导入基本系统。OpenSSL 提供了通用加密和安全通信库，是 SSL/TLS 协议的开源实现。其广泛应用于邮件、即时通讯、VoIP 和全球 Web（HTTPS）服务。Apache 和 nginx 等 Web 服务器使用 OpenSSL，其合计市场份额超过 50%，凸显 OpenSSL 在互联网基础设施中的重要性。

OpenSSL 1.1 自 2016 年 8 月发布以来，已被大多数 Linux 和 BSD 系统采用，并通过 LTS 支持。然而官方支持将在今年 9 月中旬结束，因此紧急需要采用其继任者 3.0 分支。

OpenSSL 3 完全切换至 Apache License 2.0，增加了 provider 模块概念，将过时算法隔离到 *legacy* 模块，可通过 *fips* 模块使用标准 FIPS 功能并获得认证。更新的库需要应用重新编译，部分 API 已弃用，但可显式调用旧 API 以支持过渡。FreeBSD 已配置部分库和应用请求 OpenSSL 1.1 API，以便平滑迁移至 OpenSSL 3 原生 API。

虽然更新对小块输入的性能有一定影响，但 1 KB 及以上块影响不大。FIPS provider 仍需手动步骤，FreeBSD 正在寻找默认可用的解决方案。

赞助方：FreeBSD 基金会


### Linux 兼容层更新

链接：

[Linux 兼容层状态 Wiki](https://wiki.freebsd.org/Linuxulator) URL: [https://wiki.freebsd.org/Linuxulator](https://wiki.freebsd.org/Linuxulator)

[Linux 应用状态 Wiki](https://wiki.freebsd.org/LinuxApps) URL: [https://wiki.freebsd.org/LinuxApps](https://wiki.freebsd.org/LinuxApps)

联系方式：Dmitry Chagin [dchagin@FreeBSD.org](mailto:dchagin@FreeBSD.org)

该项目旨在提升 FreeBSD 执行未修改 [linux(4)(https://man.freebsd.org/cgi/man.cgi?query=linux&sektion=4&format=html) 二进制程序的能力。

自 [cbbac5609115](https://cgit.freebsd.org/src/commit/?id=cbbac5609115) 起，实现了在 amd64 上跨信号传递保留 FPU xsave 状态，从而支持带抢占调度的现代 golang 程序。

新增功能允许在 [namei(9)([https://man.freebsd.org/cgi/man.cgi?query=namei&](https://man.freebsd.org/cgi/man.cgi?query=namei&)

### Service Jail — rc.d 服务的自动 jail

链接：

[D40369: 扩展 /usr/bin/service 以支持设置 ENV 变量](https://reviews.freebsd.org/D40369) URL: [https://reviews.freebsd.org/D40369](https://reviews.freebsd.org/D40369)

[D40370: rc.d 服务自动 jail 的基础设施](https://reviews.freebsd.org/D40370) URL: [https://reviews.freebsd.org/D40370](https://reviews.freebsd.org/D40370)

[D40371: 自动 service jail：为服务在自动 jail 中的完整功能做一些配置](https://reviews.freebsd.org/D40371) URL: [https://reviews.freebsd.org/D40371](https://reviews.freebsd.org/D40371)

联系方式：Alexander Leidinger [netchild@FreeBSD.org](mailto:netchild@FreeBSD.org)

Service jail 扩展了 [rc(8)(https://man.freebsd.org/cgi/man.cgi?query=rc&sektion=8&format=html) 系统，使 rc.d 服务可以自动被 jail。服务 jail 会继承父主机或父 jail 的文件系统，但默认使用 jail 的其他所有限制（进程可见性、受限网络访问、文件系统挂载权限、sysvipc 等）。额外配置可以允许继承父节点的 IP、sysvipc、内存页锁定，以及使用 bhyve 虚拟机监控器 ([vmm(4)(https://man.freebsd.org/cgi/man.cgi?query=vmm&sektion=4&format=html))。

例如，如果想将 `local_unbound` 放入 service jail 并可通过 IPv4 和 IPv6 访问，只需在 [rc.conf(5)(https://man.freebsd.org/cgi/man.cgi?query=rc.conf&sektion=5&format=html) 中添加：

```ini
local_unbound_svcj_options=net_basic
local_unbound_svcj=YES
```

虽然这种方式不具备使用独立文件系统和 IP/VNET 的手动 jail 的全部安全优势，但配置更加简单，同时提供了一些 jail 的安全好处，例如隐藏同一用户的其他进程。

上述链接中的补丁是对 [2019 年我所展示内容](https://lists.freebsd.org/pipermail/freebsd-jail/2019-February/003710.html) 的重写。主要区别在于引入了 ENV 变量以便更合理地追踪，这也需要修改 [service(8)(https://man.freebsd.org/cgi/man.cgi?query=service&sektion=8&format=html)。

作者计划在 `stable/14` 分支之前提交 [D40369](https://reviews.freebsd.org/D40369)。[D40370](https://reviews.freebsd.org/D40370) 和 [D40371](https://reviews.freebsd.org/D40371) 将在 14.0 发布后提交，并希望获得更多审查意见。

### 使用 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 的安全沙箱

链接：

[ktrace 分支](https://github.com/jakesfreeland/freebsd-src/tree/ff/ktrace) URL: [https://github.com/jakesfreeland/freebsd-src/tree/ff/ktrace](https://github.com/jakesfreeland/freebsd-src/tree/ff/ktrace)

联系方式：Jake Freeland [jfree@FreeBSD.org](mailto:jfree@FreeBSD.org)

#### 使用 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 进行 Capsicum 化

本报告介绍了对 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 的扩展，该扩展可记录尚未进行 Capsicum 化的程序的能力（capability）违规行为。

Capsicum 化的第一步逻辑是确定程序在哪些地方触发了能力违规。可以通过查看源码并移除与 Capsicum 不兼容的代码来解决，但这种方法既繁琐，又要求开发者熟悉所有能力模式下不允许的操作。

另一种方法是使用 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 自动发现违规行为。[ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 工具可以记录指定进程的内核活动。Capsicum 违规发生在内核内部，因此 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 可通过 `-t p` 选项记录并返回程序违规的额外信息。

传统上，程序必须进入能力模式才能报告违规。当调用受限系统调用时，它会失败并返回 `ECAPMODE: Not permitted in capability mode`。如果开发者在做错误检查，程序很可能因此终止。这使得违规追踪不太方便，因为 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 只能报告第一个能力违规，之后程序就会结束。

幸运的是，新的 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 扩展可以在程序 **未** 进入能力模式时记录违规。这意味着开发者无需修改程序即可进行能力违规追踪，程序仍能正常获取资源并执行。

#### 违规追踪示例

下面的 `cap_violate` 程序尝试触发 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 可以捕获的每一种违规行为：

```sh
# ktrace -t p ./cap_violate
# kdump
1603 ktrace   CAP   system call not allowed: execve
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   system call not allowed: readlink
1603 foo      CAP   system call not allowed: open
1603 foo      CAP   cpuset_setaffinity: restricted cpuset operation
1603 foo      CAP   openat: restricted VFS lookup: AT_FDCWD
1603 foo      CAP   openat: restricted VFS lookup: /
1603 foo      CAP   system call not allowed: bind
1603 foo      CAP   sendto: restricted address lookup: struct sockaddr { AF_INET, 0.0.0.0:5000 }
1603 foo      CAP   socket: protocol not allowed: IPPROTO_ICMP
1603 foo      CAP   kill: signal delivery not allowed: SIGCONT
1603 foo      CAP   system call not allowed: chdir
1603 foo      CAP   system call not allowed: fcntl, cmd: F_KINFO
1603 foo      CAP   operation requires CAP_WRITE, descriptor holds CAP_READ
1603 foo      CAP   attempt to increase capabilities from CAP_READ to CAP_READ,CAP_WRITE
```

前七条“system call not allowed”记录并非直接源自程序代码 `cap_violate`，而是由 FreeBSD 的 C 运行时库触发的。当你使用 `-t np` 选项同时追踪 namei 转换和能力违规时，这一点就显而易见：

```sh
# ktrace -t np ./cap_violate
# kdump
1632 ktrace   CAP   system call not allowed: execve
1632 ktrace   NAMI  "./cap_violate"
1632 ktrace   NAMI  "/libexec/ld-elf.so.1"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/etc/libmap.conf"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/usr/local/etc/libmap.d"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/var/run/ld-elf.so.hints"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/lib/libc.so.7"
1632 foo      CAP   system call not allowed: readlink
1632 foo      NAMI  "/etc/malloc.conf"
1632 foo      CAP   system call not allowed: open
1632 foo      NAMI  "/dev/pvclock"
1632 foo      CAP   cpuset_setaffinity: restricted cpuset operation
1632 foo      NAMI  "ktrace.out"
1632 foo      CAP   openat: restricted VFS lookup: AT_FDCWD
1632 foo      NAMI  "/"
1632 foo      CAP   openat: restricted VFS lookup: /
1632 foo      CAP   system call not allowed: bind
1632 foo      CAP   sendto: restricted address lookup: struct sockaddr { AF_INET, 0.0.0.0:5000 }
1632 foo      CAP   socket: protocol not allowed: IPPROTO_ICMP
1632 foo      CAP   kill: signal delivery not allowed: SIGCONT
1632 foo      CAP   system call not allowed: chdir
1632 foo      NAMI  "."
1632 foo      CAP   system call not allowed: fcntl, cmd: F_KINFO
1632 foo      CAP   operation requires CAP_WRITE, descriptor holds CAP_READ
1632 foo      CAP   attempt to increase capabilities from CAP_READ to CAP_READ,CAP_WRITE
```

实际上，能力模式总是在 C 运行时库初始化之后才会进入，因此程序永远不会触发那前七条违规记录。我们之所以看到它们，是因为 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 在程序启动前就开始记录违规信息。

这个演示清楚地表明，违规追踪并不总是完美的。它是检测受限系统调用的有用指南，但不一定完全反映程序在能力模式下的实际行为。在能力模式中，违规等同于错误；它们提示应停止执行。而违规追踪忽略了这一建议，仍然继续执行，因此可能会报告无效的违规。

下方示例追踪了工具 [unzip(1)(https://man.freebsd.org/cgi/man.cgi?query=unzip&sektion=1&format=html)（未进行 Capsicum 化）的违规情况：

```sh
# ktrace -t np unzip foo.zip
Archive:  foo.zip
creating: bar/
extracting: bar/bar.txt
creating: baz/
extracting: baz/baz.txt
# kdump
1926 ktrace   CAP   system call not allowed: execve
1926 ktrace   NAMI  "/usr/bin/unzip"
1926 ktrace   NAMI  "/libexec/ld-elf.so.1"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/etc/libmap.conf"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/local/etc/libmap.d"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/var/run/ld-elf.so.hints"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libarchive.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libarchive.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libc.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libz.so.6"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libbz2.so.4"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libbz2.so.4"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/liblzma.so.5"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/liblzma.so.5"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libbsdxml.so.4"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libprivatezstd.so.5"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libprivatezstd.so.5"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libcrypto.so.111"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libmd.so.6"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libthr.so.3"
1926 unzip    CAP   system call not allowed: readlink
1926 unzip    NAMI  "/etc/malloc.conf"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/dev/pvclock"
1926 unzip    NAMI  "foo.zip"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/etc/localtime"
1926 unzip    NAMI  "bar"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: mkdir
1926 unzip    NAMI  "bar"
1926 unzip    NAMI  "bar"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "bar/bar.txt"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "bar/bar.txt"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: mkdir
1926 unzip    NAMI  "baz"
1926 unzip    NAMI  "baz"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz/baz.txt"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz/baz.txt"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
```

对于 [unzip(1)(https://man.freebsd.org/cgi/man.cgi?query=unzip&sektion=1&format=html) 的违规追踪输出，更接近开发者第一次对自己程序进行追踪时所看到的情况。大多数程序都会链接到库。在此例中，[unzip(1)(https://man.freebsd.org/cgi/man.cgi?query=unzip&sektion=1&format=html) 链接了 [libarchive(3)(https://man.freebsd.org/cgi/man.cgi?query=libarchive&sektion=3&format=html)，这一点在追踪结果中得到了体现：

```sh
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/lib/libarchive.so.7"
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/usr/lib/libarchive.so.7"
```

[unzip(1)(https://man.freebsd.org/cgi/man.cgi?query=unzip&sektion=1&format=html) 的违规记录出现在 C 运行时违规之后：

```sh
1926 unzip    NAMI  "foo.zip"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: open
1926 unzip    NAMI  "/etc/localtime"
1926 unzip    NAMI  "bar"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: mkdir
1926 unzip    NAMI  "bar"
1926 unzip    NAMI  "bar"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "bar/bar.txt"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "bar/bar.txt"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    CAP   system call not allowed: mkdir
1926 unzip    NAMI  "baz"
1926 unzip    NAMI  "baz"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz/baz.txt"
1926 unzip    CAP   fstatat: restricted VFS lookup: AT_FDCWD
1926 unzip    NAMI  "baz/baz.txt"
1926 unzip    CAP   openat: restricted VFS lookup: AT_FDCWD
```

在这个例子中，[unzip(1)(https://man.freebsd.org/cgi/man.cgi?query=unzip&sektion=1&format=html) 正在重建压缩包中的文件结构。违规产生的原因是 `AT_FDCWD` 值在 capability 模式下不能使用。这些违规的大部分可以通过在进入 capability 模式前先打开 `AT_FDCWD`（当前目录），然后将该描述符传递给 [openat(2)(https://man.freebsd.org/cgi/man.cgi?query=openat&sektion=2&format=html)、[fstatat(2)(https://man.freebsd.org/cgi/man.cgi?query=fstatat&sektion=2&format=html) 和 [mkdirat(2)(https://man.freebsd.org/cgi/man.cgi?query=mkdirat&sektion=2&format=html) 作为相对引用来解决。

违规追踪虽然不能自动 Capsicumize 程序，但它是开发者工具箱中的另一种工具。使用 [ktrace(1)(https://man.freebsd.org/cgi/man.cgi?query=ktrace&sektion=1&format=html) 对程序进行追踪只需几秒钟，结果几乎总是 Capsicum 沙箱化程序的良好起点。

赞助方：FreeBSD 基金会

### NVMe-oF（NoF，基于 Fabrics 的 NVMe）

链接：

[nvmf2 分支](https://github.com/bsdjhb/freebsd/tree/nvmf2) URL: [https://github.com/bsdjhb/freebsd/tree/nvmf2](https://github.com/bsdjhb/freebsd/tree/nvmf2)

联系人：John Baldwin [jhb@FreeBSD.org](mailto:jhb@FreeBSD.org)

NVMe-oF 能通过网络 fabric 使用 NVMe 协议与存储设备通信。这类似于使用 iSCSI 通过网络导出存储设备。

目前 NVMe-oF 定义了 Fibre Channel、RDMA 和 TCP 的网络传输方式。

nvmf2 分支的工作包括用户态库 (**lib/libnvmf**)，该库包含传输抽象及 TCP 传输实现。还修改了 [nvmecontrol(8)(https://man.freebsd.org/cgi/man.cgi?query=nvmecontrol&sektion=8&format=html)，添加 'discover'、'connect' 和 'disconnect' 命令来管理远程控制器连接。

分支还包含内核态的 Fabric 实现。**nvmf_transport.ko** 提供传输抽象，位于 nvmf 主机（SCSI 术语中的 initiator）与各个传输之间。**nvmf_tcp.ko** 实现 TCP 传输层。**nvmf.ko** 实现 NVMe over Fabrics host（initiator），连接远程控制器并将远程命名空间导出为磁盘设备。与 NVMe PCI-e 驱动 [nvme(4)(https://man.freebsd.org/cgi/man.cgi?query=nvme&sektion=4&format=html) 类似，命名空间通过 **/dev/nvmeXnsY** 设备导出，仅支持简单操作，同时通过 CAM 导出为 ndaX 磁盘设备。不同于 [nvme(4)(https://man.freebsd.org/cgi/man.cgi?query=nvme&sektion=4&format=html)，[nvmf(4)(https://man.freebsd.org/cgi/man.cgi?query=nvmf&sektion=4&format=html) 不支持 [nvd(4)(https://man.freebsd.org/cgi/man.cgi?query=nvd&sektion=4&format=html) 驱动。[nvmecontrol(8)(https://man.freebsd.org/cgi/man.cgi?query=nvmecontrol&sektion=8&format=html) 可用于远程命名空间和控制器，例如获取日志页、显示 identify 信息等。

需要注意的是，[nvmf(4)(https://man.freebsd.org/cgi/man.cgi?query=nvmf&sektion=4&format=html) 当前实现较简单，一些错误处理仍为待办事项 O。如果发生错误，队列（及其网络连接）会被丢弃，但设备仍保留，I/O 请求暂停。可使用 `nvmecontrol reconnect` 重新连接网络连接以恢复操作。与 iSCSI 使用持久守护进程 ([iscsid(8)(https://man.freebsd.org/cgi/man.cgi?query=iscsid&sektion=8&format=html)) 不同，重连需手动进行。

当前代码非常新，可能不够健壮，尚不适合生产环境。经验丰富且愿意承担内核 panic 导致数据丢失风险的用户，可自行测试 NVMe-oF。

下一主要任务是实现 Fabrics 控制器（SCSI 术语中的 target），可能先在用户态实现简单版本，再实现内核 offload 数据处理的“真实”版本，并与 [ctld(8)(https://man.freebsd.org/cgi/man.cgi?query=ctld&sektion=8&format=html) 集成，以便通过单个配置文件和守护进程导出 iSCSI 或 NVMe 磁盘设备。这可能需要对 ctld 进行重构，以降低 iSCSI 特定性。控制器端开发还可验证传输独立层中当前未充分测试的 API 设计。预计在此步骤完成前，不会将 NVMe over Fabrics 的更改合并到主树。

赞助方：Chelsio Communications

### 内核

更新内核子系统/功能、驱动支持、文件系统等。


### 改进启动性能

链接：

[Wiki 页面](https://wiki.freebsd.org/BootTime) URL: [https://wiki.freebsd.org/BootTime](https://wiki.freebsd.org/BootTime)

[BSDCan 演讲幻灯片](https://www.bsdcan.org/events/bsdcan_2023/sessions/session/116/slides/44/BSDCan23-Firecracker.pdf) URL: [https://www.bsdcan.org/events/bsdcan_2023/sessions/session/116/slides/44/BSDCan23-

Firecracker.pdf](https://www.bsdcan.org/events/bsdcan_2023/sessions/session/116/slides/44/BSDCan23-Firecracker.pdf)

联系人：Colin Percival [cperciva@FreeBSD.org](mailto:cperciva@FreeBSD.org)

Colin 正在协调加速 FreeBSD 启动过程的工作。

近期的工作从 EC2 转向 Firecracker 虚拟机管理器，其提供非常简化的环境；将启动流程精简到最低限度，更容易识别剩余耗时并进一步优化。

通过对 FreeBSD 和 Firecracker 的一些实验性补丁，现在可以在 20 毫秒内启动 FreeBSD 内核。

部分近期改进在 Colin 的 *Porting FreeBSD to Firecracker* BSDCan 演讲中有讨论。

赞助方：[https://www.patreon.com/cperciva](https://www.patreon.com/cperciva)

### 启动加载程序的 CI 测试平台

链接：

[FreeBSD 谷歌编程之夏 Wiki 页面](https://wiki.freebsd.org/SummerOfCode2023Projects/CITestHarnessForBootloader) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/CITestHarnessForBootloader](https://wiki.freebsd.org/SummerOfCode2023Projects/CITestHarnessForBootloader)

[GitHub 项目链接](https://github.com/mightyjoe781/freebsd-src/tree/bootloader-smk/tools/boot/bootloader_test) URL: [https://github.com/mightyjoe781/freebsd-src/tree/bootloader-smk/tools/boot/bootloader_test](https://github.com/mightyjoe781/freebsd-src/tree/bootloader-smk/tools/boot/bootloader_test)

联系人：Sudhanshu Mohan Kashyap [smk@FreeBSD.org](mailto:smk@FreeBSD.org)

FreeBSD 支持多种架构、文件系统和磁盘分区方案。该项目旨在编写 Lua 脚本，用于测试所有一、二线支持架构组合的启动加载程序，并报告任何损坏的组合和预期功能。如果时间允许，脚本还可进一步集成到现有构建基础设施（Jenkins 或 GitHub Actions），生成测试结果的综合报告。

当前，开发者的修改可能会影响操作系统在特定环境下的启动能力。这些脚本可以保证修改不会导致测试环境出现回退问题。脚本设计高效，成本远低于现有的完整的 `make universe` 测试，因此开发者可以经常使用，并能无成本地集成到 CI 流程中。

目前脚本开发进展顺利，但仍需收集各类 QEMU 配置以测试不同环境。如有可用的 FreeBSD 版本 QEMU 配置，请发送至 [smk@FreeBSD.org](mailto:smk@FreeBSD.org)。

赞助方：2023 谷歌编程之夏项目

### FreeBSD 内核物理内存压缩

链接：

[谷歌编程之夏项目 Wiki 页面](https://wiki.freebsd.org/SummerOfCode2023Projects/PhysicalMemoryAntiFragmentationMechanisms) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/PhysicalMemoryAntiFragmentationMechanisms](https://wiki.freebsd.org/SummerOfCode2023Projects/PhysicalMemoryAntiFragmentationMechanisms)

[差异修订 D40575](https://reviews.freebsd.org/D40575) URL: [https://reviews.freebsd.org/D40575](https://reviews.freebsd.org/D40575)

[差异修订 D40772](https://reviews.freebsd.org/D40772) URL: [https://reviews.freebsd.org/D40772](https://reviews.freebsd.org/D40772)

联系人：Bojan Novković [bnovkov@FreeBSD.org](mailto:bnovkov@FreeBSD.org)(%[bnovkov@FreeBSD.org](mailto:5Bbnovkov@FreeBSD.org)(mailto:bnovkov@FreeBSD.org))

现代 CPU 架构通过支持大页提升性能，但由于物理内存碎片严重，大页分配可能失败。本项目实现物理内存压缩，以在运行系统中主动减少碎片化，作为谷歌编程之夏项目的一部分，目标是在虚拟内存子系统中增加多种防碎片机制。

差异修订 [D40575](https://reviews.freebsd.org/D40575) 实现了量化物理内存碎片程度的指标。[D40772](https://reviews.freebsd.org/D40772) 实现了物理内存压缩，并添加了守护进程，用于监控系统并在需要时执行压缩。

未来计划包括设计基准测试套件、运行测试，并根据评审和测试结果调整代码。该项目仍在进行中，欢迎测试、评审和反馈。

赞助方：2023 谷歌编程之夏项目

### 提高 MAXCPU

链接：

[Review D36838: amd64: 将 MAXCPU 从 256 提升至 1024](https://reviews.freebsd.org/D36838) URL: [https://reviews.freebsd.org/D36838](https://reviews.freebsd.org/D36838)

联系人：Ed Maste [emaste@FreeBSD.org](mailto:emaste@FreeBSD.org)(%[emaste@FreeBSD.org](mailto:5Bemaste@FreeBSD.org)(mailto:emaste@FreeBSD.org))

当前 amd64 和 arm64 FreeBSD 内核默认支持最多 256 个 CPU。通过设置 `MAXCPU` 内核选项，可为自定义内核增加更多核心支持。但未来 FreeBSD 14 生命周期中，更高核数的系统将越来越常见，因此计划将默认 MAXCPU 提升至 1024，以支持大核数系统“开箱即用”。

已完成的修改包括修复 `cpuset_t` 的用户态最大值为 1024，并避免使用静态 MAXCPU 大小数组，改为按需分配内存。

后续工作包括继续减少静态 MAXCPU 分配，并解决超高核数系统的可扩展性瓶颈，目标是在 FreeBSD 14 发布时提供稳定 ABI 和 KBI，支持大 CPU 数量。

赞助方：FreeBSD 基金会

### 移植 SquashFS 到 FreeBSD 内核

链接：

[Wiki 页面](https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel](https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel)

[源码](https://github.com/Mashijams/freebsd-src/tree/gsoc/squashfs) URL: [https://github.com/Mashijams/freebsd-src/tree/gsoc/squashfs](https://github.com/Mashijams/freebsd-src/tree/gsoc/squashfs)

联系人：Raghav Sharma [raghav@FreeBSD.org](mailto:raghav@FreeBSD.org)

SquashFS 是一种只读文件系统，可高效压缩整个文件系统或单个目录，自 2009 年起 Linux 内核内置支持，在嵌入式 Linux 中广泛使用。该项目目标是为 FreeBSD 内核增加 SquashFS 支持，使其能够从内存中的 SquashFS 文件系统启动。

当前驱动兼容 FreeBSD 13.2，能正确解析 SquashFS 磁盘文件，并支持 [mount(8)(https://man.freebsd.org/cgi/man.cgi?query=mount&sektion=8&format=html)。该驱动支持多种压缩方式（zstd、lzo2、zlib 等），与 Linux SquashFS 兼容。

未来计划包括添加目录、文件、扩展属性和符号链接的读取支持。项目仍在进行中，由 [Chuck Tuffli](mailto:chuck@FreeBSD.org) 指导，预计在谷歌编程之夏项目结束前完成。

赞助方：2023 谷歌编程之夏项目

### 改进 Pf

链接：

[D40911](https://reviews.freebsd.org/D40911) URL: [https://reviews.freebsd.org/D40911](https://reviews.freebsd.org/D40911)

[D40861](https://reviews.freebsd.org/D40861) URL: [https://reviews.freebsd.org/D40861](https://reviews.freebsd.org/D40861)

[D40862](https://reviews.freebsd.org/D40862) URL: [https://reviews.freebsd.org/D40862](https://reviews.freebsd.org/D40862)

[D40863](https://reviews.freebsd.org/D40863) URL: [https://reviews.freebsd.org/D40863](https://reviews.freebsd.org/D40863)

[D40864](https://reviews.freebsd.org/D40864) URL: [https://reviews.freebsd.org/D40864](https://reviews.freebsd.org/D40864)

[D40865](https://reviews.freebsd.org/D40865) URL: [https://reviews.freebsd.org/D40865](https://reviews.freebsd.org/D40865)

[D40866](https://reviews.freebsd.org/D40866) URL: [https://reviews.freebsd.org/D40866](https://reviews.freebsd.org/D40866)

[D40867](https://reviews.freebsd.org/D40867) URL: [https://reviews.freebsd.org/D40867](https://reviews.freebsd.org/D40867)

[D40868](https://reviews.freebsd.org/D40868) URL: [https://reviews.freebsd.org/D40868](https://reviews.freebsd.org/D40868)

[D40869](https://reviews.freebsd.org/D40869) URL: [https://reviews.freebsd.org/D40869](https://reviews.freebsd.org/D40869)

[D40870](https://reviews.freebsd.org/D40870) URL: [https://reviews.freebsd.org/D40870](https://reviews.freebsd.org/D40870)

联系人：Kajetan Staszkiewicz [vegeta@tuxpowered.net](mailto:vegeta@tuxpowered.net)

联系人：Naman Sood [naman@freebsdfoundation.org](mailto:naman@freebsdfoundation.org)

联系人：Kristof Provost [kp@FreeBSD.org](mailto:kp@FreeBSD.org)

[pf(4)(https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&format=html) 是 FreeBSD 中的防火墙之一，也是最流行的防火墙之一，由 OpenBSD 项目创建并移植到 FreeBSD。

#### 回溯 OpenBSD 语法

Kajetan 引入了 OpenBSD 风格的“scrub”操作语法，可用于“match”和“pass”规则。现有规则仍受支持，但现在也支持 OpenBSD 风格的“scrub”配置。

#### pfsync 协议版本控制

现在可以配置 [pfsync(4)(https://man.freebsd.org/cgi/man.cgi?query=pfsync&sektion=4&format=html) 的协议版本，能在不同内核版本之间进行状态同步的同时进行协议更改，从而支持新功能。

#### pfsync: IPv6 传输

现在也可以通过 IPv6 传输 pfsync 流量。该功能由 Naman 完成 Luiz Amaral 开始的工作。

#### SCTP

pf 正在进行对 SCTP 的支持，包括端口号过滤、状态跟踪、pfsync 故障切换以及对被拒绝连接返回 ABORT 数据块。

赞助方：InnoGames GmbH

赞助方：Orange Business Services

赞助方：FreeBSD 基金会

### 网络接口 API（IfAPI）

链接：

[原项目页面](https://wiki.freebsd.org/projects/ifnet) URL: [https://wiki.freebsd.org/projects/ifnet](https://wiki.freebsd.org/projects/ifnet)

联系人：Justin Hibbits [jhibbits@FreeBSD.org](mailto:jhibbits@FreeBSD.org)

IfAPI（前身为 DrvAPI）始于 2014 年，目标是隐藏 [ifnet(9)(https://man.freebsd.org/cgi/man.cgi?query=ifnet&sektion=9&format=html) 结构，使网络驱动通过访问器函数访问成员，从而无需重新编译驱动即可更改网络栈，并可能允许单个驱动支持多个 FreeBSD 版本。

该目标已在基本系统中实现，但仍需更新一些 ports 以使用 IfAPI。可使用 **tools/ifnet/convert_ifapi.sh** 自动完成大部分转换。文档尚在编写中，但仍需协助整理 [ifnet(9)(https://man.freebsd.org/cgi/man.cgi?query=ifnet&sektion=9&format=html) 的内容，目前部分信息已过时。

赞助方：Juniper Networks, Inc.

### 让 Netgraph 无锁化

链接：

[Wiki 页面](https://wiki.freebsd.org/SummerOfCode2023Projects/LocklessSynchronizationBetweenNodesInNetgraph) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/LocklessSynchronizationBetweenNodesInNetgraph](https://wiki.freebsd.org/SummerOfCode2023Projects/LocklessSynchronizationBetweenNodesInNetgraph)

[代码仓库](https://github.com/zinh88/epoch-netgraph) URL: [https://github.com/zinh88/epoch-netgraph](https://github.com/zinh88/epoch-netgraph)

联系人：Zain Khan [zain@FreeBSD.org](mailto:zain@FreeBSD.org)

Netgraph 通过将内核对象（节点）组织为图并使用 hook 连接，实现自定义或复杂网络功能。节点可对输入数据包执行操作，并将输出发送给其他节点。在 SMP 前的环境中，线程总能立即调用节点函数，但并发引入了节点忙碌的可能性，同时数据包路径可能因节点或 hook 被移除而引用已释放对象。

现有代码通过拓扑读写互斥锁防止结构重组导致的问题。项目目标是恢复类似单线程时的流畅数据流，使数据在重组事件中无需等待，同时保证内核安全。

FreeBSD 提供了基于 Epoch 的并发安全数据结构和机制，该项目利用 Epoch 实现安全回收。由于修改基本系统，还会影响消息队列、引用计数等设计。

项目涉及大量测试，目前只移除了部分拓扑保护锁并在 VM 上测试简单图，硬件测试将在 4 核以上系统进行。

赞助方：2023 谷歌编程之夏项目


### 架构

更新平台特定功能并支持新硬件平台。

### amd64 SIMD 增强

链接：

[SIMD 调度框架草案](https://reviews.freebsd.org/D40693) URL: [https://reviews.freebsd.org/D40693](https://reviews.freebsd.org/D40693)

[项目提案](http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt) URL: [http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt](http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt)

联系人：Robert Clausecker [clausecker@FreeBSD.org](mailto:clausecker@FreeBSD.org)

SIMD 指令集（如 SSE、AVX、NEON）在现代计算机中广泛使用，可为许多应用提供性能优势。本项目旨在提供常用 libc 函数（主要为 [string(3)(https://man.freebsd.org/cgi/man.cgi?query=string&sektion=3&format=html)）的 SIMD 加速版本，加速大部分 C 程序。

每个函数将提供最多四个实现：

- **标量**：为 amd64 优化，但不使用 SIMD
- **基线**：使用 SSE 和 SSE2，或 **x86-64-v2** 实现，使用 SSE4.2 前所有扩展
- **x86-64-v3**：使用 AVX 和 AVX2
- **x86-64-v4**：使用 AVX-512F/BW/CD/DQ

用户可通过设置 `AMD64_ARCHLEVEL` 环境变量选择 SIMD 增强级别。

当前项目仅针对 amd64，但未来可能扩展至 arm64 等架构。

赞助方：FreeBSD 基金会

### 将 mfsBSD 集成到发布构建工具中

链接：

[Wiki 文章](https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools](https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools)

[项目仓库（integrate-mfsBSD-building 分支)(https://github.com/soobinrho/freebsd-src/tree/integrate-mfsBSD-building) URL: [https://github.com/soobinrho/freebsd-src/tree/integrate-mfsBSD-building](https://github.com/soobinrho/freebsd-src/tree/integrate-mfsBSD-building)

联系人：Soobin Rho [soobinrho@FreeBSD.org](mailto:soobinrho@FreeBSD.org)

#### 什么是 mfsBSD？

“mfsBSD 是一套工具，用于创建小型但功能完整的基于 mfsroot 的 FreeBSD 发行版，将所有文件存储在内存（MFS，Memory File System）中，并可从硬盘、USB 存储设备或光盘加载。它可用于无盘系统、恢复分区以及远程覆盖其他操作系统等多种用途。”

[Martin Matuska](mailto:mm@FreeBSD.org) 是 [mfsBSD 白皮书](https://people.freebsd.org/~mm/mfsbsd/mfsbsd.pdf) 的作者，同时也是 [mfsBSD 仓库](https://github.com/mmatuska/mfsbsd) 的维护者。

#### 目标

本项目在 src/release makefile 中为 -current 和 -stable 版本的 mfsBSD 镜像创建每周快照的额外目标。目前仅生成发布版本的 mfsBSD 镜像，这可能导致其与基础工具不同步。本项目旨在解决这一问题。

#### 时间与地点

这是 2023 谷歌编程之夏项目，官方编码周期为 2023 年 5 月 29 日至 2023 年 8 月 28 日。作为开源社区的新手，作者欢迎在项目仓库中提供所有评论、建议或 RP，期间所有代码均在此维护。

导师：[Juraj Lutter](mailto:otis@FreeBSD.org) 和 [Joseph Mingone](mailto:jrm@FreeBSD.org)

赞助方：2023 谷歌编程之夏项目

## 云计算

更新云相关功能并支持新云平台。

### 作为 cloud-init 一级平台的 FreeBSD

链接：

[cloud-init 官网](https://cloud-init.io/) URL: [https://cloud-init.io/](https://cloud-init.io/)

[cloud-init 文档](https://cloudinit.readthedocs.io/en/latest/) URL: [https://cloudinit.readthedocs.io/en/latest/](https://cloudinit.readthedocs.io/en/latest/)

[cloud-init 持续重构](https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst) URL: [https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst](https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst)

联系人：Mina Galić [freebsd@igalic.co](mailto:freebsd@igalic.co)

cloud-init 是云服务器的标准初始化方式，但对非 Linux 系统支持较差，FreeBSD 缺乏 cloud-init 支持阻碍了其成为一级平台。本项目旨在使 FreeBSD 的 cloud-init 支持与 Linux 持平，并计划逐步覆盖所有 BSD 系统。

本季度进展：

- 临时网络类已重写并实现平台无关，可用于多个云提供商初始化临时网络。
- cloud-init 已在 Vultr 成功测试，希望下一版本可推动 Vultr 将 FreeBSD 镜像切换为 cloud-init。
- 扩展了 BSD 的 rsyslog 支持，并为 cloud-init 的 ds-identify 添加了 rc 脚本，实现零配置启动速度大幅提升：ds-identify 首先快速猜测云提供商，cloud-init 使用该猜测而非遍历全部提供商。用户可通过删除 `/usr/local/etc/rc.d/dsidentify` 禁用，并提供自定义列表，进一步节省启动时间。

下一步计划包括继续网络重构任务，并为 FreeBSD 添加 LXD 支持，以纳入 CI 测试，这涉及 [LXD](https://github.com/canonical/lxd/pull/11761) 和 [FreeBSD virtio 子系统](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=271793) 的工作。

欢迎早期测试者访问 [net/cloud-init-devel](https://cgit.freebsd.org/ports/tree/net/cloud-init-devel/) 并报告 bug。自上次报告以来，cloud-init 的 bug 跟踪已从 Launchpad 转移到 GitHub。

赞助方：FreeBSD 基金会

### FreeBSD 上的 OpenStack

链接：

[OpenStack](https://www.openstack.org/) URL: [https://www.openstack.org/](https://www.openstack.org/)

[FreeBSD 上的 OpenStack](https://github.com/openstack-on-freebsd) URL: [https://github.com/openstack-on-freebsd](https://github.com/openstack-on-freebsd)

联系人：Chih-Hsin Chang [starbops@hey.com](mailto:starbops@hey.com)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

项目目标是移植 OpenStack 核心组件（如 keystone、nova、neutron），使 FreeBSD 可作为 OpenStack 主机。

本季度成果：

- 移植 `nova-novncproxy` 和 `nova-serialproxy`，增加实例控制台访问方式
- 将开发环境从物理机迁移至虚拟机
- 解决实例内部网络连接问题
- 可启动多个实例
- 从 Python 3.8 移植至 3.9

下季度计划继续优化控制台代理服务，使整体流程更流畅。

POC 构建指南可在 [docs 仓库](https://github.com/openstack-on-freebsd/docs) 查阅，每个 OpenStack 组件的补丁版本均在同一 GitHub 组织下。

欢迎项目贡献者先检查文档并提供反馈。

赞助方：FreeBSD 基金会

### 在 Microsoft HyperV 与 Azure 上的 FreeBSD

链接：

[微软 Azure FreeBSD wiki](https://wiki.freebsd.org/MicrosoftAzure) URL: [https://wiki.freebsd.org/MicrosoftAzure](https://wiki.freebsd.org/MicrosoftAzure)

[微软 HyperV FreeBSD wiki](https://wiki.freebsd.org/HyperV) URL: [https://wiki.freebsd.org/HyperV](https://wiki.freebsd.org/HyperV)

联系人：微软 FreeBSD 集成服务团队 [bsdic@microsoft.com](mailto:bsdic@microsoft.com)

联系人：freebsd-cloud 邮件列表

联系人：FreeBSD Azure 发布工程团队 [releng-azure@FreeBSD.org](mailto:releng-azure@FreeBSD.org)

联系人：Wei Hu [whu@FreeBSD.org](mailto:whu@FreeBSD.org)

联系人：Souradeep Chakrabarti [schakrabarti@microsoft.com](mailto:schakrabarti@microsoft.com)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

本季度工作重点为 ARM64 架构支持及向 [Azure community gallery](https://learn.microsoft.com/azure/virtual-machines/share-gallery-community) 构建和发布镜像。测试镜像示例：

- FreeBSD-CURRENT-testing
- FreeBSD-CURRENT-gen2-testing
- FreeBSD-CURRENT-arm64-testing

使用方法：创建虚拟机时，在“Select an Image”步骤选择“Community Images (PREVIEW)”并搜索 `FreeBSD`。

进行中的任务：

- 自动化镜像构建与发布并合并到 src/release/
- 构建和发布基于 ZFS 的 Azure Marketplace 镜像（已合并到 main，可通过 `VMFS=zfs` 创建）
- 构建并发布 Hyper-V gen2 VM 镜像至 Azure Marketplace
- 构建并发布快照版本至 Azure community gallery

上述任务由 FreeBSD 基金会赞助，微软提供部分资源。

微软的 Wei Hu 与 Souradeep Chakrabarti 承担以下任务：

- 将 Hyper-V 客户端支持移植至 aarch64

  - [Bug 267654](https://bugs.freebsd.org/267654)
  - [Bug 272461](https://bugs.freebsd.org/272461)

待完成任务：

- 更新微软 Learn 上 FreeBSD 相关文档
- 支持 [Azure Pipelines](https://azure.microsoft.com/products/devops/pipelines/) 的 FreeBSD
- 更新 [Azure agent port](https://www.freshports.org/sysutils/azure-agent) 至最新版本
- 回溯 [Azure agent 本地修改](https://github.com/Azure/WALinuxAgent/pull/1892)

赞助方：微软（针对 Microsoft 团队人员及资源）

赞助方：FreeBSD 基金会（其余任务）

### EC2 上的 FreeBSD

链接：
[FreeBSD/EC2 Patreon](https://www.patreon.com/cperciva) URL: [https://www.patreon.com/cperciva](https://www.patreon.com/cperciva)

联系人：Colin Percival [cperciva@FreeBSD.org](mailto:cperciva@FreeBSD.org)

可在 x86（Intel 与 AMD）和 ARM64（Graviton）EC2 实例上运行 FreeBSD。工作仍在继续，以确保新发布的实例类型能够得到支持，包括最近宣布的 M7a“EPYC”实例，这些实例将在 FreeBSD 14.0-RELEASE 中获得支持。

每周 FreeBSD 快照最近已从“UEFI”启动模式更改为“UEFI Preferred”启动模式，从而在支持“裸机”和“上一代”不兼容 UEFI 的实例类型的同时，享受 UEFI 带来的启动性能提升。此更改将在 FreeBSD 14.0-RELEASE 中体现。

EC2 启动脚本最近已更新以支持 IMDSv2，该更新也将在 FreeBSD 14.0-RELEASE 中生效。

若 FreeBSD 13.2 用户需要这些更新，作者可提供 FreeBSD“13.2-RELEASE plus updates”AMI。

此工作由 Colin 的 FreeBSD/EC2 Patreon 赞助。


## 文档

文档树、手册页或新外部书籍/文档中的显著变更。

### 文档工程团队

链接：

[FreeBSD 文档项目](https://www.freebsd.org/docproj/) URL: [https://www.freebsd.org/docproj](https://www.freebsd.org/docproj)

[新贡献者文档指南](https://docs.freebsd.org/en/books/fdp-primer/) URL: [https://docs.freebsd.org/en/books/fdp-primer/](https://docs.freebsd.org/en/books/fdp-primer/)

[文档工程团队](https://www.freebsd.org/administration/#t-doceng) URL: [https://www.freebsd.org/administration/#t-doceng](https://www.freebsd.org/administration/#t-doceng)

联系人：FreeBSD 文档工程团队 [doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)

文档工程团队负责处理与 FreeBSD 文档工程团队相关的元项目事务；更多信息请参见 [文档工程团队章程](https://www.freebsd.org/internal/doceng/)。

本季度：

- fernape@ 被任命为新成员
- [www/gohugo](https://cgit.freebsd.org/ports/tree/www/gohugo/) Port 维护权已转交给文档工程团队，因其是文档基础设施关键部分，该决定已与前维护者达成一致
- 改进了翻译工作流程（如下节所述）

#### Port 开发者手册

新增 [`USES=nextcloud`](https://cgit.freebsd.org/doc/commit/?id=634a34b7bb37650e4f8fcbea9fd7428b3f5b911a)。

#### FDP 指南

新增一章介绍 Weblate，用于 [新贡献者 FreeBSD 文档项目指南](https://docs.freebsd.org/en/books/fdp-primer/weblate/)。该章节详细说明加入 FreeBSD 翻译团队的步骤，包括在线 Weblate 和离线翻译，提供高效翻译、校对和测试的实用建议，并指导贡献者如何将翻译正式提交到文档仓库，实现无缝集成。

#### FreeBSD Weblate 翻译

链接：

[在 Weblate 翻译 FreeBSD](https://wiki.freebsd.org/Doc/Translation/Weblate) URL: [https://wiki.freebsd.org/Doc/Translation/Weblate](https://wiki.freebsd.org/Doc/Translation/Weblate)

[FreeBSD Weblate 实例](https://translate-dev.freebsd.org/) URL: [https://translate-dev.freebsd.org/](https://translate-dev.freebsd.org/)

##### 2023 年第二季度状态

- 支持 15 种语言
- 注册用户 183 人
- [新 Weblate 服务器](https://lists.freebsd.org/archives/freebsd-translators/2023-April/000111.html)

FreeBSD Weblate 实例现运行在专用服务器上，显著提高速度和翻译效率，特别感谢 ebrandi@ 提供硬件升级。

##### 语言进展

- 中文（简体）(zh-cn) 进度：7%
- 中文（繁体）(zh-tw) 进度：3%
- 荷兰语 (nl) 进度：1%
- 法语 (fr) 进度：1%
- 德语 (de) 进度：1%
- 印尼语 (id) 进度：1%
- 意大利语 (it) 进度：5%
- 韩语 (ko) 进度：32%
- 挪威语 (nb-no) 进度：1%
- 波斯语 (fa-ir) 进度：3%
- 波兰语 进度：1%
- 葡萄牙语 (pt-br) 进度：22%
- 僧伽罗语 (si) 进度：1%
- 西班牙语 (es) 进度：33%
- 土耳其语 (tr) 进度：2%

感谢所有参与翻译或审校文档的贡献者，也请在当地用户组中推广此工作，我们始终需要更多志愿者。

#### FreeBSD 手册工作组

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

[正在重写网络章节](https://reviews.freebsd.org/D40546)。

#### FreeBSD 网站改版 - WebApps 工作组

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

工作组负责创建新的 FreeBSD 文档门户和重新设计 FreeBSD 主网站及其组件。开发者可在 FreeBSD Slack 频道 #wg-www21 跟进并加入。工作分为四个阶段：

1. 文档门户重新设计
   创建响应式新设计，并增加全局搜索功能。（*已完成*）
2. Web 上手册页重新设计
   使用 mandoc 生成 HTML 页面脚本。（*已完成*）公共实例：[https://man-dev.FreeBSD.org](https://man-dev.freebsd.org/)
3. Web 上 Ports 页面重新设计
   Ports 脚本创建应用门户。（*进行中*）
4. FreeBSD 主网站重新设计
   新设计，响应式并支持暗色主题。（*进行中*）

## Ports

涉及 Ports 的变更，无论是影响整个树的重大变动，还是单个 Port 的更新。

### FreeBSD 上的 KDE

链接：

[KDE/FreeBSD initiative](https://freebsd.kde.org/) URL: [https://freebsd.kde.org/](https://freebsd.kde.org/)

[FreeBSD — KDE Community Wiki](https://community.kde.org/FreeBSD) URL: [https://community.kde.org/FreeBSD](https://community.kde.org/FreeBSD)

联系人：Adriaan de Groot [kde@FreeBSD.org](mailto:kde@FreeBSD.org)

FreeBSD 上的 KDE 项目为 Ports 树打包了 CMake、Qt 以及 KDE 社区的软件。这些软件包括完整的桌面环境 KDE Plasma（支持 X11 与 Wayland）以及数百款可在任意 FreeBSD 机器上使用的应用程序。

KDE 团队 (kde@) 是 desktop@ 和 x11@ 的一部分，构建软件栈，使 FreeBSD 在日常使用中成为美观且可用的图形桌面工作站。下文主要介绍 KDE 相关的 Ports，但也包括对整个桌面栈重要的项目。

#### 基础设施

更新 Qt5 Ports：

- [devel/qt5-webengine](https://cgit.freebsd.org/ports/tree/devel/qt5-webengine/) 修复了在 Clang 16 下构建的问题，为即将发布的 FreeBSD 14 做准备。
- [devel/qt5-qmake](https://cgit.freebsd.org/ports/tree/devel/qt5-qmake/) 修复了在 Qt 未安装系统上安装 qmake 会引发异常的边缘情况。

更新 Qt6 Ports：

- [devel/qt6-tools](https://cgit.freebsd.org/ports/tree/devel/qt6-tools/) 修复了在 Clang 16 下构建的问题，为 FreeBSD 14 发布做准备。

[accessibility/at-spi2-core](https://cgit.freebsd.org/ports/tree/accessibility/at-spi2-core/) Port（桌面辅助技术关键组件）已更新至 2.48.0，并改进了对非 X11 桌面的支持，提升了 Wayland 系统兼容性。感谢 Jan Beich 的贡献。

[graphics/poppler](https://cgit.freebsd.org/ports/tree/graphics/poppler/) Port（许多 PDF 查看器的基础）更新至 23.05。

[ports-mgmt/packagekit-qt](https://cgit.freebsd.org/ports/tree/ports-mgmt/packagekit-qt/) Port 新增到树中，为 FreeBSD 图形化包管理器铺路。

#### KDE 栈

KDE Gear 每季度发布，KDE Plasma 每月更新，KDE Frameworks 也每月发布新版本。上述更新在上游发布后不久即可在 Ports 中体现。

- KDE Frameworks 更新到 5.105、5.106 与 5.107
- KDE Gear 更新至 23.04.0，并随即发布 .1 与 .2 修复版本
- KDE Plasma Desktop 更新至 5.27.4，随后发布 .5 与 .6 修复版本

#### 相关 Port

弃用：

- [graphics/ikona](https://cgit.freebsd.org/ports/tree/graphics/ikona/)（Rust + Qt 图标查看器）上游已放弃
- [polish/kadu](https://cgit.freebsd.org/ports/tree/polish/kadu/)（曾在波兰流行的聊天应用）已弃用
- [sysutils/plasma5-ksysguard](https://cgit.freebsd.org/ports/tree/sysutils/plasma5-ksysguard/)（系统监控应用）上游弃用，将不再更新

更新：

- [astro/kstars](https://cgit.freebsd.org/ports/tree/astro/kstars/) 更新至 3.6.4
- [devel/qcoro](https://cgit.freebsd.org/ports/tree/devel/qcoro/) 更新至 0.9.0
- [devel/qtcreator](https://cgit.freebsd.org/ports/tree/devel/qtcreator/) 更新至 10.0.2
- [games/gcompris-qt](https://cgit.freebsd.org/ports/tree/games/gcompris-qt/) 更新至 3.2
- [graphics/kphotoalbum](https://cgit.freebsd.org/ports/tree/graphics/kphotoalbum/) 更新至 5.10.0
- [net-im/tokodon](https://cgit.freebsd.org/ports/tree/net-im/tokodon/) 加入 KDE Gear
- [textproc/kdiff3](https://cgit.freebsd.org/ports/tree/textproc/kdiff3/) 更新至 1.10.1

新软件：

- [devel/kommit](https://cgit.freebsd.org/ports/tree/devel/kommit/)（Git 客户端）新增，为 gitklient 的重命名
- [multimedia/kasts](https://cgit.freebsd.org/ports/tree/multimedia/kasts/) KDE 社区新推出的播客收听应用
- [textproc/arianna](https://cgit.freebsd.org/ports/tree/textproc/arianna/) KDE 社区新推出的移动电子书阅读器，可用于阅读 FreeBSD 文档



### FreeBSD 上的 GCC

链接：

[GCC 项目](https://gcc.gnu.org/) URL: [https://gcc.gnu.org/](https://gcc.gnu.org/)

[GCC 10 发行系列](https://gcc.gnu.org/gcc-10/) URL: [https://gcc.gnu.org/gcc-10/](https://gcc.gnu.org/gcc-10/)

[GCC 11 发行系列](https://gcc.gnu.org/gcc-11/) URL: [https://gcc.gnu.org/gcc-11/](https://gcc.gnu.org/gcc-11/)

[GCC 12 发行系列](https://gcc.gnu.org/gcc-12/) URL: [https://gcc.gnu.org/gcc-12/](https://gcc.gnu.org/gcc-12/)

[GCC 13 发行系列](https://gcc.gnu.org/gcc-13/) URL: [https://gcc.gnu.org/gcc-13/](https://gcc.gnu.org/gcc-13/)

联系人：Lorenzo Salvadore [salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)

上游发布了 [GCC 13](https://gcc.gnu.org/gcc-13)。如上次报告所述，计划从 GCC 13 第一个版本开始尝试更新 GCC_DEFAULT，因此本季度大部分工作为此做准备。

GCC 13.1（首个 GCC 13 版本）发布后，在 Ports 树中创建了两个新 Port：

- [lang/gcc13](https://cgit.freebsd.org/ports/tree/lang/gcc13/) 跟踪 GCC 13 发布
- [lang/gcc14-devel](https://cgit.freebsd.org/ports/tree/lang/gcc14-devel/) 跟踪 GCC 14 上游快照

#### *-devel Ports

启用对 .init_array 与 .fini_array 的支持。FreeBSD 自提交 [83aa9cc00c2d](https://cgit.freebsd.org/src/commit/?id=83aa9cc00c2d83d05a0efe7a1496d8aab4a153bb) 起已支持。

i386、amd64 与 aarch64 默认 bootstrap 选项已从 LTO_BOOTSTRAP 回退到 STANDARD_BOOTSTRAP：

- LTO bootstrap 在这些架构上产生过多包构建失败
- LTO_BOOTSTRAP 仍可供需要的用户使用

这些更改将向生产 Ports 推送。

#### 生产 Ports

上游已发布 GCC 13，新建 Port [lang/gcc13](https://cgit.freebsd.org/ports/tree/lang/gcc13/)。GCC 11 与 12 已更新，上游计划发布 GCC 10 新版本，所有对应 Ports 需更新。

为简化维护者和用户工作，计划同时测试并更新以下内容：

- [lang/gcc10](https://cgit.freebsd.org/ports/tree/lang/gcc10/)、[lang/gcc11](https://cgit.freebsd.org/ports/tree/lang/gcc11/)、[lang/gcc12](https://cgit.freebsd.org/ports/tree/lang/gcc12/) 更新
- 将 GCC_DEFAULT 更新为 13
- 在生产 Ports 启用 .init_array 与 .fini_array
- 将生产 Ports 的 bootstrap 从 LTO_BOOTSTRAP 切换回 STANDARD_BOOTSTRAP

优势：

- 测试次数更多但实验运行更少
- Ports 用户构建次数更少

### Puppet

链接：

[Puppet](https://puppet.com/docs/puppet/latest/puppet_index.html) URL: [https://puppet.com/docs/puppet/latest/puppet_index.html](https://puppet.com/docs/puppet/latest/puppet_index.html)

联系人：Puppet 团队 [puppet@FreeBSD.org](mailto:puppet@FreeBSD.org)

Puppet 是一款自由软件配置管理工具，由 Puppet Server 提供信任源，以领域特定语言描述机器的预期配置，Puppet Agent 在每个节点上确保实际配置与预期匹配。可选 PuppetDB 用于高级架构和配置依赖关系管理。

Puppet 团队维护 Puppet 及相关工具的 Ports。

- Puppet 8 最近发布，并已加入 Ports 树
- Puppet 6 已到达生命周期终点并弃用，建议用户升级到 Puppet 7 或 Puppet 8

目前，Puppet 7 仍为依赖 Puppet 的 Ports 默认版本。Puppet 社区正在努力确保各种模块与最新代码兼容，当前升级到 Puppet 8 可能存在挑战。随着模块更新完成，预计几个月后将 Puppet 8 设为默认版本。

### FreeBSD 上的 MITRE Caldera

链接：

[MITRE Caldera](https://caldera.mitre.org/) URL: [https://caldera.mitre.org/](https://caldera.mitre.org/)

[Red Canary](https://www.redcanary.com/) URL: [https://www.redcanary.com/](https://www.redcanary.com/)

联系人：José Alonso Cárdenas Márquez [acm@FreeBSD.org](mailto:acm@FreeBSD.org)

MITRE Caldera 是一家网络安全平台，用于轻松自动化对手模拟、辅助红队手动操作以及自动化事件响应。

它基于 MITRE ATT&CK® 框架构建，是 MITRE 的一项活跃研究项目。

MITRE Caldera ([security/caldera](https://cgit.freebsd.org/ports/tree/security/caldera/)) 于 2023 年 4 月加入 Ports 树。该 Port 支持 [Atomic Red Team Project](https://github.com/redcanaryco/atomic-red-team)，可通过 [MITRE Caldera atomic plugin](https://github.com/mitre/atomic) 使用。

该工作的主要目标是提升 FreeBSD 作为信息安全或网络安全平台的可见性。

此外，你可以使用 [https://github.com/alonsobsd/caldera-makejail](https://github.com/alonsobsd/caldera-makejail) 或 [https://github.com/AppJail-makejails/caldera](https://github.com/AppJail-makejails/caldera)（来自 [AppJail](https://github.com/DtxdF/AppJail)）轻松测试 MITRE Caldera 基础设施。AppJail 是一款便于从命令行管理 jail 容器的好工具。

欢迎有兴趣的人参与项目。

当前版本：4.2.0

#### 待办事项

- 增加 Caldera 测试基础设施 makejail
- 将 FreeBSD 添加到 MITRE Caldera 官方支持平台中，参见 [https://github.com/mitre/caldera/pull/2752](https://github.com/mitre/caldera/pull/2752)
- 将 FreeBSD 添加到 Red Canary 官方支持平台中，参见 [https://github.com/redcanaryco/atomic-red-team/pull/2450](https://github.com/redcanaryco/atomic-red-team/pull/2450)

### FreeBSD 上的 Wazuh

链接：

[Wazuh](https://www.wazuh.com/) URL: [https://www.wazuh.com/](https://www.wazuh.com/)

联系人：José Alonso Cárdenas Márquez [acm@FreeBSD.org](mailto:acm@FreeBSD.org)

Wazuh 是一家免费开源平台，用于威胁预防、检测和响应，可保护本地、虚拟化、容器化及云环境中的工作负载。

Wazuh 解决方案由端点安全代理和管理服务器组成。管理服务器收集并分析代理收集的数据。Wazuh 与 [Elastic Stack](https://www.elastic.co/elastic-stack/) 和 [OpenSearch](https://opensearch.org/) 完全集成，提供搜索引擎和数据可视化工具，用户可通过其浏览安全告警。

将 Wazuh 移植到 FreeBSD 的工作开始于 [Michael Muenz](mailto:m.muenz@gmail.com)，他自 2021 年 9 月首次将 [security/wazuh-agent](https://cgit.freebsd.org/ports/tree/security/wazuh-agent/) 加入 Ports 树。2022 年 7 月，我接管该 Port，并开始移植其他 Wazuh 组件。

目前，所有 Wazuh 组件已移植或适配：[security/wazuh-manager](https://cgit.freebsd.org/ports/tree/security/wazuh-manager/)、[security/wazuh-agent](https://cgit.freebsd.org/ports/tree/security/wazuh-agent/)、[security/wazuh-server](https://cgit.freebsd.org/ports/tree/security/wazuh-server/)、[security/wazuh-indexer](https://cgit.freebsd.org/ports/tree/security/wazuh-indexer/)、[security/wazuh-dashboard](https://cgit.freebsd.org/ports/tree/security/wazuh-dashboard/)。

在 FreeBSD 上，[security/wazuh-manager](https://cgit.freebsd.org/ports/tree/security/wazuh-manager/) 与 [security/wazuh-agent](https://cgit.freebsd.org/ports/tree/security/wazuh-agent/) 从 Wazuh 源代码编译，[security/wazuh-indexer](https://cgit.freebsd.org/ports/tree/security/wazuh-indexer/) 基于 [textproc/opensearch](https://cgit.freebsd.org/ports/tree/textproc/opensearch/) 改编，用于存储代理数据。[security/wazuh-server](https://cgit.freebsd.org/ports/tree/security/wazuh-server/) 对配置文件进行了 FreeBSD 定向适配。运行时依赖包括 [security/wazuh-manager](https://cgit.freebsd.org/ports/tree/security/wazuh-manager/)、[sysutils/beats8](https://cgit.freebsd.org/ports/tree/sysutils/beats8/)（filebeat）和 [sysutils/logstash8](https://cgit.freebsd.org/ports/tree/sysutils/logstash8/)。[security/wazuh-dashboard](https://cgit.freebsd.org/ports/tree/security/wazuh-dashboard/) 使用适配的 [textproc/opensearch-dashboards](https://cgit.freebsd.org/ports/tree/textproc/opensearch-dashboards/) 以及从 Wazuh 源代码生成的 wazuh-kibana-app 插件。

该工作的主要目标同样是提升 FreeBSD 在信息安全或网络安全平台中的可见性。

此外，你可以使用 [https://github.com/alonsobsd/wazuh-makejail](https://github.com/alonsobsd/wazuh-makejail) 或 [https://github.com/AppJail-makejails/wazuh](https://github.com/AppJail-makejails/wazuh)（来自 [AppJail](https://github.com/DtxdF/AppJail)）轻松测试 Wazuh 单节点基础设施（All-in-one）。

欢迎有兴趣的人参与项目。

当前版本：4.4.4

#### 待办事项

- 增加 Wazuh 集群模式基础设施 makejail（进行中）
- 将 FreeBSD 添加到 Wazuh Inc 官方支持平台；参见 [https://github.com/wazuh/wazuh-kibana-app/pull/5413](https://github.com/wazuh/wazuh-kibana-app/pull/5413)
- 添加 FreeBSD SCA 策略（进行中）

## 第三方项目

许多项目基于 FreeBSD 构建或将 FreeBSD 组件整合到其项目中。由于这些项目可能对更广泛的 FreeBSD 社区有兴趣，我们有时会在季度报告中包含这些项目提交的简要更新。FreeBSD 项目不对这些提交内容的准确性或真实性作出任何保证。

### PkgBase.live

链接：

[网站](https://alpha.pkgbase.live/) URL: [https://alpha.pkgbase.live/](https://alpha.pkgbase.live/)

[源码](https://codeberg.org/pkgbase) URL: [https://codeberg.org/pkgbase](https://codeberg.org/pkgbase)

联系人：Mina Galić [freebsd@igalic.co](mailto:freebsd@igalic.co)

PkgBase.live 是 FreeBSD [PkgBase 项目](https://wiki.freebsd.org/PkgBase) 的非官方仓库，目前已恢复服务。

该服务灵感来自 [https://up.bsd.lv/](https://up.bsd.lv/)，曾为 STABLE 与 CURRENT 分支提供 [freebsd-update(8)(https://man.freebsd.org/cgi/man.cgi?query=freebsd-update&sektion=8&format=html)。up.bsd.live 暂停服务，使 PkgBase.live 恢复更显必要。

目前提供构建版本：

- FreeBSD 13.2-RELEASE
- FreeBSD 13-STABLE
- FreeBSD 14-CURRENT

支持平台：

- amd64
- aarch64
- armv7
- i386

RISCv64 暂时未提供。

硬件为 Vultr 的高性能 VPS。服务器与运行构建任务及提供包的 jails 均为“自托管”，安装并通过 PkgBase 保持最新。

由于尚未在 FreeBSD jails 中配置 Vultr IPv6，PkgBase.live 暂不支持 IPv6。如有经验，请联系管理员。

硬件由 FreeBSD 社区成员赞助。

### FreeBSD 容器管理：Pot、Potluck 与 Potman

链接：

[Pot GitHub 组织](https://github.com/bsdpot) URL: [https://github.com/bsdpot](https://github.com/bsdpot)

联系人：

Luca Pizzamiglio (Pot) [pizzamig@FreeBSD.org](mailto:pizzamig@FreeBSD.org)

Bretton Vine (Potluck) [bv@honeyguide.eu](mailto:bv@honeyguide.eu)

Michael Gmelin (Potman) [grembo@FreeBSD.org](mailto:grembo@FreeBSD.org)

Pot 是一款 jail 管理工具，同时支持通过 Nomad 进行编排 [详细](https://www.freebsd.org/news/status/report-2020-01-2020-03/#pot-and-the-nomad-pot-driver)。

本季度发布 [Pot 0.15.5](https://github.com/bsdpot/pot/releases/tag/0.15.5)，包含多项 bug 修复与 [属性设置功能（如 jail sysctl 变量)(https://github.com/bsdpot/pot/pull/263)，将在 2023Q3 季度包集中提供。

Potluck 旨在成为 FreeBSD 与 Pot 的 Dockerhub，即提供 Pot 风格及完整容器镜像的仓库，可与 Pot 或 Nomad 一道使用。

所有 Potluck 容器已重新构建为基于 FreeBSD 13.2 的镜像，并通过 [Pot signify](https://github.com/bsdpot/pot/pull/242) 签名。

撰写了 [《在 FreeBSD 上使用 Ansible、Pot 等构建虚拟数据中心的初学者指南》](https://honeyguide.eu/posts/ansible-pot-foundation/)，说明如何通过 Ansible playbook 部署基于 Pot 与 Potluck 的复杂环境，包括示例节点如 MariaDB、Prometheus、Grafana、nginx、OpenLDAP 或 Traefik，以及由 Nomad 与 Consul 管理的容器编排。

Pot 团队提交的 [Nomad 安全性改进补丁](https://github.com/hashicorp/nomad/pull/13343) 已被上游接受，将作为 Nomad 1.6.0 的一部分。Nomad 是调度器与编排器，支持通过 [sysutils/nomad-pot-driver](https://cgit.freebsd.org/ports/tree/sysutils/nomad-pot-driver/) 使用 Pot。

欢迎反馈与补丁。

赞助商：Honeyguide Group
