#  多地到Vultr悉尼[Sydney]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr悉尼\[Sydney\]机房的Ping测试（20180527）](/images/thumbnails/to_vultr_Sydney.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[澳大利亚-悉尼机房](https://vps123.top/vultr-facilities.html#sydney)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的澳大利亚-悉尼机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180527-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的974个有效测试样本中，共有超时点13个；响应均值为316毫秒，最快的三地区为北京、广东、上海，最慢的三地区为新疆、甘肃、吉林；江苏、湖北、北京、广东、浙江等10处有响应超时情况；上海、北京、浙江、四川、江苏等29处丢包率较高。海外21个国家地区的85个有效测试样本中，无超时点；响应均值为245毫秒，最快的三地区为澳大利亚、日本、美国，最慢的三地区为俄罗斯、巴西、南非；韩国丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_australia-sydney_20180527_mainland.png)

大陆各省份到Vultr澳大利亚-悉尼机房的测速数据 [20180527] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 8个 | 1个 | 282ms | 18.6% | 陕西 | 35个 | 0 | 314ms | 12.2%  
广东 | 80个 | 1个 | 288ms | 12.9% | 辽宁 | 40个 | 0 | 316ms | 13.8%  
上海 | 8个 | 0 | 292ms | 29.2% | 均值 | 974个 | 13个 | 316ms | 13.0%  
天津 | 5个 | 0 | 293ms | 12.0% | 江苏 | 62个 | 3个 | 318ms | 15.5%  
湖南 | 44个 | 0 | 294ms | 10.6% | 贵州 | 27个 | 0 | 324ms | 12.0%  
山西 | 37个 | 0 | 300ms | 8.4% | 湖北 | 45个 | 2个 | 324ms | 14.9%  
浙江 | 51个 | 1个 | 304ms | 16.3% | 云南 | 20个 | 0 | 325ms | 14.0%  
福建 | 36个 | 1个 | 305ms | 12.3% | 重庆 | 13个 | 1个 | 326ms | 13.8%  
江西 | 24个 | 0 | 305ms | 13.8% | 宁夏 | 13个 | 0 | 330ms | 9.1%  
黑龙江 | 39个 | 0 | 306ms | 9.9% | 内蒙古 | 33个 | 0 | 331ms | 12.4%  
广西 | 41个 | 0 | 307ms | 12.1% | 河北 | 34个 | 0 | 335ms | 10.8%  
山东 | 53个 | 1个 | 309ms | 11.5% | 四川 | 46个 | 1个 | 346ms | 15.8%  
安徽 | 38个 | 0 | 310ms | 15.1% | 新疆 | 27个 | 0 | 347ms | 10.1%  
海南 | 14个 | 0 | 310ms | 15.0% | 甘肃 | 22个 | 0 | 348ms | 13.8%  
河南 | 57个 | 1个 | 313ms | 11.9% | 吉林 | 19个 | 0 | 382ms | 15.2%  
青海 | 3个 | 0 | 313ms | 5.0% |  |  |  |  |   
  
简评：如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有974个，其中超时点13个，平均响应时间为316毫秒，丢包率为13%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的6个，超过300毫秒的24个；  
超时点较多的省份：北京；  
丢包率较高的省份：北京、广东、上海、天津、湖南、浙江、福建、江西、广西、山东、安徽、海南、河南、陕西、辽宁、江苏、贵州、湖北、云南、重庆、内蒙古、河北、四川、新疆、甘肃、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_australia-sydney_20180527_overseas.png)

海外线路到Vultr澳大利亚-悉尼机房的测速数据 [20180527] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
澳大利亚 | 2个 | 0 | 5ms | 0 | 越南 | 2个 | 0 | 247ms | 1.0%  
日本 | 2个 | 0 | 121ms | 1.0% | 菲律宾 | 1个 | 0 | 275ms | 0  
美国 | 21个 | 0 | 166ms | 4.3% | 法国 | 1个 | 0 | 291ms | 0  
香港 | 17个 | 0 | 169ms | 0 | 意大利 | 1个 | 0 | 294ms | -  
台湾 | 1个 | 0 | 181ms | - | 荷兰 | 1个 | 0 | 299ms | 0  
韩国 | 12个 | 0 | 185ms | 5.7% | 德国 | 3个 | 0 | 308ms | 0  
印度尼西亚 | 1个 | 0 | 198ms | 0 | 英国 | 2个 | 0 | 311ms | 0  
新加坡 | 5个 | 0 | 200ms | 0 | 柬埔寨 | 1个 | 0 | 316ms | 0  
马来西亚 | 5个 | 0 | 202ms | 0 | 俄罗斯 | 1个 | 0 | 333ms | 0  
加拿大 | 3个 | 0 | 228ms | 0 | 巴西 | 1个 | 0 | 337ms | 0  
均值 | 85个 | 0 | 245ms | 0.7% | 南非 | 2个 | 0 | 473ms | 0.5%  
  
简评：如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有85个，其中超时点0个，平均响应时间为245毫秒，丢包率为0%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的7个，在200-300毫秒间的7个，超过300毫秒的6个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180527 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180527 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180527-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180527")
    * [亚特兰大](/vultr/idc/atlanta/20180527-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180527")
    * [芝加哥](/vultr/idc/chicago/20180527-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180527")
    * [达拉斯](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")
    * [法兰克福](/vultr/idc/frankfurt/20180527-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180527")
    * [伦敦](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")
    * [洛杉矶](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [迈阿密](/vultr/idc/miami/20180527-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180527")
    * [新泽西](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [巴黎](/vultr/idc/paris/20180527-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180527")
    * [西雅图](/vultr/idc/seattle/20180527-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180527")
    * [硅谷](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [新加坡](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")
    * [东京](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
  * 到Vultr悉尼机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [20180622](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [20180804](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [20180918](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")



本文最初发表于[多地到Vultr悉尼[Sydney]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-vultr-idc-sydney.html)
