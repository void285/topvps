#  多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean阿姆斯特丹\[Amsterdam\]机房的Ping测试（20180527）](/images/thumbnails/to_do_Amsterdam.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[荷兰-阿姆斯特丹机房](https://vps123.top/digitalocean-facilities.html#amsterdam)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的荷兰-阿姆斯特丹机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180527-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的1935个有效测试样本中，共有超时点18个；响应均值为311毫秒，最快的三地区为上海、天津、江西，最慢的三地区为黑龙江、贵州、新疆；广东、江苏、北京、河南、山东等10处有响应超时情况；辽宁、河北、北京、湖南丢包率较高。海外21个国家地区的174个有效测试样本中，无超时点；响应均值为181毫秒，最快的三地区为荷兰、意大利、法国，最慢的三地区为柬埔寨、澳大利亚、越南。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_netherlands-amsterdam_20180527_mainland.png)

**大陆各省份到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 16个 | 0 | 227ms | 0.1%  
天津 | 10个 | 0 | 266ms | 2.1%  
江西 | 49个 | 0 | 282ms | 1.3%  
安徽 | 78个 | 0 | 282ms | 1.9%  
河北 | 67个 | 0 | 288ms | 12.9%  
辽宁 | 76个 | 0 | 289ms | 15.7%  
福建 | 72个 | 0 | 291ms | 1.9%  
内蒙古 | 65个 | 0 | 292ms | 1.3%  
江苏 | 122个 | 2个 | 293ms | 0.8%  
浙江 | 100个 | 1个 | 295ms | 0.7%  
广东 | 160个 | 4个 | 300ms | 1.4%  
均值 | 1935个 | 18个 | 311ms | 3.0%  
甘肃 | 45个 | 0 | 314ms | 2.1%  
山西 | 74个 | 0 | 314ms | 3.0%  
北京 | 16个 | 2个 | 316ms | 8.3%  
广西 | 77个 | 0 | 316ms | 3.0%  
河南 | 109个 | 2个 | 318ms | 1.8%  
湖北 | 85个 | 0 | 320ms | 2.0%  
海南 | 28个 | 0 | 321ms | 1.1%  
山东 | 103个 | 2个 | 322ms | 1.2%  
湖南 | 90个 | 1个 | 323ms | 5.3%  
宁夏 | 24个 | 0 | 324ms | 2.2%  
陕西 | 68个 | 2个 | 326ms | 4.5%  
云南 | 44个 | 0 | 327ms | 0.4%  
四川 | 96个 | 0 | 331ms | 1.1%  
吉林 | 38个 | 1个 | 331ms | 1.9%  
重庆 | 26个 | 1个 | 333ms | 2.0%  
青海 | 6个 | 0 | 334ms | 2.0%  
黑龙江 | 78个 | 0 | 339ms | 1.5%  
贵州 | 56个 | 0 | 340ms | 3.8%  
新疆 | 57个 | 0 | 356ms | 3.2%  
  
**简评：** 如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有1935个，其中超时点18个，平均响应时间为311毫秒，丢包率为3%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的11个，超过300毫秒的19个；  
超时点较多的省份：北京；  
丢包率较高的省份：河北、辽宁；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_netherlands-amsterdam_20180527_overseas.png)

**海外线路到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
荷兰 | 2个 | 0 | 1ms | 0  
意大利 | 2个 | 0 | 7ms | -  
法国 | 2个 | 0 | 11ms | 0  
德国 | 6个 | 0 | 16ms | 0  
英国 | 4个 | 0 | 31ms | 0  
加拿大 | 6个 | 0 | 98ms | 0  
俄罗斯 | 2个 | 0 | 103ms | 0  
美国 | 42个 | 0 | 144ms | 2.6%  
新加坡 | 12个 | 0 | 173ms | 0  
印度尼西亚 | 2个 | 0 | 181ms | 0.5%  
均值 | 174个 | 0 | 181ms | 0.3%  
南非 | 4个 | 0 | 190ms | 1.3%  
巴西 | 2个 | 0 | 207ms | 0  
日本 | 2个 | 0 | 263ms | 0  
香港 | 40个 | 0 | 273ms | 0  
马来西亚 | 8个 | 0 | 279ms | 0  
韩国 | 24个 | 0 | 283ms | 0  
菲律宾 | 2个 | 0 | 286ms | 1.0%  
台湾 | 2个 | 0 | 290ms | -  
柬埔寨 | 2个 | 0 | 312ms | 0  
澳大利亚 | 4个 | 0 | 317ms | 0.3%  
越南 | 4个 | 0 | 338ms | 0  
  
**简评：** 如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有174个，其中超时点0个，平均响应时间为181毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的7个，超过300毫秒的3个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180527 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180527 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [班加罗尔](/digitalocean/idc/bangalore/20180527-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180527")
    * [法兰克福](/digitalocean/idc/frankfurt/20180527-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [伦敦](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [纽约](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [新加坡](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [多伦多](/digitalocean/idc/toronto/20180527-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180527")
  * 到Digital Ocean阿姆斯特丹机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [20180622](/digitalocean/idc/amsterdam/20180622-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/amsterdam/20180804-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/amsterdam/20180918-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
  * 本期报告：在阿姆斯特丹部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/amsterdam/20180527-bwg-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180527")
    * [Digital Ocean](do/idc/amsterdam/20180527-do-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180527")
    * [Vultr](/vultr/idc/amsterdam/20180527-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180527")



本文最初发表于[多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-digitalocean-idc-amsterdam.html)
