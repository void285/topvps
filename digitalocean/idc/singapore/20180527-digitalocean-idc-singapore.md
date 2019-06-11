#  多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean新加坡\[Singapore\]机房的Ping测试（20180527）](/images/thumbnails/to_do_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[新加坡-新加坡机房](https://vps123.top/digitalocean-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180527-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的979个有效测试样本中，共有超时点17个；响应均值为252毫秒，最快的三地区为青海、北京、湖南，最慢的三地区为吉林、四川、内蒙古；江苏、浙江、广东、贵州、陕西等11处有响应超时情况；上海、安徽、云南、重庆、江苏等30处丢包率较高。海外21个国家地区的86个有效测试样本中，无超时点；响应均值为159毫秒，最快的三地区为新加坡、印度尼西亚、马来西亚，最慢的三地区为意大利、南非、巴西。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_singapore-singapore_20180527_mainland.png)

**大陆各省份到Digital Ocean新加坡-新加坡机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
青海 | 3个 | 0 | 201ms | 6.7%  
北京 | 8个 | 1个 | 208ms | 6.7%  
湖南 | 43个 | 0 | 208ms | 11.4%  
黑龙江 | 39个 | 0 | 226ms | 9.3%  
浙江 | 51个 | 2个 | 227ms | 12.4%  
江西 | 24个 | 0 | 228ms | 14.5%  
广东 | 84个 | 2个 | 231ms | 11.6%  
广西 | 38个 | 0 | 232ms | 14.2%  
河南 | 58个 | 1个 | 233ms | 12.6%  
山东 | 53个 | 1个 | 233ms | 12.5%  
安徽 | 40个 | 0 | 233ms | 20.2%  
江苏 | 62个 | 3个 | 236ms | 17.2%  
天津 | 5个 | 0 | 236ms | 12.2%  
上海 | 7个 | 0 | 243ms | 24.8%  
海南 | 14个 | 0 | 243ms | 13.0%  
贵州 | 28个 | 2个 | 245ms | 12.7%  
福建 | 36个 | 1个 | 249ms | 15.8%  
均值 | 979个 | 17个 | 252ms | 13.8%  
云南 | 20个 | 0 | 260ms | 19.6%  
山西 | 36个 | 0 | 261ms | 9.1%  
湖北 | 43个 | 1个 | 269ms | 16.7%  
陕西 | 33个 | 2个 | 269ms | 13.0%  
宁夏 | 12个 | 0 | 274ms | 13.6%  
重庆 | 15个 | 0 | 278ms | 17.8%  
河北 | 36个 | 0 | 280ms | 13.3%  
新疆 | 29个 | 0 | 281ms | 10.0%  
甘肃 | 23个 | 0 | 283ms | 14.4%  
辽宁 | 39个 | 1个 | 297ms | 11.6%  
吉林 | 19个 | 0 | 298ms | 16.6%  
四川 | 48个 | 0 | 300ms | 16.7%  
内蒙古 | 33个 | 0 | 305ms | 15.2%  
  
**简评：** 如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有979个，其中超时点17个，平均响应时间为252毫秒，丢包率为13%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的29个，超过300毫秒的1个；  
超时点较多的省份：北京；  
丢包率较高的省份：湖南、浙江、江西、广东、广西、河南、山东、安徽、江苏、天津、上海、海南、贵州、福建、云南、湖北、陕西、宁夏、重庆、河北、新疆、甘肃、辽宁、吉林、四川、内蒙古；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_singapore-singapore_20180527_overseas.png)

**海外线路到Digital Ocean新加坡-新加坡机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
新加坡 | 6个 | 0 | 1ms | 0  
印度尼西亚 | 1个 | 0 | 24ms | 2.0%  
马来西亚 | 4个 | 0 | 50ms | 0  
越南 | 2个 | 0 | 62ms | 0  
香港 | 18个 | 0 | 70ms | 0  
日本 | 1个 | 0 | 81ms | 0  
柬埔寨 | 1个 | 0 | 93ms | 0  
台湾 | 1个 | 0 | 99ms | -  
菲律宾 | 1个 | 0 | 102ms | 0  
韩国 | 12个 | 0 | 113ms | 1.7%  
澳大利亚 | 2个 | 0 | 150ms | 0  
均值 | 86个 | 0 | 159ms | 0.4%  
法国 | 1个 | 0 | 174ms | 0  
荷兰 | 1个 | 0 | 179ms | 0  
英国 | 2个 | 0 | 180ms | 0  
美国 | 21个 | 0 | 181ms | 2.8%  
加拿大 | 4个 | 0 | 242ms | 0  
俄罗斯 | 1个 | 0 | 259ms | 0  
德国 | 3个 | 0 | 265ms | 0  
意大利 | 1个 | 0 | 328ms | -  
南非 | 2个 | 0 | 341ms | 0.5%  
巴西 | 1个 | 0 | 346ms | 0  
  
**简评：** 如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有86个，其中超时点0个，平均响应时间为159毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的5个，在100-200毫秒间的7个，在200-300毫秒间的3个，超过300毫秒的3个；

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
    * [纽约](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [多伦多](/digitalocean/idc/toronto/20180527-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180527")
  * 到Digital Ocean新加坡机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [20180622](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180527-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [Linode](/linode/idc/singapore/20180527-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180527")
    * [Vultr](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")



本文最初发表于[多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-digitalocean-idc-singapore.html)
