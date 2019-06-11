#  多地到Linode亚特兰大[Atlanta]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode亚特兰大\[Atlanta\]机房的Ping测试（20180514）](/images/thumbnails/to_linode_Atlanta.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-亚特兰大机房](https://vps123.top/linode-facilities.html#atlanta)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-亚特兰大机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180514-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Linode美国-亚特兰大机房的PING测试结果，连通概况如下：大陆30个省市的951个有效测试样本中，共有超时点14个；响应均值为283毫秒，最快的三地区为天津、上海、吉林，最慢的三地区为广西、四川、云南；浙江、广东、北京、山东、江苏等9处有响应超时情况；青海、云南、广西、湖南、甘肃等28处丢包率较高。海外17个国家地区的79个有效测试样本中，无超时点；响应均值为186毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为马来西亚、南非、印度尼西亚。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于亚特兰大\[Atlanta\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_usa-atlanta_20180514_mainland.png)

**大陆各省份到Linode美国-亚特兰大机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 4个 | 0 | 215ms | 2.5%  
上海 | 8个 | 0 | 226ms | 5.4%  
吉林 | 13个 | 0 | 236ms | 0.9%  
北京 | 7个 | 1个 | 247ms | 16.8%  
陕西 | 33个 | 0 | 256ms | 11.3%  
辽宁 | 41个 | 0 | 257ms | 14.2%  
河北 | 30个 | 0 | 258ms | 8.8%  
山东 | 53个 | 1个 | 259ms | 18.0%  
江苏 | 63个 | 1个 | 260ms | 17.0%  
安徽 | 41个 | 1个 | 260ms | 18.2%  
山西 | 34个 | 0 | 264ms | 16.0%  
河南 | 54个 | 0 | 268ms | 17.9%  
福建 | 33个 | 1个 | 270ms | 10.5%  
黑龙江 | 38个 | 0 | 272ms | 16.1%  
浙江 | 49个 | 4个 | 274ms | 13.3%  
内蒙古 | 35个 | 0 | 274ms | 14.0%  
宁夏 | 11个 | 0 | 276ms | 16.2%  
均值 | 951个 | 14个 | 283ms | 15.9%  
甘肃 | 22个 | 0 | 289ms | 19.8%  
江西 | 25个 | 0 | 291ms | 16.0%  
海南 | 10个 | 0 | 297ms | 16.9%  
青海 | 3个 | 0 | 301ms | 27.3%  
湖北 | 46个 | 0 | 303ms | 14.3%  
广东 | 74个 | 3个 | 304ms | 18.2%  
湖南 | 44个 | 0 | 307ms | 20.0%  
贵州 | 27个 | 1个 | 309ms | 16.8%  
新疆 | 30个 | 1个 | 311ms | 16.8%  
重庆 | 15个 | 0 | 313ms | 14.9%  
广西 | 37个 | 0 | 318ms | 21.0%  
四川 | 47个 | 0 | 329ms | 14.1%  
云南 | 24个 | 0 | 338ms | 25.0%  
  
**简评：** 如果你考虑在Linode的亚特兰大[Atlanta]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于亚特兰大[Atlanta]的机房的连通状况。到此机房的ping监测点共有951个，其中超时点14个，平均响应时间为283毫秒，丢包率为15%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的20个，超过300毫秒的10个；  
超时点较多的省份：北京；  
丢包率较高的省份：北京、陕西、辽宁、山东、江苏、安徽、山西、河南、福建、黑龙江、浙江、内蒙古、宁夏、甘肃、江西、海南、青海、湖北、广东、湖南、贵州、新疆、重庆、广西、四川、云南；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于亚特兰大\[Atlanta\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_usa-atlanta_20180514_overseas.png)

**海外线路到Linode美国-亚特兰大机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 3个 | 0 | 37ms | 0  
美国 | 19个 | 0 | 49ms | 0  
法国 | 2个 | 0 | 97ms | 0  
英国 | 2个 | 0 | 104ms | 0  
德国 | 2个 | 0 | 113ms | 0  
巴西 | 1个 | 0 | 121ms | 0  
均值 | 79个 | 0 | 186ms | 0.4%  
台湾 | 1个 | 0 | 190ms | -  
韩国 | 13个 | 0 | 192ms | 0  
俄罗斯 | 1个 | 0 | 196ms | 0  
日本 | 2个 | 0 | 200ms | 1.0%  
澳大利亚 | 2个 | 0 | 210ms | 0.5%  
新加坡 | 6个 | 0 | 221ms | 0  
菲律宾 | 1个 | 0 | 223ms | 1.0%  
香港 | 18个 | 0 | 232ms | 0  
马来西亚 | 4个 | 0 | 266ms | 1.0%  
南非 | 1个 | 0 | 294ms | 0  
印度尼西亚 | 1个 | 0 | 417ms | 3.0%  
  
**简评：** 如果你考虑在Linode的亚特兰大[Atlanta]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于亚特兰大[Atlanta]的机房的连通状况。到此机房的ping监测点共有79个，其中超时点0个，平均响应时间为186毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的1个，在100-200毫秒间的7个，在200-300毫秒间的6个，超过300毫秒的1个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180514 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180514 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [达拉斯](/linode/idc/dallas/20180514-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180514")
    * [法兰克福](/linode/idc/frankfurt/20180514-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180514")
    * [佛利蒙](/linode/idc/fremont/20180514-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180514")
    * [伦敦](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")
    * [纽瓦克](/linode/idc/newark/20180514-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180514")
    * [新加坡](/linode/idc/singapore/20180514-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180514")
    * [东京](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
  * 到Linode亚特兰大机房的 _其他近期报告_ ： 
    * [20180527](/linode/idc/atlanta/20180527-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180527")
    * [20180622](/linode/idc/atlanta/20180622-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180622")
    * [20180804](/linode/idc/atlanta/20180804-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180804")
    * [20180918](/linode/idc/atlanta/20180918-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180918")
  * 本期报告：在亚特兰大部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/atlanta/20180514-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180514")



本文最初发表于[多地到Linode亚特兰大[Atlanta]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-linode-idc-atlanta.html)
