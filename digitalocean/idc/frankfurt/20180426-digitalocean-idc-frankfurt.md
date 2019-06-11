#  多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean法兰克福\[Frankfurt\]机房的Ping测试（20180426）](/images/thumbnails/to_do_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[德国-法兰克福机房](https://vps123.top/digitalocean-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180426-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Digital Ocean德国-法兰克福机房的PING测试结果，连通概况如下：大陆31个省市的820个有效测试样本中，共有超时点6个；响应均值为305毫秒，最快的三地区为天津、北京、上海，最慢的三地区为吉林、新疆、西藏；浙江、北京、河北、江苏、新疆有响应超时情况；甘肃、宁夏、安徽、江西、广西等29处丢包率较高。海外18个国家地区的80个有效测试样本中，共有超时点1个；响应均值为186毫秒，最快的三地区为德国、法国、荷兰，最慢的三地区为韩国、澳大利亚、柬埔寨；香港有响应超时情况；印度尼西亚、日本丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_germany-frankfurt_20180426_mainland.png)

**大陆各省份到Digital Ocean德国-法兰克福机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 5个 | 0 | 239ms | 6.8%  
北京 | 4个 | 1个 | 255ms | 8.3%  
上海 | 6个 | 0 | 257ms | 9.7%  
河北 | 28个 | 1个 | 268ms | 11.4%  
广东 | 54个 | 0 | 279ms | 8.2%  
重庆 | 9个 | 0 | 292ms | 9.3%  
辽宁 | 34个 | 0 | 292ms | 10.9%  
广西 | 34个 | 0 | 293ms | 11.8%  
河南 | 51个 | 0 | 297ms | 6.0%  
山西 | 32个 | 0 | 299ms | 5.9%  
陕西 | 29个 | 0 | 300ms | 8.8%  
甘肃 | 19个 | 0 | 300ms | 14.1%  
湖北 | 38个 | 0 | 301ms | 10.5%  
宁夏 | 11个 | 0 | 301ms | 13.3%  
云南 | 25个 | 0 | 302ms | 7.4%  
江西 | 23个 | 0 | 304ms | 12.3%  
内蒙古 | 29个 | 0 | 304ms | 4.9%  
湖南 | 41个 | 0 | 305ms | 6.7%  
均值 | 820个 | 6个 | 305ms | 9.3%  
福建 | 27个 | 0 | 306ms | 11.3%  
浙江 | 37个 | 2个 | 310ms | 8.9%  
安徽 | 37个 | 0 | 310ms | 13.3%  
海南 | 10个 | 0 | 316ms | 10.5%  
江苏 | 50个 | 1个 | 317ms | 8.8%  
山东 | 44个 | 0 | 318ms | 7.1%  
黑龙江 | 29个 | 0 | 322ms | 11.1%  
四川 | 44个 | 0 | 323ms | 10.0%  
贵州 | 23个 | 0 | 328ms | 9.4%  
青海 | 4个 | 0 | 334ms | 10.5%  
吉林 | 16个 | 0 | 337ms | 11.3%  
新疆 | 26个 | 1个 | 345ms | 8.6%  
西藏 | 1个 | 0 | 361ms | 5.0%  
  
**简评：** 如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有820个，其中超时点6个，平均响应时间为305毫秒，丢包率为9%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的12个，超过300毫秒的19个；  
超时点较多的省份：北京；  
丢包率较高的省份：河北、辽宁、广西、甘肃、湖北、宁夏、江西、福建、安徽、海南、黑龙江、四川、青海、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_germany-frankfurt_20180426_overseas.png)

**海外线路到Digital Ocean德国-法兰克福机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
德国 | 1个 | 0 | 1ms | 0  
法国 | 2个 | 0 | 9ms | 0  
荷兰 | 2个 | 0 | 11ms | 0  
英国 | 3个 | 0 | 41ms | 0  
俄罗斯 | 1个 | 0 | 94ms | 0  
加拿大 | 4个 | 0 | 104ms | 0  
美国 | 16个 | 0 | 156ms | 0  
南非 | 1个 | 0 | 175ms | 0  
新加坡 | 5个 | 0 | 180ms | 0  
均值 | 80个 | 1个 | 186ms | 2.4%  
印度尼西亚 | 1个 | 0 | 198ms | 25.0%  
香港 | 20个 | 1个 | 225ms | 0  
越南 | 1个 | 0 | 228ms | 1.0%  
马来西亚 | 4个 | 0 | 228ms | 0  
台湾 | 1个 | 0 | 281ms | -  
日本 | 3个 | 0 | 289ms | 7.3%  
韩国 | 12个 | 0 | 289ms | 0  
澳大利亚 | 2个 | 0 | 365ms | 5.0%  
柬埔寨 | 1个 | 0 | 472ms | 2.0%  
  
**简评：** 如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有80个，其中超时点1个，平均响应时间为186毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的6个，超过300毫秒的2个；  
丢包率较高的国家/地区：印度尼西亚；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180426 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180426 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180426-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180426")
    * [班加罗尔](/digitalocean/idc/bangalore/20180426-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180426")
    * [伦敦](/digitalocean/idc/london/20180426-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180426")
    * [纽约](/digitalocean/idc/newyork/20180426-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180426")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180426-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180426")
    * [新加坡](/digitalocean/idc/singapore/20180426-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180426")
    * [多伦多](/digitalocean/idc/toronto/20180426-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180426")
  * 到Digital Ocean法兰克福机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/frankfurt/20180514-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/frankfurt/20180527-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/frankfurt/20180622-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/frankfurt/20180804-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180426-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180426")
    * [Linode](/linode/idc/frankfurt/20180426-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180426")
    * [Vultr](/vultr/idc/frankfurt/20180426-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180426")



本文最初发表于[多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-digitalocean-idc-frankfurt.html)
