#  多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean法兰克福\[Frankfurt\]机房的Ping测试（20180918）](/images/thumbnails/to_do_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[德国-法兰克福机房](https://vps123.top/digitalocean-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180918-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Digital Ocean德国-法兰克福机房的PING测试结果，连通概况如下：大陆31个省市的1447个有效测试样本中，共有超时点11个；响应均值为286毫秒，最快的三地区为宁夏、青海、天津，最慢的三地区为黑龙江、西藏、吉林；江苏、浙江、山西、辽宁、广东等6处有响应超时情况；吉林、山西、西藏、河南、山东等21处丢包率较高。海外16个国家地区的59个有效测试样本中，无超时点；响应均值为188毫秒，最快的三地区为意大利、德国、荷兰，最慢的三地区为印度尼西亚、菲律宾、澳大利亚；菲律宾、赞比亚丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_germany-frankfurt_20180918_mainland.png)

**大陆各省份到Digital Ocean德国-法兰克福机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
宁夏 | 7个 | 0 | 226ms | 0.5%  
青海 | 5个 | 0 | 233ms | 0  
天津 | 6个 | 0 | 244ms | 3.0%  
浙江 | 67个 | 2个 | 250ms | 3.7%  
河北 | 59个 | 0 | 254ms | 8.3%  
内蒙古 | 60个 | 0 | 258ms | 11.8%  
甘肃 | 36个 | 0 | 261ms | 2.3%  
上海 | 8个 | 0 | 263ms | 9.4%  
江苏 | 93个 | 4个 | 266ms | 5.6%  
广西 | 62个 | 0 | 266ms | 8.3%  
陕西 | 44个 | 0 | 267ms | 7.2%  
辽宁 | 60个 | 1个 | 268ms | 12.7%  
湖北 | 54个 | 0 | 270ms | 4.9%  
云南 | 28个 | 0 | 270ms | 6.5%  
江西 | 40个 | 0 | 272ms | 3.6%  
北京 | 8个 | 0 | 273ms | 1.4%  
广东 | 123个 | 1个 | 275ms | 6.3%  
安徽 | 71个 | 0 | 275ms | 2.8%  
湖南 | 68个 | 0 | 276ms | 10.2%  
四川 | 73个 | 1个 | 286ms | 5.6%  
均值 | 1447个 | 11个 | 286ms | 8.5%  
福建 | 45个 | 0 | 287ms | 6.2%  
海南 | 14个 | 0 | 300ms | 4.2%  
贵州 | 44个 | 0 | 301ms | 7.7%  
山西 | 56个 | 2个 | 301ms | 15.6%  
重庆 | 8个 | 0 | 307ms | 13.1%  
山东 | 94个 | 0 | 314ms | 13.2%  
新疆 | 36个 | 0 | 324ms | 9.0%  
河南 | 92个 | 0 | 333ms | 14.0%  
黑龙江 | 60个 | 0 | 347ms | 13.1%  
西藏 | 4个 | 0 | 383ms | 14.3%  
吉林 | 22个 | 0 | 392ms | 16.6%  
  
**简评：** 如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有1447个，其中超时点11个，平均响应时间为286毫秒，丢包率为8%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的22个，超过300毫秒的9个；  
丢包率较高的省份：内蒙古、辽宁、湖南、山西、重庆、山东、河南、黑龙江、西藏、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_germany-frankfurt_20180918_overseas.png)

**海外线路到Digital Ocean德国-法兰克福机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
意大利 | 1个 | 0 | 11ms | -  
德国 | 3个 | 0 | 24ms | 0  
荷兰 | 1个 | 0 | 86ms | 0  
加拿大 | 2个 | 0 | 87ms | -  
新加坡 | 4个 | 0 | 161ms | 0  
美国 | 9个 | 0 | 161ms | 0  
香港 | 15个 | 0 | 163ms | 1.3%  
均值 | 59个 | 0 | 188ms | 3.3%  
台湾 | 2个 | 0 | 211ms | 0  
越南 | 2个 | 0 | 212ms | 0  
马来西亚 | 3个 | 0 | 224ms | 0  
赞比亚 | 2个 | 0 | 225ms | 7.7%  
韩国 | 8个 | 0 | 240ms | 0  
日本 | 2个 | 0 | 250ms | 1.7%  
印度尼西亚 | 1个 | 0 | 280ms | 3.3%  
菲律宾 | 2个 | 0 | 331ms | 31.7%  
澳大利亚 | 2个 | 0 | 339ms | 0.5%  
  
**简评：** 如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有59个，其中超时点0个，平均响应时间为188毫秒，丢包率为3%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的2个，在100-200毫秒间的3个，在200-300毫秒间的7个，超过300毫秒的2个；  
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
    * [伦敦](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
    * [纽约](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")
    * [新加坡](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
    * [多伦多](/digitalocean/idc/toronto/20180918-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180918")
  * 到Digital Ocean法兰克福机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/frankfurt/20180514-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/frankfurt/20180527-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/frankfurt/20180622-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/frankfurt/20180804-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180918-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
    * [Linode](/linode/idc/frankfurt/20180918-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180918")
    * [Vultr](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-digitalocean-idc-frankfurt.html)
