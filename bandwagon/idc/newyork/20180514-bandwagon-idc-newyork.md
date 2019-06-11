#  多地到BandwagonHost纽约[NewYork]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到BandwagonHost纽约\[NewYork\]机房的Ping测试（20180514）](/images/thumbnails/to_bwg_NewYork.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[BandwagonHost](https://vps123.top/go/bwg)的[美国-纽约机房](https://vps123.top/bandwagon-facilities.html#newyork)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[BandwagonHost](https://vps123.top/go/bwg)的美国-纽约机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[BandwagonHost全部机房](/bandwagon/isp/china/20180514-bandwagon-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到BandwagonHost美国-纽约机房的PING测试结果，连通概况如下：大陆28个省市的187个有效测试样本中，共有超时点16个；响应均值为319毫秒，最快的三地区为江西、上海、山东，最慢的三地区为湖北、甘肃、云南；浙江、江苏、福建、四川、辽宁等12处有响应超时情况；广西、湖北、四川、广东、江苏等13处丢包率较高。海外13个国家地区的55个有效测试样本中，共有超时点2个；响应均值为160毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为马来西亚、新加坡、香港；香港有响应超时情况；香港、马来西亚丢包率较高。

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商BandwagonHost位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/bwg_20180514/plot_idc_bwg_usa-newyork_20180514_mainland.png)

大陆各省份到BandwagonHost美国-纽约机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
江西 | 4个 | 0 | 254ms | 0 | 安徽 | 5个 | 1个 | 318ms | 1.7%  
上海 | 3个 | 0 | 256ms | 0 | 内蒙古 | 3个 | 0 | 319ms | 1.1%  
山东 | 6个 | 0 | 263ms | 0 | 均值 | 187个 | 16个 | 319ms | 12.0%  
吉林 | 1个 | 0 | 274ms | 0 | 海南 | 1个 | 0 | 320ms | 0  
北京 | 5个 | 0 | 289ms | 6.7% | 湖南 | 6个 | 0 | 325ms | 3.3%  
四川 | 5个 | 1个 | 298ms | 26.7% | 贵州 | 7个 | 1个 | 331ms | 16.7%  
江苏 | 20个 | 2个 | 298ms | 22.8% | 重庆 | 5个 | 1个 | 338ms | 22.2%  
黑龙江 | 4个 | 0 | 299ms | 1.1% | 广西 | 4个 | 0 | 366ms | 27.8%  
辽宁 | 7个 | 1个 | 301ms | 10.0% | 广东 | 26个 | 1个 | 366ms | 24.8%  
天津 | 2个 | 0 | 304ms | 0 | 河北 | 2个 | 0 | 370ms | 20.0%  
河南 | 9个 | 0 | 305ms | 3.3% | 山西 | 3个 | 0 | 374ms | 3.3%  
陕西 | 8个 | 1个 | 305ms | 4.2% | 湖北 | 8个 | 1个 | 379ms | 27.8%  
福建 | 15个 | 2个 | 306ms | 8.3% | 甘肃 | 1个 | 0 | 383ms | 0  
浙江 | 23个 | 3个 | 315ms | 14.3% | 云南 | 2个 | 1个 | 392ms | 6.7%  
新疆 | 2个 | 0 | 318ms | 0 |  |  |  |  |   
  
简评：如果你考虑在BandwagonHost的纽约[NewYork]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有187个，其中超时点16个，平均响应时间为319毫秒，丢包率为12%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的8个，超过300毫秒的20个；  
超时点较多的省份：四川、辽宁、陕西、福建、浙江、安徽、贵州、重庆、湖北；  
丢包率较高的省份：四川、江苏、辽宁、浙江、贵州、重庆、广西、广东、河北、湖北；

## 海外测速点

![海外各国家地区到VPS提供商BandwagonHost位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/bwg_20180514/plot_idc_bwg_usa-newyork_20180514_overseas.png)

海外线路到BandwagonHost美国-纽约机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 1个 | 0 | 9ms | - | 俄罗斯 | 1个 | 0 | 172ms | 0  
美国 | 18个 | 0 | 62ms | 0 | 台湾 | 1个 | 0 | 196ms | -  
法国 | 1个 | 0 | 83ms | 0 | 韩国 | 11个 | 0 | 204ms | 0  
德国 | 1个 | 0 | 86ms | 0 | 澳大利亚 | 1个 | 0 | 232ms | 0  
巴西 | 1个 | 0 | 134ms | 0 | 马来西亚 | 1个 | 0 | 234ms | 10.0%  
日本 | 1个 | 0 | 152ms | 0 | 新加坡 | 3个 | 0 | 254ms | 0  
均值 | 55个 | 2个 | 160ms | 2.3% | 香港 | 14个 | 2个 | 265ms | 15.0%  
  
简评：如果你考虑在BandwagonHost的纽约[NewYork]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有55个，其中超时点2个，平均响应时间为160毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的3个，在100-200毫秒间的4个，在200-300毫秒间的5个；  
超时点较多的国家/地区：香港；  
丢包率较高的国家/地区：马来西亚、香港；

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [BandwagonHost](https://vps123.top/pingtests/idc-bandwagon/20180514 "本期BandwagonHost的全部测速报告")
    * [各地到BandwagonHost某机房](https://vps123.top/pingtests/idc-bandwagon/isp-global/20180514 "以BandwagonHost某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到BandwagonHost各机房](https://vps123.top/pingtests/idc-bandwagon/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较BandwagonHost各机房")
  * 本期到BandwagonHost _其他机房_ 的报告： 
    * [阿姆斯特丹](/bandwagon/idc/amsterdam/20180514-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180514")
    * [佛罗里达](/bandwagon/idc/florida/20180514-bandwagon-idc-florida.md "多地到BandwagonHost佛罗里达机房的Ping测试 20180514")
    * [佛利蒙](/bandwagon/idc/fremont/20180514-bandwagon-idc-fremont.md "多地到BandwagonHost佛利蒙机房的Ping测试 20180514")
    * [香港](/bandwagon/idc/hongkong/20180514-bandwagon-idc-hongkong.md "多地到BandwagonHost香港机房的Ping测试 20180514")
    * [洛杉矶](/bandwagon/idc/losangeles/20180514-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180514")
    * [凤凰城](/bandwagon/idc/phoenix/20180514-bandwagon-idc-phoenix.md "多地到BandwagonHost凤凰城机房的Ping测试 20180514")
    * [温哥华](/bandwagon/idc/vancouver/20180514-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180514")
  * 到BandwagonHost纽约机房的 _其他近期报告_ ： 
    * [20180527](/bandwagon/idc/newyork/20180527-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180527")
    * [20180622](/bandwagon/idc/newyork/20180622-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180622")
    * [20180804](/bandwagon/idc/newyork/20180804-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180804")
    * [20180918](/bandwagon/idc/newyork/20180918-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180918")
  * 本期报告：在纽约部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/newyork/20180514-bwg-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180514")
    * [Digital Ocean](do/idc/newyork/20180514-do-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")



本文最初发表于[多地到BandwagonHost纽约[NewYork]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-bandwagon-idc-newyork.html)
