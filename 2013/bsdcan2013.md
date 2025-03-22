# 2013 BSDCan 开发者峰会特别篇

- 原文链接：<https://www.freebsd.org/status/report-2013-05-devsummit.html>

这份特别的状态报告包含了 BSDCan 2013 DevSummit 各个工作组讨论的总结。FreeBSD 项目在多个事件中组织 DevSummit，通常是在主要的 BSD 大会上，以便开发者能够面对面地会面并讨论相关事项。

## [超越 Buildworld……](https://www.freebsd.org/status/report-2013-05-devsummit.html#Beyond-Buildworld...)

联系人：Brooks Davis <[brooks@FreeBSD.org](mailto:brooks@FreeBSD.org)>

Buildworld 是 FreeBSD 构建系统中用于构建基本系统的目标。此次会议旨在调查当前的限制、讨论近期的改进，并提出该过程的未来发展方向。

近年来，FreeBSD 在嵌入式系统中的使用越来越多，因此交叉开发变得更加重要。最近，Brooks Davis 提交的一项更改可在没有 root 权限的情况下构建整个基本系统并创建磁盘映像。这使得嵌入式开发变得更加容易，因为多个用户现在可以共享一台昂贵的开发机器，而无需授予他们 root 权限，这台机器能够快速执行构建。

此次会议还讨论了 bmake 导入，它引入了 NetBSD 的 make，并结合 Juniper 的一些改进，应该可以实现更精确的依赖关系跟踪和更快的并行及增量构建。这将为项目的其余部分带来一些额外的好处，例如使我们的 tinderbox 基础设施能够更快地报告构建失败，并及时通知开发者他们是否破坏了构建。

一个经常被请求的功能，当前由 Marcel Moolenar 正在研究，是能够从其他平台构建 FreeBSD。目前，开发基于 FreeBSD 的嵌入式系统需要一个 FreeBSD 主机系统来进行构建，这种要求是我们希望避免的进入障碍。

在 10.x 和 11.x 时间范围内，我们计划对工具链进行一系列更改，包括用基于 LLVM 的工具替代 GNU binutils，并导入 MCLinker。虽然这些改动不太可能成为 10.0 的默认配置，但我们希望能够在今年提供一个无 GPL 的功能性基本系统选项。

## [文档](https://www.freebsd.org/status/report-2013-05-devsummit.html#Documentation)

联系人：Dru Lavigne <[dru@FreeBSD.org](mailto:dru@FreeBSD.org)>  
联系人：Benedict Reuschling <[bcr@FreeBSD.org](mailto:bcr@FreeBSD.org)>

文档工作组在主要会议期间召开了会议，并且还在几个富有成效的晚上改进了 FreeBSD 文档的现状。

FreeBSD 手册最近进行了重大更新，目前正在进行工作，计划发布一个快照版本，并作为专业出版的印刷版提供。还有一些部分需要更新，文档团队正在与相关开发者合作，审阅这些内容。

我们讨论了 FreeBSD 网站的重新设计。目前，许多最常访问的页面难以导航，其视觉设计也略显过时。文档团队正在设计改进的结构，并且已有多方提供协助来改善外观。

FreeBSD 项目是国际化的，许多贡献者的母语并非英语。为了鼓励更多全球开发者参与，提供高质量的文档翻译至关重要。PC-BSD 使用 pootle（可通过 FreeBSD Ports 获得）来帮助保持翻译的一致性和时效性，我们正在评估是否也为 FreeBSD 采用相同的做法。

文档团队计划在 8 月与剑桥 DevSummit 同时举办一个 Docs Hackathon。



## [网络接收性能](https://www.freebsd.org/status/report-2013-05-devsummit.html#Network-Receive-Performance)

联系人：George Neville-Neil <[gnn@FreeBSD.org](mailto:gnn@FreeBSD.org)>

FreeBSD 传统上是一个支持非常高性能网络的平台。这是它被选为奈飞流媒体设备的主要原因之一，该设备目前负责美国超过 20% 的互联网流量。本次会议的目标是讨论连接接收端的当前瓶颈。

现代网卡支持多个接收队列，并且可以根据不同的标准将数据包交付到相应的队列中。设计一个好的 API 来访问这些功能非常重要，因为它缩短了数据包从到达网卡到被交付到用户空间进程的路径。例如，在集群应用或虚拟机的极端情况下，接收队列可能会直接从进程访问，从而绕过内核。在更常规的设置中，数据包应该交付到与接收进程在同一 CPU 上的内核线程，这样到用户空间的拷贝过程就会非常便宜。

该小组检查了多个不同的提案，包括一些补丁，并讨论了通用 API 的需求。该工作仍在进行中。



## [Ports 和软件包](https://www.freebsd.org/status/report-2013-05-devsummit.html#Ports-and-Packages)

