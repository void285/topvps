#  多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean法兰克福\[Frankfurt\]机房的Ping测试（20180527）](/images/thumbnails/to_do_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[德国-法兰克福机房](https://vps123.top/digitalocean-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180527-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的983个有效测试样本中，共有超时点8个；响应均值为277毫秒，最快的三地区为天津、上海、北京，最慢的三地区为黑龙江、新疆、山东；北京、广东、安徽、浙江、河南等8处有响应超时情况；辽宁、河北丢包率较高。海外21个国家地区的85个有效测试样本中，无超时点；响应均值为172毫秒，最快的三地区为法国、荷兰、意大利，最慢的三地区为菲律宾、韩国、澳大利亚。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_germany-frankfurt_20180527_mainland.png)

**大陆各省份到Digital Ocean德国-法兰克福机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 5个 | 0 | 215ms | 0  
上海 | 8个 | 0 | 243ms | 3.0%  
北京 | 8个 | 1个 | 248ms | 1.4%  
内蒙古 | 34个 | 0 | 256ms | 0.1%  
青海 | 3个 | 0 | 258ms | 0.3%  
河北 | 36个 | 0 | 260ms | 13.5%  
广东 | 83个 | 1个 | 262ms | 0.6%  
宁夏 | 12个 | 0 | 262ms | 0.2%  
海南 | 14个 | 0 | 265ms | 0.6%  
湖北 | 44个 | 0 | 267ms | 0.1%  
甘肃 | 23个 | 0 | 268ms | 0.2%  
安徽 | 39个 | 1个 | 268ms | 2.4%  
广西 | 39个 | 0 | 269ms | 3.6%  
辽宁 | 39个 | 0 | 269ms | 15.7%  
重庆 | 14个 | 0 | 270ms | 0  
浙江 | 51个 | 1个 | 273ms | 2.4%  
江西 | 25个 | 0 | 274ms | 1.2%  
均值 | 983个 | 8个 | 277ms | 2.4%  
湖南 | 44个 | 0 | 278ms | 4.6%  
河南 | 56个 | 1个 | 279ms | 0.1%  
云南 | 22个 | 0 | 280ms | 0.8%  
四川 | 49个 | 0 | 281ms | 0.6%  
山西 | 38个 | 0 | 281ms | 0.6%  
江苏 | 64个 | 1个 | 284ms | 0.4%  
福建 | 36个 | 0 | 287ms | 2.2%  
贵州 | 27个 | 1个 | 290ms | 3.2%  
吉林 | 18个 | 0 | 295ms | 0.3%  
陕西 | 33个 | 0 | 298ms | 1.9%  
黑龙江 | 39个 | 0 | 301ms | 0.1%  
新疆 | 28个 | 0 | 303ms | 2.9%  
山东 | 52个 | 1个 | 314ms | 1.4%  
  
**简评：** 如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有983个，其中超时点8个，平均响应时间为277毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的27个，超过300毫秒的3个；  
超时点较多的省份：北京；  
丢包率较高的省份：河北、辽宁；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_germany-frankfurt_20180527_overseas.png)

**海外线路到Digital Ocean德国-法兰克福机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
法国 | 1个 | 0 | 10ms | 0  
荷兰 | 1个 | 0 | 11ms | 0  
意大利 | 1个 | 0 | 11ms | -  
德国 | 3个 | 0 | 13ms | 0  
英国 | 2个 | 0 | 48ms | 0  
俄罗斯 | 1个 | 0 | 94ms | 0  
加拿大 | 4个 | 0 | 103ms | 0  
美国 | 21个 | 0 | 157ms | 2.5%  
新加坡 | 5个 | 0 | 172ms | 0  
均值 | 85个 | 0 | 172ms | 0.4%  
印度尼西亚 | 1个 | 0 | 185ms | 2.0%  
马来西亚 | 4个 | 0 | 216ms | 0  
香港 | 19个 | 0 | 216ms | 0  
巴西 | 1个 | 0 | 217ms | 0  
南非 | 2个 | 0 | 218ms | 1.0%  
日本 | 1个 | 0 | 246ms | 0  
越南 | 2个 | 0 | 271ms | 1.0%  
柬埔寨 | 1个 | 0 | 272ms | 0  
台湾 | 1个 | 0 | 274ms | -  
菲律宾 | 1个 | 0 | 279ms | 0  
韩国 | 12个 | 0 | 287ms | 0  
澳大利亚 | 1个 | 0 | 321ms | 1.0%  
  
**简评：** 如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有85个，其中超时点0个，平均响应时间为172毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在50-100毫秒间的1个，在100-200毫秒间的4个，在200-300毫秒间的10个，超过300毫秒的1个；

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
    * [伦敦](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [纽约](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [新加坡](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [多伦多](/digitalocean/idc/toronto/20180527-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180527")
  * 到Digital Ocean法兰克福机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/frankfurt/20180514-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [20180622](/digitalocean/idc/frankfurt/20180622-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/frankfurt/20180804-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180527-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [Linode](/linode/idc/frankfurt/20180527-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180527")
    * [Vultr](/vultr/idc/frankfurt/20180527-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180527")



本文最初发表于[多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-digitalocean-idc-frankfurt.html)
