#  多地到Digital Ocean伦敦[London]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean伦敦\[London\]机房的Ping测试（20180918）](/images/thumbnails/to_do_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[英国-伦敦机房](https://vps123.top/digitalocean-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180918-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Digital Ocean英国-伦敦机房的PING测试结果，连通概况如下：大陆31个省市的1238个有效测试样本中，共有超时点10个；响应均值为286毫秒，最快的三地区为宁夏、浙江、河北，最慢的三地区为黑龙江、西藏、吉林；江苏、浙江、广东、福建、山西有响应超时情况；西藏、山西、吉林、黑龙江、河南等25处丢包率较高。海外16个国家地区的60个有效测试样本中，无超时点；响应均值为180毫秒，最快的三地区为意大利、德国、加拿大，最慢的三地区为日本、澳大利亚、菲律宾；菲律宾丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_uk-london_20180918_mainland.png)

**大陆各省份到Digital Ocean英国-伦敦机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
宁夏 | 6个 | 0 | 237ms | 0  
浙江 | 60个 | 2个 | 249ms | 3.8%  
河北 | 51个 | 0 | 250ms | 7.0%  
广西 | 48个 | 0 | 255ms | 6.1%  
内蒙古 | 49个 | 0 | 259ms | 7.9%  
安徽 | 68个 | 0 | 261ms | 5.3%  
天津 | 6个 | 0 | 262ms | 5.1%  
湖北 | 46个 | 0 | 270ms | 6.1%  
辽宁 | 46个 | 0 | 270ms | 8.4%  
甘肃 | 30个 | 0 | 273ms | 1.8%  
江西 | 36个 | 0 | 275ms | 6.7%  
湖南 | 63个 | 0 | 276ms | 8.5%  
广东 | 104个 | 2个 | 278ms | 7.6%  
陕西 | 40个 | 0 | 280ms | 7.7%  
江苏 | 79个 | 4个 | 281ms | 5.9%  
云南 | 23个 | 0 | 282ms | 7.7%  
北京 | 7个 | 0 | 283ms | 0.1%  
四川 | 62个 | 0 | 285ms | 3.2%  
上海 | 7个 | 0 | 286ms | 8.2%  
均值 | 1238个 | 10个 | 286ms | 7.7%  
福建 | 39个 | 1个 | 291ms | 7.5%  
青海 | 4个 | 0 | 294ms | 10.8%  
贵州 | 35个 | 0 | 299ms | 6.3%  
海南 | 13个 | 0 | 305ms | 4.2%  
山东 | 91个 | 0 | 310ms | 11.5%  
重庆 | 7个 | 0 | 314ms | 9.4%  
河南 | 78个 | 0 | 318ms | 11.9%  
山西 | 44个 | 1个 | 329ms | 13.6%  
新疆 | 30个 | 0 | 330ms | 7.0%  
黑龙江 | 42个 | 0 | 335ms | 12.2%  
西藏 | 4个 | 0 | 352ms | 18.0%  
吉林 | 20个 | 0 | 377ms | 13.2%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有1238个，其中超时点10个，平均响应时间为286毫秒，丢包率为7%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的22个，超过300毫秒的9个；  
丢包率较高的省份：青海、山东、河南、山西、黑龙江、西藏、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_uk-london_20180918_overseas.png)

**海外线路到Digital Ocean英国-伦敦机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
意大利 | 1个 | 0 | 11ms | -  
德国 | 3个 | 0 | 29ms | 0  
加拿大 | 2个 | 0 | 75ms | 0  
荷兰 | 1个 | 0 | 111ms | 0  
美国 | 8个 | 0 | 150ms | 0  
新加坡 | 4个 | 0 | 162ms | 0  
香港 | 14个 | 0 | 167ms | 0  
均值 | 60个 | 0 | 180ms | 1.0%  
台湾 | 2个 | 0 | 192ms | 0  
印度尼西亚 | 1个 | 0 | 201ms | 0  
马来西亚 | 6个 | 0 | 208ms | 0  
赞比亚 | 1个 | 0 | 209ms | 0  
越南 | 2个 | 0 | 225ms | 1.0%  
韩国 | 8个 | 0 | 226ms | 0  
日本 | 3个 | 0 | 251ms | 4.0%  
澳大利亚 | 2个 | 0 | 293ms | 1.7%  
菲律宾 | 2个 | 0 | 366ms | 8.3%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有60个，其中超时点0个，平均响应时间为180毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的7个，超过300毫秒的1个；

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
    * [纽约](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")
    * [新加坡](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
    * [多伦多](/digitalocean/idc/toronto/20180918-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180918")
  * 到Digital Ocean伦敦机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/london/20180622-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180918-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
    * [Linode](/linode/idc/london/20180918-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180918")
    * [Vultr](/vultr/idc/london/20180918-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean伦敦[London]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-digitalocean-idc-london.html)
