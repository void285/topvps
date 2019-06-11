#  多地到Linode纽瓦克[Newark]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode纽瓦克\[Newark\]机房的Ping测试（20180804）](/images/thumbnails/to_linode_Newark.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-纽瓦克机房](https://vps123.top/linode-facilities.html#newark)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-纽瓦克机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180804-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5390个有效测试样本中，共有超时点36个；响应均值为276毫秒，最快的三地区为广东、海南、广西，最慢的三地区为吉林、新疆、西藏；江苏、浙江、江西、贵州、上海等8处有响应超时情况；天津、安徽、内蒙古、西藏、福建等7处丢包率较高。海外19个国家地区的231个有效测试样本中，无超时点；响应均值为179毫秒，最快的三地区为加拿大、荷兰、巴西，最慢的三地区为印度尼西亚、马来西亚、菲律宾；菲律宾丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于纽瓦克市\[\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_idc_linode_usa-newark_20180804_mainland.png)

大陆各省份到Linode美国-纽瓦克机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
广东 | 438个 | 0 | 249ms | 2.3% | 福建 | 168个 | 0 | 280ms | 6.1%  
海南 | 48个 | 0 | 260ms | 0.9% | 重庆 | 34个 | 0 | 280ms | 1.6%  
广西 | 228个 | 0 | 262ms | 0.8% | 河南 | 354个 | 0 | 281ms | 3.4%  
湖南 | 262个 | 0 | 262ms | 1.1% | 辽宁 | 220个 | 0 | 281ms | 4.2%  
湖北 | 202个 | 0 | 265ms | 1.9% | 云南 | 130个 | 2个 | 282ms | 1.0%  
浙江 | 240个 | 6个 | 266ms | 3.0% | 山东 | 368个 | 2个 | 283ms | 4.6%  
北京 | 36个 | 0 | 266ms | 2.2% | 甘肃 | 112个 | 0 | 284ms | 2.4%  
贵州 | 160个 | 4个 | 267ms | 1.9% | 上海 | 30个 | 4个 | 284ms | 0.6%  
宁夏 | 32个 | 0 | 270ms | 5.8% | 内蒙古 | 224个 | 0 | 285ms | 7.0%  
山西 | 186个 | 0 | 270ms | 2.3% | 江西 | 138个 | 6个 | 286ms | 3.2%  
青海 | 16个 | 0 | 272ms | 0 | 安徽 | 238个 | 0 | 287ms | 7.9%  
陕西 | 174个 | 0 | 273ms | 1.8% | 天津 | 16个 | 0 | 289ms | 12.3%  
河北 | 240个 | 0 | 275ms | 3.3% | 黑龙江 | 204个 | 0 | 300ms | 5.1%  
江苏 | 340个 | 8个 | 276ms | 4.0% | 吉林 | 96个 | 0 | 300ms | 4.3%  
均值 | 5390个 | 36个 | 276ms | 3.2% | 新疆 | 162个 | 4个 | 308ms | 0.2%  
四川 | 286个 | 0 | 279ms | 1.0% | 西藏 | 8个 | 0 | 409ms | 7.0%  
  
简评：如果你考虑在Linode的纽瓦克市[]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽瓦克市[]的机房的连通状况。到此机房的ping监测点共有5390个，其中超时点36个，平均响应时间为276毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的29个，超过300毫秒的2个；  
超时点较多的省份：上海；  
丢包率较高的省份：天津；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于纽瓦克市\[\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_idc_linode_usa-newark_20180804_overseas.png)

海外线路到Linode美国-纽瓦克机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 15个 | 0 | 27ms | 0 | 香港 | 60个 | 0 | 198ms | 0  
荷兰 | 3个 | 0 | 68ms | 0 | 新加坡 | 15个 | 0 | 209ms | 0  
巴西 | 3个 | 0 | 70ms | 0 | 日本 | 6个 | 0 | 219ms | 2.2%  
意大利 | 3个 | 0 | 72ms | - | 台湾 | 3个 | 0 | 219ms | 0  
美国 | 48个 | 0 | 94ms | 0 | 澳大利亚 | 6个 | 0 | 221ms | 0  
德国 | 9个 | 0 | 95ms | 0 | 韩国 | 21个 | 0 | 225ms | 0  
英国 | 6个 | 0 | 102ms | 0 | 法国 | 3个 | 0 | 234ms | 0  
俄罗斯 | 3个 | 0 | 116ms | - | 印度尼西亚 | 6个 | 0 | 266ms | 0  
均值 | 231个 | 0 | 179ms | 4.4% | 马来西亚 | 12个 | 0 | 279ms | 0.3%  
南非 | 6个 | 0 | 191ms | 1.0% | 菲律宾 | 3个 | 0 | 509ms | 71.0%  
  
简评：如果你考虑在Linode的纽瓦克市[]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽瓦克市[]的机房的连通状况。到此机房的ping监测点共有231个，其中超时点0个，平均响应时间为179毫秒，丢包率为4%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的5个，在100-200毫秒间的4个，在200-300毫秒间的8个，超过300毫秒的1个；  
丢包率较高的国家/地区：菲律宾；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180804 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180804 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180804-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180804")
    * [达拉斯](/linode/idc/dallas/20180804-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180804")
    * [法兰克福](/linode/idc/frankfurt/20180804-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180804")
    * [佛利蒙](/linode/idc/fremont/20180804-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180804")
    * [伦敦](/linode/idc/london/20180804-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180804")
    * [新加坡](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")
    * [东京](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")
  * 到Linode纽瓦克机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/newark/20180514-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180514")
    * [20180527](/linode/idc/newark/20180527-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180527")
    * [20180622](/linode/idc/newark/20180622-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180622")
    * [20180918](/linode/idc/newark/20180918-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180918")



本文最初发表于[多地到Linode纽瓦克[Newark]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-linode-idc-newark.html)
