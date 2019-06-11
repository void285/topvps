#  多地到Linode达拉斯[Dallas]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode达拉斯\[Dallas\]机房的Ping测试（20180426）](/images/thumbnails/to_linode_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-达拉斯机房](https://vps123.top/linode-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180426-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Linode美国-达拉斯机房的PING测试结果，连通概况如下：大陆31个省市的842个有效测试样本中，共有超时点4个；响应均值为292毫秒，最快的三地区为吉林、重庆、宁夏，最慢的三地区为青海、西藏、新疆；浙江、江苏、甘肃有响应超时情况；湖北、天津、江苏、江西、安徽等28处丢包率较高。海外19个国家地区的79个有效测试样本中，共有超时点1个；响应均值为189毫秒，最快的三地区为美国、加拿大、法国，最慢的三地区为印度尼西亚、菲律宾、柬埔寨；日本有响应超时情况；柬埔寨丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_idc_linode_usa-dallas_20180426_mainland.png)

**大陆各省份到Linode美国-达拉斯机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
吉林 | 16个 | 0 | 256ms | 12.4%  
重庆 | 10个 | 0 | 266ms | 8.7%  
宁夏 | 10个 | 0 | 268ms | 2.5%  
广东 | 55个 | 0 | 269ms | 9.1%  
湖北 | 38个 | 0 | 271ms | 22.6%  
广西 | 35个 | 0 | 271ms | 6.3%  
山西 | 33个 | 0 | 271ms | 12.3%  
浙江 | 40个 | 2个 | 272ms | 17.7%  
上海 | 8个 | 0 | 272ms | 9.0%  
天津 | 4个 | 0 | 274ms | 21.7%  
四川 | 44个 | 0 | 281ms | 8.8%  
海南 | 12个 | 0 | 281ms | 4.8%  
江苏 | 49个 | 1个 | 285ms | 20.8%  
北京 | 3个 | 0 | 288ms | 17.3%  
内蒙古 | 31个 | 0 | 289ms | 10.9%  
黑龙江 | 34个 | 0 | 290ms | 12.9%  
贵州 | 23个 | 0 | 291ms | 6.7%  
均值 | 842个 | 4个 | 292ms | 13.1%  
山东 | 48个 | 0 | 299ms | 10.0%  
江西 | 21个 | 0 | 300ms | 20.4%  
陕西 | 27个 | 0 | 300ms | 8.1%  
河南 | 51个 | 0 | 302ms | 17.1%  
河北 | 31个 | 0 | 302ms | 13.5%  
辽宁 | 36个 | 0 | 303ms | 12.6%  
安徽 | 38个 | 0 | 305ms | 18.5%  
湖南 | 39个 | 0 | 306ms | 10.9%  
云南 | 25个 | 0 | 313ms | 10.6%  
福建 | 27个 | 0 | 315ms | 14.2%  
甘肃 | 21个 | 1个 | 337ms | 14.8%  
青海 | 4个 | 0 | 339ms | 7.0%  
西藏 | 1个 | 0 | 341ms | 0  
新疆 | 28个 | 0 | 359ms | 16.6%  
  
**简评：** 如果你考虑在Linode的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有842个，其中超时点4个，平均响应时间为292毫秒，丢包率为13%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的20个，超过300毫秒的11个；  
丢包率较高的省份：吉林、湖北、山西、浙江、天津、江苏、北京、内蒙古、黑龙江、山东、江西、河南、河北、辽宁、安徽、湖南、云南、福建、甘肃、新疆；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_idc_linode_usa-dallas_20180426_overseas.png)

**海外线路到Linode美国-达拉斯机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
美国 | 16个 | 0 | 34ms | 0  
加拿大 | 3个 | 0 | 36ms | 0  
法国 | 2个 | 0 | 113ms | 0  
荷兰 | 2个 | 0 | 119ms | 0  
英国 | 3个 | 0 | 122ms | 0  
德国 | 1个 | 0 | 125ms | 0  
日本 | 3个 | 1个 | 153ms | 0.5%  
韩国 | 12个 | 0 | 186ms | 0  
均值 | 79个 | 1个 | 189ms | 0.6%  
台湾 | 1个 | 0 | 192ms | -  
香港 | 19个 | 0 | 201ms | 0  
新加坡 | 5个 | 0 | 205ms | 0  
俄罗斯 | 1个 | 0 | 217ms | 0  
澳大利亚 | 2个 | 0 | 223ms | 0  
马来西亚 | 4个 | 0 | 225ms | 0.3%  
越南 | 1个 | 0 | 250ms | 0  
南非 | 1个 | 0 | 265ms | 0  
印度尼西亚 | 1个 | 0 | 265ms | 2.0%  
菲律宾 | 1个 | 0 | 266ms | 2.0%  
柬埔寨 | 1个 | 0 | 393ms | 6.0%  
  
**简评：** 如果你考虑在Linode的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有79个，其中超时点1个，平均响应时间为189毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在100-200毫秒间的7个，在200-300毫秒间的9个，超过300毫秒的1个；  
超时点较多的国家/地区：日本；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180426 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180426 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180426-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180426")
    * [法兰克福](/linode/idc/frankfurt/20180426-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180426")
    * [佛利蒙](/linode/idc/fremont/20180426-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180426")
    * [伦敦](/linode/idc/london/20180426-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180426")
    * [纽瓦克](/linode/idc/newark/20180426-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180426")
    * [新加坡](/linode/idc/singapore/20180426-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180426")
    * [东京](/linode/idc/tokyo/20180426-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180426")
  * 到Linode达拉斯机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/dallas/20180514-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180514")
    * [20180527](/linode/idc/dallas/20180527-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180527")
    * [20180622](/linode/idc/dallas/20180622-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180622")
    * [20180804](/linode/idc/dallas/20180804-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180804")
    * [20180918](/linode/idc/dallas/20180918-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180918")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/dallas/20180426-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180426")



本文最初发表于[多地到Linode达拉斯[Dallas]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-linode-idc-dallas.html)
