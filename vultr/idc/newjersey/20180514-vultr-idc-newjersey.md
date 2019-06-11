#  多地到Vultr新泽西[NewJersey]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr新泽西\[NewJersey\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_NewJersey.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-新泽西机房](https://vps123.top/vultr-facilities.html#newjersey)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-新泽西机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr美国-新泽西机房的PING测试结果，连通概况如下：大陆31个省市的978个有效测试样本中，共有超时点12个；响应均值为314毫秒，最快的三地区为上海、北京、江西，最慢的三地区为河北、新疆、西藏；浙江、江苏、广东、北京、安徽等7处有响应超时情况；湖北、江苏、江西、湖南、河北等11处丢包率较高。海外18个国家地区的78个有效测试样本中，无超时点；响应均值为196毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为南非、印度尼西亚、柬埔寨；柬埔寨、印度尼西亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于新泽西\[NewJersey\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-newjersey_20180514_mainland.png)

**大陆各省份到Vultr美国-新泽西机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 8个 | 0 | 264ms | 0.5%  
北京 | 8个 | 1个 | 266ms | 0.5%  
江西 | 23个 | 0 | 286ms | 13.2%  
浙江 | 51个 | 4个 | 289ms | 9.4%  
天津 | 5个 | 0 | 291ms | 7.7%  
江苏 | 62个 | 2个 | 292ms | 16.7%  
广东 | 78个 | 2个 | 297ms | 1.1%  
安徽 | 42个 | 1个 | 297ms | 9.6%  
宁夏 | 12个 | 0 | 298ms | 1.0%  
陕西 | 33个 | 0 | 302ms | 1.9%  
福建 | 35个 | 1个 | 304ms | 1.5%  
黑龙江 | 39个 | 0 | 307ms | 2.1%  
吉林 | 15个 | 0 | 309ms | 1.7%  
海南 | 12个 | 0 | 310ms | 4.5%  
山东 | 52个 | 1个 | 311ms | 2.4%  
湖南 | 43个 | 0 | 312ms | 10.3%  
贵州 | 28个 | 0 | 313ms | 6.8%  
广西 | 36个 | 0 | 313ms | 1.9%  
均值 | 978个 | 12个 | 314ms | 6.1%  
湖北 | 48个 | 0 | 315ms | 21.7%  
辽宁 | 40个 | 0 | 320ms | 2.6%  
内蒙古 | 36个 | 0 | 322ms | 3.9%  
云南 | 24个 | 0 | 327ms | 6.1%  
重庆 | 15个 | 0 | 327ms | 2.0%  
山西 | 38个 | 0 | 331ms | 3.3%  
河南 | 56个 | 0 | 333ms | 6.9%  
四川 | 49个 | 0 | 335ms | 4.2%  
青海 | 4个 | 0 | 337ms | 0.5%  
甘肃 | 22个 | 0 | 340ms | 1.8%  
河北 | 34个 | 0 | 348ms | 10.2%  
新疆 | 29个 | 0 | 351ms | 1.6%  
西藏 | 1个 | 0 | 474ms | 0  
  
**简评：** 如果你考虑在Vultr的新泽西[NewJersey]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新泽西[NewJersey]的机房的连通状况。到此机房的ping监测点共有978个，其中超时点12个，平均响应时间为314毫秒，丢包率为6%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的9个，超过300毫秒的22个；  
超时点较多的省份：北京；  
丢包率较高的省份：江西、江苏、湖南、湖北、河北；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于新泽西\[NewJersey\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-newjersey_20180514_overseas.png)

**海外线路到Vultr美国-新泽西机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 3个 | 0 | 17ms | 0  
美国 | 19个 | 0 | 60ms | 0  
法国 | 2个 | 0 | 77ms | 0  
英国 | 2个 | 0 | 85ms | 0  
德国 | 2个 | 0 | 98ms | 0  
巴西 | 1个 | 0 | 126ms | 0  
俄罗斯 | 1个 | 0 | 166ms | 0  
日本 | 2个 | 0 | 174ms | 1.0%  
台湾 | 1个 | 0 | 192ms | -  
均值 | 78个 | 0 | 196ms | 2.8%  
韩国 | 13个 | 0 | 204ms | 0  
澳大利亚 | 1个 | 0 | 227ms | 0  
菲律宾 | 1个 | 0 | 235ms | 2.0%  
新加坡 | 6个 | 0 | 256ms | 0  
香港 | 18个 | 0 | 260ms | 0  
马来西亚 | 3个 | 0 | 286ms | 0  
南非 | 1个 | 0 | 299ms | 0  
印度尼西亚 | 1个 | 0 | 332ms | 9.0%  
柬埔寨 | 1个 | 0 | 442ms | 35.0%  
  
**简评：** 如果你考虑在Vultr的新泽西[NewJersey]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新泽西[NewJersey]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点0个，平均响应时间为196毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的4个，在100-200毫秒间的4个，在200-300毫秒间的7个，超过300毫秒的2个；  
丢包率较高的国家/地区：柬埔寨；

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
    * [巴黎](/vultr/idc/paris/20180514-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180514")
    * [西雅图](/vultr/idc/seattle/20180514-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180514")
    * [硅谷](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr新泽西机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [20180622](/vultr/idc/newjersey/20180622-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180622")
    * [20180804](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [20180918](/vultr/idc/newjersey/20180918-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180918")



本文最初发表于[多地到Vultr新泽西[NewJersey]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-newjersey.html)
