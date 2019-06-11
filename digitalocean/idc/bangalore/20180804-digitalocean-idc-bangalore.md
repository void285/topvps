#  多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean班加罗尔\[Bangalore\]机房的Ping测试（20180804）](/images/thumbnails/to_do_Bangalore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[印度-班加罗尔机房](https://vps123.top/digitalocean-facilities.html#bangalore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的印度-班加罗尔机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180804-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的4887个有效测试样本中，共有超时点37个；响应均值为350毫秒，最快的三地区为浙江、湖北、广东，最慢的三地区为新疆、西藏、青海；江苏、浙江、上海、江西、贵州等8处有响应超时情况；西藏、天津、云南、安徽、青海丢包率较高。海外18个国家地区的234个有效测试样本中，无超时点；响应均值为196毫秒，最快的三地区为印度尼西亚、新加坡、菲律宾，最慢的三地区为韩国、澳大利亚、南非；美国、马来西亚丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_india-bangalore_20180804_mainland.png)

**大陆各省份到Digital Ocean印度-班加罗尔机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
浙江 | 226个 | 7个 | 296ms | 0.8%  
湖北 | 173个 | 0 | 313ms | 2.3%  
广东 | 406个 | 0 | 321ms | 2.0%  
上海 | 31个 | 4个 | 325ms | 1.0%  
江苏 | 335个 | 9个 | 330ms | 2.5%  
北京 | 36个 | 0 | 338ms | 1.2%  
湖南 | 237个 | 3个 | 339ms | 3.0%  
辽宁 | 210个 | 3个 | 340ms | 2.1%  
江西 | 127个 | 4个 | 341ms | 2.2%  
陕西 | 138个 | 3个 | 346ms | 1.1%  
河北 | 232个 | 0 | 347ms | 2.9%  
山东 | 346个 | 0 | 349ms | 0.5%  
安徽 | 207个 | 0 | 349ms | 6.0%  
河南 | 323个 | 0 | 350ms | 3.5%  
云南 | 115个 | 0 | 350ms | 6.6%  
均值 | 4887个 | 37个 | 350ms | 2.6%  
重庆 | 34个 | 0 | 351ms | 0.6%  
广西 | 220个 | 0 | 355ms | 2.2%  
四川 | 273个 | 0 | 357ms | 2.1%  
黑龙江 | 144个 | 0 | 359ms | 2.7%  
天津 | 20个 | 0 | 361ms | 16.1%  
海南 | 32个 | 0 | 365ms | 4.3%  
福建 | 160个 | 0 | 371ms | 3.3%  
山西 | 169个 | 0 | 376ms | 2.5%  
宁夏 | 32个 | 0 | 377ms | 0.4%  
甘肃 | 104个 | 0 | 380ms | 0.9%  
贵州 | 138个 | 4个 | 382ms | 1.9%  
内蒙古 | 200个 | 0 | 383ms | 2.1%  
吉林 | 72个 | 0 | 414ms | 5.0%  
新疆 | 123个 | 0 | 421ms | 2.0%  
西藏 | 8个 | 0 | 434ms | 19.0%  
青海 | 16个 | 0 | 444ms | 5.3%  
  
**简评：** 如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有4887个，其中超时点37个，平均响应时间为350毫秒，丢包率为2%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的1个，超过300毫秒的30个；  
超时点较多的省份：上海；  
丢包率较高的省份：天津、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_india-bangalore_20180804_overseas.png)

**海外线路到Digital Ocean印度-班加罗尔机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
印度尼西亚 | 6个 | 0 | 70ms | 0  
新加坡 | 15个 | 0 | 87ms | 0  
菲律宾 | 3个 | 0 | 114ms | 0  
日本 | 6个 | 0 | 127ms | 2.7%  
巴西 | 3个 | 0 | 158ms | 0  
意大利 | 3个 | 0 | 159ms | -  
德国 | 9个 | 0 | 164ms | 0  
香港 | 66个 | 0 | 182ms | 0  
马来西亚 | 12个 | 0 | 186ms | 6.3%  
均值 | 234个 | 0 | 196ms | 1.3%  
俄罗斯 | 3个 | 0 | 200ms | -  
美国 | 48个 | 0 | 228ms | 8.5%  
台湾 | 3个 | 0 | 234ms | 0  
加拿大 | 15个 | 0 | 240ms | 0  
英国 | 6个 | 0 | 253ms | 0.5%  
荷兰 | 3个 | 0 | 259ms | 0  
韩国 | 21个 | 0 | 262ms | 0  
澳大利亚 | 6个 | 0 | 290ms | 0  
南非 | 6个 | 0 | 321ms | 3.5%  
  
**简评：** 如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有234个，其中超时点0个，平均响应时间为196毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50-100毫秒间的2个，在100-200毫秒间的8个，在200-300毫秒间的7个，超过300毫秒的1个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180804 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180804 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180804-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
    * [法兰克福](/digitalocean/idc/frankfurt/20180804-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [伦敦](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [纽约](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [新加坡](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [多伦多](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")
  * 到Digital Ocean班加罗尔机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/bangalore/20180514-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/bangalore/20180527-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/bangalore/20180622-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180622")
    * [20180918](/digitalocean/idc/bangalore/20180918-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-digitalocean-idc-bangalore.html)
