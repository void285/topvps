#  多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean阿姆斯特丹\[Amsterdam\]机房的Ping测试（20180918）](/images/thumbnails/to_do_Amsterdam.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[荷兰-阿姆斯特丹机房](https://vps123.top/digitalocean-facilities.html#amsterdam)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的荷兰-阿姆斯特丹机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180918-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Digital Ocean荷兰-阿姆斯特丹机房的PING测试结果，连通概况如下：大陆31个省市的2679个有效测试样本中，共有超时点29个；响应均值为298毫秒，最快的三地区为浙江、宁夏、河北，最慢的三地区为黑龙江、西藏、吉林；江苏、广东、浙江、山西、福建等8处有响应超时情况；吉林、西藏、山西、河南、青海等26处丢包率较高。海外17个国家地区的164个有效测试样本中，共有超时点6个；响应均值为183毫秒，最快的三地区为意大利、德国、俄罗斯，最慢的三地区为韩国、澳大利亚、菲律宾；马来西亚、新加坡、香港有响应超时情况；菲律宾丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_netherlands-amsterdam_20180918_mainland.png)

**大陆各省份到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
浙江 | 126个 | 4个 | 258ms | 5.6%  
宁夏 | 13个 | 0 | 268ms | 1.5%  
河北 | 112个 | 0 | 269ms | 10.1%  
广西 | 107个 | 0 | 271ms | 8.0%  
安徽 | 140个 | 0 | 271ms | 6.4%  
内蒙古 | 108个 | 0 | 275ms | 12.3%  
上海 | 15个 | 0 | 277ms | 9.4%  
甘肃 | 61个 | 0 | 278ms | 3.7%  
湖北 | 99个 | 1个 | 279ms | 5.6%  
江苏 | 169个 | 9个 | 283ms | 5.6%  
广东 | 229个 | 8个 | 283ms | 5.4%  
江西 | 72个 | 0 | 289ms | 7.0%  
湖南 | 135个 | 0 | 289ms | 9.5%  
福建 | 89个 | 2个 | 291ms | 8.4%  
青海 | 10个 | 0 | 293ms | 13.5%  
天津 | 11个 | 0 | 295ms | 4.3%  
辽宁 | 112个 | 1个 | 295ms | 12.4%  
北京 | 15个 | 0 | 296ms | 3.1%  
云南 | 53个 | 0 | 297ms | 6.5%  
陕西 | 85个 | 0 | 297ms | 8.1%  
四川 | 136个 | 0 | 298ms | 3.5%  
均值 | 2679个 | 29个 | 298ms | 8.9%  
贵州 | 80个 | 1个 | 310ms | 8.1%  
海南 | 26个 | 0 | 310ms | 8.8%  
重庆 | 14个 | 0 | 313ms | 12.2%  
山东 | 183个 | 0 | 320ms | 11.8%  
河南 | 162个 | 0 | 336ms | 14.2%  
山西 | 94个 | 3个 | 340ms | 15.7%  
新疆 | 68个 | 0 | 342ms | 10.4%  
黑龙江 | 104个 | 0 | 350ms | 12.1%  
西藏 | 8个 | 0 | 352ms | 16.3%  
吉林 | 43个 | 0 | 402ms | 17.8%  
  
**简评：** 如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有2679个，其中超时点29个，平均响应时间为298毫秒，丢包率为8%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的21个，超过300毫秒的10个；  
丢包率较高的省份：河北、内蒙古、青海、辽宁、重庆、山东、河南、山西、新疆、黑龙江、西藏、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_netherlands-amsterdam_20180918_overseas.png)

**海外线路到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
意大利 | 2个 | 0 | 7ms | -  
德国 | 6个 | 0 | 24ms | 0  
俄罗斯 | 2个 | 0 | 42ms | -  
加拿大 | 6个 | 0 | 84ms | 0  
荷兰 | 2个 | 0 | 102ms | 0  
美国 | 32个 | 0 | 146ms | 0.9%  
新加坡 | 10个 | 1个 | 171ms | 0  
均值 | 164个 | 6个 | 183ms | 1.5%  
香港 | 42个 | 1个 | 190ms | 0  
台湾 | 4个 | 0 | 201ms | 0  
印度尼西亚 | 2个 | 0 | 202ms | 0.5%  
越南 | 4个 | 0 | 223ms | 0.5%  
赞比亚 | 2个 | 0 | 223ms | 5.0%  
马来西亚 | 12个 | 4个 | 233ms | 0  
日本 | 6个 | 0 | 244ms | 0.3%  
韩国 | 24个 | 0 | 246ms | 0  
澳大利亚 | 4个 | 0 | 334ms | 0.3%  
菲律宾 | 4个 | 0 | 437ms | 14.7%  
  
**简评：** 如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有164个，其中超时点6个，平均响应时间为183毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的1个，在100-200毫秒间的4个，在200-300毫秒间的7个，超过300毫秒的2个；  
超时点较多的国家/地区：马来西亚；  
丢包率较高的国家/地区：菲律宾；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180918 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180918 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [班加罗尔](/digitalocean/idc/bangalore/20180918-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180918")
    * [法兰克福](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
    * [伦敦](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
    * [纽约](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")
    * [新加坡](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
    * [多伦多](/digitalocean/idc/toronto/20180918-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180918")
  * 到Digital Ocean阿姆斯特丹机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/amsterdam/20180527-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/amsterdam/20180622-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/amsterdam/20180804-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
  * 本期报告：在阿姆斯特丹部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/amsterdam/20180918-bwg-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180918")
    * [Digital Ocean](do/idc/amsterdam/20180918-do-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
    * [Vultr](/vultr/idc/amsterdam/20180918-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-digitalocean-idc-amsterdam.html)
