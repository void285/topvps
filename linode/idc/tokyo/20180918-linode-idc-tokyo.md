#  多地到Linode东京[Tokyo]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode东京\[Tokyo\]机房的Ping测试（20180918）](/images/thumbnails/to_linode_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[日本-东京机房](https://vps123.top/linode-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180918-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Linode日本-东京机房的PING测试结果，连通概况如下：大陆31个省市的1270个有效测试样本中，共有超时点13个；响应均值为140毫秒，最快的三地区为上海、吉林、山西，最慢的三地区为宁夏、青海、西藏；江苏、山西、浙江、广东、贵州等6处有响应超时情况；西藏、安徽、山东、江苏、福建等10处丢包率较高。海外16个国家地区的61个有效测试样本中，无超时点；响应均值为180毫秒，最快的三地区为日本、越南、印度尼西亚，最慢的三地区为澳大利亚、菲律宾、赞比亚；菲律宾丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/linode_20180918/plot_idc_linode_japan-tokyo_20180918_mainland.png)

大陆各省份到Linode日本-东京机房的测速数据 [20180918] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 6个 | 0 | 106ms | 1.4% | 天津 | 7个 | 0 | 140ms | 3.0%  
吉林 | 19个 | 0 | 108ms | 1.1% | 均值 | 1270个 | 13个 | 140ms | 3.8%  
山西 | 49个 | 2个 | 109ms | 1.6% | 广东 | 108个 | 1个 | 142ms | 0.6%  
重庆 | 8个 | 0 | 119ms | 0 | 江苏 | 85个 | 6个 | 143ms | 7.4%  
辽宁 | 49个 | 0 | 121ms | 1.8% | 浙江 | 62个 | 2个 | 146ms | 5.2%  
黑龙江 | 46个 | 0 | 123ms | 1.2% | 安徽 | 66个 | 0 | 146ms | 7.7%  
河南 | 80个 | 0 | 125ms | 6.0% | 陕西 | 40个 | 0 | 148ms | 1.0%  
广西 | 48个 | 0 | 126ms | 1.9% | 贵州 | 36个 | 1个 | 161ms | 5.4%  
河北 | 48个 | 0 | 126ms | 1.5% | 湖北 | 48个 | 1个 | 164ms | 2.4%  
内蒙古 | 50个 | 0 | 128ms | 3.2% | 新疆 | 29个 | 0 | 174ms | 2.7%  
山东 | 90个 | 0 | 129ms | 7.5% | 四川 | 65个 | 0 | 175ms | 3.1%  
北京 | 7个 | 0 | 131ms | 0.9% | 云南 | 28个 | 0 | 175ms | 3.2%  
湖南 | 63个 | 0 | 132ms | 1.9% | 甘肃 | 31个 | 0 | 176ms | 5.0%  
江西 | 38个 | 0 | 137ms | 5.4% | 宁夏 | 3个 | 0 | 176ms | 3.0%  
海南 | 14个 | 0 | 137ms | 1.4% | 青海 | 5个 | 0 | 203ms | 5.3%  
福建 | 40个 | 0 | 140ms | 6.8% | 西藏 | 2个 | 0 | 335ms | 11.5%  
  
简评：如果你考虑在Linode的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有1270个，其中超时点13个，平均响应时间为140毫秒，丢包率为3%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的29个，在200-300毫秒间的1个，超过300毫秒的1个；  
丢包率较高的省份：西藏；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/linode_20180918/plot_idc_linode_japan-tokyo_20180918_overseas.png)

海外线路到Linode日本-东京机房的测速数据 [20180918] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
日本 | 3个 | 0 | 28ms | 0 | 加拿大 | 2个 | 0 | 165ms | 0  
越南 | 2个 | 0 | 71ms | 0 | 均值 | 61个 | 0 | 180ms | 2.4%  
印度尼西亚 | 1个 | 0 | 94ms | 0 | 德国 | 2个 | 0 | 222ms | 0  
韩国 | 10个 | 0 | 99ms | 0 | 荷兰 | 1个 | 0 | 236ms | 0  
美国 | 9个 | 0 | 110ms | 0 | 俄罗斯 | 1个 | 0 | 289ms | -  
新加坡 | 4个 | 0 | 114ms | 0 | 澳大利亚 | 1个 | 0 | 296ms | 0  
香港 | 14个 | 0 | 124ms | 0 | 菲律宾 | 2个 | 0 | 307ms | 35.0%  
马来西亚 | 6个 | 0 | 127ms | 0 | 赞比亚 | 2个 | 0 | 477ms | 1.5%  
台湾 | 1个 | 0 | 127ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Linode的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有61个，其中超时点0个，平均响应时间为180毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的3个，在100-200毫秒间的6个，在200-300毫秒间的4个，超过300毫秒的2个；  
丢包率较高的国家/地区：菲律宾；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180918 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180918 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180918-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180918")
    * [达拉斯](/linode/idc/dallas/20180918-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180918")
    * [法兰克福](/linode/idc/frankfurt/20180918-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180918")
    * [佛利蒙](/linode/idc/fremont/20180918-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180918")
    * [伦敦](/linode/idc/london/20180918-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180918")
    * [纽瓦克](/linode/idc/newark/20180918-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180918")
    * [新加坡](/linode/idc/singapore/20180918-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180918")
  * 到Linode东京机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
    * [20180527](/linode/idc/tokyo/20180527-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180527")
    * [20180622](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")
    * [20180804](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")



本文最初发表于[多地到Linode东京[Tokyo]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-linode-idc-tokyo.html)
