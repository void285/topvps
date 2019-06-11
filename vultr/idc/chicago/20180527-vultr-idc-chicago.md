#  多地到Vultr芝加哥[Chicago]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr芝加哥\[Chicago\]机房的Ping测试（20180527）](/images/thumbnails/to_vultr_Chicago.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-芝加哥机房](https://vps123.top/vultr-facilities.html#chicago)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-芝加哥机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180527-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的975个有效测试样本中，共有超时点13个；响应均值为276毫秒，最快的三地区为河南、山东、河北，最慢的三地区为甘肃、青海、新疆；河南、湖南、广东、山东、北京等10处有响应超时情况；天津、黑龙江、吉林、贵州、海南等27处丢包率较高。海外21个国家地区的87个有效测试样本中，无超时点；响应均值为179毫秒，最快的三地区为加拿大、美国、意大利，最慢的三地区为南非、印度尼西亚、柬埔寨。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于芝加哥\[Chicago\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_usa-chicago_20180527_mainland.png)

**大陆各省份到Vultr美国-芝加哥机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
河南 | 58个 | 2个 | 254ms | 5.7%  
山东 | 53个 | 1个 | 255ms | 5.7%  
河北 | 35个 | 0 | 262ms | 5.8%  
山西 | 37个 | 0 | 262ms | 7.2%  
天津 | 5个 | 0 | 263ms | 17.5%  
黑龙江 | 39个 | 0 | 268ms | 14.3%  
北京 | 8个 | 1个 | 268ms | 4.8%  
湖南 | 43个 | 2个 | 268ms | 12.2%  
江苏 | 62个 | 1个 | 271ms | 8.5%  
广东 | 79个 | 2个 | 271ms | 5.0%  
福建 | 37个 | 0 | 273ms | 9.5%  
海南 | 14个 | 0 | 275ms | 12.8%  
浙江 | 51个 | 0 | 276ms | 9.3%  
陕西 | 32个 | 0 | 276ms | 10.2%  
辽宁 | 40个 | 0 | 276ms | 7.9%  
均值 | 975个 | 13个 | 276ms | 8.7%  
广西 | 40个 | 0 | 277ms | 10.2%  
上海 | 7个 | 0 | 280ms | 4.3%  
湖北 | 46个 | 1个 | 281ms | 10.1%  
吉林 | 19个 | 0 | 281ms | 13.8%  
内蒙古 | 33个 | 0 | 281ms | 10.4%  
江西 | 25个 | 0 | 282ms | 6.4%  
安徽 | 39个 | 0 | 282ms | 5.1%  
贵州 | 27个 | 0 | 287ms | 13.2%  
重庆 | 14个 | 1个 | 287ms | 7.3%  
云南 | 18个 | 1个 | 291ms | 11.6%  
宁夏 | 13个 | 0 | 291ms | 10.5%  
四川 | 46个 | 1个 | 295ms | 10.8%  
甘肃 | 22个 | 0 | 304ms | 5.5%  
青海 | 4个 | 0 | 306ms | 11.5%  
新疆 | 29个 | 0 | 314ms | 7.7%  
  
**简评：** 如果你考虑在Vultr的芝加哥[Chicago]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于芝加哥[Chicago]的机房的连通状况。到此机房的ping监测点共有975个，其中超时点13个，平均响应时间为276毫秒，丢包率为8%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的27个，超过300毫秒的3个；  
超时点较多的省份：北京；  
丢包率较高的省份：天津、黑龙江、湖南、海南、陕西、广西、湖北、吉林、内蒙古、贵州、云南、宁夏、四川、青海；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于芝加哥\[Chicago\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_usa-chicago_20180527_overseas.png)

**海外线路到Vultr美国-芝加哥机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 4个 | 0 | 29ms | 0  
美国 | 21个 | 0 | 52ms | 3.4%  
意大利 | 1个 | 0 | 95ms | -  
荷兰 | 1个 | 0 | 97ms | 0  
法国 | 1个 | 0 | 99ms | 0  
英国 | 2个 | 0 | 103ms | 0  
德国 | 3个 | 0 | 110ms | 0  
巴西 | 1个 | 0 | 140ms | 0  
日本 | 2个 | 0 | 165ms | 0  
均值 | 87个 | 0 | 179ms | 0.7%  
台湾 | 1个 | 0 | 181ms | -  
俄罗斯 | 1个 | 0 | 190ms | 0  
韩国 | 12个 | 0 | 194ms | 0  
香港 | 18个 | 0 | 211ms | 0  
越南 | 2个 | 0 | 211ms | 0  
新加坡 | 6个 | 0 | 222ms | 0  
澳大利亚 | 1个 | 0 | 229ms | 0  
菲律宾 | 1个 | 0 | 244ms | 1.0%  
马来西亚 | 5个 | 0 | 245ms | 0.2%  
南非 | 2个 | 0 | 279ms | 3.5%  
印度尼西亚 | 1个 | 0 | 284ms | 0  
柬埔寨 | 1个 | 0 | 385ms | 5.0%  
  
**简评：** 如果你考虑在Vultr的芝加哥[Chicago]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于芝加哥[Chicago]的机房的连通状况。到此机房的ping监测点共有87个，其中超时点0个，平均响应时间为179毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的4个，在100-200毫秒间的7个，在200-300毫秒间的8个，超过300毫秒的1个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180527 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180527 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180527-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180527")
    * [亚特兰大](/vultr/idc/atlanta/20180527-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180527")
    * [达拉斯](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")
    * [法兰克福](/vultr/idc/frankfurt/20180527-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180527")
    * [伦敦](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")
    * [洛杉矶](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [迈阿密](/vultr/idc/miami/20180527-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180527")
    * [新泽西](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [巴黎](/vultr/idc/paris/20180527-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180527")
    * [西雅图](/vultr/idc/seattle/20180527-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180527")
    * [硅谷](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [新加坡](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")
    * [悉尼](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [东京](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
  * 到Vultr芝加哥机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/chicago/20180514-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180514")
    * [20180622](/vultr/idc/chicago/20180622-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180622")
    * [20180804](/vultr/idc/chicago/20180804-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180804")
    * [20180918](/vultr/idc/chicago/20180918-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180918")



本文最初发表于[多地到Vultr芝加哥[Chicago]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-vultr-idc-chicago.html)
