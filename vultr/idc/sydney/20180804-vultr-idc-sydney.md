#  多地到Vultr悉尼[Sydney]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr悉尼\[Sydney\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_Sydney.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[澳大利亚-悉尼机房](https://vps123.top/vultr-facilities.html#sydney)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的澳大利亚-悉尼机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的3089个有效测试样本中，共有超时点83个；响应均值为320毫秒，最快的三地区为湖南、广东、上海，最慢的三地区为吉林、宁夏、新疆；江苏、浙江、广东、上海、贵州等9处有响应超时情况；宁夏、天津、安徽、福建、江西等30处丢包率较高。海外19个国家地区的210个有效测试样本中，无超时点；响应均值为225毫秒，最快的三地区为法国、澳大利亚、日本，最慢的三地区为南非、俄罗斯、菲律宾；菲律宾丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_australia-sydney_20180804_mainland.png)

大陆各省份到Vultr澳大利亚-悉尼机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
湖南 | 125个 | 0 | 255ms | 6.9% | 陕西 | 97个 | 0 | 317ms | 16.1%  
广东 | 274个 | 9个 | 256ms | 4.4% | 湖北 | 113个 | 0 | 318ms | 10.3%  
上海 | 27个 | 4个 | 265ms | 12.1% | 均值 | 3089个 | 83个 | 320ms | 15.9%  
重庆 | 41个 | 0 | 283ms | 12.7% | 天津 | 16个 | 0 | 324ms | 34.8%  
北京 | 36个 | 0 | 288ms | 21.2% | 云南 | 63个 | 0 | 325ms | 10.5%  
西藏 | 4个 | 0 | 290ms | 14.0% | 安徽 | 104个 | 0 | 342ms | 28.2%  
海南 | 28个 | 0 | 292ms | 7.0% | 江苏 | 238个 | 33个 | 344ms | 25.1%  
广西 | 124个 | 0 | 297ms | 8.4% | 山西 | 109个 | 0 | 352ms | 18.4%  
贵州 | 98个 | 3个 | 300ms | 14.4% | 四川 | 157个 | 0 | 359ms | 8.7%  
河北 | 132个 | 0 | 306ms | 14.5% | 内蒙古 | 104个 | 0 | 369ms | 19.4%  
河南 | 195个 | 3个 | 307ms | 14.2% | 甘肃 | 60个 | 0 | 372ms | 20.3%  
山东 | 190个 | 3个 | 308ms | 12.9% | 辽宁 | 146个 | 0 | 376ms | 21.1%  
浙江 | 162个 | 22个 | 310ms | 24.0% | 青海 | 8个 | 0 | 382ms | 21.0%  
黑龙江 | 116个 | 0 | 310ms | 12.9% | 吉林 | 60个 | 0 | 385ms | 21.3%  
江西 | 75个 | 0 | 311ms | 25.3% | 宁夏 | 16个 | 0 | 387ms | 35.3%  
福建 | 92个 | 3个 | 315ms | 27.5% | 新疆 | 79个 | 3个 | 390ms | 18.4%  
  
简评：如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有3089个，其中超时点83个，平均响应时间为320毫秒，丢包率为15%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的9个，超过300毫秒的22个；  
超时点较多的省份：上海、浙江、江苏；  
丢包率较高的省份：上海、重庆、北京、西藏、贵州、河北、河南、山东、浙江、黑龙江、江西、福建、陕西、湖北、天津、云南、安徽、江苏、山西、内蒙古、甘肃、辽宁、青海、吉林、宁夏、新疆；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_australia-sydney_20180804_overseas.png)

海外线路到Vultr澳大利亚-悉尼机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
法国 | 3个 | 0 | 0 | 0 | 均值 | 210个 | 0 | 225ms | 4.0%  
澳大利亚 | 3个 | 0 | 8ms | 0 | 加拿大 | 9个 | 0 | 228ms | 0  
日本 | 3个 | 0 | 134ms | 0 | 印度尼西亚 | 3个 | 0 | 259ms | 0  
新加坡 | 15个 | 0 | 146ms | 0 | 巴西 | 3个 | 0 | 292ms | 0  
韩国 | 21个 | 0 | 157ms | 0 | 意大利 | 3个 | 0 | 295ms | -  
台湾 | 3个 | 0 | 170ms | 0 | 德国 | 6个 | 0 | 309ms | 0  
荷兰 | 3个 | 0 | 172ms | 0 | 英国 | 3个 | 0 | 311ms | 1.0%  
美国 | 48个 | 0 | 177ms | 0 | 南非 | 6个 | 0 | 333ms | 2.0%  
香港 | 63个 | 0 | 193ms | 0 | 俄罗斯 | 3个 | 0 | 361ms | -  
马来西亚 | 9个 | 0 | 209ms | 0.3% | 菲律宾 | 3个 | 0 | 536ms | 65.0%  
  
简评：如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有210个，其中超时点0个，平均响应时间为225毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在100-200毫秒间的7个，在200-300毫秒间的5个，超过300毫秒的5个；  
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
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr悉尼机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [20180527](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [20180622](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [20180918](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")



本文最初发表于[多地到Vultr悉尼[Sydney]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-sydney.html)
