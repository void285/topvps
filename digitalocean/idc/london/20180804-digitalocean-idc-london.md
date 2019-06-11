#  多地到Digital Ocean伦敦[London]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean伦敦\[London\]机房的Ping测试（20180804）](/images/thumbnails/to_do_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[英国-伦敦机房](https://vps123.top/digitalocean-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180804-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的4802个有效测试样本中，共有超时点24个；响应均值为291毫秒，最快的三地区为广西、河北、重庆，最慢的三地区为新疆、青海、西藏；江苏、浙江、江西、上海有响应超时情况；西藏、云南、宁夏、安徽丢包率较高。海外19个国家地区的237个有效测试样本中，共有超时点3个；响应均值为170毫秒，最快的三地区为巴西、意大利、德国，最慢的三地区为澳大利亚、法国、菲律宾；香港有响应超时情况；菲律宾丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_uk-london_20180804_mainland.png)

**大陆各省份到Digital Ocean英国-伦敦机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
广西 | 216个 | 0 | 261ms | 1.6%  
河北 | 220个 | 0 | 261ms | 3.0%  
重庆 | 37个 | 0 | 264ms | 2.8%  
天津 | 16个 | 0 | 265ms | 2.0%  
海南 | 32个 | 0 | 269ms | 3.6%  
湖北 | 177个 | 0 | 277ms | 2.7%  
江西 | 127个 | 4个 | 278ms | 1.4%  
辽宁 | 210个 | 0 | 278ms | 1.6%  
内蒙古 | 200个 | 0 | 280ms | 1.9%  
福建 | 157个 | 0 | 281ms | 2.1%  
湖南 | 233个 | 0 | 281ms | 3.0%  
上海 | 24个 | 4个 | 281ms | 0.2%  
安徽 | 195个 | 0 | 283ms | 5.3%  
四川 | 262个 | 0 | 284ms | 1.1%  
云南 | 115个 | 0 | 286ms | 6.1%  
甘肃 | 104个 | 0 | 289ms | 1.1%  
均值 | 4802个 | 24个 | 291ms | 2.4%  
浙江 | 218个 | 7个 | 292ms | 0.8%  
陕西 | 138个 | 0 | 292ms | 1.0%  
广东 | 407个 | 0 | 292ms | 3.1%  
山西 | 165个 | 0 | 295ms | 1.4%  
江苏 | 339个 | 9个 | 298ms | 0.8%  
北京 | 36个 | 0 | 300ms | 0.6%  
宁夏 | 32个 | 0 | 300ms | 6.0%  
河南 | 319个 | 0 | 306ms | 3.6%  
黑龙江 | 152个 | 0 | 308ms | 2.8%  
吉林 | 68个 | 0 | 309ms | 0  
山东 | 326个 | 0 | 315ms | 2.8%  
贵州 | 130个 | 0 | 323ms | 2.9%  
新疆 | 123个 | 0 | 323ms | 1.2%  
青海 | 16个 | 0 | 343ms | 0  
西藏 | 8个 | 0 | 464ms | 34.2%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有4802个，其中超时点24个，平均响应时间为291毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的23个，超过300毫秒的8个；  
超时点较多的省份：上海；  
丢包率较高的省份：西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_uk-london_20180804_overseas.png)

**海外线路到Digital Ocean英国-伦敦机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
巴西 | 3个 | 0 | 1ms | 0  
意大利 | 3个 | 0 | 10ms | -  
德国 | 9个 | 0 | 27ms | 0  
俄罗斯 | 3个 | 0 | 49ms | -  
英国 | 6个 | 0 | 52ms | 0  
加拿大 | 15个 | 0 | 85ms | 0  
荷兰 | 3个 | 0 | 128ms | 0  
美国 | 48个 | 0 | 154ms | 3.8%  
均值 | 237个 | 3个 | 170ms | 1.3%  
新加坡 | 15个 | 0 | 174ms | 0  
南非 | 6个 | 0 | 189ms | 0.5%  
香港 | 66个 | 3个 | 191ms | 0  
印度尼西亚 | 6个 | 0 | 209ms | 0  
马来西亚 | 12个 | 0 | 210ms | 2.0%  
台湾 | 3个 | 0 | 242ms | 0  
韩国 | 21个 | 0 | 266ms | 0  
日本 | 3个 | 0 | 282ms | 1.0%  
澳大利亚 | 6个 | 0 | 291ms | 1.7%  
法国 | 3个 | 0 | 306ms | 0  
菲律宾 | 6个 | 0 | 368ms | 13.5%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有237个，其中超时点3个，平均响应时间为170毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的2个，在100-200毫秒间的5个，在200-300毫秒间的6个，超过300毫秒的2个；  
丢包率较高的国家/地区：菲律宾；

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
    * [纽约](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [新加坡](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [多伦多](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")
  * 到Digital Ocean伦敦机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/london/20180622-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [20180918](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180804-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [Linode](/linode/idc/london/20180804-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180804")
    * [Vultr](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")



本文最初发表于[多地到Digital Ocean伦敦[London]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-digitalocean-idc-london.html)
