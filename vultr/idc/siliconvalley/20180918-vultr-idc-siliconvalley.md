#  多地到Vultr硅谷[SiliconValley]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr硅谷\[SiliconValley\]机房的Ping测试（20180918）](/images/thumbnails/to_vultr_Atlanta.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-硅谷机房](https://vps123.top/vultr-facilities.html#siliconvalley)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-硅谷机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180918-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Vultr美国-硅谷机房的PING测试结果，连通概况如下：大陆31个省市的1426个有效测试样本中，共有超时点10个；响应均值为212毫秒，最快的三地区为北京、重庆、海南，最慢的三地区为青海、新疆、西藏；江苏、浙江、广东、山西有响应超时情况；西藏、青海、湖北丢包率较高。海外17个国家地区的81个有效测试样本中，无超时点；响应均值为174毫秒，最快的三地区为美国、加拿大、台湾，最慢的三地区为荷兰、印度尼西亚、赞比亚；赞比亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于硅谷\[SiliconValley\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_usa-siliconvalley_20180918_mainland.png)

**大陆各省份到Vultr美国-硅谷机房的测速数据 [20180918]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
北京 | 9个 | 0 | 190ms | 0.2%  
重庆 | 9个 | 0 | 193ms | 1.4%  
海南 | 14个 | 0 | 193ms | 1.2%  
江苏 | 93个 | 4个 | 197ms | 2.0%  
安徽 | 70个 | 0 | 197ms | 2.6%  
浙江 | 66个 | 2个 | 198ms | 2.2%  
山东 | 93个 | 0 | 200ms | 2.9%  
广东 | 123个 | 2个 | 201ms | 2.1%  
山西 | 58个 | 2个 | 203ms | 1.1%  
广西 | 63个 | 0 | 205ms | 2.9%  
吉林 | 20个 | 0 | 206ms | 1.0%  
上海 | 8个 | 0 | 206ms | 0  
福建 | 40个 | 0 | 207ms | 2.4%  
辽宁 | 60个 | 0 | 207ms | 2.3%  
河北 | 62个 | 0 | 208ms | 4.4%  
宁夏 | 7个 | 0 | 209ms | 2.9%  
湖南 | 71个 | 0 | 210ms | 2.3%  
湖北 | 53个 | 0 | 212ms | 6.2%  
均值 | 1426个 | 10个 | 212ms | 2.5%  
江西 | 39个 | 0 | 213ms | 2.1%  
天津 | 7个 | 0 | 217ms | 3.0%  
内蒙古 | 57个 | 0 | 218ms | 2.7%  
黑龙江 | 55个 | 0 | 219ms | 2.3%  
贵州 | 42个 | 0 | 221ms | 2.5%  
陕西 | 42个 | 0 | 223ms | 0.9%  
云南 | 34个 | 0 | 228ms | 2.5%  
河南 | 88个 | 0 | 234ms | 1.1%  
四川 | 71个 | 0 | 234ms | 4.0%  
甘肃 | 33个 | 0 | 237ms | 2.1%  
青海 | 5个 | 0 | 253ms | 6.7%  
新疆 | 33个 | 0 | 261ms | 4.1%  
西藏 | 1个 | 0 | 399ms | 7.0%  
  
**简评：** 如果你考虑在Vultr的硅谷[SiliconValley]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于硅谷[SiliconValley]的机房的连通状况。到此机房的ping监测点共有1426个，其中超时点10个，平均响应时间为212毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的7个，在200-300毫秒间的23个，超过300毫秒的1个；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于硅谷\[SiliconValley\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_usa-siliconvalley_20180918_overseas.png)

**海外线路到Vultr美国-硅谷机房的测速数据 [20180918]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
美国 | 16个 | 0 | 31ms | 0  
加拿大 | 3个 | 0 | 71ms | 0  
台湾 | 2个 | 0 | 87ms | 0  
韩国 | 12个 | 0 | 126ms | 0  
日本 | 3个 | 0 | 139ms | 0  
新加坡 | 5个 | 0 | 146ms | 0  
意大利 | 1个 | 0 | 149ms | -  
香港 | 21个 | 0 | 157ms | 0  
澳大利亚 | 2个 | 0 | 167ms | 1.7%  
德国 | 3个 | 0 | 168ms | 0  
均值 | 81个 | 0 | 174ms | 0.9%  
菲律宾 | 1个 | 0 | 189ms | 0  
俄罗斯 | 1个 | 0 | 197ms | -  
越南 | 2个 | 0 | 209ms | 0  
马来西亚 | 6个 | 0 | 215ms | 0  
荷兰 | 1个 | 0 | 234ms | 0  
印度尼西亚 | 1个 | 0 | 328ms | 3.3%  
赞比亚 | 1个 | 0 | 345ms | 9.0%  
  
**简评：** 如果你考虑在Vultr的硅谷[SiliconValley]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于硅谷[SiliconValley]的机房的连通状况。到此机房的ping监测点共有81个，其中超时点0个，平均响应时间为174毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的2个，在100-200毫秒间的9个，在200-300毫秒间的3个，超过300毫秒的2个；

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
    * [新加坡](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")
    * [悉尼](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")
    * [东京](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 到Vultr硅谷机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [20180527](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [20180622](/vultr/idc/siliconvalley/20180622-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180622")
    * [20180804](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")



本文最初发表于[多地到Vultr硅谷[SiliconValley]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-vultr-idc-siliconvalley.html)
