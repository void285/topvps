#  多地到Vultr新加坡[Singapore]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr新加坡\[Singapore\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[新加坡-新加坡机房](https://vps123.top/vultr-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的3157个有效测试样本中，共有超时点68个；响应均值为243毫秒，最快的三地区为广东、湖南、重庆，最慢的三地区为内蒙古、辽宁、吉林；江苏、浙江、辽宁、上海、广东等8处有响应超时情况；青海、安徽、宁夏、江西、上海等30处丢包率较高。海外19个国家地区的216个有效测试样本中，无超时点；响应均值为179毫秒，最快的三地区为印度尼西亚、新加坡、台湾，最慢的三地区为南非、俄罗斯、菲律宾；菲律宾丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_singapore-singapore_20180804_mainland.png)

**大陆各省份到Vultr新加坡-新加坡机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
广东 | 282个 | 3个 | 178ms | 7.0%  
湖南 | 141个 | 0 | 191ms | 12.4%  
重庆 | 41个 | 0 | 196ms | 10.0%  
上海 | 27个 | 4个 | 206ms | 30.1%  
江西 | 75个 | 0 | 215ms | 32.0%  
海南 | 28个 | 0 | 215ms | 14.1%  
浙江 | 174个 | 22个 | 218ms | 25.4%  
河南 | 199个 | 0 | 223ms | 14.4%  
云南 | 67个 | 0 | 223ms | 15.1%  
安徽 | 112个 | 0 | 223ms | 35.0%  
贵州 | 94个 | 3个 | 226ms | 19.3%  
广西 | 124个 | 0 | 227ms | 14.7%  
福建 | 88个 | 3个 | 228ms | 26.9%  
湖北 | 113个 | 0 | 228ms | 14.4%  
山东 | 210个 | 0 | 234ms | 17.8%  
江苏 | 242个 | 24个 | 239ms | 25.7%  
北京 | 36个 | 0 | 240ms | 10.9%  
均值 | 3157个 | 68个 | 243ms | 18.8%  
陕西 | 97个 | 0 | 255ms | 16.7%  
河北 | 132个 | 0 | 262ms | 13.8%  
四川 | 169个 | 3个 | 274ms | 16.5%  
甘肃 | 60个 | 0 | 278ms | 30.0%  
黑龙江 | 84个 | 0 | 280ms | 18.2%  
宁夏 | 16个 | 0 | 285ms | 32.8%  
天津 | 20个 | 0 | 288ms | 22.3%  
山西 | 113个 | 0 | 291ms | 14.3%  
新疆 | 75个 | 0 | 298ms | 27.3%  
西藏 | 4个 | 0 | 306ms | 4.0%  
青海 | 8个 | 0 | 308ms | 36.0%  
内蒙古 | 112个 | 0 | 314ms | 20.1%  
辽宁 | 150个 | 6个 | 315ms | 22.5%  
吉林 | 64个 | 0 | 338ms | 23.8%  
  
**简评：** 如果你考虑在Vultr的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有3157个，其中超时点68个，平均响应时间为243毫秒，丢包率为18%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的3个，在200-300毫秒间的23个，超过300毫秒的5个；  
超时点较多的省份：上海、浙江；  
丢包率较高的省份：湖南、重庆、上海、江西、海南、浙江、河南、云南、安徽、贵州、广西、福建、湖北、山东、江苏、北京、陕西、河北、四川、甘肃、黑龙江、宁夏、天津、山西、新疆、青海、内蒙古、辽宁、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_singapore-singapore_20180804_overseas.png)

**海外线路到Vultr新加坡-新加坡机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
印度尼西亚 | 3个 | 0 | 28ms | 0  
新加坡 | 15个 | 0 | 33ms | 0  
台湾 | 3个 | 0 | 72ms | 0  
马来西亚 | 9个 | 0 | 80ms | 1.0%  
韩国 | 21个 | 0 | 86ms | 0  
香港 | 66个 | 0 | 90ms | 0  
日本 | 3个 | 0 | 101ms | 0  
巴西 | 3个 | 0 | 155ms | 0  
美国 | 48个 | 0 | 164ms | 0  
法国 | 3个 | 0 | 168ms | 0  
均值 | 216个 | 0 | 179ms | 3.0%  
澳大利亚 | 3个 | 0 | 180ms | 0  
荷兰 | 3个 | 0 | 183ms | 0  
加拿大 | 12个 | 0 | 246ms | 0  
意大利 | 3个 | 0 | 250ms | -  
德国 | 6个 | 0 | 254ms | 0  
英国 | 3个 | 0 | 272ms | 0  
南非 | 6个 | 0 | 282ms | 0.5%  
俄罗斯 | 3个 | 0 | 284ms | -  
菲律宾 | 3个 | 0 | 477ms | 49.0%  
  
**简评：** 如果你考虑在Vultr的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有216个，其中超时点0个，平均响应时间为179毫秒，丢包率为3%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的4个，在100-200毫秒间的6个，在200-300毫秒间的6个，超过300毫秒的1个；  
丢包率较高的国家/地区：菲律宾；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180804 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180804 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180804-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180804")
    * [亚特兰大](/vultr/idc/atlanta/20180804-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180804")
    * [芝加哥](/vultr/idc/chicago/20180804-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180804")
    * [达拉斯](/vultr/idc/dallas/20180804-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180804")
    * [法兰克福](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")
    * [伦敦](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")
    * [洛杉矶](/vultr/idc/losangeles/20180804-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180804")
    * [迈阿密](/vultr/idc/miami/20180804-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180804")
    * [新泽西](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr新加坡机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [20180527](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")
    * [20180622](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [20180918](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180804-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [Linode](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")



本文最初发表于[多地到Vultr新加坡[Singapore]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-singapore.html)
