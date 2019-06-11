#  多地到Linode伦敦[London]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode伦敦\[London\]机房的Ping测试（20180804）](/images/thumbnails/to_linode_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[英国-伦敦机房](https://vps123.top/linode-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180804-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5407个有效测试样本中，共有超时点18个；响应均值为281毫秒，最快的三地区为上海、江苏、北京，最慢的三地区为贵州、吉林、西藏；广西、上海、浙江、重庆有响应超时情况；云南、湖南、重庆、浙江、福建等11处丢包率较高。海外19个国家地区的234个有效测试样本中，共有超时点3个；响应均值为184毫秒，最快的三地区为巴西、意大利、德国，最慢的三地区为法国、澳大利亚、菲律宾；香港有响应超时情况；美国、菲律宾丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_idc_linode_uk-london_20180804_mainland.png)

**大陆各省份到Linode英国-伦敦机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 27个 | 4个 | 233ms | 0  
江苏 | 339个 | 0 | 256ms | 0.4%  
北京 | 32个 | 0 | 258ms | 1.0%  
河南 | 371个 | 0 | 259ms | 1.7%  
湖北 | 205个 | 0 | 262ms | 7.0%  
河北 | 248个 | 0 | 263ms | 2.9%  
青海 | 16个 | 0 | 264ms | 0  
江西 | 135个 | 0 | 265ms | 1.6%  
安徽 | 240个 | 0 | 267ms | 2.2%  
陕西 | 175个 | 0 | 273ms | 0.3%  
山东 | 338个 | 0 | 274ms | 1.6%  
浙江 | 244个 | 4个 | 274ms | 8.7%  
宁夏 | 32个 | 0 | 274ms | 5.1%  
辽宁 | 227个 | 0 | 278ms | 1.0%  
广西 | 235个 | 7个 | 280ms | 6.5%  
均值 | 5407个 | 18个 | 281ms | 4.1%  
福建 | 169个 | 0 | 283ms | 8.4%  
海南 | 52个 | 0 | 283ms | 6.9%  
天津 | 20个 | 0 | 284ms | 1.3%  
山西 | 190个 | 0 | 284ms | 2.4%  
广东 | 438个 | 0 | 286ms | 2.5%  
甘肃 | 112个 | 0 | 288ms | 1.9%  
重庆 | 31个 | 3个 | 289ms | 10.7%  
四川 | 289个 | 0 | 290ms | 8.2%  
湖南 | 265个 | 0 | 298ms | 11.2%  
云南 | 131个 | 0 | 302ms | 15.9%  
内蒙古 | 228个 | 0 | 303ms | 1.7%  
新疆 | 155个 | 0 | 307ms | 2.0%  
黑龙江 | 200个 | 0 | 307ms | 1.9%  
贵州 | 159个 | 0 | 309ms | 7.6%  
吉林 | 100个 | 0 | 326ms | 1.3%  
西藏 | 4个 | 0 | 409ms | 3.0%  
  
**简评：** 如果你考虑在Linode的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有5407个，其中超时点18个，平均响应时间为281毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的24个，超过300毫秒的7个；  
超时点较多的省份：上海；  
丢包率较高的省份：重庆、湖南、云南；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_idc_linode_uk-london_20180804_overseas.png)

**海外线路到Linode英国-伦敦机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
巴西 | 3个 | 0 | 1ms | 0  
意大利 | 3个 | 0 | 8ms | -  
德国 | 9个 | 0 | 28ms | 0  
英国 | 6个 | 0 | 35ms | 0  
俄罗斯 | 3个 | 0 | 55ms | -  
加拿大 | 15个 | 0 | 90ms | 0  
荷兰 | 3个 | 0 | 145ms | 0  
美国 | 48个 | 0 | 156ms | 11.3%  
新加坡 | 15个 | 0 | 168ms | 0  
南非 | 6个 | 0 | 181ms | 1.5%  
均值 | 234个 | 3个 | 184ms | 1.4%  
香港 | 63个 | 3个 | 192ms | 0  
印度尼西亚 | 6个 | 0 | 203ms | 0  
韩国 | 21个 | 0 | 251ms | 0  
台湾 | 3个 | 0 | 255ms | 0  
日本 | 6个 | 0 | 259ms | 1.0%  
马来西亚 | 12个 | 0 | 270ms | 0.5%  
法国 | 3个 | 0 | 294ms | 0  
澳大利亚 | 6个 | 0 | 318ms | 0  
菲律宾 | 3个 | 0 | 586ms | 10.0%  
  
**简评：** 如果你考虑在Linode的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有234个，其中超时点3个，平均响应时间为184毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的2个，在100-200毫秒间的5个，在200-300毫秒间的6个，超过300毫秒的2个；  
丢包率较高的国家/地区：美国、菲律宾；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180804 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180804 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180804-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180804")
    * [达拉斯](/linode/idc/dallas/20180804-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180804")
    * [法兰克福](/linode/idc/frankfurt/20180804-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180804")
    * [佛利蒙](/linode/idc/fremont/20180804-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180804")
    * [纽瓦克](/linode/idc/newark/20180804-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180804")
    * [新加坡](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")
    * [东京](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")
  * 到Linode伦敦机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")
    * [20180527](/linode/idc/london/20180527-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180527")
    * [20180622](/linode/idc/london/20180622-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180622")
    * [20180918](/linode/idc/london/20180918-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180804-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [Vultr](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")



本文最初发表于[多地到Linode伦敦[London]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-linode-idc-london.html)
