#  多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean纽约\[NewYork\]机房的Ping测试（20180918）](/images/thumbnails/to_do_NewYork.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-纽约机房](https://vps123.top/digitalocean-facilities.html#newyork)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-纽约机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180918-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Digital Ocean美国-纽约机房的PING测试结果，连通概况如下：大陆31个省市的3928个有效测试样本中，共有超时点42个；响应均值为282毫秒，最快的三地区为上海、河南、浙江，最慢的三地区为吉林、新疆、西藏；江苏、浙江、广东、山西、广西等11处有响应超时情况；内蒙古、吉林、山东、辽宁、河南等9处丢包率较高。海外16个国家地区的223个有效测试样本中，无超时点；响应均值为180毫秒，最快的三地区为加拿大、意大利、美国，最慢的三地区为赞比亚、马来西亚、菲律宾；菲律宾、日本丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_usa-newyork_20180918_mainland.png)

**大陆各省份到Digital Ocean美国-纽约机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 20个 | 0 | 247ms | 1.2%  
河南 | 243个 | 0 | 263ms | 8.8%  
浙江 | 192个 | 10个 | 263ms | 3.2%  
北京 | 22个 | 0 | 263ms | 0.2%  
山西 | 147个 | 3个 | 265ms | 7.9%  
河北 | 170个 | 0 | 271ms | 6.8%  
安徽 | 203个 | 1个 | 272ms | 2.9%  
湖北 | 142个 | 1个 | 273ms | 2.5%  
江苏 | 252个 | 13个 | 274ms | 4.6%  
广西 | 159个 | 2个 | 274ms | 2.7%  
山东 | 254个 | 0 | 278ms | 9.3%  
广东 | 334个 | 8个 | 278ms | 4.0%  
江西 | 116个 | 0 | 281ms | 2.7%  
辽宁 | 164个 | 0 | 282ms | 9.1%  
均值 | 3928个 | 42个 | 282ms | 5.4%  
重庆 | 22个 | 1个 | 283ms | 1.8%  
海南 | 42个 | 0 | 283ms | 3.2%  
内蒙古 | 158个 | 0 | 284ms | 11.7%  
黑龙江 | 146个 | 0 | 285ms | 8.2%  
天津 | 17个 | 0 | 287ms | 2.0%  
湖南 | 196个 | 1个 | 287ms | 3.9%  
福建 | 132个 | 1个 | 288ms | 3.1%  
陕西 | 124个 | 1个 | 289ms | 2.5%  
贵州 | 111个 | 0 | 293ms | 4.5%  
云南 | 78个 | 0 | 297ms | 2.3%  
宁夏 | 16个 | 0 | 302ms | 1.6%  
四川 | 196个 | 0 | 303ms | 4.7%  
甘肃 | 94个 | 0 | 312ms | 2.7%  
青海 | 16个 | 0 | 314ms | 2.1%  
吉林 | 61个 | 0 | 330ms | 10.7%  
新疆 | 90个 | 0 | 335ms | 4.7%  
西藏 | 11个 | 0 | 387ms | 6.5%  
  
**简评：** 如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有3928个，其中超时点42个，平均响应时间为282毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的24个，超过300毫秒的7个；  
丢包率较高的省份：内蒙古、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_usa-newyork_20180918_overseas.png)

**海外线路到Digital Ocean美国-纽约机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 6个 | 0 | 8ms | -  
意大利 | 3个 | 0 | 71ms | -  
美国 | 45个 | 0 | 86ms | 0.1%  
德国 | 9个 | 0 | 97ms | 0  
俄罗斯 | 3个 | 0 | 116ms | -  
台湾 | 6个 | 0 | 134ms | 0  
荷兰 | 3个 | 0 | 166ms | 0  
韩国 | 36个 | 0 | 172ms | 0  
均值 | 223个 | 0 | 180ms | 2.1%  
香港 | 60个 | 0 | 187ms | 0  
日本 | 6个 | 0 | 197ms | 8.3%  
新加坡 | 15个 | 0 | 217ms | 0  
澳大利亚 | 6个 | 0 | 246ms | 0.3%  
越南 | 6个 | 0 | 274ms | 0.6%  
赞比亚 | 5个 | 0 | 282ms | 1.0%  
马来西亚 | 9个 | 0 | 304ms | 0  
菲律宾 | 5个 | 0 | 332ms | 17.3%  
  
**简评：** 如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有223个，其中超时点0个，平均响应时间为180毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的3个，在100-200毫秒间的6个，在200-300毫秒间的4个，超过300毫秒的2个；  
丢包率较高的国家/地区：菲律宾；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180918 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180918 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180918-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
    * [班加罗尔](/digitalocean/idc/bangalore/20180918-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180918")
    * [法兰克福](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
    * [伦敦](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")
    * [新加坡](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
    * [多伦多](/digitalocean/idc/toronto/20180918-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180918")
  * 到Digital Ocean纽约机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
  * 本期报告：在纽约部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/newyork/20180918-bwg-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180918")
    * [Digital Ocean](do/idc/newyork/20180918-do-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-digitalocean-idc-newyork.html)
