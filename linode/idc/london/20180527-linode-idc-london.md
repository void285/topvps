#  多地到Linode伦敦[London]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode伦敦\[London\]机房的Ping测试（20180527）](/images/thumbnails/to_linode_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[英国-伦敦机房](https://vps123.top/linode-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180527-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的961个有效测试样本中，共有超时点9个；响应均值为293毫秒，最快的三地区为上海、浙江、北京，最慢的三地区为甘肃、黑龙江、新疆；江苏、浙江、北京、广东、重庆等8处有响应超时情况；贵州、湖南、四川、黑龙江、新疆等12处丢包率较高。海外21个国家地区的86个有效测试样本中，无超时点；响应均值为174毫秒，最快的三地区为法国、荷兰、意大利，最慢的三地区为澳大利亚、柬埔寨、菲律宾；柬埔寨丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/linode_20180527/plot_idc_linode_uk-london_20180527_mainland.png)

**大陆各省份到Linode英国-伦敦机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 8个 | 0 | 241ms | 1.9%  
浙江 | 49个 | 1个 | 266ms | 2.7%  
北京 | 8个 | 1个 | 269ms | 2.0%  
广东 | 78个 | 1个 | 271ms | 4.0%  
安徽 | 37个 | 0 | 273ms | 5.7%  
天津 | 5个 | 0 | 275ms | 1.6%  
青海 | 3个 | 0 | 276ms | 4.3%  
湖北 | 44个 | 0 | 278ms | 3.6%  
江苏 | 62个 | 2个 | 283ms | 5.7%  
河北 | 33个 | 0 | 285ms | 5.1%  
重庆 | 15个 | 1个 | 288ms | 3.8%  
海南 | 14个 | 0 | 288ms | 4.8%  
吉林 | 19个 | 0 | 289ms | 3.3%  
辽宁 | 40个 | 0 | 289ms | 4.2%  
福建 | 34个 | 0 | 291ms | 5.6%  
河南 | 54个 | 1个 | 292ms | 4.7%  
四川 | 47个 | 0 | 292ms | 6.4%  
均值 | 961个 | 9个 | 293ms | 5.0%  
广西 | 39个 | 0 | 295ms | 5.5%  
内蒙古 | 34个 | 0 | 296ms | 5.4%  
江西 | 23个 | 0 | 297ms | 4.9%  
陕西 | 32个 | 1个 | 300ms | 5.5%  
云南 | 21个 | 0 | 301ms | 4.4%  
宁夏 | 12个 | 0 | 304ms | 3.3%  
湖南 | 47个 | 0 | 304ms | 10.2%  
山西 | 36个 | 0 | 305ms | 3.6%  
山东 | 50个 | 1个 | 306ms | 2.0%  
贵州 | 27个 | 0 | 309ms | 11.3%  
甘肃 | 23个 | 0 | 309ms | 4.3%  
黑龙江 | 40个 | 0 | 323ms | 5.9%  
新疆 | 27个 | 0 | 352ms | 5.8%  
  
**简评：** 如果你考虑在Linode的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有961个，其中超时点9个，平均响应时间为293毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的21个，超过300毫秒的9个；  
超时点较多的省份：北京；  
丢包率较高的省份：湖南、贵州；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/linode_20180527/plot_idc_linode_uk-london_20180527_overseas.png)

**海外线路到Linode英国-伦敦机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
法国 | 1个 | 0 | 8ms | 0  
荷兰 | 1个 | 0 | 8ms | 0  
意大利 | 1个 | 0 | 8ms | -  
英国 | 2个 | 0 | 17ms | 0  
德国 | 3个 | 0 | 21ms | 0  
加拿大 | 3个 | 0 | 90ms | 0  
俄罗斯 | 1个 | 0 | 104ms | 0  
美国 | 21个 | 0 | 131ms | 1.0%  
均值 | 86个 | 0 | 174ms | 0.7%  
南非 | 2个 | 0 | 185ms | 0  
新加坡 | 5个 | 0 | 190ms | 0  
印度尼西亚 | 1个 | 0 | 193ms | 0  
巴西 | 1个 | 0 | 195ms | 0  
马来西亚 | 5个 | 0 | 231ms | 0  
日本 | 1个 | 0 | 237ms | 0  
香港 | 20个 | 0 | 239ms | 1.7%  
越南 | 2个 | 0 | 239ms | 0  
台湾 | 1个 | 0 | 259ms | -  
韩国 | 12个 | 0 | 278ms | 0  
澳大利亚 | 1个 | 0 | 336ms | 0  
柬埔寨 | 1个 | 0 | 344ms | 10.0%  
菲律宾 | 1个 | 0 | 353ms | 0  
  
**简评：** 如果你考虑在Linode的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有86个，其中超时点0个，平均响应时间为174毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在50-100毫秒间的1个，在100-200毫秒间的6个，在200-300毫秒间的6个，超过300毫秒的3个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180527 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180527 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180527-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180527")
    * [达拉斯](/linode/idc/dallas/20180527-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180527")
    * [法兰克福](/linode/idc/frankfurt/20180527-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180527")
    * [佛利蒙](/linode/idc/fremont/20180527-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180527")
    * [纽瓦克](/linode/idc/newark/20180527-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180527")
    * [新加坡](/linode/idc/singapore/20180527-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180527")
    * [东京](/linode/idc/tokyo/20180527-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180527")
  * 到Linode伦敦机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")
    * [20180622](/linode/idc/london/20180622-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180622")
    * [20180804](/linode/idc/london/20180804-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180804")
    * [20180918](/linode/idc/london/20180918-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180527-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [Vultr](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")



本文最初发表于[多地到Linode伦敦[London]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-linode-idc-london.html)
