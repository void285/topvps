#  多地到Linode新加坡[Singapore]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode新加坡\[Singapore\]机房的Ping测试（20180622）](/images/thumbnails/to_linode_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[新加坡-新加坡机房](https://vps123.top/linode-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180622-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的895个有效测试样本中，共有超时点29个；响应均值为264毫秒，最快的三地区为陕西、贵州、湖南，最慢的三地区为天津、重庆、香港；云南、江苏、浙江、河南、湖北等16处有响应超时情况；天津、吉林、青海、上海、重庆等29处丢包率较高。海外17个国家地区的53个有效测试样本中，无超时点；响应均值为134毫秒，最快的三地区为印度尼西亚、马来西亚、菲律宾，最慢的三地区为英国、南非、加拿大。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_idc_linode_singapore-singapore_20180622_mainland.png)

大陆各省份到Linode新加坡-新加坡机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
陕西 | 28个 | 1个 | 221ms | 14.7% | 河南 | 51个 | 2个 | 268ms | 11.0%  
贵州 | 25个 | 1个 | 228ms | 5.8% | 宁夏 | 14个 | 0 | 269ms | 14.6%  
湖南 | 35个 | 0 | 233ms | 4.7% | 辽宁 | 34个 | 1个 | 269ms | 13.3%  
广西 | 43个 | 0 | 235ms | 8.3% | 黑龙江 | 30个 | 0 | 270ms | 14.8%  
福建 | 34个 | 1个 | 245ms | 10.5% | 甘肃 | 17个 | 0 | 273ms | 14.2%  
北京 | 8个 | 0 | 245ms | 12.7% | 上海 | 8个 | 1个 | 279ms | 18.4%  
江西 | 23个 | 0 | 248ms | 12.4% | 四川 | 42个 | 1个 | 285ms | 11.6%  
广东 | 79个 | 1个 | 248ms | 8.1% | 内蒙古 | 33个 | 0 | 289ms | 14.0%  
山西 | 36个 | 0 | 251ms | 15.7% | 湖北 | 35个 | 2个 | 297ms | 10.7%  
海南 | 11个 | 0 | 253ms | 8.0% | 吉林 | 18个 | 0 | 309ms | 20.8%  
江苏 | 66个 | 3个 | 255ms | 14.8% | 青海 | 5个 | 0 | 315ms | 19.0%  
河北 | 30个 | 0 | 263ms | 14.0% | 新疆 | 18个 | 1个 | 317ms | 13.6%  
均值 | 895个 | 29个 | 264ms | 12.3% | 云南 | 21个 | 9个 | 320ms | 10.1%  
山东 | 38个 | 1个 | 267ms | 14.9% | 天津 | 3个 | 0 | 321ms | 22.3%  
浙江 | 49个 | 2个 | 267ms | 13.9% | 重庆 | 13个 | 1个 | 332ms | 17.8%  
安徽 | 36个 | 1个 | 267ms | 13.8% | 香港 | 12个 | 0 | - | -  
  
简评：如果你考虑在Linode的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有895个，其中超时点29个，平均响应时间为264毫秒，丢包率为12%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的24个，超过300毫秒的6个；  
超时点较多的省份：上海、云南；  
丢包率较高的省份：陕西、福建、北京、江西、山西、江苏、河北、山东、浙江、安徽、河南、宁夏、辽宁、黑龙江、甘肃、上海、四川、内蒙古、湖北、吉林、青海、新疆、云南、天津、重庆；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_idc_linode_singapore-singapore_20180622_overseas.png)

海外线路到Linode新加坡-新加坡机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
印度尼西亚 | 1个 | 0 | 23ms | 1.0% | 越南 | 3个 | 0 | 130ms | 1.7%  
马来西亚 | 5个 | 0 | 52ms | 0 | 均值 | 53个 | 0 | 134ms | 0.4%  
菲律宾 | 2个 | 0 | 55ms | 0.5% | 柬埔寨 | 1个 | 0 | 158ms | 0  
香港 | 12个 | 0 | 89ms | 0 | 法国 | 1个 | 0 | 184ms | 0  
新加坡 | 2个 | 0 | 92ms | 0 | 巴西 | 1个 | 0 | 195ms | 0  
台湾 | 1个 | 0 | 98ms | 0 | 美国 | 9个 | 0 | 205ms | 0  
日本 | 1个 | 0 | 102ms | 3.0% | 英国 | 2个 | 0 | 218ms | 0  
韩国 | 8个 | 0 | 102ms | 0 | 南非 | 2个 | 0 | 222ms | 0  
澳大利亚 | 1个 | 0 | 115ms | 0 | 加拿大 | 1个 | 0 | 248ms | 0  
  
简评：如果你考虑在Linode的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有53个，其中超时点0个，平均响应时间为134毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的5个，在100-200毫秒间的7个，在200-300毫秒间的4个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180622 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180622 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180622-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180622")
    * [达拉斯](/linode/idc/dallas/20180622-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180622")
    * [法兰克福](/linode/idc/frankfurt/20180622-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180622")
    * [佛利蒙](/linode/idc/fremont/20180622-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180622")
    * [伦敦](/linode/idc/london/20180622-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180622")
    * [纽瓦克](/linode/idc/newark/20180622-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180622")
    * [东京](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")
  * 到Linode新加坡机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/singapore/20180514-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180514")
    * [20180527](/linode/idc/singapore/20180527-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180527")
    * [20180804](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")
    * [20180918](/linode/idc/singapore/20180918-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180622-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [Vultr](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")



本文最初发表于[多地到Linode新加坡[Singapore]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-linode-idc-singapore.html)
