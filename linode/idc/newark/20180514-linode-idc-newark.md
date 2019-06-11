#  多地到Linode纽瓦克[Newark]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode纽瓦克\[Newark\]机房的Ping测试（20180514）](/images/thumbnails/to_linode_Newark.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-纽瓦克机房](https://vps123.top/linode-facilities.html#newark)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-纽瓦克机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180514-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Linode美国-纽瓦克机房的PING测试结果，连通概况如下：大陆30个省市的984个有效测试样本中，共有超时点12个；响应均值为290毫秒，最快的三地区为上海、安徽、江苏，最慢的三地区为湖南、甘肃、新疆；浙江、江苏、广东、福建、北京等7处有响应超时情况；湖南丢包率较高。海外17个国家地区的78个有效测试样本中，无超时点；响应均值为181毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为马来西亚、南非、印度尼西亚。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于纽瓦克市\[\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_usa-newark_20180514_mainland.png)

**大陆各省份到Linode美国-纽瓦克机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 8个 | 0 | 247ms | 0.5%  
安徽 | 43个 | 0 | 257ms | 4.7%  
江苏 | 63个 | 2个 | 261ms | 3.2%  
福建 | 39个 | 1个 | 264ms | 1.0%  
江西 | 25个 | 0 | 269ms | 2.0%  
天津 | 4个 | 0 | 272ms | 4.3%  
浙江 | 52个 | 4个 | 274ms | 2.6%  
北京 | 7个 | 1个 | 274ms | 2.7%  
吉林 | 13个 | 0 | 275ms | 1.2%  
陕西 | 32个 | 0 | 276ms | 2.9%  
重庆 | 15个 | 1个 | 276ms | 2.1%  
广东 | 79个 | 2个 | 279ms | 2.6%  
广西 | 39个 | 0 | 283ms | 3.5%  
青海 | 4个 | 0 | 285ms | 4.3%  
贵州 | 27个 | 0 | 286ms | 1.3%  
海南 | 10个 | 0 | 290ms | 3.1%  
均值 | 984个 | 12个 | 290ms | 3.8%  
山东 | 53个 | 1个 | 292ms | 4.2%  
河北 | 34个 | 0 | 294ms | 3.2%  
河南 | 58个 | 0 | 295ms | 3.7%  
辽宁 | 41个 | 0 | 299ms | 3.9%  
湖北 | 46个 | 0 | 300ms | 2.9%  
云南 | 24个 | 0 | 301ms | 2.8%  
山西 | 38个 | 0 | 305ms | 4.6%  
黑龙江 | 38个 | 0 | 307ms | 4.4%  
宁夏 | 12个 | 0 | 307ms | 2.3%  
内蒙古 | 35个 | 0 | 310ms | 3.6%  
四川 | 48个 | 0 | 313ms | 1.8%  
湖南 | 47个 | 0 | 313ms | 19.1%  
甘肃 | 22个 | 0 | 316ms | 3.0%  
新疆 | 28个 | 0 | 328ms | 2.7%  
  
**简评：** 如果你考虑在Linode的纽瓦克市[]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽瓦克市[]的机房的连通状况。到此机房的ping监测点共有984个，其中超时点12个，平均响应时间为290毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的21个，超过300毫秒的9个；  
超时点较多的省份：北京；  
丢包率较高的省份：湖南；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于纽瓦克市\[\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/linode_20180514/plot_idc_linode_usa-newark_20180514_overseas.png)

**海外线路到Linode美国-纽瓦克机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 3个 | 0 | 16ms | 0  
美国 | 18个 | 0 | 63ms | 0.4%  
法国 | 2个 | 0 | 80ms | 0  
英国 | 2个 | 0 | 84ms | 0  
德国 | 2个 | 0 | 97ms | 0  
巴西 | 1个 | 0 | 127ms | 0  
俄罗斯 | 1个 | 0 | 166ms | 0  
日本 | 2个 | 0 | 173ms | 0  
均值 | 78个 | 0 | 181ms | 0.4%  
台湾 | 1个 | 0 | 197ms | -  
韩国 | 13个 | 0 | 209ms | 0  
菲律宾 | 1个 | 0 | 228ms | 0  
澳大利亚 | 2个 | 0 | 228ms | 0.5%  
新加坡 | 6个 | 0 | 241ms | 0  
香港 | 18个 | 0 | 252ms | 0  
马来西亚 | 4个 | 0 | 271ms | 0.8%  
南非 | 1个 | 0 | 283ms | 0  
印度尼西亚 | 1个 | 0 | 375ms | 5.0%  
  
**简评：** 如果你考虑在Linode的纽瓦克市[]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽瓦克市[]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点0个，平均响应时间为181毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的4个，在100-200毫秒间的4个，在200-300毫秒间的7个，超过300毫秒的1个；

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
    * [新加坡](/linode/idc/singapore/20180514-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180514")
    * [东京](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
  * 到Linode纽瓦克机房的 _其他近期报告_ ： 
    * [20180527](/linode/idc/newark/20180527-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180527")
    * [20180622](/linode/idc/newark/20180622-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180622")
    * [20180804](/linode/idc/newark/20180804-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180804")
    * [20180918](/linode/idc/newark/20180918-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180918")



本文最初发表于[多地到Linode纽瓦克[Newark]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-linode-idc-newark.html)
