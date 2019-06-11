#  多地到Vultr洛杉矶[LosAngeles]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr洛杉矶\[LosAngeles\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_LosAngeles.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-洛杉矶机房](https://vps123.top/vultr-facilities.html#losangeles)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-洛杉矶机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的3120个有效测试样本中，共有超时点44个；响应均值为221毫秒，最快的三地区为广东、北京、湖南，最慢的三地区为新疆、宁夏、西藏；浙江、江苏、湖北、上海、广东等9处有响应超时情况；上海、宁夏、福建、甘肃、安徽等7处丢包率较高。海外19个国家地区的210个有效测试样本中，共有超时点6个；响应均值为164毫秒，最快的三地区为荷兰、美国、加拿大，最慢的三地区为马来西亚、印度尼西亚、菲律宾；香港有响应超时情况；菲律宾、美国丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-losangeles_20180804_mainland.png)

**大陆各省份到Vultr美国-洛杉矶机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
广东 | 277个 | 3个 | 195ms | 1.2%  
北京 | 32个 | 0 | 198ms | 2.9%  
湖南 | 141个 | 3个 | 202ms | 1.6%  
山东 | 186个 | 0 | 203ms | 1.3%  
海南 | 28个 | 0 | 203ms | 2.1%  
青海 | 8个 | 0 | 209ms | 0  
湖北 | 113个 | 6个 | 210ms | 2.2%  
天津 | 20个 | 0 | 210ms | 3.1%  
广西 | 124个 | 0 | 210ms | 1.9%  
河南 | 191个 | 0 | 211ms | 3.7%  
浙江 | 158个 | 10个 | 214ms | 3.2%  
上海 | 31个 | 4个 | 214ms | 9.4%  
江苏 | 235个 | 9个 | 215ms | 3.6%  
河北 | 128个 | 0 | 215ms | 4.5%  
贵州 | 94个 | 0 | 221ms | 1.9%  
均值 | 3120个 | 44个 | 221ms | 3.3%  
重庆 | 41个 | 3个 | 222ms | 3.0%  
山西 | 109个 | 0 | 225ms | 2.4%  
辽宁 | 154个 | 0 | 225ms | 5.5%  
陕西 | 101个 | 3个 | 227ms | 2.6%  
安徽 | 115个 | 3个 | 227ms | 6.4%  
云南 | 67个 | 0 | 228ms | 6.2%  
黑龙江 | 112个 | 0 | 230ms | 2.8%  
四川 | 169个 | 0 | 232ms | 1.8%  
福建 | 92个 | 0 | 236ms | 6.8%  
内蒙古 | 104个 | 0 | 237ms | 3.9%  
吉林 | 60个 | 0 | 241ms | 4.5%  
江西 | 75个 | 0 | 257ms | 4.6%  
甘肃 | 60个 | 0 | 270ms | 6.7%  
新疆 | 75个 | 0 | 275ms | 3.3%  
宁夏 | 16个 | 0 | 289ms | 8.8%  
西藏 | 4个 | 0 | 383ms | 2.0%  
  
**简评：** 如果你考虑在Vultr的洛杉矶[LosAngeles]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有3120个，其中超时点44个，平均响应时间为221毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的2个，在200-300毫秒间的28个，超过300毫秒的1个；  
超时点较多的省份：上海；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-losangeles_20180804_overseas.png)

**海外线路到Vultr美国-洛杉矶机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
荷兰 | 3个 | 0 | 11ms | 0  
美国 | 45个 | 0 | 35ms | 7.6%  
加拿大 | 9个 | 0 | 74ms | 0  
意大利 | 3个 | 0 | 132ms | -  
巴西 | 3个 | 0 | 140ms | 0  
新加坡 | 15个 | 0 | 140ms | 0  
日本 | 3个 | 0 | 141ms | 3.0%  
韩国 | 21个 | 0 | 147ms | 0  
德国 | 6个 | 0 | 151ms | 0  
法国 | 3个 | 0 | 156ms | 0  
香港 | 66个 | 6个 | 161ms | 0  
均值 | 210个 | 6个 | 164ms | 4.0%  
澳大利亚 | 3个 | 0 | 165ms | 0  
南非 | 6个 | 0 | 175ms | 0  
英国 | 3个 | 0 | 176ms | 0  
俄罗斯 | 3个 | 0 | 179ms | -  
台湾 | 3个 | 0 | 194ms | 0  
马来西亚 | 9个 | 0 | 214ms | 0  
印度尼西亚 | 3个 | 0 | 229ms | 1.0%  
菲律宾 | 3个 | 0 | 495ms | 56.0%  
  
**简评：** 如果你考虑在Vultr的洛杉矶[LosAngeles]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有210个，其中超时点6个，平均响应时间为164毫秒，丢包率为4%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的1个，在100-200毫秒间的13个，在200-300毫秒间的2个，超过300毫秒的1个；  
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
    * [迈阿密](/vultr/idc/miami/20180804-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180804")
    * [新泽西](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr洛杉矶机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/losangeles/20180514-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180514")
    * [20180527](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [20180622](/vultr/idc/losangeles/20180622-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180622")
    * [20180918](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
  * 本期报告：在洛杉矶部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/losangeles/20180804-bwg-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180804")



本文最初发表于[多地到Vultr洛杉矶[LosAngeles]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-losangeles.html)
