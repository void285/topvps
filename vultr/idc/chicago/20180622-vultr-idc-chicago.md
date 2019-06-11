#  多地到Vultr芝加哥[Chicago]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr芝加哥\[Chicago\]机房的Ping测试（20180622）](/images/thumbnails/to_vultr_Chicago.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-芝加哥机房](https://vps123.top/vultr-facilities.html#chicago)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-芝加哥机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180622-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的923个有效测试样本中，共有超时点24个；响应均值为284毫秒，最快的三地区为天津、福建、北京，最慢的三地区为新疆、云南、香港；云南、浙江、江苏、广东、安徽等12处有响应超时情况；吉林、山西、山东、河北、辽宁等26处丢包率较高。海外18个国家地区的82个有效测试样本中，共有超时点1个；响应均值为162毫秒，最快的三地区为加拿大、美国、德国，最慢的三地区为澳大利亚、印度尼西亚、马来西亚；香港有响应超时情况。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于芝加哥\[Chicago\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-chicago_20180622_mainland.png)

**大陆各省份到Vultr美国-芝加哥机房的测速数据 [20180622]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 3个 | 0 | 254ms | 22.7%  
福建 | 29个 | 0 | 259ms | 17.6%  
北京 | 9个 | 0 | 262ms | 7.6%  
浙江 | 52个 | 2个 | 265ms | 4.5%  
安徽 | 36个 | 1个 | 267ms | 10.4%  
上海 | 7个 | 1个 | 272ms | 2.9%  
陕西 | 26个 | 0 | 273ms | 11.8%  
江苏 | 68个 | 2个 | 275ms | 15.7%  
湖南 | 39个 | 0 | 275ms | 19.3%  
湖北 | 38个 | 0 | 277ms | 12.8%  
江西 | 26个 | 0 | 277ms | 12.6%  
重庆 | 13个 | 0 | 278ms | 12.2%  
山西 | 34个 | 0 | 279ms | 30.8%  
广西 | 44个 | 0 | 280ms | 14.3%  
均值 | 923个 | 24个 | 284ms | 17.6%  
山东 | 45个 | 0 | 285ms | 29.3%  
海南 | 10个 | 0 | 285ms | 16.0%  
内蒙古 | 34个 | 1个 | 289ms | 21.0%  
河北 | 34个 | 0 | 290ms | 28.6%  
贵州 | 23个 | 0 | 291ms | 17.3%  
广东 | 73个 | 2个 | 291ms | 15.2%  
黑龙江 | 32个 | 1个 | 292ms | 22.5%  
辽宁 | 35个 | 1个 | 293ms | 26.2%  
甘肃 | 18个 | 0 | 294ms | 0.8%  
吉林 | 18个 | 1个 | 296ms | 33.2%  
四川 | 41个 | 0 | 298ms | 14.2%  
河南 | 51个 | 1个 | 300ms | 22.6%  
宁夏 | 13个 | 0 | 302ms | 17.0%  
青海 | 5个 | 0 | 308ms | 0  
新疆 | 18个 | 0 | 312ms | 21.5%  
云南 | 25个 | 10个 | 318ms | 10.8%  
香港 | 24个 | 1个 | - | -  
  
**简评：** 如果你考虑在Vultr的芝加哥[Chicago]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于芝加哥[Chicago]的机房的连通状况。到此机房的ping监测点共有923个，其中超时点24个，平均响应时间为284毫秒，丢包率为17%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的26个，超过300毫秒的4个；  
超时点较多的省份：上海、云南；  
丢包率较高的省份：天津、福建、安徽、陕西、江苏、湖南、湖北、江西、重庆、山西、广西、山东、海南、内蒙古、河北、贵州、广东、黑龙江、辽宁、吉林、四川、河南、宁夏、新疆、云南；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于芝加哥\[Chicago\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-chicago_20180622_overseas.png)

**海外线路到Vultr美国-芝加哥机房的测速数据 [20180622]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 2个 | 0 | 27ms | 0  
美国 | 18个 | 0 | 50ms | 0  
德国 | 1个 | 0 | 96ms | -  
法国 | 1个 | 0 | 98ms | 0  
意大利 | 1个 | 0 | 98ms | -  
巴西 | 1个 | 0 | 99ms | 0  
均值 | 82个 | 1个 | 162ms | 0.3%  
南非 | 2个 | 0 | 170ms | 0  
日本 | 1个 | 0 | 174ms | -  
台湾 | 2个 | 0 | 176ms | 0  
英国 | 2个 | 0 | 182ms | 0  
香港 | 24个 | 1个 | 183ms | 0  
新加坡 | 5个 | 0 | 187ms | 0  
韩国 | 14个 | 0 | 195ms | 0  
菲律宾 | 2个 | 0 | 199ms | 0.5%  
越南 | 2个 | 0 | 210ms | 0  
澳大利亚 | 1个 | 0 | 217ms | 2.0%  
印度尼西亚 | 1个 | 0 | 265ms | 0  
马来西亚 | 2个 | 0 | 288ms | 2.5%  
  
**简评：** 如果你考虑在Vultr的芝加哥[Chicago]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于芝加哥[Chicago]的机房的连通状况。到此机房的ping监测点共有82个，其中超时点1个，平均响应时间为162毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的4个，在100-200毫秒间的8个，在200-300毫秒间的4个；

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
    * [东京](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
  * 到Vultr芝加哥机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/chicago/20180514-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180514")
    * [20180527](/vultr/idc/chicago/20180527-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180527")
    * [20180804](/vultr/idc/chicago/20180804-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180804")
    * [20180918](/vultr/idc/chicago/20180918-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180918")



本文最初发表于[多地到Vultr芝加哥[Chicago]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-vultr-idc-chicago.html)
