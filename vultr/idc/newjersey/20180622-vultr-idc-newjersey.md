#  多地到Vultr新泽西[NewJersey]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr新泽西\[NewJersey\]机房的Ping测试（20180622）](/images/thumbnails/to_vultr_NewJersey.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-新泽西机房](https://vps123.top/vultr-facilities.html#newjersey)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-新泽西机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180622-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的892个有效测试样本中，共有超时点26个；响应均值为298毫秒，最快的三地区为海南、河北、山东，最慢的三地区为新疆、云南、香港；云南、江苏、广东、河南、贵州等11处有响应超时情况；北京、贵州、河南丢包率较高。海外15个国家地区的46个有效测试样本中，无超时点；响应均值为167毫秒，最快的三地区为加拿大、美国、巴西，最慢的三地区为澳大利亚、越南、印度尼西亚。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于新泽西\[NewJersey\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-newjersey_20180622_mainland.png)

**大陆各省份到Vultr美国-新泽西机房的测速数据 [20180622]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
海南 | 11个 | 0 | 272ms | 0.6%  
河北 | 31个 | 0 | 279ms | 1.0%  
山东 | 37个 | 0 | 281ms | 2.3%  
福建 | 32个 | 0 | 283ms | 3.6%  
山西 | 35个 | 0 | 284ms | 1.7%  
贵州 | 23个 | 1个 | 285ms | 5.5%  
湖南 | 36个 | 0 | 285ms | 2.6%  
上海 | 8个 | 1个 | 285ms | 2.1%  
河南 | 53个 | 2个 | 289ms | 5.5%  
湖北 | 34个 | 0 | 292ms | 2.9%  
江苏 | 67个 | 4个 | 293ms | 3.3%  
广东 | 74个 | 3个 | 294ms | 2.2%  
广西 | 42个 | 0 | 296ms | 4.0%  
陕西 | 30个 | 1个 | 297ms | 2.9%  
安徽 | 35个 | 1个 | 298ms | 3.9%  
均值 | 892个 | 26个 | 298ms | 2.9%  
内蒙古 | 33个 | 0 | 301ms | 2.9%  
江西 | 24个 | 0 | 302ms | 2.5%  
北京 | 10个 | 0 | 303ms | 6.2%  
浙江 | 49个 | 1个 | 304ms | 3.1%  
辽宁 | 35个 | 0 | 304ms | 3.1%  
黑龙江 | 30个 | 0 | 309ms | 2.5%  
宁夏 | 13个 | 0 | 314ms | 0.9%  
重庆 | 13个 | 0 | 314ms | 0.6%  
四川 | 40个 | 1个 | 317ms | 2.4%  
吉林 | 19个 | 0 | 317ms | 1.4%  
青海 | 5个 | 0 | 318ms | 1.2%  
天津 | 3个 | 0 | 329ms | 1.8%  
甘肃 | 17个 | 1个 | 332ms | 2.0%  
新疆 | 20个 | 0 | 336ms | 1.8%  
云南 | 22个 | 10个 | 339ms | 0.9%  
香港 | 11个 | 0 | - | -  
  
**简评：** 如果你考虑在Vultr的新泽西[NewJersey]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新泽西[NewJersey]的机房的连通状况。到此机房的ping监测点共有892个，其中超时点26个，平均响应时间为298毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的15个，超过300毫秒的15个；  
超时点较多的省份：上海、云南；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于新泽西\[NewJersey\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-newjersey_20180622_overseas.png)

**海外线路到Vultr美国-新泽西机房的测速数据 [20180622]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 1个 | 0 | 53ms | 0  
美国 | 10个 | 0 | 72ms | 0  
巴西 | 1个 | 0 | 78ms | 0  
法国 | 1个 | 0 | 82ms | 0  
新加坡 | 2个 | 0 | 158ms | 0  
南非 | 2个 | 0 | 163ms | 0.5%  
香港 | 11个 | 0 | 166ms | 0  
均值 | 46个 | 0 | 167ms | 0.1%  
英国 | 2个 | 0 | 168ms | 0.5%  
日本 | 1个 | 0 | 187ms | 0  
台湾 | 1个 | 0 | 213ms | 0  
韩国 | 8个 | 0 | 214ms | 0  
菲律宾 | 2个 | 0 | 227ms | 0  
澳大利亚 | 1个 | 0 | 229ms | 0  
越南 | 2个 | 0 | 230ms | 0  
印度尼西亚 | 1个 | 0 | 264ms | 0  
  
**简评：** 如果你考虑在Vultr的新泽西[NewJersey]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新泽西[NewJersey]的机房的连通状况。到此机房的ping监测点共有46个，其中超时点0个，平均响应时间为167毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50-100毫秒间的4个，在100-200毫秒间的5个，在200-300毫秒间的6个；

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
    * [芝加哥](/vultr/idc/chicago/20180622-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180622")
    * [达拉斯](/vultr/idc/dallas/20180622-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180622")
    * [法兰克福](/vultr/idc/frankfurt/20180622-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180622")
    * [伦敦](/vultr/idc/london/20180622-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180622")
    * [洛杉矶](/vultr/idc/losangeles/20180622-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180622")
    * [迈阿密](/vultr/idc/miami/20180622-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180622")
    * [巴黎](/vultr/idc/paris/20180622-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180622")
    * [西雅图](/vultr/idc/seattle/20180622-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180622")
    * [硅谷](/vultr/idc/siliconvalley/20180622-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180622")
    * [新加坡](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [悉尼](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [东京](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
  * 到Vultr新泽西机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/newjersey/20180514-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180514")
    * [20180527](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [20180804](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [20180918](/vultr/idc/newjersey/20180918-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180918")



本文最初发表于[多地到Vultr新泽西[NewJersey]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-vultr-idc-newjersey.html)
