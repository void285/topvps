#  多地到Vultr巴黎[Paris]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr巴黎\[Paris\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_Paris.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[法国-巴黎机房](https://vps123.top/vultr-facilities.html#paris)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的法国-巴黎机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的3157个有效测试样本中，共有超时点36个；响应均值为294毫秒，最快的三地区为青海、宁夏、河北，最慢的三地区为江西、安徽、西藏；江苏、浙江、广东、广西、上海等7处有响应超时情况；西藏、云南、上海、河北丢包率较高。海外18个国家地区的213个有效测试样本中，无超时点；响应均值为187毫秒，最快的三地区为巴西、意大利、德国，最慢的三地区为台湾、澳大利亚、菲律宾；菲律宾丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于巴黎\[Paris\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_france-paris_20180804_mainland.png)

**大陆各省份到Vultr法国-巴黎机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
青海 | 8个 | 0 | 220ms | 0  
宁夏 | 16个 | 0 | 239ms | 1.5%  
河北 | 128个 | 0 | 259ms | 5.1%  
辽宁 | 154个 | 0 | 261ms | 2.0%  
天津 | 16个 | 0 | 264ms | 0  
重庆 | 41个 | 3个 | 265ms | 3.3%  
甘肃 | 60个 | 0 | 265ms | 2.1%  
广西 | 128个 | 4个 | 266ms | 2.8%  
河南 | 199个 | 0 | 269ms | 3.0%  
陕西 | 97个 | 0 | 273ms | 2.9%  
北京 | 36个 | 0 | 279ms | 1.3%  
内蒙古 | 104个 | 0 | 279ms | 1.9%  
湖南 | 133个 | 3个 | 281ms | 4.3%  
新疆 | 79个 | 0 | 282ms | 2.2%  
湖北 | 121个 | 0 | 287ms | 3.5%  
四川 | 165个 | 0 | 293ms | 1.4%  
云南 | 67个 | 0 | 294ms | 7.1%  
吉林 | 64个 | 0 | 294ms | 0.6%  
均值 | 3157个 | 36个 | 294ms | 2.9%  
山西 | 109个 | 0 | 297ms | 1.4%  
黑龙江 | 100个 | 0 | 303ms | 3.4%  
江苏 | 238个 | 9个 | 308ms | 2.4%  
贵州 | 94个 | 0 | 310ms | 4.4%  
山东 | 214个 | 0 | 315ms | 1.5%  
福建 | 88个 | 0 | 315ms | 4.9%  
浙江 | 174个 | 7个 | 315ms | 3.7%  
广东 | 282个 | 6个 | 315ms | 2.6%  
海南 | 28个 | 0 | 316ms | 2.3%  
上海 | 31个 | 4个 | 324ms | 5.6%  
江西 | 75个 | 0 | 340ms | 3.9%  
安徽 | 104个 | 0 | 348ms | 4.1%  
西藏 | 4个 | 0 | 427ms | 9.0%  
  
**简评：** 如果你考虑在Vultr的巴黎[Paris]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于巴黎[Paris]的机房的连通状况。到此机房的ping监测点共有3157个，其中超时点36个，平均响应时间为294毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的19个，超过300毫秒的12个；  
超时点较多的省份：上海；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于巴黎\[Paris\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_france-paris_20180804_overseas.png)

**海外线路到Vultr法国-巴黎机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
巴西 | 3个 | 0 | 8ms | 0  
意大利 | 3个 | 0 | 8ms | -  
德国 | 6个 | 0 | 25ms | 0  
英国 | 3个 | 0 | 52ms | 0  
俄罗斯 | 3个 | 0 | 52ms | -  
加拿大 | 12个 | 0 | 94ms | 0  
荷兰 | 3个 | 0 | 146ms | 0  
美国 | 48个 | 0 | 159ms | 0  
南非 | 6个 | 0 | 179ms | 1.0%  
均值 | 213个 | 0 | 187ms | 4.1%  
香港 | 66个 | 0 | 196ms | 0  
新加坡 | 15个 | 0 | 197ms | 0  
马来西亚 | 9个 | 0 | 258ms | 0  
日本 | 3个 | 0 | 264ms | 0  
印度尼西亚 | 3个 | 0 | 268ms | 0  
韩国 | 21个 | 0 | 282ms | 0  
台湾 | 3个 | 0 | 284ms | 0  
澳大利亚 | 3个 | 0 | 308ms | 0  
菲律宾 | 3个 | 0 | 596ms | 65.0%  
  
**简评：** 如果你考虑在Vultr的巴黎[Paris]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于巴黎[Paris]的机房的连通状况。到此机房的ping监测点共有213个，其中超时点0个，平均响应时间为187毫秒，丢包率为4%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的3个，在100-200毫秒间的5个，在200-300毫秒间的5个，超过300毫秒的2个；  
丢包率较高的国家/地区：菲律宾；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180804 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180804 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180804-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180804")
    * [亚特兰大](/vultr/idc/atlanta/20180804-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180804")
    * [芝加哥](/vultr/idc/chicago/20180804-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180804")
    * [达拉斯](/vultr/idc/dallas/20180804-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180804")
    * [法兰克福](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")
    * [伦敦](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")
    * [洛杉矶](/vultr/idc/losangeles/20180804-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180804")
    * [迈阿密](/vultr/idc/miami/20180804-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180804")
    * [新泽西](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr巴黎机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/paris/20180514-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180514")
    * [20180527](/vultr/idc/paris/20180527-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180527")
    * [20180622](/vultr/idc/paris/20180622-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180622")
    * [20180918](/vultr/idc/paris/20180918-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180918")



本文最初发表于[多地到Vultr巴黎[Paris]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-paris.html)
