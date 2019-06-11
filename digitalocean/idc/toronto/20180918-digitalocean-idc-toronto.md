#  多地到Digital Ocean多伦多[Toronto]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean多伦多\[Toronto\]机房的Ping测试（20180918）](/images/thumbnails/to_do_Toronto.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[加拿大-多伦多机房](https://vps123.top/digitalocean-facilities.html#toronto)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的加拿大-多伦多机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180918-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Digital Ocean加拿大-多伦多机房的PING测试结果，连通概况如下：大陆31个省市的1238个有效测试样本中，共有超时点15个；响应均值为283毫秒，最快的三地区为北京、上海、天津，最慢的三地区为青海、新疆、西藏；江苏、浙江、广东、山西、辽宁等6处有响应超时情况；黑龙江、河南、吉林、山西、辽宁等18处丢包率较高。海外16个国家地区的63个有效测试样本中，无超时点；响应均值为193毫秒，最快的三地区为加拿大、意大利、美国，最慢的三地区为马来西亚、印度尼西亚、菲律宾；日本、菲律宾、赞比亚丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于多伦多\[Toronto\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_canada-toronto_20180918_mainland.png)

**大陆各省份到Digital Ocean加拿大-多伦多机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
北京 | 8个 | 0 | 248ms | 6.4%  
上海 | 6个 | 0 | 248ms | 2.0%  
天津 | 6个 | 0 | 257ms | 0  
广西 | 49个 | 0 | 258ms | 2.0%  
浙江 | 59个 | 3个 | 266ms | 6.2%  
重庆 | 7个 | 0 | 266ms | 13.1%  
广东 | 101个 | 3个 | 268ms | 4.5%  
湖南 | 61个 | 0 | 270ms | 5.1%  
安徽 | 65个 | 0 | 270ms | 2.3%  
福建 | 42个 | 0 | 273ms | 4.3%  
河北 | 50个 | 0 | 275ms | 11.3%  
贵州 | 37个 | 0 | 279ms | 3.8%  
江苏 | 81个 | 5个 | 279ms | 8.2%  
山东 | 86个 | 0 | 282ms | 13.0%  
海南 | 13个 | 0 | 282ms | 1.8%  
湖北 | 50个 | 0 | 283ms | 6.0%  
均值 | 1238个 | 15个 | 283ms | 8.2%  
江西 | 37个 | 0 | 285ms | 5.3%  
山西 | 44个 | 2个 | 285ms | 14.6%  
云南 | 21个 | 0 | 286ms | 2.7%  
河南 | 79个 | 0 | 288ms | 16.5%  
辽宁 | 49个 | 1个 | 288ms | 13.7%  
内蒙古 | 49个 | 0 | 292ms | 12.7%  
陕西 | 41个 | 1个 | 293ms | 5.4%  
四川 | 62个 | 0 | 298ms | 4.6%  
吉林 | 19个 | 0 | 301ms | 16.2%  
宁夏 | 5个 | 0 | 303ms | 0.6%  
黑龙江 | 42个 | 0 | 304ms | 19.4%  
甘肃 | 30个 | 0 | 306ms | 2.0%  
青海 | 5个 | 0 | 321ms | 10.4%  
新疆 | 30个 | 0 | 323ms | 9.9%  
西藏 | 4个 | 0 | 404ms | 4.5%  
  
**简评：** 如果你考虑在Digital Ocean的多伦多[Toronto]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于多伦多[Toronto]的机房的连通状况。到此机房的ping监测点共有1238个，其中超时点15个，平均响应时间为283毫秒，丢包率为8%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的24个，超过300毫秒的7个；  
丢包率较高的省份：重庆、河北、山东、山西、河南、辽宁、内蒙古、吉林、黑龙江、青海；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于多伦多\[Toronto\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_canada-toronto_20180918_overseas.png)

**海外线路到Digital Ocean加拿大-多伦多机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 3个 | 0 | 7ms | 0  
意大利 | 1个 | 0 | 81ms | -  
美国 | 9个 | 0 | 102ms | 0  
德国 | 3个 | 0 | 116ms | 0  
台湾 | 2个 | 0 | 127ms | 0  
韩国 | 8个 | 0 | 171ms | 0  
均值 | 63个 | 0 | 193ms | 2.5%  
荷兰 | 1个 | 0 | 195ms | 0  
香港 | 15个 | 0 | 198ms | 0  
日本 | 3个 | 0 | 202ms | 20.3%  
新加坡 | 4个 | 0 | 202ms | 0  
越南 | 2个 | 0 | 242ms | 0  
澳大利亚 | 2个 | 0 | 264ms | 0  
赞比亚 | 1个 | 0 | 282ms | 6.7%  
马来西亚 | 6个 | 0 | 286ms | 0  
印度尼西亚 | 1个 | 0 | 288ms | 1.0%  
菲律宾 | 2个 | 0 | 327ms | 10.0%  
  
**简评：** 如果你考虑在Digital Ocean的多伦多[Toronto]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于多伦多[Toronto]的机房的连通状况。到此机房的ping监测点共有63个，其中超时点0个，平均响应时间为193毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的6个，在200-300毫秒间的7个，超过300毫秒的1个；  
丢包率较高的国家/地区：日本、菲律宾；

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
    * [新加坡](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
  * 到Digital Ocean多伦多机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/toronto/20180514-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/toronto/20180527-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/toronto/20180622-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")



本文最初发表于[多地到Digital Ocean多伦多[Toronto]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-digitalocean-idc-toronto.html)
