#  多地到Vultr东京[Tokyo]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr东京\[Tokyo\]机房的Ping测试（20180622）](/images/thumbnails/to_vultr_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[日本-东京机房](https://vps123.top/vultr-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180622-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的912个有效测试样本中，共有超时点29个；响应均值为181毫秒，最快的三地区为湖南、福建、贵州，最慢的三地区为云南、新疆、香港；云南、江苏、浙江、四川、广东等11处有响应超时情况；天津、青海、浙江、吉林、北京等29处丢包率较高。海外15个国家地区的47个有效测试样本中，无超时点；响应均值为147毫秒，最快的三地区为日本、台湾、越南，最慢的三地区为南非、巴西、澳大利亚；澳大利亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_japan-tokyo_20180622_mainland.png)

大陆各省份到Vultr日本-东京机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
湖南 | 38个 | 0 | 140ms | 4.9% | 河北 | 35个 | 0 | 188ms | 10.3%  
福建 | 33个 | 0 | 144ms | 13.9% | 辽宁 | 35个 | 1个 | 189ms | 9.9%  
贵州 | 22个 | 0 | 145ms | 6.6% | 浙江 | 49个 | 3个 | 191ms | 18.5%  
广东 | 75个 | 2个 | 158ms | 8.5% | 黑龙江 | 32个 | 0 | 195ms | 12.1%  
安徽 | 36个 | 2个 | 161ms | 14.0% | 甘肃 | 17个 | 0 | 195ms | 17.1%  
江西 | 26个 | 0 | 165ms | 11.2% | 湖北 | 39个 | 0 | 199ms | 11.1%  
广西 | 44个 | 0 | 166ms | 8.3% | 山东 | 37个 | 0 | 201ms | 10.4%  
海南 | 11个 | 0 | 166ms | 7.6% | 青海 | 5个 | 0 | 201ms | 20.2%  
北京 | 9个 | 0 | 168ms | 18.3% | 四川 | 41个 | 3个 | 202ms | 6.6%  
山西 | 34个 | 0 | 171ms | 8.6% | 重庆 | 12个 | 0 | 206ms | 17.6%  
江苏 | 68个 | 4个 | 172ms | 12.2% | 内蒙古 | 34个 | 0 | 207ms | 14.1%  
宁夏 | 13个 | 0 | 176ms | 16.5% | 天津 | 3个 | 0 | 208ms | 34.9%  
均值 | 912个 | 29个 | 181ms | 11.6% | 吉林 | 18个 | 0 | 224ms | 18.5%  
河南 | 52个 | 1个 | 182ms | 9.2% | 云南 | 25个 | 10个 | 232ms | 13.3%  
陕西 | 30个 | 1个 | 182ms | 13.6% | 新疆 | 19个 | 1个 | 242ms | 15.9%  
上海 | 8个 | 1个 | 182ms | 18.2% | 香港 | 12个 | 0 | - | -  
  
简评：如果你考虑在Vultr的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有912个，其中超时点29个，平均响应时间为181毫秒，丢包率为11%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的21个，在200-300毫秒间的9个；  
超时点较多的省份：上海、云南；  
丢包率较高的省份：福建、安徽、江西、北京、江苏、宁夏、陕西、上海、河北、浙江、黑龙江、甘肃、湖北、山东、青海、重庆、内蒙古、天津、吉林、云南、新疆；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_japan-tokyo_20180622_overseas.png)

海外线路到Vultr日本-东京机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
日本 | 1个 | 0 | 23ms | 2.0% | 美国 | 10个 | 0 | 132ms | 0  
台湾 | 1个 | 0 | 29ms | 0 | 均值 | 47个 | 0 | 147ms | 0.6%  
越南 | 2个 | 0 | 73ms | 0 | 加拿大 | 1个 | 0 | 179ms | 0  
菲律宾 | 2个 | 0 | 78ms | 0 | 英国 | 2个 | 0 | 199ms | 0  
香港 | 12个 | 0 | 79ms | 0 | 法国 | 1个 | 0 | 230ms | 0  
韩国 | 8个 | 0 | 92ms | 0.4% | 南非 | 2个 | 0 | 270ms | 0  
印度尼西亚 | 1个 | 0 | 97ms | 0 | 巴西 | 1个 | 0 | 280ms | 0  
新加坡 | 2个 | 0 | 98ms | 0 | 澳大利亚 | 1个 | 0 | 349ms | 6.0%  
  
简评：如果你考虑在Vultr的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有47个，其中超时点0个，平均响应时间为147毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的6个，在100-200毫秒间的3个，在200-300毫秒间的3个，超过300毫秒的1个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180622 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180622 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180622-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180622")
    * [亚特兰大](/vultr/idc/atlanta/20180622-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180622")
    * [芝加哥](/vultr/idc/chicago/20180622-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180622")
    * [达拉斯](/vultr/idc/dallas/20180622-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180622")
    * [法兰克福](/vultr/idc/frankfurt/20180622-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180622")
    * [伦敦](/vultr/idc/london/20180622-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180622")
    * [洛杉矶](/vultr/idc/losangeles/20180622-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180622")
    * [迈阿密](/vultr/idc/miami/20180622-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180622")
    * [新泽西](/vultr/idc/newjersey/20180622-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180622")
    * [巴黎](/vultr/idc/paris/20180622-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180622")
    * [西雅图](/vultr/idc/seattle/20180622-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180622")
    * [硅谷](/vultr/idc/siliconvalley/20180622-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180622")
    * [新加坡](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [悉尼](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
  * 到Vultr东京机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
    * [20180527](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
    * [20180804](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
    * [20180918](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")



本文最初发表于[多地到Vultr东京[Tokyo]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-vultr-idc-tokyo.html)
