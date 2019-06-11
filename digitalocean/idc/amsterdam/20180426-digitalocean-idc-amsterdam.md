#  多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean阿姆斯特丹\[Amsterdam\]机房的Ping测试（20180426）](/images/thumbnails/to_do_Amsterdam.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[荷兰-阿姆斯特丹机房](https://vps123.top/digitalocean-facilities.html#amsterdam)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的荷兰-阿姆斯特丹机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180426-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Digital Ocean荷兰-阿姆斯特丹机房的PING测试结果，连通概况如下：大陆31个省市的1623个有效测试样本中，共有超时点14个；响应均值为307毫秒，最快的三地区为天津、上海、北京，最慢的三地区为云南、贵州、西藏；浙江、内蒙古、江苏、广东、北京等8处有响应超时情况；黑龙江、贵州、安徽丢包率较高。海外17个国家地区的154个有效测试样本中，共有超时点1个；响应均值为185毫秒，最快的三地区为荷兰、法国、德国，最慢的三地区为台湾、澳大利亚、柬埔寨；美国有响应超时情况；柬埔寨丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_netherlands-amsterdam_20180426_mainland.png)

**大陆各省份到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 10个 | 0 | 229ms | 0  
上海 | 12个 | 0 | 239ms | 0.3%  
北京 | 8个 | 1个 | 249ms | 1.4%  
河北 | 57个 | 0 | 276ms | 1.6%  
辽宁 | 70个 | 0 | 277ms | 2.5%  
江西 | 45个 | 0 | 284ms | 2.5%  
福建 | 48个 | 0 | 286ms | 1.5%  
甘肃 | 38个 | 0 | 286ms | 0.5%  
宁夏 | 22个 | 1个 | 288ms | 1.7%  
安徽 | 78个 | 0 | 288ms | 5.6%  
浙江 | 76个 | 4个 | 295ms | 0.7%  
陕西 | 53个 | 1个 | 295ms | 0.7%  
河南 | 102个 | 0 | 299ms | 0.7%  
内蒙古 | 61个 | 2个 | 300ms | 0.8%  
青海 | 8个 | 0 | 302ms | 0.1%  
江苏 | 100个 | 2个 | 302ms | 0.8%  
广东 | 113个 | 2个 | 307ms | 1.0%  
均值 | 1623个 | 14个 | 307ms | 2.2%  
山西 | 65个 | 0 | 313ms | 2.0%  
广西 | 66个 | 0 | 318ms | 4.2%  
湖北 | 73个 | 0 | 319ms | 2.9%  
重庆 | 18个 | 0 | 319ms | 2.0%  
山东 | 86个 | 0 | 320ms | 2.1%  
海南 | 20个 | 0 | 321ms | 1.8%  
湖南 | 81个 | 1个 | 327ms | 3.3%  
新疆 | 53个 | 0 | 328ms | 0.8%  
吉林 | 28个 | 0 | 332ms | 2.8%  
四川 | 87个 | 0 | 333ms | 2.0%  
黑龙江 | 59个 | 0 | 334ms | 5.8%  
云南 | 37个 | 0 | 338ms | 2.3%  
贵州 | 47个 | 0 | 347ms | 5.8%  
西藏 | 2个 | 0 | 385ms | 0.5%  
  
**简评：** 如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有1623个，其中超时点14个，平均响应时间为307毫秒，丢包率为2%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的14个，超过300毫秒的17个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_netherlands-amsterdam_20180426_overseas.png)

**海外线路到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
荷兰 | 4个 | 0 | 1ms | 0  
法国 | 4个 | 0 | 8ms | 0  
德国 | 2个 | 0 | 12ms | 0  
英国 | 6个 | 0 | 19ms | 0  
加拿大 | 7个 | 0 | 98ms | 0  
俄罗斯 | 2个 | 0 | 102ms | 0  
美国 | 32个 | 1个 | 140ms | 0  
南非 | 2个 | 0 | 167ms | 0  
马来西亚 | 6个 | 0 | 184ms | 0  
均值 | 154个 | 1个 | 185ms | 2.1%  
新加坡 | 10个 | 0 | 193ms | 0  
越南 | 2个 | 0 | 230ms | 0  
日本 | 5个 | 0 | 260ms | 0.2%  
香港 | 40个 | 0 | 271ms | 0  
韩国 | 24个 | 0 | 290ms | 0.3%  
台湾 | 2个 | 0 | 305ms | -  
澳大利亚 | 4个 | 0 | 317ms | 0  
柬埔寨 | 2个 | 0 | 554ms | 32.5%  
  
**简评：** 如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有154个，其中超时点1个，平均响应时间为185毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的4个，超过300毫秒的3个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180426 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180426 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [班加罗尔](/digitalocean/idc/bangalore/20180426-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180426")
    * [法兰克福](/digitalocean/idc/frankfurt/20180426-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180426")
    * [伦敦](/digitalocean/idc/london/20180426-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180426")
    * [纽约](/digitalocean/idc/newyork/20180426-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180426")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180426-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180426")
    * [新加坡](/digitalocean/idc/singapore/20180426-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180426")
    * [多伦多](/digitalocean/idc/toronto/20180426-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180426")
  * 到Digital Ocean阿姆斯特丹机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/amsterdam/20180527-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/amsterdam/20180622-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/amsterdam/20180804-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/amsterdam/20180918-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
  * 本期报告：在阿姆斯特丹部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/amsterdam/20180426-bwg-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180426")
    * [Digital Ocean](do/idc/amsterdam/20180426-do-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180426")
    * [Vultr](/vultr/idc/amsterdam/20180426-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180426")



本文最初发表于[多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-digitalocean-idc-amsterdam.html)
