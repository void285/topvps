#  多地到Linode东京[Tokyo]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode东京\[Tokyo\]机房的Ping测试（20180527）](/images/thumbnails/to_linode_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[日本-东京机房](https://vps123.top/linode-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180527-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的954个有效测试样本中，共有超时点20个；响应均值为176毫秒，最快的三地区为浙江、湖南、山西，最慢的三地区为吉林、重庆、河北；广东、山东、江西、江苏、湖北等13处有响应超时情况；上海、重庆、四川、江西、湖北等30处丢包率较高。海外21个国家地区的86个有效测试样本中，共有超时点1个；响应均值为169毫秒，最快的三地区为日本、台湾、韩国，最慢的三地区为巴西、荷兰、南非；韩国有响应超时情况。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/linode_20180527/plot_idc_linode_japan-tokyo_20180527_mainland.png)

**大陆各省份到Linode日本-东京机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
浙江 | 48个 | 1个 | 159ms | 14.8%  
湖南 | 45个 | 1个 | 159ms | 9.8%  
山西 | 35个 | 0 | 159ms | 8.4%  
江西 | 23个 | 2个 | 160ms | 15.6%  
北京 | 8个 | 1个 | 160ms | 9.5%  
广西 | 38个 | 0 | 161ms | 11.8%  
福建 | 37个 | 0 | 162ms | 13.1%  
安徽 | 35个 | 0 | 162ms | 15.3%  
青海 | 4个 | 0 | 163ms | 8.3%  
海南 | 14个 | 0 | 164ms | 12.3%  
江苏 | 64个 | 2个 | 165ms | 14.8%  
河南 | 52个 | 1个 | 166ms | 9.9%  
天津 | 5个 | 0 | 169ms | 15.3%  
广东 | 80个 | 3个 | 169ms | 11.6%  
山东 | 50个 | 3个 | 173ms | 11.8%  
宁夏 | 12个 | 0 | 173ms | 9.3%  
上海 | 8个 | 0 | 173ms | 28.9%  
陕西 | 31个 | 0 | 174ms | 10.3%  
均值 | 954个 | 20个 | 176ms | 12.4%  
黑龙江 | 40个 | 1个 | 177ms | 9.1%  
辽宁 | 37个 | 0 | 180ms | 13.2%  
贵州 | 26个 | 1个 | 183ms | 11.7%  
云南 | 22个 | 0 | 187ms | 14.0%  
湖北 | 43个 | 2个 | 190ms | 15.5%  
甘肃 | 23个 | 0 | 193ms | 10.7%  
内蒙古 | 34个 | 0 | 195ms | 11.8%  
四川 | 47个 | 1个 | 197ms | 16.1%  
新疆 | 27个 | 0 | 204ms | 8.2%  
吉林 | 19个 | 0 | 205ms | 12.0%  
重庆 | 15个 | 1个 | 207ms | 16.8%  
河北 | 32个 | 0 | 218ms | 10.3%  
  
**简评：** 如果你考虑在Linode的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有954个，其中超时点20个，平均响应时间为176毫秒，丢包率为12%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的26个，在200-300毫秒间的4个；  
超时点较多的省份：北京；  
丢包率较高的省份：浙江、江西、广西、福建、安徽、海南、江苏、天津、广东、山东、上海、陕西、辽宁、贵州、云南、湖北、甘肃、内蒙古、四川、吉林、重庆、河北；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/linode_20180527/plot_idc_linode_japan-tokyo_20180527_overseas.png)

**海外线路到Linode日本-东京机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
日本 | 1个 | 0 | 1ms | 0  
台湾 | 1个 | 0 | 39ms | -  
韩国 | 12个 | 1个 | 56ms | 2.7%  
越南 | 2个 | 0 | 72ms | 0  
香港 | 19个 | 0 | 79ms | 0  
印度尼西亚 | 1个 | 0 | 89ms | 1.0%  
新加坡 | 5个 | 0 | 97ms | 0  
马来西亚 | 5个 | 0 | 103ms | 0  
美国 | 21个 | 0 | 115ms | 0.3%  
澳大利亚 | 2个 | 0 | 159ms | 0  
均值 | 86个 | 1个 | 169ms | 0.6%  
菲律宾 | 1个 | 0 | 175ms | 1.0%  
加拿大 | 3个 | 0 | 183ms | 0  
俄罗斯 | 1个 | 0 | 183ms | 0  
柬埔寨 | 1个 | 0 | 241ms | 5.0%  
德国 | 3个 | 0 | 253ms | 0  
法国 | 1个 | 0 | 265ms | 0  
意大利 | 1个 | 0 | 266ms | -  
英国 | 2个 | 0 | 271ms | 0  
巴西 | 1个 | 0 | 273ms | 0  
荷兰 | 1个 | 0 | 276ms | 0  
南非 | 2个 | 0 | 368ms | 1.0%  
  
**简评：** 如果你考虑在Linode的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有86个，其中超时点1个，平均响应时间为169毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的5个，在100-200毫秒间的6个，在200-300毫秒间的7个，超过300毫秒的1个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180527 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180527 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180527-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180527")
    * [达拉斯](/linode/idc/dallas/20180527-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180527")
    * [法兰克福](/linode/idc/frankfurt/20180527-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180527")
    * [佛利蒙](/linode/idc/fremont/20180527-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180527")
    * [伦敦](/linode/idc/london/20180527-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180527")
    * [纽瓦克](/linode/idc/newark/20180527-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180527")
    * [新加坡](/linode/idc/singapore/20180527-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180527")
  * 到Linode东京机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
    * [20180622](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")
    * [20180804](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")
    * [20180918](/linode/idc/tokyo/20180918-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180918")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")



本文最初发表于[多地到Linode东京[Tokyo]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-linode-idc-tokyo.html)
