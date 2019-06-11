#  多地到Linode法兰克福[Frankfurt]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode法兰克福\[Frankfurt\]机房的Ping测试（20180514）](/images/thumbnails/to_linode_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[德国-法兰克福机房](https://vps123.top/linode-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180514-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Linode德国-法兰克福机房的PING测试结果，连通概况如下：大陆30个省市的949个有效测试样本中，共有超时点16个；响应均值为290毫秒，最快的三地区为青海、辽宁、广东，最慢的三地区为重庆、上海、新疆；江苏、福建、浙江、山东、广东等8处有响应超时情况；青海、甘肃、浙江、宁夏、山西等19处丢包率较高。海外17个国家地区的79个有效测试样本中，无超时点；响应均值为187毫秒，最快的三地区为法国、德国、英国，最慢的三地区为韩国、澳大利亚、台湾。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_germany-frankfurt_20180514_mainland.png)

大陆各省份到Linode德国-法兰克福机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
青海 | 4个 | 0 | 240ms | 12.5% | 福建 | 36个 | 3个 | 291ms | 3.0%  
辽宁 | 39个 | 0 | 260ms | 6.5% | 海南 | 9个 | 0 | 292ms | 2.8%  
广东 | 75个 | 1个 | 265ms | 2.8% | 山西 | 33个 | 0 | 294ms | 9.1%  
安徽 | 41个 | 1个 | 269ms | 7.7% | 山东 | 53个 | 2个 | 297ms | 7.5%  
江苏 | 61个 | 4个 | 271ms | 3.6% | 河南 | 56个 | 0 | 298ms | 6.5%  
河北 | 31个 | 0 | 272ms | 4.6% | 湖北 | 44个 | 0 | 302ms | 5.9%  
云南 | 22个 | 0 | 275ms | 1.6% | 陕西 | 32个 | 0 | 302ms | 7.1%  
内蒙古 | 35个 | 0 | 277ms | 7.9% | 贵州 | 28个 | 0 | 303ms | 6.2%  
宁夏 | 12个 | 0 | 279ms | 9.9% | 浙江 | 53个 | 3个 | 315ms | 10.9%  
天津 | 5个 | 0 | 280ms | 1.2% | 江西 | 25个 | 0 | 316ms | 8.5%  
北京 | 7个 | 1个 | 283ms | 4.8% | 黑龙江 | 38个 | 0 | 316ms | 7.6%  
广西 | 38个 | 0 | 285ms | 4.1% | 吉林 | 14个 | 0 | 317ms | 0.4%  
甘肃 | 22个 | 0 | 285ms | 11.3% | 重庆 | 14个 | 0 | 318ms | 7.0%  
四川 | 47个 | 0 | 289ms | 1.6% | 上海 | 8个 | 0 | 321ms | 8.9%  
湖南 | 40个 | 1个 | 290ms | 7.8% | 新疆 | 27个 | 0 | 325ms | 8.3%  
均值 | 949个 | 16个 | 290ms | 6.1% |  |  |  |  |   
  
简评：如果你考虑在Linode的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有949个，其中超时点16个，平均响应时间为290毫秒，丢包率为6%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的20个，超过300毫秒的10个；  
超时点较多的省份：北京；  
丢包率较高的省份：青海、甘肃、浙江；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_germany-frankfurt_20180514_overseas.png)

海外线路到Linode德国-法兰克福机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
法国 | 2个 | 0 | 9ms | 0 | 香港 | 18个 | 0 | 219ms | 0  
德国 | 2个 | 0 | 15ms | 0 | 马来西亚 | 4个 | 0 | 225ms | 1.0%  
英国 | 2个 | 0 | 34ms | 0 | 南非 | 1个 | 0 | 225ms | 0  
俄罗斯 | 1个 | 0 | 95ms | 0 | 印度尼西亚 | 1个 | 0 | 252ms | 2.0%  
加拿大 | 3个 | 0 | 100ms | 0 | 日本 | 2个 | 0 | 255ms | 0  
美国 | 19个 | 0 | 151ms | 0 | 菲律宾 | 1个 | 0 | 271ms | 0  
均值 | 79个 | 0 | 187ms | 0.2% | 韩国 | 13个 | 0 | 287ms | 0  
新加坡 | 6个 | 0 | 198ms | 0 | 澳大利亚 | 2个 | 0 | 310ms | 0  
巴西 | 1个 | 0 | 219ms | 0 | 台湾 | 1个 | 0 | 314ms | -  
  
简评：如果你考虑在Linode的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有79个，其中超时点0个，平均响应时间为187毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的2个，在100-200毫秒间的2个，在200-300毫秒间的8个，超过300毫秒的2个；

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
    * [佛利蒙](/linode/idc/fremont/20180514-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180514")
    * [伦敦](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")
    * [纽瓦克](/linode/idc/newark/20180514-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180514")
    * [新加坡](/linode/idc/singapore/20180514-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180514")
    * [东京](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
  * 到Linode法兰克福机房的 _其他近期报告_ ： 
    * [20180527](/linode/idc/frankfurt/20180527-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180527")
    * [20180622](/linode/idc/frankfurt/20180622-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180622")
    * [20180804](/linode/idc/frankfurt/20180804-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180804")
    * [20180918](/linode/idc/frankfurt/20180918-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180514-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [Vultr](/vultr/idc/frankfurt/20180514-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180514")



本文最初发表于[多地到Linode法兰克福[Frankfurt]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-linode-idc-frankfurt.html)
