#  多地到Vultr法兰克福[Frankfurt]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr法兰克福\[Frankfurt\]机房的Ping测试（20180527）](/images/thumbnails/to_vultr_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[德国-法兰克福机房](https://vps123.top/vultr-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180527-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的962个有效测试样本中，共有超时点34个；响应均值为280毫秒，最快的三地区为北京、青海、天津，最慢的三地区为新疆、黑龙江、吉林；江苏、广东、湖北、浙江、江西等15处有响应超时情况；河北、辽宁、湖南、新疆、贵州丢包率较高。海外21个国家地区的85个有效测试样本中，无超时点；响应均值为185毫秒，最快的三地区为法国、荷兰、德国，最慢的三地区为印度尼西亚、澳大利亚、柬埔寨。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_germany-frankfurt_20180527_mainland.png)

**大陆各省份到Vultr德国-法兰克福机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
北京 | 8个 | 1个 | 245ms | 0  
青海 | 4个 | 0 | 246ms | 2.3%  
天津 | 5个 | 0 | 250ms | 0.2%  
河北 | 35个 | 0 | 256ms | 14.2%  
海南 | 14个 | 0 | 257ms | 1.6%  
上海 | 7个 | 0 | 262ms | 0  
广西 | 40个 | 1个 | 264ms | 2.9%  
内蒙古 | 33个 | 0 | 265ms | 1.9%  
广东 | 81个 | 5个 | 266ms | 1.7%  
重庆 | 15个 | 1个 | 267ms | 4.1%  
安徽 | 38个 | 1个 | 268ms | 1.5%  
辽宁 | 40个 | 1个 | 268ms | 12.3%  
湖北 | 45个 | 3个 | 270ms | 2.6%  
云南 | 19个 | 0 | 272ms | 0.9%  
宁夏 | 13个 | 0 | 273ms | 2.1%  
山西 | 38个 | 0 | 273ms | 1.9%  
江西 | 23个 | 2个 | 279ms | 2.9%  
均值 | 962个 | 34个 | 280ms | 3.5%  
福建 | 32个 | 1个 | 281ms | 2.1%  
甘肃 | 22个 | 0 | 282ms | 1.6%  
四川 | 45个 | 2个 | 283ms | 2.3%  
湖南 | 45个 | 1个 | 283ms | 5.7%  
浙江 | 49个 | 3个 | 284ms | 2.0%  
江苏 | 62个 | 9个 | 288ms | 1.6%  
河南 | 57个 | 2个 | 290ms | 4.4%  
贵州 | 25个 | 0 | 291ms | 5.4%  
陕西 | 31个 | 0 | 291ms | 2.0%  
山东 | 52个 | 1个 | 302ms | 2.2%  
新疆 | 27个 | 0 | 312ms | 5.5%  
黑龙江 | 39个 | 0 | 315ms | 3.6%  
吉林 | 18个 | 0 | 326ms | 1.9%  
  
**简评：** 如果你考虑在Vultr的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有962个，其中超时点34个，平均响应时间为280毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的26个，超过300毫秒的4个；  
超时点较多的省份：北京、江苏；  
丢包率较高的省份：河北、辽宁；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_germany-frankfurt_20180527_overseas.png)

**海外线路到Vultr德国-法兰克福机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
法国 | 1个 | 0 | 9ms | 0  
荷兰 | 1个 | 0 | 13ms | 0  
德国 | 3个 | 0 | 14ms | 0  
意大利 | 1个 | 0 | 14ms | -  
英国 | 1个 | 0 | 51ms | 0  
俄罗斯 | 1个 | 0 | 83ms | 0  
加拿大 | 4个 | 0 | 107ms | 0  
美国 | 21个 | 0 | 156ms | 3.0%  
新加坡 | 5个 | 0 | 176ms | 0  
均值 | 85个 | 0 | 185ms | 0.6%  
南非 | 2个 | 0 | 193ms | 2.0%  
巴西 | 1个 | 0 | 210ms | 0  
马来西亚 | 5个 | 0 | 217ms | 0.2%  
香港 | 18个 | 0 | 220ms | 0  
菲律宾 | 1个 | 0 | 248ms | 0  
日本 | 2个 | 0 | 262ms | 1.5%  
越南 | 2个 | 0 | 267ms | 0  
韩国 | 12个 | 0 | 299ms | 0  
台湾 | 1个 | 0 | 300ms | -  
印度尼西亚 | 1个 | 0 | 316ms | 0  
澳大利亚 | 1个 | 0 | 350ms | 0  
柬埔寨 | 1个 | 0 | 392ms | 4.0%  
  
**简评：** 如果你考虑在Vultr的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有85个，其中超时点0个，平均响应时间为185毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的2个，在100-200毫秒间的4个，在200-300毫秒间的8个，超过300毫秒的3个；

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
    * [芝加哥](/vultr/idc/chicago/20180527-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180527")
    * [达拉斯](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")
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
  * 到Vultr法兰克福机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/frankfurt/20180514-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180514")
    * [20180622](/vultr/idc/frankfurt/20180622-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180622")
    * [20180804](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")
    * [20180918](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180527-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [Linode](/linode/idc/frankfurt/20180527-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180527")



本文最初发表于[多地到Vultr法兰克福[Frankfurt]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-vultr-idc-frankfurt.html)
