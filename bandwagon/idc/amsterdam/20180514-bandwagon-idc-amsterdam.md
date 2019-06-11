#  多地到BandwagonHost阿姆斯特丹[Amsterdam]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到BandwagonHost阿姆斯特丹\[Amsterdam\]机房的Ping测试（20180514）](/images/thumbnails/to_bwg_Amsterdam.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[BandwagonHost](https://vps123.top/go/bwg)的[荷兰-阿姆斯特丹机房](https://vps123.top/bandwagon-facilities.html#amsterdam)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[BandwagonHost](https://vps123.top/go/bwg)的荷兰-阿姆斯特丹机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[BandwagonHost全部机房](/bandwagon/isp/china/20180514-bandwagon-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到BandwagonHost荷兰-阿姆斯特丹机房的PING测试结果，连通概况如下：大陆28个省市的185个有效测试样本中，共有超时点19个；响应均值为355毫秒，最快的三地区为新疆、安徽、上海，最慢的三地区为贵州、甘肃、山西；浙江、江苏、广东、福建、重庆等10处有响应超时情况；贵州、湖北、广西、江西、重庆等14处丢包率较高。海外14个国家地区的61个有效测试样本中，无超时点；响应均值为170毫秒，最快的三地区为英国、德国、法国，最慢的三地区为台湾、澳大利亚、香港。

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商BandwagonHost位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/bwg_20180514/plot_idc_bwg_netherlands-amsterdam_20180514_mainland.png)

大陆各省份到BandwagonHost荷兰-阿姆斯特丹机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
新疆 | 2个 | 1个 | 271ms | 0 | 福建 | 14个 | 2个 | 364ms | 14.7%  
安徽 | 5个 | 1个 | 283ms | 1.7% | 海南 | 1个 | 0 | 378ms | 16.7%  
上海 | 3个 | 0 | 284ms | 3.3% | 辽宁 | 7个 | 0 | 383ms | 4.7%  
湖南 | 7个 | 0 | 301ms | 0 | 内蒙古 | 3个 | 0 | 384ms | 0  
江苏 | 21个 | 3个 | 307ms | 8.3% | 四川 | 6个 | 0 | 390ms | 1.7%  
天津 | 2个 | 0 | 316ms | 5.0% | 吉林 | 1个 | 0 | 392ms | 0  
山东 | 6个 | 1个 | 318ms | 6.7% | 重庆 | 5个 | 2个 | 394ms | 23.3%  
浙江 | 24个 | 4个 | 318ms | 13.8% | 云南 | 2个 | 0 | 407ms | 23.3%  
河北 | 2个 | 0 | 328ms | 0 | 江西 | 4个 | 0 | 408ms | 30.0%  
陕西 | 7个 | 1个 | 333ms | 4.2% | 湖北 | 7个 | 0 | 460ms | 44.4%  
广东 | 25个 | 3个 | 338ms | 3.3% | 广西 | 4个 | 0 | 464ms | 37.8%  
河南 | 9个 | 0 | 349ms | 5.6% | 贵州 | 6个 | 1个 | 465ms | 46.7%  
黑龙江 | 4个 | 0 | 350ms | 0 | 甘肃 | 1个 | 0 | 519ms | 16.7%  
均值 | 185个 | 19个 | 355ms | 11.9% | 山西 | 2个 | 0 | - | -  
北京 | 5个 | 0 | 357ms | 16.0% |  |  |  |  |   
  
简评：如果你考虑在BandwagonHost的阿姆斯特丹[Amsterdam]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有185个，其中超时点19个，平均响应时间为355毫秒，丢包率为11%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的3个，超过300毫秒的24个；  
超时点较多的省份：安徽、江苏、山东、浙江、陕西、广东、福建、重庆、贵州；  
丢包率较高的省份：浙江、北京、福建、海南、重庆、云南、江西、湖北、广西、贵州、甘肃；

## 海外测速点

![海外各国家地区到VPS提供商BandwagonHost位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/bwg_20180514/plot_idc_bwg_netherlands-amsterdam_20180514_overseas.png)

海外线路到BandwagonHost荷兰-阿姆斯特丹机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
英国 | 1个 | 0 | 6ms | 0 | 马来西亚 | 1个 | 0 | 195ms | 0  
德国 | 1个 | 0 | 8ms | 0 | 巴西 | 1个 | 0 | 206ms | 0  
法国 | 1个 | 0 | 15ms | 0 | 日本 | 1个 | 0 | 259ms | 0  
加拿大 | 1个 | 0 | 88ms | - | 韩国 | 11个 | 0 | 285ms | 0  
俄罗斯 | 1个 | 0 | 89ms | 0 | 台湾 | 1个 | 0 | 286ms | -  
美国 | 17个 | 0 | 141ms | 1.0% | 澳大利亚 | 1个 | 0 | 309ms | 0  
均值 | 61个 | 0 | 170ms | 0.1% | 香港 | 19个 | 0 | 315ms | 0  
新加坡 | 4个 | 0 | 189ms | 0 |  |  |  |  |   
  
简评：如果你考虑在BandwagonHost的阿姆斯特丹[Amsterdam]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有61个，其中超时点0个，平均响应时间为170毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的2个，在100-200毫秒间的3个，在200-300毫秒间的4个，超过300毫秒的2个；

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [BandwagonHost](https://vps123.top/pingtests/idc-bandwagon/20180514 "本期BandwagonHost的全部测速报告")
    * [各地到BandwagonHost某机房](https://vps123.top/pingtests/idc-bandwagon/isp-global/20180514 "以BandwagonHost某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到BandwagonHost各机房](https://vps123.top/pingtests/idc-bandwagon/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较BandwagonHost各机房")
  * 本期到BandwagonHost _其他机房_ 的报告： 
    * [佛罗里达](/bandwagon/idc/florida/20180514-bandwagon-idc-florida.md "多地到BandwagonHost佛罗里达机房的Ping测试 20180514")
    * [佛利蒙](/bandwagon/idc/fremont/20180514-bandwagon-idc-fremont.md "多地到BandwagonHost佛利蒙机房的Ping测试 20180514")
    * [香港](/bandwagon/idc/hongkong/20180514-bandwagon-idc-hongkong.md "多地到BandwagonHost香港机房的Ping测试 20180514")
    * [洛杉矶](/bandwagon/idc/losangeles/20180514-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180514")
    * [纽约](/bandwagon/idc/newyork/20180514-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180514")
    * [凤凰城](/bandwagon/idc/phoenix/20180514-bandwagon-idc-phoenix.md "多地到BandwagonHost凤凰城机房的Ping测试 20180514")
    * [温哥华](/bandwagon/idc/vancouver/20180514-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180514")
  * 到BandwagonHost阿姆斯特丹机房的 _其他近期报告_ ： 
    * [20180527](/bandwagon/idc/amsterdam/20180527-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180527")
    * [20180622](/bandwagon/idc/amsterdam/20180622-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180622")
    * [20180804](/bandwagon/idc/amsterdam/20180804-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180804")
    * [20180918](/bandwagon/idc/amsterdam/20180918-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180918")
  * 本期报告：在阿姆斯特丹部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/amsterdam/20180514-bwg-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180514")
    * [Digital Ocean](do/idc/amsterdam/20180514-do-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [Vultr](/vultr/idc/amsterdam/20180514-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180514")



本文最初发表于[多地到BandwagonHost阿姆斯特丹[Amsterdam]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-bandwagon-idc-amsterdam.html)
