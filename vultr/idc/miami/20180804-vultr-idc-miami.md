#  多地到Vultr迈阿密[Miami]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr迈阿密\[Miami\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_Miami.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-迈阿密机房](https://vps123.top/vultr-facilities.html#miami)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-迈阿密机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的3245个有效测试样本中，共有超时点38个；响应均值为325毫秒，最快的三地区为天津、上海、山东，最慢的三地区为新疆、青海、西藏；浙江、江苏、湖南、上海有响应超时情况；西藏、宁夏、重庆、黑龙江、安徽等26处丢包率较高。海外19个国家地区的213个有效测试样本中，共有超时点3个；响应均值为187毫秒，最快的三地区为加拿大、荷兰、美国，最慢的三地区为印度尼西亚、马来西亚、菲律宾；香港有响应超时情况；菲律宾、美国丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于迈阿密\[Miami\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-miami_20180804_mainland.png)

**大陆各省份到Vultr美国-迈阿密机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 16个 | 0 | 261ms | 5.5%  
上海 | 27个 | 4个 | 271ms | 0.2%  
山东 | 210个 | 0 | 292ms | 7.1%  
湖北 | 125个 | 0 | 295ms | 6.2%  
北京 | 36个 | 0 | 303ms | 2.4%  
河北 | 132个 | 0 | 304ms | 7.7%  
广东 | 282个 | 0 | 308ms | 3.3%  
江苏 | 242个 | 12个 | 309ms | 6.6%  
湖南 | 141个 | 6个 | 309ms | 6.3%  
浙江 | 182个 | 16个 | 311ms | 6.9%  
黑龙江 | 112个 | 0 | 311ms | 12.8%  
山西 | 113个 | 0 | 311ms | 5.4%  
重庆 | 41个 | 0 | 321ms | 13.5%  
海南 | 28个 | 0 | 322ms | 3.9%  
均值 | 3245个 | 38个 | 325ms | 7.2%  
辽宁 | 154个 | 0 | 328ms | 5.6%  
贵州 | 94个 | 0 | 332ms | 7.9%  
内蒙古 | 112个 | 0 | 333ms | 6.6%  
广西 | 132个 | 0 | 334ms | 5.5%  
陕西 | 97个 | 0 | 336ms | 5.7%  
河南 | 207个 | 0 | 339ms | 10.4%  
云南 | 67个 | 0 | 339ms | 12.2%  
吉林 | 64个 | 0 | 339ms | 8.9%  
福建 | 96个 | 0 | 341ms | 6.5%  
安徽 | 128个 | 0 | 341ms | 12.5%  
江西 | 75个 | 0 | 345ms | 6.9%  
四川 | 165个 | 0 | 358ms | 4.6%  
甘肃 | 60个 | 0 | 373ms | 7.1%  
宁夏 | 16个 | 0 | 373ms | 19.5%  
新疆 | 79个 | 0 | 400ms | 5.1%  
青海 | 8个 | 0 | 418ms | 7.5%  
西藏 | 4个 | 0 | 481ms | 95.0%  
  
**简评：** 如果你考虑在Vultr的迈阿密[Miami]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于迈阿密[Miami]的机房的连通状况。到此机房的ping监测点共有3245个，其中超时点38个，平均响应时间为325毫秒，丢包率为7%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的4个，超过300毫秒的27个；  
超时点较多的省份：上海；  
丢包率较高的省份：黑龙江、重庆、河南、云南、安徽、宁夏、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于迈阿密\[Miami\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-miami_20180804_overseas.png)

**海外线路到Vultr美国-迈阿密机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 12个 | 0 | 44ms | 0  
荷兰 | 3个 | 0 | 65ms | 0  
美国 | 48个 | 0 | 97ms | 6.0%  
巴西 | 3个 | 0 | 100ms | 0  
意大利 | 3个 | 0 | 104ms | -  
德国 | 6个 | 0 | 121ms | 0  
英国 | 3个 | 0 | 137ms | 1.0%  
俄罗斯 | 3个 | 0 | 148ms | -  
日本 | 3个 | 0 | 180ms | 0  
均值 | 213个 | 3个 | 187ms | 4.6%  
南非 | 6个 | 0 | 192ms | 0  
新加坡 | 15个 | 0 | 212ms | 0  
法国 | 3个 | 0 | 213ms | 0  
香港 | 63个 | 3个 | 213ms | 0  
台湾 | 3个 | 0 | 231ms | 0  
韩国 | 21个 | 0 | 233ms | 0  
澳大利亚 | 3个 | 0 | 234ms | 0  
印度尼西亚 | 3个 | 0 | 271ms | 0  
马来西亚 | 9个 | 0 | 306ms | 0.7%  
菲律宾 | 3个 | 0 | 449ms | 71.0%  
  
**简评：** 如果你考虑在Vultr的迈阿密[Miami]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于迈阿密[Miami]的机房的连通状况。到此机房的ping监测点共有213个，其中超时点3个，平均响应时间为187毫秒，丢包率为4%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的3个，在100-200毫秒间的6个，在200-300毫秒间的7个，超过300毫秒的2个；  
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
    * [新泽西](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr迈阿密机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/miami/20180514-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180514")
    * [20180527](/vultr/idc/miami/20180527-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180527")
    * [20180622](/vultr/idc/miami/20180622-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180622")
    * [20180918](/vultr/idc/miami/20180918-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180918")



本文最初发表于[多地到Vultr迈阿密[Miami]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-miami.html)
