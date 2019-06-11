#  多地到Linode达拉斯[Dallas]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode达拉斯\[Dallas\]机房的Ping测试（20180918）](/images/thumbnails/to_linode_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-达拉斯机房](https://vps123.top/linode-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180918-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Linode美国-达拉斯机房的PING测试结果，连通概况如下：大陆31个省市的1344个有效测试样本中，共有超时点16个；响应均值为247毫秒，最快的三地区为上海、安徽、浙江，最慢的三地区为新疆、青海、西藏；江苏、浙江、广东、湖南、湖北等9处有响应超时情况；吉林、上海、北京、青海、河北等17处丢包率较高。海外17个国家地区的80个有效测试样本中，无超时点；响应均值为184毫秒，最快的三地区为加拿大、美国、台湾，最慢的三地区为马来西亚、赞比亚、菲律宾；菲律宾、印度尼西亚丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/linode_20180918/plot_idc_linode_usa-dallas_20180918_mainland.png)

**大陆各省份到Linode美国-达拉斯机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 6个 | 0 | 226ms | 13.6%  
安徽 | 67个 | 0 | 228ms | 2.8%  
浙江 | 66个 | 2个 | 230ms | 5.0%  
江苏 | 91个 | 6个 | 232ms | 6.1%  
广东 | 121个 | 2个 | 233ms | 5.1%  
广西 | 55个 | 0 | 234ms | 4.7%  
湖南 | 65个 | 1个 | 234ms | 3.8%  
湖北 | 51个 | 1个 | 236ms | 4.0%  
江西 | 41个 | 0 | 237ms | 3.8%  
天津 | 7个 | 0 | 239ms | 0.1%  
北京 | 7个 | 0 | 239ms | 13.0%  
海南 | 14个 | 0 | 239ms | 3.6%  
宁夏 | 1个 | 0 | 241ms | 1.0%  
山东 | 92个 | 0 | 242ms | 8.4%  
福建 | 41个 | 1个 | 243ms | 4.0%  
重庆 | 8个 | 0 | 243ms | 5.3%  
河北 | 49个 | 0 | 246ms | 11.0%  
辽宁 | 58个 | 1个 | 246ms | 9.7%  
贵州 | 39个 | 1个 | 247ms | 6.4%  
山西 | 53个 | 1个 | 247ms | 8.4%  
均值 | 1344个 | 16个 | 247ms | 6.4%  
吉林 | 19个 | 0 | 254ms | 17.2%  
四川 | 68个 | 0 | 255ms | 3.7%  
云南 | 27个 | 0 | 258ms | 2.8%  
内蒙古 | 53个 | 0 | 260ms | 10.8%  
黑龙江 | 49个 | 0 | 262ms | 11.0%  
陕西 | 44个 | 0 | 264ms | 3.6%  
河南 | 82个 | 0 | 271ms | 8.9%  
甘肃 | 32个 | 0 | 276ms | 5.4%  
新疆 | 30个 | 0 | 301ms | 4.3%  
青海 | 6个 | 0 | 342ms | 11.8%  
西藏 | 2个 | 0 | 391ms | 10.5%  
  
**简评：** 如果你考虑在Linode的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有1344个，其中超时点16个，平均响应时间为247毫秒，丢包率为6%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的28个，超过300毫秒的3个；  
丢包率较高的省份：上海、北京、河北、吉林、内蒙古、黑龙江、青海、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/linode_20180918/plot_idc_linode_usa-dallas_20180918_overseas.png)

**海外线路到Linode美国-达拉斯机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 3个 | 0 | 36ms | 0  
美国 | 15个 | 0 | 58ms | 2.0%  
台湾 | 2个 | 0 | 105ms | 0  
意大利 | 1个 | 0 | 106ms | -  
德国 | 3个 | 0 | 138ms | 0  
韩国 | 12个 | 0 | 150ms | 0  
俄罗斯 | 2个 | 0 | 153ms | 0  
新加坡 | 5个 | 0 | 176ms | 0  
日本 | 2个 | 0 | 177ms | 0  
香港 | 20个 | 0 | 177ms | 0  
均值 | 80个 | 0 | 184ms | 2.8%  
澳大利亚 | 1个 | 0 | 200ms | 0  
荷兰 | 1个 | 0 | 204ms | 0  
越南 | 2个 | 0 | 239ms | 0  
印度尼西亚 | 1个 | 0 | 260ms | 10.0%  
马来西亚 | 6个 | 0 | 263ms | 0  
赞比亚 | 2个 | 0 | 306ms | 1.0%  
菲律宾 | 2个 | 0 | 390ms | 31.7%  
  
**简评：** 如果你考虑在Linode的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有80个，其中超时点0个，平均响应时间为184毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的9个，在200-300毫秒间的4个，超过300毫秒的2个；  
丢包率较高的国家/地区：印度尼西亚、菲律宾；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180918 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180918 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180918-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180918")
    * [法兰克福](/linode/idc/frankfurt/20180918-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180918")
    * [佛利蒙](/linode/idc/fremont/20180918-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180918")
    * [伦敦](/linode/idc/london/20180918-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180918")
    * [纽瓦克](/linode/idc/newark/20180918-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180918")
    * [新加坡](/linode/idc/singapore/20180918-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180918")
    * [东京](/linode/idc/tokyo/20180918-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180918")
  * 到Linode达拉斯机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/dallas/20180514-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180514")
    * [20180527](/linode/idc/dallas/20180527-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180527")
    * [20180622](/linode/idc/dallas/20180622-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180622")
    * [20180804](/linode/idc/dallas/20180804-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180804")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")



本文最初发表于[多地到Linode达拉斯[Dallas]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-linode-idc-dallas.html)
