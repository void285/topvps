#  多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean班加罗尔\[Bangalore\]机房的Ping测试（20180426）](/images/thumbnails/to_do_Bangalore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[印度-班加罗尔机房](https://vps123.top/digitalocean-facilities.html#bangalore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的印度-班加罗尔机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180426-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Digital Ocean印度-班加罗尔机房的PING测试结果，连通概况如下：大陆31个省市的831个有效测试样本中，共有超时点4个；响应均值为369毫秒，最快的三地区为浙江、天津、江苏，最慢的三地区为吉林、新疆、西藏；浙江、江苏、北京有响应超时情况；西藏、安徽、江西、宁夏、甘肃等14处丢包率较高。海外16个国家地区的75个有效测试样本中，无超时点；响应均值为190毫秒，最快的三地区为新加坡、马来西亚、日本，最慢的三地区为加拿大、南非、柬埔寨；柬埔寨丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_india-bangalore_20180426_mainland.png)

**大陆各省份到Digital Ocean印度-班加罗尔机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
浙江 | 36个 | 2个 | 271ms | 2.6%  
天津 | 5个 | 0 | 337ms | 0.3%  
江苏 | 49个 | 1个 | 340ms | 7.7%  
辽宁 | 35个 | 0 | 343ms | 4.8%  
湖北 | 37个 | 0 | 346ms | 3.5%  
北京 | 4个 | 1个 | 348ms | 0.3%  
广东 | 57个 | 0 | 351ms | 3.7%  
上海 | 6个 | 0 | 357ms | 3.0%  
河南 | 52个 | 0 | 365ms | 6.0%  
江西 | 23个 | 0 | 366ms | 9.4%  
湖南 | 42个 | 0 | 366ms | 5.0%  
广西 | 35个 | 0 | 369ms | 6.4%  
均值 | 831个 | 4个 | 369ms | 5.5%  
山西 | 32个 | 0 | 370ms | 3.8%  
陕西 | 29个 | 0 | 373ms | 4.6%  
山东 | 46个 | 0 | 374ms | 4.8%  
海南 | 10个 | 0 | 377ms | 3.2%  
河北 | 30个 | 0 | 379ms | 6.1%  
安徽 | 35个 | 0 | 380ms | 11.3%  
云南 | 28个 | 0 | 382ms | 6.6%  
重庆 | 9个 | 0 | 383ms | 4.7%  
四川 | 44个 | 0 | 388ms | 3.0%  
内蒙古 | 31个 | 0 | 393ms | 4.3%  
青海 | 4个 | 0 | 394ms | 6.0%  
甘肃 | 20个 | 0 | 398ms | 8.3%  
黑龙江 | 31个 | 0 | 399ms | 7.5%  
宁夏 | 11个 | 0 | 400ms | 8.4%  
福建 | 26个 | 0 | 401ms | 7.1%  
贵州 | 21个 | 0 | 401ms | 6.9%  
吉林 | 15个 | 0 | 401ms | 2.3%  
新疆 | 27个 | 0 | 417ms | 4.9%  
西藏 | 1个 | 0 | 455ms | 12.0%  
  
**简评：** 如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有831个，其中超时点4个，平均响应时间为369毫秒，丢包率为5%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的1个，超过300毫秒的30个；  
超时点较多的省份：北京；  
丢包率较高的省份：安徽、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_india-bangalore_20180426_overseas.png)

**海外线路到Digital Ocean印度-班加罗尔机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
新加坡 | 5个 | 0 | 44ms | 0  
马来西亚 | 3个 | 0 | 52ms | 0  
日本 | 3个 | 0 | 125ms | 1.7%  
台湾 | 1个 | 0 | 128ms | -  
香港 | 20个 | 0 | 156ms | 0  
荷兰 | 2个 | 0 | 157ms | 0  
韩国 | 12个 | 0 | 163ms | 0.2%  
法国 | 2个 | 0 | 167ms | 0  
澳大利亚 | 1个 | 0 | 179ms | 0  
德国 | 1个 | 0 | 184ms | 0  
均值 | 75个 | 0 | 190ms | 1.5%  
英国 | 3个 | 0 | 199ms | 0  
美国 | 16个 | 0 | 229ms | 0  
越南 | 1个 | 0 | 242ms | 0  
加拿大 | 3个 | 0 | 265ms | 0  
南非 | 1个 | 0 | 303ms | 0  
柬埔寨 | 1个 | 0 | 452ms | 20.0%  
  
**简评：** 如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有75个，其中超时点0个，平均响应时间为190毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的9个，在200-300毫秒间的3个，超过300毫秒的2个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180426 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180426 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180426-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180426")
    * [法兰克福](/digitalocean/idc/frankfurt/20180426-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180426")
    * [伦敦](/digitalocean/idc/london/20180426-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180426")
    * [纽约](/digitalocean/idc/newyork/20180426-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180426")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180426-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180426")
    * [新加坡](/digitalocean/idc/singapore/20180426-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180426")
    * [多伦多](/digitalocean/idc/toronto/20180426-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180426")
  * 到Digital Ocean班加罗尔机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/bangalore/20180514-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/bangalore/20180527-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/bangalore/20180622-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/bangalore/20180804-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/bangalore/20180918-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-digitalocean-idc-bangalore.html)
