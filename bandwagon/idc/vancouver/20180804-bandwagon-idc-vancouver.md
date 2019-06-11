#  多地到BandwagonHost温哥华[Vancouver]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到BandwagonHost温哥华\[Vancouver\]机房的Ping测试（20180804）](/images/thumbnails/to_bwg_Vancouver.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[BandwagonHost](https://vps123.top/go/bwg)的[加拿大-温哥华机房](https://vps123.top/bandwagon-facilities.html#vancouver)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[BandwagonHost](https://vps123.top/go/bwg)的加拿大-温哥华机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[BandwagonHost全部机房](/bandwagon/isp/china/20180804-bandwagon-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆21个省市的389个有效测试样本中，共有超时点48个；响应均值为208毫秒，最快的三地区为湖北、江西、河南，最慢的三地区为湖南、安徽、山西；江苏、陕西、浙江、上海、湖北等9处有响应超时情况；辽宁、福建、浙江、江苏丢包率较高。海外13个国家地区的168个有效测试样本中，无超时点；响应均值为126毫秒，最快的三地区为南非、荷兰、加拿大，最慢的三地区为法国、俄罗斯、韩国。

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商BandwagonHost位于温哥华\[Vancouver\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/bwg_20180804/plot_idc_bwg_canada-vancouver_20180804_mainland.png)

**大陆各省份到BandwagonHost加拿大-温哥华机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
湖北 | 13个 | 3个 | 152ms | 0  
江西 | 7个 | 0 | 161ms | 0  
河南 | 7个 | 0 | 172ms | 0  
山东 | 10个 | 3个 | 176ms | 0  
贵州 | 23个 | 0 | 190ms | 0  
广西 | 11个 | 0 | 192ms | 5.0%  
福建 | 24个 | 3个 | 193ms | 20.0%  
重庆 | 13个 | 3个 | 198ms | 0  
北京 | 16个 | 0 | 198ms | 0  
江苏 | 71个 | 15个 | 206ms | 8.8%  
均值 | 389个 | 48个 | 208ms | 7.1%  
广东 | 49个 | 0 | 209ms | 5.0%  
四川 | 13个 | 3个 | 213ms | 0  
陕西 | 14个 | 7个 | 215ms | 0  
辽宁 | 19个 | 0 | 240ms | 50.0%  
上海 | 11个 | 4个 | 245ms | 0  
浙江 | 58个 | 7个 | 255ms | 10.0%  
新疆 | 3个 | 0 | - | -  
云南 | 3个 | 0 | - | -  
湖南 | 9个 | 0 | - | -  
安徽 | 6个 | 0 | - | -  
山西 | 9个 | 0 | - | -  
  
**简评：** 如果你考虑在BandwagonHost的温哥华[Vancouver]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于温哥华[Vancouver]的机房的连通状况。到此机房的ping监测点共有389个，其中超时点48个，平均响应时间为208毫秒，丢包率为7%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在100-200毫秒间的9个，在200-300毫秒间的7个；  
超时点较多的省份：湖北、山东、福建、重庆、江苏、四川、陕西、上海、浙江；  
丢包率较高的省份：福建、辽宁、浙江；

## 海外测速点

![海外各国家地区到VPS提供商BandwagonHost位于温哥华\[Vancouver\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/bwg_20180804/plot_idc_bwg_canada-vancouver_20180804_overseas.png)

**海外线路到BandwagonHost加拿大-温哥华机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
南非 | 3个 | 0 | 30ms | 0  
荷兰 | 3个 | 0 | 43ms | 0  
加拿大 | 3个 | 0 | 69ms | -  
美国 | 42个 | 0 | 73ms | 0  
均值 | 168个 | 0 | 126ms | 0  
巴西 | 3个 | 0 | 133ms | 0  
意大利 | 3个 | 0 | 138ms | -  
德国 | 3个 | 0 | 140ms | -  
新加坡 | 12个 | 0 | 148ms | 0  
台湾 | 3个 | 0 | 155ms | 0  
香港 | 66个 | 0 | 157ms | 0  
法国 | 3个 | 0 | 175ms | 0  
俄罗斯 | 3个 | 0 | 186ms | -  
韩国 | 21个 | 0 | 194ms | 0  
  
**简评：** 如果你考虑在BandwagonHost的温哥华[Vancouver]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于温哥华[Vancouver]的机房的连通状况。到此机房的ping监测点共有168个，其中超时点0个，平均响应时间为126毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的2个，在100-200毫秒间的9个；

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [BandwagonHost](https://vps123.top/pingtests/idc-bandwagon/20180804 "本期BandwagonHost的全部测速报告")
    * [各地到BandwagonHost某机房](https://vps123.top/pingtests/idc-bandwagon/isp-global/20180804 "以BandwagonHost某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到BandwagonHost各机房](https://vps123.top/pingtests/idc-bandwagon/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较BandwagonHost各机房")
  * 本期到BandwagonHost _其他机房_ 的报告： 
    * [阿姆斯特丹](/bandwagon/idc/amsterdam/20180804-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180804")
    * [佛罗里达](/bandwagon/idc/florida/20180804-bandwagon-idc-florida.md "多地到BandwagonHost佛罗里达机房的Ping测试 20180804")
    * [佛利蒙](/bandwagon/idc/fremont/20180804-bandwagon-idc-fremont.md "多地到BandwagonHost佛利蒙机房的Ping测试 20180804")
    * [香港](/bandwagon/idc/hongkong/20180804-bandwagon-idc-hongkong.md "多地到BandwagonHost香港机房的Ping测试 20180804")
    * [洛杉矶](/bandwagon/idc/losangeles/20180804-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180804")
    * [纽约](/bandwagon/idc/newyork/20180804-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180804")
    * [凤凰城](/bandwagon/idc/phoenix/20180804-bandwagon-idc-phoenix.md "多地到BandwagonHost凤凰城机房的Ping测试 20180804")
  * 到BandwagonHost温哥华机房的 _其他近期报告_ ： 
    * [20180514](/bandwagon/idc/vancouver/20180514-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180514")
    * [20180527](/bandwagon/idc/vancouver/20180527-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180527")
    * [20180622](/bandwagon/idc/vancouver/20180622-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180622")
    * [20180918](/bandwagon/idc/vancouver/20180918-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180918")



本文最初发表于[多地到BandwagonHost温哥华[Vancouver]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-bandwagon-idc-vancouver.html)
