#  多地到Vultr新加坡[Singapore]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr新加坡\[Singapore\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[新加坡-新加坡机房](https://vps123.top/vultr-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr新加坡-新加坡机房的PING测试结果，连通概况如下：大陆31个省市的972个有效测试样本中，共有超时点13个；响应均值为186毫秒，最快的三地区为福建、湖南、广西，最慢的三地区为新疆、山西、河北；江苏、浙江、福建、广西、广东等7处有响应超时情况；陕西、山西、河北、黑龙江、内蒙古等18处丢包率较高。海外18个国家地区的80个有效测试样本中，无超时点；响应均值为169毫秒，最快的三地区为新加坡、马来西亚、香港，最慢的三地区为澳大利亚、巴西、南非；印度尼西亚、南非、菲律宾、加拿大、马来西亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_singapore-singapore_20180514_mainland.png)

**大陆各省份到Vultr新加坡-新加坡机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
福建 | 35个 | 1个 | 144ms | 1.7%  
湖南 | 48个 | 0 | 144ms | 3.2%  
广西 | 36个 | 1个 | 146ms | 4.4%  
广东 | 83个 | 1个 | 148ms | 2.7%  
海南 | 12个 | 0 | 149ms | 3.6%  
安徽 | 39个 | 0 | 150ms | 6.9%  
云南 | 24个 | 0 | 151ms | 2.5%  
北京 | 8个 | 1个 | 155ms | 3.6%  
天津 | 5个 | 0 | 157ms | 8.9%  
上海 | 9个 | 0 | 157ms | 6.7%  
贵州 | 27个 | 0 | 159ms | 4.3%  
江西 | 22个 | 0 | 163ms | 8.8%  
甘肃 | 21个 | 0 | 169ms | 4.8%  
西藏 | 1个 | 0 | 170ms | 0  
江苏 | 63个 | 5个 | 171ms | 6.0%  
青海 | 3个 | 0 | 175ms | 3.7%  
宁夏 | 12个 | 0 | 179ms | 5.9%  
浙江 | 52个 | 3个 | 180ms | 5.0%  
河南 | 59个 | 0 | 185ms | 8.4%  
均值 | 972个 | 13个 | 186ms | 7.7%  
山东 | 50个 | 1个 | 191ms | 10.2%  
重庆 | 15个 | 0 | 191ms | 4.1%  
湖北 | 47个 | 0 | 196ms | 11.1%  
吉林 | 13个 | 0 | 200ms | 10.1%  
黑龙江 | 40个 | 0 | 206ms | 11.9%  
陕西 | 30个 | 0 | 211ms | 15.6%  
四川 | 49个 | 0 | 219ms | 9.9%  
辽宁 | 37个 | 0 | 228ms | 11.1%  
内蒙古 | 33个 | 0 | 231ms | 11.2%  
新疆 | 28个 | 0 | 239ms | 10.0%  
山西 | 38个 | 0 | 240ms | 12.8%  
河北 | 33个 | 0 | 262ms | 12.3%  
  
**简评：** 如果你考虑在Vultr的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有972个，其中超时点13个，平均响应时间为186毫秒，丢包率为7%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的23个，在200-300毫秒间的8个；  
超时点较多的省份：北京；  
丢包率较高的省份：山东、湖北、吉林、黑龙江、陕西、辽宁、内蒙古、新疆、山西、河北；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_singapore-singapore_20180514_overseas.png)

**海外线路到Vultr新加坡-新加坡机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
新加坡 | 6个 | 0 | 1ms | 2.7%  
马来西亚 | 3个 | 0 | 25ms | 5.3%  
香港 | 19个 | 0 | 47ms | 0  
菲律宾 | 1个 | 0 | 59ms | 8.0%  
台湾 | 1个 | 0 | 62ms | -  
日本 | 2个 | 0 | 87ms | 4.0%  
韩国 | 13个 | 0 | 93ms | 2.3%  
印度尼西亚 | 1个 | 0 | 126ms | 22.0%  
俄罗斯 | 1个 | 0 | 168ms | 0  
均值 | 80个 | 0 | 169ms | 4.7%  
美国 | 19个 | 0 | 198ms | 0  
柬埔寨 | 1个 | 0 | 222ms | 2.0%  
德国 | 2个 | 0 | 229ms | 3.5%  
英国 | 2个 | 0 | 235ms | 3.5%  
法国 | 2个 | 0 | 248ms | 4.0%  
加拿大 | 3个 | 0 | 249ms | 8.0%  
澳大利亚 | 2个 | 0 | 260ms | 4.0%  
巴西 | 1个 | 0 | 365ms | 0  
南非 | 1个 | 0 | 379ms | 11.0%  
  
**简评：** 如果你考虑在Vultr的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有80个，其中超时点0个，平均响应时间为169毫秒，丢包率为4%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的4个，在100-200毫秒间的3个，在200-300毫秒间的6个，超过300毫秒的2个；  
丢包率较高的国家/地区：印度尼西亚、南非；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180514 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180514 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180514-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180514")
    * [亚特兰大](/vultr/idc/atlanta/20180514-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180514")
    * [芝加哥](/vultr/idc/chicago/20180514-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180514")
    * [达拉斯](/vultr/idc/dallas/20180514-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180514")
    * [法兰克福](/vultr/idc/frankfurt/20180514-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180514")
    * [伦敦](/vultr/idc/london/20180514-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180514")
    * [洛杉矶](/vultr/idc/losangeles/20180514-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180514")
    * [迈阿密](/vultr/idc/miami/20180514-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180514")
    * [新泽西](/vultr/idc/newjersey/20180514-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180514")
    * [巴黎](/vultr/idc/paris/20180514-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180514")
    * [西雅图](/vultr/idc/seattle/20180514-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180514")
    * [硅谷](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr新加坡机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")
    * [20180622](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [20180804](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [20180918](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180514-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [Linode](/linode/idc/singapore/20180514-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180514")



本文最初发表于[多地到Vultr新加坡[Singapore]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-singapore.html)
