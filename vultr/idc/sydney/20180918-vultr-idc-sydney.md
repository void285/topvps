#  多地到Vultr悉尼[Sydney]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr悉尼\[Sydney\]机房的Ping测试（20180918）](/images/thumbnails/to_vultr_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[澳大利亚-悉尼机房](https://vps123.top/vultr-facilities.html#sydney)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的澳大利亚-悉尼机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180918-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Vultr澳大利亚-悉尼机房的PING测试结果，连通概况如下：大陆31个省市的1410个有效测试样本中，共有超时点12个；响应均值为272毫秒，最快的三地区为广西、陕西、上海，最慢的三地区为西藏、宁夏、青海；江苏、浙江、江西、广东、山西等6处有响应超时情况；山东、河南丢包率较高。海外17个国家地区的81个有效测试样本中，共有超时点1个；响应均值为244毫秒，最快的三地区为澳大利亚、日本、新加坡，最慢的三地区为俄罗斯、菲律宾、赞比亚；韩国有响应超时情况；菲律宾、赞比亚、印度尼西亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_australia-sydney_20180918_mainland.png)

**大陆各省份到Vultr澳大利亚-悉尼机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
广西 | 62个 | 0 | 244ms | 0.5%  
陕西 | 43个 | 0 | 245ms | 0.2%  
上海 | 7个 | 0 | 249ms | 4.7%  
天津 | 7个 | 0 | 250ms | 4.9%  
江西 | 42个 | 1个 | 256ms | 0.2%  
浙江 | 65个 | 2个 | 257ms | 0.9%  
安徽 | 66个 | 0 | 257ms | 0.2%  
广东 | 119个 | 1个 | 261ms | 0.8%  
湖南 | 65个 | 0 | 261ms | 0.6%  
辽宁 | 61个 | 0 | 264ms | 0.6%  
河南 | 88个 | 0 | 267ms | 5.1%  
山东 | 91个 | 0 | 268ms | 7.2%  
河北 | 60个 | 0 | 269ms | 3.6%  
福建 | 43个 | 0 | 270ms | 1.9%  
海南 | 14个 | 0 | 270ms | 0.3%  
内蒙古 | 55个 | 0 | 272ms | 1.6%  
山西 | 57个 | 1个 | 272ms | 0.2%  
均值 | 1410个 | 12个 | 272ms | 1.7%  
黑龙江 | 53个 | 0 | 273ms | 2.8%  
吉林 | 22个 | 0 | 273ms | 0.1%  
江苏 | 92个 | 6个 | 274ms | 1.1%  
重庆 | 8个 | 0 | 275ms | 0  
北京 | 8个 | 0 | 281ms | 3.3%  
云南 | 32个 | 0 | 285ms | 0.2%  
贵州 | 43个 | 1个 | 293ms | 0.5%  
四川 | 73个 | 0 | 298ms | 1.4%  
湖北 | 52个 | 0 | 306ms | 0.5%  
新疆 | 36个 | 0 | 310ms | 2.2%  
甘肃 | 32个 | 0 | 312ms | 0.3%  
西藏 | 2个 | 0 | 323ms | 1.5%  
宁夏 | 6个 | 0 | 326ms | 0  
青海 | 6个 | 0 | 340ms | 0.2%  
  
**简评：** 如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有1410个，其中超时点12个，平均响应时间为272毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的25个，超过300毫秒的6个；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_australia-sydney_20180918_overseas.png)

**海外线路到Vultr澳大利亚-悉尼机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
澳大利亚 | 2个 | 0 | 20ms | 0  
日本 | 3个 | 0 | 139ms | 0.3%  
新加坡 | 5个 | 0 | 162ms | 0  
美国 | 15个 | 0 | 164ms | 0  
韩国 | 12个 | 1个 | 188ms | 0  
马来西亚 | 6个 | 0 | 188ms | 0.5%  
台湾 | 2个 | 0 | 188ms | 0  
香港 | 20个 | 0 | 216ms | 0  
加拿大 | 3个 | 0 | 227ms | 0  
均值 | 81个 | 1个 | 244ms | 3.0%  
印度尼西亚 | 1个 | 0 | 288ms | 6.7%  
越南 | 2个 | 0 | 294ms | 0  
意大利 | 1个 | 0 | 294ms | -  
荷兰 | 1个 | 0 | 295ms | 0  
德国 | 3个 | 0 | 312ms | 0  
俄罗斯 | 1个 | 0 | 337ms | -  
菲律宾 | 2个 | 0 | 356ms | 28.3%  
赞比亚 | 2个 | 0 | 490ms | 8.7%  
  
**简评：** 如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有81个，其中超时点1个，平均响应时间为244毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的6个，在200-300毫秒间的6个，超过300毫秒的4个；  
丢包率较高的国家/地区：菲律宾；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180918 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180918 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180918-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180918")
    * [亚特兰大](/vultr/idc/atlanta/20180918-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180918")
    * [芝加哥](/vultr/idc/chicago/20180918-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180918")
    * [达拉斯](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
    * [法兰克福](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")
    * [伦敦](/vultr/idc/london/20180918-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180918")
    * [洛杉矶](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
    * [迈阿密](/vultr/idc/miami/20180918-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180918")
    * [新泽西](/vultr/idc/newjersey/20180918-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180918")
    * [巴黎](/vultr/idc/paris/20180918-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180918")
    * [西雅图](/vultr/idc/seattle/20180918-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180918")
    * [硅谷](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")
    * [新加坡](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")
    * [东京](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 到Vultr悉尼机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [20180527](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [20180622](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [20180804](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")



本文最初发表于[多地到Vultr悉尼[Sydney]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-vultr-idc-sydney.html)
