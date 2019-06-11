#  多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean纽约\[NewYork\]机房的Ping测试（20180527）](/images/thumbnails/to_do_NewYork.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-纽约机房](https://vps123.top/digitalocean-facilities.html#newyork)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-纽约机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180527-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的2935个有效测试样本中，共有超时点22个；响应均值为268毫秒，最快的三地区为上海、北京、海南，最慢的三地区为黑龙江、青海、新疆；北京、广东、河南、江苏、山东等11处有响应超时情况。海外21个国家地区的257个有效测试样本中，无超时点；响应均值为177毫秒，最快的三地区为加拿大、美国、意大利，最慢的三地区为印度尼西亚、柬埔寨、菲律宾。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_usa-newyork_20180527_mainland.png)

大陆各省份到Digital Ocean美国-纽约机房的测速数据 [20180527] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 24个 | 0 | 232ms | 0 | 福建 | 108个 | 0 | 270ms | 0.2%  
北京 | 24个 | 3个 | 247ms | 0 | 贵州 | 84个 | 0 | 271ms | 2.4%  
海南 | 42个 | 0 | 252ms | 0.3% | 重庆 | 44个 | 1个 | 272ms | 0.1%  
广东 | 250个 | 3个 | 254ms | 0.9% | 宁夏 | 36个 | 0 | 273ms | 0.2%  
河南 | 163个 | 3个 | 256ms | 0.5% | 湖南 | 134个 | 0 | 273ms | 4.2%  
河北 | 107个 | 0 | 256ms | 1.1% | 云南 | 62个 | 0 | 274ms | 1.7%  
江西 | 73个 | 0 | 258ms | 0 | 天津 | 15个 | 0 | 277ms | 2.3%  
江苏 | 191个 | 3个 | 259ms | 0.4% | 内蒙古 | 100个 | 0 | 281ms | 0.4%  
浙江 | 155个 | 1个 | 259ms | 1.1% | 陕西 | 99个 | 1个 | 282ms | 1.6%  
山西 | 113个 | 1个 | 259ms | 0.2% | 甘肃 | 69个 | 0 | 282ms | 0.7%  
山东 | 155个 | 3个 | 260ms | 0.4% | 四川 | 146个 | 2个 | 283ms | 1.4%  
安徽 | 116个 | 0 | 260ms | 1.3% | 吉林 | 57个 | 0 | 283ms | 0.1%  
辽宁 | 116个 | 0 | 260ms | 0.6% | 黑龙江 | 117个 | 0 | 289ms | 0.5%  
广西 | 113个 | 0 | 263ms | 1.6% | 青海 | 9个 | 0 | 299ms | 1.1%  
湖北 | 128个 | 0 | 266ms | 0.1% | 新疆 | 85个 | 1个 | 318ms | 1.6%  
均值 | 2935个 | 22个 | 268ms | 0.9% |  |  |  |  |   
  
简评：如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有2935个，其中超时点22个，平均响应时间为268毫秒，丢包率为0%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的29个，超过300毫秒的1个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_usa-newyork_20180527_overseas.png)

海外线路到Digital Ocean美国-纽约机房的测速数据 [20180527] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 12个 | 0 | 20ms | 0 | 台湾 | 3个 | 0 | 199ms | -  
美国 | 63个 | 0 | 70ms | 2.5% | 韩国 | 36个 | 0 | 216ms | 0.6%  
意大利 | 3个 | 0 | 71ms | - | 越南 | 6个 | 0 | 227ms | 0.2%  
法国 | 3个 | 0 | 77ms | 0 | 香港 | 55个 | 0 | 237ms | 0  
荷兰 | 3个 | 0 | 87ms | 0 | 新加坡 | 17个 | 0 | 243ms | 0  
德国 | 9个 | 0 | 88ms | 0 | 澳大利亚 | 5个 | 0 | 247ms | 0.4%  
英国 | 6个 | 0 | 98ms | 0 | 南非 | 6个 | 0 | 253ms | 0.5%  
巴西 | 3个 | 0 | 126ms | 0 | 马来西亚 | 12个 | 0 | 261ms | 0.1%  
日本 | 3个 | 0 | 167ms | 0 | 印度尼西亚 | 3个 | 0 | 272ms | 0.7%  
俄罗斯 | 3个 | 0 | 174ms | 0 | 柬埔寨 | 3个 | 0 | 277ms | 0  
均值 | 257个 | 0 | 177ms | 0.3% | 菲律宾 | 3个 | 0 | 298ms | 0  
  
简评：如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有257个，其中超时点0个，平均响应时间为177毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的6个，在100-200毫秒间的4个，在200-300毫秒间的10个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180527 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180527 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180527-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180527")
    * [班加罗尔](/digitalocean/idc/bangalore/20180527-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180527")
    * [法兰克福](/digitalocean/idc/frankfurt/20180527-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [伦敦](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [新加坡](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [多伦多](/digitalocean/idc/toronto/20180527-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180527")
  * 到Digital Ocean纽约机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [20180622](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
  * 本期报告：在纽约部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/newyork/20180527-bwg-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180527")
    * [Digital Ocean](do/idc/newyork/20180527-do-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")



本文最初发表于[多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-digitalocean-idc-newyork.html)
