#  多地到Linode亚特兰大[Atlanta]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode亚特兰大\[Atlanta\]机房的Ping测试（20180622）](/images/thumbnails/to_linode_Atlanta.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-亚特兰大机房](https://vps123.top/linode-facilities.html#atlanta)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-亚特兰大机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180622-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的903个有效测试样本中，共有超时点20个；响应均值为275毫秒，最快的三地区为北京、天津、浙江，最慢的三地区为甘肃、新疆、香港；云南、江苏、浙江、上海、湖南等10处有响应超时情况；四川、福建、安徽、云南、广西等9处丢包率较高。海外18个国家地区的82个有效测试样本中，无超时点；响应均值为171毫秒，最快的三地区为美国、加拿大、德国，最慢的三地区为越南、马来西亚、柬埔寨。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于亚特兰大\[Atlanta\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_idc_linode_usa-atlanta_20180622_mainland.png)

大陆各省份到Linode美国-亚特兰大机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 8个 | 0 | 221ms | 0.3% | 贵州 | 25个 | 0 | 277ms | 4.5%  
天津 | 3个 | 0 | 230ms | 1.7% | 江西 | 22个 | 1个 | 278ms | 5.7%  
浙江 | 49个 | 1个 | 246ms | 3.4% | 安徽 | 35个 | 1个 | 280ms | 7.2%  
江苏 | 68个 | 3个 | 248ms | 3.2% | 吉林 | 17个 | 0 | 282ms | 5.1%  
广东 | 70个 | 0 | 256ms | 4.2% | 陕西 | 27个 | 0 | 285ms | 1.7%  
上海 | 8个 | 1个 | 260ms | 3.3% | 内蒙古 | 34个 | 0 | 286ms | 1.7%  
海南 | 11个 | 0 | 262ms | 1.9% | 辽宁 | 34个 | 1个 | 286ms | 3.9%  
山东 | 44个 | 0 | 266ms | 2.9% | 河南 | 52个 | 1个 | 287ms | 3.6%  
湖南 | 35个 | 1个 | 266ms | 2.3% | 黑龙江 | 30个 | 0 | 298ms | 5.3%  
河北 | 34个 | 0 | 267ms | 3.0% | 宁夏 | 14个 | 0 | 298ms | 4.4%  
湖北 | 34个 | 0 | 268ms | 5.3% | 云南 | 22个 | 9个 | 299ms | 6.2%  
广西 | 43个 | 0 | 269ms | 5.7% | 青海 | 5个 | 0 | 304ms | 3.6%  
山西 | 35个 | 0 | 272ms | 2.2% | 四川 | 42个 | 0 | 308ms | 8.8%  
重庆 | 13个 | 1个 | 273ms | 5.0% | 甘肃 | 18个 | 0 | 316ms | 2.8%  
福建 | 33个 | 0 | 275ms | 7.5% | 新疆 | 18个 | 0 | 319ms | 4.9%  
均值 | 903个 | 20个 | 275ms | 4.2% | 香港 | 20个 | 0 | - | -  
  
简评：如果你考虑在Linode的亚特兰大[Atlanta]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于亚特兰大[Atlanta]的机房的连通状况。到此机房的ping监测点共有903个，其中超时点20个，平均响应时间为275毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的26个，超过300毫秒的4个；  
超时点较多的省份：上海、云南；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于亚特兰大\[Atlanta\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_idc_linode_usa-atlanta_20180622_overseas.png)

海外线路到Linode美国-亚特兰大机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 21个 | 0 | 52ms | 0.1% | 台湾 | 2个 | 0 | 184ms | 0  
加拿大 | 1个 | 0 | 69ms | 0 | 香港 | 20个 | 0 | 185ms | 0  
德国 | 1个 | 0 | 90ms | - | 新加坡 | 5个 | 0 | 196ms | 0  
意大利 | 1个 | 0 | 96ms | - | 韩国 | 13个 | 0 | 214ms | 0  
巴西 | 1个 | 0 | 99ms | 0 | 菲律宾 | 2个 | 0 | 218ms | 0  
法国 | 1个 | 0 | 101ms | 0 | 澳大利亚 | 1个 | 0 | 241ms | 0  
英国 | 2个 | 0 | 164ms | 0 | 越南 | 2个 | 0 | 244ms | 0  
日本 | 2个 | 0 | 167ms | 1.0% | 马来西亚 | 4个 | 0 | 254ms | 0.3%  
南非 | 2个 | 0 | 171ms | 0 | 柬埔寨 | 1个 | 0 | 333ms | 0  
均值 | 82个 | 0 | 171ms | 0.1% |  |  |  |  |   
  
简评：如果你考虑在Linode的亚特兰大[Atlanta]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于亚特兰大[Atlanta]的机房的连通状况。到此机房的ping监测点共有82个，其中超时点0个，平均响应时间为171毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50-100毫秒间的5个，在100-200毫秒间的7个，在200-300毫秒间的5个，超过300毫秒的1个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180622 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180622 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [达拉斯](/linode/idc/dallas/20180622-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180622")
    * [法兰克福](/linode/idc/frankfurt/20180622-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180622")
    * [佛利蒙](/linode/idc/fremont/20180622-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180622")
    * [伦敦](/linode/idc/london/20180622-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180622")
    * [纽瓦克](/linode/idc/newark/20180622-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180622")
    * [新加坡](/linode/idc/singapore/20180622-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180622")
    * [东京](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")
  * 到Linode亚特兰大机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/atlanta/20180514-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180514")
    * [20180527](/linode/idc/atlanta/20180527-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180527")
    * [20180804](/linode/idc/atlanta/20180804-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180804")
    * [20180918](/linode/idc/atlanta/20180918-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180918")
  * 本期报告：在亚特兰大部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/atlanta/20180622-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180622")



本文最初发表于[多地到Linode亚特兰大[Atlanta]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-linode-idc-atlanta.html)
