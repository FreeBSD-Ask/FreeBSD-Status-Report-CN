# FreeBSD 2023 年第一季度状态报告

- 原文链接：[FreeBSD Status Report First Quarter 2023](https://www.freebsd.org/status/report-2023-01-2023-03/)

这是 2023 年的第一份状态报告，共包含 25 篇报告：我们带来了常规的团队报告、云项目的最新动态，以及 src、ports 和 doc 树的进展等内容。  

此外，我们还提供了一些关于 [13.2-RELEASE](https://www.freebsd.org/releases/13.2R/announce/) 的信息。该版本原定于 2023 年第一季度末发布，但由于本报告发布时新版本已经释出，因此用户现在可以直接安装。现在 RELEASE 版本的用户可以享受到诸多改进，例如对 [iwlwifi(4)](https://man.freebsd.org/cgi/man.cgi?query=iwlwifi&sektion=4&format=html) 驱动有更好的支持，以及全新的 [rtw88(4)](https://man.freebsd.org/cgi/man.cgi?query=rtw88&sektion=4&format=html) 驱动等，这些主题在既往状态报告中已有涉及。  

祝阅读愉快！  

Lorenzo Salvadore 代表状态团队敬上。

## FreeBSD 团队报告  

可在 [管理页面](https://www.freebsd.org/administration/) 找到来自各个官方和半官方团队的报告。  

### FreeBSD 核心团队  

**联系人**：FreeBSD 核心团队 <[core@FreeBSD.org](mailto:core@FreeBSD.org)>  

FreeBSD 核心团队是 FreeBSD 的管理机构。  

#### 事项  

##### 核心团队章程：草案  

在 2023 年的第一次核心团队会议上，来自 2022 年 12 月美国博尔德会议的团队代表向整个团队汇报了代表团的结论。团队将继续讨论相关问题，并与 FreeBSD 基金会合作推进。  

##### FreeBSD 年度开发者调查  

核心团队与 FreeBSD 基金会达成一致，由 FreeBSD 基金会负责开展年度开发者调查。  

##### Matrix 即时通讯方案  

核心团队正在持续评估 Matrix 作为 FreeBSD 开发者的即时通讯（IM）解决方案。目前已部署了一个实例，并正在进行测试。  

#### Commit 权限  

* 核心团队批准了 Cheng Cui (cc@) 的 src commit 权限。  
* 核心团队批准恢复 Joseph Koshy (jkoshy@) 的 src commit 权限。  

### FreeBSD 基金会  

**相关链接**： 

[FreeBSD 基金会](https://www.freebsdfoundation.org/)：[https://www.freebsdfoundation.org](https://www.freebsdfoundation.org/)  
[技术路线图](https://freebsdfoundation.org/blog/technology-roadmap/)：[https://freebsdfoundation.org/blog/technology-roadmap/](https://freebsdfoundation.org/blog/technology-roadmap/)  
[捐赠](https://www.freebsdfoundation.org/donate/)：[https://www.freebsdfoundation.org/donate/](https://www.freebsdfoundation.org/donate/)  
[基金会合作伙伴计划](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)：[https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)  
[FreeBSD 期刊](https://www.freebsdfoundation.org/journal/)：[https://www.freebsdfoundation.org/journal/](https://www.freebsdfoundation.org/journal/)  
[基金会新闻与活动](https://www.freebsdfoundation.org/news-and-events/)：[https://www.freebsdfoundation.org/news-and-events/](https://www.freebsdfoundation.org/news-and-events/)  

**联系人**：Deb Goodkin <[deb@FreeBSDFoundation.org](mailto:deb@FreeBSDFoundation.org)>  

FreeBSD 基金会是一家 501(c)(3) 非营利组织，致力于支持和推广 FreeBSD 项目及其全球社区。基金会接受个人和企业捐赠，以资助和管理软件开发项目、会议和开发者峰会。我们还向 FreeBSD 贡献者提供旅行资助，购买和维护硬件以改进 FreeBSD 基础设施，并提供资源以增强安全性、质量保证和版本工程工作。  

此外，基金会还发布推广材料，以宣传、教育并倡导 FreeBSD 项目，促进商业供应商与 FreeBSD 开发者之间的合作，并作为 FreeBSD 项目的法律实体，处理合同、许可协议及其他法律事务。

#### 筹款工作  

我们的 2022 年筹款数据终于统计完成，总共筹集了 **$1,231,096**！不过，这一金额未能达到我们的目标，因此我们不得不动用 **$74,000** 的长期投资资金。  

除了来自用户和贡献者的大量捐款，我们还收到了来自 Juniper、Meta、Arm、奈飞、倍福、Tarsnap、Modirum、Koum Family Foundation 和 Stormshield 等公司的大额捐款。在此，我谨代表基金会向所有个人和企业捐助者致以最诚挚的感谢，感谢大家在 2022 年的财政支持！  

今年，我们的预算约为 **$2,230,000**，其中包括对 FreeBSD 宣传推广和软件开发的更多投入。超过一半的预算将直接用于提升 FreeBSD 并保障其安全性。为了满足 2023 年的预算需求，我们提高了筹款目标，并计划使用部分投资资金。当我们收到第一笔百万美元捐款时，就制定了每年使用最多 10% 资金以增强 FreeBSD 开发工作的计划，因此这已成为我们多年来的筹资策略之一。  

目前，2023 年预算正在由董事会审批，待批准后将正式公布。  

本季度，我们收到了来自 Juniper、Tarsnap、微软和 Stormshield 的捐款，可谓开局良好！但为了支持 2023 年的各项计划，我们仍需更多资金。  

如果你希望帮助我们继续推进 FreeBSD 相关工作，请考虑为我们的 **2023 年筹款活动** 捐款：[https://www.freebsdfoundation.org/donate/](https://www.freebsdfoundation.org/donate/)  

此外，我们还设有 **合作伙伴计划**，面向大额商业捐助者，详情请访问：[https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/](https://freebsdfoundation.org/our-donors/freebsd-foundation-partnership-program/)  

#### 操作系统改进  

在 2023 年第一季度，共有 **226** 个 src、**39** 个 ports 和 **12** 个 doc 树的提交将基金会标注作为赞助方。其中部分工作在单独的报告条目中进行了详细介绍：  

* 持续集成  
* 在启用了日志式软更新的文件系统上启用快照  
* FreeBSD 作为一级架构 cloud-init 平台  
* FreeBSD 发行工程团队  
* 改进 **kinst DTrace** 提供程序  
* 在 FreeBSD 上运行 **OpenStack**  

此外，基金会还赞助了以下工作：  

* **OpenSSH** 修复与更新至 **9.2p1** 和 **9.3p1** 版本  
* **libpcap** 导入第三方并更新至 **1.10.3** 版本  
* **tmpfs**、**msdosfs** 和 **makefs** 的改进  
* 新增 **kqueue1** 系统调用  
* **man 页面** 更新  
* **DTrace** 和 **bhyve** 的修复  
* **LinuxKPI** 相关工作  

#### 持续集成与质量保证  

基金会为 FreeBSD 项目提供了一名全职员工，并资助多个项目，以改进持续集成（CI）、自动化测试以及整体质量保证工作。你可以在专门的报告条目中了解更多 CI 相关工作。  

目前，基金会正在资助一个项目，目标是开发一组脚本，帮助 **src 开发者** 进行 CI 测试。该项目的主要目标之一是在 **提交前阶段** 提供更多可见性。[第一阶段的评审](https://reviews.freebsd.org/D38815) 已提交。

#### FreeBSD 宣传与教育

我们的大部分工作致力于推广 FreeBSD 项目。这可能包括宣传有趣的 FreeBSD 成果、制作宣传资料和视频教程、参加活动或进行演讲。我们制作的宣传资料旨在教授人们 FreeBSD 的基础知识，帮助他们更容易地采用或为该项目做出贡献。除了参加和演讲之外，我们还鼓励并协助社区成员举办自己的 FreeBSD 活动、进行演讲或设置 FreeBSD 展台。

FreeBSD 基金会赞助了全球众多会议、活动和峰会。这些活动可以是 BSD 相关、开源或面向代表性不足群体的技术活动。我们支持以 FreeBSD 为主题的活动，以便为知识分享、项目合作以及开发者与商业用户之间的协作提供平台，从而构建一个健康的生态系统。同时，我们支持非 FreeBSD 活动，以宣传和提升 FreeBSD 的知名度，增加 FreeBSD 在各个应用领域中的使用，并吸引更多贡献者加入该项目。我们已基本恢复了面对面参加活动，并开始筹划于 2023 年 5 月举行的面对面开发者峰会，该峰会将与 BSDCan 同时举办。除了参加和筹划活动外，我们还不断推出新的培训计划，并更新我们的 [操作指南](https://freebsdfoundation.org/freebsd-project/resources/)，以便让更多人尝试 FreeBSD。

看看我们在宣传与教育方面的一些工作：

* 在比利时布鲁塞尔举办的 FOSDEM 2023（2023 年 2 月 4-5 日）设立了展位。查看 [行程报告](https://freebsdfoundation.org/blog/fosdem-2023-conference-report/)。
* 在英国伦敦举办的 State of Open Con 2023（2023 年 2 月 7-8 日）设立了展台。 [了解更多](https://freebsdfoundation.org/blog/advocating-for-freebsd-around-the-world/)。
* 在美国加州帕萨迪纳举办的 SCALE 20x（2023 年 3 月 9-12 日）中赞助并举办了研讨会，同时设立了展位。查看 [行程报告](https://freebsdfoundation.org/blog/freebsd-at-scale-20x/)。
* 在美国北卡罗来纳州夏洛特赞助了 Open Source 101（2023 年 3 月 23 日）。
* 赞助并开始筹划将于 2023 年 5 月 17-18 日在加拿大安大略省渥太华举办的面对面 [开发者峰会](https://wiki.freebsd.org/DevSummit/202305)。
* 确保了我们的媒体合作伙伴赞助地位，并为将于 2023 年 10 月 15-17 日在美国北卡罗来纳州罗利举行的 [All Things Open](https://2023.allthingsopen.org/) 提交了研讨会方案。
* 为将于 2023 年 7 月 13-16 日在美国俄勒冈州波特兰举行的 [FOSSY](https://sfconservancy.org/fossy/) 提交了研讨会提案。
* FreeBSD 项目已被接纳为 Google Summer of Code 的 [参与组织](https://summerofcode.withgoogle.com/programs/2023/organizations/the-freebsd-project)。
* 我们举办了 [GSoC 办公时间](https://youtu.be/NpOkTR_d8os) 以帮助潜在参与者解答疑问。
* 发布了 [三月通讯](https://freebsdfoundation.org/news-and-events/newsletter/freebsd-foundation-update-march-2023/)。
* 其他博客文章：
  * [探索 FreeBSD 与 Ampere Altra 的内核秘密](https://freebsdfoundation.org/blog/under-the-hood-with-freebsd-and-ampere-altra/)
  * [招聘启事：FreeBSD 用户空间软件开发工程师](https://freebsdfoundation.org/blog/under-the-hood-with-freebsd-and-ampere-altra/) — 注：该职位目前已停止招聘。
  * [BSDCan 2023 差旅补助申请现已开启](https://freebsdfoundation.org/blog/bsdcan-2023-travel-grant-application-now-open/) — 注：申请现已结束。
* FreeBSD 新闻报道：
  * [VMBlog 与 Deb Goodkin 对谈“开放大会现状”](https://freebsdfoundation.org/news-and-events/latest-news/vmblog-state-of-open-con-qa-with-deb-goodkin/)

我们通过发布专业制作的 **FreeBSD 期刊** 来教育全球用户了解 FreeBSD。如前所述，FreeBSD 期刊现已免费发行。你可以在 [https://www.freebsdfoundation.org/journal/](https://www.freebsdfoundation.org/journal/) 了解更多信息并获取最新期刊。

有关我们参加的活动及即将举行的活动的更多信息，请访问 [https://www.FreeBSDfoundation.org/news-and-events/](https://www.freebsdfoundation.org/news-and-events/)。

#### 法律/FreeBSD 知识产权

基金会拥有 FreeBSD 的商标，保护这些商标是我们的责任。同时，我们也为 核心团队提供法律支持，以调查相关问题。

请访问 [https://www.freebsdfoundation.org](https://www.freebsdfoundation.org/) 了解更多关于我们如何支持 FreeBSD以及我们能为你提供哪些帮助的信息！



### FreeBSD 发行工程团队

**相关链接**：  
[FreeBSD 13.2-RELEASE 日程](https://www.freebsd.org/releases/13.2R/schedule/)  
[FreeBSD 14.0-RELEASE 日程](https://www.freebsd.org/releases/14.0R/schedule/)  
[FreeBSD 版本](https://download.freebsd.org/releases/ISO-IMAGES/)  
[FreeBSD 开发快照](https://download.freebsd.org/snapshots/ISO-IMAGES/)

**联系人**：FreeBSD 发行工程团队 <[re@FreeBSD.org](mailto:re@FreeBSD.org)>

FreeBSD 发行工程团队负责为 FreeBSD 官方项目发布设定和公布发行日程，宣布代码冻结，以及维护相关分支等工作。

在 2023 年第一季度，发行工程团队开始了即将推出的 13.2-RELEASE 工作。截至目前，13.2 版本周期按照原定日程进行，不过增加了第四、第五和第六个 RC 版本，将最终发行时间从三月底推迟到四月初。

发行工程团队继续为 **main**、**stable/13** 和 **stable/12** 分支提供每周的开发快照构建。

**赞助商**：Rubicon Communications, LLC ("Netgate")  
**赞助商**：Tarsnap  
**赞助商**： FreeBSD 基金会



### 集群管理团队

**相关链接**：  
[集群管理团队成员](https://www.freebsd.org/administration/#t-clusteradm)

**联系人**：集群管理团队 <[clusteradm@FreeBSD.org](mailto:clusteradm@FreeBSD.org)>

FreeBSD 集群管理团队负责管理项目依赖的机器，这些机器用于同步分布式工作和通信。

本季度，团队的工作内容包括：

* 定期支持 FreeBSD.org 用户账户。
* 为所有物理主机和镜像站提供定期的磁盘及零部件支持（包括更换）。
* 改进 PowerPC 软件包构建器。
  * 借助 FreeBSD 基金会提供的新零件，构建器现在配置了带散热片的新 NVMe 硬盘和更多内存，成功解决了过热问题，并显著加快了软件包构建速度。
* 将动态资源与主网站解耦。
  * 与文档工程团队（doceng）和网站管理员（webmaster）协调工作，将动态资源从 www.FreeBSD.org 和 docs.FreeBSD.org 网站中解耦出来。

#### 正在进行的工作

* 对主站进行大规模网络升级。
  * 我们的主站已收到新的 [Juniper](https://www.juniper.net/) 交换机，以替换旧设备。感谢 Juniper 的捐赠。
* 更换主站和部分镜像站中的旧服务器。
  * 除了已损坏的 CI 服务器外，我们还有几台旧服务器存在磁盘损坏和电源故障的问题。此项任务正与 FreeBSD 基金会及其他捐赠者/赞助商共同推进。
* 部署镜像网站的基础设施。
  * 由于 FreeBSD 网站现已基本为静态内容，我们已开始部署基础设施，以在全球 FreeBSD 项目管理的镜像站点上镜像 www.FreeBSD.org 和 docs.FreeBSD.org。
* 为内部 FreeBSD.org 搜索需求创建全新的搜索数据库引擎，支持例如邮件列表和文档的搜索。

#### FreeBSD 官方镜像概况

当前的镜像站点分布在：  
**澳大利亚、巴西、德国、日本（两个全量镜像站）、马来西亚、南非、台湾、英国（全量镜像站）以及美国——加利福尼亚、新泽西（主站）和华盛顿。**

硬件和网络连接由下列单位慷慨提供：

* [Bytemark Hosting](https://www.bytemark.co.uk/)
* [BroadBand Tower, Inc. 的云与 SDN 实验室](https://www.bbtower.co.jp/en/corporate/)
* [國立陽明交通大學資訊工程學系](https://www.cs.nycu.edu.tw/)
* [Equinix](https://deploy.equinix.com/)
* [澳大利亚互联网协会](https://internet.asn.au/)
* [Internet Systems Consortium](https://www.isc.org/)
* [INX-ZA](https://www.inx.net.za/)
* [KDDI Web Communications Inc](https://www.kddi-webcommunications.co.jp/english/)
* [马来西亚研究与教育网络](https://www.mohe.gov.my/en/services/research/myren)
* [Metapeer](https://www.metapeer.com/)
* [New York Internet](https://www.nyi.net/)
* [NIC.br](https://nic.br/)
* [Your.Org](https://your.org/)

位于法兰克福的单机镜像是欧洲主要的带宽和使用量最大的镜像站。

我们仍在寻找位于欧洲的额外全量镜像站（需要五台服务器），以替换英国现有的全量镜像站的老旧服务器。

目前我们已经注意到，在全球互联网交换中心（如澳大利亚、巴西和南非）设立单机镜像是一种不错的模式；如果你认识或在这些中心工作的人员能够赞助一台单机镜像服务器，请与我们联系。美国（西海岸）和欧洲（任一地点）是优选区域。

有关全量镜像站的完整规格，请参见 [通用镜像布局](https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout)；有关单机镜像站，请参见 [tiny-mirror](https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror)。



### 持续集成

**相关链接**：  
[FreeBSD Jenkins 实例](https://ci.freebsd.org/)  
[FreeBSD CI 构件存档](https://artifact.ci.freebsd.org/)  
[FreeBSD Jenkins Wiki](https://wiki.freebsd.org/Jenkins)  
[托管 CI Wiki](https://wiki.freebsd.org/HostedCI)  
[第三方软件 CI](https://wiki.freebsd.org/3rdPartySoftwareCI)  
[Tickets 相关于 freebsd-testing@](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)  
[FreeBSD CI 代码仓库](https://github.com/freebsd/freebsd-ci)  
[dev-ci 邮件列表](https://lists.freebsd.org/subscription/dev-ci)

**联系方式**：  
* Jenkins 管理员 <[jenkins-admin@FreeBSD.org](mailto:jenkins-admin@FreeBSD.org)>  
* Li-Wen Hsu <[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)>  
* [freebsd-testing 邮件列表](https://lists.freebsd.org/mailman/listinfo/freebsd-testing)  
* [EFNet 上的 IRC #freebsd-ci 频道]()

在 2023 年第一季度，我们与项目的贡献者和开发者合作，满足他们的测试需求。同时，我们也与外部项目和公司合作，通过在 FreeBSD 上进行更多测试来提升他们产品的质量。

**已完成的重要任务：**

* [FreeBSD-main-aarch64-KASAN_test](https://ci.freebsd.org/job/FreeBSD-main-aarch64-KASAN_test/) 以及相关支持任务已添加。
* [FreeBSD-stable-13-amd64-KASAN_test](https://ci.freebsd.org/job/FreeBSD-stable-13-amd64-KASAN_test/) 以及相关支持任务已添加。
* [FreeBSD-main-amd64-gcc12_build](https://ci.freebsd.org/job/FreeBSD-main-amd64-gcc12_build/) 现已向可能相关的提交者发送失败报告。
* 对 trasz@ 提交的非 x86 架构测试进行了各种修复或变通处理。
* 在 [AsiaBSDCon 2023 开发者峰会](https://wiki.freebsd.org/DevSummit/202303) 上进行了测试/CI 状态更新报告。

**正在进行的任务：**

* 设计并实现提交前（pre-commit）的 CI 构建和测试（以支持 [工作流程工作组](https://gitlab.com/bsdimp/freebsd-workflow)）。
* 设计并实现利用 CI 集群构建发行构件，类似发行工程的工作方式。
* 简化贡献者和开发者搭建 CI/测试环境的流程。
* 搭建 CI 阶段环境，并在其上部署实验性任务。
* 整理 freebsd-ci 代码仓库中的脚本，为合并到 src 代码仓库做准备。
* 改进硬件测试实验室，并增加更多用于测试的硬件。
* 合并 [https://reviews.freebsd.org/D38815](https://reviews.freebsd.org/D38815)。
* 合并 [https://reviews.freebsd.org/D36257](https://reviews.freebsd.org/D36257)。

**待办或排队的任务：**

* 收集和整理 [CI 任务和想法](https://hackmd.io/@FreeBSD-CI/freebsd-ci-todo)。
* 为运行测试的虚拟机设置公共网络访问。
* 实现使用裸金属硬件运行测试套件。
* 添加针对 -CURRENT 版本的 drm ports 构建测试。
* 计划运行 ztest 测试。
* 帮助更多软件将 FreeBSD 支持集成到其 CI 流水线中（相关 Wiki 页面：[3rdPartySoftwareCI](https://wiki.freebsd.org/3rdPartySoftwareCI) 和 [HostedCI](https://wiki.freebsd.org/HostedCI)）。
* 与托管 CI 提供商合作，以获得更好的 FreeBSD 支持。

有关更多正在进行中的信息，请参阅 [freebsd-testing@ 相关的 Bugzilla 工单](https://bugs.freebsd.org/bugzilla/buglist.cgi?bug_status=%3Cem%3Eopen%3C/em%3E&email1=testing%40FreeBSD.org&emailassigned_to1=1&emailcc1=1&emailtype1=equals)，并欢迎你加入我们的工作！

**赞助商： FreeBSD 基金会**


### Ports Collection

**相关链接：**  
[关于 FreeBSD Ports](https://www.freebsd.org/ports/)  
[如何为 Ports 做贡献](https://docs.freebsd.org/en/articles/contributing/#ports-contributing)  
[FreeBSD Ports 监控](http://portsmon.freebsd.org/)  
[Ports 管理团队](https://www.freebsd.org/portmgr/)  
[Ports Tarball](http://ftp.freebsd.org/pub/FreeBSD/ports/ports/)

**联系人：**  
René Ladan <[portmgr-secretary@FreeBSD.org](mailto:portmgr-secretary@FreeBSD.org)>  
FreeBSD Ports 管理团队 <[portmgr@FreeBSD.org](mailto:portmgr@FreeBSD.org)>

Ports 管理团队负责监督 Ports Tree 的总体方向、构建软件包（通过其子系统 pkgmgr）以及人员管理。以下是本季度发生的事项：

- 目前 Ports 中大约有 33,500 个 Port。针对这些 Port，共有 3,021 个未解决的问题报告，其中有 764 个尚未分配。
- 今年前三个月，`main` 分支有 163 位提交者提交了 9,021 次提交，而 `2023Q1` 分支有 55 位提交者提交了 701 次提交。与 `2022Q4` 相比，这意味着 Port 数量、Port PR、Port 提交次数以及活跃的 Ports 提交者都有小幅增长。

本季度期间，我们迎来了以下新成员或回归成员：  
- 欢迎 Robert Clausecker (fuz@)、Vladimir Druzenko (vvd@) 以及 Robert Nagy (rnagy@)；  
- 欢迎 Norikatsu Shigemura (nork@) 回归；  
- 向 Marius Strobl (marius@) 道别。  
此外，Portgmr 在成功完成 lurkership 后，新增了 Muhammad Moinur Rahman (bofh@) 成为新成员。

在每两周一次的 portmgr 会议上，讨论了以下主题：

- 改善内核模块二进制软件包的现状；
- 如何衡量 Port 对其依赖项的影响以及如何维护高影响力的 Port。

本季度还进行了 32 次 exp-run，用于测试 Port更新、更改默认版本（例如：LLVM 升级至 15、MySQL 升级至 8.0、Ruby 升级至 3.1）以及在 base 中更新 byacc。此外，Go 的默认版本切换到了 1.20，而 Lazarus 的默认版本切换到了 2.2.6。

引入了四个新的 USES 变量：

- `budgie`：支持与 Budgie 桌面相关的 Port；
- `ldap`：为 OpenLDAP 提供支持，默认版本更新为 26（即 2.6）；
- `nextcloud`：支持 Nextcloud 应用程序；
- `ruby`：为  Port Ruby 提供支持（原先为 `bsd.ruby.mk`）。



### Status Team

**相关链接：**  
[FreeBSD 状态报告](https://www.freebsd.org/status/)  
[FreeBSD 状态报告流程](https://docs.freebsd.org/en/articles/freebsd-status-report-process/)  
[已存档状态报告 GitHub 仓库](https://github.com/freebsd/freebsd-quarterly)

**联系人：**  
<[status@FreeBSD.org](mailto:status@FreeBSD.org)>

#### 新工作流程已启动

今年第一季度，[status team](https://reviews.freebsd.org/project/profile/88/) 开始实施去年底宣布的新工作流程。以下是一些细节说明。

#### 新的电子邮件地址

上个季度我们宣布创建了新的电子邮件地址：

- <[status@FreeBSD.org](mailto:status@FreeBSD.org)>：用于直接与 *status* 团队互动；
- <[status-submissions@FreeBSD.org](mailto:status-submissions@FreeBSD.org)>：用于提交报告；
- <[freebsd-status-calls@FreeBSD.org](mailto:freebsd-status-calls@FreeBSD.org)>：这是一个邮件列表，你可以 [订阅](https://lists.freebsd.org/subscription/freebsd-status-calls) 以获取状态报告提交截止日期的提醒。

遗憾的是，目前该邮件列表的运作并未达到预期。[该问题已被报告](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=269893)，但尚未找到解决方案。不过，通过变通方法，我们成功将第二次和最后一次提醒发送到了该 [邮件列表](https://lists.freebsd.org/archives/freebsd-status-calls/2023-March/)。

#### 自动化

我们引入了一些自动化措施，以确保不会丢失任何报告提交：

- 在 Phabricator 上，通过 [herald rule](https://reviews.freebsd.org/H166) 自动阻止任何修改状态报告目录的审查请求：即使报告提交者忘记将 *status* 团队添加为审查者，salvadore@（*status* 团队成员）也会阻止该补丁提交。同样，该规则还会阻止任何包含 *status* 团队作为审查者的审查请求，以确保至少有一名 *status* 团队成员在提交前对补丁进行了审核。
- 通过 [GitHub action](https://github.com/freebsd/freebsd-doc/blob/main/.github/workflows/label-pull-requests.yml) 自动为任何修改状态报告目录的拉取请求添加新引入的 [status report](https://github.com/freebsd/freebsd-doc/pulls?q=label%3A%22status+report%22) 标签。该 GitHub action 可由任何希望根据修改文件路径自动应用更多标签的人员轻松修改。

未来还计划引入更多自动化措施。

#### 文档重组

状态报告的 [README](https://cgit.freebsd.org/doc/diff/website/content/en/status/README?id=7cd49b34af842b2cf247c944b7d8bc3c1bef8fc8) 和 [操作指南](https://cgit.freebsd.org/doc/diff/website/content/en/status/howto/_index.adoc?id=7cd49b34af842b2cf247c944b7d8bc3c1bef8fc8) 已经更新并合并为一份独一无二的文档：即 [FreeBSD 状态报告流程](https://docs.freebsd.org/en/articles/freebsd-status-report-process/)。你可以查阅该文档，了解关于报告提交和发布的详细信息。随着 status 团队新工作流程的推进，该文档将定期更新。特别是，关于自动化的新材料即将推出。

## 用户空间

涉及基本系统及其内置程序的变更。

### 改进 daemon(8) 

**相关链接：**  
[daemon(8)](https://man.freebsd.org/cgi/man.cgi?query=daemon&sektion=8&format=html)  
[Libera IRC](https://libera.chat/)

**联系方式：**  
Ihor Antonov <[ihor@antonovs.family](mailto:ihor@antonovs.family)>  
Kyle Evans <[kevans@FreeBSD.org](mailto:kevans@FreeBSD.org)>

目前正在进行一项改进 `daemon` 工具代码质量和监控能力的工作。`daemon` 是一个可以将任何正在运行的进程转为后台运行或进行监控的工具，如果进程崩溃，它会自动重启该进程。`daemon` 在 ports 树中被广泛使用，并且可以在基本系统中得到更多应用。

本季度添加了对 `long_opts` 的支持，并对代码库进行了初步重构，为进一步的改进做好准备。目前没有功能性变化，但未来会有更多改进。如果你遇到意外的 bug，请直接联系或者在 Libera IRC 的 `#freebsd-dev` 频道中与我们联系。

下季度计划的工作事项包括：

- 对所有事件源使用 kqueue；
- 修复 [Bug #268580](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=268580)；
- 修复 [Bug #236117](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=236117)；
- 修复 [Bug #254511](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=254511)；
- 修复 [Bug #212829](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=212829)；
- 实现 `procctl PROC_REAP_ACQUIRE`。

我们欢迎各位反馈、bug 报告（不论旧的或新的）以及功能请求。



## 内核

更新内核子系统/特性、驱动支持、文件系统等内容。

### 在 13.2 中启用使用日志式软更新的文件系统快照

**联系方式：**  
Marshall Kirk McKusick <[mckusick@freebsd.org](mailto:mckusick@freebsd.org)>

在 2023 年第一季度，将 UFS/FFS 文件系统在启用日志式软更新时制作快照的能力合并到了 `releng/13.2` 分支中，并将用于在在线文件系统上进行后台转储，最终将在 FreeBSD 13.2-RELEASE 中发布。

通过向 [dump(8)](https://man.freebsd.org/cgi/man.cgi?query=dump&sektion=8&format=html) 命令传递 `-L` 标志来请求后台转储。

有关该项目的详细信息，请参阅 [2022 年第四季度报告](https://www.freebsd.org/status/report-2022-10-2022-12/#_enabling_snapshots_on_filesystems_using_journaled_soft_updates)。

**赞助商：** FreeBSD 基金会



### 改进 kinst DTrace 提供程序

**相关链接：**  
[libdtrace: implement inline function tracing](https://reviews.freebsd.org/D38825)  
[dtrace(1): add -d flag to dump D script post-dt_sugar](https://reviews.freebsd.org/D38732)

**联系方式：**  
Christos Margiolis <[christos@FreeBSD.org](mailto:christos@FreeBSD.org)>  
Mark Johnston <[markj@FreeBSD.org](mailto:markj@FreeBSD.org)>

kinst 是由 christos@ 和 markj@ 创建的一个全新的 DTrace 提供程序，它允许对内核函数中的任意指令进行跟踪。kinst 已被加入到 FreeBSD 14.0 的基本系统中。

[2022Q3 状态报告](https://www.freebsd.org/status/report-2022-07-2022-09/#_dtrace_instruction_level_dynamic_tracing) 对 kinst 做了简要介绍。我们目前正致力于内联函数跟踪的工作（请参见上文评审 [D38825](https://reviews.freebsd.org/D38825)），这是一个备受需求的 DTrace 特性，通过使用内核 DWARF 和 ELF 信息来定位每个内联副本的调用点，并利用这些信息将 D 语言语法转换，从而将 kinst 探针转换为相应形式。

```
 kinst::<inline_func>:<entry/return>
        /<pred>/
        {
                <acts>
        }
```

变为

```
 kinst::<caller_func1>:<offset>,
        kinst::<caller_func2>:<offset>,
        kinst::<caller_func3>:<offset>
        /<pred>/
        {
                <acts>
        }
```

示例：

```sh
# dtrace -dn 'kinst::cam_iosched_has_more_trim:entry { printf("t%dt%s", pid, execname); }'
        kinst::cam_iosched_get_trim:13,
        kinst::cam_iosched_next_bio:13,
        kinst::cam_iosched_schedule:40
        {
                printf("t%dt%s", pid, execname);
        }

        dtrace: description 'kinst::cam_iosched_has_more_trim:entry ' matched 3 probes
        CPU     ID                    FUNCTION:NAME
          2  79315          cam_iosched_next_bio:13     0       kernel
          2  79316          cam_iosched_schedule:40     0       kernel
          0  79316          cam_iosched_schedule:40     12      intr
          2  79315          cam_iosched_next_bio:13     0       kernel
          2  79316          cam_iosched_schedule:40     0       kernel
          0  79316          cam_iosched_schedule:40     12      intr
        ^C
```

一个新的 `-d` 标志也已添加到 [dtrace(1)](https://man.freebsd.org/cgi/man.cgi?query=dtrace&sektion=1&format=html) 中，该标志在 libdtrace 进行语法转换后会将 D 脚本转储出来。

进一步的目标包括：

* 在 D 语言中实现一个 `locals` 结构，用于存储被跟踪函数的局部变量。例如，对于 `kinst::foo:<x>`，我们可以在 D 脚本中通过 `print(locals→bar)` 来打印局部变量 `bar`。
* 将 kinst 移植到 riscv 和/或 arm64 平台。

**赞助商：** FreeBSD 基金会



### 原生 Linux timerfd

**相关链接：**  
[Differential revision](https://reviews.freebsd.org/D38459)

**联系方式：**  
Jake Freeland <[jfree@FreeBSD.org](mailto:jfree@FreeBSD.org)>

timerfd 功能是一组 Linux 标准系统调用，用于操作间隔定时器。这些定时器类似于每进程定时器，但它们由文件描述符表示，而不是与进程绑定。这些文件描述符可以传递给其他进程，在 [fork(2)](https://man.freebsd.org/cgi/man.cgi?query=fork&sektion=2&format=html) 后保留，并且可以通过 [kevent(2)](https://man.freebsd.org/cgi/man.cgi?query=kevent&sektion=2&format=html)、[poll(2)](https://man.freebsd.org/cgi/man.cgi?query=poll&sektion=2&format=html) 或 [select(2)](https://man.freebsd.org/cgi/man.cgi?query=select&sektion=2&format=html) 进行监控。

FreeBSD 中已有一个 timerfd 的实现用于 Linux 兼容性，但 [此差异修订](https://reviews.freebsd.org/D38459)使该接口变为原生接口。此更改的目标是简化那些包含 timerfd 的程序在 FreeBSD 上的移植过程。

该具体实现避免向系统调用表中添加新名称。相反，`timerfd_create()` 被封装在 `specialfd()` 系统调用中，而 `timerfd_gettime()` 和 `timerfd_settime()` 调用则通过 `ioctl()` 进行封装。

希望在 FreeBSD 上获得支持的开发者应尽量避免使用 timerfd。建立任意定时器时，推荐使用 `kqueue()` 的 `EVFILT_TIMER` 过滤器。



## 架构

更新特定平台的功能并为新硬件平台提供支持。

### AArch64 上的内核地址消毒器

**联系方式：**  
Kyle Evans <[kevans@FreeBSD.org](mailto:kevans@FreeBSD.org)>

消毒器（Sanitizers）是一类错误检测工具，它们利用编译器（在此案例中为 LLVM）插入的检测代码和运行时状态跟踪相结合的方法，来检测 C 代码中的错误。这些工具可以自动检测许多 C 语言编程错误，例如使用已释放内存和未初始化变量的情况，这些错误往往需要大量工作才能发现。它们在与回归测试套件或模糊测试工具（如 [syzkaller](https://github.com/google/syzkaller)）结合时效果尤为显著。与 Valgrind 等工具不同，启用特定消毒器需要对软件重新编译，但消毒器可以在内核中使用。启用了消毒器的内核在运行时会带来显著的性能开销，无论是在 CPU 利用率还是内存使用上。

自 [89c52f9d59fa](https://cgit.freebsd.org/src/commit/?id=89c52f9d59fa) 起，此前仅限于 amd64 的内核地址消毒器现已被移植到 arm64 平台。

此前在多种机器上已进行了测试，包括：

* 各种 Ampere Altra 机器
* QEMU 虚拟机
* Microsoft 的 "Volterra" 开发板
* bhyve（正在进行中）。

我们欢迎并感激在其他硬件上的进一步测试。

**赞助商：** Juniper Networks, Inc.  

**赞助商：** Klara, Inc.

### bsd-user：上游合并与状态报告

**相关链接：**  
[QEMU Project](https://qemu.org/)  
[FreeBSD bsd-user qemu 分支](https://github.com/qemu-bsd-user/qemu-bsd-user)  
[QEMU Project 的 GitLab 镜像](https://gitlab.com/qemu-project/qemu)

**联系方式：**  
Warner Losh <[imp@FreeBSD.org](mailto:imp@FreeBSD.org)>

本季度，Warner 向 qemu-project 仓库上游提交了两个补丁集（第三个补丁集正在待定中）。Doug Rabson 提交了一些优化，使内核能够保存对 qemu-user 模拟器的句柄以便在未来执行时使用。我们还与一些有意在 NetBSD 上让 bsd-user 运行的人取得了联系。Google Summer of Code 项目对上游合并工作表现出了一些兴趣。

#### 上游合并工作

本季度，sysctl 系统调用已上游合并。Doug 的更改也已上游（见下文）。围绕 NetBSD 与 OpenBSD 以及动态生成系统调用的部分代码清理工作尚在待定中。

#### Doug Rabson 的更改

作为其容器工作的一部分，Doug 提交了允许内核缓存运行程序所用模拟器的更改。这使得内核可以直接使用缓存的模拟器来执行新二进制文件，从而简化了 bsd-user 的工作，并消除了其与 linux-user 之间的一个差异来源。Doug 还提供了一个重要的修复，解决了 aarch64 无法运行的问题。

#### Bug 修复与改进

除了 Doug 的修复外，Warner 本季度也对代码做了一些清理工作：

* Warner 移除了模拟器中最后剩余的“在任何 BSD 上运行”代码。
* 尽管基本的系统调用可以在所有 BSD 之间进行模拟，但它们的系统调用接口已经分歧太大，并且功能过于丰富，短期内难以实现通用化。
* Warner 原计划直接移除 NetBSD 和 OpenBSD 的部分，但至少 NetBSD 那边对使代码能编译起来表现出了一定兴趣。
* 现在 NetBSD 那边已有了联系方式并明确了方向，Warner 希望他们能提交 pull request 以便在 NetBSD 上构建 bsd-user。
* Warner 增加了 SIGSYS 支持，这样可以更早捕获未实现的系统调用，并改进其报告机制以收集更多失败信息。
* Warner 对 `blitz` 分支中的部分代码进行了清理。
* 我们已经在 `blitz` 分支中上游合并到了 8.0rc1 版本，以保持最新状态。

#### 编程之夏项目

对 bsd-user 上游合并任务有很大兴趣，Warner 已将此任务添加到 QEMU 项目列表中。希望能资助一名学生来完成将所有运行简单程序所需的系统调用上游合并的工作。运气好的话，我们将能够运行任何与 clang 做相同工作（其中一个目标是能够编译 hello world 程序）的程序。未来的季度报告将提供更多细节，前提是我们有幸获得该项目的资助名额。

#### 需要的帮助

我们始终欢迎对 bsd-user 项目的帮助：

* 欢迎针对新增系统调用的 pull request。
* 对于许多我们手工完成的工作（如系统调用参数跟踪）的自动化将大有裨益。
* 热心的志愿者如果愿意协助我进行上游合并工作也非常欢迎（许多任务都很简单且耗时不多，适合不想长期承诺的人）。
* 与 NetBSD 那边的人员进行协调，以及清理他们提出的问题。
* 需要修复一些 bug（特别是线程相关的 bug）。

## Cloud

更新云平台相关特性并支持新的云平台。

### FreeBSD 作为 Tier 1 cloud-init 平台

**相关链接：**  
[cloud-init 网站](https://cloud-init.io/)  
[cloud-init 文档](https://cloudinit.readthedocs.io/en/latest/)  
[cloud-init 正在进行的重构](https://github.com/canonical/cloud-init/blob/main/WIP-ONGOING-REFACTORIZATION.rst)

**联系方式：**  
Mina Galić <[freebsd@igalic.co](mailto:freebsd@igalic.co)>

cloud-init 是在云中配置服务器的标准方式。不幸的是，除 Linux 外的操作系统对 cloud-init 的支持较差，而 FreeBSD 上缺乏 cloud-init 支持也阻碍了希望将 FreeBSD 作为一级平台提供服务的云服务提供商。为了解决这一问题，本项目旨在使 FreeBSD 的 cloud-init 支持与 Linux 保持一致，更广泛的计划是使所有 BSD 系统均能获得该支持。

由于个人原因以及缺乏合适资源，本季度项目进展非常缓慢。我一直在尝试 [移植 Infiniband 功能](https://github.com/canonical/cloud-init/pull/2003)。这证明颠覆了我的一个假设，即 [ifconfig(8)](https://man.freebsd.org/cgi/man.cgi?query=ifconfig&sektion=8&format=html) 就足以确定 FreeBSD 上的网络接口。

在等待资源期间，我调试并修复了一个启动 panic 问题：[499171a98c88](https://cgit.freebsd.org/src/commit/?id=499171a98c8813e4dc6e085461d5c47750efa555)。这使得在 LXD（cloud-init 的 CI 平台）上启动 FreeBSD 成为可能。我们仍需要解决 [高 CPU 占用问题](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=269823)，但已有一个被接受的评审：[D38898](https://reviews.freebsd.org/D38898)。

一位在 Azure 工作的 cloud-init 同事设法让我获得了 Azure 上 [HPC 虚拟机](https://learn.microsoft.com/en-us/azure/architecture/topics/high-performance-computing) 的访问权限。不幸的是，这个权限仅限于短时间内使用，并不足以弄清 FreeBSD 上如何启动 Infiniband —— 这项任务在 Linux 上由 [Azure Agent](https://github.com/Azure/WALinuxAgent/) 负责，而 FreeBSD 的 [sysutils/azure-agent](https://cgit.freebsd.org/ports/tree/sysutils/azure-agent/) 则明显不足。

有兴趣参与该项目的人可以提供他们 Infiniband 系统的 [ifconfig(8)](https://man.freebsd.org/cgi/man.cgi?query=ifconfig&sektion=8&format=html)、[ibstat(8)](https://man.freebsd.org/cgi/man.cgi?query=ibstat&sektion=8&format=html)、[ibv_devinfo(1)](https://man.freebsd.org/cgi/man.cgi?query=ibv_devinfo&sektion=1&format=html) 等命令的输出粘贴内容（例如，查看 [这里的粘贴](https://lists.freebsd.org/archives/freebsd-infiniband/2023-February/000005.html)）。如果能获得带 Infiniband 网卡的硬件，或听到有使用 FreeBSD 在 Azure HPC 上成功运行 Infiniband 的人，也将让我非常高兴。

如果对此平台有兴趣，我将投入更多精力修复 Azure Agent。

**赞助商：** FreeBSD 基金会

### FreeBSD 上的 OpenStack

**相关链接：**  
[OpenStack](https://www.openstack.org/)  
[OpenStack on FreeBSD](https://github.com/openstack-on-freebsd)

**联系方式：**  
Chih-Hsin Chang <[starbops@hey.com](mailto:starbops@hey.com)>  
Li-Wen Hsu <[lwhsu@FreeBSD.org](mailto:lwhsu@FreeBSD.org)>

本项目旨在移植关键的 OpenStack 组件，使 FreeBSD 能够作为 OpenStack 主机运行。

在 2023 Q1 中，大新闻是我们已经能够在 OpenStack 平台上通过 [bhyve(8)](https://man.freebsd.org/cgi/man.cgi?query=bhyve&sektion=8&format=html) 启动 FreeBSD 实例。但对于启动的实例，其功能仍存在一些主要限制，需要解决：

* 无自助服务网络（仅支持扁平网络）
* 实例内无网络连通性
* 仅支持 FreeBSD 原始镜像（已测试 `FreeBSD-13.1-RELEASE-amd64.raw`）
* 无磁盘大小调整功能
* 无控制台集成（需要手动使用 [cu(1)](https://man.freebsd.org/cgi/man.cgi?query=cu&sektion=1&format=html) 命令）

构建 POC 站点的详细步骤文档可以在 [`docs` 仓库](https://github.com/openstack-on-freebsd/docs) 中找到。各个 OpenStack 组件的打补丁版本均在同一 GitHub 组织下管理。

此外，我们于 3 月底参加了 AsiaBSDCon 2023，并在开发者峰会上就当前项目状态做了简短汇报。活动中获得了宝贵反馈，下一季度我们将重点关注以下问题：

* 解决 Open vSwitch 网络问题
* 将各个 OpenStack 组件转换为 FreeBSD  Port

有兴趣参与该项目的人可以首先按照安装指南检查文档。以下是项目的一项开放任务：

* 针对 oslo.privsep 库的 FreeBSD 特定实现

我们始终欢迎反馈和帮助。

**赞助商：** FreeBSD 基金会


## 文档

关于文档树、手册页或新外部书籍/文档的重要变更。

### 文档工程团队

**相关链接：**  
[FreeBSD 文档项目](https://www.freebsd.org/docproj/)  
[FreeBSD 文档项目 —— 新贡献者入门指南](https://docs.freebsd.org/en/books/fdp-primer/)  
[文档工程团队](https://www.freebsd.org/administration/#t-doceng)

**联系方式：**  
FreeBSD Doceng Team <[doceng@FreeBSD.org](mailto:doceng@FreeBSD.org)>

doceng@ 团队负责处理与 FreeBSD 文档项目相关的一些元项目问题；更多信息请参见 [FreeBSD Doceng 团队章程](https://www.freebsd.org/internal/doceng/).

在上个季度期间：

- 接受了 Pau Amma 的文档提交权限（doc commit bit）。
- 提出了 Lorenzo Salvadore 成为文档提交者的提议，carlavilla@ 和 dbaio@ 将对他进行指导。
- Ryusuke SUZUKI 从 doceng 团队辞任。doceng 团队感谢 ryusuke@ 为团队所做的贡献。

待定及讨论中的事项：

- 已经向文档集中添加了一份 [关于许可的新文档](https://cgit.freebsd.org/doc/commit/?id=4c50528a8678246a6d01765acac8c395434b8c7e).

#### 《Porter 手册》

手册中新增了三个 `Uses` 开关：

- [新增 Uses = ruby](https://cgit.freebsd.org/doc/commit/?id=407dbb9254e7b6b379b8257f34f7732ed1afc71f).
- [新增 Uses = ldap](https://cgit.freebsd.org/doc/commit/?id=afa1a31005978bac63874fff8a1833f69a81dae3).
- [新增 Uses = budgie](https://cgit.freebsd.org/doc/commit/?id=689f1b026a02bf6d7039bdfec59353196d83ccef).

此外：

- [已修正 NVIDIA 安装与配置选项](https://cgit.freebsd.org/doc/commit/?id=9af61238fc24d4772b3c9e5fbd63fcaee2526699).
- [已改进高级网络章节](https://cgit.freebsd.org/doc/commit/?id=3c6d3dea4a3ee60e7f0033afc9c5bf74e9ae1d31).

#### FreeBSD 在 Weblate 上的翻译工作

**相关链接：**  
[在 Weblate 上翻译 FreeBSD](https://wiki.freebsd.org/Doc/Translation/Weblate)  
[FreeBSD Weblate 实例](https://translate-dev.freebsd.org/)

##### 2022 年 Q4 状态

- 12 种语言
- 150 位注册用户

##### 语言进展

- 中文（简体） (zh-cn) —— 进度：14%
- 中文（繁体） (zh-tw) —— 进度：11%
- 荷兰语 (nl) —— 进度：1%
- 法语 (fr) —— 进度：1%
- 德语 (de) —— 进度：1%
- 印度尼西亚语 (id) —— 进度：1%
- 意大利语 (it) —— 进度：10%
- 韩语 (ko) —— 进度：11%
- 挪威语 (nb-no) —— 进度：1%
- 波斯语 (fa-ir) —— 进度：6%
- 葡萄牙语 (pt-br) —— 进度：29%
- 僧伽罗语 (si) —— 进度：1%
- 西班牙语 (es) —— 进度：37%
- 土耳其语 (tr) —— 进度：5%

我们感谢所有参与文档翻译或审核工作的人员。

同时，请在你所在的本地用户组中宣传这一工作，我们始终需要更多志愿者。

#### FreeBSD 手册工作组

**联系方式：**  
Sergio Carlavilla <[carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)>

手册第 1 至第 6 章已完成更新，第 7 章正在进行中。

#### FreeBSD 网站改版 —— WebApps 工作组

**联系方式：**  
Sergio Carlavilla <[carlavilla@FreeBSD.org](mailto:carlavilla@FreeBSD.org)>

该工作组负责创建新的 FreeBSD 文档门户，并重新设计 FreeBSD 主网站及其组件。FreeBSD 开发者可以在 FreeBSD Slack 频道中的 #wg-www21 跟进并加入该工作组。该工作将分为四个阶段：

1. 文档门户的重新设计  
   创建一个全新的、响应式且具备全局搜索功能的设计。（*已完成*）
2. 在线手册页的重新设计  
   使用 mandoc 生成 HTML 页面的脚本。（*已完成*）公开实例地址：[https://man-dev.FreeBSD.org](https://man-dev.freebsd.org/)
3. 在线 Ports 页面重新设计  
   利用 Ports 脚本创建一个应用程序门户。（*进行中*）
4. FreeBSD 主网站重新设计  
   新的网站设计，响应式且带有深色主题。（*进行中*）

### FreeBSD 俄语文档项目

**相关链接：**  
[FAQ](https://docs.freebsd.org/ru/books/faq/)  
[网站](https://www.freebsd.org/ru/)

**联系方式：**  
Andrey Zakhvatov <[andrey.zakhvatov@gmail.com](mailto:andrey.zakhvatov@gmail.com)>

FreeBSD 俄语文档项目目前的目标是提供 FreeBSD 文档中最重要部分（FAQ、Handbook、网站）的最新俄语翻译。为讲俄语的人士提供高质量的官方技术资料，并提升该操作系统在全球的接受度至关重要。我们希望这一活动能在讲俄语的 FreeBSD 社区内获得支持，并促使翻译材料数量的增加。

FAQ 的翻译已更新并与最新原版同步。网站页面的更新也有了非常细微的进展。

如果你愿意参与，请查阅[官方翻译指南](https://docs.freebsd.org/en/books/fdp-primer/translations/)。我们非常需要你在以下方面提供翻译帮助：

- 网站页面（较简单）
- 手册的章节（目前仅有 X11 章节正在进行中）
- 文章



## Ports

涉及 Ports 的变更，无论是涉及整个 Ports 的大范围改动，还是单个 Port 的调整。

### Freshports: SQL 注入攻击与求助

**相关链接：**  
[FreshPorts](https://freshports.org/)  
[FreshPorts 博客](https://news.freshports.org/)

**联系方式：**  
Dan Langille <[dvl@FreeBSD.org](mailto:dvl@FreeBSD.org)>

FreshPorts 和 FreshSource 已对 FreeBSD 的提交进行了长达 20 年的跟踪报道。它们覆盖所有提交，不仅仅是 Port 相关的。

FreshPorts 跟踪提交情况，并从各个 Port 的 Makefile 中提取数据，以创建一个对 Ports 维护者和使用者都非常有用的信息数据库。

例如，[https://www.freshports.org/security/acme.sh/](https://www.freshports.org/security/acme.sh/) 展示了  Port [security/acme.sh](https://cgit.freebsd.org/ports/tree/security/acme.sh/) 的历史记录，可以追溯到该  Port 于 2017 年 5 月创建时。同时，还提供了依赖关系、风味、配置选项和可用软件包等信息。这一切对 Ports 的用户和开发者都非常有用。

#### SQL 注入攻击

三月份时，发现了一起 SQL 注入攻击，并对网站进行了修补。我们通过 Twitter 账号、状态页面以及网站每一页顶部发布了通知。攻击的直接入口已被关闭，并很快完成了修补。随后，在网站的各个部分增加了额外的预防性补丁。所有已知的问题均已修复。用户已收到通知，并被建议更改密码。

详细信息请见：

- [SQL 注入问题已修复](https://news.freshports.org/2023/03/24/sql-inejection-issues-fixed/)
- [FreshSource 代码修复](https://news.freshports.org/2023/03/24/freshsource-code-fixes/)

#### 求助

FreshPorts 已运行超过 22 年，将来必须由其他人接手。我希望现在就开始这个交接过程。FreshPorts 涉及多个方面：

- FreeBSD 管理（更新操作系统和软件包）
- 前端代码（网站 —— 主要是 PHP 编写）
- 后端代码（提交处理 —— 使用 Perl、Python、Shell 编写）
- 数据库设计（PostgreSQL）

与应用程序和操作系统相比，数据库变化不大且维护工作较少。网站基本上可以自动运行。偶尔，FreeBSD Ports 基础设施的某些变动会导致部分功能出现问题或需要修改，但通常不紧急。这并不会占用太多时间，并且其中包含了大量的学习机会。虽然 FreshPorts 不是一个复杂的应用，但它也绝非易事。

### DRM 驱动（即 GPU 驱动）

**相关链接：**  
[GitHub 代码仓库](https://github.com/freebsd/drm-kmod)

**联系方式：**  
Emmanuel Vadot <[manu@FreeBSD.org](mailto:manu@FreeBSD.org)>  
Jean-Sébastien Pédron <[dumbbell@FreeBSD.org](mailto:dumbbell@FreeBSD.org)>  
Graphics 团队 <[freebsd-x11@FreeBSD.org](mailto:freebsd-x11@FreeBSD.org)>

GPU 由 DRM 驱动管理。这些驱动是专为 Linux 开发的，并采用宽松的许可协议。我们的目标是将这些驱动移植到 FreeBSD，以确保现代 GPU 能够获得完整支持。

由于我们很长时间未发布报告来分享进展，因此本次状态报告涵盖的内容不仅限于最近一个季度。



#### 更新至 Linux 5.15 LTS 和 Linux 5.16

截至本次报告，[graphics/drm-kmod](https://cgit.freebsd.org/ports/tree/graphics/drm-kmod/) 元 Port 仍然在 FreeBSD 13.1 及更高版本上安装来自 Linux 5.10（发布于 2020 年 12 月 13 日）的 DRM 驱动。该版本的驱动缺乏对新款 GPU 的支持，尤其是不支持 Intel 第 12 代 Alder Lake GPU。过去几个月，我们一直在努力更新 DRM 驱动，以支持更新的 AMD 和 Intel GPU。

`drm-kmod` Git 仓库的 `master` 分支首先更新到了 Linux 5.15（发布于 2021 年 10 月 31 日）。Linux 5.15 是一个长期支持（LTS）版本，因此我们希望利用这一点。从这一点开始，我们采取了两条并行路径：

- 创建了 `5.15-lts` 分支，以回溯合并 Linux 5.15.x 的所有补丁修复。该工作现已在  Port `drm-515-kmod` 中提供。  
- 继续推进后续 Linux 版本的移植工作。目前 `master` 分支已更新至 Linux 5.16（发布于 2022 年 1 月 9 日）。

Linux 5.15 LTS 版本的 Intel 驱动支持 12 代 GPU（Alder Lake）。它在 FreeBSD 上基本可用，但目前仅经过了初步测试，因此 [graphics/drm-kmod](https://cgit.freebsd.org/ports/tree/graphics/drm-kmod/) 仍然安装的是 [graphics/drm-510-kmod](https://cgit.freebsd.org/ports/tree/graphics/drm-510-kmod/)，而非 [graphics/drm-515-kmod](https://cgit.freebsd.org/ports/tree/graphics/drm-515-kmod/)。最终，FreeBSD 应该能够在这一代 Intel GPU 及多款新 AMD GPU 上正常运行，但在实际测试和使用过程中仍可能出现问题。

在此过程中，我们已将固件更新至 [linux-firmware](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git) 20230210 版本。



#### Linux 5.17 及后续工作

我们已经移植了 Linux 5.17（发布于 2022 年 3 月 20 日）的 DRM 驱动，但[该工作仍位于独立的分支](https://github.com/freebsd/drm-kmod/pull/236)。

目前有几个问题阻碍了进一步测试和合并到 `master` 分支：

- FreeBSD 当前与 [vt(4)](https://man.freebsd.org/cgi/man.cgi?query=vt&sektion=4&format=html)（控制台/终端驱动）的集成方式，与 DRM 驱动基于 Linux fbdev KPI（内核编程接口）的预期相差较远。Intel 和 AMD 驱动的某些改动导致 [vt(4)](https://man.freebsd.org/cgi/man.cgi?query=vt&sektion=4&format=html) 在 5.17 版本更新后无法正常工作。  
- Linux 5.17 的初始发布版本未包含对 12 代 Intel GPU 的修复，而这些修复已被回溯至 Linux 5.15 LTS 版本。因此，该版本在 Intel 12 代 GPU 上表现得相当不稳定。

为了解决 [vt(4)](https://man.freebsd.org/cgi/man.cgi?query=vt&sektion=4&format=html) 集成层的问题，我们已经开始[开发一个新的 vt 后端，以使用 DRM 驱动暴露的 fbdev 回调](https://github.com/freebsd/drm-kmod/pull/243)。该后端将随 DRM 驱动一起提供，而不是作为 FreeBSD 内核的一部分，以便在驱动演进时更容易维护。目前该工作仍在进行中，其中的锁管理尤其复杂。

针对 Linux 5.17 版本对 Intel 12 代 GPU 的支持问题，我们可能不会回溯 Linux 5.17.x 版本的补丁，而是将重点放在 Linux 5.18（发布于 2022 年 5 月 22 日）及更高版本的移植工作上。

### FreeBSD 上的 KDE

**相关链接：**  
[KDE FreeBSD](https://freebsd.kde.org/)  
[KDE Community FreeBSD](https://community.kde.org/FreeBSD)  

**联系方式：**  
Adriaan de Groot <[kde@FreeBSD.org](mailto:kde@FreeBSD.org)>  

FreeBSD 上的 KDE 项目负责在 FreeBSD Ports 中打包 CMake、Qt 以及来自 KDE 社区的软件。这些软件包括完整的 KDE Plasma 桌面环境（支持 X11 和 Wayland），以及数百款可在任何 FreeBSD 机器上运行的应用程序。  

KDE 团队（kde@）是 desktop@ 和 x11@ 组的一部分，负责构建软件栈，使 FreeBSD 成为一个美观、可用的日常桌面系统。以下内容主要涉及 KDE 相关 Port，同时也包含对整个桌面环境至关重要的内容。  



#### 基础设施  

- Qt5  Port 已更新至 KDE 补丁集合 5.15.8。  
- Qt6  Port（KDE 目前尚未使用，但许多 Port 支持 Qt6 并提供 Qt6 版本）已更新至 6.4.2，并新增了 Qt6 WebEngine 的 Python 绑定。  
- CMake  Port 已更新至 3.25.1，并修复了 FreeBSD 软件包的 CPack 生成器。  
- [graphics/poppler](https://cgit.freebsd.org/ports/tree/graphics/poppler/)（许多 PDF 查看器依赖的库）已更新至 23.01。  
- [sysutils/bsdisks](https://cgit.freebsd.org/ports/tree/sysutils/bsdisks/)（用于模拟 Linux udisks 的 shim，适用于大多数桌面环境）已更新至 0.29。  



#### KDE 软件栈  

KDE Gear 每季度发布一次，KDE Plasma 每月更新一次，KDE Frameworks 也每月发布新版本。这些较大规模的更新会在上游发布后不久合入 Ports ，因此不单独列出。  

- KDE Frameworks 更新至 5.104。  
- KDE Gear 更新至 22.12.3。  
- KDE Plasma 桌面已更新至 5.27。本次更新因底层支持栈存在未解决问题，以及早期 KDE Plasma 版本的一个补丁错误放置，导致延迟。感谢 arrowd@ 和 Serenity Cybersecurity, LLC 解决了相关问题。  
- 新增  Port [devel/ktextaddons](https://cgit.freebsd.org/ports/tree/devel/ktextaddons/) 。该软件是 KDE PIM 套件的一部分，未来可能成为新的 KDE Framework 组件。  



#### 相关 Port  

- [audio/amarok](https://cgit.freebsd.org/ports/tree/audio/amarok/)（2000 年代初最受欢迎的 KDE 音频播放器之一）已在 Ports 中标记为“已废弃”，因其上游已停止维护。  
- [astro/kstars](https://cgit.freebsd.org/ports/tree/astro/kstars/)（交互式天文馆软件）已更新至 3.6.3。  
- [devel/gitqlient](https://cgit.freebsd.org/ports/tree/devel/gitqlient/)（Git 图形界面客户端）已更新至 1.6.1，增加对新 Git 命令的支持。  
- [devel/okteta](https://cgit.freebsd.org/ports/tree/devel/okteta/)（十六进制查看器和二进制编辑器）已更新至 0.26.10。  
- [devel/qcoro](https://cgit.freebsd.org/ports/tree/devel/qcoro/)（支持 Qt 的 C++ 协程库）已更新至 0.8.0。  
- [graphics/krita](https://cgit.freebsd.org/ports/tree/graphics/krita/)（绘画与图形创作软件）已更新至 5.1.5。  
- [graphics/quickqanava](https://cgit.freebsd.org/ports/tree/graphics/quickqanava/)（图形可视化库）已正式发布，并在 Ports 中进行了更新。  
- [irc/kvirc](https://cgit.freebsd.org/ports/tree/irc/kvirc/)（IRC 客户端）已更新至最新提交版本，虽然没有正式发布，但包含了一些错误修复。  
- [multimedia/haruna](https://cgit.freebsd.org/ports/tree/multimedia/haruna/)（视频和音频播放器）已更新至 0.10.3。  
- [net-im/neochat](https://cgit.freebsd.org/ports/tree/net-im/neochat/)（Matrix 聊天客户端之一）已更新，以匹配 [net-im/libquotient](https://cgit.freebsd.org/ports/tree/net-im/libquotient/) 的新版本。然而，由于与 FreeBSD 旧版本的兼容性问题仍在持续，KDE-FreeBSD 团队已宣布 FreeBSD 12 版本“事实上不再受支持”。  
- [net-im/ruqola](https://cgit.freebsd.org/ports/tree/net-im/ruqola/)（Rocket Chat 客户端）已更新至 1.9.1。  
- [security/keysmith](https://cgit.freebsd.org/ports/tree/security/keysmith/)（二步验证支持软件）已更新至 23.01.0。  



### FSX  

**相关链接：**  
[GitHub](https://github.com/asomers/fsx-rs)  
[FreshPorts](https://www.freshports.org/devel/fsx/)  

**联系方式：**  
Alan Somers <[asomers@freebsd.org](mailto:asomers@freebsd.org)>  

FSX（File System eXerciser）工具最早由 Apple 在 1990 年代编写，并自 FreeBSD 5.0 起成为 FreeBSD 代码库的一部分。该工具通过随机生成的操作流对文件系统进行压力测试，并在每次读取后验证文件数据。然而，该工具从未作为操作系统的一部分安装，仅存在于源代码树中，这使得它在 CI 流水线中难以使用。此外，该工具还存在其他限制。  

因此，本季度我用 Rust 重新编写了该工具。新版本在相同的种子值下，与原始工具的行为保持字节级兼容。但未来版本可能会打破向后兼容性，以添加 `fspacectl` 和 `copy_file_range` 等新功能。目前，新版本已进入 Ports ，后续我将移除原始版本。

### FreeBSD 上的 GCC

**链接：**  
[GCC 项目](https://gcc.gnu.org/)：[https://gcc.gnu.org](https://gcc.gnu.org/)  
[GCC 11 版本系列](https://gcc.gnu.org/gcc-11/)：[https://gcc.gnu.org/gcc-11/](https://gcc.gnu.org/gcc-11/)  
[GCC 12 版本系列](https://gcc.gnu.org/gcc-12/)：[https://gcc.gnu.org/gcc-12/](https://gcc.gnu.org/gcc-12/)  

**联系方式：**  
Lorenzo Salvadore <[salvadore@FreeBSD.org](mailto:salvadore@FreeBSD.org)>  
Gerald Pfeifer <[gerald@pfeifer.com](mailto:gerald@pfeifer.com)>  

本季度的主要更新是清理 ports 树中的旧版 GCC，以便更高效地处理 bug。

#### 旧版 GCC ports 的弃用

ports 树仍包含多个与旧版和不受支持的 GCC 相关的 ports。它们通常只是少数旧 ports 的依赖项，而这些旧 ports 最好更新至受支持的 GCC 版本，或者直接被弃用。为此，已创建[错误报告](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=269644)来跟踪问题，并已开始着手解决。感谢所有参与 ports 维护的贡献者！

#### `USE_GCC=X+` 的弃用

Gerald 维护 GCC ports 多年，虽然最近不再是主要维护者，但仍在 FreeBSD 上贡献 GCC 维护工作，简化 ports 树中的 GCC 相关基础架构，例如移除对旧版 GCC 的特殊处理。

本季度，他最重要的改动可能是[移除了 `USE_GCC=X+`](https://cgit.freebsd.org/ports/commit/?id=9b5f5ab8482f105311d01a32260ef32bba4a2628) 的支持。现在，任何依赖 GCC 的 port 必须：

- 如果 `GCC_DEFAULT` 适用，则设置 `USE_GCC=yes`；  
- 如果 `GCC_DEFAULT` 不适用，则需要指定特定版本，例如 `USE_GCC=11`；  
- 不再允许使用 `USE_GCC=11+` 这样的最低版本要求。



### Valgrind：为 3.21 版本做准备

**链接：**  
[Valgrind 官网](https://www.valgrind.org/)：[https://www.valgrind.org/](https://www.valgrind.org/)  
[Valgrind 更新日志](https://www.valgrind.org/docs/manual/dist.news.html)：[https://www.valgrind.org/docs/manual/dist.news.html](https://www.valgrind.org/docs/manual/dist.news.html)  

**联系方式：**  
Paul Floyd <[pjfloyd@wanadoo.fr](mailto:pjfloyd@wanadoo.fr)>  

[devel/valgrind-devel](https://cgit.freebsd.org/ports/tree/devel/valgrind-devel/) port 已于 2023-02-20 进行了一次中间更新，其中包含即将发布的 Valgrind 3.21 的大部分内容。正式版本将在本季度报告发布后不久发布。

本次更新带来了一些改进，例如：

- `vgdb` 界面得到了优化，现在更容易查看哪些内存已初始化，哪些尚未初始化。  
- `Helgrind` 线程检查功能修复了一些问题。  

针对 FreeBSD 进行了以下改动：

- 在 `amd64` 架构上，地址空间限制从 32GB 提高到 128GB，使其与 Linux 和 Solaris 保持一致。  
- 修复了 `kern.proc.pathname.PID` [sysctl(3)](https://man.freebsd.org/cgi/man.cgi?query=sysctl&sektion=3&format=html)，现在它正确返回 guest 进程的路径，而不是 Valgrind 自身的路径。  
- 修复了 `_umtx_op` 相关的误报，并调整了 `auxv AT_EXECPATH` 的处理方式，使其行为类似于 `kern.proc.pathname.PID`。  
- 添加了 [sctp_generic_sendmsg(2)](https://man.freebsd.org/cgi/man.cgi?query=sctp_generic_sendmsg&sektion=2&format=html) 和 [sctp_generic_recvmsg(2)](https://man.freebsd.org/cgi/man.cgi?query=sctp_generic_recvmsg&sektion=2&format=html) 的系统调用封装。

此外，虽然当前 ports 版本的 Valgrind 尚未包含，但后续将提供以下改进：

- 之前，Valgrind 不支持 [rfork(2)](https://man.freebsd.org/cgi/man.cgi?query=rfork&sektion=2&format=html)，导致程序直接崩溃。现在，它会更优雅地失败，并返回 `EINVAL` 或 `ENOSYS`。  
- `posix_spawn(3)` 将在 `rfork(2)` 失败时回退到 `vfork(2)`。  
- 修复了 `mknodat(2)` 在 `i386` 架构上的错误实现。  
- 重新设计了所有对齐分配函数，使其行为更接近 Valgrind 构建平台，而非 Linux glibc。

## 第三方项目

许多项目基于 FreeBSD 构建，或将 FreeBSD 组件集成到其项目中。由于这些项目可能会引起 FreeBSD 社区的兴趣，我们有时会在季度报告中简要介绍这些项目的最新进展。这些信息均由相关项目提交，FreeBSD 项目不对其准确性或真实性作出任何保证。

### PkgBase.live

**链接：**  
[网站（存档）](https://web.archive.org/web/20221220222828/https://alpha.pkgbase.live/)：[https://web.archive.org/web/20221220222828/https://alpha.pkgbase.live/](https://web.archive.org/web/20221220222828/https://alpha.pkgbase.live/)  
[网站源码](https://codeberg.org/pkgbase/website)：[https://codeberg.org/pkgbase/website](https://codeberg.org/pkgbase/website)  

**联系方式：**  
Mina Galić <[freebsd@igalic.co](mailto:freebsd@igalic.co)>  

PkgBase.live *曾经* 是 FreeBSD [PkgBase 项目](https://wiki.freebsd.org/PkgBase)的一个非官方仓库。它的灵感来源于 [https://up.bsd.lv/](https://up.bsd.lv/)，后者为 FreeBSD STABLE 和 CURRENT 分支提供 [freebsd-update(8)](https://man.freebsd.org/cgi/man.cgi?query=freebsd-update&sektion=8&format=html) 服务。

PkgBase 的硬件由 FreeBSD 社区的一位成员赞助。然而，随着时间推移，该硬件不得不退役，我提前三个月得到了通知。而在这段时间里，我刚刚搬到另一个国家，生活动荡，因此未能找到替代方案。

目前，PkgBase.live 已停止运行。

不过，[网站](https://codeberg.org/pkgbase/website) 仍然可以访问，其中的 ["How Did She Do it?!"](https://codeberg.org/pkgbase/website/src/branch/main/howto/howdo.md) 依然可用。我鼓励其他人复制这个项目。

如果有人愿意提供新的硬件赞助，我将非常感激！

另外，我已经联系了 FreeBSD 项目，他们正在将 PkgBase 整合到 Release Engineering 中。然而，他们目前尚未准备就绪，并且无法“直接”接管 PkgBase.live，因为它使用的是完全不同的流程。



### 容器与 FreeBSD：Pot、Potluck 和 Potman

**链接：**  
[Pot 组织（GitHub）](https://github.com/bsdpot)：[https://github.com/bsdpot](https://github.com/bsdpot)  

**联系方式：**  
Luca Pizzamiglio（Pot）<[pizzamig@freebsd.org](mailto:pizzamig@freebsd.org)>  
Bretton Vine（Potluck）<[bv@honeyguide.eu](mailto:bv@honeyguide.eu)>  
Michael Gmelin（Potman）<[grembo@freebsd.org](mailto:grembo@freebsd.org)>  

[Pot](https://github.com/bsdpot/pot) 是一个 Jail 管理工具，同时[支持通过 Nomad 进行编排](https://www.freebsd.org/news/status/report-2020-01-2020-03/#pot-and-the-nomad-pot-driver)。

在上个季度，[Pot](https://github.com/bsdpot/pot/commits/master) 进行了一些小修复，但尚未发布新版本。

Potluck 的目标是在 FreeBSD 和 Pot 生态系统中扮演类似于 Linux 上 DockerHub 的角色：提供 pot 镜像和完整的容器镜像，以便与 Pot 及 Nomad 结合使用。

所有 Potluck 镜像已重新构建，以包含最新的 FreeBSD 安全公告。此外，还新增了 [Smokeping 网络延迟监控镜像](https://github.com/bsdpot/potluck/tree/master/smokeping)。另外，[Jitsi](https://github.com/bsdpot/potluck/tree/master/jitsi-meet) 镜像也进行了大量改进，但仍存在一些可靠性问题。

此外，最近发布了两篇新的博客文章，展示了如何轻松使用 Potluck 镜像：

- [如何使用 Minio 作为对象存储，结合 Prometheus 监控，部署 Nextcloud](https://honeyguide.eu/posts/minio-beast-nextcloud/)  
- [如何使用 OpenLDAP 进行访问管理，搭建自己的 Matrix Synapse 服务器](https://honeyguide.eu/posts/openldap-matrix-blog-post/)  

一如既往，我们欢迎反馈和补丁贡献！
