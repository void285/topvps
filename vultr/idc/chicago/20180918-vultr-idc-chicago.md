#  多地到Vultr芝加哥[Chicago]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr芝加哥\[Chicago\]机房的Ping测试（20180918）](/images/thumbnails/to_vultr_LosAngeles.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-芝加哥机房](https://vps123.top/vultr-facilities.html#chicago)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-芝加哥机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180918-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Vultr美国-芝加哥机房的PING测试结果，连通概况如下：大陆31个省市的1399个有效测试样本中，共有超时点11个；响应均值为251毫秒，最快的三地区为江苏、浙江、广东，最慢的三地区为甘肃、新疆、西藏；江苏、浙江、广东、重庆、山西等6处有响应超时情况；天津丢包率较高。海外16个国家地区的74个有效测试样本中，无超时点；响应均值为176毫秒，最快的三地区为加拿大、美国、意大利，最慢的三地区为印度尼西亚、马来西亚、赞比亚；印度尼西亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于芝加哥\[Chicago\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_usa-chicago_20180918_mainland.png)

大陆各省份到Vultr美国-芝加哥机房的测速数据 [20180918] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
江苏 | 93个 | 5个 | 228ms | 0.1% | 北京 | 10个 | 0 | 250ms | 0.1%  
浙江 | 66个 | 2个 | 233ms | 0.8% | 辽宁 | 62个 | 0 | 250ms | 1.0%  
广东 | 121个 | 1个 | 234ms | 0 | 湖南 | 65个 | 1个 | 251ms | 1.6%  
重庆 | 8个 | 1个 | 236ms | 0.6% | 均值 | 1399个 | 11个 | 251ms | 1.0%  
上海 | 8个 | 0 | 237ms | 0 | 贵州 | 41个 | 0 | 254ms | 0.1%  
河北 | 60个 | 0 | 240ms | 0 | 黑龙江 | 54个 | 0 | 262ms | 0.7%  
安徽 | 67个 | 0 | 240ms | 0.6% | 宁夏 | 6个 | 0 | 262ms | 0.2%  
山东 | 90个 | 0 | 241ms | 1.5% | 内蒙古 | 53个 | 0 | 263ms | 1.9%  
广西 | 59个 | 0 | 241ms | 0.9% | 四川 | 78个 | 0 | 264ms | 1.2%  
海南 | 14个 | 0 | 242ms | 0.3% | 云南 | 30个 | 0 | 267ms | 0.2%  
福建 | 39个 | 0 | 243ms | 0.5% | 青海 | 5个 | 0 | 269ms | 0  
湖北 | 53个 | 0 | 243ms | 0.1% | 河南 | 86个 | 0 | 272ms | 4.1%  
吉林 | 20个 | 0 | 244ms | 0.4% | 陕西 | 42个 | 0 | 273ms | 0.6%  
天津 | 7个 | 0 | 246ms | 10.0% | 甘肃 | 32个 | 0 | 279ms | 0.7%  
江西 | 41个 | 0 | 247ms | 0.1% | 新疆 | 32个 | 0 | 307ms | 3.8%  
山西 | 56个 | 1个 | 249ms | 0.1% | 西藏 | 1个 | 0 | 376ms | 3.0%  
  
简评：如果你考虑在Vultr的芝加哥[Chicago]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于芝加哥[Chicago]的机房的连通状况。到此机房的ping监测点共有1399个，其中超时点11个，平均响应时间为251毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的29个，超过300毫秒的2个；  
超时点较多的省份：重庆；  
丢包率较高的省份：天津；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于芝加哥\[Chicago\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_usa-chicago_20180918_overseas.png)

海外线路到Vultr美国-芝加哥机房的测速数据 [20180918] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 3个 | 0 | 17ms | 0 | 新加坡 | 5个 | 0 | 190ms | 0  
美国 | 11个 | 0 | 82ms | 0 | 荷兰 | 1个 | 0 | 192ms | 0  
意大利 | 1个 | 0 | 96ms | - | 菲律宾 | 1个 | 0 | 216ms | 2.0%  
台湾 | 2个 | 0 | 114ms | 0 | 澳大利亚 | 2个 | 0 | 220ms | 5.0%  
德国 | 3个 | 0 | 116ms | 0 | 越南 | 2个 | 0 | 233ms | 0  
韩国 | 12个 | 0 | 164ms | 0 | 印度尼西亚 | 1个 | 0 | 270ms | 6.7%  
日本 | 3个 | 0 | 173ms | 2.1% | 马来西亚 | 6个 | 0 | 272ms | 0  
均值 | 74个 | 0 | 176ms | 1.6% | 赞比亚 | 2个 | 0 | 286ms | 3.2%  
香港 | 19个 | 0 | 187ms | 5.0% |  |  |  |  |   
  
简评：如果你考虑在Vultr的芝加哥[Chicago]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于芝加哥[Chicago]的机房的连通状况。到此机房的ping监测点共有74个，其中超时点0个，平均响应时间为176毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的2个，在100-200毫秒间的7个，在200-300毫秒间的6个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180918 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180918 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180918-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180918")
    * [亚特兰大](/vultr/idc/atlanta/20180918-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180918")
    * [达拉斯](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
    * [法兰克福](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")
    * [伦敦](/vultr/idc/london/20180918-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180918")
    * [洛杉矶](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
    * [迈阿密](/vultr/idc/miami/20180918-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180918")
    * [新泽西](/vultr/idc/newjersey/20180918-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180918")
    * [巴黎](/vultr/idc/paris/20180918-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180918")
    * [西雅图](/vultr/idc/seattle/20180918-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180918")
    * [硅谷](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")
    * [新加坡](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")
    * [悉尼](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")
    * [东京](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 到Vultr芝加哥机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/chicago/20180514-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180514")
    * [20180527](/vultr/idc/chicago/20180527-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180527")
    * [20180622](/vultr/idc/chicago/20180622-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180622")
    * [20180804](/vultr/idc/chicago/20180804-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180804")



本文最初发表于[多地到Vultr芝加哥[Chicago]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-vultr-idc-chicago.html)
