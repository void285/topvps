#  多地到BandwagonHost阿姆斯特丹[Amsterdam]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到BandwagonHost阿姆斯特丹\[Amsterdam\]机房的Ping测试（20180426）](/images/thumbnails/to_bwg_Amsterdam.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[BandwagonHost](https://vps123.top/go/bwg)的[荷兰-阿姆斯特丹机房](https://vps123.top/bandwagon-facilities.html#amsterdam)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[BandwagonHost](https://vps123.top/go/bwg)的荷兰-阿姆斯特丹机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[BandwagonHost全部机房](/bandwagon/isp/china/20180426-bandwagon-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到BandwagonHost荷兰-阿姆斯特丹机房的PING测试结果，连通概况如下：大陆28个省市的116个有效测试样本中，共有超时点4个；响应均值为362毫秒，最快的三地区为海南、安徽、江苏，最慢的三地区为江西、贵州、广西；浙江、江苏、陕西有响应超时情况；江西、广西、湖北、贵州、陕西等23处丢包率较高。海外15个国家地区的67个有效测试样本中，无超时点；响应均值为156毫秒，最快的三地区为荷兰、英国、德国，最慢的三地区为韩国、香港、澳大利亚。

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商BandwagonHost位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/bwg_20180426/plot_idc_bwg_netherlands-amsterdam_20180426_mainland.png)

大陆各省份到BandwagonHost荷兰-阿姆斯特丹机房的测速数据 [20180426] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
海南 | 1个 | 0 | 256ms | 0 | 福建 | 10个 | 0 | 369ms | 11.3%  
安徽 | 5个 | 0 | 293ms | 7.5% | 辽宁 | 6个 | 0 | 380ms | 9.4%  
江苏 | 8个 | 1个 | 305ms | 9.5% | 湖南 | 3个 | 0 | 383ms | 1.7%  
云南 | 2个 | 0 | 309ms | 0 | 黑龙江 | 3个 | 0 | 385ms | 11.1%  
广东 | 10个 | 0 | 315ms | 6.3% | 湖北 | 3个 | 0 | 397ms | 32.2%  
上海 | 3个 | 0 | 321ms | 12.2% | 北京 | 4个 | 0 | 402ms | 16.7%  
浙江 | 16个 | 2个 | 324ms | 7.9% | 内蒙古 | 3个 | 0 | 406ms | 12.2%  
天津 | 3个 | 0 | 326ms | 8.3% | 山东 | 1个 | 0 | 407ms | 0  
重庆 | 3个 | 0 | 338ms | 10.0% | 吉林 | 1个 | 0 | 407ms | 16.7%  
河北 | 2个 | 0 | 341ms | 8.3% | 陕西 | 6个 | 1个 | 413ms | 17.3%  
山西 | 2个 | 0 | 342ms | 10.0% | 新疆 | 1个 | 0 | 451ms | 6.7%  
四川 | 2个 | 0 | 344ms | 1.7% | 江西 | 2个 | 0 | 451ms | 38.3%  
河南 | 8个 | 0 | 352ms | 7.8% | 贵州 | 4个 | 0 | 505ms | 30.8%  
均值 | 116个 | 4个 | 362ms | 11.9% | 广西 | 3个 | 0 | 522ms | 35.6%  
甘肃 | 1个 | 0 | 367ms | 10.0% |  |  |  |  |   
  
简评：如果你考虑在BandwagonHost的阿姆斯特丹[Amsterdam]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有116个，其中超时点4个，平均响应时间为362毫秒，丢包率为11%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的2个，超过300毫秒的26个；  
超时点较多的省份：江苏、浙江、陕西；  
丢包率较高的省份：上海、重庆、山西、甘肃、福建、黑龙江、湖北、北京、内蒙古、吉林、陕西、江西、贵州、广西；

## 海外测速点

![海外各国家地区到VPS提供商BandwagonHost位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/bwg_20180426/plot_idc_bwg_netherlands-amsterdam_20180426_overseas.png)

海外线路到BandwagonHost荷兰-阿姆斯特丹机房的测速数据 [20180426] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
荷兰 | 2个 | 0 | 1ms | 0 | 南非 | 1个 | 0 | 169ms | 0  
英国 | 2个 | 0 | 6ms | 0 | 新加坡 | 5个 | 0 | 195ms | 0  
德国 | 1个 | 0 | 10ms | 0 | 马来西亚 | 1个 | 0 | 203ms | 0  
法国 | 1个 | 0 | 12ms | 0 | 日本 | 1个 | 0 | 249ms | 0  
加拿大 | 1个 | 0 | 91ms | - | 台湾 | 1个 | 0 | 285ms | -  
俄罗斯 | 1个 | 0 | 97ms | 0 | 韩国 | 11个 | 0 | 290ms | 0  
美国 | 19个 | 0 | 140ms | 0 | 香港 | 19个 | 0 | 296ms | 0  
均值 | 67个 | 0 | 156ms | 0 | 澳大利亚 | 1个 | 0 | 306ms | 0  
  
简评：如果你考虑在BandwagonHost的阿姆斯特丹[Amsterdam]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有67个，其中超时点0个，平均响应时间为156毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的2个，在100-200毫秒间的3个，在200-300毫秒间的5个，超过300毫秒的1个；

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [BandwagonHost](https://vps123.top/pingtests/idc-bandwagon/20180426 "本期BandwagonHost的全部测速报告")
    * [各地到BandwagonHost某机房](https://vps123.top/pingtests/idc-bandwagon/isp-global/20180426 "以BandwagonHost某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到BandwagonHost各机房](https://vps123.top/pingtests/idc-bandwagon/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较BandwagonHost各机房")
  * 本期到BandwagonHost _其他机房_ 的报告： 
    * [佛罗里达](/bandwagon/idc/florida/20180426-bandwagon-idc-florida.md "多地到BandwagonHost佛罗里达机房的Ping测试 20180426")
    * [佛利蒙](/bandwagon/idc/fremont/20180426-bandwagon-idc-fremont.md "多地到BandwagonHost佛利蒙机房的Ping测试 20180426")
    * [香港](/bandwagon/idc/hongkong/20180426-bandwagon-idc-hongkong.md "多地到BandwagonHost香港机房的Ping测试 20180426")
    * [洛杉矶](/bandwagon/idc/losangeles/20180426-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180426")
    * [纽约](/bandwagon/idc/newyork/20180426-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180426")
    * [凤凰城](/bandwagon/idc/phoenix/20180426-bandwagon-idc-phoenix.md "多地到BandwagonHost凤凰城机房的Ping测试 20180426")
    * [温哥华](/bandwagon/idc/vancouver/20180426-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180426")
  * 到BandwagonHost阿姆斯特丹机房的 _其他近期报告_ ： 
    * [20180514](/bandwagon/idc/amsterdam/20180514-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180514")
    * [20180527](/bandwagon/idc/amsterdam/20180527-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180527")
    * [20180622](/bandwagon/idc/amsterdam/20180622-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180622")
    * [20180804](/bandwagon/idc/amsterdam/20180804-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180804")
    * [20180918](/bandwagon/idc/amsterdam/20180918-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180918")
  * 本期报告：在阿姆斯特丹部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/amsterdam/20180426-bwg-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180426")
    * [Digital Ocean](do/idc/amsterdam/20180426-do-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180426")
    * [Vultr](/vultr/idc/amsterdam/20180426-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180426")



本文最初发表于[多地到BandwagonHost阿姆斯特丹[Amsterdam]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-bandwagon-idc-amsterdam.html)
