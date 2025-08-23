# FreeBSD 2022 年第三季度状态报告

- 原文：[FreeBSD Status Report Third Quarter 2023](https://www.freebsd.org/status/report-2023-07-2023-09/)

这是 2023 年第三季度状态报告，共包含 32 条条目。

这是夏季季度，因此包含了来自谷歌编程之夏的许多有趣新闻。当然，我们还有常规的团队报告，许多项目也与我们分享了它们的最新进展。为 FreeBSD 14 的首次发布，已经完成了大量重要工作。

祝阅读愉快。

Lorenzo Salvadore 

代表状态团队敬上。

## FreeBSD 团队报告

来自各个官方及半官方团队的条目，摘自 [管理页面](https://www.freebsd.org/administration/)。

### FreeBSD 核心团队

联系方式：FreeBSD 核心团队 [core@FreeBSD.org](mailto:core@FreeBSD.org)

FreeBSD 核心团队是 FreeBSD 的管理机构。

#### Hans Petter Selasky 逝世

FreeBSD 核心团队感谢 Hans Petter Selasky 多年来的奉献。我们对他的去世深感悲痛，并与社区一道哀悼。

[悼文](https://lists.freebsd.org/archives/freebsd-announce/2023-July/000076.html)。

#### 与 FreeBSD 基金会的会议

核心团队继续与 FreeBSD 基金会举行会议，讨论 FreeBSD 管理、开发及后续发展的下一步措施。核心团队与基金会董事会及员工进行了两次会议，讨论了基金会如何帮助核心团队及整个项目。

#### Portmgr 任期限制

核心团队与 Ports 管理团队讨论了为开发者设定团队任期限制的提议。该提议已被 Ports 管理团队批准，并将于 2024 年初生效，同时通过常规观察者计划，确保持续有新成员加入 Ports 管理团队。

#### FreeBSD 15 弃用 32 位平台

正在进行的工作包括将对 32 位平台的支持标记为 FreeBSD 15 的“弃用”。

#### Matrix IM

Matrix 实例及 Element-web 客户端的测试仍在进行。

计划在 9 月 EuroBSDCon 之后发布 Beta 版本。

#### 改进提交权限过期策略

核心团队将明确开发者成为同仁后，如何更新 PGP 密钥的流程。

#### EuroBSDCon

核心团队成员在葡萄牙科英布拉参加 EuroBSDCon 期间，与 FreeBSD 基金会会面，讨论项目发展方向。

### FreeBSD 基金会

链接：

[FreeBSD 基金会](https://freebsdfoundation.org/) URL: [https://freebsdfoundation.org/](https://freebsdfoundation.org/)

[技术路线图](https://freebsdfoundation.org/blog/technology-roadmap/) URL: [https://freebsdfoundation.org/blog/technology-roadmap/](https://freebsdfoundation.org/blog/technology-roadmap/)

[捐赠](https://freebsdfoundation.org/donate/) URL: [https://freebsdfoundation.org/donate/](https://freebsdfoundation.org/donate/)

[基金会合作计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/) URL: [https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)

[FreeBSD 期刊](https://freebsdfoundation.org/journal/) URL: [https://freebsdfoundation.org/journal/](https://freebsdfoundation.org/journal/)

[基金会活动](https://freebsdfoundation.org/our-work/events/) URL: [https://freebsdfoundation.org/our-work/events/](https://freebsdfoundation.org/our-work/events/)

联系方式：Deb Goodkin [deb@FreeBSDFoundation.org](mailto:deb@FreeBSDFoundation.org)

FreeBSD 基金会是一家 501(c)(3) 非营利组织，致力于支持和推广 FreeBSD 项目及全球社区。个人和企业的捐赠用于资助和管理软件开发项目、会议和开发者峰会。基金会还为 FreeBSD 贡献者提供差旅资助，购买并支持硬件以改善和维护 FreeBSD 基础设施，并提供资源以提升安全性、质量保证和集群管理能力。基金会发布宣传资料以推广、教育和倡导 FreeBSD，促进商业厂商与 FreeBSD 开发者之间的合作，并代表 FreeBSD 项目执行合同、许可协议及其他需要法人实体的法律事务。

本季度，我们协助 FreeBSD 庆祝 30 周年！这一庆祝活动推动我们加快了 FreeBSD 的发展与创新，同时让我们专注于确定关键投资领域。在九月的董事会会议上，我们细化了目标，重点放在提升 FreeBSD 的采用率和知名度、多元化资金来源，以及投资于社区健康和项目长期稳定性。目前，我们正在确定主要受众和目标市场，同时为这些目标制定可衡量的成果。

在本状态报告中，您将了解到我们为推动 FreeBSD 成长与创新所做的工作。我们将重点介绍内部软件开发团队以及外部资助项目在技术改进方面的工作。同时，您也将了解我们在社区外推广 FreeBSD 的宣传工作，以及我们为与现有和潜在商业用户建立联系所做的努力。

#### 筹款

我们衷心感谢所有慷慨捐赠以支持我们工作的个人和机构。除了众多个人捐赠，我们特别感谢 NetApp、奈飞和 ARM 的重大捐赠。仅第三季度，我们就收到了捐款 183,842 美元，今年累计达到了 375,000 美元。今年预算约为 2,230,000 美元，其中包括增加对 FreeBSD 宣传和软件开发的投入。超过一半的预算用于直接改善 FreeBSD 并保持其安全。通过配备专职人员专注于合作伙伴关系，我们能够有效强调投资我们工作的意义，并突显 FreeBSD 对企业的长期可行性。您的支持对我们的使命至关重要，我们深表感谢。请考虑为 2023 年筹款活动捐赠！[https://freebsdfoundation.org/donate/](https://freebsdfoundation.org/donate/) 对于大型商业捐赠者，请查看更新后的 [FreeBSD 基金会合作计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)。

#### 合作与研究

在本季度的合作与研究中，我们在三个关键领域取得了进展：

首先，[企业工作组](https://wiki.freebsd.org/EnterpriseWorkingGroup)逐渐发展壮大，目前已有 58 名参与者，并在四个工作流中开展积极项目。这四个工作流包括云原生、Samba、bhyve 可管理性以及对 AI 工作负载的支持。另有若干其他领域受到关注，预计到今年年底及明年第一季度，我们将在多个重点领域看到重要功能更新。

其次，我们在与其他开源社区成员和组织（尤其是 [Open Source Initiative](https://opensource.org/)）的合作中取得了良好进展，以推动 FreeBSD 社区的提案和技术发展。通过与开源倡议的 [开放政策联盟](https://opensource.org/programs/open-policy-alliance)合作，我们正在向美国政府提交回应，说明如何支持开源安全性与可持续性。为此，Greg Wallace 参与了在北卡罗来纳州罗利举行的 All Things Open 大会，由开放政策联盟组织的专题讨论。此外，Greg Wallace 还跟踪了美国政府如何将 CHERI 纳入默认安全策略的政策建议中，[例如最近美国及全球政府安全机构的报告](https://www.cisa.gov/sites/default/files/2023-10/Shifting-the-Balance-of-Cybersecurity-Risk-Principles-and-Approaches-for-Secure-by-Design-Software.pdf)。在报告第 28 页，CHERI 被列为紧随 Rust 之后关键的“安全设计”策略。

最后，我们继续加强与越来越多使用 FreeBSD 的企业的合作关系。多个会议有助于促进这些关系，包括 EuroBSDCon、Open Source Summit 和 All Things Open。我们还开发了一个新项目，以支持与美国政府合作的厂商/云用户。该项目的具体细节将在 FreeBSD 厂商峰会上公布。

#### 宣传

我们的许多工作专注于 FreeBSD 项目宣传。这包括展示有趣的 FreeBSD 工作、制作文献与视频教程、参加活动或进行演讲。我们制作的文献旨在教授 FreeBSD 基础知识，帮助人们更轻松地采用或贡献 FreeBSD。除了参加和演讲活动外，我们还鼓励并协助社区成员举办自己的 FreeBSD 活动、进行演讲或维护 FreeBSD 展台。

FreeBSD 基金会在全球范围内赞助许多会议、活动和峰会。这些活动可以是 BSD 相关的、开源的，或面向弱势群体的技术活动。我们支持以 FreeBSD 为中心的活动，为知识分享、协作开发和促进开发者与商业用户之间的合作提供场所，从而维护健康的生态系统。我们也支持非 FreeBSD 活动，以宣传和提高 FreeBSD 的认知度，增加 FreeBSD 在不同应用中的使用，并招募更多贡献者。我们不断将新活动加入年度计划。今年七月，我们在俄勒冈州波特兰举办了 FOSSY 新开源会议的研讨会并设立了展台。除了参加和策划会议外，我们持续开展新的培训计划，并更新了 [操作指南](https://freebsdfoundation.org/freebsd-project/resources/)，以便让更多人尝试 FreeBSD。

我们的部分宣传工作包括：

* 2023 年 7 月 13-16 日，在波特兰的 [FOSSY](https://sfconservancy.org/fossy/) 举办研讨会并设立展台
* 2023 年 7 月 27-29 日，在台湾新北市成为 COSCUP 友好级赞助商
* 在 EuroBSDCon FreeBSD 开发者峰会上进行演讲，并在 [EuroBSDCon 2023](https://2023.eurobsdcon.org/)（2023 年 9 月 14-17 日，葡萄牙科英布拉）赞助并设立展台
* 参加 [Open Source Summit, Europe](https://events.linuxfoundation.org/open-source-summit-europe/)（2023 年 9 月 19-21 日，西班牙毕尔巴鄂）
* 继续筹备 [2023 年 11 月 FreeBSD 厂商峰会](https://freebsdfoundation.org/news-and-events/event-calendar/november-2023-freebsd-vendor-summit/)（11 月 2-3 日，加州圣何塞）
* 持续管理谷歌编程之夏项目
* 发布 [七月通讯](https://freebsdfoundation.org/news-and-events/newsletter/freebsd-foundation-update-july-2023/)
* 其他博客文章
  * [在活动中宣传：2023 年五月 FreeBSD 开发者峰会和 BSDCan](https://freebsdfoundation.org/blog/advocating-at-events-may-2023-freebsd-dev-summit-and-bsdcan/)
  * [升级到 FreeBSD 13.2 的十大理由](https://freebsdfoundation.org/blog/top-ten-reasons-to-upgrade-to-freebsd-13-2/)
  * [2023 年七月软件开发项目更新](https://freebsdfoundation.org/blog/july-2023-software-development-projects-update/)
  * [用于研究的 FreeBSD：CHERI/Morello](https://freebsdfoundation.org/blog/freebsd-for-research-cheri-morello/)
  * 介绍 FreeBSD 谷歌编程之夏 2023 学生
    * [Soobin Rho](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-soobin-rho/)
    * [Raghav Sharma](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-raghav-sharma/)
    * [Sudhanshu Mohan Kashyap](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-sudhanshu-mohan-kashyap/)
    * [Aymeric Wibo](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-aymeric-wibo/)
  * [介绍 2023 年夏季滑铁卢大学实习生：Naman Sood](https://freebsdfoundation.org/blog/meet-the-summer-2023-university-of-waterloo-co-op-student-naman-sood/)
  * [介绍 FreeBSD 基金会 2023 年夏季实习生：Jake Freeland](https://freebsdfoundation.org/blog/meet-freebsd-foundation-2023-summer-intern-jake-freeland/)
* FreeBSD 新闻

  * [FreeBSD 基金会加入 OSI 开放政策联盟](https://freebsdfoundation.org/news-and-events/latest-news/freebsd-foundation-joins-osis-open-policy-alliance/)
  * [Hackernoon: 我们使用开源 FreeBSD 作为企业操作系统的 5 个理由](https://freebsdfoundation.org/news-and-events/latest-news/hackernoon-5-reasons-we-use-open-source-freebsd-as-our-enterprise-os/)
  * [What the Dev Podcast: FreeBSD 项目的演变](https://freebsdfoundation.org/news-and-events/latest-news/what-the-dev-podcast-the-evolution-of-the-freebsd-project/)

我们通过出版专业制作的 FreeBSD 期刊来向全球普及 FreeBSD。如前所述，FreeBSD 期刊现已免费提供。详情及最新期刊请访问 [https://www.freebsdfoundation.org/journal/](https://www.freebsdfoundation.org/journal/)。

更多关于我们参加的活动和即将举行的活动信息，请访问 [https://freebsdfoundation.org/our-work/events/](https://freebsdfoundation.org/our-work/events/)。

#### 改进操作系统

在 2023 年第三季度，共有 282 个 src、652 个 ports 和 24 个 doc 树提交标注 FreeBSD 基金会为赞助方。其中部分基金会赞助的工作在单独报告中进行了描述：

* [通过使用日志软更新启用文件系统快照](https://www.freebsd.org/status/report-2023-07-2023-09/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates)
* [登录类修复与改进](https://www.freebsd.org/status/report-2023-07-2023-09/#_login_classes_fixes_and_improvements)
* [改进基于基本系统的 OpenSSL 3](https://www.freebsd.org/status/report-2023-07-2023-09/#_openssl_3_in_baseimproved)
* [FreeBSD 上的 OpenStack](https://www.freebsd.org/status/report-2023-07-2023-09/#_openstack_on_freebsd)
* [进程可见性安全策略](https://www.freebsd.org/status/report-2023-07-2023-09/#_process_visibility_security_policies)
* [amd64 的 SIMD 增强](https://www.freebsd.org/status/report-2023-07-2023-09/#_simd_enhancements_for_amd64)

技术团队成员参加了在葡萄牙科英布拉举行的 EuroBSDCon 2023。許立文 举办了教程，帮助新手参与 FreeBSD 项目。在会议之前，举行了 FreeBSD 开发者峰会，团队在会上展示了他们的 [近期工作简报](https://wiki.freebsd.org/DevSummit/202309?action=AttachFile&do=view&target=Foundation_Technology_Team_Devsummit_Fall_2023.pdf)。

六个暑期实习/项目顺利结束：

* [Jake Freeland](https://freebsdfoundation.org/blog/meet-freebsd-foundation-2023-summer-intern-jake-freeland/) 在暑期参与 [Capsicum 项目](https://freebsdfoundation.org/project/capsicum-internship/)，进行违规追踪、适配各类守护进程如 [syslogd(8)](https://man.freebsd.org/cgi/man.cgi?query=syslogd&sektion=8&format=html)，并编写文档。
* [Naman Sood](https://freebsdfoundation.org/blog/meet-the-summer-2023-university-of-waterloo-co-op-student-naman-sood/) 完成了[各种任务，主要与网络相关](https://freebsdfoundation.org/project/networking-summer-internship/)。
* En-Wei Wu 完成了 [另一项无线网络实习](https://freebsdfoundation.org/project/wireless-internship/)，改进并扩展了 net80211(4) WiFi 模拟器 wtap。
* Yan-Hao Wang 参与了 [文档与测试项目](https://freebsdfoundation.org/project/documentation-and-testing-internship/)，如构建在线 man 页编辑器并为部分用户空间工具添加测试用例。
* Christos Margiolis 完成了 [改进 kinst DTrace 提供者的项目](https://freebsdfoundation.org/project/improving-the-kinst-dtrace-provider/)，实现了内联函数追踪，并将 kinst 移植到 arm64 和 riscv。
* 为了准备 FreeBSD 14.0，Muhammad Moinur (Moin) Rahman 提交了 700 多个针对近期 OpenSSL 和 LLVM 更新影响 ports 的修复或解决方法。

有关当前和过去基金会承包工作的更多信息，请访问 [基金会项目页面](https://freebsdfoundation.org/our-work/projects/)。

本季度完成的其他基金会赞助工作示例：

* 改进 riscv64 CPU 身份与特性检测
* 从零重写 [intro(9)](https://man.freebsd.org/cgi/man.cgi?query=intro&sektion=9&format=html) man 页
* 对 [hwpmc(4)](https://man.freebsd.org/cgi/man.cgi?query=hwpmc&sektion=4&format=html) 模块以及 [pmc(3)](https://man.freebsd.org/cgi/man.cgi?query=pmc&sektion=3&format=html) 库和工具进行代码维护与 bug 修复
* 为 FreeBSD 14.0 做准备，提交了多项 [freebsd-update(8)](https://man.freebsd.org/cgi/man.cgi?query=freebsd-update&sektion=8&format=html) 修复
* 对 LinuxKPI、iwlwifi 和 net802.11 代码提交了 37 项更新与修复
* 更新 SSH，先为 OpenSSH 9.3p2，再为 9.4p1
* 修补 ssh-keygen，使其在无参数调用时生成 Ed25519 密钥
* 添加 Linux [membarrier(2)](https://man.freebsd.org/cgi/man.cgi?query=membarrier&sektion=2&format=html) 系统调用的全新实现
* 将 amd64 和 arm64 的 MAXCPU 增加至 1024
* 提交修复以防止受影响机器上 Zenbleed 自动误操作/数据泄露（通过 chicken bit）
* 审查内核中调度优先级的使用情况，以强化 rtprio() 系统调用，并在某些情况下提高其实用性

#### 支持 FreeBSD 基础设施

基金会提供硬件和两名员工以支持 FreeBSD 集群。通过捐赠，基金会与集群管理团队协调，购买了五台新软件包构建器、三台新 Web 服务器、一台新防火墙/路由器、两台包镜像服务器，以及两台新的持续集成服务器。除一台软件包镜像服务器外，所有新硬件均部署在美国东海岸。

#### 持续集成与质量保证

基金会提供专职人员并资助项目，以改进 FreeBSD 项目的持续集成、自动化测试及整体质量保证工作。有关 CI 工作的详细信息，可参阅专门报告条目。

#### 法律与 FreeBSD 知识产权

基金会持有 FreeBSD 商标，并负责保护这些商标。同时，我们为核心团队提供法律支持，以调查出现的问题。

访问 [https://freebsdfoundation.org](https://freebsdfoundation.org/) 可了解更多关于基金会如何支持 FreeBSD 以及我们能为您提供的帮助。

### FreeBSD 发布工程团队

链接：

[FreeBSD 14.0-RELEASE 计划](https://www.freebsd.org/releases/14.0R/schedule/) URL: [https://www.freebsd.org/releases/14.0R/schedule/](https://www.freebsd.org/releases/14.0R/schedule/)

[FreeBSD 发布](https://download.freebsd.org/releases/ISO-IMAGES/) URL: [https://download.freebsd.org/releases/ISO-IMAGES/](https://download.freebsd.org/releases/ISO-IMAGES/)

[FreeBSD 开发快照](https://download.freebsd.org/snapshots/ISO-IMAGES/) URL: [https://download.freebsd.org/snapshots/ISO-IMAGES/](https://download.freebsd.org/snapshots/ISO-IMAGES/)

联系方式：FreeBSD 发布工程团队，[re@FreeBSD.org](mailto:re@FreeBSD.org)

FreeBSD 发布工程团队负责制定并发布 FreeBSD 官方版本的发布计划、宣布代码冻结、维护相关分支等工作。

在 2023 年第三季度，发布工程团队开始了即将到来的 14.0-RELEASE 周期的工作。截至目前，BETA3 已发布，BETA4 将紧随其后。

发布工程团队继续为 **main** 和 **stable/13** 分支提供每周开发快照构建。

赞助：Tarsnap

赞助：[https://www.gofundme.com/f/gjbbsd/](https://www.gofundme.com/f/gjbbsd/)

赞助：FreeBSD 基金会


### 持续集成

链接：

[FreeBSD Jenkins 实例](https://ci.freebsd.org/) URL: [https://ci.FreeBSD.org](https://ci.FreeBSD.org)

[FreeBSD CI Tinderbox 视图](https://tinderbox.freebsd.org/) URL: [https://https://tinderbox.freebsd.org](https://https//tinderbox.freebsd.org)

[FreeBSD CI 构件存档](https://artifact.ci.freebsd.org/) URL: [https://artifact.ci.FreeBSD.org](https://artifact.ci.FreeBSD.org)

[托管 CI wiki](https://wiki.freebsd.org/HostedCI) URL: [https://wiki.FreeBSD.org/HostedCI](https://wiki.freebsd.org/HostedCI)

[第三方软件 CI](https://wiki.freebsd.org/3rdPartySoftwareCI) URL: [https://wiki.FreeBSD.org/3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI)

[freebsd-testing@ 相关工单](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals) URL: 

[https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)

[FreeBSD CI 仓库](https://github.com/freebsd/freebsd-ci) URL: [https://github.com/freebsd/freebsd-ci](https://github.com/freebsd/freebsd-ci)

[dev-ci 邮件列表](https://lists.freebsd.org/subscription/dev-ci) URL: [https://lists.FreeBSD.org/subscription/dev-ci](https://lists.freebsd.org/subscription/dev-ci)

联系方式：Jenkins 管理员 [jenkins-admin@FreeBSD.org](mailto:jenkins-admin@FreeBSD.org)

联系方式：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

联系方式：[freebsd-testing 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-testing)

联系方式：IRC EFNet #freebsd-ci 频道

在 2023 年第三季度，我们与项目贡献者和开发者合作，满足他们的测试需求。同时，也与外部项目和公司合作，通过在 FreeBSD 上进行更多测试来增强其产品。

已完成的重要任务：

* 为 stable/14 分支添加构建任务
* 更新 CI 结果的 ["Tinderbox" 视图](https://tinderbox.freebsd.org/)，现在包括测试结果和当前失败或不稳定系列的“起点”
* 该工作主要由基金会实习生 Yan-Hao Wang 完成，他的其他贡献在本报告的其他条目中有所记录

进行中的任务：

* 设计与实现 pre-commit CI 构建和测试，以及基于 pull/merge 请求的系统（支持 [工作流工作组](https://gitlab.com/bsdimp/freebsd-workflow)）
* 概念验证系统正在开发中
* 设计与实现使用 CI 集群构建发布构件的能力
* 简化贡献者和开发者的 CI/测试环境配置
* 设置 CI 阶段环境并放置实验任务
* 改进硬件测试实验室并增加更多测试硬件
* 合并 [https://reviews.freebsd.org/D38815](https://reviews.freebsd.org/D38815)
* 合并 [https://reviews.freebsd.org/D36257](https://reviews.freebsd.org/D36257)

开放或排队任务：

* 收集和整理 [CI 任务与想法](https://hackmd.io/@FreeBSD-CI/freebsd-ci-todo)
* 为运行测试的 VM 客户机设置公网访问
* 使用裸机硬件运行测试套件
* 为 -CURRENT 分支添加 drm ports 构建测试
* 计划运行 ztest 测试
* 协助更多软件在其 CI 流程中支持 FreeBSD（Wiki 页面：[3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI)、[HostedCI](https://wiki.freebsd.org/HostedCI)）
* 与托管 CI 提供商合作，提升对 FreeBSD 的支持

更多进行中任务信息请参见 [freebsd-testing@ 相关工单](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)，欢迎加入我们的工作！

赞助：FreeBSD 基金会

### Ports

链接：

[关于 FreeBSD Ports](https://www.freebsd.org/ports/) URL:[https://www.FreeBSD.org/ports/](https://www.freebsd.org/ports/)

[为 Ports 贡献](https://docs.freebsd.org/en/articles/contributing/#ports-contributing) URL: [https://docs.freebsd.org/en/articles/contributing/#ports-contributing](https://docs.freebsd.org/en/articles/contributing/#ports-contributing)

[FreeBSD Ports 监控](http://portsmon.freebsd.org/) URL: [http://portsmon.freebsd.org/](http://portsmon.freebsd.org/)

[Ports 管理团队](https://www.freebsd.org/portmgr/) URL: [https://www.freebsd.org/portmgr/](https://www.freebsd.org/portmgr/)

[Ports 压缩包](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/) URL: [http://ftp.freebsd.org/pub/FreeBSD/ports/ports/](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/)

联系方式：René Ladan [portmgr-secretary@FreeBSD.org](mailto:portmgr-secretary@FreeBSD.org)

联系方式：FreeBSD Ports 管理团队 [portmgr@FreeBSD.org](mailto:portmgr@FreeBSD.org)

Ports 管理团队负责把控 Ports 数据树的整体方向、构建包及人员事务。以下是上一季度的工作概况：

* 根据 INDEX，目前 Ports 共有 34,600 个 ports。目前有 3,000 个开放的 ports PR，其中约 730 个未分配。上一季度，main 分支有 130 位提交者完成 11,454 次提交，2023Q3 分支有 37 位提交者完成 828 次提交。相比上一季度，未分配 PR 数量略有下降，main 分支提交数增加 10%，但季度分支的回移次数减少，ports 总数略有增长。

在第三季度，我们欢迎 Joel Bodenmann (jbo@) 成为新的 ports 提交者，为已经是 src 提交者的 mizhka@ 授予了 ports 提交权限，同时收回了 knu@ 和 uqs@ 的提交权限以保管，因他们一年未活跃。

Portmgr 在第三季度讨论并处理了以下事项：

* 对子包（sub-packages）取得一些进展，并由 pizzamig@ 在 EuroBSDCon 做了 lightning talk
* 重构 ports 树的部分内容（LIB_DEPENDS、PREFIX、MANPREFIX、MANPATH）

Ports 数据树中对 FreeBSD 13.1 的支持已于 8 月 1 日达到生命周期终止，被移除。

基础设施方面的更新：

* 为 ebur128 和 guile 添加了 USES
* Mono、Perl、PostgreSQL 的默认版本分别更新为 5.20、5.34 和 15
* ebur128、guile 和 pycryptography 的默认版本分别设置为 "rust"、2.2 和 "rust"
* 主要 ports 更新如下：

  * pkg 更新到 1.20.7
  * chromium 更新到 117.0.5938.132
  * Firefox 更新到 118.0.1
  * KDE 更新到 5.27.8
  * Rust 更新到 1.72.0
  * Wine 更新到 8.0.2

上一季度，pgkmgr@ 进行了 18 次 exp-run，用于测试各类 ports 升级、默认版本更新以及 pycryptography 的变更。

## 项目

涉及多个类别的项目，包括内核、用户空间、Ports 和外部项目。

### 完善 FreeBSD 桌面体验

链接：


[外部媒体管理器](https://github.com/outpaddling/qmediamanager) URL: [https://github.com/outpaddling/qmediamanager](https://github.com/outpaddling/qmediamanager)

[基于 devd 的自动挂载器](https://github.com/outpaddling/devd-mount) URL: [https://github.com/outpaddling/devd-mount](https://github.com/outpaddling/devd-mount)

[SUID 挂载工具](https://github.com/outpaddling/npmount) URL: [https://github.com/outpaddling/npmount](https://github.com/outpaddling/npmount)

[更新弹窗通知](https://github.com/outpaddling/freebsd-update-notify) URL: [https://github.com/outpaddling/freebsd-update-notify](https://github.com/outpaddling/freebsd-update-notify)

联系方式：Jason Bacon [jwb@FreeBSD.org](mailto:jwb@FreeBSD.org)

[sysutils/desktop-installer](https://cgit.freebsd.org/ports/tree/sysutils/desktop-installer/) port 已存在十余年，可快速在裸 FreeBSD 系统上配置任何桌面环境或窗口管理器。然而，FreeBSD base 和 Ports 集合缺少一些终端用户期望的桌面功能。

已增强桌面安装器的电池监控脚本，可在不同充放电级别显示弹窗通知。

[deskutils/qmediamanager](https://cgit.freebsd.org/ports/tree/deskutils/qmediamanager/) 与 [sysutils/devd-mount](https://cgit.freebsd.org/ports/tree/sysutils/devd-mount/) 和 [sysutils/npmount](https://cgit.freebsd.org/ports/tree/sysutils/npmount/) 配合使用，可在 devd 通知时挂载插入的媒体，并弹出窗口为用户提供查看文件系统信息、打开文件管理器、格式化、复制磁盘映像或卸载的选项，为使用 USB 等外部媒体提供方便且安全的操作方式。

第四个新 port [deskutils/freebsd-update-notify](https://cgit.freebsd.org/ports/tree/deskutils/freebsd-update-notify/) 可在有新基本系统更新可用或配置的时间限制到达时弹窗通知用户。如果用户选择更新，系统会通过 [auto-update-system(1)](https://man.freebsd.org/cgi/man.cgi?query=auto-update-system&sektion=1&format=html)]([sysutils/auto-admin](https://cgit.freebsd.org/ports/tree/sysutils/auto-admin/) 的功能）更新整个系统（包括软件包、ports 和 base）。

这些新工具让 FreeBSD 桌面体验更接近主流桌面操作系统的便利性。工具已稳定可靠，但仍需审查，欢迎用户对默认行为和配置选项提供反馈。

### 改进 LLDB 内核模块

链接：

[谷歌编程之夏 Wiki 项目](https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement](https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement)

[项目代码库](https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel) URL: [https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel](https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel)

[LLVM PR](https://github.com/llvm/llvm-project/pull/67106) URL: [https://github.com/llvm/llvm-project/pull/67106](https://github.com/llvm/llvm-project/pull/67106)

联系方式：Sheng-Yi Hong [aokblast@FreeBSD.org](mailto:aokblast@FreeBSD.org)

LLDB 内核模块改进项目（前一季度报告中提及）为 FreeBSD 内核在 LLDB 上实现了 DynamicLoader 插件。

该插件已完成开发，可正确加载从内核 coredump 提取的所有内核模块及其调试文件。

插件已在 x86-64（可重定位类型内核模块）和 arm64(EC2)](共享库类型内核模块）平台测试，两者均表现良好。

当前，该插件准备通过 [LLVM PullRequest](https://github.com/llvm/llvm-project/pull/67106) 合入 LLVM 代码库。

赞助：2023 年谷歌编程之夏计划

## 用户空间

## 影响基本系统及其中程序的变更

### 改进基本系统中的 OpenSSL 3

链接：

[OpenSSL 下载](https://www.openssl.org/source/) URL: [https://www.openssl.org/source/](https://www.openssl.org/source/)

联系方式：Pierre Pronchery [pierre@freebsdfoundation.org](mailto:pierre@freebsdfoundation.org)

本条为对 [上一季度报告](https://www.freebsd.org/status/report-2023-04-2023-06/) 关于 [OpenSSL 3 集成入基本系统](https://www.freebsd.org/status/report-2023-04-2023-06/#_openssl_3_in_base) 的后续说明。

自上次报告以来，最显著的更新是 3.0.10 和 3.0.11 版本发布，修复了低至中等严重性的 CVE 问题（[CVE-2023-2975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2975)、[CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)、[CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)、[CVE-2023-4807](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4807)）。

然而，这并非唯一更改，本季度还修复了一些与集成相关的问题，大多在使用基本系统中的 OpenSSL 3 构建 ports 时发现。

修复内容包括：

* 将 engines 和 legacy provider 与 libcrypto.so 共享对象链接，以确保符号可见性，为此在构建系统中 [需要应用 hack](https://cgit.freebsd.org/src/commit/Makefile.inc1?id=1a18383a52bc373e316d224cef1298debf6f7e25)
* 修正 FIPS provider 的源文件列表
* 确保对已废弃的 0.9.8 API 的向后兼容性，这对于基于 OpenSSH [ssh-agent(1)](https://man.freebsd.org/cgi/man.cgi?query=ssh-agent&sektion=1&format=html) 认证机制的 [security/pam_ssh_agent_auth](https://cgit.freebsd.org/ports/tree/security/pam_ssh_agent_auth/) PAM 模块尤其有用

### 登录类修复与改进

链接：

[审查堆栈起始](https://reviews.freebsd.org/D40339) URL: [https://reviews.freebsd.org/D40339](https://reviews.freebsd.org/D40339)

联系方式：Olivier Certner [olce.freebsd.statusreports@certner.fr](mailto:olce.freebsd.statusreports@certner.fr)

#### 背景

登录类主要用于在用户登录时，根据其所属登录类设置各种进程属性和特性。登录类通常指定资源限制、环境变量以及进程属性，如调度优先级和 umask。详情见 [login.conf(5)](https://man.freebsd.org/cgi/man.cgi?query=login.conf&sektion=5&format=html)。

#### 变更内容

`priority` 和 `umask` 功能现在支持 `inherit` 特殊值，可显式继承登录进程的属性。例如，当从非默认优先级的进程临时以其他用户登录时，可确保该用户启动的进程仍保持相同优先级。

用户现在可在本地配置文件 (**~/.login_conf**) 中覆盖全局设置（**/etc/login.conf**）的 `priority`。注意非特权用户无法提升优先级，并且在此上下文中使用 `inherit` 无意义，因为全局设置总是首先应用。

修复内容：

* 修复当 `priority` 指定实时优先级时，最终使用的优先级出现 off-by-one 错误（实时类中数值最高优先级 31 无法设置）
* 安全性：防止 setuid/setgid 进程应用某些用户 **~/.login_conf** 中的指令（因权限不足而无法应用的指令可能在此类进程中被错误应用）

相关手册页已更新以反映新功能，并改进了 [login.conf(5)](https://man.freebsd.org/cgi/man.cgi?query=login.conf&sektion=5&format=html) 中 `priority` 和 `umask` 的说明。

#### 状态

部分补丁已在 [Konstantin Belousov](mailto:kib@FreeBSD.org) 和 [Warner Losh](mailto:imp@FreeBSD.org) 的帮助下完成审查，其余补丁正在等待审查（欢迎志愿者参与），预计不会造成负担。

未来计划通过弃用未显式指定 `priority` 时重置为 0 的行为来提升一致性，这与 `umask` 已有 15+ 年的处理方式相同。

赞助：Kumacom SAS（开发工作）

赞助：FreeBSD 基金会（部分审查）

## 内核

内核子系统/功能、驱动支持、文件系统等的更新。

### 在使用日志软更新的文件系统上启用快照

联系人：Marshall Kirk McKusick [mckusick@FreeBSD.org](mailto:mckusick@FreeBSD.org)

该项目使在使用日志软更新时可以对 UFS/FFS 文件系统创建快照。该项目的详细信息已在[2022 年第四季度报告](https://www.freebsd.org/status/report-2022-10-2022-12/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates)中描述。

该项目有两个里程碑：

第一个里程碑是使在使用日志软更新时能够创建快照，并可利用这些快照对运行中的文件系统执行后台转储。后台转储可通过向 [dump(8)](https://man.freebsd.org/cgi/man.cgi?query=dump&sektion=8&format=html) 使用 `-L` 参数来请求。此里程碑已于 2022 年第四季度完成，并在 13.2 版本中发布，具体情况见[2023 年第一季度报告](https://www.freebsd.org/status/report-2023-01-2023-03/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates_in_13_2)。

第二个里程碑是在使用日志软更新的文件系统上利用快照进行后台检查。此里程碑已于 2023 年第三季度完成，并随 14.0 版本发布，同时也在 13.2-STABLE 版本中提供。

赞助：FreeBSD 基金会

### FreeBSD 内核的 SquashFS 驱动

链接：

[Wiki 页面](https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel](https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel)

[源代码](https://github.com/Mashijams/freebsd-src/tree/gsoc/testing) URL: [https://github.com/Mashijams/freebsd-src/tree/gsoc/testing](https://github.com/Mashijams/freebsd-src/tree/gsoc/testing)

联系人：Raghav Sharma [raghav@FreeBSD.org](mailto:raghav@FreeBSD.org)

本季度我们完成了内核的 SquashFS 驱动工作。现在可以在 FreeBSD 13.2-RELEASE 及更高版本上挂载 SquashFS 压缩档案，并执行所有基本的只读文件系统操作。

代码工作包括：

* 实现目录读取支持的 vop_lookup() 和 vop_readdir() 钩子。
* 实现文件读取支持的 vop_read() 和 vop_strategy() 钩子。
* 实现符号链接读取支持的 vop_readlink() 钩子。

我们还为 SquashFS 实现了扩展属性接口函数。剩下的工作是实现它们的内核接口钩子。

同时还进行了大量的 bug 修复。其中一个主要问题是无法列出根目录的第一个条目，原因是 SquashFS 的 `inode_number` 可能为零，而内核在列出目录项时会跳过零值。我们目前通过向 dirent 传递虚拟的 `inode_number` 来替代零值，解决了该问题。

代码审查目前正在与我的导师 [Chuck Tuffli](mailto:chuck@FreeBSD.org) 进行中。

我很高兴地宣布，SquashFS 将会出现在即将发布的 FreeBSD 版本中。

赞助： 2023 谷歌编程之夏项目

### 进程可见性安全策略

链接：

[审查堆栈起始](https://reviews.freebsd.org/D40626) URL: [https://reviews.freebsd.org/D40626](https://reviews.freebsd.org/D40626)

联系人：Olivier Certner [olce.freebsd.statusreports@certner.fr](mailto:olce.freebsd.statusreports@certner.fr)

#### 背景

FreeBSD 实现了三种内置安全策略，用于限制特定用户可以看到的进程，目的是防止信息泄露和不必要的交互。

第一种策略可以阻止非特权用户查看或操作其真实 UID 不匹配的进程。可以通过将 sysctl `security.bsd.see_other_uids` 设置为 0（默认值为 1）来启用。

第二种策略可以阻止非特权用户查看或操作其凭证中不包含用户所属组的进程。可以通过将 sysctl `security.bsd.see_other_gids` 设置为 0（默认值为 1）来启用。

第三种策略可以阻止非特权用户的进程查看或操作位于严格子 jail 的进程。jail 子系统已经阻止此类进程查看非其子代 jail 中的进程（参见 [jail(8)](https://man.freebsd.org/cgi/man.cgi?query=jail&sektion=8&format=html) 特别是“Hierarchical Jails”章节）。此策略的一个可能用途是结合上述第一种策略，将子 jail 中真实 UID 与祖先 jail 中某些用户相同的进程隐藏，因为在逻辑上这些不同 jail 中拥有相同 UID 的用户被视为不同用户。可以通过将 sysctl `security.bsd.see_jail_proc` 设置为 0（默认值为 1）来启用。

在对这些策略的代码进行审查并结合实际测试后，我们发现了一些问题和限制，因此对该主题进行了改进。

#### 变更

由 `security.bsd.see_jail_proc` 控制的策略已进行了以下修复和改进：

* 强化 `security.bsd.see_jail_proc` 策略，防止未授权用户尝试随机终止、改变优先级或调试子 jail 中相同真实 UID 的进程。此前，如果正确猜到 PID，即使这些进程不可见，也可能成功。
* 使该策略可以被 MAC 策略覆盖，与其他策略一致。

由 `security.bsd.see_other_gids` 控制的策略已修复为在判断用户是否属于某进程的组时，考虑进程的真实组而非有效组。其理由是某些用户在通过 setgid 位获得额外权限时，仍应继续看到其启动的进程；反之，用户不应看到由特权用户启动且临时加入其主组的进程。此新行为与 `security.bsd.see_other_uids` 对用户 ID 一直采用的方式一致（即考虑进程的真实 UID，而非有效 UID）。

我们已更新与这些安全策略相关的手册页，包括 [security(7)](https://man.freebsd.org/cgi/man.cgi?query=security&sektion=7&format=html)、[sysctl(8)](https://man.freebsd.org/cgi/man.cgi?query=sysctl&sektion=8&format=html) 和 [ptrace(2)](https://man.freebsd.org/cgi/man.cgi?query=ptrace&sektion=2&format=html)。若干内部函数的手册页（实现或利用这些策略的函数）也已改版。

#### 状态

在 [Mitchell Horne](mailto:mhorne@FreeBSD.org)、[Pau Amma](mailto:pauamma@gundo.com)、[Benedict Reuschling](mailto:bcr@FreeBSD.org) 和 [Ed Maste](mailto:emaste@FreeBSD.org) 的帮助下，大部分提交的更改已完成审查并获得批准，因此将很快合入源码树。补丁系列起始于 [review D40626](https://reviews.freebsd.org/D40626)。点击“Stack”标签可查看实现这些更改的完整审查列表。

作为后续步骤，我们正在考虑默认开启策略 `security.bsd.see_jail_proc`（即 sysctl 默认值变为 0），除非有反对意见。

赞助：Kumacom SAS（开发工作）

赞助：FreeBSD 基金会（大部分审查工作）

### 更新 Linux 兼容层

链接：

[Linuxulator 状态 Wiki 页面](https://wiki.freebsd.org/Linuxulator) URL: [https://wiki.freebsd.org/Linuxulator](https://wiki.freebsd.org/Linuxulator)

[Linux 应用状态 Wiki 页面](https://wiki.freebsd.org/LinuxApps) URL: [https://wiki.freebsd.org/LinuxApps](https://wiki.freebsd.org/LinuxApps)

联系人：Dmitry Chagin [dchagin@FreeBSD.org](mailto:dchagin@FreeBSD.org)

该项目旨在提升 FreeBSD 执行未修改 [linux(4)](https://man.freebsd.org/cgi/man.cgi?query=linux&sektion=4&format=html) 二进制文件的能力。

截至 [22dca7acf775](https://cgit.freebsd.org/src/commit/?id=22dca7acf775)，已实现 xattr 系统调用，使 Linux rsync 可用。

截至 [bbe017e0415a](https://cgit.freebsd.org/src/commit/?id=bbe017e0415a)，已实现 ioprio 系统调用，使得可在 FreeBSD 上 debootstrap Ubuntu 23.04。

## 架构

更新特定平台的功能并引入对新硬件平台的支持。

### NXP DPAA2 支持

链接：

[FreeBSD 源码树中的 DPAA2](https://cgit.freebsd.org/src/tree/sys/dev/dpaa2) URL: [https://cgit.freebsd.org/src/tree/sys/dev/dpaa2](https://cgit.freebsd.org/src/tree/sys/dev/dpaa2)

[在 Github 的 DPAA2](https://github.com/mcusim/freebsd-src) URL: [https://github.com/mcusim/freebsd-src](https://github.com/mcusim/freebsd-src)

联系人：Dmitry Salychev [dsl@FreeBSD.org](mailto:dsl@FreeBSD.org)

联系人：Bjoern A. Zeeb [bz@FreeBSD.org](mailto:bz@FreeBSD.org)

#### 什么是 DPAA2？

DPAA2 是某些 NXP SoC 中的硬件级网络架构，包含多个硬件模块，包括管理复合体（MC，用于操作 DPAA2 对象的命令接口）、线速 I/O 处理器（WRIOP，用于数据包分发、排队和丢弃决策）、队列和缓冲管理器（QBMan，控制 Rx/Tx 队列、Rx 缓冲池）等。管理复合体运行 NXP 提供的固件，将这些模块抽象为 DPAA2 对象，从而简化对底层硬件的访问。

#### 与上次报告的变化

* 改进了 DPAA2 通道之间的隔离 [改进](https://cgit.freebsd.org/src/commit/?id=58983e4b0253ad38a3e1ef2166fedd3133fdb552)。
* 修复了高网络负载下的 panic [修复](https://github.com/mcusim/freebsd-src/issues/19)。
* 支持 FDT/ACPI MDIO。
* NFS 根挂载在通过 DPAA2 网络启动时不再挂起 [修复](https://github.com/mcusim/freebsd-src/issues/7)。
* 驱动开始 [启动](https://github.com/mcusim/freebsd-src/issues/2) 使用自己的命令门户（DPMCP）与 MC 通信。
* [所有已关闭问题列表](https://github.com/mcusim/freebsd-src/issues?q=is%3Aissue+is%3Aclosed)。

#### 进行中的工作

已开始在 [dev/sff](https://cgit.freebsd.org/src/commit/?id=2a9021898c4ee2154787da862c238cfeccd655df) 上支持 SFF/SFP 模块，以便在超过 1 Gbit/s 链路上测试 DPAA2 驱动。

#### 计划

* 高网络负载测试（2.5 Gbit/s、10 Gbit/s）及瓶颈缓解。
* 基于缓存内存的软件门户。
* 驱动资源释放，以正确卸载 dpaa2.ko。
* 硬件支持的进一步模块（DPSW、DCE 等）。

赞助：Traverse Technologies（提供 Ten64 硬件用于测试）

### amd64 的 SIMD 增强

链接：

[项目提案](http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt) URL: [http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt](http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt)

[simd(7)](https://man.freebsd.org/cgi/man.cgi?query=simd&sektion=7&manpath=FreeBSD+15.0-CURRENT) URL: [https://man.freebsd.org/cgi/man.cgi?query=simd&sektion=7&manpath=FreeBSD+15.0-CURRENT](https://man.freebsd.org/cgi/man.cgi?query=simd&sektion=7&manpath=FreeBSD+15.0-CURRENT)

联系人：Robert Clausecker [fuz@FreeBSD.org](mailto:fuz@FreeBSD.org)

SIMD 指令集扩展（如 SSE、AVX 和 NEON）在现代计算机中广泛存在，为许多应用提供性能优势。该项目旨在为常用 libc 函数（主要是 [string(3)](https://man.freebsd.org/cgi/man.cgi?query=string&sektion=3&format=html) 中描述的函数）提供 SIMD 加速版本，加快大多数 C 程序的运行速度。

每个优化函数将提供最多四种实现：

* **标量** 实现：针对 amd64 优化，但不使用 SIMD。
* **基线** 实现：使用 SSE 和 SSE2，或 **x86-64-v2** 实现：使用所有 SSE 扩展直至 SSE4.2。
* **x86-64-v3** 实现：使用 AVX 和 AVX2。
* **x86-64-v4** 实现：使用 AVX-512F/BW/CD/DQ。

用户可通过设置 `ARCHLEVEL` 环境变量选择使用的 SIMD 加速等级。

虽然当前项目仅针对 amd64，但未来可能扩展至其他架构，如 arm64。

过去几个月，该项目取得了显著进展。已完成 SIMD 加速版本的函数包括 [bcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=bcmp&sektion=3&format=html)、[index(3)](https://man.freebsd.org/cgi/man.cgi?query=index&sektion=3&format=html)、[memchr(3)](https://man.freebsd.org/cgi/man.cgi?query=memchr&sektion=3&format=html)、[memcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=memcmp&sektion=3&format=html)、[stpcpy(3)](https://man.freebsd.org/cgi/man.cgi?query=stpcpy&sektion=3&format=html)、[strchr(3)](https://man.freebsd.org/cgi/man.cgi?query=strchr&sektion=3&format=html)、[strchrnul(3)](https://man.freebsd.org/cgi/man.cgi?query=strchrnul&sektion=3&format=html)、[strcpy(3)](https://man.freebsd.org/cgi/man.cgi?query=strcpy&sektion=3&format=html)、[strcspn(3)](https://man.freebsd.org/cgi/man.cgi?query=strcspn&sektion=3&format=html)、[strlen(3)](https://man.freebsd.org/cgi/man.cgi?query=strlen&sektion=3&format=html)、[strnlen(3)](https://man.freebsd.org/cgi/man.cgi?query=strnlen&sektion=3&format=html) 和 [strspn(3)](https://man.freebsd.org/cgi/man.cgi?query=strspn&sektion=3&format=html)。正在开发的函数包括 [memcpy(3)](https://man.freebsd.org/cgi/man.cgi?query=memcpy&sektion=3&format=html)、[memmove(3)](https://man.freebsd.org/cgi/man.cgi?query=memmove&sektion=3&format=html)、[strcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=strcmp&sektion=3&format=html)、[timingsafe_bcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=timingsafe_bcmp&sektion=3&format=html)](见 [D41673](https://reviews.freebsd.org/D41673)）、[timingsafe_memcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=timingsafe_memcmp&sektion=3&format=html)](见 [D41696](https://reviews.freebsd.org/D41696)）。遗憾的是，这些优化未能赶上 FreeBSD 14.0，但计划纳入 FreeBSD 14.1。

赞助：FreeBSD 基金会

### 将 mfsBSD 集成到发布构建工具中

链接：

[Wiki 文章](https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools](https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools)

[Phabricator 上的代码审查](https://reviews.freebsd.org/D41705) URL: [https://reviews.freebsd.org/D41705](https://reviews.freebsd.org/D41705)

[FreeBSD 基金会博客文章](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-soobin-rho/) URL: [https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-soobin-rho/](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-soobin-rho/)

联系人：Soobin Rho [soobinrho@FreeBSD.org](mailto:soobinrho@FreeBSD.org)

#### 什么是 mfsBSD？

mfsBSD 是一个工具集，用于创建基于 mfsroot 的小型但功能完整的 FreeBSD 发行版，将所有文件存储在内存中（MFS，Memory File System），并从硬盘、USB 存储设备或光学介质加载。它可用于多种用途，包括无盘系统、恢复分区以及远程覆盖其他操作系统。

[Martin Matuška](mailto:mm@FreeBSD.org) 是 mfsBSD 的创建者，也是最初的（2009 年）[mfsBSD 白皮书](https://people.freebsd.org/~mm/mfsbsd/mfsbsd.pdf) 的作者，上述摘录即来源于此。上游 mfsBSD 在 [GitHub 仓库](https://github.com/mmatuska/mfsbsd) 进行维护。

#### 项目目的

本项目将 mfsBSD 集成到 FreeBSD 发布工具集中，在 **/usr/src/release/Makefile** 中创建 mfsBSD 镜像的附加目标（**.img** 和 **.iso** 文件）。在集成之前，mfsBSD 仅存在于 FreeBSD 发布工具链之外，并且仅生成 -RELEASE 版本。

通过本项目，mfsBSD 镜像将可在官方 FreeBSD 发布页面获取。你也可以通过执行 `cd /usr/src/release && make release WITH_MFSBSD=1` 自行构建 mfsBSD，这将会在 **/usr/obj/usr/src/${ARCH}/release/** 生成 **mfsbsd-se.img** 和 **mfsbsd-se.iso**。

#### 与上季度的变化

代码已完成，目前正在审查中。如果你希望参与审查过程，可以随时加入！这里是 [我的修订](https://reviews.freebsd.org/D41705)。

赞助：谷歌（谷歌编程之夏 2023）

## 云平台

更新云相关功能并引入对新云平台的支持。

### FreeBSD 上的 OpenStack

链接：

[OpenStack](https://www.openstack.org/) URL: [https://www.openstack.org/](https://www.openstack.org/)

[FreeBSD 上的 OpenStack](https://github.com/openstack-on-freebsd) URL: [https://github.com/openstack-on-freebsd](https://github.com/openstack-on-freebsd)

联系人：Chih-Hsin Chang [starbops@hey.com](mailto:starbops@hey.com)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

OpenStack 是一款开源云操作系统，为在云平台上部署各种资源提供了宝贵支持。然而，在 FreeBSD 主机上运行 OpenStack 控制平面存在挑战。本项目旨在使 FreeBSD 能够无缝作为 OpenStack 主机运行。

本季度，我们专注于概念验证（POC）的最后一部分：VM 控制台集成。目标是让用户通过 OpenStack 客户端获取串行控制台，以访问运行在基于 FreeBSD 的 OpenStack 集群上的 VM 实例。这一点很重要，因为目前 Neutron 的托管 DHCP 服务尚无可用 Port，用户需手动配置 VM 实例的正确 IP 才能连网。然而，[bhyve(8)](https://man.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8&format=html) 原生不支持串行控制台，我们需通过网络导出 [nmdm(4)](https://man.freebsd.org/cgi/man.cgi?query=nmdm&sektion=4&format=html) 设备。实现方式是使用自定义代理 [`socat-manager`](https://github.com/openstack-on-freebsd/socat-manager/blob/main/server.py)，并借助 [socat(1)](https://man.freebsd.org/cgi/man.cgi?query=socat&sektion=1&format=html) 监听 OpenStack `nova-compute` 分配的特定端口，再通过 [bhyve 的自定义 Libvirt hook](https://github.com/openstack-on-freebsd/socat-manager/tree/main/hooks) 将两端连接，实现控制台访问。在开发 hook 脚本过程中，我们发现 Libvirt 为 bhyve 提供的 hook 接口 [实现不完善](https://gitlab.com/libvirt/libvirt/-/issues/528)，所幸 Libvirt 开发者及时 [修复了问题](https://gitlab.com/libvirt/libvirt/-/commit/ad8c4d9d6d09d51a9530ed84fcd2220713aab928)，未来我们将对 hook 脚本进行优化。

我们还解决了嵌套 bhyve 问题（在 Linux KVM 上运行 bhyve VM），该问题在上季度报告中提及，由 APIC 模拟的两个 VT-x 特性 `VID` 和 `PostIntr` 引起。由于主机 CPU 拥有这些特性，我们需在作为 bhyve 主机的 L1 虚拟机中在 **/boot/loader.conf** 禁用它们，以避免 L2 虚拟机宕机。这对于在完全虚拟化环境中进行项目开发至关重要，也降低了其他用户在其环境中尝试或验证整个 POC 的门槛。

展望第四季度，我们将完成 POC 并修订文档，同时移植至 FreeBSD 14.0-RELEASE。缺少对应 FreeBSD 包的依赖将逐一 port。我们还计划与 OpenStack [2023.1 Antelope](https://releases.openstack.org/antelope/index.html) 版本对齐。欢迎有兴趣的人员查阅文档并参与项目。

赞助：FreeBSD 基金会

### 微软 HyperV 和 Azure 上的 FreeBSD

链接：

[FreeBSD wiki 上的 Microsoft Azure 文章](https://wiki.freebsd.org/MicrosoftAzure) URL: [https://wiki.freebsd.org/MicrosoftAzure](https://wiki.freebsd.org/MicrosoftAzure)

[FreeBSD wiki 上的 Microsoft HyperV 文章](https://wiki.freebsd.org/HyperV) URL: [https://wiki.freebsd.org/HyperV](https://wiki.freebsd.org/HyperV)


联系人：微软 FreeBSD 集成服务小组 [bsdic@microsoft.com](mailto:bsdic@microsoft.com)

联系人：[freebsd-cloud 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-cloud)

联系人：FreeBSD Azure Release Engineering Team [releng-azure@FreeBSD.org](mailto:releng-azure@FreeBSD.org)

联系人：Wei Hu [whu@FreeBSD.org](mailto:whu@FreeBSD.org)

联系人：Souradeep Chakrabarti [schakrabarti@microsoft.com](mailto:schakrabarti@microsoft.com)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

本季度，我们主要工作在 ARM64 架构支持，以及构建并发布基于 UFS 和 ZFS 的镜像至 [Azure 社区图库](https://learn.microsoft.com/azure/virtual-machines/share-gallery-community)。项目测试公共图库中有部分测试镜像，名称为 `FreeBSDCGTest-d8a43fa5-745a-4910-9f71-0c9da2ac22bf`：

* FreeBSD-CURRENT-testing
* FreeBSD-CURRENT-gen2-testing
* FreeBSD-CURRENT-arm64-testing
* FreeBSD-CURRENT-zfs-testing
* FreeBSD-CURRENT-zfs-gen1-testing

使用方法：创建虚拟机时，在“选择镜像”步骤中选择“其他项”下的“社区镜像”，然后搜索 `FreeBSD`。

我们的目标是为 14.0-RELEASE 提供所有这些镜像。

进行中的任务：

* 自动化镜像构建与发布流程，并合并到 src/release/
* 构建并发布所有支持的 VM 镜像到 Azure Marketplace
* 构建并发布快照版本至 Azure community gallery

上述任务由 FreeBSD 基金会赞助，微软提供资源支持。

Wei Hu 和 Souradeep Chakrabarti 修复了 ARM64 上的若干关键 bug：

* [https://bugs.freebsd.org/267654](https://bugs.freebsd.org/267654)
* [https://bugs.freebsd.org/272461](https://bugs.freebsd.org/272461)
* [https://bugs.freebsd.org/272666](https://bugs.freebsd.org/272666)

根因已在 [e7a9817b8d32: Hyper-V: vmbus: implementat bus_get_dma_tag in vmbus](https://cgit.freebsd.org/src/commit/?id=e7a9817b8d328dda04069b65944ce2ed6f54c6f0) 修复。

继续改进 Microsoft Azure 网络适配器（MANA）支持。

待办事项：

* 更新 FreeBSD 相关文档于 [Microsoft Learn](https://learn.microsoft.com/)
* 支持 FreeBSD 在 [Azure Pipelines](https://azure.microsoft.com/products/devops/pipelines/) 上运行
* 将 [Azure agent port](https://www.freshports.org/sysutils/azure-agent) 更新至最新版本
* 回溯 [Azure agent 本地修改](https://github.com/Azure/WALinuxAgent/pull/1892)

赞助：微软（人员及资源支持）

赞助：FreeBSD 基金会（其他所有支持）

### EC2 上的 FreeBSD

链接：

[FreeBSD/EC2 Patreon](https://www.patreon.com/cperciva) URL: [https://www.patreon.com/cperciva](https://www.patreon.com/cperciva)

联系人：Colin Percival [cperciva@FreeBSD.org](mailto:cperciva@FreeBSD.org)

FreeBSD 可在 x86（Intel 和 AMD）和 ARM64（Graviton）EC2 实例上使用。工作仍在进行，以确保将来发布的实例类型能够得到支持。

每周 FreeBSD 快照现在包括针对 14.0 和 15.0 的实验性采用 ZFS 根分区的 AMI。此更改将在 FreeBSD 14.0-RELEASE 中生效。

正在进行发布实验性“cloud-init” AMI 的工作，预计将赶上 FreeBSD 14.0-RELEASE 发布。

该工作由 Colin 的 FreeBSD/EC2 Patreon 支持。

## 文档

文档树、手册页或新的外部书籍/文档的重要变化。

### 文档工程团队

链接：

[FreeBSD 文档项目](https://www.freebsd.org/docproj/) URL: [https://www.freebsd.org/docproj/](https://www.freebsd.org/docproj/)

[新贡献者 FreeBSD 文档项目指南](https://docs.freebsd.org/en/books/fdp-primer/) URL: [https://docs.freebsd.org/en/books/fdp-primer/](https://docs.freebsd.org/en/books/fdp-primer/)

[文档工程团队](https://www.freebsd.org/administration/#t-doceng) URL: [https://www.freebsd.org/administration/#t-doceng](https://www.freebsd.org/administration/#t-doceng)

联系人：FreeBSD 文档工程团队团队 [doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)

文档工程团队负责处理 FreeBSD 文档团队相关的一些元项目问题；更多信息请参见 [文档工程团队章程](https://www.freebsd.org/internal/doceng/)。

本季度：

* 文档门户的搜索功能从 DuckDuckGo 转移到我们自己的搜索引擎；更多信息见 [此提交](https://cgit.freebsd.org/doc/commit/?id=ac4fd34edfa1e5e2edb6fb9fc61acd782a0ed33b)
* 根据请求，grahamperrin@ 的 doc 提交权限被暂存
* 根据请求，pluknet@ 的 doc 提交权限被暂存

#### Port 开发者手册

手册中新增了 `USES` 选项：

* [`USES= ebur128`](https://cgit.freebsd.org/doc/commit/?id=ee08121ef177489c031870601de1cc728de646e5)
* [`USES= guile`](https://cgit.freebsd.org/doc/commit/?id=4f16184d81f1c02196d91e8d2511f23fd48e8822)

#### Weblate 上的 FreeBSD 翻译

链接：

[在 Weblate 上翻译 FreeBSD](https://wiki.freebsd.org/Doc/Translation/Weblate) URL: [https://wiki.freebsd.org/Doc/Translation/Weblate](https://wiki.freebsd.org/Doc/Translation/Weblate)

[FreeBSD Weblate 实例](https://translate-dev.freebsd.org/) URL: [https://translate-dev.freebsd.org/](https://translate-dev.freebsd.org/)

##### 2023 年第三季度状态

* 17 种团队语言
* 189 位注册用户

四位新翻译人员加入 Weblate：

* minso：韩语（ko）和法语（fr_FR）
* strgalt-t：德语（de_DE）
* bsdmeg：德语（de_DE）
* mvsf：葡萄牙语（pt_BR）

##### 语言进度

* 中文（简体)](zh-cn) (进度：7%)
* 中文（繁体)](zh-tw) (进度：3%)
* 荷兰语 (nl) (进度：1%)
* 法语 (fr) (进度：1%)
* 德语 (de) (进度：1%)
* 印度尼西亚语 (id) (进度：1%)
* 意大利语 (it) (进度：5%)
* 韩语 (ko) (进度：33%)
* 挪威语 (nb-no) (进度：1%)
* 波斯语 (fa-ir) (进度：2%)
* 波兰语 (进度：1%)
* 葡萄牙语 (pt-br) (进度：22%)
* 西班牙语 (es) (进度：35%)
* 土耳其语 (tr) (进度：2%)

感谢所有参与翻译或审阅文档的人员。同时请在本地用户组中推广此工作，我们始终需要更多志愿者。

#### FreeBSD 手册工作组

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

* [已重写网络章节](https://reviews.freebsd.org/D40546)
* [已重写 Jail 章节已](https://cgit.freebsd.org/doc/commit/?id=612b7cc1721224c494c5b2600188e1508bb5611b)
* 下一步工作是文件系统部分：UFS、OpenZFS、其他文件系统

#### FAQ 工作组

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

计划编写新的 FAQ，随 FreeBSD 14.0 一起发布。

#### FreeBSD 网站改版 — WebApps 工作组

联系人：Sergio Carlavilla [carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)

负责创建新的 FreeBSD Documentation Portal 并重新设计 FreeBSD 主网站及其组件。开发者可在 FreeBSD Slack 频道 #wg-www21 关注并加入工作组。工作分三阶段：

1. Web 上的手册页重设计
   使用 mandoc 生成 HTML 页面脚本。（*已完成，Doceng 批准，部署日期待定*）公共实例：[https://man-dev.FreeBSD.org](https://man-dev.freebsd.org/)
2. FreeBSD 主网站重设计
   新设计，响应式及暗色主题。（*几乎完成，已在 EuroBSDCon 展示*）
3. Web 上的 Ports 页面重设计
   使用 Ports 脚本创建应用门户。（*进行中*）

### FreeBSD 在线文档编辑器和 Man 页面编辑器

链接：

[FreeBSD 在线文档编辑器](https://github.com/Wang-Yan-Hao/FreeBSD-Online-Document-Editor) URL: [https://github.com/Wang-Yan-Hao/FreeBSD-Online-Document-Editor](https://github.com/Wang-Yan-Hao/FreeBSD-Online-Document-Editor)

[FreeBSD 在线 Man 页面编辑器](https://github.com/Wang-Yan-Hao/man_page_editor) URL: [https://github.com/Wang-Yan-Hao/man_page_editor](https://github.com/Wang-Yan-Hao/man_page_editor)

联系人：Yan-Hao Wang [bses30074@gmail.com](mailto:bses30074@gmail.com)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

目前我们的文档翻译流程包括使用 Weblate 和直接编辑 [doc](https://cgit.freebsd.org/doc/) 仓库。我们认识到此流程略显繁琐，因此致力于提供更便捷的替代方案，类似 wiki 社区的操作。引入在线文档编辑器和 Man 页面编辑器，这是一个用户友好、所见即所得的静态站点，旨在翻译文档和手册页。我们的目标是将所有翻译功能整合到单一平台，使翻译过程尽可能简便。

然而，我们仍需要以下支持：

1. 文档编辑器和 Man 页面编辑器使用简单 JavaScript 开发。我们希望前端开发人员评估代码效率，因为我（Yan-Hao Wang）前端经验有限。
2. 我们还需要网络安全开发人员协助发现并解决安全问题，以确保项目安全托管并降低潜在漏洞。
3. 由于目前没有现成 JavaScript 库渲染 mandoc，我自行创建了一个，但在编辑过程中仍存在一些隐藏错误。我们需要 JavaScript 开发人员帮助修复这些渲染问题。

赞助：FreeBSD 基金会

### FreeBSD 专家系统

链接：

[FreeBSD Expert System](https://github.com/Wang-Yan-Hao/freebsd_expert_system) URL: [https://github.com/Wang-Yan-Hao/freebsd_expert_system](https://github.com/Wang-Yan-Hao/freebsd_expert_system)

联系人：Yan-Hao Wang [bses30074@gmail.com](mailto:bses30074@gmail.com)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

机器学习和深度学习技术在当今世界越来越普及，就像 ChatGPT 的广泛应用一样。我们正在开发一个 ChatGPT 插件，使其能够访问最新的 FreeBSD 数据，从而将 ChatGPT 转变为 FreeBSD 专家系统。我们已经完成了数据清理脚本编写，并构建了一个嵌入式模型以搜索相关信息。

然而，在项目的以下方面我们仍需要帮助：

* 因为我不是机器学习或深度学习专家，可在这些领域我们遇到了许多困难，例如数据清理的充分性以及最终插件开发过程中的不确定性。我们希望在这方面获得指导。

赞助：FreeBSD 基金会

## Ports

影响 Ports 的更改，包括触及大部分树的广泛变动或单个 Port 的修改。

### FreeBSD 上的 KDE

链接：

[KDE/FreeBSD 项目](https://freebsd.kde.org/) URL: [https://freebsd.kde.org/](https://freebsd.kde.org/)

[FreeBSD — KDE 社区 Wiki](https://community.kde.org/FreeBSD) URL: [https://community.kde.org/FreeBSD](https://community.kde.org/FreeBSD)

联系人：Adriaan de Groot [kde@FreeBSD.org](mailto:kde@FreeBSD.org)

FreeBSD 上的 KDE 项目为 Ports 树打包了 CMake、Qt 及 KDE 社区软件。软件包括完整桌面环境 KDE Plasma（支持 X11 和 Wayland）及数百个可在任何 FreeBSD 机器上使用的应用程序。

KDE 团队（kde@）隶属于 desktop@ 和 x11@，构建软件栈，使 FreeBSD 成为可日常使用的图形桌面工作站。以下内容主要描述 KDE 的 Ports，但也涵盖整个桌面栈的重要项目。

#### 基础设施

Qt5 现已进入长期支持，仅偶尔更新。本季度更新到 5.15.10。Qt6 随上游发布定期更新，7 月底发布 6.5.2，随后更新 6.5.3。

CMake 本季度无更新，因此至少落后一个小版本。最新版本的更新日志对 FreeBSD 没有特别内容，因此无需升级。

[sysutils/polkit](https://cgit.freebsd.org/ports/tree/sysutils/polkit/) 和 [sysutils/consolekit2](https://cgit.freebsd.org/ports/tree/sysutils/consolekit2/) 均已更新，为 FreeBSD 桌面提供更好的安全策略和控制台处理。[x11/sddm](https://cgit.freebsd.org/ports/tree/x11/sddm/) 更新以提供更好的图形登录管理器。

[multimedia/pipewire](https://cgit.freebsd.org/ports/tree/multimedia/pipewire/) 更新到 0.3.81，为 KDE 和 GNOME 等桌面提供多媒体支持。

#### KDE 栈

KDE Gear 每季度发布，KDE Plasma 每月更新，KDE Frameworks 每月也有新版本。这些大型更新在上游发布后不久合并，不单独列出。

* KDE Frameworks 达到 5.110 版本。KDE Frameworks 5 系列正在收尾，约六个月后上游进入长期支持。
* KDE Plasma Desktop 更新至 5.27.8。与 Frameworks 类似，KDE Plasma 5 的开发正逐渐结束，上游将转向 KDE Plasma 6。
* KDE Gear 更新至 23.08.1。

#### 相关 Ports

KDE 生态包含大量的 Ports，大部分由 kde@ 维护，均基于 Qt 和 KDE Frameworks。kde@ 团队根据需要更新所有相关 Ports。本季度，例如 tcberner@ 和 arrowd@ 更新或修复了以下 Ports（远不止这些）：

* [astro/merkaartor](https://cgit.freebsd.org/ports/tree/astro/merkaartor/)
* [devel/massif-visualizer](https://cgit.freebsd.org/ports/tree/devel/massif-visualizer/)
* [finance/alkimia](https://cgit.freebsd.org/ports/tree/finance/alkimia/)
* [irc/quassel](https://cgit.freebsd.org/ports/tree/irc/quassel/)
* [net-im/kaidan](https://cgit.freebsd.org/ports/tree/net-im/kaidan/)
* [sysutils/bsdisks](https://cgit.freebsd.org/ports/tree/sysutils/bsdisks/)
* [sysutils/k3b](https://cgit.freebsd.org/ports/tree/sysutils/k3b/)

感谢 jhale@ 更新了 [devel/qtcreator](https://cgit.freebsd.org/ports/tree/devel/qtcreator/) 至 11.0.3，为 Qt 和 KDE 应用开发提供更多功能的集成开发环境。

#### 弃用

Web 浏览器体积大，安全面广。已计划移除老旧的 WebKit Port [www/qt5-webkit](https://cgit.freebsd.org/ports/tree/www/qt5-webkit/)，用户已迁移至 WebEngine。所依赖的 WebKit 分支已不再维护。

### FreeBSD 上的 Pantheon 桌面

链接：

[elementary OS](https://elementary.io/) URL: [https://elementary.io/](https://elementary.io/)

[开发仓库](https://codeberg.org/olivierd/freebsd-ports-elementary) URL: [https://codeberg.org/olivierd/freebsd-ports-elementary](https://codeberg.org/olivierd/freebsd-ports-elementary)

联系人：Olivier Duchateau [duchateau.olivier@gmail.com](mailto:duchateau.olivier@gmail.com)

Pantheon 桌面环境为 elementary OS 设计，基于 GNOME 技术（如 Mutter、GTK 3 和 4），使用 Vala 编写。目标是为最终用户提供完整桌面环境。

因部分核心组件依赖 [deskutils/xdg-desktop-portal](https://cgit.freebsd.org/ports/tree/deskutils/xdg-desktop-portal/)，**需要 13.2-RELEASE 或更高版本**。

仓库包含 **elementary.mk** 文件，用于 **Mk/Uses** 框架、官方应用和依赖 [x11-toolkits/granite7](https://cgit.freebsd.org/ports/tree/x11-toolkits/granite7/) 的精选 Port。

我已提交多项补丁以保持这些 Port 更新：

* [deskutils/iconbrowser](https://cgit.freebsd.org/ports/tree/deskutils/iconbrowser/)
* [multimedia/elementary-videos](https://cgit.freebsd.org/ports/tree/multimedia/elementary-videos/)
* [x11-themes/gnome-icons-elementary](https://cgit.freebsd.org/ports/tree/x11-themes/gnome-icons-elementary/)
* [editors/elementary-code](https://cgit.freebsd.org/ports/tree/editors/elementary-code/)

Bugzilla 上仍有以下 Ports 的更新问题待解决：[bug 列表](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&query_format=advanced&short_desc=elementary-calendar%20elementary-terminal%20granite7&short_desc_type=anywordssubstr)：

* [x11-toolkits/granite7](https://cgit.freebsd.org/ports/tree/x11-toolkits/granite7/)：更新至 7.3.0
* [deskutils/elementary-calendar](https://cgit.freebsd.org/ports/tree/deskutils/elementary-calendar/)：更新至 7.0.0
* [x11/elementary-terminal](https://cgit.freebsd.org/ports/tree/x11/elementary-terminal/)：更新至 6.1.2

同时，我也在更新 GNOME 栈（尤其是 WebKitGTK、libwnck、Mutter、Vala），发现 [x11/plank](https://cgit.freebsd.org/ports/tree/x11/plank/) 出现若干回归（与监控打开的应用相关）。

开发仓库中新增三个应用：

* deskutils/atlas：地图查看器
* deskutils/nimbus：天气小工具
* audio/leopod：播客客户端

### FreeBSD Office 团队

链接：

[FreeBSD Office 项目](https://wiki.freebsd.org/Office) URL: [https://wiki.freebsd.org/Office](https://wiki.freebsd.org/Office)

[FreeBSD Office 邮件列表](https://lists.freebsd.org/subscription/freebsd-office) URL: [https://lists.freebsd.org/subscription/freebsd-office](https://lists.freebsd.org/subscription/freebsd-office)

联系人：FreeBSD Office 团队 ML [office@FreeBSD.org](mailto:office@FreeBSD.org)

联系人：Dima Panov [fluffy@FreeBSD.org](mailto:fluffy@FreeBSD.org)

联系人：許立文 [lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)

FreeBSD Office 团队致力于办公相关软件套件和工具，如 OpenOffice 和 LibreOffice。

本季度工作重点是向所有 FreeBSD 用户提供最新稳定版本的 LibreOffice 套件及配套应用。

2023 年第三季度期间，我们为 LibreOffice Port 推送维护补丁，并将最新 7.6.2 版本及所有配套库（如 MDDS、libIxion 等）引入 Ports 树。LibreOffice Ports 的所有预发布开发均在 [LibreOffice WIP 仓库](https://github.com/freebsd/freebsd-ports-libreoffice) 中进行。

同时，我们将 Boost 更新至最新 1.83 版本。所有对 Boost Porting 感兴趣的人员可向 [Boost WIP 仓库](https://github.com/fluffykhv/freebsd-ports-boost) 提交补丁。

我们正在寻找帮助完成以下开放任务的人：

* [开放 Bug 列表](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=office%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=substring&list_id=650685&order=Bug+Number&query_format=advanced) 包含所有待处理问题
* 回溯 [Ports 中的本地补丁](https://cgit.freebsd.org/ports/tree/editors/libreoffice/files)

补丁、意见和异议均欢迎在邮件列表和 Bugzilla 中提交。

### Wifibox：在 FreeBSD 上用 Linux 驱动你的无线网卡

链接：

[项目 GitHub 页面](https://github.com/pgj/freebsd-wifibox) URL: [https://github.com/pgj/freebsd-wifibox](https://github.com/pgj/freebsd-wifibox)

[net/wifibox Port](https://cgit.freebsd.org/ports/tree/net/wifibox) URL: [https://cgit.freebsd.org/ports/tree/net/wifibox](https://cgit.freebsd.org/ports/tree/net/wifibox)

联系人：PÁLI Gábor János [pali.gabor@gmail.com](mailto:pali.gabor@gmail.com)

Wifibox 是一项实验性项目，用于探索在 FreeBSD 主机系统上通过虚拟化 Linux 客机驱动无线网卡的方法。已有手动设置指南，而 Wifibox 旨在将这些想法整合为一个易于使用的软件包。

* 它使用 [bhyve(8)](https://man.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8&format=html) 运行嵌入式 Linux 系统，从而实现低资源占用。要求 x64 CPU 带 I/O MMU（AMD-Vi、Intel VT-d）、约 150 MB 物理内存，以及可用磁盘空间用于虚拟机虚拟磁盘镜像，在某些情况下仅需约 30 MB。适用于 FreeBSD 12 及更高版本，部分网卡可能需要 FreeBSD 13。
* 虚拟机使用 [Alpine Linux](https://alpinelinux.org/)，这是一个面向安全的轻量级发行版，基于 [musl libc](https://www.musl-libc.org/) 和 [BusyBox](https://busybox.net/)，并引入了一些来自 [Arch Linux](https://archlinux.org/) 的自定义扩展和补丁。内置多种诊断工具以便更好管理硬件。近期版本基于 Linux 6.1，也可选择 Linux 6.5。
* 配置文件与主机系统共享。虚拟机可使用 [wpa_supplicant(8)](https://man.freebsd.org/cgi/man.cgi?query=wpa_supplicant&sektion=8&format=html) 或 [hostapd(8)](https://man.freebsd.org/cgi/man.cgi?query=hostapd&sektion=8&format=html)](取决于配置），可直接导入主机的 [wpa_supplicant.conf(5)](https://man.freebsd.org/cgi/man.cgi?query=wpa_supplicant.conf&sektion=5&format=html) 或 [hostapd.conf(5)](https://man.freebsd.org/cgi/man.cgi?query=hostapd.conf&sektion=5&format=html) 文件，无需修改。
* 配置完成后，客机可暴露 [wpa_supplicant(8)](https://man.freebsd.org/cgi/man.cgi?query=wpa_supplicant&sektion=8&format=html) 和 [hostapd(8)](https://man.freebsd.org/cgi/man.cgi?query=hostapd&sektion=8&format=html) 的控制套接字，使主机可直接使用相关工具，如 [wpa_cli(8)](https://man.freebsd.org/cgi/man.cgi?query=wpa_cli&sektion=8&format=html)、[wpa_gui(8)](https://man.freebsd.org/cgi/man.cgi?query=wpa_gui&sektion=8&format=html)](来自 [net/wpa_supplicant_gui](https://cgit.freebsd.org/ports/tree/net/wpa_supplicant_gui/) 包）或 [hostapd_cli(8)](https://man.freebsd.org/cgi/man.cgi?query=hostapd_cli&sektion=8&format=html)。
* 软件以单一包形式提供，易于安装和卸载，带 [rc(8)](https://man.freebsd.org/cgi/man.cgi?query=rc&sektion=8&format=html) 系统服务，可在启动时自动运行客机，关机时自动停止。
* 可配置 IPv6 流量转发，当前为实验性选项，默认开启。

Wifibox 已在 Intel 芯片组上进行了大量测试，表现出良好的性能与稳定性，可作为 FreeBSD 对这些芯片组支持尚未完善时的过渡方案。

已确认 Wifibox 可用于 Atheros、Realtek 和 Mediatek 芯片组，欢迎对其他芯片组提供反馈。博通芯片（常见于 MacBook Pro）也可工作，但存在已知的稳定性问题。

### 容器与 FreeBSD：Pot、Potluck 与 Potman

链接：

[Pot 组织 GitHub 页面](https://github.com/bsdpot) URL: [https://github.com/bsdpot](https://github.com/bsdpot)

联系人：Luca Pizzamiglio (Pot) [pizzamig@FreeBSD.org](mailto:pizzamig@FreeBSD.org)

联系人：Bretton Vine (Potluck) [bv@honeyguide.eu](mailto:bv@honeyguide.eu)

联系人：Michael Gmelin (Potman) [grembo@FreeBSD.org](mailto:grembo@FreeBSD.org)


Pot 是一款 jail 管理工具，同时支持通过 Nomad 进行编排。[详细说明](https://www.freebsd.org/news/status/report-2020-01-2020-03/#pot-and-the-nomad-pot-driver)。

本季度完成了 [Pot 0.15.6](https://github.com/bsdpot/pot/pull/274) 的开发，新增了自定义 [pf(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&format=html) 规则配置钩子。

此外，还发布了 [Nomad Pot Driver 0.9.1](https://github.com/bsdpot/nomad-pot-driver/releases/tag/v0.9.1)，能在 Nomad 作业描述中设置 Pot 属性。

Potluck 的目标是成为 FreeBSD 和 Pot 的“Dockerhub”：提供 Pot flavours 和完整容器镜像的仓库，可用于 Pot，并在许多情况下与 Nomad 配合使用。

本季度提供了许多新的容器镜像，例如：[Caddy S3 代理](https://github.com/bsdpot/potluck/tree/master/caddy-s3-nomad)、[Mastodon 实例](https://github.com/bsdpot/potluck/tree/master/mastodon-s3) 和 [Redis 容器](https://github.com/bsdpot/potluck/tree/master/redis-single)。目前共有 50 个容器可用，可通过 [Potluck 镜像注册表](https://potluck.honeyguide.net/) 下载预构建镜像（如果信任我们的构建过程），或从 [Potluck GitHub 仓库](https://github.com/bsdpot/potluck) 中的 Pot flavour 文件自行构建。

2023 年 7/8 月的 FreeBSD Journal 包含 Luca 的文章 [使用 pot 与 nomad 编排 Jail](https://freebsdfoundation.org/wp-content/uploads/2023/08/Pizzamiglio.pdf)，说明如何将 Pot 和 Potluck 与 Nomad 配合，在多台主机上编排容器。

最后，补丁 ([90b1184d93c8](https://cgit.freebsd.org/ports/commit/?id=90b1184d93c8)) 为 Port [devel/sccache](https://cgit.freebsd.org/ports/tree/devel/sccache/) 添加了构建集群支持。

一如既往，欢迎反馈和提交补丁。

赞助方：Nikulipe UAB, Honeyguide Group
