#  多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean新加坡\[Singapore\]机房的Ping测试（20180918）](/images/thumbnails/to_do_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[新加坡-新加坡机房](https://vps123.top/digitalocean-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180918-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Digital Ocean新加坡-新加坡机房的PING测试结果，连通概况如下：大陆31个省市的1353个有效测试样本中，共有超时点12个；响应均值为256毫秒，最快的三地区为广西、天津、湖南，最慢的三地区为宁夏、西藏、吉林；江苏、浙江、广东、贵州、山西有响应超时情况；吉林、辽宁、内蒙古、河南、重庆等17处丢包率较高。海外15个国家地区的56个有效测试样本中，无超时点；响应均值为166毫秒，最快的三地区为新加坡、马来西亚、越南，最慢的三地区为荷兰、意大利、赞比亚；菲律宾丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_singapore-singapore_20180918_mainland.png)

**大陆各省份到Digital Ocean新加坡-新加坡机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
广西 | 54个 | 0 | 169ms | 3.2%  
天津 | 6个 | 0 | 213ms | 2.8%  
湖南 | 67个 | 0 | 214ms | 3.7%  
陕西 | 43个 | 0 | 216ms | 3.5%  
安徽 | 71个 | 0 | 219ms | 3.3%  
福建 | 46个 | 0 | 224ms | 3.2%  
浙江 | 63个 | 3个 | 224ms | 7.0%  
江西 | 37个 | 0 | 233ms | 3.8%  
云南 | 26个 | 0 | 233ms | 2.8%  
广东 | 114个 | 3个 | 241ms | 4.9%  
黑龙江 | 53个 | 0 | 242ms | 14.4%  
河南 | 83个 | 0 | 250ms | 15.8%  
海南 | 14个 | 0 | 250ms | 8.1%  
均值 | 1353个 | 12个 | 256ms | 8.2%  
重庆 | 7个 | 0 | 257ms | 15.8%  
山东 | 93个 | 0 | 264ms | 11.4%  
江苏 | 86个 | 4个 | 264ms | 6.1%  
北京 | 7个 | 0 | 265ms | 3.0%  
贵州 | 39个 | 1个 | 266ms | 6.8%  
上海 | 8个 | 0 | 273ms | 7.5%  
河北 | 58个 | 0 | 275ms | 12.0%  
湖北 | 48个 | 0 | 276ms | 4.0%  
四川 | 69个 | 0 | 277ms | 5.4%  
甘肃 | 33个 | 0 | 284ms | 2.8%  
山西 | 47个 | 1个 | 287ms | 13.9%  
内蒙古 | 55个 | 0 | 289ms | 16.0%  
新疆 | 34个 | 0 | 317ms | 5.6%  
青海 | 5个 | 0 | 320ms | 2.7%  
辽宁 | 55个 | 0 | 333ms | 19.5%  
宁夏 | 6个 | 0 | 349ms | 0.7%  
西藏 | 4个 | 0 | 361ms | 6.8%  
吉林 | 22个 | 0 | 390ms | 21.9%  
  
**简评：** 如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有1353个，其中超时点12个，平均响应时间为256毫秒，丢包率为8%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的1个，在200-300毫秒间的24个，超过300毫秒的6个；  
丢包率较高的省份：黑龙江、河南、重庆、山东、河北、山西、内蒙古、辽宁、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_singapore-singapore_20180918_overseas.png)

**海外线路到Digital Ocean新加坡-新加坡机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
新加坡 | 4个 | 0 | 44ms | 0  
马来西亚 | 3个 | 0 | 52ms | 0  
越南 | 2个 | 0 | 53ms | 0  
日本 | 2个 | 0 | 75ms | 3.3%  
香港 | 15个 | 0 | 100ms | 0  
台湾 | 2个 | 0 | 117ms | 0  
美国 | 9个 | 0 | 140ms | 0  
韩国 | 7个 | 0 | 151ms | 0  
澳大利亚 | 2个 | 0 | 153ms | 0.5%  
均值 | 56个 | 0 | 166ms | 2.0%  
菲律宾 | 2个 | 0 | 176ms | 21.7%  
加拿大 | 2个 | 0 | 232ms | -  
德国 | 3个 | 0 | 234ms | 0  
荷兰 | 1个 | 0 | 253ms | 0  
意大利 | 1个 | 0 | 313ms | -  
赞比亚 | 1个 | 0 | 400ms | 0  
  
**简评：** 如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有56个，其中超时点0个，平均响应时间为166毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的4个，在100-200毫秒间的5个，在200-300毫秒间的3个，超过300毫秒的2个；  
丢包率较高的国家/地区：菲律宾；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180918 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180918 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180918-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
    * [班加罗尔](/digitalocean/idc/bangalore/20180918-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180918")
    * [法兰克福](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
    * [伦敦](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
    * [纽约](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")
    * [多伦多](/digitalocean/idc/toronto/20180918-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180918")
  * 到Digital Ocean新加坡机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180918-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
    * [Linode](/linode/idc/singapore/20180918-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180918")
    * [Vultr](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-digitalocean-idc-singapore.html)
