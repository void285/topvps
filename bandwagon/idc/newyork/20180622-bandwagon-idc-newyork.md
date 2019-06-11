#  多地到BandwagonHost纽约[NewYork]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到BandwagonHost纽约\[NewYork\]机房的Ping测试（20180622）](/images/thumbnails/to_bwg_NewYork.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[BandwagonHost](https://vps123.top/go/bwg)的[美国-纽约机房](https://vps123.top/bandwagon-facilities.html#newyork)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[BandwagonHost](https://vps123.top/go/bwg)的美国-纽约机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[BandwagonHost全部机房](/bandwagon/isp/china/20180622-bandwagon-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆29个省市的224个有效测试样本中，共有超时点10个；响应均值为260毫秒，最快的三地区为海南、安徽、北京，最慢的三地区为吉林、新疆、香港；江苏、浙江、山东、上海、云南等7处有响应超时情况；广西、上海、广东、江西、湖南等12处丢包率较高。海外12个国家地区的68个有效测试样本中，共有超时点1个；响应均值为121毫秒，最快的三地区为加拿大、南非、美国，最慢的三地区为新加坡、韩国、台湾；香港有响应超时情况。

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商BandwagonHost位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/bwg_20180622/plot_idc_bwg_usa-newyork_20180622_mainland.png)

大陆各省份到BandwagonHost美国-纽约机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
海南 | 1个 | 0 | 232ms | 0 | 重庆 | 6个 | 0 | 263ms | 6.7%  
安徽 | 6个 | 0 | 245ms | 5.8% | 贵州 | 7个 | 0 | 264ms | 0  
北京 | 7个 | 0 | 246ms | 0 | 湖南 | 6个 | 0 | 264ms | 10.0%  
福建 | 14个 | 0 | 246ms | 5.9% | 黑龙江 | 3个 | 0 | 265ms | 0  
山东 | 6个 | 1个 | 247ms | 0 | 广西 | 5个 | 0 | 266ms | 22.5%  
江苏 | 25个 | 3个 | 247ms | 7.5% | 上海 | 3个 | 1个 | 268ms | 16.7%  
山西 | 5个 | 0 | 247ms | 0 | 内蒙古 | 4个 | 0 | 271ms | 5.0%  
河北 | 2个 | 0 | 254ms | 0 | 云南 | 2个 | 1个 | 272ms | 0  
江西 | 4个 | 0 | 256ms | 10.0% | 广东 | 27个 | 1个 | 274ms | 11.9%  
河南 | 5个 | 0 | 257ms | 0 | 四川 | 6个 | 0 | 275ms | 5.0%  
甘肃 | 1个 | 0 | 257ms | 0 | 湖北 | 6个 | 0 | 276ms | 3.3%  
陕西 | 8个 | 0 | 258ms | 0.6% | 天津 | 1个 | 0 | 284ms | 10.0%  
浙江 | 26个 | 2个 | 260ms | 5.8% | 吉林 | 2个 | 0 | 289ms | 6.7%  
均值 | 224个 | 10个 | 260ms | 5.7% | 新疆 | 2个 | 0 | 301ms | 0  
辽宁 | 9个 | 0 | 262ms | 0 | 香港 | 25个 | 1个 | - | -  
  
简评：如果你考虑在BandwagonHost的纽约[NewYork]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有224个，其中超时点10个，平均响应时间为260毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的27个，超过300毫秒的1个；  
超时点较多的省份：山东、江苏、上海；  
丢包率较高的省份：江西、湖南、广西、上海、广东、天津；

## 海外测速点

![海外各国家地区到VPS提供商BandwagonHost位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/bwg_20180622/plot_idc_bwg_usa-newyork_20180622_overseas.png)

海外线路到BandwagonHost美国-纽约机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 1个 | 0 | 9ms | - | 均值 | 68个 | 1个 | 121ms | 0  
南非 | 1个 | 0 | 60ms | 0 | 日本 | 1个 | 0 | 186ms | -  
美国 | 18个 | 0 | 64ms | 0 | 香港 | 25个 | 1个 | 192ms | 0  
德国 | 1个 | 0 | 74ms | - | 新加坡 | 5个 | 0 | 206ms | 0  
意大利 | 1个 | 0 | 76ms | - | 韩国 | 11个 | 0 | 211ms | 0  
巴西 | 1个 | 0 | 78ms | 0 | 台湾 | 2个 | 0 | 219ms | 0  
法国 | 1个 | 0 | 84ms | 0 |  |  |  |  |   
  
简评：如果你考虑在BandwagonHost的纽约[NewYork]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有68个，其中超时点1个，平均响应时间为121毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的6个，在100-200毫秒间的2个，在200-300毫秒间的3个；

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [BandwagonHost](https://vps123.top/pingtests/idc-bandwagon/20180622 "本期BandwagonHost的全部测速报告")
    * [各地到BandwagonHost某机房](https://vps123.top/pingtests/idc-bandwagon/isp-global/20180622 "以BandwagonHost某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到BandwagonHost各机房](https://vps123.top/pingtests/idc-bandwagon/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较BandwagonHost各机房")
  * 本期到BandwagonHost _其他机房_ 的报告： 
    * [阿姆斯特丹](/bandwagon/idc/amsterdam/20180622-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180622")
    * [佛罗里达](/bandwagon/idc/florida/20180622-bandwagon-idc-florida.md "多地到BandwagonHost佛罗里达机房的Ping测试 20180622")
    * [佛利蒙](/bandwagon/idc/fremont/20180622-bandwagon-idc-fremont.md "多地到BandwagonHost佛利蒙机房的Ping测试 20180622")
    * [香港](/bandwagon/idc/hongkong/20180622-bandwagon-idc-hongkong.md "多地到BandwagonHost香港机房的Ping测试 20180622")
    * [洛杉矶](/bandwagon/idc/losangeles/20180622-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180622")
    * [凤凰城](/bandwagon/idc/phoenix/20180622-bandwagon-idc-phoenix.md "多地到BandwagonHost凤凰城机房的Ping测试 20180622")
    * [温哥华](/bandwagon/idc/vancouver/20180622-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180622")
  * 到BandwagonHost纽约机房的 _其他近期报告_ ： 
    * [20180514](/bandwagon/idc/newyork/20180514-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180514")
    * [20180527](/bandwagon/idc/newyork/20180527-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180527")
    * [20180804](/bandwagon/idc/newyork/20180804-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180804")
    * [20180918](/bandwagon/idc/newyork/20180918-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180918")
  * 本期报告：在纽约部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/newyork/20180622-bwg-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180622")
    * [Digital Ocean](do/idc/newyork/20180622-do-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")



本文最初发表于[多地到BandwagonHost纽约[NewYork]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-bandwagon-idc-newyork.html)
