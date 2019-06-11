#  多地到Linode东京[Tokyo]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode东京\[Tokyo\]机房的Ping测试（20180514）](/images/thumbnails/to_linode_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[日本-东京机房](https://vps123.top/linode-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180514-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Linode日本-东京机房的PING测试结果，连通概况如下：大陆30个省市的968个有效测试样本中，共有超时点15个；响应均值为121毫秒，最快的三地区为天津、上海、福建，最慢的三地区为重庆、新疆、河北；广东、浙江、北京、福建、江苏等8处有响应超时情况；安徽、上海、北京、江西、新疆等15处丢包率较高。海外17个国家地区的78个有效测试样本中，无超时点；响应均值为150毫秒，最快的三地区为日本、台湾、韩国，最慢的三地区为英国、巴西、南非。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_japan-tokyo_20180514_mainland.png)

大陆各省份到Linode日本-东京机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
天津 | 4个 | 0 | 73ms | 1.7% | 广西 | 38个 | 0 | 116ms | 6.1%  
上海 | 8个 | 0 | 89ms | 12.0% | 广东 | 78个 | 5个 | 117ms | 4.0%  
福建 | 36个 | 1个 | 94ms | 3.3% | 陕西 | 32个 | 1个 | 117ms | 5.0%  
海南 | 10个 | 0 | 97ms | 4.1% | 浙江 | 52个 | 3个 | 121ms | 6.4%  
北京 | 8个 | 2个 | 102ms | 11.7% | 云南 | 24个 | 0 | 121ms | 3.1%  
湖南 | 44个 | 0 | 103ms | 5.4% | 均值 | 968个 | 15个 | 121ms | 5.3%  
吉林 | 13个 | 0 | 104ms | 2.2% | 宁夏 | 12个 | 0 | 122ms | 5.4%  
江苏 | 63个 | 1个 | 106ms | 6.3% | 内蒙古 | 32个 | 0 | 122ms | 3.3%  
山西 | 38个 | 0 | 107ms | 3.0% | 河南 | 56个 | 0 | 127ms | 4.1%  
辽宁 | 41个 | 0 | 110ms | 5.6% | 青海 | 4个 | 0 | 128ms | 4.0%  
山东 | 52个 | 1个 | 111ms | 4.2% | 四川 | 47个 | 1个 | 129ms | 5.5%  
黑龙江 | 37个 | 0 | 113ms | 2.6% | 甘肃 | 22个 | 0 | 141ms | 6.2%  
湖北 | 46个 | 0 | 114ms | 5.4% | 重庆 | 16个 | 0 | 145ms | 5.8%  
江西 | 23个 | 0 | 114ms | 9.4% | 新疆 | 29个 | 0 | 172ms | 6.9%  
贵州 | 28个 | 0 | 115ms | 4.0% | 河北 | 32个 | 0 | 218ms | 5.0%  
安徽 | 43个 | 0 | 115ms | 12.2% |  |  |  |  |   
  
简评：如果你考虑在Linode的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有968个，其中超时点15个，平均响应时间为121毫秒，丢包率为5%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50-100毫秒间的4个，在100-200毫秒间的25个，在200-300毫秒间的1个；  
超时点较多的省份：北京；  
丢包率较高的省份：上海、北京、安徽；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_japan-tokyo_20180514_overseas.png)

海外线路到Linode日本-东京机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
日本 | 2个 | 0 | 9ms | 0.5% | 均值 | 78个 | 0 | 150ms | 0.1%  
台湾 | 1个 | 0 | 40ms | - | 澳大利亚 | 2个 | 0 | 157ms | 0  
韩国 | 12个 | 0 | 61ms | 0 | 加拿大 | 3个 | 0 | 181ms | 0  
香港 | 18个 | 0 | 70ms | 0 | 俄罗斯 | 1个 | 0 | 183ms | 0  
菲律宾 | 1个 | 0 | 72ms | 1.0% | 德国 | 2个 | 0 | 247ms | 0.5%  
新加坡 | 6个 | 0 | 91ms | 0 | 法国 | 2个 | 0 | 248ms | 0  
马来西亚 | 4个 | 0 | 93ms | 0 | 英国 | 2个 | 0 | 255ms | 0  
印度尼西亚 | 1个 | 0 | 112ms | 0 | 巴西 | 1个 | 0 | 281ms | 0  
美国 | 19个 | 0 | 118ms | 0 | 南非 | 1个 | 0 | 345ms | 0  
  
简评：如果你考虑在Linode的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点0个，平均响应时间为150毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的5个，在100-200毫秒间的5个，在200-300毫秒间的4个，超过300毫秒的1个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180514 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180514 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180514-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180514")
    * [达拉斯](/linode/idc/dallas/20180514-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180514")
    * [法兰克福](/linode/idc/frankfurt/20180514-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180514")
    * [佛利蒙](/linode/idc/fremont/20180514-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180514")
    * [伦敦](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")
    * [纽瓦克](/linode/idc/newark/20180514-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180514")
    * [新加坡](/linode/idc/singapore/20180514-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180514")
  * 到Linode东京机房的 _其他近期报告_ ： 
    * [20180527](/linode/idc/tokyo/20180527-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180527")
    * [20180622](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")
    * [20180804](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")
    * [20180918](/linode/idc/tokyo/20180918-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180918")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")



本文最初发表于[多地到Linode东京[Tokyo]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-linode-idc-tokyo.html)
