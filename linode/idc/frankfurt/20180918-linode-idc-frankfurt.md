#  多地到Linode法兰克福[Frankfurt]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode法兰克福\[Frankfurt\]机房的Ping测试（20180918）]()

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[德国-法兰克福机房](https://vps123.top/linode-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180918-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Linode德国-法兰克福机房的PING测试结果，连通概况如下：大陆31个省市的1323个有效测试样本中，共有超时点39个；响应均值为286毫秒，最快的三地区为宁夏、甘肃、天津，最慢的三地区为西藏、重庆、吉林；江苏、湖北、福建、浙江、广东等14处有响应超时情况；天津、上海、吉林、重庆、青海等24处丢包率较高。海外17个国家地区的83个有效测试样本中，无超时点；响应均值为190毫秒，最快的三地区为意大利、德国、加拿大，最慢的三地区为韩国、澳大利亚、菲律宾；菲律宾丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/linode_20180918/plot_idc_linode_germany-frankfurt_20180918_mainland.png)

大陆各省份到Linode德国-法兰克福机房的测速数据 [20180918] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
宁夏 | 6个 | 0 | 214ms | 0 | 四川 | 69个 | 2个 | 288ms | 5.9%  
甘肃 | 31个 | 0 | 233ms | 4.0% | 广西 | 54个 | 0 | 288ms | 7.1%  
天津 | 7个 | 0 | 247ms | 18.2% | 湖北 | 49个 | 6个 | 295ms | 6.0%  
安徽 | 67个 | 0 | 249ms | 1.9% | 广东 | 116个 | 3个 | 296ms | 5.8%  
河北 | 46个 | 0 | 250ms | 7.6% | 云南 | 28个 | 0 | 297ms | 4.0%  
陕西 | 43个 | 0 | 259ms | 3.6% | 新疆 | 31个 | 0 | 299ms | 4.7%  
江苏 | 88个 | 12个 | 269ms | 6.1% | 山东 | 87个 | 1个 | 300ms | 12.0%  
福建 | 43个 | 3个 | 270ms | 5.3% | 河南 | 77个 | 1个 | 303ms | 12.6%  
浙江 | 63个 | 3个 | 271ms | 8.0% | 青海 | 6个 | 0 | 310ms | 12.8%  
内蒙古 | 50个 | 0 | 274ms | 8.4% | 海南 | 14个 | 0 | 313ms | 6.5%  
湖南 | 67个 | 1个 | 276ms | 9.1% | 黑龙江 | 52个 | 0 | 314ms | 11.1%  
上海 | 6个 | 0 | 276ms | 18.2% | 山西 | 52个 | 1个 | 324ms | 11.8%  
江西 | 39个 | 1个 | 281ms | 4.8% | 贵州 | 39个 | 3个 | 332ms | 9.6%  
辽宁 | 55个 | 1个 | 283ms | 11.4% | 西藏 | 3个 | 0 | 337ms | 8.7%  
北京 | 7个 | 0 | 284ms | 11.6% | 重庆 | 8个 | 1个 | 340ms | 17.3%  
均值 | 1323个 | 39个 | 286ms | 7.9% | 吉林 | 20个 | 0 | 345ms | 17.5%  
  
简评：如果你考虑在Linode的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有1323个，其中超时点39个，平均响应时间为286毫秒，丢包率为7%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的22个，超过300毫秒的9个；  
超时点较多的省份：江苏、湖北、重庆；  
丢包率较高的省份：天津、上海、辽宁、北京、山东、河南、青海、黑龙江、山西、重庆、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/linode_20180918/plot_idc_linode_germany-frankfurt_20180918_overseas.png)

海外线路到Linode德国-法兰克福机房的测速数据 [20180918] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
意大利 | 1个 | 0 | 9ms | - | 台湾 | 2个 | 0 | 194ms | 0  
德国 | 3个 | 0 | 23ms | 0 | 赞比亚 | 2个 | 0 | 205ms | 2.0%  
加拿大 | 3个 | 0 | 86ms | 0 | 越南 | 2个 | 0 | 213ms | 0  
荷兰 | 1个 | 0 | 93ms | 0 | 马来西亚 | 6个 | 0 | 218ms | 0  
俄罗斯 | 2个 | 0 | 142ms | 0 | 日本 | 3个 | 0 | 257ms | 0.3%  
美国 | 15个 | 0 | 150ms | 0 | 印度尼西亚 | 1个 | 0 | 268ms | 3.3%  
新加坡 | 5个 | 0 | 167ms | 0 | 韩国 | 12个 | 0 | 275ms | 0  
香港 | 21个 | 0 | 185ms | 0 | 澳大利亚 | 2个 | 0 | 326ms | 0  
均值 | 83个 | 0 | 190ms | 2.4% | 菲律宾 | 2个 | 0 | 416ms | 32.2%  
  
简评：如果你考虑在Linode的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有83个，其中超时点0个，平均响应时间为190毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的2个，在100-200毫秒间的5个，在200-300毫秒间的6个，超过300毫秒的2个；  
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
    * [佛利蒙](/linode/idc/fremont/20180918-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180918")
    * [伦敦](/linode/idc/london/20180918-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180918")
    * [纽瓦克](/linode/idc/newark/20180918-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180918")
    * [新加坡](/linode/idc/singapore/20180918-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180918")
    * [东京](/linode/idc/tokyo/20180918-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180918")
  * 到Linode法兰克福机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/frankfurt/20180514-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180514")
    * [20180527](/linode/idc/frankfurt/20180527-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180527")
    * [20180622](/linode/idc/frankfurt/20180622-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180622")
    * [20180804](/linode/idc/frankfurt/20180804-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180804")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180918-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
    * [Vultr](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")



本文最初发表于[多地到Linode法兰克福[Frankfurt]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-linode-idc-frankfurt.html)
