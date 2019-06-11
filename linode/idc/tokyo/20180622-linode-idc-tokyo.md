#  多地到Linode东京[Tokyo]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode东京\[Tokyo\]机房的Ping测试（20180622）](/images/thumbnails/to_linode_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[日本-东京机房](https://vps123.top/linode-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180622-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的861个有效测试样本中，共有超时点39个；响应均值为181毫秒，最快的三地区为福建、湖南、贵州，最慢的三地区为新疆、云南、香港；云南、江苏、浙江、四川、福建等17处有响应超时情况；青海、甘肃、重庆、吉林、北京等29处丢包率较高。海外16个国家地区的49个有效测试样本中，无超时点；响应均值为152毫秒，最快的三地区为日本、台湾、韩国，最慢的三地区为巴西、英国、柬埔寨。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_idc_linode_japan-tokyo_20180622_mainland.png)

大陆各省份到Linode日本-东京机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
福建 | 29个 | 2个 | 145ms | 7.0% | 均值 | 861个 | 39个 | 181ms | 8.7%  
湖南 | 36个 | 0 | 147ms | 4.4% | 辽宁 | 34个 | 2个 | 182ms | 9.4%  
贵州 | 24个 | 0 | 158ms | 6.5% | 湖北 | 32个 | 1个 | 192ms | 10.5%  
广西 | 41个 | 0 | 158ms | 8.6% | 天津 | 2个 | 0 | 194ms | 10.5%  
海南 | 12个 | 1个 | 158ms | 6.1% | 浙江 | 53个 | 4个 | 195ms | 9.1%  
山东 | 44个 | 1个 | 164ms | 9.8% | 黑龙江 | 32个 | 0 | 198ms | 9.7%  
江西 | 22个 | 0 | 166ms | 6.8% | 青海 | 5个 | 0 | 203ms | 17.2%  
河南 | 41个 | 1个 | 167ms | 9.0% | 重庆 | 12个 | 1个 | 209ms | 13.0%  
山西 | 29个 | 2个 | 170ms | 6.7% | 内蒙古 | 27个 | 0 | 215ms | 10.5%  
广东 | 72个 | 2个 | 172ms | 5.6% | 四川 | 41个 | 3个 | 218ms | 10.2%  
安徽 | 30个 | 2个 | 172ms | 8.2% | 甘肃 | 15个 | 0 | 218ms | 14.2%  
江苏 | 68个 | 4个 | 174ms | 9.6% | 吉林 | 19个 | 0 | 219ms | 12.6%  
北京 | 9个 | 0 | 178ms | 12.4% | 上海 | 7个 | 1个 | 222ms | 6.8%  
陕西 | 27个 | 1个 | 178ms | 7.6% | 新疆 | 24个 | 1个 | 223ms | 10.7%  
河北 | 29个 | 0 | 178ms | 6.8% | 云南 | 20个 | 10个 | 228ms | 8.3%  
宁夏 | 13个 | 0 | 179ms | 10.2% | 香港 | 12个 | 0 | - | -  
  
简评：如果你考虑在Linode的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有861个，其中超时点39个，平均响应时间为181毫秒，丢包率为8%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的21个，在200-300毫秒间的9个；  
超时点较多的省份：上海、云南；  
丢包率较高的省份：北京、宁夏、湖北、天津、青海、重庆、内蒙古、四川、甘肃、吉林、新疆；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_idc_linode_japan-tokyo_20180622_overseas.png)

海外线路到Linode日本-东京机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
日本 | 1个 | 0 | 18ms | 1.0% | 均值 | 49个 | 0 | 152ms | 0.5%  
台湾 | 1个 | 0 | 30ms | 0 | 澳大利亚 | 1个 | 0 | 198ms | 1.0%  
韩国 | 7个 | 0 | 53ms | 1.1% | 加拿大 | 1个 | 0 | 225ms | 0  
菲律宾 | 2个 | 0 | 63ms | 1.0% | 法国 | 1个 | 0 | 234ms | 0  
越南 | 2个 | 0 | 73ms | 0 | 南非 | 2个 | 0 | 235ms | 0  
香港 | 12个 | 0 | 91ms | 0 | 巴西 | 1个 | 0 | 258ms | 0  
新加坡 | 2个 | 0 | 101ms | 0 | 英国 | 1个 | 0 | 272ms | 0  
马来西亚 | 4个 | 0 | 103ms | 0.3% | 柬埔寨 | 1个 | 0 | 353ms | 3.0%  
美国 | 10个 | 0 | 135ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Linode的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有49个，其中超时点0个，平均响应时间为152毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的4个，在100-200毫秒间的4个，在200-300毫秒间的5个，超过300毫秒的1个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180622 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180622 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180622-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180622")
    * [达拉斯](/linode/idc/dallas/20180622-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180622")
    * [法兰克福](/linode/idc/frankfurt/20180622-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180622")
    * [佛利蒙](/linode/idc/fremont/20180622-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180622")
    * [伦敦](/linode/idc/london/20180622-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180622")
    * [纽瓦克](/linode/idc/newark/20180622-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180622")
    * [新加坡](/linode/idc/singapore/20180622-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180622")
  * 到Linode东京机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
    * [20180527](/linode/idc/tokyo/20180527-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180527")
    * [20180804](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")
    * [20180918](/linode/idc/tokyo/20180918-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180918")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")



本文最初发表于[多地到Linode东京[Tokyo]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-linode-idc-tokyo.html)
