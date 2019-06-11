#  多地到Vultr东京[Tokyo]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr东京\[Tokyo\]机房的Ping测试（20180918）](/images/thumbnails/to_vultr_Miami.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[日本-东京机房](https://vps123.top/vultr-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180918-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Vultr日本-东京机房的PING测试结果，连通概况如下：大陆31个省市的1406个有效测试样本中，共有超时点18个；响应均值为139毫秒，最快的三地区为山西、吉林、上海，最慢的三地区为云南、新疆、西藏；江苏、浙江、山西、上海、广西等10处有响应超时情况；河南、山东、西藏、北京、新疆丢包率较高。海外17个国家地区的72个有效测试样本中，无超时点；响应均值为184毫秒，最快的三地区为日本、韩国、越南，最慢的三地区为荷兰、澳大利亚、赞比亚；菲律宾、台湾、赞比亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_japan-tokyo_20180918_mainland.png)

**大陆各省份到Vultr日本-东京机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
山西 | 56个 | 2个 | 109ms | 0.9%  
吉林 | 23个 | 0 | 113ms | 0.9%  
上海 | 8个 | 1个 | 113ms | 3.1%  
辽宁 | 59个 | 0 | 118ms | 3.2%  
广西 | 59个 | 1个 | 121ms | 1.8%  
黑龙江 | 54个 | 0 | 124ms | 0.7%  
内蒙古 | 54个 | 0 | 124ms | 2.7%  
山东 | 92个 | 0 | 126ms | 7.2%  
河北 | 58个 | 0 | 126ms | 1.0%  
河南 | 87个 | 0 | 127ms | 7.6%  
北京 | 8个 | 0 | 133ms | 5.8%  
湖南 | 71个 | 0 | 133ms | 2.9%  
天津 | 7个 | 0 | 136ms | 3.7%  
江西 | 39个 | 0 | 136ms | 1.9%  
海南 | 13个 | 0 | 139ms | 1.8%  
均值 | 1406个 | 18个 | 139ms | 2.9%  
福建 | 42个 | 0 | 140ms | 2.5%  
江苏 | 91个 | 6个 | 142ms | 2.4%  
安徽 | 69个 | 1个 | 142ms | 2.5%  
重庆 | 8个 | 0 | 143ms | 2.0%  
陕西 | 43个 | 0 | 144ms | 1.4%  
浙江 | 66个 | 3个 | 145ms | 1.7%  
广东 | 123个 | 1个 | 146ms | 1.3%  
贵州 | 43个 | 1个 | 153ms | 1.9%  
湖北 | 52个 | 1个 | 160ms | 1.7%  
宁夏 | 7个 | 0 | 162ms | 4.5%  
四川 | 72个 | 1个 | 168ms | 3.4%  
青海 | 5个 | 0 | 168ms | 4.7%  
甘肃 | 32个 | 0 | 170ms | 4.2%  
云南 | 33个 | 0 | 176ms | 2.8%  
新疆 | 31个 | 0 | 182ms | 5.3%  
西藏 | 1个 | 0 | 310ms | 7.0%  
  
**简评：** 如果你考虑在Vultr的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有1406个，其中超时点18个，平均响应时间为139毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的30个，超过300毫秒的1个；  
超时点较多的省份：上海；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_japan-tokyo_20180918_overseas.png)

**海外线路到Vultr日本-东京机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
日本 | 3个 | 0 | 33ms | 1.3%  
韩国 | 10个 | 0 | 100ms | 0  
越南 | 2个 | 0 | 101ms | 0  
美国 | 12个 | 0 | 102ms | 0  
新加坡 | 5个 | 0 | 103ms | 0  
台湾 | 1个 | 0 | 113ms | 10.0%  
香港 | 17个 | 0 | 126ms | 0  
马来西亚 | 6个 | 0 | 129ms | 0.3%  
菲律宾 | 2个 | 0 | 140ms | 15.0%  
加拿大 | 3个 | 0 | 163ms | 0  
均值 | 72个 | 0 | 184ms | 2.4%  
印度尼西亚 | 1个 | 0 | 213ms | 3.3%  
俄罗斯 | 1个 | 0 | 218ms | -  
意大利 | 1个 | 0 | 242ms | -  
德国 | 3个 | 0 | 258ms | 0  
荷兰 | 1个 | 0 | 335ms | 0  
澳大利亚 | 2个 | 0 | 342ms | 0  
赞比亚 | 2个 | 0 | 414ms | 5.8%  
  
**简评：** 如果你考虑在Vultr的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有72个，其中超时点0个，平均响应时间为184毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的8个，在200-300毫秒间的4个，超过300毫秒的3个；  
丢包率较高的国家/地区：台湾、菲律宾；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180918 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180918 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180918-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180918")
    * [亚特兰大](/vultr/idc/atlanta/20180918-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180918")
    * [芝加哥](/vultr/idc/chicago/20180918-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180918")
    * [达拉斯](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
    * [法兰克福](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")
    * [伦敦](/vultr/idc/london/20180918-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180918")
    * [洛杉矶](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
    * [迈阿密](/vultr/idc/miami/20180918-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180918")
    * [新泽西](/vultr/idc/newjersey/20180918-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180918")
    * [巴黎](/vultr/idc/paris/20180918-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180918")
    * [西雅图](/vultr/idc/seattle/20180918-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180918")
    * [硅谷](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")
    * [新加坡](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")
    * [悉尼](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")
  * 到Vultr东京机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
    * [20180527](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
    * [20180622](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
    * [20180804](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/tokyo/20180918-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180918")



本文最初发表于[多地到Vultr东京[Tokyo]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-vultr-idc-tokyo.html)
