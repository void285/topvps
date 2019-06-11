#  多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean新加坡\[Singapore\]机房的Ping测试（20180804）](/images/thumbnails/to_do_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[新加坡-新加坡机房](https://vps123.top/digitalocean-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180804-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的4917个有效测试样本中，共有超时点77个；响应均值为298毫秒，最快的三地区为重庆、黑龙江、湖南，最慢的三地区为辽宁、新疆、吉林；江苏、浙江、广东、江西、福建等12处有响应超时情况；江西、福建、安徽、重庆、上海等31处丢包率较高。海外18个国家地区的237个有效测试样本中，共有超时点6个；响应均值为159毫秒，最快的三地区为印度尼西亚、新加坡、台湾，最慢的三地区为加拿大、菲律宾、意大利；香港、韩国有响应超时情况；菲律宾、美国丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_singapore-singapore_20180804_mainland.png)

**大陆各省份到Digital Ocean新加坡-新加坡机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
重庆 | 37个 | 3个 | 235ms | 25.3%  
黑龙江 | 156个 | 0 | 242ms | 5.1%  
湖南 | 241个 | 3个 | 254ms | 7.3%  
安徽 | 206个 | 0 | 259ms | 27.2%  
浙江 | 222个 | 10个 | 267ms | 23.4%  
广东 | 409个 | 9个 | 268ms | 5.5%  
湖北 | 177个 | 0 | 271ms | 7.6%  
陕西 | 145个 | 3个 | 274ms | 10.5%  
贵州 | 126个 | 4个 | 279ms | 6.3%  
云南 | 119个 | 0 | 279ms | 13.7%  
江苏 | 334个 | 18个 | 281ms | 19.3%  
海南 | 32个 | 0 | 289ms | 9.9%  
江西 | 131个 | 8个 | 291ms | 30.2%  
北京 | 36个 | 0 | 291ms | 8.2%  
山东 | 358个 | 0 | 292ms | 11.4%  
福建 | 152个 | 6个 | 292ms | 27.6%  
广西 | 227个 | 0 | 293ms | 8.7%  
天津 | 24个 | 0 | 294ms | 8.3%  
河南 | 327个 | 0 | 296ms | 10.8%  
上海 | 31个 | 4个 | 297ms | 24.1%  
四川 | 269个 | 0 | 298ms | 8.9%  
均值 | 4917个 | 77个 | 298ms | 12.6%  
河北 | 228个 | 0 | 301ms | 7.0%  
山西 | 169个 | 3个 | 348ms | 9.7%  
甘肃 | 104个 | 0 | 351ms | 14.3%  
内蒙古 | 204个 | 0 | 354ms | 9.5%  
青海 | 16个 | 0 | 366ms | 17.0%  
宁夏 | 32个 | 0 | 370ms | 17.2%  
西藏 | 4个 | 0 | 373ms | 20.0%  
辽宁 | 210个 | 6个 | 382ms | 12.7%  
新疆 | 123个 | 0 | 412ms | 14.9%  
吉林 | 68个 | 0 | 421ms | 11.9%  
  
**简评：** 如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有4917个，其中超时点77个，平均响应时间为298毫秒，丢包率为12%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的21个，超过300毫秒的10个；  
超时点较多的省份：上海；  
丢包率较高的省份：重庆、安徽、浙江、陕西、云南、江苏、江西、山东、福建、河南、上海、甘肃、青海、宁夏、西藏、辽宁、新疆、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_singapore-singapore_20180804_overseas.png)

**海外线路到Digital Ocean新加坡-新加坡机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
印度尼西亚 | 6个 | 0 | 28ms | 1.0%  
新加坡 | 15个 | 0 | 33ms | 0  
台湾 | 3个 | 0 | 73ms | 0  
马来西亚 | 12个 | 0 | 74ms | 1.3%  
香港 | 66个 | 3个 | 89ms | 0  
日本 | 6个 | 0 | 101ms | 1.7%  
澳大利亚 | 6个 | 0 | 109ms | 0  
韩国 | 21个 | 3个 | 113ms | 0  
均值 | 237个 | 6个 | 159ms | 1.5%  
美国 | 48个 | 0 | 164ms | 5.5%  
荷兰 | 3个 | 0 | 185ms | 0  
巴西 | 3个 | 0 | 191ms | 0  
俄罗斯 | 3个 | 0 | 208ms | -  
南非 | 6个 | 0 | 210ms | 0.5%  
德国 | 9个 | 0 | 229ms | 0  
英国 | 6个 | 0 | 236ms | 1.0%  
加拿大 | 15个 | 0 | 245ms | 0  
菲律宾 | 6个 | 0 | 264ms | 13.0%  
意大利 | 3个 | 0 | 314ms | -  
  
**简评：** 如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有237个，其中超时点6个，平均响应时间为159毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的3个，在100-200毫秒间的6个，在200-300毫秒间的6个，超过300毫秒的1个；  
超时点较多的国家/地区：韩国；  
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
    * [伦敦](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [纽约](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [多伦多](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")
  * 到Digital Ocean新加坡机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [20180918](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180804-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [Linode](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")
    * [Vultr](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")



本文最初发表于[多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-digitalocean-idc-singapore.html)
