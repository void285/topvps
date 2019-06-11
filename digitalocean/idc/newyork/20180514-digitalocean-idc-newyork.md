#  多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean纽约\[NewYork\]机房的Ping测试（20180514）](/images/thumbnails/to_do_NewYork.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-纽约机房](https://vps123.top/digitalocean-facilities.html#newyork)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-纽约机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180514-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Digital Ocean美国-纽约机房的PING测试结果，连通概况如下：大陆31个省市的2747个有效测试样本中，共有超时点40个；响应均值为293毫秒，最快的三地区为北京、天津、上海，最慢的三地区为四川、新疆、西藏；浙江、山东、广东、江苏、北京等14处有响应超时情况；吉林、贵州、浙江、江苏、江西等19处丢包率较高。海外19个国家地区的241个有效测试样本中，无超时点；响应均值为189毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为南非、印度尼西亚、柬埔寨；柬埔寨、印度尼西亚丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_usa-newyork_20180514_mainland.png)

大陆各省份到Digital Ocean美国-纽约机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 24个 | 3个 | 243ms | 1.4% | 海南 | 31个 | 0 | 295ms | 5.6%  
天津 | 15个 | 0 | 260ms | 2.9% | 安徽 | 109个 | 0 | 296ms | 6.8%  
上海 | 25个 | 0 | 265ms | 7.6% | 江西 | 67个 | 0 | 297ms | 9.2%  
河南 | 145个 | 1个 | 269ms | 4.1% | 湖南 | 123个 | 1个 | 297ms | 4.5%  
河北 | 88个 | 0 | 276ms | 6.1% | 重庆 | 44个 | 3个 | 299ms | 0.7%  
山东 | 158个 | 5个 | 282ms | 6.8% | 内蒙古 | 95个 | 0 | 299ms | 8.0%  
广东 | 229个 | 5个 | 282ms | 3.2% | 浙江 | 149个 | 8个 | 300ms | 10.8%  
陕西 | 95个 | 1个 | 282ms | 6.5% | 甘肃 | 58个 | 0 | 300ms | 1.6%  
广西 | 100个 | 3个 | 283ms | 1.9% | 云南 | 67个 | 0 | 303ms | 3.4%  
辽宁 | 112个 | 0 | 283ms | 7.2% | 江苏 | 178个 | 4个 | 307ms | 10.7%  
黑龙江 | 115个 | 0 | 290ms | 8.9% | 青海 | 10个 | 0 | 307ms | 1.8%  
宁夏 | 29个 | 0 | 290ms | 4.7% | 湖北 | 137个 | 1个 | 311ms | 7.7%  
吉林 | 41个 | 0 | 291ms | 12.7% | 贵州 | 78个 | 0 | 311ms | 11.5%  
福建 | 102个 | 3个 | 293ms | 6.3% | 四川 | 141个 | 0 | 313ms | 5.7%  
山西 | 106个 | 1个 | 293ms | 7.7% | 新疆 | 73个 | 1个 | 329ms | 7.3%  
均值 | 2747个 | 40个 | 293ms | 6.5% | 西藏 | 3个 | 0 | 344ms | 0  
  
简评：如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有2747个，其中超时点40个，平均响应时间为293毫秒，丢包率为6%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的23个，超过300毫秒的8个；  
超时点较多的省份：北京；  
丢包率较高的省份：吉林、浙江、江苏、贵州；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_usa-newyork_20180514_overseas.png)

海外线路到Digital Ocean美国-纽约机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 9个 | 0 | 18ms | 0.7% | 台湾 | 3个 | 0 | 198ms | -  
美国 | 54个 | 0 | 70ms | 3.6% | 韩国 | 39个 | 0 | 208ms | 0  
法国 | 6个 | 0 | 82ms | 0 | 香港 | 57个 | 0 | 222ms | 1.3%  
英国 | 6个 | 0 | 86ms | 0.5% | 澳大利亚 | 6个 | 0 | 237ms | 0  
荷兰 | 3个 | 0 | 87ms | 0 | 菲律宾 | 3个 | 0 | 243ms | 0.7%  
德国 | 6个 | 0 | 100ms | 0 | 新加坡 | 18个 | 0 | 247ms | 0  
巴西 | 2个 | 0 | 126ms | 0 | 马来西亚 | 9个 | 0 | 264ms | 1.1%  
俄罗斯 | 3个 | 0 | 171ms | 0 | 南非 | 5个 | 0 | 267ms | 0  
日本 | 6个 | 0 | 174ms | 0 | 印度尼西亚 | 3个 | 0 | 321ms | 5.3%  
均值 | 241个 | 0 | 189ms | 1.9% | 柬埔寨 | 3个 | 0 | 469ms | 20.7%  
  
简评：如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有241个，其中超时点0个，平均响应时间为189毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的5个，在100-200毫秒间的4个，在200-300毫秒间的7个，超过300毫秒的2个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180514 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180514 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [班加罗尔](/digitalocean/idc/bangalore/20180514-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180514")
    * [法兰克福](/digitalocean/idc/frankfurt/20180514-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [伦敦](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [新加坡](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [多伦多](/digitalocean/idc/toronto/20180514-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180514")
  * 到Digital Ocean纽约机房的 _其他近期报告_ ： 
    * [20180527](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
  * 本期报告：在纽约部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/newyork/20180514-bwg-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180514")
    * [Digital Ocean](do/idc/newyork/20180514-do-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")



本文最初发表于[多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-digitalocean-idc-newyork.html)
