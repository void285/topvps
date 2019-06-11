#  多地到Vultr阿姆斯特丹[Amsterdam]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr阿姆斯特丹\[Amsterdam\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Amsterdam.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[荷兰-阿姆斯特丹机房](https://vps123.top/vultr-facilities.html#amsterdam)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的荷兰-阿姆斯特丹机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr荷兰-阿姆斯特丹机房的PING测试结果，连通概况如下：大陆31个省市的913个有效测试样本中，共有超时点11个；响应均值为289毫秒，最快的三地区为上海、青海、安徽，最慢的三地区为黑龙江、吉林、西藏；浙江、山东、安徽、北京、广东等8处有响应超时情况；江苏、浙江、贵州、上海、山西等7处丢包率较高。海外18个国家地区的79个有效测试样本中，共有超时点1个；响应均值为199毫秒，最快的三地区为法国、德国、英国，最慢的三地区为澳大利亚、台湾、柬埔寨；香港有响应超时情况；柬埔寨丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_netherlands-amsterdam_20180514_mainland.png)

**大陆各省份到Vultr荷兰-阿姆斯特丹机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 9个 | 0 | 234ms | 7.9%  
青海 | 4个 | 0 | 256ms | 0.8%  
安徽 | 37个 | 1个 | 259ms | 2.1%  
天津 | 5个 | 0 | 260ms | 4.2%  
甘肃 | 20个 | 0 | 261ms | 0.9%  
重庆 | 16个 | 0 | 269ms | 0.2%  
北京 | 8个 | 1个 | 270ms | 0  
宁夏 | 12个 | 0 | 270ms | 1.5%  
内蒙古 | 34个 | 0 | 272ms | 2.1%  
广东 | 75个 | 1个 | 273ms | 3.1%  
广西 | 33个 | 0 | 274ms | 2.1%  
海南 | 11个 | 0 | 274ms | 3.1%  
云南 | 21个 | 0 | 280ms | 1.8%  
湖北 | 45个 | 1个 | 281ms | 3.4%  
辽宁 | 34个 | 0 | 281ms | 5.8%  
江西 | 21个 | 0 | 283ms | 3.1%  
河北 | 30个 | 0 | 284ms | 3.1%  
湖南 | 42个 | 0 | 285ms | 2.8%  
均值 | 913个 | 11个 | 289ms | 4.0%  
陕西 | 33个 | 0 | 291ms | 2.8%  
福建 | 35个 | 1个 | 297ms | 2.7%  
浙江 | 48个 | 3个 | 299ms | 8.7%  
山西 | 37个 | 0 | 299ms | 7.7%  
四川 | 46个 | 0 | 300ms | 3.0%  
江苏 | 53个 | 1个 | 300ms | 9.5%  
河南 | 50个 | 0 | 302ms | 3.7%  
贵州 | 24个 | 0 | 308ms | 8.6%  
新疆 | 28个 | 0 | 312ms | 2.5%  
山东 | 49个 | 2个 | 315ms | 4.2%  
黑龙江 | 36个 | 0 | 321ms | 5.5%  
吉林 | 16个 | 0 | 323ms | 2.1%  
西藏 | 1个 | 0 | 368ms | 0  
  
**简评：** 如果你考虑在Vultr的阿姆斯特丹[Amsterdam]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有913个，其中超时点11个，平均响应时间为289毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的24个，超过300毫秒的7个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_netherlands-amsterdam_20180514_overseas.png)

**海外线路到Vultr荷兰-阿姆斯特丹机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
法国 | 2个 | 0 | 9ms | 0  
德国 | 2个 | 0 | 21ms | 0  
英国 | 2个 | 0 | 22ms | 0  
加拿大 | 3个 | 0 | 96ms | 0  
俄罗斯 | 1个 | 0 | 98ms | 0  
美国 | 19个 | 0 | 142ms | 0  
新加坡 | 6个 | 0 | 187ms | 0  
印度尼西亚 | 1个 | 0 | 194ms | 5.0%  
均值 | 79个 | 1个 | 199ms | 1.6%  
巴西 | 1个 | 0 | 205ms | 0  
南非 | 1个 | 0 | 215ms | 0  
菲律宾 | 1个 | 0 | 229ms | 0  
日本 | 2个 | 0 | 266ms | 0  
韩国 | 13个 | 0 | 281ms | 0  
马来西亚 | 3个 | 0 | 284ms | 0.7%  
香港 | 18个 | 1个 | 289ms | 0  
澳大利亚 | 2个 | 0 | 298ms | 0  
台湾 | 1个 | 0 | 311ms | -  
柬埔寨 | 1个 | 0 | 442ms | 22.0%  
  
**简评：** 如果你考虑在Vultr的阿姆斯特丹[Amsterdam]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有79个，其中超时点1个，平均响应时间为199毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的2个，在100-200毫秒间的3个，在200-300毫秒间的8个，超过300毫秒的2个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180514 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180514 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
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
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr阿姆斯特丹机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/amsterdam/20180527-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180527")
    * [20180622](/vultr/idc/amsterdam/20180622-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180622")
    * [20180804](/vultr/idc/amsterdam/20180804-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180804")
    * [20180918](/vultr/idc/amsterdam/20180918-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180918")
  * 本期报告：在阿姆斯特丹部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/amsterdam/20180514-bwg-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180514")
    * [Digital Ocean](do/idc/amsterdam/20180514-do-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")



本文最初发表于[多地到Vultr阿姆斯特丹[Amsterdam]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-amsterdam.html)
