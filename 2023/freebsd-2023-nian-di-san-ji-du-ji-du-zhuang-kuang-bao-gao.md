# FreeBSD 2023 年第三季度状态报告

- 原文地址：<https://www.freebsd.org/status/report-2023-07-2023-09/>
- 译者：ChatGPT & ykla

这是 2023 年第三季度的状态报告，共包含 32 个条目。

这一季度是夏季，因此包含了许多有趣的来自谷歌编程之夏的新闻。当然，我们也有我们通常的团队报告，许多项目与我们分享了它们的最新动态。为 FreeBSD 14 的第一次发布做了许多重要的工作。

祝你阅读愉快。

Lorenzo Salvadore，代表状态团队。

目录

- [FreeBSD 团队报告](https://www.freebsd.org/status/report-2023-07-2023-09/#FreeBSD-Team-Reports)

  - [FreeBSD 核心团队](https://www.freebsd.org/status/report-2023-07-2023-09/#_freebsd_core_team)
  - [FreeBSD 基金会](https://www.freebsd.org/status/report-2023-07-2023-09/#_freebsd_foundation)
  - [FreeBSD 发布工程团队](https://www.freebsd.org/status/report-2023-07-2023-09/#_freebsd_release_engineering_team)
  - [持续集成](https://www.freebsd.org/status/report-2023-07-2023-09/#_continuous_integration)
  - [Ports](https://www.freebsd.org/status/report-2023-07-2023-09/#_ports_collection)

- [项目](https://www.freebsd.org/status/report-2023-07-2023-09/#projects)

  - [填补 FreeBSD 桌面体验中的空白](https://www.freebsd.org/status/report-2023-07-2023-09/#_filling_gaps_in_the_freebsd_desktop_experience)
  - [LLDB 内核模块改进](https://www.freebsd.org/status/report-2023-07-2023-09/#_lldb_kernel_module_improvement)

- [用户空间](https://www.freebsd.org/status/report-2023-07-2023-09/#userland)

  - [基于 Base 的 OpenSSL 3 —  改进](https://www.freebsd.org/status/report-2023-07-2023-09/#_openssl_3_in_baseimproved)
  - [登录类修复和改进](https://www.freebsd.org/status/report-2023-07-2023-09/#_login_classes_fixes_and_improvements)

- [内核](https://www.freebsd.org/status/report-2023-07-2023-09/#kernel)

  - [在使用日志软更新的文件系统上启用快照](https://www.freebsd.org/status/report-2023-07-2023-09/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates)
  - [FreeBSD 内核的 SquashFS 驱动程序](https://www.freebsd.org/status/report-2023-07-2023-09/#_squashfs_driver_for_freebsd_kernel)
  - [进程可见性安全策略](https://www.freebsd.org/status/report-2023-07-2023-09/#_process_visibility_security_policies)
  - [Linux 兼容性层更新](https://www.freebsd.org/status/report-2023-07-2023-09/#_linux_compatibility_layer_update)

- [体系结构](https://www.freebsd.org/status/report-2023-07-2023-09/#architectures)

  - [NXP DPAA2 支持](https://www.freebsd.org/status/report-2023-07-2023-09/#_nxp_dpaa2_support)
  - [amd64 的 SIMD 增强](https://www.freebsd.org/status/report-2023-07-2023-09/#_simd_enhancements_for_amd64)
  - [将 mfsBSD 集成到发布构建工具中](https://www.freebsd.org/status/report-2023-07-2023-09/#_integrate_mfsbsd_into_the_release_building_tools)

- [云](https://www.freebsd.org/status/report-2023-07-2023-09/#cloud)

  - [FreeBSD 上的 OpenStack](https://www.freebsd.org/status/report-2023-07-2023-09/#_openstack_on_freebsd)
  - [FreeBSD 在 Microsoft HyperV 和 Azure 上](https://www.freebsd.org/status/report-2023-07-2023-09/#_freebsd_on_microsoft_hyperv_and_azure)
  - [FreeBSD 在 EC2 上](https://www.freebsd.org/status/report-2023-07-2023-09/#_freebsd_on_ec2)

- [文档](https://www.freebsd.org/status/report-2023-07-2023-09/#documentation)

  - [文档工程团队](https://www.freebsd.org/status/report-2023-07-2023-09/#_documentation_engineering_team)
  - [FreeBSD 在线编辑器和手册编辑器](https://www.freebsd.org/status/report-2023-07-2023-09/#_freebsd_online_editor_and_man_page_editor)
  - [FreeBSD 专家系统](https://www.freebsd.org/status/report-2023-07-2023-09/#_freebsd_expert_system)

- [port](https://www.freebsd.org/status/report-2023-07-2023-09/#ports)

  - [FreeBSD 上的 KDE](https://www.freebsd.org/status/report-2023-07-2023-09/#_kde_on_freebsd)
  - [FreeBSD 上的 Pantheon 桌面](https://www.freebsd.org/status/report-2023-07-2023-09/#_pantheon_desktop_on_freebsd)
  - [FreeBSD 办公团队](https://www.freebsd.org/status/report-2023-07-2023-09/#_freebsd_office_team)
  - [Wifibox：使用 Linux 驱动 FreeBSD 上的无线网卡](https://www.freebsd.org/status/report-2023-07-2023-09/#_wifibox_use_linux_to_drive_your_wireless_card_on_freebsd)
  - [FreeBSD 上的 GCC](https://www.freebsd.org/status/report-2023-07-2023-09/#_gcc_on_freebsd)
  - [Valgrind：为 FreeBSD 15 更新的 valgrind-devel](https://www.freebsd.org/status/report-2023-07-2023-09/#_valgrind_valgrind_devel_updated_for_freebsd_15)
  - [GitLab 16.3 可用](https://www.freebsd.org/status/report-2023-07-2023-09/#_gitlab_16_3_available)
  - [PortOptsCLI — Ports 可访问性](https://www.freebsd.org/status/report-2023-07-2023-09/#_portoptscliports_collection_accessibility)

- [第三方项目](https://www.freebsd.org/status/report-2023-07-2023-09/#third-Party-Projects)

  - [介绍 BSD Cafe 项目](https://www.freebsd.org/status/report-2023-07-2023-09/#_introducing_the_bsd_cafe_project)
  - [容器和 FreeBSD：Pot、Potluck 和 Potman](https://www.freebsd.org/status/report-2023-07-2023-09/#_containers_and_freebsd_pot_potluck_and_potman)

## FreeBSD 团队报告

来自各个官方和半官方团队的条目，详见[管理页面](https://www.freebsd.org/administration/)。

### FreeBSD 核心团队

联系方式：FreeBSD 核心团队 <[core@FreeBSD.org](mailto:core@FreeBSD.org)>

FreeBSD 核心团队是 FreeBSD 的治理机构。

#### Hans Petter Selasky 的逝世

FreeBSD 核心团队感谢 Hans Petter Selasky 多年来的贡献。我们对他的离世感到悲痛，并与社区共同悼念。

[悼念文章](https://lists.freebsd.org/archives/freebsd-announce/2023-July/000076.html)。

#### 与 FreeBSD 基金会的会议

核心团队继续与 FreeBSD 基金会会晤，讨论 FreeBSD 的管理、开发和未来的下一步。核心团队与基金会董事会及其员工进行了两次会议。他们讨论了基金会如何帮助核心团队和整个项目。

#### Portmgr termlimits

核心团队与 Ports 管理团队讨论了引入一个开发者在团队中的时间限制的提案。该提案得到了 Ports 管理团队的批准，并将于 2024 年初生效，届时将定期进行潜在成员计划，以确保 Ports 管理团队有持续的新成员流动。

#### FreeBSD 15 中弃用 32 位平台

正在进行工作，将对 FreeBSD 15 中 32 位平台的支持标记为“弃用”。

#### Matrix 即时通讯

Matrix 实例和 Element-web 客户端的测试仍在进行中。计划在九月的 EuroBSDCon 之后发布 Beta 版本。

#### 改进提交权过期策略

核心团队将说明如果开发者成为了提交者，如何进行 PGP 密钥更新。

#### EuroBSDCon

核心团队成员在 EuroBSDcon 期间与 FreeBSD 基金会在科英布拉会面，讨论项目的方向。

### FreeBSD 基金会

链接：
[FreeBSD 基金会](https://freebsdfoundation.org/) URL: [https://freebsdfoundation.org/](https://freebsdfoundation.org/)

[技术路线图](https://freebsdfoundation.org/blog/technology-roadmap/) URL: [https://freebsdfoundation.org/blog/technology-roadmap/](https://freebsdfoundation.org/blog/technology-roadmap/)

[捐赠](https://freebsdfoundation.org/donate/) URL: [https://freebsdfoundation.org/donate/](https://freebsdfoundation.org/donate/)

[基金会合作伙伴计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/) URL: [https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)

[FreeBSD 期刊](https://freebsdfoundation.org/journal/) URL: [https://freebsdfoundation.org/journal/](https://freebsdfoundation.org/journal/)

[基金会活动](https://freebsdfoundation.org/our-work/events/) URL: [https://freebsdfoundation.org/our-work/events/](https://freebsdfoundation.org/our-work/events/)

联系人：Deb Goodkin <[deb@FreeBSDFoundation.org](mailto:deb@FreeBSDFoundation.org)>

FreeBSD 基金会是一家 501(c)(3) 非营利组织，致力于支持和推动全球 FreeBSD 项目和社区。个人和公司的捐赠赞助和管理软件开发项目、会议和开发者峰会。我们还向 FreeBSD 贡献者提供差旅赞助，购买和支持硬件以改善和维护 FreeBSD 基础设施，并提供资源以提高安全性、质量保证和集群管理工作。我们发布营销材料以推广、教育和宣传 FreeBSD，促进商业供应商与 FreeBSD 开发者之间的合作，并最终代表 FreeBSD 项目执行合同、许可协议和其他需要认可法律实体的安排。

在本季度，我们协助 FreeBSD 庆祝其 30 周年！这一激动人心的时刻推动我们加速努力，推动 FreeBSD 在增长和创新方面取得进展，这使我们集中精力确定可以投入资源的关键领域。在 9 月份的董事会会议上，我们优化了我们的目标，重点放在增加 FreeBSD 的采用和可见性、多元化我们的资金来源，以及投资于项目的社区健康和长期稳定性。我们正在确定目标受众和市场，同时为这些目标制定可衡量的结果。

在本状态报告中，你将更多地了解我们如何助力 FreeBSD 增长和进行创新工作。我们将重点介绍我们通过内部软件开发人员和外部项目资金支持所做的所有技术工作。你将了解我们在推动 FreeBSD 面向社区外受众的宣传工作。最后，你将看到我们为与现有和潜在商业用户建立联系所付出的巨大努力。

#### 筹款

我们要向那些慷慨捐助以支持我们工作的人表示衷心的感谢。除了许多个人贡献之外，我们特别感谢 NetApp、Netflix 和 ARM 的重要捐赠。仅在第三季度，我们就收到了 183,842 美元的捐款，使我们今年的总额达到了 375,000 美元。今年我们的预算约为 2,230,000 美元，其中包括增加用于 FreeBSD 宣传和软件开发的支出。我们一半以上的预算用于直接改进 FreeBSD 并保持其安全。通过一个专注于合作伙伴关系的专门人员，我们可以有效强调投资我们努力的重要性，并强调 FreeBSD 对公司的长期可行性。你的支持对我们的使命至关重要，我们深感你对 FreeBSD 社区的支持。请考虑向我们 2023 年的筹款活动捐款！[https://freebsdfoundation.org/donate/](https://freebsdfoundation.org/donate/) 对于我们更大的商业捐赠者，请查看我们更新的[FreeBSD 基金会合作伙伴计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)。

## 合作与研究

在本季度，合作与研究取得了三个关键领域的进展：

首先，[企业工作组](https://wiki.freebsd.org/EnterpriseWorkingGroup)开始蓬勃发展，参与人数增至 58 人，并在四个工作流中展开积极项目。这些领域分别是云原生、Samba、bhyve 可管理性以及对 AI 工作负载的支持。对其他几个领域也有兴趣，我预计到年底和明年第一季度，我们将在多个关注领域看到有意义的功能更新。

其次，我们在与其他开源社区成员和组织的合作方面取得了良好的进展，特别是与[开源倡议](https://opensource.org/)合作，推动 FreeBSD 社区的提案和技术。与开源倡议的[开放政策联盟](https://opensource.org/programs/open-policy-alliance/)合作，我们正在提交回应美国政府关于如何支持开源安全性和可持续性的信息请求。作为其中的一部分，Greg Wallace 参与了由开放政策联盟在最近在北卡罗来纳州罗利举行的 All Things Open 大会上组织的一个小组讨论。Greg Wallace 还一直在追踪美国政府如何将 CHERI 纳入其有关默认安全性的政策建议中，[例如来自美国和全球政府安全机构的最新报告](https://www.cisa.gov/sites/default/files/2023-10/Shifting-the-Balance-of-Cybersecurity-Risk-Principles-and-Approaches-for-Secure-by-Design-Software.pdf)。在第 28 页，CHERI 被列为关键的“安全设计”策略之后，仅次于 Rust。

最后，我们继续加强与越来越多使用 FreeBSD 的公司的合作关系。多个会议有助于促进这些关系，包括 EuroBSDCon、开源峰会和 All Things Open。我们还制定了一个新的计划，支持与美国政府合作的供应商/云用户。该计划的详细信息将在 FreeBSD 供应商峰会上宣布。

#### 宣传

我们的许多努力都致力于 FreeBSD 项目的宣传。这可能涉及突出显示有趣的 FreeBSD 工作、制作文学和视频教程、参加活动或进行演讲。我们制作文学的目标是教导人们 FreeBSD 的基础知识，并帮助他们更容易地采用或做出贡献。除了参加和在活动中发表演讲之外，我们鼓励并帮助社区成员组织自己的 FreeBSD 活动、进行演讲或设置 FreeBSD 展台。

FreeBSD 基金会赞助了许多全球各地的会议、活动和峰会。这些事件可以是与 BSD 相关的、开源的或面向少数群体的技术事件。我们支持以 FreeBSD 为重点的事件，以帮助提供一个分享知识、共同开发项目和促进开发人员与商业用户之间合作的场所。所有这些都有助于提供一个健康的生态系统。我们参与非 FreeBSD 活动，以推广和提高 FreeBSD 的知名度，增加 FreeBSD 在不同应用中的使用，并招募更多的项目贡献者。我们不断将新的事件添加到我们的年度日程中。今年七月，我们在俄勒冈州波特兰举办的 FOSSY，一场新的开源大会上举办了研讨会并设置了展台。除了参加和策划会议，我们还在不断推动新的培训计划，并更新我们的[指南选择](https://freebsdfoundation.org/freebsd-project/resources/)，以促进更多人尝试 FreeBSD。

查看一些我们的宣传工作：

- 于 2023 年 7 月 13 日至 16 日在俄勒冈州波特兰的[FOSSY](https://sfconservancy.org/fossy/)举办研讨会并设置展台。
- 于 2023 年 7 月 27 日至 29 日在台湾新北市举办的 COSCUP 的友好级赞助商
- 在 EuroBSDCon 2023（2023 年 9 月 14 日至 17 日，葡萄牙科英布拉）上发表演讲，并赞助并设置了展台
- 参加了[Open Source Summit, Europe](https://events.linuxfoundation.org/open-source-summit-europe/)，于 2023 年 9 月 19 日至 21 日在西班牙毕尔巴鄂
- 继续筹划[2023 年 11 月 FreeBSD 供应商峰会](https://freebsdfoundation.org/news-and-events/event-calendar/november-2023-freebsd-vendor-summit/)，于 2023 年 11 月 2 日至 3 日在加利福尼亚州圣何塞举行
- 继续管理我们的谷歌编程之夏项目
- 发布了[七月简报](https://freebsdfoundation.org/news-and-events/newsletter/freebsd-foundation-update-july-2023/)
- 附加博客文章

  - [宣传活动：2023 年 5 月 FreeBSD 开发者峰会和 BSDCan](https://freebsdfoundation.org/blog/advocating-at-events-may-2023-freebsd-dev-summit-and-bsdcan/)
  - [升级到 FreeBSD 13.2 的前十大理由](https://freebsdfoundation.org/blog/top-ten-reasons-to-upgrade-to-freebsd-13-2/)

- [2023 年 7 月软件开发项目更新](https://freebsdfoundation.org/blog/july-2023-software-development-projects-update/)
- [研究中的 FreeBSD：CHERI/Morello](https://freebsdfoundation.org/blog/freebsd-for-research-cheri-morello/)
- 认识 FreeBSD 谷歌编程之夏学生

  - [Soobin Rho](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-soobin-rho/)
  - [Raghav Sharma](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-raghav-sharma/)
  - [Sudhanshu Mohan Kashyap](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-sudhanshu-mohan-kashyap/)
  - [Aymeric Wibo](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-aymeric-wibo/)

- [认识 2023 年滑铁卢大学夏季实习生：Naman Sood](https://freebsdfoundation.org/blog/meet-the-summer-2023-university-of-waterloo-co-op-student-naman-sood/)
- [认识 FreeBSD 基金会 2023 年夏季实习生：Jake Freeland](https://freebsdfoundation.org/blog/meet-freebsd-foundation-2023-summer-intern-jake-freeland/)
- 在新闻中的 FreeBSD

  - [FreeBSD 基金会加入 OSI 的开放政策联盟](https://freebsdfoundation.org/news-and-events/latest-news/freebsd-foundation-joins-osis-open-policy-alliance/)
  - [Hackernoon：我们将开源 FreeBSD 用作企业操作系统的 5 个原因](https://freebsdfoundation.org/news-and-events/latest-news/hackernoon-5-reasons-we-use-open-source-freebsd-as-our-enterprise-os/)
  - [What the Dev Podcast：FreeBSD 项目的演变](https://freebsdfoundation.org/news-and-events/latest-news/what-the-dev-podcast-the-evolution-of-the-freebsd-project/)

我们通过出版专业制作的 FreeBSD 期刊来向全世界宣传 FreeBSD。正如我们先前提到的，FreeBSD Journal 现在是一份免费出版物。了解更多并访问最新杂志，[https://www.freebsdfoundation.org/journal/](https://www.freebsdfoundation.org/journal/)。你可以在[https://freebsdfoundation.org/our-work/events/](https://freebsdfoundation.org/our-work/events/)找到我们参加的事件和即将举行的事件的更多信息。

## 改进操作系统

在 2023 年第三季度，有 282 个 src（源代码）、652 个 port 和 24 个 doc tree（文档）的提交由 FreeBSD 基金会赞助。一些由基金会赞助的工作在单独的报告条目中有所说明：

- [启用使用日志软更新的文件系统上的快照](https://www.freebsd.org/status/report-2023-07-2023-09/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates)
- [登录类修复和改进](https://www.freebsd.org/status/report-2023-07-2023-09/#_login_classes_fixes_and_improvements)
- [OpenSSL 3 在基础设施中的改进](https://www.freebsd.org/status/report-2023-07-2023-09/#_openssl_3_in_baseimproved)
- [FreeBSD 上的 OpenStack](https://www.freebsd.org/status/report-2023-07-2023-09/#_openstack_on_freebsd)
- [进程可见性安全策略](https://www.freebsd.org/status/report-2023-07-2023-09/#_process_visibility_security_policies)
- [amd64 的 SIMD 增强](https://www.freebsd.org/status/report-2023-07-2023-09/#_simd_enhancements_for_amd64)。

技术团队的成员参加了在葡萄牙科英布拉举办的 EuroBSDCon 2023。許立文提供了一项教程，帮助新手为 FreeBSD 做出贡献。在会议之前，FreeBSD 开发者峰会举行，团队在会上提供了一份[关于他们最近工作的简短更新](https://wiki.freebsd.org/DevSummit/202309?action=AttachFile&do=view&target=Foundation_Technology_Team_Devsummit_Fall_2023.pdf)。

六个暑期实习/项目已经结束：

- [Jake Freeland](https://freebsdfoundation.org/blog/meet-freebsd-foundation-2023-summer-intern-jake-freeland/)在夏季期间致力于一个[Capsicum 项目](https://freebsdfoundation.org/project/capsicum-internship/)，用于跟踪违规行为，调整各种守护程序，如[syslogd(8)](https://man.freebsd.org/cgi/man.cgi?query=syslogd&sektion=8&format=html)，并编写文档。
- [Naman Sood](https://freebsdfoundation.org/blog/meet-the-summer-2023-university-of-waterloo-co-op-student-naman-sood/)致力于[各种任务，主要与网络相关](https://freebsdfoundation.org/project/networking-summer-internship/)。
- En-Wei Wu 完成了[另一个无线实习](https://freebsdfoundation.org/project/wireless-internship/)，以改进和扩展 wtap，即 net80211(4) Wi-Fi 模拟器。
- 致力于一个[文档和测试项目](https://freebsdfoundation.org/project/documentation-and-testing-internship/)，例如构建在线手册编辑器并为某些用户空间工具添加测试用例。
- Christos Margiolis 完成了他的[项目，改进 kinst DTrace 提供者](https://freebsdfoundation.org/project/improving-the-kinst-dtrace-provider/)，通过实现内联函数追踪并将 kinst 移植到 arm64 和 riscv。
- 为了准备 FreeBSD 14.0，Muhammad Moinur（Moin）Rahman 提交了 700 多个修复或对最近的 OpenSSL 和 LLVM 更新受影响的 port 的解决方法。

有关当前和过去基金会合同工作的更多信息，请访问[基金会项目页面](https://freebsdfoundation.org/our-work/projects/)。

以下是本季度完成的其他基金会赞助的工作的样本：

- 改进了 riscv64 CPU 的标识和功能检测
- 从头开始重写了[intro(9)](https://man.freebsd.org/cgi/man.cgi?query=intro&sektion=9&format=html)手册页面
- 在[hwpmc(4)](https://man.freebsd.org/cgi/man.cgi?query=hwpmc&sektion=4&format=html)模块和[pmc(3)](https://man.freebsd.org/cgi/man.cgi?query=pmc&sektion=3&format=html)库和工具中执行了代码维护并修复了错误
- 为 FreeBSD 14.0 做准备，提交了各种有关[freebsd-update(8)](https://man.freebsd.org/cgi/man.cgi?query=freebsd-update&sektion=8&format=html)的修复
- 向 LinuxKPI、iwlwifi 和 net802.11 代码提交了许多（37 个）更新和修复
- 将 SSH 升级到 OpenSSH 9.3p2，然后升级到 9.4p1
- 修补了 ssh-keygen 以在没有参数的情况下生成 Ed25519 密钥
- 添加了 Linux [membarrier(2)](https://man.freebsd.org/cgi/man.cgi?query=membarrier&sektion=2&format=html)系统调用的清洁室实现
- 在 amd64 和 arm64 上将 MAXCPU 增加到 1024
- 为受影响的机器提交了自动 Zenbleed 失效/数据泄漏防护的修复（通过 chicken bit）
- 回顾了内核中整个调度优先级的使用情况，以改进 rtprio() 系统调用的进行中的工作，并在某些情况下使其更有用。

#### 支持 FreeBSD 基础设施

基金会提供硬件和两名员工来帮助支持 FreeBSD 集群。通过你的捐赠，基金会与集群管理团队协调，购买了五个新的软件构建器、三个新的 Web 服务器、一个新的防火墙/路由器、两个软件包镜像和两个用于持续集成的新服务器。除了一个软件包镜像外，所有新硬件都将位于美国东海岸。

#### 持续集成和质量保证

基金会提供一名全职员工和资金，以改进 FreeBSD 项目的持续集成、自动化测试和总体质量保证工作。你可以在专门的报告条目中详细了解有关 CI 工作的信息。

#### 法律/FreeBSD 知识产权

基金会拥有 FreeBSD 商标，并且我们有责任保护这些商标。我们还为核心团队提供法律支持，以调查出现的问题。

请访问[https://freebsdfoundation.org](https://freebsdfoundation.org/)，了解有关我们如何支持 FreeBSD 以及我们如何帮助你的更多信息！

### FreeBSD 发布工程团队

链接：

- [FreeBSD 14.0-RELEASE 发布计划](https://www.freebsd.org/releases/14.0R/schedule/) URL: [https://www.freebsd.org/releases/14.0R/schedule/](https://www.freebsd.org/releases/14.0R/schedule/)
- [FreeBSD 发布版本](https://download.freebsd.org/releases/ISO-IMAGES/) URL: [https://download.freebsd.org/releases/ISO-IMAGES/](https://download.freebsd.org/releases/ISO-IMAGES/)
- [FreeBSD 开发快照](https://download.freebsd.org/snapshots/ISO-IMAGES/) URL: [https://download.freebsd.org/snapshots/ISO-IMAGES/](https://download.freebsd.org/snapshots/ISO-IMAGES/)

联系人：FreeBSD 发布工程团队，<[re@FreeBSD.org](mailto:re@FreeBSD.org)>

FreeBSD 发布工程团队负责制定和发布 FreeBSD 官方项目的发布计划，宣布代码冻结以及维护相应分支等工作。

在今年的第三季度，FreeBSD 发布工程团队开始了即将到来的 14.0-RELEASE 循环的工作。截至本文撰写时，已发布 BETA3，将很快推出 BETA4。

发布工程团队继续为**main**和**stable/13**分支提供每周的开发快照构建。

赞助商：Tarsnap
赞助商：[https://www.gofundme.com/f/gjbbsd/](https://www.gofundme.com/f/gjbbsd/)
赞助商：FreeBSD 基金会

### 持续集成

链接：

- [FreeBSD Jenkins 实例](https://ci.freebsd.org/) URL: [https://ci.FreeBSD.org](https://ci.freebsd.org/)
- [FreeBSD CI Tinderbox 视图](https://tinderbox.freebsd.org/) URL: [https://https://tinderbox.freebsd.org](https://https//tinderbox.freebsd.org)
- [FreeBSD CI 构件存档](https://artifact.ci.freebsd.org/) URL: [https://artifact.ci.FreeBSD.org](https://artifact.ci.freebsd.org/)
- [托管 CI 维基](https://wiki.freebsd.org/HostedCI) URL: [https://wiki.FreeBSD.org/HostedCI](https://wiki.freebsd.org/HostedCI)
- [第三方软件 CI](https://wiki.freebsd.org/3rdPartySoftwareCI) URL: [https://wiki.FreeBSD.org/3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI) -[与 freebsd-testing@相关的问题](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals) URL: [https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)​[*open*](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)​[&amp;email1=testing%40FreeBSD.org&amp;emailassigned_to1=1&amp;emailcc1=1&amp;emailtype1=equals](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)
- [FreeBSD CI 存储库](https://github.com/freebsd/freebsd-ci) URL: [https://github.com/freebsd/freebsd-ci](https://github.com/freebsd/freebsd-ci)
- [dev-ci 邮件列表](https://lists.freebsd.org/subscription/dev-ci) URL: [https://lists.FreeBSD.org/subscription/dev-ci](https://lists.FreeBSD.org/subscription/dev-ci)

联系人：

- Jenkins 管理员 <[jenkins-admin@FreeBSD.org](mailto:jenkins-admin@FreeBSD.org)>
- 許立文 <[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)>
- [freebsd-testing 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-testing)
- IRC #freebsd-ci 频道，位于 EFNet 上

在 2023 年第三季度，我们与项目贡献者和开发人员合作，以满足其测试需求。与此同时，我们与外部项目和公司合作，通过在 FreeBSD 上进行更多测试来增强其产品。

重要已完成的任务：

- 为 stable/14 分支添加作业
- 更新[“Tinderbox”视图](https://tinderbox.freebsd.org/)的 CI 结果，现在包括测试结果和当前失败或不稳定系列的“起点”。
- 这主要由基金会实习生 Yan-Hao Wang 完成。他的其他贡献在本报告的其他条目中有所说明。

进行中的任务：

- 设计和实施预提交 CI 构建和测试以及基于拉取/合并请求的系统（以支持[workflow 工作组](https://gitlab.com/bsdimp/freebsd-workflow)）
- 概念验证系统正在进行中。
- 设计和实施使用 CI 集群构建发行工件，就像发行工程一样
- 简化为贡献者和开发人员设置 CI

测试环境

- 设置 CI 阶段环境并在其中放置实验性作业
- 改进硬件测试实验室并添加更多用于测试的硬件
- 合并[https://reviews.freebsd.org/D38815](https://reviews.freebsd.org/D38815)
- 合并[https://reviews.freebsd.org/D36257](https://reviews.freebsd.org/D36257)

打开或排队的任务：

- 收集和整理[CI 任务和想法](https://hackmd.io/@FreeBSD-CI/freebsd-ci-todo)
- 为运行测试的 VM 客户端设置公共网络访问
- 实施使用裸机硬件运行测试套件
- 添加构建针对-CURRENT 的 drm port 的测试
- 计划运行 ztest 测试
- 在其 CI 管道中帮助更多软件获得 FreeBSD 支持（维基页面：[第三方软件 CI](https://wiki.freebsd.org/3rdPartySoftwareCI)，[托管 CI](https://wiki.freebsd.org/HostedCI)）
- 与托管 CI 提供商合作，以更好地支持 FreeBSD

有关更多进行中的信息，请查看[与 freebsd-testing@相关的票务](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)，请随时加入我们的努力！

赞助商：FreeBSD 基金会

### Ports

链接：

- [关于 FreeBSD Ports](https://www.freebsd.org/ports/) URL:[https://www.FreeBSD.org/ports/](https://www.freebsd.org/ports/)
- [贡献到 Ports](https://docs.freebsd.org/en/articles/contributing/#ports-contributing) URL: [https://docs.freebsd.org/en/articles/contributing/#ports-contributing](https://docs.freebsd.org/en/articles/contributing/#ports-contributing)
- [FreeBSD Ports 监控](http://portsmon.freebsd.org/) URL: [http://portsmon.freebsd.org/](http://portsmon.freebsd.org/)
- [Ports 管理团队](https://www.freebsd.org/portmgr/) URL: [https://www.freebsd.org/portmgr/](https://www.freebsd.org/portmgr/)
- [Ports Tarball](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/) URL: [http://ftp.freebsd.org/pub/FreeBSD/ports/ports/](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/)

联系人：René Ladan <[portmgr-secretary@FreeBSD.org](mailto:portmgr-secretary@FreeBSD.org)>

联系人：FreeBSD Ports 管理团队 <[portmgr@FreeBSD.org](mailto:portmgr@FreeBSD.org)>

Ports 管理团队负责监督 Ports 的整体方向、构建软件包以及人事事务。以下是上一季度发生的情况。

- 根据 INDEX 文件，Ports 目前包含 34,600 个 Port。目前有 3,000 个开放的 port 问题报告（PR），其中有 730 个未分配。上一季度主分支有 130 位贡献者进行了 11,454 次提交，2023Q3 分支有 37 位贡献者进行了 828 次提交。与上一季度相比，这意味着未分配 PR 数量略有减少，主分支提交次数增加了 10%，但季度分支的反向移植较少。Port 的数量也略有增长。

在 Q3 期间，我们欢迎 Joel Bodenmann（jbo@）作为新的 port 贡献者，向 mizhka@授予了 port 提交权限，他已经是 src 贡献者，并在一年的沉寂后将 kn​​u@ 和 uqs@ 的提交权限进行了保留。

在 Q3 期间，Ports 管理团队讨论和处理了以下事项：

- 在子包和闪电演讲中取得了一些进展，由 pizzamig@ 在 EuroBSDCon 上进行了演讲
- 对 Ports 的一些部分进行了全面改进（LIB_DEPENDS、PREFIX、MANPREFIX、MANPATH）

对 FreeBSD 13.1 的支持已从 Ports 中删除，因为它在 8 月 1 日已经达到了寿命终点。

在基础设施方面发生了以下事情：

- 添加了对 ebur128 和 guile 的 USES
- 将 Mono、Perl 和 PostgreSQL 的默认版本分别更新为 5.20、5.34 和 15
- 对 ebur128、guile 和 pycryptography 的默认版本进行了添加，分别为"rust"、2.2 和"rust"
- 发生的主要 port 更新有：

  - 将 pkg 更新到 1.20.7
  - 将 Chromium 更新到 117.0.5938.132
  - 将 Firefox 更新到 118.0.1
  - 将 KDE 更新到 5.27.8
  - 将 Rust 更新到 1.72.0
  - 将 Wine 更新到 8.0.2

在上一季度，pgkmgr@ 进行了 18 次实验性运行，测试了各种 port 升级、port 默认版本更新和 pycryptography 更改。

## 项目

跨足多个类别的项目，涉及了从内核和用户空间到 Ports 或外部项目的各个方面。

### 填补 FreeBSD 桌面体验的空白

链接：

- [外部媒体管理器](https://github.com/outpaddling/qmediamanager) URL: [https://github.com/outpaddling/qmediamanager](https://github.com/outpaddling/qmediamanager)
- [基于 devd 的自动挂载程序](https://github.com/outpaddling/devd-mount) URL: [https://github.com/outpaddling/devd-mount](https://github.com/outpaddling/devd-mount)
- [SUID 挂载工具](https://github.com/outpaddling/npmount) URL: [https://github.com/outpaddling/npmount](https://github.com/outpaddling/npmount)
- [更新弹出通知](https://github.com/outpaddling/freebsd-update-notify) URL: [https://github.com/outpaddling/freebsd-update-notify](https://github.com/outpaddling/freebsd-update-notify)

联系人：Jason Bacon <[jwb@FreeBSD.org](mailto:jwb@FreeBSD.org)>

[sysutils/desktop-installer](https://cgit.freebsd.org/ports/tree/sysutils/desktop-installer/) port 已经存在了十多年，可以快速配置裸露的 FreeBSD 系统，使用任何桌面环境或窗口管理器。然而，FreeBSD 基础和 Ports 缺少一些终端用户在桌面操作系统中期望的常见功能。

桌面安装程序的电池监视脚本已经增强，以在各个充电/放电水平显示弹出通知。

[deskutils/qmediamanager](https://cgit.freebsd.org/ports/tree/deskutils/qmediamanager/)，与[sysutils/devd-mount](https://cgit.freebsd.org/ports/tree/sysutils/devd-mount/)和[sysutils/npmount](https://cgit.freebsd.org/ports/tree/sysutils/npmount/)一起，可以在从 devd 接收到通知时挂载插入的媒体，并显示一个弹出窗口，为用户提供显示文件系统信息、打开文件管理器、重新格式化、将磁盘镜像复制到设备或卸载的选项。它提供了一种便捷且安全的方式来处理外部媒体，如 USB 存储设备。

第四个新 port - [deskutils/freebsd-update-notify](https://cgit.freebsd.org/ports/tree/deskutils/freebsd-update-notify/) - 在新的基本更新可用时或经过可配置的时间限制后显示一个弹出窗口通知。如果用户选择继续进行更新，则使用[auto-update-system(1)](https://man.freebsd.org/cgi/man.cgi?query=auto-update-system&sektion=1&format=html)（[sysutils/auto-admin](https://cgit.freebsd.org/ports/tree/sysutils/auto-admin/)的特性）更新整个系统（软件包、port 和基本系统）。

这些新工具使 FreeBSD 桌面体验更接近于最受欢迎的桌面操作系统的便利性。

这些工具实际上是个原型，稳定可靠，但需要审查。用户对默认行为和配置选项的反馈将不胜感激。

### LLDB Kernel Module Improvement

链接：

- [GSoC Wiki Project](https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement](https://wiki.freebsd.org/SummerOfCode2023Projects/LLDBKernelModuleImprovement)
- [Project Codebase](https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel) URL: [https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel](https://github.com/aokblast/freebsd-src/tree/lldb_dynamicloader_freebsd_kernel)
- [LLVM PullRequest](https://github.com/llvm/llvm-project/pull/67106) URL: [https://github.com/llvm/llvm-project/pull/67106](https://github.com/llvm/llvm-project/pull/67106)

联系人：Sheng-Yi Hong <[aokblast@FreeBSD.org](mailto:aokblast@FreeBSD.org)>

在上一季度报告中说明的 LLDB 内核模块改进项目实现了 FreeBSD 内核在 LLDB 上的 DynamicLoader 插件。

所有工作都已完成，即该插件可以正确加载从内核核心转储中提取的所有内核模块及其调试文件。

该插件已在 x86-64 和 arm64（EC2）上进行了测试，用于可重定位类型内核模块和共享库类型内核模块。这两个平台都表明该插件运行良好。

目前，该插件准备合并到 LLVM 代码库中的[LLVM PullRequest](https://github.com/llvm/llvm-project/pull/67106)中。

赞助方：2023 谷歌编程之夏

## 用户空间

影响基本系统及其中程序的变更。

### OpenSSL 3 在基本系统中的改进

链接：

- [OpenSSL Downloads](https://www.openssl.org/source/) URL: [https://www.openssl.org/source/](https://www.openssl.org/source/)

联系人：Pierre Pronchery <[pierre@freebsdfoundation.org](mailto:pierre@freebsdfoundation.org)>

这是对[将 OpenSSL 3 整合到基本系统](https://www.freebsd.org/status/report-2023-04-2023-06/)的[上一个季度报告](https://www.freebsd.org/status/report-2023-04-2023-06/#_openssl_3_in_base)的后续。

自上一报告以来最明显的更新无疑是 3.0.10 和 3.0.11 版本，修复了低到中等严重性的 CVE 问题（[CVE-2023-2975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2975)、[CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)、[CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)、[CVE-2023-4807](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4807))。

然而，这些并不是唯一的更改，本季度解决了一些与整合相关的特定问题，其中大多数是在使用在基本系统中使用 OpenSSL 3 构建 port 时发现的。

修复包括：

- 使用 libcrypto.so 共享对象正确链接引擎和遗留提供程序，以便符号能正确可见。为此，在构建系统中需要一个[小技巧](https://cgit.freebsd.org/src/commit/Makefile.inc1?id=1a18383a52bc373e316d224cef1298debf6f7e25)。
- 更正 FIPS 提供程序的源文件列表。
- 确保`priority`和`umask`功能可以继承登录进程的属性。这在从具有非默认优先级的进程暂时以其他用户身份登录时很有用，以确保由该用户启动的进程仍具有相同的优先级级别。

### 登录类修复与改进

链接：

- [Start of the reviews stack](https://reviews.freebsd.org/D40339) URL: [https://reviews.freebsd.org/D40339](https://reviews.freebsd.org/D40339)

联系人：Olivier Certner <[olce.freebsd.statusreports@certner.fr](mailto:olce.freebsd.statusreports@certner.fr)>

#### 背景

登录类是一种主要用于在登录时设置各种进程属性和属性的机制，取决于登录的用户以及他所属的登录类。登录类通常指定资源限制、环境变量和进程属性，如调度优先级和 umask。有关更多信息，请参见[login.conf(5)](https://man.freebsd.org/cgi/man.cgi?query=login.conf&sektion=5&format=html)。

#### 变更

`priority`和`umask`功能现在接受`inherit`特殊值，明确要求从登录进程继承属性。例如，在从具有非默认优先级的进程暂时以其他用户身份登录时，可以确保由该用户启动的进程仍具有相同的优先级级别。

用户现在可以在其本地配置文件（ **~/.login_conf** ）中覆盖`priority`功能的全局设置（在 **/etc/login.conf** 中）。但请注意，如果用户无特权，则不能增加其优先级，并且在这种上下文中使用`inherit`毫无意义，因为始终首先应用全局设置。

修复：

- 修复了一个错误，当`priority`功能指定实时优先级时，使用的最终优先级存在偏差（实时类别中的数值最高优先级（31）永远无法设置）。
- 安全性：防止 setuid/setgid 进程应用来自某个用户的 **~/.login_conf** 的指令（由于权限不足而无法应用的该目

录中的指令可能会突然变得可应用于这样的进程）。

我们还更新了相关的手册页面以反映新功能，并改进了[login.conf(5)](https://man.freebsd.org/cgi/man.cgi?query=login.conf&sektion=5&format=html)中`priority`和`umask`功能的说明。

#### 状态

由于[Konstantin Belousov](mailto:kib@FreeBSD.org)和[Warner Losh](mailto:imp@FreeBSD.org)的协助，该系列中的某些补丁已经得到了审查。其他补丁正在等待审查（欢迎志愿者进行审查！），这不太可能费时费力。

我们计划通过在未明确指定`priority`功能的情况下将其重置为 0 的操作，来提高一致性，这在 15 多年的`umask`情况下一直如此。

赞助方：Kumacom SAS（进行开发工作）
赞助方：The FreeBSD Foundation（进行一些审查）

## 内核

有关内核子系统/功能、驱动程序支持、文件系统等的更新。

### 启用使用日志软更新的文件系统的快照

联系人：Marshall Kirk McKusick <[mckusick@FreeBSD.org](mailto:mckusick@FreeBSD.org)>

该项目在使用日志软更新时为 UFS/FFS 文件系统提供了快照功能。该项目的详细信息在[2022 年第四季度报告](https://www.freebsd.org/status/report-2022-10-2022-12/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates)中有说明。

该项目有两个关键阶段：

该项目的第一个阶段是使在使用日志软更新时能够创建快照，并在活动文件系统上使用它们执行后台转储。通过使用 -L 参数请求后台转储，使用 [dump(8)](https://man.freebsd.org/cgi/man.cgi?query=dump&sektion=8&format=html)。该阶段于 2022 年第四季度完成，并在 13.2 版本中提供，详见[2023 年第一季度报告](https://www.freebsd.org/status/report-2023-01-2023-03/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates_in_13_2)。

该项目的第二个阶段是在运行日志软更新的文件系统上使用快照进行后台检查。该阶段于 2023 年第三季度完成，及时包含在 14.0 版本中，并在 13.2-STABLE 版本中提供。

赞助方：The FreeBSD Foundation

### FreeBSD 内核的 SquashFS 驱动程序

链接：

- [Wiki page](https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel) URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel](https://wiki.freebsd.org/SummerOfCode2023Projects/PortSquashFuseToTheFreeBSDKernel)
- [Source code](https://github.com/Mashijams/freebsd-src/tree/gsoc/testing) URL: [https://github.com/Mashijams/freebsd-src/tree/gsoc/testing](https://github.com/Mashijams/freebsd-src/tree/gsoc/testing)

联系人：Raghav Sharma <[raghav@FreeBSD.org](mailto:raghav@FreeBSD.org)>

本季度，我们完成了内核的 SquashFS 驱动程序工作。我们现在可以在 FreeBSD 13.2-RELEASE 或更高版本上挂载 SquashFS 文件，并执行所有基本的只读文件系统操作。

工作代码包括：

- 为目录读取支持实现 vop_lookup() 和 vop_readdir() 钩子。
- 为文件读取支持实现 vop_read() 和 vop_strategy() 钩子。
- 为符号链接读取支持实现 vop_readlink() 钩子。

我们还为 SquashFS 实现了扩展属性接口函数。现在只剩下实现它们的内核接口钩子。

此外，还进行了许多错误修复。一个主要问题是找出为什么我们无法列出根目录的第一个条目，原来 SquashFS 可能具有`inode_number`为零，而内核由于某种原因在列出 dirents 时跳过了零。目前，我们通过传递虚构的`inode_number`（而不是零）给 dirent 来解决了这个问题。

代码审查目前正在进行中，由我的导师 [Chuck Tuffli](mailto:chuck@FreeBSD.org) 负责。

我很高兴地说，SquashFS 将在即将发布的 FreeBSD 版本中找到其位置。

赞助方：2023 谷歌编程之夏

### 进程可见性安全策略

链接：

[开始审查栈](https://reviews.freebsd.org/D40626) URL: [https://reviews.freebsd.org/D40626](https://reviews.freebsd.org/D40626)

联系人：Olivier Certner <[olce.freebsd.statusreports@certner.fr](mailto:olce.freebsd.statusreports@certner.fr)>

#### 背景

FreeBSD 实现了三种内置的安全策略，限制了特定用户可以看到哪些进程，旨在防止信息泄漏和不必要的交互。

第一种可以防止非特权用户看到或与其实际 UID 不同的进程进行交互。可以通过将 sysctl `security.bsd.see_other_uids` 设置为 0（默认值为 1）来激活。

第二种可以防止非特权用户看到或与其凭据中没有用户是其成员的进程进行交互。可以通过将 sysctl `security.bsd.see_other_gids` 设置为 0（默认值为 1）来激活。

第三种可以防止非特权用户的进程看到或与处于严格子 Jail 中的进程进行交互。Jail 子系统已经阻止这样的进程看到不是其后代的 Jail 中的进程（参见 [jail(8)](https://man.freebsd.org/cgi/man.cgi?query=jail&sektion=8&format=html)，特别是“分层 Jail”一节）。此策略的一个可能的用途是与上面的第一种策略结合使用，以隐藏在具有与祖先 Jail 中的某个用户相同的实际 UID 的子 Jail 中的进程，因为在这些不同的 Jail 中具有相同 UID 的用户在逻辑上被视为不同的用户。可以通过将 sysctl `security.bsd.see_jail_proc` 设置为 0（默认值为 1）来激活。

在审查这些策略的代码并进行实际测试之后，我们注意到了一些问题和限制，这促使我们对此进行了工作。

#### 更改

由 `security.bsd.see_jail_proc` sysctl 控制的策略已经接收了以下修复和改进：

- 强化 `security.bsd.see_jail_proc` 策略，防止未经授权的用户试图在随机情况下杀死、更改优先级或调试具有相同（真实）UID 的子 Jail 中的进程，即使这些进程对它们不可见，只要猜测的进程 PID 正确，就会成功。
- 使该策略可以被 MAC 策略覆盖，就像其他策略一样。

由 `security.bsd.see_other_gids` 控制的策略已经修复，以考虑进程的真实组而不是其有效组，以确定试图访问进程的用户是否是进程所属组的成员。其原因是一些用户应该继续看到它们启动的进程，即使它们通过 setgid 位获得进一步的权限。反之，他们不应该看到由特权用户启动的临时进入用户的主组的进程。这种新行为与 `security.bsd.see_other_uids` 对用户 ID 始终执行的行为一致（即考虑某个进程的真实用户 ID 而不是有效 ID）。

我们已更新与这些安全策略相关的手册页，包括 [security(7)](https://man.freebsd.org/cgi/man.cgi?query=security&sektion=7&format=html)、[sysctl(8)](https://man.freebsd.org/cgi/man.cgi?query=sysctl&sektion=8&format=html) 和 [ptrace(2)](https://man.freebsd.org/cgi/man.cgi?query=ptrace&sektion=2&format=html)。还翻新了一些实施或利用这些策略的内部函数的手册页。

#### 状态

在 [Mitchell Horne](mailto:mhorne@FreeBSD.org)、[Pau Amma](mailto:pauamma@gundo.com)、[Benedict Reuschling](mailto:bcr@FreeBSD.org) 和 [Ed Maste](mailto:emaste@FreeBSD.org) 的帮助下，大多数提交的更改已经被审查并获得批准，因此它们应该很快就会到达代码树。补丁系列始于 [审查 D40626](https://reviews.freebsd.org/D40626)。从那里，点击“Stack”选项卡以查看实施更改的所有审查列表。

作为后续步骤，我们正在考虑默认启用 `security.bsd.see_jail_proc` 策略（即 sysctl 的默认值将变为 0），除非有异议。

赞助方：Kumacom SAS（开发工作）
赞助方：The FreeBSD Foundation（大部分审查）

### Linux 兼容性层更新

链接：

[Linuxulator 状态维基页面](https://wiki.freebsd.org/Linuxulator) URL: [https://wiki.freebsd.org/Linuxulator](https://wiki.freebsd.org/Linuxulator)

[Linux 应用程序状态维基页面](https://wiki.freebsd.org/LinuxApps) URL: [https://wiki.freebsd.org/LinuxApps](https://wiki.freebsd.org/LinuxApps)

联系人：Dmitry Chagin <[dchagin@FreeBSD.org](mailto:dchagin@FreeBSD.org)>

该项目的目标是提高 FreeBSD 执行未经修改的 [linux(4)](https://man.freebsd.org/cgi/man.cgi?query=linux&sektion=4&format=html) 二进制文件的能力。

截至 [22dca7acf775](https://cgit.freebsd.org/src/commit/?id=22dca7acf775)，已经实现了 xattr 系统调用。这使得可以使用 Linux rsync。

截至 [bbe017e0415a](https://cgit.freebsd.org/src/commit/?id=bbe017e0415a)，已经实现了 ioprio 系统调用。这使得可以使用 debootstrap 安装 Ubuntu 23.04。

## 架构

更新特定于平台的功能并为新的硬件平台提供支持。

### NXP DPAA2 支持

链接：
[FreeBSD 源代码中的 DPAA2](https://cgit.freebsd.org/src/tree/sys/dev/dpaa2) URL: [https://cgit.freebsd.org/src/tree/sys/dev/dpaa2](https://cgit.freebsd.org/src/tree/sys/dev/dpaa2)

[GitHub 上的 DPAA2](https://github.com/mcusim/freebsd-src) URL: [https://github.com/mcusim/freebsd-src](https://github.com/mcusim/freebsd-src)

联系人：Dmitry Salychev <[dsl@FreeBSD.org](mailto:dsl@FreeBSD.org)>

联系人：Bjoern A. Zeeb <[bz@FreeBSD.org](mailto:bz@FreeBSD.org)>

#### 什么是 DPAA2？

DPAA2 是一种硬件级网络架构，存在于一些 NXP SoC 中，其中包含硬件块，包括管理复杂（MC，用于操纵 DPAA2 对象的命令接口）、线速 I/O 处理器（WRIOP，分发数据包、排队、丢弃决策）、队列和缓冲区管理器（QBMan，Rx/Tx 队列控制、Rx 缓冲区池）等。管理复杂运行 NXP 提供的固件，该固件提供 DPAA2 对象作为对这些块的底层硬件进行简化访问的抽象层，以简化对底层硬件的访问。

#### 与上一报告相比的变化

- 改进了 DPAA2 通道之间的隔离性。
- 修复了在大量网络负载下的恐慌。
- FDT/ACPI MDIO 支持。
- NFS 根挂载不再在通过 DPAA2 进行的 netboot 上挂起。
- 已开始与 MC 通过它们自己的命令门户（DPMCP）通信的驱动程序。
- [所有已关闭问题的列表](https://github.com/mcusim/freebsd-src/issues?q=is%3Aissue+is%3Aclosed)。

#### 进展中的工作

已经开始在 [dev/sff](https://cgit.freebsd.org/src/commit/?id=2a9021898c4ee2154787da862c238cfeccd655df) 上进行工作，以支持 SFF/SFP 模块，以便在超过 1 Gbit/s 的链路上测试 DPAA2 驱动程序。

#### 计划

- 进行大量网络负载测试（2.5 Gbit/s、10 Gbit/s）和消除瓶颈。
- 支持基于缓存的内存软件门户。
- 驱动程序资源的释放以正确卸载 dpaa2.ko。
- 进一步支持硬件支持的其他部分（DPSW、DCE 等）。

赞助方：Traverse Technologies（提供 Ten64 硬件进行测试）

### amd64 SIMD 增强

链接：
[项目提案](http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt) URL: [http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt](http://fuz.su/~fuz/freebsd/2023-04-05_libc-proposal.txt)
[simd(7)](https://man.freebsd.org/cgi/man.cgi?query=simd&sektion=7&manpath=FreeBSD+15.0-CURRENT) URL: [https://man.freebsd.org/cgi/man.cgi?query=simd&amp;sektion=7&amp;manpath=FreeBSD+15.0-CURRENT](https://man.freebsd.org/cgi/man.cgi?query=simd&sektion=7&manpath=FreeBSD+15.0-CURRENT)

联系人：Robert Clausecker <[fuz@FreeBSD.org](mailto:fuz@FreeBSD.org)>

SIMD 指令集扩展，如 SSE、AVX 和 NEON，在现代计算机上普遍存在，并为许多应用程序提供性能优势。该项目的目标是提供常见 libc 函数的 SIMD 增强版本（主要是 [string(3)](https://man.freebsd.org/cgi/man.cgi?query=string&sektion=3&format=html) 中说明的函数），加速大多数 C 程序的执行。

对于每个经过优化的函数，将提供最多四个实现：

- 一个仅对 amd64 进行了优化但没有使用任何 SIMD 的 **标量** 实现，
- 一个使用 SSE 和 SSE2 的 **基准** 实现，或者使用所有 SSE 扩展直到 SSE4.2 的 **x86-64-v2** 实现，
- 一个使用 AVX 和 AVX2 的 **x86-64-v3** 实现，以及
- 一个使用 AVX-512F/BW/CD/DQ 的 **x86-64-v4** 实现。

用户将能够通过设置 `ARCHLEVEL` 环境变量来选择使用哪个级别的 SIMD 增强。

尽管当前的项目仅涉及 amd64，但今后可能会将其扩展到其他架构，如 arm64。

在过去的几个月里，这个项目取得了显著的进展。对 [bcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=bcmp&sektion=3&format=html)、[index(3)](https://man.freebsd.org/cgi/man.cgi?query=index&sektion=3&format=html)、[memchr(3)](https://man.freebsd.org/cgi/man.cgi?query=memchr&sektion=3&format=html)、[memcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=memcmp&sektion=3&format=html)、[stpcpy(3)](https://man.freebsd.org/cgi/man.cgi?query=stpcpy&sektion=3&format=html)、[strchr(3)](https://man.freebsd.org/cgi/man.cgi?query=strchr&sektion=3&format=html)、[strchrnul(3)](https://man.freebsd.org/cgi/man.cgi?query=strchrnul&sektion=3&format=html)、[strcpy(3)](https://man.freebsd.org/cgi/man.cgi?query=strcpy&sektion=3&format=html)、[strcspn(3)](https://man.freebsd.org/cgi/man.cgi?query=strcspn&sektion=3&format=html)、[strlen(3)](https://man.freebsd.org/cgi/man.cgi?query=strlen&sektion=3&format=html)、[strnlen(3)](https://man.freebsd.org/cgi/man.cgi?query=strnlen&sektion=3&format=html) 和 [strspn(3)](https://man.freebsd.org/cgi/man.cgi?query=strspn&sektion=3&format=html) 进行了 SIMD 增强的版本已经完成。[memcpy(3)](https://man.freebsd.org/cgi/man.cgi?query=memcpy&sektion=3&format=html)、[memmove(3)](https://man.freebsd.org/cgi/man.cgi?query=memmove&sektion=3&format=html)、[strcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=strcmp&sektion=3&format=html)、[timingsafe_bcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=timingsafe_bcmp&sektion=3&format=html)（参见 [D41673](https://reviews.freebsd.org/D41673)）和 [timingsafe_memcmp(3)](https://man.freebsd.org/cgi/man.cgi?query=timingsafe_memcmp&sektion=3&format=html)（参见 [D41696](https://reviews.freebsd.org/D41696)）的函数正在进行中。不幸的是，这项工作没有包含在 FreeBSD 14.0 中，但计划包含在 FreeBSD 14.1 中。

赞助方：The FreeBSD Foundation

### 将 mfsBSD 集成到发布构建工具中

链接：

[维基文章](https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools)

URL: [https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools](https://wiki.freebsd.org/SummerOfCode2023Projects/IntegrateMfsBSDIntoTheReleaseBuildingTools)

[Phabricator 上的代码审查](https://reviews.freebsd.org/D41705)

URL: [https://reviews.freebsd.org/D41705](https://reviews.freebsd.org/D41705)

[FreeBSD Foundation 博客文章](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-soobin-rho/)

URL: [https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-soobin-rho/](https://freebsdfoundation.org/blog/meet-the-2023-freebsd-google-summer-of-code-students-soobin-rho/)

联系人：Soobin Rho <[soobinrho@FreeBSD.org](mailto:soobinrho@FreeBSD.org)>

#### 什么是 mfsBSD？

"mfsBSD 是一个工具集，用于创建基于 FreeBSD 的小型但功能齐全的 mfsroot 发行版，将所有文件存储在内存中（MFS）[Memory File System] 并从硬盘驱动器、USB 存储设备或光学介质加载。它可用于各种用途，包括无磁盘系统、恢复分区以及远程覆盖其他操作系统。"

[Martin Matuška](mailto:mm@FreeBSD.org) 是 mfsBSD 的创作者。他还是原始（2009 年）[mfsBSD 白皮书](https://people.freebsd.org/~mm/mfsbsd/mfsbsd.pdf)的作者，以上摘录自该白皮书。上游的 mfsBSD 在 [GitHub 上的仓库](https://github.com/mmatuska/mfsbsd) 中维护。

#### 项目目的

该项目将 mfsBSD 集成到 FreeBSD 发布工具集中，通过在 **/usr/src/release/Makefile** 中创建 mfsBSD 镜像（ **.img** 和 **.iso** 文件）的附加目标。在集成之前，mfsBSD 仅存在于 FreeBSD 发布工具链之外，并且仅会生成 -RELEASE 版本。

有了这个项目，mfsBSD 镜像将会出现在官方 FreeBSD 发布页面。你还可以通过调用 `cd /usr/src/release && make release WITH_MFSBSD=1` 来构建 mfsBSD，然后会在 **/usr/obj/usr/src/${ARCH}/release/** 中创建 **mfsbsd-se.img** 和 **mfsbsd-se.iso**。

#### 与上一季度的变化

代码已经准备就绪，目前正在进行审查。如果你想参与审查流程，请随时加入！这是 [我的修订](https://reviews.freebsd.org/D41705)。

赞助方：Google, Inc. (GSoC 2023)

## 云

更新云特定功能并为新的云平台提供支持。

### FreeBSD 上的 OpenStack

链接：
[OpenStack](https://www.openstack.org/) URL: [https://www.openstack.org/](https://www.openstack.org/)

[FreeBSD 上的 OpenStack](https://github.com/openstack-on-freebsd) URL: [https://github.com/openstack-on-freebsd](https://github.com/openstack-on-freebsd)

联系人：Chih-Hsin Chang <[starbops@hey.com](mailto:starbops@hey.com)>

联系人：許立文 <[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)>

OpenStack 是一款开源的云操作系统，对于在云平台上部署各种资源类型非常有价值。然而，将 OpenStack 的控制平面运行在 FreeBSD 主机上一直是一个挑战。我们项目的任务是使 FreeBSD 能够无缝地作为 OpenStack 主机运行。

在本季度，我们专注于整个概念验证（POC）的最后一部分，即 VM 控制台集成。目标是让用户通过 OpenStack 客户端获取串行控制台，以访问运行在基于 FreeBSD 的 OpenStack 集群上的 VM 实例。这也很重要，因为现在我们在 Neutron 中没有托管 DHCP 服务的 Port。用户需要手动配置正确的 IP 地址，以使 VM 实例具有网络连接。然而，[bhyve(8)](https://man.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8&format=html) 并不会本地公开串行控制台，因此我们需要通过网络导出 [nmdm(4)](https://man.freebsd.org/cgi/man.cgi?query=nmdm&sektion=4&format=html) 设备。这是通过一个名为 [`socat-manager`](https://github.com/openstack-on-freebsd/socat-manager/blob/main/server.py) 的自定义代理完成的，是的，我们利用 [socat(1)](https://man.freebsd.org/cgi/man.cgi?query=socat&sektion=1&format=html) 在由 OpenStack `nova-compute` 分配的特定 port 上监听，以集成到其工作流程中。借助另一个关键部分，即 [bhyve 的自定义 Libvirt 钩子](https://github.com/openstack-on-freebsd/socat-manager/tree/main/hooks)，我们可以连接两个端点并使控制台对用户可访问。在开发钩子脚本时，我们发现 Libvirt 专门为 bhyve 提供的钩子接口 [没有很好地实现](https://gitlab.com/libvirt/libvirt/-/issues/528)。幸运的是，Libvirt 开发人员 [及时解决了问题](https://gitlab.com/libvirt/libvirt/-/commit/ad8c4d9d6d09d51a9530ed84fcd2220713aab928)，我们计划在将来发布修复时完善我们的钩子脚本。

我们还解决了在 [上一季度报告](https://www.freebsd.org/status/report-2023-04-2023-06/#_openstack_on_freebsd) 中提到的我们的开发环境中的嵌套 bhyve 问题（在 Linux KVM 之上运行 bhyve VM）。这是由两个 VT-x 功能的 APIC 模拟引起的：`VID` 和 `PostIntr`。

我们主机的 CPU 具有这两个功能，因此我们需要在 L1 guest 中禁用它们，L1 guest 充当 bhyve 主机，在 **/boot/loader.conf** 中，以使 L2 guest 不挂起。对于我们能够在一个完全虚拟化的环境中进行项目工作至关重要，因为缺乏物理资源。这对于对项目感兴趣的人同样重要，降低了尝试在其环境中进行整个 POC 的门槛，而不需要太高的设置要求。

展望第四季度，我们的重点是用修订后的文档完成 POC 并移植到 FreeBSD 14.0-RELEASE。缺少相应 FreeBSD 软件包的依赖项将逐个移植。我们还计划将我们的工作与 OpenStack [2023.1 Antelope](https://releases.openstack.org/antelope/index.html) 进行合并。我们邀请对我们的文档感兴趣的人探索并为该项目的成功做出贡献。

赞助商：The FreeBSD Foundation

### FreeBSD 在 Microsoft HyperV 和 Azure 上

链接：
[FreeBSD 维基上的 Microsoft Azure 文章](https://wiki.freebsd.org/MicrosoftAzure) URL: [https://wiki.freebsd.org/MicrosoftAzure](https://wiki.freebsd.org/MicrosoftAzure)

[FreeBSD 维基上的 Microsoft HyperV 文章](https://wiki.freebsd.org/HyperV) URL: [https://wiki.freebsd.org/HyperV](https://wiki.freebsd.org/HyperV)

联系人：Microsoft FreeBSD Integration Services Team <[bsdic@microsoft.com](mailto:bsdic@microsoft.com)>

联系人：[freebsd-cloud 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-cloud)

联系人：The FreeBSD Azure Release Engineering Team <[releng-azure@FreeBSD.org](mailto:releng-azure@FreeBSD.org)>

联系人：Wei Hu <[whu@FreeBSD.org](mailto:whu@FreeBSD.org)>

联系人：Souradeep Chakrabarti <[schakrabarti@microsoft.com](mailto:schakrabarti@microsoft.com)>

联系人：許立文 <[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)>

在本季度，我们主要致力于 ARM64 架构支持，构建并发布基于 UFS 和 ZFS 的镜像到 [Azure 社区库](https://learn.microsoft.com/azure/virtual-machines/share-gallery-community)。在项目的测试公共库中，名为 `FreeBSDCGTest-d8

a43fa5-745a-4910-9f71-0c9da2ac22bf`，有一些测试镜像可用：

- FreeBSD-CURRENT-testing
- FreeBSD-CURRENT-gen2-testing
- FreeBSD-CURRENT-arm64-testing
- FreeBSD-CURRENT-zfs-testing
- FreeBSD-CURRENT-zfs-gen1-testing

要使用它们，创建虚拟机时：

1. 在 `Select an Image` 步骤中，在 `Other items` 中选择 `Community Images`
2. 搜索 `FreeBSD`

我们的目标是为 14.0-RELEASE 提供以上所有这些镜像。

正在进行的任务：

- 自动化镜像构建和发布过程，并合并到 src/release/ 中。
- 将所有支持的 VM 镜像构建和发布到 Azure Marketplace
- 将快照构建发布到 Azure 社区库

上述任务由 The FreeBSD Foundation 赞助，由 Microsoft 提供资源。

Wei Hu 和 Souradeep Chakrabarti 在 arm64 中解决了几个关键 bug：

- [https://bugs.freebsd.org/267654](https://bugs.freebsd.org/267654)
- [https://bugs.freebsd.org/272461](https://bugs.freebsd.org/272461)
- [https://bugs.freebsd.org/272666](https://bugs.freebsd.org/272666)

根本原因在 [e7a9817b8d32: Hyper-V: vmbus: implementat bus_get_dma_tag in vmbus](https://cgit.freebsd.org/src/commit/?id=e7a9817b8d328dda04069b65944ce2ed6f54c6f0) 中得以识别和解决。

并继续改进 Microsoft Azure Network Adapter (MANA) 支持。

待处理任务：

- 在 [Microsoft Learn](https://learn.microsoft.com/) 上更新 FreeBSD 相关文档
- 在 [Azure Pipelines](https://azure.microsoft.com/products/devops/pipelines/) 中支持 FreeBSD
- 将 [Azure 代理 port](https://www.freshports.org/sysutils/azure-agent) 更新到最新版本
- 将 [Azure 代理的本地修改](https://github.com/Azure/WALinuxAgent/pull/1892) 上游

赞助方：对于 Microsoft 的人员和为其他方提供资源的一切，由 The FreeBSD Foundation 赞助。

### FreeBSD 在 EC2 上

链接：

[FreeBSD/EC2 Patreon](https://www.patreon.com/cperciva) URL: [https://www.patreon.com/cperciva](https://www.patreon.com/cperciva)

联系人：Colin Percival <[cperciva@FreeBSD.org](mailto:cperciva@FreeBSD.org)>

FreeBSD 可以在 x86（Intel 和 AMD）和 ARM64（Graviton）EC2 实例上使用。工作正在进行，以确保即将推出的实例类型得到支持。

现在，每周 FreeBSD 快照都包括用于 14.0 和 15.0 的实验性 ZFS-root AMI。这个变化将出现在 FreeBSD 14.0-RELEASE 中。

正在进行的工作包括开始发布实验性的 "cloud-init" AMI。预计这将在 FreeBSD 14.0-RELEASE 推出时实现。

这项工作得到了 Colin 的 FreeBSD/EC2 Patreon 的支持。

## 文档

文档、手册页或新的外部书籍/文件中的重要更改。

### 文档工程团队

链接：[FreeBSD 文档项目](https://www.freebsd.org/docproj/) URL: [https://www.freebsd.org/docproj/](https://www.freebsd.org/docproj/)

链接：[FreeBSD 文档项目新贡献者入门指南](https://docs.freebsd.org/en/books/fdp-primer/) URL: [https://docs.freebsd.org/en/books/fdp-primer/](https://docs.freebsd.org/en/books/fdp-primer/)

链接：[文档工程团队](https://www.freebsd.org/administration/#t-doceng) URL: [https://www.freebsd.org/administration/#t-doceng](https://www.freebsd.org/administration/#t-doceng)

联系人：FreeBSD Doceng Team <[doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)>

doceng@ 团队是处理与 FreeBSD 文档项目相关的一些元项目问题的团体；有关更多信息，请参阅 [FreeBSD Doceng Team Charter](https://www.freebsd.org/internal/doceng/)。

在本季度：

- 文档门户的搜索功能已从 DuckDuckGo 移至我们自己的搜索引擎；有关更多信息，请参阅 [此提交](https://cgit.freebsd.org/doc/commit/?id=ac4fd34edfa1e5e2edb6fb9fc61acd782a0ed33b)。
- 根据 grahamperrin@ 的请求，他的文档提交权限已被保留。
- 根据 pluknet@ 的请求，他的文档提交权限已被保留。

#### Porter’s Handbook

Handbook 中已添加了新的 `USES` 标记：

- [`USES\= ebur128`](https://cgit.freebsd.org/doc/commit/?id=ee08121ef177489c031870601de1cc728de646e5)。
- [`USES\= guile`](https://cgit.freebsd.org/doc/commit/?id=4f16184d81f1c02196d91e8d2511f23fd48e8822)。

#### FreeBSD 在 Weblate 上的翻译

链接：[在 Weblate 上翻译 FreeBSD](https://wiki.freebsd.org/Doc/Translation/Weblate) URL: [https://wiki.freebsd.org/Doc/Translation/Weblate](https://wiki.freebsd.org/Doc/Translation/Weblate)

链接：[FreeBSD Weblate 实例](https://translate-dev.freebsd.org/) URL: [https://translate-dev.freebsd.org/](https://translate-dev.freebsd.org/)

##### 2023 年第三季度状态

- 17 种团队语言
- 189 注册用户

四名新的翻译者加入了 Weblate：

- minso 在韩语（ko）和法语（fr_FR）方面。
- strgalt-t 在德语（de_DE）方面。
- bsdmeg 在德语（de_DE）方面。
- mvsf 在葡萄牙语（pt_BR）方面。

##### 语言

- 中文（简体）（zh-cn）（进度：7%）
- 中文（繁体）（zh-tw）（进度：3%）
- 荷兰语（nl）（进度：1%）
- 法语（fr）（进度：1%）
- 德语（de）（进度：1%）
- 印尼语（id）（进度：1%）
- 意大利语（it）（进度：5%）
- 韩语（ko）（进度：33%）
- 挪威语（nb-no）（进度：1%）
- 波斯语（fa-ir）（进度：2%）
- 波兰语（进度：1%）
- 葡萄牙语（进度：0%）
- 葡萄牙语（pt-br）（进度：22%）
- 西班牙语（es）（进度：35%）
- 土耳其语（tr）（进度：2%）

我们要感谢所有贡献者，翻译或审核文档。

并请在你的本地用户组中宣传此努力，我们始终需要更多的志愿者。

#### FreeBSD 手册工作组

联系人：Sergio Carlavilla <[carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)>

- [网络章节已经重写](https://reviews.freebsd.org/D40546)
- [Jails 章节已经重写](https://cgit.freebsd.org/doc/commit/?id=612b7cc1721224c494c5b2600188e1508bb5611b)
- 下一个要处理的部分将是文件系统部分：UFS、OpenZFS、其他文件系统。

#### 工作组 FAQ

联系人：Sergio Carlavilla <[carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)>

这个工作组的想法是撰写一个新的 FAQ。将与 FreeBSD 14.0 一同发布。

#### FreeBSD 网站改版——WebApps 工作组

联系人：Sergio Carlavilla <[carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)>

负责创建新的 FreeBSD 文档门户并重新设计 FreeBSD 主网站及其组件的工作组。FreeBSD 开发者可以在 FreeBSD Slack 频道 #wg-www21 上关注并加入这个工作组。工作将分为三个阶段：

1. 重新设计 Web 上的手册页
   使用 mandoc 生成 HTML 页面的脚本。 (*已完成，已由 Doceng 批准，部署日期尚未确定*) [https://man-dev.FreeBSD.org](https://man-dev.freebsd.org/) 上的公共实例。
2. 重新设计 FreeBSD 主网站
   新设计，响应式和深色主题。 (*几乎完成，在 EuroBSDCon 上进行了演示*)
3. 重新设计 Web 上的 Ports 页面
   用于创建应用程序门户的 Ports 脚本。 (*进行中*)

### FreeBSD 在线编辑器和 Man 手册编辑器

链接：

[FreeBSD 在线文档编辑器](https://github.com/Wang-Yan-Hao/FreeBSD-Online-Document-Editor) URL: [https://github.com/Wang-Yan-Hao/FreeBSD-Online-Document-Editor](https://github.com/Wang-Yan-Hao/FreeBSD-Online-Document-Editor)

[FreeBSD 在线 Man 手册编辑器](https://github.com/Wang-Yan-Hao/man_page_editor) URL: [https://github.com/Wang-Yan-Hao/man_page_editor](https://github.com/Wang-Yan-Hao/man_page_editor)

联系人：Yan-Hao Wang <[bses30074@gmail.com](mailto:bses30074@gmail.com)>

联系人：許立文 <[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)>

目前，我们的文档翻译过程涉及使用 Weblate 和直接编辑 [doc](https://cgit.freebsd.org/doc/) 存储库。我们意识到这个过程可能有些繁琐，因此我们正在努力提供一个更方便的替代方案，类似于维基社区的做法。介绍在线文档编辑器和 Man 手册编辑器，这是一个用户友好的所见即所得（WYSIWYG）静态站点，用于翻译文档和 man 手册。我们的目标是在一个平台上 consolide 所有翻译功能，使翻译过程尽可能简单。

然而，我们仍然需要这两个项目的帮助，具体如下：

1. 文档编辑器和 Man 手册编辑器是使用简单的 JavaScript 开发的。我们正在寻找一位 Web 开发人员来评估代码的效率，因为我（Yan-Hao Wang）在前端开发方面并不精通。
2. 我们还在寻找一位网络安全开发人员，协助我们识别和解决这两个项目中的安全问题。这对于确保这些项目的安全托管并减轻潜在漏洞至关重要。
3. 由于目前没有现有的 JavaScript 库可以渲染 mandoc，我不得不创建自己的库。然而，在编辑过程中仍然存在一些隐藏的错误。我们需要一位 JavaScript 开发人员来帮助纠正这些渲染问题。

赞助：FreeBSD 基金会

### FreeBSD 专家系统

链接：
[FreeBSD 专家系统](https://github.com/Wang-Yan-Hao/freebsd_expert_system) URL: [https://github.com/Wang-Yan-Hao/freebsd_expert_system](https://github.com/Wang-Yan-Hao/freebsd_expert_system)

联系人：Yan-Hao Wang <[bses30074@gmail.com](mailto:bses30074@gmail.com)>联系人：許立文 <[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)>

在今天的世界中，机器学习和深度学习技术变得越来越普遍，就像 ChatGPT 的普及一样。我们正在开发一个 ChatGPT 插件，可以访问最新的 FreeBSD 数据，将 ChatGPT 转变为 FreeBSD 专家系统。我们已经编写了数据清理的脚本并构建了一个嵌入式模型来搜索相关信息。

然而，我们需要在这个项目的以下方面得到帮助：

- 虽然我不是机器学习或深度学习方面的专家，但我们在这些领域遇到了许多挑战，例如数据清理的充分性以及最终插件开发过程中的不确定性。我们将感激在这方面的指导。

赞助：FreeBSD 基金会

## Ports

影响 Ports 的变化，无论是触及大部分树的全面变化还是单独的 port 本身。

### FreeBSD 上的 KDE

链接：

[KDE/FreeBSD 主动性](https://freebsd.kde.org/) URL: [https://freebsd.kde.org/](https://freebsd.kde.org/)

[FreeBSD —— KDE 社区维基](https://community.kde.org/FreeBSD) URL: [https://community.kde.org/FreeBSD](https://community.kde.org/FreeBSD)

联系人：Adriaan de Groot <[kde@FreeBSD.org](mailto:kde@FreeBSD.org)>

KDE on FreeBSD 项目为 FreeBSD Ports 打包了 CMake、Qt 和来自 KDE Community 的软件。该软件包括一个名为 KDE Plasma（适用于 X11 和 Wayland）的完整桌面环境，以及可以在任何 FreeBSD 计算机上使用的数百个应用程序。

KDE 团队（kde@）是 desktop@ 和 x11@ 的一部分，构建软件堆栈，使 FreeBSD 成为一台美观且可用作日常驱动图形桌面工作站的计算机。下面的说明主要说明了与 KDE 相关的 Port，但也包括对整个桌面堆栈重要的项目。

#### 基础设施

Qt5 现在进入了长期支持阶段，仅在极少数情况下进行更新。在本季度进行了到 5.15.10 的更新。Qt6 现在已经使用正常的上游发布进行了更新，7 月底发布了 6.5.2 版本，之后又发布了 6.5.3 版本。

本季度 CMake 没有更新，因此我们现在至少滞后了一个次要版本。最新版本的变更日志对 FreeBSD 的影响不大，因此没有升级的特殊原因。

[sysutils/polkit](https://cgit.freebsd.org/ports/tree/sysutils/polkit/) 和 [sysutils/consolekit2](https://cgit.freebsd.org/ports/tree/sysutils/consolekit2/) 都已更新，为 FreeBSD 桌面提供了改进的安全策略和控制台处理。[x11/sddm](https://cgit.freebsd.org/ports/tree/x11/sddm/) 已更新，提供更好的图形化登录管理器。

[multimedia/pipewire](https://cgit.freebsd.org/ports/tree/multimedia/pipewire/) 已更新到 0.3.81 版本。这为 KDE 和 GNOME 等桌面提供了多媒体支持。

#### KDE Stack

KDE Gear 每季度发布一次，KDE Plasma 每月更新一次，KDE Frameworks 每月也有新版本发布。这些（大型）更新在它们的上游发布后不久就会到来，不会单独列出。

- KDE Frameworks 已达到 5.110 版。KDE Frameworks 5 系列正在逐渐结束，尽管在上游进入长期支持之前还需要大约六个月。
- KDE Plasma Desktop 已更新到 5.27.8 版。与框架一样，上游工作正在减少，以支持 KDE Plasma 6。
- KDE Gear 已更新到 23.08.1 版。

#### 相关的 Ports

KDE 生态系统包括各种 port —— 大多数由 kde@ 维护，所有这些 port 都建立在共享的 Qt 和 KDE Frameworks 基础上。kde@ 团队根据需要更新它们。例如，本季度 tcberner@ 和 arrowd@ 更新或修复了（远不止于此的）以下一系列 port：

- [astro/merkaartor](https://cgit.freebsd.org/ports/tree/astro/merkaartor/)
- [devel/massif-visualizer](https://cgit.freebsd.org/ports/tree/devel/massif-visualizer/)
- [finance/alkimia](https://cgit.freebsd.org/ports/tree/finance/alkimia/)
- [irc/quassel](https://cgit.freebsd.org/ports/tree/irc/quassel/)
- [net-im/kaidan](https://cgit.freebsd.org/ports/tree/net-im/kaidan/)
- [sysutils/bsdisks](https://cgit.freebsd.org/ports/tree/sysutils/bsdisks/)
- [sysutils/k3b](https://cgit.freebsd.org/ports/tree/sysutils/k3b/)

感谢 jhale@，[devel/qtcreator](https://cgit.freebsd.org/ports/tree/devel/qtcreator/) 已更新到 11.0.3 版，为创建 Qt 和 KDE 应用程序的功能丰富的集成开发环境提供了另一个选择。

#### 弃用

Web 浏览器庞大，并且具有相当大的安全性。备受尊敬的 [www/qt5-webkit](https://cgit.freebsd.org/ports/tree/www/qt5-webkit/) WebKit port 已计划删除，并且已将其用户移至 WebEngine。我们依赖的 WebKit 分支已不再得到积极维护。

### FreeBSD 上的 Pantheon 桌面

链接：

[elementary OS](https://elementary.io/) URL: [https://elementary.io/](https://elementary.io/)

[开发仓库](https://codeberg.org/olivierd/freebsd-ports-elementary) URL: [https://codeberg.org/olivierd/freebsd-ports-elementary](https://codeberg.org/olivierd/freebsd-ports-elementary)

联系人：Olivier Duchateau <[duchateau.olivier@gmail.com](mailto:duchateau.olivier@gmail.com)>

Pantheon 桌面环境是为 elementary OS 设计的。它基于 GNOME 技术（如 Mutter、GTK 3 和 4），使用 Vala 编写。其目标是为最终用户提供完整的桌面环境。

**要求使用 13.2-RELEASE 或更高版本**，因为几个核心组件依赖于 [deskutils/xdg-desktop-portal](https://cgit.freebsd.org/ports/tree/deskutils/xdg-desktop-portal/)。

该仓库包含一个名为 **elementary.mk** 的文件，用于 **Mk/Uses** 框架、官方应用程序和依赖于 [x11-toolkits/granite7](https://cgit.freebsd.org/ports/tree/x11-toolkits/granite7/) 的精选 Port。

我已经提交了几个补丁，以保持这些 port 的最新状态：

- [deskutils/iconbrowser](https://cgit.freebsd.org/ports/tree/deskutils/iconbrowser/)
- [multimedia/elementary-videos](https://cgit.freebsd.org/ports/tree/multimedia/elementary-videos/)
- [x11-themes/gnome-icons-elementary](https://cgit.freebsd.org/ports/tree/x11-themes/gnome-icons-elementary/)
- [editors/elementary-code](https://cgit.freebsd.org/ports/tree/editors/elementary-code/)

以下 port 的 [bug 报告](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&query_format=advanced&short_desc=elementary-calendar%20elementary-terminal%20granite7&short_desc_type=anywordssubstr) 仍然在 bugzilla 上保持打开状态，等待更新：

- [x11-toolkits/granite7](https://cgit.freebsd.org/ports/tree/x11-toolkits/granite7/): 更新到 7.3.0
- [deskutils/elementary-calendar](https://cgit.freebsd.org/ports/tree/deskutils/elementary-calendar/): 更新到 7.0.0
- [x11/elementary-terminal](https://cgit.freebsd.org/ports/tree/x11/elementary-terminal/): 更新到 6.1.2

同时，我还致力于更新 GNOME 栈（特别是 WebKitGTK、libwnck、Mutter、Vala）。我注意到了一些特别是与 [x11/plank](https://cgit.freebsd.org/ports/tree/x11/plank/) 相关的回归问题（与监视打开的应用程序有关）。

在开发仓库中新增了三个新应用程序：

- deskutils/atlas，地图查看器
- deskutils/nimbus，天气小部件
- audio/leopod，播客客户端

### FreeBSD Office 团队

链接：
[FreeBSD Office 项目](https://wiki.freebsd.org/Office) URL: [https://wiki.freebsd.org/Office](https://wiki.freebsd.org/Office)

[FreeBSD Office 邮件列表](https://lists.freebsd.org/subscription/freebsd-office) URL: [https://lists.freebsd.org/subscription/freebsd-office](https://lists.freebsd.org/subscription/freebsd-office)

联系人：FreeBSD Office 团队 ML <[office@FreeBSD.org](mailto:office@FreeBSD.org)>

联系人：Dima Panov <[fluffy@FreeBSD.org](mailto:fluffy@FreeBSD.org)>

联系人：許立文 <[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)>

FreeBSD Office 团队致力于开发一系列办公相关的软件套件和工具，如 OpenOffice 和 LibreOffice。

在本季度，工作重点是为所有 FreeBSD 用户提供最新稳定版本的 LibreOffice 套件和配套应用程序。

在 2023Q3 期间，我们为 LibreOffice port 推送了维护补丁，并将最新的 7.6.2 版本及其所有配套库，如 MDDS、libIxion 等，带入了 Ports。LibreOffice port 的所有预发布开发都在 [LibreOffice WIP 仓库](https://github.com/freebsd/freebsd-ports-libreoffice) 中进行。

与 LibreOffice 一起，我们还将 Boost 更新到最新的 1.83 版本。所有对 Boost 的移植感兴趣的人都可以向 [Boost WIP 仓库](https://github.com/fluffykhv/freebsd-ports-boost) 提交补丁。

我们正在寻找帮助完成以下任务的人：

- [打开的 bug 列表](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=office%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=substring&list_id=650685&order=Bug+Number&query_format=advanced) 包含所有需要关注的已提交问题
- 上游 [在 ports 中的本地补丁](https://cgit.freebsd.org/ports/tree/editors/libreoffice/files)

欢迎在邮件列表和 Bugzilla 中提供补丁、评论和反馈。

### Wifibox：使用 Linux 驱动 FreeBSD 上的无线网卡

链接：

[项目 GitHub 页面](https://github.com/pgj/freebsd-wifibox) URL: [https://github.com/pgj/freebsd-wifibox](https://github.com/pgj/freebsd-wifibox)

[net/wifibox port](https://cgit.freebsd.org/ports/tree/net/wifibox) URL: [https://cgit.freebsd.org/ports/tree/net/wifibox](https://cgit.freebsd.org/ports/tree/net/wifibox)

联系人：PÁLI Gábor János <[pali.gabor@gmail.com](mailto:pali.gabor@gmail.com)>

Wifibox 是一个实验性项目，用于探索在 FreeBSD 主机系统上部署虚拟化 Linux 客户端以驱动无线网卡的方法。已有一些指南说明如何手动设置此项，而 Wifibox 的目标是将这些想法实现为一个易于使用的单一软件包。

- 它使用 [bhyve(8)](https://man.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8&format=html) 运行嵌入式 Linux 系统。这有助于实现低资源占用。它需要具有 I/O MMU（AMD-Vi、Intel VT-d）的 x64 CPU，约 150 MB 物理内存，并且为客户端虚拟磁盘镜像提供一些可用的磁盘空间，根据情况可以仅为约 30 MB。它与 FreeBSD 12 及更高版本兼容，但某些网卡可能需要 FreeBSD 13。
- 客户端使用 [Alpine Linux](https://alpinelinux.org/) 构建，这是一个基于 [musl libc](https://www.musl-libc.org/) 和 [BusyBox](https://busybox.net/) 的面向安全的轻量级发行版，并导入了来自 [Arch Linux](https://archlinux.org/) 的一些自定义扩展和补丁。它附带了一些用于更好地管理正在使用的硬件的诊断工具。最新版本具有 Linux 6.1，但也提供 Linux 6.5 作为替代。
- 配置文件与主机系统共享。客户端使用 [wpa_supplicant(8)](https://man.freebsd.org/cgi/man.cgi?query=wpa_supplicant&sektion=8&format=html) 或 [hostapd(8)](https://man.freebsd.org/cgi/man.cgi?query=hostapd&sektion=8&format=html)（取决于配置）因此可以导入主机的 [wpa_supplicant.conf(5)](https://man.freebsd.org/cgi/man.cgi?query=wpa_supplicant.conf&sektion=5&format=html) 或 [hostapd.conf(5)](https://man.freebsd.org/cgi/man.cgi?query=hostapd.conf&sektion=5&format=html) 文件而无需进行任何更改。
- 配置后，客户端可以公开 [wpa_supplicant(8)](https://man.freebsd.org/cgi/man.cgi?query=wpa_supplicant&sektion=8&format=html) 和 [hostapd(8)](https://man.freebsd.org/cgi/man.cgi?query=hostapd&sektion=8&format=html) 控制套接字，从而使主机可以直接使用相关实用程序，如 [wpa_cli(8)](https://man.freebsd.org/cgi/man.cgi?query=wpa_cli&sektion=8&format=html) 或 [wpa_gui(8)](https://man.freebsd.org/cgi/man.cgi?query=wpa_gui&sektion=8&format=html)（来自 [net/wpa_supplicant_gui](https://cgit.freebsd.org/ports/tree/net/wpa_supplicant_gui/) 软件包）或 [hostapd_cli(8)](https://man.freebsd.org/cgi/man.cgi?query=hostapd_cli&sektion=8&format=html)。
- 一切都打包在一个单一的软件包中，可以轻松安装和卸载。这带有一个 [rc(8)](https://man.freebsd.org/cgi/man.cgi?query=rc&sektion=8&format=html) 系统服务，它会在启动时自动启动客户端，并在关闭时停止客户端。
- 可以配置为 IPv6 流量转发，这是一个当前为实验性选项，但默认已打开。

Wifibox 主要经过了对 Intel 芯片组的测试，并显示出很好的性能和稳定性。因此，在 FreeBSD 完善对这些芯片组的支持之前，它可能是一个过渡性的解决方案。

已确认 Wifibox 与 Atheros、Realtek 和 Mediatek 芯片组一起工作，欢迎反馈其他芯片组的情况。Broadcom 芯片（MacBook Pro 通常使用）也可以使用，但已知存在稳定性问题。

### FreeBSD 上的 GCC

链接：

[GCC 项目](https://gcc.gnu.org/) URL: [https://gcc.gnu.org/](https://gcc.gnu.org/)

[GCC 10 发布系列](https://gcc.gnu.org/gcc-10/) URL: [https://gcc.gnu.org/gcc-10/](https://gcc.gnu.org/gcc-10/)

[GCC 11 发布系列](https://gcc.gnu.org/gcc-11/) URL: [https://gcc.gnu.org/gcc-11/](https://gcc.gnu.org/gcc-11/)

[GCC 12 发布系列](https://gcc.gnu.org/gcc-12/) URL: [https://gcc.gnu.org/gcc-12/](https://gcc.gnu.org/gcc-12/)

[GCC 13 发布系列](https://gcc.gnu.org/gcc-13/) URL: [https://gcc.gnu.org/gcc-13/](https://gcc.gnu.org/gcc-13/)

联系人：Lorenzo Salvadore <[salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)>

将默认的 GCC 版本更新到 GCC 13 的过程已经开始，并进行了[测试运行](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=273397)。感谢运行测试运行的 [Antoine Brodin](mailto:antoine@FreeBSD.org) 以及所有其他参与的开发人员和 port 维护人员。

同样的测试运行包含了上一季度状态报告中预期的其他补丁。特别是包含了更新以下内容的补丁：

- [lang/gcc11](https://cgit.freebsd.org/ports/tree/lang/gcc11/) 到版本 11.4.0;
- [lang/gcc12](https://cgit.freebsd.org/ports/tree/lang/gcc12/) 到版本 12.3.0;
- [lang/gcc13](https://cgit.freebsd.org/ports/tree/lang/gcc13/) 到版本 13.2.0。

读者可能还记得我计划在 GCC 13.1.0 发布后立即将默认版本更新为 GCC 13，但可以注意到 GCC 开发人员在我努力处理 GCC port 时更快地发布了 13.2.0 版本。

在测试运行中报告的大多数错误都是由同一错误引起的：`error: expected identifier before '__is_convertible'`。似乎问题是 FreeBSD 12 的 libcxx 与 GCC 13 标头之间的不兼容性。请查看[测试运行中的讨论](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=273397) 获取更多信息，并提供你的反馈。

### Valgrind：为 FreeBSD 15 更新 valgrind-devel

链接：

[Valgrind 主页](https://www.valgrind.org/) URL: [https://www.valgrind.org/](https://www.valgrind.org/)

[Valgrind 新闻](https://www.valgrind.org/docs/manual/dist.news.html) URL: [https://www.valgrind.org/docs/manual/dist.news.html](https://www.valgrind.org/docs/manual/dist.news.html)

联系人：Paul Floyd <[pjfloyd@wanadoo.fr](mailto:pjfloyd@wanadoo.fr)>

[devel/valgrind-devel](https://cgit.freebsd.org/ports/tree/devel/valgrind-devel/) 正在更新的过程中。这包含了即将在十月份正式发布的 Valgrind 3.22 版本中的大部分内容。

`memcheck` 已经增强了一些检查。它现在会报告使用大小为零的 `realloc`。这样的用法是不可移植的，并已被弃用（C23 将使其成为未定义行为）。`memcheck` 现在验证用于 `memalign`、`posix_memalign`、`aligned_alloc` 以及所有 `operator new` 和 `operator delete` 的对齐和大小重载的值。读取 `DWARF` 调试信息现在以一种懒惰的方式进行，这可以提高性能。

通常有许多小的 bug 修复。

对于 FreeBSD，现在支持 FreeBSD 15。现在支持两个额外的 `_umtx_op` 操作，`UMTX_OP_GET_MIN_TIMEOUT` 和 `UMTX_OP_SET_MIN_TIMEOUT`。修复了对具有 guest pid 或 -1 的 sysctl kern proc pathname 使用的问题，之前返回的是 Valgrind 主机的路径。现在 sysctl 将返回 guest 的路径。已添加对 `close_range` 系统调用的支持。

### GitLab 16.3 已发布

链接：

[Gitlab 16.3 新特性](https://about.gitlab.com/releases/2023/08/22/gitlab-16-3-released/) URL: [https://about.gitlab.com/releases/2023/08/22/gitlab-16-3-released/]
(https://about.gitlab.com/releases/2023/08/22/gitlab-16-3-released/)

联系人：Matthias Fechner <[mfechner@FreeBSD.org](mailto:mfechner@FreeBSD.org)>

GitLab 是一个 DevOps 平台。它为团队带来了高效的速度，充满信心的开发过程，无需牺牲安全性，并提供对 DevOps 成功的全面可见性。

版本 16.3 现在在 FreeBSD 上可用，请查看 [www/gitlab-ce](https://cgit.freebsd.org/ports/tree/www/gitlab-ce/) Port。升级非常重要，因为版本 16.3 将是以后所有升级的要求。只有从 GitLab 16.3 才能升级到 16.4。

可以在 [https://gitlab.fechner.net/mfechner/Gitlab-docu/-/blob/master/install/16.3-freebsd.md?ref_type=heads](https://gitlab.fechner.net/mfechner/Gitlab-docu/-/blob/master/install/16.3-freebsd.md?ref_type=heads) 找到。升级的文档可在 [https://gitlab.fechner.net/mfechner/Gitlab-docu/-/blob/master/update/16.1-16.3-freebsd.md?ref_type=heads](https://gitlab.fechner.net/mfechner/Gitlab-docu/-/blob/master/update/16.1-16.3-freebsd.md?ref_type=heads) 找到安装文档。

我将等到 16.4 版本升级（预计在 20.9 或 22.9 左右发布，不确定），直到创建 ports 的 *quarterly* 分支 2023Q4，以避免破坏不使用主分支 (*latest*) 的系统。GitLab 用户应始终选择主分支，如安装手册中所述。

### PortOptsCLI — Ports 可访问性

链接：

[项目存储库](https://gitlab.com/alfix/portoptscli) URL: [https://gitlab.com/alfix/portoptscli](https://gitlab.com/alfix/portoptscli)

联系人：Alfonso Sabato Siciliano <[asiciliano@FreeBSD.org](mailto:asiciliano@FreeBSD.org)>

联系人：FreeBSD 可访问性邮件列表 <[freebsd-accessibility@FreeBSD.org](mailto:freebsd-accessibility@FreeBSD.org)>

FreeBSD 提供了 Ports，为用户和管理员提供了一种安装应用程序的简单方法。在构建和安装之前可以配置一个 Port。`make config` 命令使用 [ports-mgmt/dialog4ports](https://cgit.freebsd.org/ports/tree/ports-mgmt/dialog4ports/) 和 [ports-mgmt/portconfig](https://cgit.freebsd.org/ports/tree/ports-mgmt/portconfig/) 通过文本用户界面（TUI）交互式设置 Port。

不幸的是，屏幕阅读器在 TUI 中表现不佳；这是一个众所周知的可访问性问题。FreeBSD 提供了数以万计的 port；port 配置是一个关键功能，但对于视力受损的用户而言是不可访问的。

PortOptsCLI（Port Options CLI）是一个通过命令行界面设置 port 选项的新实用程序。确切地说，PortOptsCLI 提供了导航配置对话框（复选框/单选按钮）并通过交互方式设置其项目的命令。它也适用于语音合成器；目前已与 [accessibility/orca](https://cgit.freebsd.org/ports/tree/accessibility/orca/) 进行了测试。可以通过 [ports-mgmt/portoptscli](https://cgit.freebsd.org/ports/tree/ports-mgmt/portoptscli/) port 或软件包安装 PortOptsCLI。

欢迎提供建议和新想法。如果可能，请将报告发送到 FreeBSD 可访问性邮件列表，以在公共位置共享和跟踪讨论。

## 第三方项目

许多项目基于 FreeBSD 或将 FreeBSD 的组件纳入其项目中。由于这些项目可能对更广泛的 FreeBSD 社区感兴趣，因此我们有时会在季度报告中包含这些项目提交的简要更新。FreeBSD 项目对这些提交中的任何声明的准确性或真实性不作表示。

### 介绍 BSD Cafe 项目

链接：

[BSD Cafe 项目主页](https://wiki.bsd.cafe/) URL: [https://wiki.bsd.cafe/](https://wiki.bsd.cafe/)

[BSD Cafe Mastodon 实例](https://mastodon.bsd.cafe/) URL: [https://mastodon.bsd.cafe/](https://mastodon.bsd.cafe/)

联系人：Stefano Marinelli <[stefano@dragas.it](mailto:stefano@dragas.it)>

我们很高兴向大家介绍 BSD Cafe 项目的首个组成部分！

数月前，当我首次注册 [bsd.cafe](https://bsd.cafe/) 域名时，我构想了一个主题酒吧，在那里朋友、熟人和顾客可以聚在一起进行关于 \*BSD 系统、Linux 和开源技术的非正式对话。就像任何酒吧一样，我们的讨论可以涵盖各种主题，同时保持相互尊重的精神。

BSD Cafe 将成为由 \*BSD 驱动的各种工具和服务的中心。

我们的首次亮相是一个全新的 [Mastodon](https://joinmastodon.org/) 实例（开源微博客软件和服务），作为通向联合宇宙的门户，联合宇宙是许多使用 [ActivityPub](https://www.w3.org/TR/activitypub) 去中心化社交网络协议的服务联合体。现在已开放注册。该服务器遵循明确定义的指南，促进积极的行为，并明确禁止任何形式的仇恨。包容性、尊重和建设性对话是该实例的基石。

我们的主要服务器目前托管在芬兰的一个小型虚拟机上，运行在 FreeBSD 上。服务被划分为 VNET jails，在本地区域网络中通过专用桥连接。此外，我们实施了 VPN 系统，并具有将单个 jails 迁移到更强大机器的灵活性。

为了进行多媒体数据和缓存托管，我们使用了一个独立的物理服务器（同样基于 FreeBSD，在一个 jail 中），由 Cloudflare 管理。这里的目标是缓存和地理分布数据，从而有效减少主 VPS 上的网络拥塞。

我们的反向代理（前端）、邮件服务器、媒体服务器和实例本身都可以通过 IPv6 访问。

在初始阶段，这个 Mastodon 实例没有预加载的内容。我们的意图是让它根据用户的兴趣和关注者有机地发展。在这个阶段，我们已经克制了先发制人的封锁。我们强烈鼓励用户及时报告任何他们认为需要关注的事情。

我们邀请你加入我们的 [https://mastodon.bsd.cafe/](https://mastodon.bsd.cafe/)，以培养一个重视建设性互动并拥抱包容性的社区，一个为所有人提供安全而宁静的空间。

此外，我们建立了一个网站，地址是 [https://wiki.bsd.cafe/](https://wiki.bsd.cafe/)，将提供有关我们的工具、服务、规则、正常运行时间等的概述。

最近，已进行了 Miniflux 安装，因此 BSD Cafe 用户可以将其用作个人 RSS 订阅阅读器。更多信息：[https://wiki.bsd.cafe/miniflux-bsd-cafe](https://wiki.bsd.cafe/miniflux-bsd-cafe)。

### 容器与 FreeBSD：Pot、Potluck 和 Potman

链接：

[Pot 在 GitHub 上的组织](https://github.com/bsdpot) URL: [https://github.com/bsdpot](https://github.com/bsdpot)

联系人：Luca Pizzamiglio (Pot) <[pizzamig@FreeBSD.org](mailto:pizzamig@FreeBSD.org)>

联系人：Bretton Vine (Potluck) <[bv@honeyguide.eu](mailto:bv@honeyguide.eu)>

联系人：Michael Gmelin (Potman) <[grembo@FreeBSD.org](mailto:grembo@FreeBSD.org)>

Pot 是一个 Jail 管理工具，[还支持通过 Nomad 进行编排](https://www.freebsd.org/news/status/report-2020-01-2020-03/#pot-and-the-nomad-pot-driver)。

在本季度，完成了 [Pot 0.15.6](https://github.com/bsdpot/pot/pull/274)，增加了自定义 [pf(4)](https://man.freebsd.org/cgi/man.cgi?query=pf&sektion=4&format=html) 规则配置钩子。

此外，发布了 [Nomad Pot Driver 0.9.1](https://github.com/bsdpot/nomad-pot-driver/releases/tag/v0.9.1)，该驱动程序允许在 Nomad 作业说明中设置 Pot 属性。

Potluck 的目标是成为 FreeBSD 和 Pot 的 Dockerhub：Pot 的 flavor 和完整的容器镜像的存储库，可用于 Pot 以及许多情况下的 Nomad。

提供了相当多的新容器镜像，例如 [Caddy S3 代理](https://github.com/bsdpot/potluck/tree/master/caddy-s3-nomad)、[Mastodon 实例](https://github.com/bsdpot/potluck/tree/master/mastodon-s3) 和 [Redis 容器](https://github.com/bsdpot/potluck/tree/master/redis-single)。总共有 50 个容器可供使用，可以在 [Potluck 镜像注册表](https://potluck.honeyguide.net/) 中下载为现成的镜像（如果你信任我们的构建过程），或者可以从 [Potluck GitHub 仓库](https://github.com/bsdpot/potluck) 中存储的 Pot  flavor 文件中自行构建。

2023 年 7 月 / 8 月的 FreeBSD 期刊包含了 Luca 的 [使用 pot 和 nomad 进行 Jail 编排](https://freebsdfoundation.org/wp-content/uploads/2023/08/Pizzamiglio.pdf) 文章，解释了如何使用 Pot 和 Potluck 与 Nomad 一起在多个主机上进行容器编排。

最后但同样重要的是，一个补丁（[90b1184d93c8](https://cgit.freebsd.org/ports/commit/?id=90b1184d93c8)）为 [devel/sccache](https://cgit.freebsd.org/ports/tree/devel/sccache/) port 添加了构建集群支持。

一如既往，欢迎反馈和补丁。

赞助商：Nikulipe UAB，Honeyguide Group

**最后修改于**：2023 年 11 月 7 日，由 [Lorenzo Salvadore](https://cgit.freebsd.org/doc/commit/?id=6dda2e9ab0)
