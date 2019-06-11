#  多地到Linode新加坡[Singapore]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode新加坡\[Singapore\]机房的Ping测试（20180527）](/images/thumbnails/to_linode_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[新加坡-新加坡机房](https://vps123.top/linode-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180527-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的977个有效测试样本中，共有超时点18个；响应均值为224毫秒，最快的三地区为湖南、山东、江西，最慢的三地区为内蒙古、上海、吉林；江苏、山东、广东、湖南、河南等10处有响应超时情况；上海、重庆、湖北、安徽、江西等30处丢包率较高。海外21个国家地区的88个有效测试样本中，共有超时点1个；响应均值为169毫秒，最快的三地区为新加坡、印度尼西亚、马来西亚，最慢的三地区为俄罗斯、巴西、南非；香港有响应超时情况。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/linode_20180527/plot_idc_linode_singapore-singapore_20180527_mainland.png)

**大陆各省份到Linode新加坡-新加坡机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
湖南 | 46个 | 1个 | 185ms | 10.8%  
山东 | 53个 | 3个 | 200ms | 11.4%  
江西 | 24个 | 0 | 201ms | 15.2%  
广西 | 39个 | 0 | 203ms | 12.1%  
河南 | 55个 | 1个 | 205ms | 8.6%  
山西 | 36个 | 0 | 206ms | 8.0%  
浙江 | 50个 | 1个 | 207ms | 13.8%  
黑龙江 | 40个 | 0 | 213ms | 8.7%  
安徽 | 38个 | 0 | 213ms | 15.3%  
贵州 | 28个 | 0 | 217ms | 10.9%  
江苏 | 63个 | 5个 | 217ms | 14.1%  
青海 | 4个 | 0 | 218ms | 8.3%  
河北 | 36个 | 0 | 222ms | 10.4%  
陕西 | 33个 | 0 | 224ms | 9.5%  
均值 | 977个 | 18个 | 224ms | 11.8%  
海南 | 14个 | 0 | 227ms | 11.1%  
辽宁 | 39个 | 0 | 228ms | 11.3%  
广东 | 79个 | 3个 | 229ms | 11.5%  
北京 | 8个 | 1个 | 230ms | 7.6%  
宁夏 | 12个 | 0 | 230ms | 9.5%  
新疆 | 28个 | 0 | 238ms | 7.7%  
福建 | 36个 | 1个 | 239ms | 13.6%  
天津 | 5个 | 0 | 239ms | 10.9%  
湖北 | 44个 | 1个 | 245ms | 15.5%  
云南 | 21个 | 0 | 247ms | 13.0%  
四川 | 48个 | 0 | 249ms | 14.1%  
甘肃 | 23个 | 0 | 251ms | 11.7%  
重庆 | 15个 | 1个 | 261ms | 15.7%  
内蒙古 | 34个 | 0 | 261ms | 10.8%  
上海 | 8个 | 0 | 272ms | 19.7%  
吉林 | 18个 | 0 | 279ms | 11.9%  
  
**简评：** 如果你考虑在Linode的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有977个，其中超时点18个，平均响应时间为224毫秒，丢包率为11%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的2个，在200-300毫秒间的28个；  
超时点较多的省份：北京；  
丢包率较高的省份：湖南、山东、江西、广西、浙江、安徽、贵州、江苏、河北、海南、辽宁、广东、福建、天津、湖北、云南、四川、甘肃、重庆、内蒙古、上海、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/linode_20180527/plot_idc_linode_singapore-singapore_20180527_overseas.png)

**海外线路到Linode新加坡-新加坡机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
新加坡 | 6个 | 0 | 1ms | 0  
印度尼西亚 | 1个 | 0 | 20ms | 0  
马来西亚 | 5个 | 0 | 27ms | 0  
越南 | 2个 | 0 | 51ms | 0  
香港 | 20个 | 1个 | 53ms | 0  
台湾 | 1个 | 0 | 61ms | -  
日本 | 1个 | 0 | 73ms | 0  
韩国 | 12个 | 0 | 110ms | 0  
菲律宾 | 1个 | 0 | 134ms | 0  
澳大利亚 | 2个 | 0 | 163ms | 0  
柬埔寨 | 1个 | 0 | 166ms | 2.0%  
均值 | 88个 | 1个 | 169ms | 0.2%  
荷兰 | 1个 | 0 | 179ms | 0  
美国 | 21个 | 0 | 187ms | 1.7%  
法国 | 1个 | 0 | 198ms | 0  
加拿大 | 3个 | 0 | 233ms | 0  
英国 | 2个 | 0 | 260ms | 0  
德国 | 3个 | 0 | 276ms | 0  
意大利 | 1个 | 0 | 324ms | -  
俄罗斯 | 1个 | 0 | 327ms | 0  
巴西 | 1个 | 0 | 346ms | 0  
南非 | 2个 | 0 | 369ms | 0  
  
**简评：** 如果你考虑在Linode的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有88个，其中超时点1个，平均响应时间为169毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的4个，在100-200毫秒间的7个，在200-300毫秒间的3个，超过300毫秒的4个；

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
    * [东京](/linode/idc/tokyo/20180527-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180527")
  * 到Linode新加坡机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/singapore/20180514-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180514")
    * [20180622](/linode/idc/singapore/20180622-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180622")
    * [20180804](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")
    * [20180918](/linode/idc/singapore/20180918-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180527-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [Vultr](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")



本文最初发表于[多地到Linode新加坡[Singapore]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-linode-idc-singapore.html)
