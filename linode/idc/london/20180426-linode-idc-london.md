#  多地到Linode伦敦[London]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode伦敦\[London\]机房的Ping测试（20180426）](/images/thumbnails/to_linode_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[英国-伦敦机房](https://vps123.top/linode-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180426-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Linode英国-伦敦机房的PING测试结果，连通概况如下：大陆31个省市的817个有效测试样本中，共有超时点9个；响应均值为314毫秒，最快的三地区为上海、浙江、天津，最慢的三地区为青海、新疆、西藏；浙江、江苏、湖南、内蒙古、吉林等8处有响应超时情况；西藏、重庆、江苏、上海、河南等31处丢包率较高。海外19个国家地区的79个有效测试样本中，无超时点；响应均值为179毫秒，最快的三地区为荷兰、法国、英国，最慢的三地区为韩国、澳大利亚、柬埔寨；德国、柬埔寨丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_idc_linode_uk-london_20180426_mainland.png)

大陆各省份到Linode英国-伦敦机房的测速数据 [20180426] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 8个 | 0 | 270ms | 19.4% | 内蒙古 | 30个 | 1个 | 313ms | 12.9%  
浙江 | 38个 | 2个 | 288ms | 11.3% | 均值 | 817个 | 9个 | 314ms | 13.7%  
天津 | 5个 | 0 | 289ms | 13.3% | 吉林 | 15个 | 1个 | 315ms | 11.5%  
安徽 | 40个 | 0 | 295ms | 14.9% | 北京 | 4个 | 1个 | 317ms | 8.7%  
海南 | 12个 | 0 | 296ms | 10.0% | 辽宁 | 34个 | 0 | 318ms | 12.6%  
河北 | 26个 | 0 | 300ms | 12.8% | 重庆 | 8个 | 0 | 319ms | 21.4%  
广西 | 33个 | 0 | 301ms | 14.7% | 陕西 | 25个 | 0 | 320ms | 15.6%  
江西 | 19个 | 0 | 302ms | 12.7% | 甘肃 | 20个 | 0 | 326ms | 14.3%  
四川 | 42个 | 0 | 305ms | 10.6% | 河南 | 48个 | 0 | 327ms | 17.7%  
湖北 | 39个 | 0 | 306ms | 13.5% | 山西 | 31个 | 0 | 329ms | 15.2%  
江苏 | 48个 | 1个 | 307ms | 20.1% | 贵州 | 22个 | 0 | 332ms | 14.2%  
山东 | 46个 | 0 | 308ms | 7.6% | 云南 | 25个 | 0 | 336ms | 14.5%  
广东 | 57个 | 0 | 308ms | 11.2% | 黑龙江 | 32个 | 0 | 338ms | 17.3%  
宁夏 | 10个 | 0 | 309ms | 11.5% | 青海 | 4个 | 1个 | 342ms | 16.3%  
福建 | 27个 | 0 | 311ms | 11.4% | 新疆 | 29个 | 1个 | 378ms | 16.0%  
湖南 | 39个 | 1个 | 313ms | 11.6% | 西藏 | 1个 | 0 | 446ms | 24.0%  
  
简评：如果你考虑在Linode的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有817个，其中超时点9个，平均响应时间为314毫秒，丢包率为13%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的6个，超过300毫秒的25个；  
超时点较多的省份：北京、青海；  
丢包率较高的省份：上海、浙江、天津、安徽、海南、河北、广西、江西、四川、湖北、江苏、广东、宁夏、福建、湖南、内蒙古、吉林、辽宁、重庆、陕西、甘肃、河南、山西、贵州、云南、黑龙江、青海、新疆、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_idc_linode_uk-london_20180426_overseas.png)

海外线路到Linode英国-伦敦机房的测速数据 [20180426] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
荷兰 | 2个 | 0 | 6ms | 0 | 印度尼西亚 | 1个 | 0 | 196ms | 0  
法国 | 2个 | 0 | 7ms | 0 | 马来西亚 | 4个 | 0 | 206ms | 0.5%  
英国 | 3个 | 0 | 16ms | 0 | 香港 | 19个 | 0 | 226ms | 0  
德国 | 1个 | 0 | 32ms | 10.0% | 越南 | 1个 | 0 | 230ms | 0  
加拿大 | 3个 | 0 | 86ms | 0 | 日本 | 3个 | 0 | 244ms | 0.3%  
俄罗斯 | 1个 | 0 | 105ms | 0 | 菲律宾 | 1个 | 0 | 270ms | 1.0%  
美国 | 16个 | 0 | 137ms | 0 | 台湾 | 1个 | 0 | 272ms | -  
南非 | 1个 | 0 | 161ms | 0 | 韩国 | 12个 | 0 | 277ms | 0.3%  
均值 | 79个 | 0 | 179ms | 1.0% | 澳大利亚 | 2个 | 0 | 324ms | 0  
新加坡 | 5个 | 0 | 186ms | 0 | 柬埔寨 | 1个 | 0 | 419ms | 6.0%  
  
简评：如果你考虑在Linode的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有79个，其中超时点0个，平均响应时间为179毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的7个，超过300毫秒的2个；  
丢包率较高的国家/地区：德国；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180426 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180426 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180426-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180426")
    * [达拉斯](/linode/idc/dallas/20180426-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180426")
    * [法兰克福](/linode/idc/frankfurt/20180426-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180426")
    * [佛利蒙](/linode/idc/fremont/20180426-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180426")
    * [纽瓦克](/linode/idc/newark/20180426-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180426")
    * [新加坡](/linode/idc/singapore/20180426-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180426")
    * [东京](/linode/idc/tokyo/20180426-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180426")
  * 到Linode伦敦机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")
    * [20180527](/linode/idc/london/20180527-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180527")
    * [20180622](/linode/idc/london/20180622-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180622")
    * [20180804](/linode/idc/london/20180804-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180804")
    * [20180918](/linode/idc/london/20180918-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180426-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180426")
    * [Vultr](/vultr/idc/london/20180426-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180426")



本文最初发表于[多地到Linode伦敦[London]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-linode-idc-london.html)
