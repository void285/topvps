#  多地到Digital Ocean伦敦[London]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean伦敦\[London\]机房的Ping测试（20180527）](/images/thumbnails/to_do_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[英国-伦敦机房](https://vps123.top/digitalocean-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180527-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的974个有效测试样本中，共有超时点8个；响应均值为276毫秒，最快的三地区为上海、北京、天津，最慢的三地区为山东、黑龙江、新疆；北京、广东、辽宁、河南、四川等8处有响应超时情况；辽宁、湖南丢包率较高。海外21个国家地区的86个有效测试样本中，无超时点；响应均值为165毫秒，最快的三地区为荷兰、法国、意大利，最慢的三地区为菲律宾、韩国、澳大利亚。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_uk-london_20180527_mainland.png)

**大陆各省份到Digital Ocean英国-伦敦机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 8个 | 0 | 231ms | 0  
北京 | 8个 | 1个 | 243ms | 0  
天津 | 5个 | 0 | 247ms | 0  
广东 | 84个 | 1个 | 260ms | 0.5%  
海南 | 14个 | 0 | 261ms | 2.4%  
湖北 | 43个 | 0 | 262ms | 2.4%  
宁夏 | 12个 | 0 | 263ms | 0.3%  
安徽 | 40个 | 0 | 263ms | 1.8%  
辽宁 | 41个 | 1个 | 263ms | 13.5%  
广西 | 37个 | 0 | 264ms | 2.2%  
内蒙古 | 31个 | 0 | 264ms | 0  
江西 | 24个 | 0 | 266ms | 0.8%  
重庆 | 14个 | 0 | 266ms | 2.6%  
河北 | 33个 | 0 | 269ms | 2.2%  
云南 | 22个 | 0 | 270ms | 4.4%  
河南 | 54个 | 1个 | 273ms | 0.5%  
甘肃 | 23个 | 0 | 274ms | 0.3%  
湖南 | 45个 | 0 | 275ms | 6.7%  
均值 | 974个 | 8个 | 276ms | 2.1%  
四川 | 47个 | 1个 | 278ms | 0.8%  
浙江 | 52个 | 0 | 279ms | 0.7%  
江苏 | 62个 | 1个 | 281ms | 0.3%  
福建 | 35个 | 0 | 283ms | 1.8%  
山西 | 37个 | 0 | 283ms | 0.7%  
陕西 | 33个 | 0 | 284ms | 1.9%  
青海 | 3个 | 0 | 291ms | 0  
贵州 | 28个 | 0 | 292ms | 3.7%  
吉林 | 19个 | 0 | 298ms | 2.1%  
山东 | 53个 | 1个 | 306ms | 1.4%  
黑龙江 | 39个 | 1个 | 308ms | 1.1%  
新疆 | 28个 | 0 | 314ms | 1.8%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有974个，其中超时点8个，平均响应时间为276毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的27个，超过300毫秒的3个；  
超时点较多的省份：北京；  
丢包率较高的省份：辽宁；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_uk-london_20180527_overseas.png)

**海外线路到Digital Ocean英国-伦敦机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
荷兰 | 1个 | 0 | 8ms | 0  
法国 | 1个 | 0 | 9ms | 0  
意大利 | 1个 | 0 | 11ms | -  
德国 | 3个 | 0 | 20ms | 0  
英国 | 2个 | 0 | 27ms | 0  
加拿大 | 3个 | 0 | 88ms | 0  
俄罗斯 | 1个 | 0 | 109ms | 0  
美国 | 21个 | 0 | 137ms | 0  
均值 | 86个 | 0 | 165ms | 0.2%  
新加坡 | 6个 | 0 | 166ms | 0  
南非 | 2个 | 0 | 183ms | 1.0%  
巴西 | 1个 | 0 | 197ms | 0  
马来西亚 | 4个 | 0 | 213ms | 0  
香港 | 19个 | 0 | 215ms | 1.7%  
印度尼西亚 | 1个 | 0 | 219ms | 2.0%  
日本 | 1个 | 0 | 233ms | 0  
柬埔寨 | 1个 | 0 | 254ms | 0  
越南 | 2个 | 0 | 259ms | 0  
台湾 | 1个 | 0 | 270ms | -  
菲律宾 | 1个 | 0 | 270ms | 0  
韩国 | 12个 | 0 | 282ms | 0  
澳大利亚 | 2个 | 0 | 300ms | 0  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有86个，其中超时点0个，平均响应时间为165毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的10个；

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
    * [纽约](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [新加坡](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [多伦多](/digitalocean/idc/toronto/20180527-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180527")
  * 到Digital Ocean伦敦机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [20180622](/digitalocean/idc/london/20180622-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180527-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [Linode](/linode/idc/london/20180527-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180527")
    * [Vultr](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")



本文最初发表于[多地到Digital Ocean伦敦[London]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-digitalocean-idc-london.html)
