#  多地到Vultr新泽西[NewJersey]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr新泽西\[NewJersey\]机房的Ping测试（20180918）](/images/thumbnails/to_vultr_Sydney.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-新泽西机房](https://vps123.top/vultr-facilities.html#newjersey)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-新泽西机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180918-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Vultr美国-新泽西机房的PING测试结果，连通概况如下：大陆31个省市的1439个有效测试样本中，共有超时点11个；响应均值为273毫秒，最快的三地区为上海、北京、安徽，最慢的三地区为吉林、新疆、西藏；江苏、浙江、安徽、广东、贵州等7处有响应超时情况；吉林、辽宁、河南、山西、内蒙古等12处丢包率较高。海外16个国家地区的80个有效测试样本中，无超时点；响应均值为180毫秒，最快的三地区为加拿大、意大利、美国，最慢的三地区为越南、马来西亚、印度尼西亚。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于新泽西\[NewJersey\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_usa-newjersey_20180918_mainland.png)

**大陆各省份到Vultr美国-新泽西机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 8个 | 0 | 247ms | 3.1%  
北京 | 8个 | 0 | 250ms | 1.4%  
安徽 | 71个 | 1个 | 251ms | 2.8%  
广东 | 124个 | 1个 | 252ms | 4.4%  
宁夏 | 7个 | 0 | 255ms | 0  
江苏 | 93个 | 4个 | 256ms | 4.5%  
福建 | 47个 | 0 | 257ms | 2.2%  
青海 | 5个 | 0 | 260ms | 0  
浙江 | 65个 | 2个 | 261ms | 2.6%  
江西 | 40个 | 0 | 261ms | 4.3%  
天津 | 7个 | 0 | 265ms | 0  
湖北 | 52个 | 0 | 266ms | 3.9%  
湖南 | 71个 | 0 | 267ms | 5.6%  
广西 | 64个 | 0 | 268ms | 3.0%  
重庆 | 9个 | 0 | 269ms | 2.2%  
河北 | 60个 | 0 | 269ms | 7.4%  
山东 | 94个 | 0 | 271ms | 8.2%  
甘肃 | 32个 | 0 | 272ms | 0.1%  
均值 | 1439个 | 11个 | 273ms | 5.6%  
海南 | 14个 | 0 | 275ms | 6.3%  
陕西 | 43个 | 0 | 277ms | 3.6%  
辽宁 | 60个 | 0 | 277ms | 11.3%  
贵州 | 43个 | 1个 | 279ms | 6.8%  
云南 | 34个 | 0 | 282ms | 1.3%  
内蒙古 | 57个 | 0 | 283ms | 8.5%  
山西 | 59个 | 1个 | 286ms | 9.2%  
四川 | 71个 | 1个 | 287ms | 2.8%  
河南 | 87个 | 0 | 294ms | 9.7%  
黑龙江 | 56个 | 0 | 306ms | 8.1%  
吉林 | 21个 | 0 | 308ms | 18.7%  
新疆 | 35个 | 0 | 329ms | 4.5%  
西藏 | 2个 | 0 | 351ms | 7.0%  
  
**简评：** 如果你考虑在Vultr的新泽西[NewJersey]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新泽西[NewJersey]的机房的连通状况。到此机房的ping监测点共有1439个，其中超时点11个，平均响应时间为273毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的27个，超过300毫秒的4个；  
丢包率较高的省份：辽宁、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于新泽西\[NewJersey\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_usa-newjersey_20180918_overseas.png)

**海外线路到Vultr美国-新泽西机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 3个 | 0 | 23ms | 0  
意大利 | 1个 | 0 | 74ms | -  
美国 | 16个 | 0 | 82ms | 0  
德国 | 3个 | 0 | 97ms | 0  
俄罗斯 | 1个 | 0 | 122ms | -  
台湾 | 2个 | 0 | 127ms | 0  
荷兰 | 1个 | 0 | 171ms | 0  
均值 | 80个 | 0 | 180ms | 0.6%  
韩国 | 12个 | 0 | 185ms | 0  
香港 | 21个 | 0 | 189ms | 0  
日本 | 3个 | 0 | 194ms | 3.3%  
新加坡 | 5个 | 0 | 212ms | 0  
菲律宾 | 1个 | 0 | 224ms | 1.0%  
澳大利亚 | 2个 | 0 | 240ms | 0.5%  
越南 | 2个 | 0 | 241ms | 0  
马来西亚 | 6个 | 0 | 278ms | 0  
印度尼西亚 | 1个 | 0 | 427ms | 3.3%  
  
**简评：** 如果你考虑在Vultr的新泽西[NewJersey]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新泽西[NewJersey]的机房的连通状况。到此机房的ping监测点共有80个，其中超时点0个，平均响应时间为180毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的3个，在100-200毫秒间的6个，在200-300毫秒间的5个，超过300毫秒的1个；

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
    * [巴黎](/vultr/idc/paris/20180918-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180918")
    * [西雅图](/vultr/idc/seattle/20180918-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180918")
    * [硅谷](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")
    * [新加坡](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")
    * [悉尼](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")
    * [东京](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 到Vultr新泽西机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/newjersey/20180514-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180514")
    * [20180527](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [20180622](/vultr/idc/newjersey/20180622-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180622")
    * [20180804](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")



本文最初发表于[多地到Vultr新泽西[NewJersey]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-vultr-idc-newjersey.html)
