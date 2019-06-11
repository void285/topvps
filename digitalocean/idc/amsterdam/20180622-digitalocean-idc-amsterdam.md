#  多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean阿姆斯特丹\[Amsterdam\]机房的Ping测试（20180622）](/images/thumbnails/to_do_Amsterdam.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[荷兰-阿姆斯特丹机房](https://vps123.top/digitalocean-facilities.html#amsterdam)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的荷兰-阿姆斯特丹机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180622-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的1747个有效测试样本中，共有超时点49个；响应均值为296毫秒，最快的三地区为天津、浙江、上海，最慢的三地区为四川、新疆、香港；云南、香港、浙江、江苏、河南等16处有响应超时情况；青海、甘肃、宁夏、新疆、贵州等8处丢包率较高。海外18个国家地区的173个有效测试样本中，共有超时点5个；响应均值为175毫秒，最快的三地区为德国、意大利、法国，最慢的三地区为越南、澳大利亚、柬埔寨；香港有响应超时情况。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_netherlands-amsterdam_20180622_mainland.png)

**大陆各省份到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180622]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 6个 | 0 | 240ms | 4.1%  
浙江 | 101个 | 4个 | 258ms | 1.7%  
上海 | 14个 | 2个 | 261ms | 1.3%  
江苏 | 128个 | 4个 | 265ms | 0.8%  
河北 | 57个 | 0 | 270ms | 2.3%  
安徽 | 70个 | 2个 | 271ms | 1.9%  
北京 | 19个 | 0 | 275ms | 2.0%  
广东 | 144个 | 2个 | 277ms | 1.2%  
江西 | 44个 | 0 | 283ms | 1.8%  
福建 | 59个 | 0 | 285ms | 1.7%  
重庆 | 24个 | 1个 | 288ms | 1.6%  
内蒙古 | 65个 | 0 | 288ms | 4.7%  
辽宁 | 66个 | 2个 | 294ms | 5.5%  
均值 | 1747个 | 49个 | 296ms | 3.1%  
广西 | 87个 | 1个 | 298ms | 2.4%  
河南 | 97个 | 3个 | 303ms | 5.5%  
山西 | 66个 | 1个 | 303ms | 4.4%  
湖北 | 68个 | 0 | 306ms | 1.8%  
陕西 | 54个 | 1个 | 306ms | 4.4%  
宁夏 | 28个 | 0 | 310ms | 6.5%  
海南 | 20个 | 0 | 310ms | 2.5%  
青海 | 10个 | 0 | 312ms | 8.5%  
湖南 | 70个 | 0 | 312ms | 3.1%  
甘肃 | 33个 | 0 | 313ms | 6.8%  
山东 | 81个 | 0 | 317ms | 1.1%  
黑龙江 | 49个 | 0 | 317ms | 5.3%  
贵州 | 44个 | 2个 | 317ms | 5.6%  
云南 | 46个 | 17个 | 326ms | 1.1%  
吉林 | 27个 | 1个 | 327ms | 3.3%  
四川 | 79个 | 0 | 340ms | 2.7%  
新疆 | 43个 | 1个 | 341ms | 6.3%  
香港 | 48个 | 5个 | - | -  
  
**简评：** 如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有1747个，其中超时点49个，平均响应时间为296毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的14个，超过300毫秒的16个；  
超时点较多的省份：上海、云南、香港；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_netherlands-amsterdam_20180622_overseas.png)

**海外线路到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180622]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
德国 | 2个 | 0 | 6ms | -  
意大利 | 2个 | 0 | 7ms | -  
法国 | 2个 | 0 | 8ms | 0  
巴西 | 2个 | 0 | 13ms | 0  
加拿大 | 4个 | 0 | 99ms | 0  
英国 | 3个 | 0 | 130ms | 0  
美国 | 41个 | 0 | 131ms | 0  
新加坡 | 10个 | 0 | 170ms | 0  
均值 | 173个 | 5个 | 175ms | 0.3%  
南非 | 4个 | 0 | 178ms | 0.5%  
香港 | 48个 | 5个 | 214ms | 0  
菲律宾 | 4个 | 0 | 245ms | 0  
韩国 | 28个 | 0 | 262ms | 0.3%  
台湾 | 4个 | 0 | 262ms | 0  
马来西亚 | 7个 | 0 | 265ms | 0.1%  
日本 | 4个 | 0 | 267ms | 3.5%  
越南 | 4个 | 0 | 286ms | 0  
澳大利亚 | 2个 | 0 | 296ms | 0  
柬埔寨 | 2个 | 0 | 312ms | 0  
  
**简评：** 如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有173个，其中超时点5个，平均响应时间为175毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的1个，在100-200毫秒间的4个，在200-300毫秒间的8个，超过300毫秒的1个；  
超时点较多的国家/地区：香港；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180622 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180622 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [班加罗尔](/digitalocean/idc/bangalore/20180622-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180622")
    * [法兰克福](/digitalocean/idc/frankfurt/20180622-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [伦敦](/digitalocean/idc/london/20180622-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [纽约](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [新加坡](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [多伦多](/digitalocean/idc/toronto/20180622-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180622")
  * 到Digital Ocean阿姆斯特丹机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/amsterdam/20180527-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180527")
    * [20180804](/digitalocean/idc/amsterdam/20180804-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/amsterdam/20180918-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
  * 本期报告：在阿姆斯特丹部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/amsterdam/20180622-bwg-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180622")
    * [Digital Ocean](do/idc/amsterdam/20180622-do-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180622")
    * [Vultr](/vultr/idc/amsterdam/20180622-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180622")



本文最初发表于[多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-digitalocean-idc-amsterdam.html)
