#  多地到Vultr新泽西[NewJersey]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr新泽西\[NewJersey\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_NewJersey.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-新泽西机房](https://vps123.top/vultr-facilities.html#newjersey)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-新泽西机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5208个有效测试样本中，共有超时点44个；响应均值为324毫秒，最快的三地区为上海、湖北、湖南，最慢的三地区为甘肃、西藏、青海；浙江、江苏、广东、贵州、上海等8处有响应超时情况；西藏、天津、贵州、吉林、安徽等10处丢包率较高。海外19个国家地区的237个有效测试样本中，共有超时点3个；响应均值为169毫秒，最快的三地区为加拿大、荷兰、巴西，最慢的三地区为马来西亚、印度尼西亚、菲律宾；香港有响应超时情况；菲律宾丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于新泽西\[NewJersey\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-newjersey_20180804_mainland.png)

**大陆各省份到Vultr美国-新泽西机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 27个 | 4个 | 261ms | 0.2%  
湖北 | 193个 | 0 | 302ms | 2.3%  
湖南 | 246个 | 0 | 302ms | 3.9%  
浙江 | 220个 | 10个 | 305ms | 4.1%  
河北 | 244个 | 0 | 305ms | 3.8%  
黑龙江 | 184个 | 0 | 306ms | 4.0%  
海南 | 48个 | 0 | 307ms | 4.2%  
天津 | 16个 | 0 | 308ms | 13.3%  
山东 | 358个 | 0 | 310ms | 3.7%  
广东 | 437个 | 6个 | 310ms | 2.6%  
山西 | 193个 | 3个 | 311ms | 3.0%  
贵州 | 146个 | 6个 | 318ms | 8.2%  
北京 | 28个 | 0 | 320ms | 3.7%  
安徽 | 215个 | 0 | 324ms | 7.3%  
均值 | 5208个 | 44个 | 324ms | 4.5%  
河南 | 367个 | 0 | 326ms | 5.5%  
广西 | 240个 | 0 | 326ms | 4.0%  
陕西 | 150个 | 0 | 327ms | 3.8%  
江苏 | 331个 | 9个 | 328ms | 6.9%  
重庆 | 41个 | 3个 | 330ms | 7.3%  
内蒙古 | 208个 | 0 | 330ms | 6.7%  
云南 | 123个 | 0 | 332ms | 4.0%  
福建 | 160个 | 0 | 338ms | 6.4%  
江西 | 131个 | 0 | 338ms | 2.7%  
吉林 | 100个 | 0 | 340ms | 8.1%  
辽宁 | 226个 | 3个 | 344ms | 3.3%  
四川 | 277个 | 0 | 349ms | 3.5%  
宁夏 | 32个 | 0 | 360ms | 2.2%  
新疆 | 131个 | 0 | 373ms | 4.2%  
甘肃 | 112个 | 0 | 380ms | 2.6%  
西藏 | 8个 | 0 | 390ms | 30.8%  
青海 | 16个 | 0 | 404ms | 3.0%  
  
**简评：** 如果你考虑在Vultr的新泽西[NewJersey]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新泽西[NewJersey]的机房的连通状况。到此机房的ping监测点共有5208个，其中超时点44个，平均响应时间为324毫秒，丢包率为4%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的1个，超过300毫秒的30个；  
超时点较多的省份：上海；  
丢包率较高的省份：天津、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于新泽西\[NewJersey\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-newjersey_20180804_overseas.png)

**海外线路到Vultr美国-新泽西机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 15个 | 0 | 19ms | 0  
荷兰 | 3个 | 0 | 67ms | 0  
巴西 | 3个 | 0 | 72ms | 0  
意大利 | 3个 | 0 | 72ms | -  
美国 | 48个 | 0 | 94ms | 1.8%  
德国 | 9个 | 0 | 96ms | 0  
英国 | 6个 | 0 | 112ms | 1.0%  
俄罗斯 | 3个 | 0 | 117ms | -  
均值 | 237个 | 3个 | 169ms | 2.4%  
南非 | 6个 | 0 | 173ms | 0  
日本 | 6个 | 0 | 190ms | 1.0%  
香港 | 63个 | 3个 | 192ms | 0  
新加坡 | 15个 | 0 | 211ms | 0  
韩国 | 21个 | 0 | 213ms | 0  
台湾 | 3个 | 0 | 216ms | 0  
法国 | 3个 | 0 | 222ms | 0  
澳大利亚 | 6个 | 0 | 233ms | 0  
马来西亚 | 12个 | 0 | 265ms | 0.8%  
印度尼西亚 | 6个 | 0 | 270ms | 0  
菲律宾 | 6个 | 0 | 390ms | 36.5%  
  
**简评：** 如果你考虑在Vultr的新泽西[NewJersey]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新泽西[NewJersey]的机房的连通状况。到此机房的ping监测点共有237个，其中超时点3个，平均响应时间为169毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的5个，在100-200毫秒间的5个，在200-300毫秒间的7个，超过300毫秒的1个；  
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
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr新泽西机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/newjersey/20180514-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180514")
    * [20180527](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [20180622](/vultr/idc/newjersey/20180622-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180622")
    * [20180918](/vultr/idc/newjersey/20180918-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180918")



本文最初发表于[多地到Vultr新泽西[NewJersey]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-newjersey.html)
