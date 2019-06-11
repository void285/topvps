#  多地到Linode东京[Tokyo]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode东京\[Tokyo\]机房的Ping测试（20180426）](/images/thumbnails/to_linode_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[日本-东京机房](https://vps123.top/linode-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180426-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Linode日本-东京机房的PING测试结果，连通概况如下：大陆31个省市的812个有效测试样本中，共有超时点4个；响应均值为124毫秒，最快的三地区为天津、福建、上海，最慢的三地区为重庆、新疆、河北；浙江、江苏、北京有响应超时情况；上海、新疆、甘肃、河北、青海等18处丢包率较高。海外19个国家地区的79个有效测试样本中，共有超时点1个；响应均值为158毫秒，最快的三地区为日本、台湾、韩国，最慢的三地区为荷兰、法国、南非；韩国有响应超时情况。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_idc_linode_japan-tokyo_20180426_mainland.png)

**大陆各省份到Linode日本-东京机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 5个 | 0 | 76ms | 5.0%  
福建 | 24个 | 0 | 94ms | 4.7%  
上海 | 8个 | 0 | 94ms | 14.6%  
山西 | 31个 | 0 | 99ms | 2.0%  
海南 | 12个 | 0 | 106ms | 4.7%  
湖南 | 40个 | 0 | 108ms | 2.9%  
江苏 | 49个 | 1个 | 110ms | 4.5%  
吉林 | 17个 | 0 | 110ms | 4.1%  
江西 | 17个 | 0 | 112ms | 5.6%  
湖北 | 35个 | 0 | 113ms | 6.1%  
安徽 | 40个 | 0 | 113ms | 5.8%  
山东 | 46个 | 0 | 116ms | 5.7%  
北京 | 4个 | 1个 | 116ms | 7.3%  
广西 | 32个 | 0 | 117ms | 8.6%  
辽宁 | 33个 | 0 | 117ms | 6.8%  
河南 | 51个 | 0 | 118ms | 6.5%  
浙江 | 32个 | 2个 | 118ms | 5.9%  
内蒙古 | 29个 | 0 | 120ms | 3.8%  
贵州 | 23个 | 0 | 122ms | 6.3%  
黑龙江 | 32个 | 0 | 123ms | 5.0%  
均值 | 812个 | 4个 | 124ms | 5.8%  
宁夏 | 10个 | 0 | 127ms | 7.2%  
四川 | 41个 | 0 | 132ms | 7.3%  
广东 | 58个 | 0 | 133ms | 2.0%  
陕西 | 27个 | 0 | 137ms | 4.3%  
云南 | 25个 | 0 | 138ms | 5.4%  
青海 | 4个 | 0 | 148ms | 10.0%  
甘肃 | 21个 | 0 | 152ms | 11.1%  
西藏 | 1个 | 0 | 153ms | 0  
重庆 | 8个 | 0 | 170ms | 4.3%  
新疆 | 28个 | 0 | 183ms | 11.3%  
河北 | 29个 | 0 | 190ms | 10.6%  
  
**简评：** 如果你考虑在Linode的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有812个，其中超时点4个，平均响应时间为124毫秒，丢包率为5%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50-100毫秒间的4个，在100-200毫秒间的27个；  
超时点较多的省份：北京；  
丢包率较高的省份：上海、青海、甘肃、新疆、河北；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_idc_linode_japan-tokyo_20180426_overseas.png)

**海外线路到Linode日本-东京机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
日本 | 3个 | 0 | 7ms | 1.0%  
台湾 | 1个 | 0 | 40ms | -  
韩国 | 12个 | 1个 | 64ms | 2.8%  
香港 | 19个 | 0 | 83ms | 0  
印度尼西亚 | 1个 | 0 | 92ms | 0  
新加坡 | 5个 | 0 | 93ms | 0  
马来西亚 | 4个 | 0 | 100ms | 0.3%  
菲律宾 | 1个 | 0 | 112ms | 2.0%  
美国 | 16个 | 0 | 126ms | 0  
澳大利亚 | 2个 | 0 | 134ms | 0  
均值 | 79个 | 1个 | 158ms | 0.3%  
加拿大 | 3个 | 0 | 170ms | 0  
俄罗斯 | 1个 | 0 | 186ms | 0  
柬埔寨 | 1个 | 0 | 189ms | 0  
越南 | 1个 | 0 | 207ms | 0  
德国 | 1个 | 0 | 243ms | 0  
英国 | 3个 | 0 | 249ms | 0  
荷兰 | 2个 | 0 | 257ms | 0  
法国 | 2个 | 0 | 267ms | 0  
南非 | 1个 | 0 | 388ms | 0  
  
**简评：** 如果你考虑在Linode的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有79个，其中超时点1个，平均响应时间为158毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的5个，在100-200毫秒间的6个，在200-300毫秒间的5个，超过300毫秒的1个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180426 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180426 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180426-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180426")
    * [达拉斯](/linode/idc/dallas/20180426-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180426")
    * [法兰克福](/linode/idc/frankfurt/20180426-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180426")
    * [佛利蒙](/linode/idc/fremont/20180426-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180426")
    * [伦敦](/linode/idc/london/20180426-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180426")
    * [纽瓦克](/linode/idc/newark/20180426-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180426")
    * [新加坡](/linode/idc/singapore/20180426-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180426")
  * 到Linode东京机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
    * [20180527](/linode/idc/tokyo/20180527-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180527")
    * [20180622](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")
    * [20180804](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")
    * [20180918](/linode/idc/tokyo/20180918-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180918")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/tokyo/20180426-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180426")



本文最初发表于[多地到Linode东京[Tokyo]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-linode-idc-tokyo.html)