| 链接 |
| --- |
| [关于 Poudriere 状态的幻灯片](http://people.freebsd.org/~bdrewery/poudriere-0515.pdf) |
| [关于基于 QEMU 的交叉构建的幻灯片](http://people.freebsd.org/~sson/imgact_binmisc/20130515-bsdcan-xbuild-ports.pdf) |

联系人：Erwin Lansing <[erwin@FreeBSD.org](mailto:erwin@FreeBSD.org)>

 Ports 和软件包工作组讨论了安全事件的影响及其经验教训。传统的二进制包构建现在已上线，构建这些包的基础设施也已变得更加易于维护。构建 pkg(8)（新式）软件包应该很快就能实现。

Bryan Drewery 简短介绍了 Poudriere 新包构建器的状态。它可用于构建本地部署和官方 FreeBSD 软件包的包集合。当原始的包构建基础设施设计时，在高端机器上构建像 Mozilla 这样的大型 Port 需要一天时间。现在，FreeBSD 集群中的单台机器就能在一天之内构建完整的 Port 树。Poudriere 设计为适应这种模式，并且不依赖于 Port 内部支持并行构建。相反，它会在单独的 jail 中构建每个 Port，当不依赖的 Port 可以并行构建时，便利用空闲的 CPU。

展望未来，该项目计划将软件包发布与基本系统发布解耦。每个基本系统发布系列应该在该系列内向后兼容，因此 N.x 的软件包应适用于 N.x+1。该项目将为每个分支每周构建软件包集，并保留两周时间，不进行质量保证（QA），同时每月发布经过 QA 测试的集，并且保留 12 个月。

Stacy Son 和 Brooks Davis 讨论了针对不太常见架构的软件包。Stacy 已经为 FreeBSD 带来了 QEMU 用户模式支持。这意味着 MIPS 或 ARM 上的 FreeBSD 二进制文件可以在 x86 FreeBSD 系统上运行。内核将检测外部二进制文件并在模拟器中启动它。Stacy 使用这一功能创建包含交叉编译器和主机架构的 shell 的 jail，但目标架构则使用原生库。这使得即便是没有交叉构建意识的 Port，也可以运行配置脚本，例如编译和运行可执行文件，同时将构建的计算密集型部分（编译和链接）放在模拟外执行。通过这种方法，我们可以轻松在单台 x86 机器上为 MIPS 和 ARM 构建每周的包集合。对于嵌入式系统的安装，仍然存在一些未解决的问题。pkg(8) 基础设施能够将许多软件包安装到磁盘映像中，但无法在目标系统启动前运行复杂的安装后脚本。


## [UEFI](https://www.freebsd.org/status/report-2013-05-devsummit.html#UEFI)

联系人：Benno Rice <[benno@FreeBSD.org](mailto:benno@FreeBSD.org)>

UEFI 是 Intel 推出的新引导固件标准。它带来了一些挑战，包括 SecureBoot 限制，后者阻止固件引导未签名的内核和引导加载程序。目前这不是一个问题，因为大多数系统要么默认没有启用此限制，要么可以轻松禁用，但未来这一问题将变得更加重要。

FreeBSD 对 UEFI 的支持目标是合并当前项目分支中的引导加载程序，该加载程序将执行签名验证，然后交给更常规的 FreeBSD 引导加载程序。这个加载程序将非常简单，因此不需要频繁更改（和重新签名）。FreeBSD 基金会将负责确保引导加载程序被签名，并与 SecureBoot 配合工作。

在接下来的几个月里，需要进行一些重构和重组工作，以确保 FreeBSD 引导过程能够与 UEFI 干净地配合。这些任务包括：删除在使用 UEFI 的各个平台之间的代码重复，移除 i386 内核中的一些遗留支持，以及重新组织某些引导加载程序代码的构建方式。待 clang 在生成 UNIX 二进制文件时支持 MS Windows 调用约定（UEFI 使用的约定），与 UEFI 的交互将得到简化。Benno Rice 正在这方面进行工作，David Chisnall 提供了一些协助，这项支持预计很快会出现。



## [虚拟化](https://www.freebsd.org/status/report-2013-05-devsummit.html#Virtualization)

| 链接 |
| --- |
| [总体状态幻灯片](http://people.freebsd.org/~grehan/bsdcan13_virt_ext.pdf) |
| [Xen 状态幻灯片](http://people.freebsd.org/~gibbs/XenStatusBSDCan2013.pdf) |
| [VirtIO 状态幻灯片](http://people.freebsd.org/~bryanv/pdfs/bsdcan2013_virtio.pdf) |
| [Bhyve 幻灯片](http://people.freebsd.org/~grehan/bsdcan13_bhyve.pdf) |

联系人：Peter Grehan <[grehan@FreeBSD.org](mailto:grehan@FreeBSD.org)>

虚拟化是一个日益重要的话题，像 Amazon 这样的大型供应商部署了大量的虚拟机，许多用户也在桌面系统上部署虚拟机进行测试和向后兼容。目前，FreeBSD 支持多种虚拟化选项。这个工作组讨论了几种虚拟化技术的当前状态和未来方向。

Xen 是大规模虚拟化的事实标准，FreeBSD 已经支持作为虚拟机运行一段时间。SpectraLogic 为此提供了资金支持，推动了相关工作的进展，目标有两个重叠的方向。第一个是允许 FreeBSD 作为 Domain 0 操作系统运行。Domain 0 是具有更高权限的操作系统，它能够直接与硬件交互，并且必须为虚拟机提供虚拟化设备。为此需要完整的半虚拟化支持。与此相关的是，当作为硬件虚拟化的虚拟机启动时，使用更多半虚拟化硬件的能力。这包括支持新的 PVH 模式，该模式利用硬件支持内存操作，但对其他操作使用半虚拟化驱动，从而在 Xen 上实现最佳性能。

FreeBSD 的 VirtualBox  Port 正在顺利推进，已经初步支持客机中的 3D 加速。微软提供的 HyperV 补丁目前正在测试，预计将纳入 FreeBSD 10 中。

FreeBSD 还包括自己的虚拟化基础设施 bhyve（发音为“beehive”），旨在支持硬件辅助虚拟化。在过去的一年中，bhyve 取得了显著进展，目前已支持 AMD 和 Intel 的虚拟化扩展。凭借如此多的虚拟化选项，FreeBSD 现在在虚拟化方面无论是作为主机还是虚拟机都处于非常有利的位置。
