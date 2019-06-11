#  多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean纽约\[NewYork\]机房的Ping测试（20180804）](/images/thumbnails/to_do_NewYork.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-纽约机房](https://vps123.top/digitalocean-facilities.html#newyork)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-纽约机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180804-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的14148个有效测试样本中，共有超时点143个；响应均值为303毫秒，最快的三地区为河南、北京、湖北，最慢的三地区为甘肃、新疆、西藏；江苏、浙江、江西、上海、山西等15处有响应超时情况；西藏、天津、青海、宁夏、甘肃等22处丢包率较高。海外20个国家地区的658个有效测试样本中，无超时点；响应均值为171毫秒，最快的三地区为加拿大、荷兰、巴西，最慢的三地区为印度尼西亚、马来西亚、菲律宾；菲律宾丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_usa-newyork_20180804_mainland.png)

**大陆各省份到Digital Ocean美国-纽约机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
河南 | 893个 | 0 | 279ms | 5.4%  
北京 | 96个 | 0 | 285ms | 4.1%  
湖北 | 507个 | 3个 | 288ms | 4.8%  
山东 | 1002个 | 3个 | 289ms | 5.7%  
广东 | 1211个 | 3个 | 289ms | 5.4%  
海南 | 96个 | 0 | 289ms | 5.2%  
上海 | 89个 | 12个 | 291ms | 3.6%  
河北 | 636个 | 0 | 293ms | 5.9%  
浙江 | 658个 | 34个 | 296ms | 4.5%  
陕西 | 403个 | 3个 | 297ms | 2.7%  
江苏 | 954个 | 36个 | 298ms | 5.2%  
安徽 | 646个 | 0 | 298ms | 7.1%  
山西 | 507个 | 6个 | 299ms | 2.9%  
湖南 | 731个 | 3个 | 300ms | 4.8%  
重庆 | 108个 | 3个 | 303ms | 5.8%  
均值 | 14148个 | 143个 | 303ms | 5.7%  
江西 | 385个 | 24个 | 305ms | 5.2%  
黑龙江 | 440个 | 0 | 306ms | 3.9%  
福建 | 448个 | 3个 | 307ms | 7.0%  
云南 | 321个 | 3个 | 310ms | 8.1%  
广西 | 649个 | 4个 | 313ms | 6.7%  
内蒙古 | 552个 | 0 | 313ms | 8.0%  
辽宁 | 622个 | 3个 | 313ms | 5.3%  
四川 | 775个 | 0 | 314ms | 6.4%  
天津 | 64个 | 0 | 319ms | 15.0%  
贵州 | 386个 | 0 | 320ms | 4.3%  
宁夏 | 84个 | 0 | 332ms | 9.0%  
吉林 | 196个 | 0 | 345ms | 6.5%  
青海 | 48个 | 0 | 346ms | 10.8%  
甘肃 | 312个 | 0 | 348ms | 8.7%  
新疆 | 305个 | 0 | 361ms | 5.2%  
西藏 | 24个 | 0 | 444ms | 15.2%  
  
**简评：** 如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有14148个，其中超时点143个，平均响应时间为303毫秒，丢包率为5%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的14个，超过300毫秒的17个；  
超时点较多的省份：上海；  
丢包率较高的省份：天津、青海、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_usa-newyork_20180804_overseas.png)

**海外线路到Digital Ocean美国-纽约机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 34个 | 0 | 21ms | 0  
荷兰 | 12个 | 0 | 67ms | 0  
巴西 | 9个 | 0 | 71ms | 0  
意大利 | 9个 | 0 | 71ms | -  
德国 | 23个 | 0 | 94ms | 0  
美国 | 139个 | 0 | 96ms | 1.1%  
英国 | 14个 | 0 | 115ms | 0  
俄罗斯 | 9个 | 0 | 115ms | -  
南非 | 12个 | 0 | 131ms | 0  
均值 | 658个 | 0 | 171ms | 0.6%  
香港 | 198个 | 0 | 196ms | 0  
日本 | 14个 | 0 | 196ms | 2.9%  
韩国 | 63个 | 0 | 201ms | 0  
新加坡 | 41个 | 0 | 205ms | 0  
台湾 | 9个 | 0 | 217ms | 0  
澳大利亚 | 14个 | 0 | 229ms | 0  
法国 | 9个 | 0 | 235ms | 0  
越南 | 2个 | 0 | 243ms | 0  
印度尼西亚 | 14个 | 0 | 267ms | 0  
马来西亚 | 22个 | 0 | 269ms | 0.6%  
菲律宾 | 11个 | 0 | 392ms | 5.5%  
  
**简评：** 如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有658个，其中超时点0个，平均响应时间为171毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的5个，在100-200毫秒间的5个，在200-300毫秒间的8个，超过300毫秒的1个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180804 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180804 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180804-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
    * [班加罗尔](/digitalocean/idc/bangalore/20180804-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180804")
    * [法兰克福](/digitalocean/idc/frankfurt/20180804-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [伦敦](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [新加坡](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [多伦多](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")
  * 到Digital Ocean纽约机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [20180918](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
  * 本期报告：在纽约部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/newyork/20180804-bwg-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180804")
    * [Digital Ocean](do/idc/newyork/20180804-do-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")



本文最初发表于[多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-digitalocean-idc-newyork.html)
