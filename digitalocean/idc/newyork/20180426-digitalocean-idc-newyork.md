#  多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean纽约\[NewYork\]机房的Ping测试（20180426）](/images/thumbnails/to_do_NewYork.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-纽约机房](https://vps123.top/digitalocean-facilities.html#newyork)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-纽约机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180426-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Digital Ocean美国-纽约机房的PING测试结果，连通概况如下：大陆31个省市的2486个有效测试样本中，共有超时点16个；响应均值为290毫秒，最快的三地区为北京、天津、上海，最慢的三地区为甘肃、青海、西藏；浙江、江苏、辽宁、新疆、北京等7处有响应超时情况。海外15个国家地区的204个有效测试样本中，共有超时点1个；响应均值为155毫秒，最快的三地区为加拿大、英国、美国，最慢的三地区为马来西亚、澳大利亚、新加坡；香港有响应超时情况。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_usa-newyork_20180426_mainland.png)

大陆各省份到Digital Ocean美国-纽约机房的测速数据 [20180426] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 9个 | 1个 | 225ms | 0.3% | 广西 | 99个 | 0 | 292ms | 3.3%  
天津 | 14个 | 0 | 249ms | 0.5% | 陕西 | 84个 | 0 | 293ms | 2.0%  
上海 | 19个 | 0 | 260ms | 1.3% | 福建 | 80个 | 0 | 294ms | 2.2%  
河南 | 157个 | 0 | 269ms | 2.0% | 辽宁 | 103个 | 2个 | 294ms | 3.4%  
山西 | 99个 | 0 | 269ms | 1.2% | 重庆 | 27个 | 0 | 295ms | 1.8%  
湖南 | 115个 | 0 | 276ms | 1.5% | 云南 | 80个 | 0 | 297ms | 1.5%  
海南 | 30个 | 0 | 276ms | 2.1% | 安徽 | 114个 | 0 | 297ms | 2.1%  
山东 | 137个 | 0 | 277ms | 1.0% | 吉林 | 49个 | 0 | 300ms | 3.4%  
河北 | 94个 | 0 | 279ms | 1.3% | 内蒙古 | 89个 | 1个 | 300ms | 2.9%  
湖北 | 111个 | 0 | 281ms | 1.6% | 宁夏 | 32个 | 1个 | 301ms | 2.9%  
黑龙江 | 92个 | 0 | 284ms | 3.6% | 贵州 | 66个 | 0 | 305ms | 3.1%  
广东 | 174个 | 0 | 284ms | 1.7% | 四川 | 129个 | 0 | 312ms | 2.5%  
江西 | 65个 | 0 | 290ms | 1.5% | 新疆 | 75个 | 2个 | 329ms | 2.0%  
均值 | 2486个 | 16个 | 290ms | 2.0% | 甘肃 | 65个 | 0 | 329ms | 2.3%  
浙江 | 116个 | 6个 | 291ms | 1.8% | 青海 | 12个 | 0 | 338ms | 1.5%  
江苏 | 147个 | 3个 | 292ms | 1.3% | 西藏 | 3个 | 0 | 352ms | 2.3%  
  
简评：如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有2486个，其中超时点16个，平均响应时间为290毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的24个，超过300毫秒的7个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_usa-newyork_20180426_overseas.png)

海外线路到Digital Ocean美国-纽约机房的测速数据 [20180426] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 6个 | 0 | 11ms | 0 | 俄罗斯 | 3个 | 0 | 183ms | 0  
英国 | 6个 | 0 | 69ms | 0 | 台湾 | 3个 | 0 | 203ms | -  
美国 | 48个 | 0 | 71ms | 0 | 韩国 | 36个 | 0 | 211ms | 3.2%  
法国 | 6个 | 0 | 74ms | 0 | 香港 | 60个 | 1个 | 218ms | 0  
荷兰 | 6个 | 0 | 85ms | 0 | 南非 | 3个 | 0 | 230ms | 0  
德国 | 3个 | 0 | 86ms | 0 | 马来西亚 | 3个 | 0 | 235ms | 0  
均值 | 204个 | 1个 | 155ms | 0.2% | 澳大利亚 | 3个 | 0 | 236ms | 0  
日本 | 3个 | 0 | 165ms | 0 | 新加坡 | 15个 | 0 | 245ms | 0  
  
简评：如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有204个，其中超时点1个，平均响应时间为155毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的5个，在100-200毫秒间的2个，在200-300毫秒间的7个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180426 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180426 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180426-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180426")
    * [班加罗尔](/digitalocean/idc/bangalore/20180426-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180426")
    * [法兰克福](/digitalocean/idc/frankfurt/20180426-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180426")
    * [伦敦](/digitalocean/idc/london/20180426-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180426")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180426-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180426")
    * [新加坡](/digitalocean/idc/singapore/20180426-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180426")
    * [多伦多](/digitalocean/idc/toronto/20180426-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180426")
  * 到Digital Ocean纽约机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
  * 本期报告：在纽约部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/newyork/20180426-bwg-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180426")
    * [Digital Ocean](do/idc/newyork/20180426-do-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180426")



本文最初发表于[多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-digitalocean-idc-newyork.html)
