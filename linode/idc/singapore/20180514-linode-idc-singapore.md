#  多地到Linode新加坡[Singapore]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode新加坡\[Singapore\]机房的Ping测试（20180514）](/images/thumbnails/to_linode_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[新加坡-新加坡机房](https://vps123.top/linode-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180514-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Linode新加坡-新加坡机房的PING测试结果，连通概况如下：大陆30个省市的956个有效测试样本中，共有超时点14个；响应均值为162毫秒，最快的三地区为山东、河南、安徽，最慢的三地区为四川、上海、重庆；浙江、江苏、湖北、山东、河南等10处有响应超时情况；四川、云南、上海、广西、贵州等6处丢包率较高。海外17个国家地区的80个有效测试样本中，无超时点；响应均值为164毫秒，最快的三地区为新加坡、马来西亚、印度尼西亚，最慢的三地区为法国、俄罗斯、巴西。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_singapore-singapore_20180514_mainland.png)

大陆各省份到Linode新加坡-新加坡机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
山东 | 49个 | 1个 | 128ms | 0.5% | 均值 | 956个 | 14个 | 162ms | 3.3%  
河南 | 57个 | 1个 | 134ms | 1.3% | 宁夏 | 11个 | 0 | 165ms | 1.4%  
安徽 | 40个 | 0 | 142ms | 4.5% | 内蒙古 | 36个 | 0 | 166ms | 1.6%  
山西 | 36个 | 0 | 143ms | 1.4% | 甘肃 | 20个 | 0 | 170ms | 1.9%  
贵州 | 27个 | 1个 | 144ms | 6.1% | 广东 | 75个 | 1个 | 181ms | 4.5%  
江西 | 25个 | 0 | 147ms | 3.5% | 吉林 | 15个 | 0 | 182ms | 3.3%  
湖南 | 46个 | 1个 | 147ms | 3.2% | 青海 | 4个 | 0 | 183ms | 0  
辽宁 | 36个 | 0 | 147ms | 3.5% | 湖北 | 45个 | 2个 | 183ms | 5.5%  
江苏 | 62个 | 2个 | 149ms | 2.3% | 广西 | 39个 | 0 | 186ms | 6.2%  
福建 | 34个 | 1个 | 150ms | 1.6% | 云南 | 24个 | 0 | 190ms | 6.6%  
浙江 | 53个 | 3个 | 151ms | 2.0% | 北京 | 7个 | 1个 | 193ms | 0  
黑龙江 | 37个 | 0 | 155ms | 2.2% | 新疆 | 29个 | 0 | 202ms | 1.4%  
陕西 | 32个 | 0 | 155ms | 3.3% | 四川 | 49个 | 0 | 203ms | 8.9%  
海南 | 10个 | 0 | 156ms | 3.4% | 上海 | 8个 | 0 | 210ms | 6.4%  
天津 | 5个 | 0 | 159ms | 0 | 重庆 | 14个 | 0 | 215ms | 4.8%  
河北 | 31个 | 0 | 159ms | 2.2% |  |  |  |  |   
  
简评：如果你考虑在Linode的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有956个，其中超时点14个，平均响应时间为162毫秒，丢包率为3%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的26个，在200-300毫秒间的4个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_singapore-singapore_20180514_overseas.png)

海外线路到Linode新加坡-新加坡机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
新加坡 | 6个 | 0 | 1ms | 0 | 美国 | 19个 | 0 | 188ms | 0.4%  
马来西亚 | 4个 | 0 | 28ms | 0.3% | 南非 | 1个 | 0 | 216ms | 0  
印度尼西亚 | 1个 | 0 | 46ms | 0 | 加拿大 | 3个 | 0 | 232ms | 0  
香港 | 19个 | 0 | 52ms | 0 | 澳大利亚 | 2个 | 0 | 233ms | 0  
菲律宾 | 1个 | 0 | 56ms | 0 | 德国 | 2个 | 0 | 263ms | 1.0%  
台湾 | 1个 | 0 | 60ms | - | 英国 | 2个 | 0 | 273ms | 0  
日本 | 2个 | 0 | 81ms | 0 | 法国 | 2个 | 0 | 274ms | 0  
韩国 | 13个 | 0 | 105ms | 0 | 俄罗斯 | 1个 | 0 | 322ms | 0  
均值 | 80个 | 0 | 164ms | 0.1% | 巴西 | 1个 | 0 | 362ms | 0  
  
简评：如果你考虑在Linode的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有80个，其中超时点0个，平均响应时间为164毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的4个，在100-200毫秒间的2个，在200-300毫秒间的6个，超过300毫秒的2个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180514 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180514 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180514-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180514")
    * [达拉斯](/linode/idc/dallas/20180514-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180514")
    * [法兰克福](/linode/idc/frankfurt/20180514-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180514")
    * [佛利蒙](/linode/idc/fremont/20180514-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180514")
    * [伦敦](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")
    * [纽瓦克](/linode/idc/newark/20180514-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180514")
    * [东京](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
  * 到Linode新加坡机房的 _其他近期报告_ ： 
    * [20180527](/linode/idc/singapore/20180527-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180527")
    * [20180622](/linode/idc/singapore/20180622-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180622")
    * [20180804](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")
    * [20180918](/linode/idc/singapore/20180918-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180514-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [Vultr](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")



本文最初发表于[多地到Linode新加坡[Singapore]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-linode-idc-singapore.html)
