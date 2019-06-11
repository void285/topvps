#  多地到Linode纽瓦克[Newark]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode纽瓦克\[Newark\]机房的Ping测试（20180426）](/images/thumbnails/to_linode_Newark.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-纽瓦克机房](https://vps123.top/linode-facilities.html#newark)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-纽瓦克机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180426-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Linode美国-纽瓦克机房的PING测试结果，连通概况如下：大陆31个省市的836个有效测试样本中，共有超时点6个；响应均值为296毫秒，最快的三地区为广东、湖南、河南，最慢的三地区为重庆、新疆、西藏；浙江、吉林、江苏、北京、新疆有响应超时情况；天津、重庆、江苏、辽宁、北京等14处丢包率较高。海外19个国家地区的77个有效测试样本中，无超时点；响应均值为192毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为马来西亚、菲律宾、柬埔寨；柬埔寨丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于纽瓦克市\[\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_idc_linode_usa-newark_20180426_mainland.png)

**大陆各省份到Linode美国-纽瓦克机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
广东 | 58个 | 0 | 274ms | 4.2%  
湖南 | 40个 | 0 | 276ms | 3.3%  
河南 | 50个 | 0 | 277ms | 2.6%  
山东 | 46个 | 0 | 277ms | 3.8%  
广西 | 36个 | 0 | 280ms | 5.9%  
山西 | 34个 | 0 | 281ms | 4.4%  
海南 | 12个 | 0 | 286ms | 4.8%  
河北 | 33个 | 0 | 291ms | 5.4%  
湖北 | 38个 | 0 | 292ms | 5.7%  
青海 | 4个 | 0 | 294ms | 0  
福建 | 25个 | 0 | 294ms | 6.5%  
吉林 | 16个 | 1个 | 294ms | 6.3%  
贵州 | 22个 | 0 | 296ms | 4.5%  
均值 | 836个 | 6个 | 296ms | 5.1%  
江苏 | 49个 | 1个 | 297ms | 7.4%  
浙江 | 38个 | 2个 | 298ms | 5.3%  
江西 | 21个 | 0 | 299ms | 4.2%  
黑龙江 | 32个 | 0 | 299ms | 4.8%  
陕西 | 27个 | 0 | 301ms | 3.0%  
安徽 | 41个 | 0 | 302ms | 4.7%  
上海 | 7个 | 0 | 302ms | 3.0%  
辽宁 | 34个 | 0 | 303ms | 7.2%  
四川 | 43个 | 0 | 309ms | 5.6%  
内蒙古 | 32个 | 0 | 310ms | 6.5%  
天津 | 5个 | 0 | 314ms | 18.3%  
云南 | 22个 | 0 | 315ms | 5.1%  
甘肃 | 21个 | 0 | 327ms | 4.9%  
北京 | 4个 | 1个 | 328ms | 7.0%  
宁夏 | 10个 | 0 | 330ms | 4.3%  
重庆 | 10个 | 0 | 347ms | 10.7%  
新疆 | 25个 | 1个 | 349ms | 4.3%  
西藏 | 1个 | 0 | 440ms | 3.0%  
  
**简评：** 如果你考虑在Linode的纽瓦克市[]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽瓦克市[]的机房的连通状况。到此机房的ping监测点共有836个，其中超时点6个，平均响应时间为296毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的17个，超过300毫秒的14个；  
超时点较多的省份：北京；  
丢包率较高的省份：天津、重庆；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于纽瓦克市\[\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_idc_linode_usa-newark_20180426_overseas.png)

**海外线路到Linode美国-纽瓦克机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 3个 | 0 | 16ms | 0  
美国 | 15个 | 0 | 63ms | 0  
法国 | 2个 | 0 | 77ms | 0  
荷兰 | 2个 | 0 | 82ms | 0  
英国 | 3个 | 0 | 88ms | 0  
德国 | 1个 | 0 | 99ms | 0  
俄罗斯 | 1个 | 0 | 171ms | 0  
日本 | 2个 | 0 | 189ms | 0  
均值 | 77个 | 0 | 192ms | 0.7%  
台湾 | 1个 | 0 | 202ms | -  
韩国 | 12个 | 0 | 215ms | 0  
香港 | 19个 | 0 | 229ms | 0  
南非 | 1个 | 0 | 232ms | 0  
澳大利亚 | 2个 | 0 | 236ms | 0.5%  
新加坡 | 5个 | 0 | 243ms | 0  
印度尼西亚 | 1个 | 0 | 247ms | 0  
越南 | 1个 | 0 | 260ms | 1.0%  
马来西亚 | 4个 | 0 | 263ms | 1.8%  
菲律宾 | 1个 | 0 | 302ms | 4.0%  
柬埔寨 | 1个 | 0 | 439ms | 6.0%  
  
**简评：** 如果你考虑在Linode的纽瓦克市[]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽瓦克市[]的机房的连通状况。到此机房的ping监测点共有77个，其中超时点0个，平均响应时间为192毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的5个，在100-200毫秒间的2个，在200-300毫秒间的9个，超过300毫秒的2个；

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
    * [伦敦](/linode/idc/london/20180426-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180426")
    * [新加坡](/linode/idc/singapore/20180426-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180426")
    * [东京](/linode/idc/tokyo/20180426-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180426")
  * 到Linode纽瓦克机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/newark/20180514-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180514")
    * [20180527](/linode/idc/newark/20180527-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180527")
    * [20180622](/linode/idc/newark/20180622-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180622")
    * [20180804](/linode/idc/newark/20180804-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180804")
    * [20180918](/linode/idc/newark/20180918-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180918")



本文最初发表于[多地到Linode纽瓦克[Newark]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-linode-idc-newark.html)
