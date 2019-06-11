#  多地到Vultr悉尼[Sydney]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr悉尼\[Sydney\]机房的Ping测试（20180622）](/images/thumbnails/to_vultr_Sydney.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[澳大利亚-悉尼机房](https://vps123.top/vultr-facilities.html#sydney)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的澳大利亚-悉尼机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180622-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的888个有效测试样本中，共有超时点33个；响应均值为304毫秒，最快的三地区为湖南、河南、广东，最慢的三地区为青海、云南、香港；云南、江苏、浙江、香港、河南等15处有响应超时情况；北京、上海、重庆、天津、陕西等26处丢包率较高。海外18个国家地区的83个有效测试样本中，共有超时点2个；响应均值为210毫秒，最快的三地区为澳大利亚、日本、新加坡，最慢的三地区为法国、意大利、南非；香港有响应超时情况。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_australia-sydney_20180622_mainland.png)

**大陆各省份到Vultr澳大利亚-悉尼机房的测速数据 [20180622]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
湖南 | 34个 | 0 | 259ms | 2.6%  
河南 | 44个 | 1个 | 276ms | 8.4%  
广东 | 76个 | 1个 | 280ms | 6.6%  
贵州 | 24个 | 1个 | 281ms | 5.9%  
山东 | 37个 | 0 | 281ms | 8.7%  
北京 | 11个 | 0 | 282ms | 14.9%  
广西 | 41个 | 0 | 284ms | 6.3%  
山西 | 33个 | 0 | 284ms | 5.3%  
福建 | 29个 | 1个 | 285ms | 7.0%  
陕西 | 24个 | 1个 | 285ms | 11.5%  
河北 | 30个 | 0 | 290ms | 5.9%  
天津 | 3个 | 0 | 291ms | 13.1%  
海南 | 12个 | 0 | 296ms | 4.5%  
安徽 | 34个 | 1个 | 303ms | 5.9%  
均值 | 888个 | 33个 | 304ms | 7.5%  
江西 | 25个 | 0 | 306ms | 7.0%  
江苏 | 68个 | 5个 | 307ms | 9.2%  
湖北 | 33个 | 1个 | 311ms | 6.3%  
浙江 | 54个 | 5个 | 312ms | 11.4%  
黑龙江 | 32个 | 0 | 312ms | 8.8%  
辽宁 | 36个 | 0 | 315ms | 7.6%  
宁夏 | 13个 | 0 | 320ms | 7.7%  
重庆 | 12个 | 1个 | 320ms | 13.2%  
上海 | 7个 | 1个 | 326ms | 14.9%  
内蒙古 | 28个 | 0 | 330ms | 9.0%  
吉林 | 19个 | 0 | 351ms | 8.3%  
甘肃 | 14个 | 0 | 352ms | 8.6%  
四川 | 40个 | 1个 | 353ms | 4.3%  
新疆 | 24个 | 1个 | 360ms | 6.7%  
青海 | 5个 | 0 | 363ms | 10.0%  
云南 | 22个 | 10个 | 376ms | 3.2%  
香港 | 24个 | 2个 | - | -  
  
**简评：** 如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有888个，其中超时点33个，平均响应时间为304毫秒，丢包率为7%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的13个，超过300毫秒的17个；  
超时点较多的省份：上海、云南；  
丢包率较高的省份：北京、陕西、天津、浙江、重庆、上海、青海；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_australia-sydney_20180622_overseas.png)

**海外线路到Vultr澳大利亚-悉尼机房的测速数据 [20180622]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
澳大利亚 | 1个 | 0 | 11ms | 0  
日本 | 2个 | 0 | 121ms | 3.0%  
新加坡 | 5个 | 0 | 151ms | 0  
英国 | 2个 | 0 | 157ms | 0  
台湾 | 2个 | 0 | 162ms | 0  
香港 | 24个 | 2个 | 167ms | 0  
美国 | 18个 | 0 | 174ms | 0  
韩国 | 14个 | 0 | 184ms | 0  
马来西亚 | 2个 | 0 | 195ms | 1.0%  
印度尼西亚 | 1个 | 0 | 200ms | 1.0%  
均值 | 83个 | 2个 | 210ms | 0.6%  
加拿大 | 2个 | 0 | 232ms | 0  
越南 | 2个 | 0 | 248ms | 0  
菲律宾 | 2个 | 0 | 252ms | 0  
巴西 | 1个 | 0 | 294ms | 0  
德国 | 1个 | 0 | 299ms | -  
法国 | 1个 | 0 | 301ms | 0  
意大利 | 1个 | 0 | 304ms | -  
南非 | 2个 | 0 | 330ms | 5.0%  
  
**简评：** 如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有83个，其中超时点2个，平均响应时间为210毫秒，丢包率为0%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的9个，在200-300毫秒间的5个，超过300毫秒的3个；

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
    * [新泽西](/vultr/idc/newjersey/20180622-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180622")
    * [巴黎](/vultr/idc/paris/20180622-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180622")
    * [西雅图](/vultr/idc/seattle/20180622-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180622")
    * [硅谷](/vultr/idc/siliconvalley/20180622-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180622")
    * [新加坡](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [东京](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
  * 到Vultr悉尼机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [20180527](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [20180804](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [20180918](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")



本文最初发表于[多地到Vultr悉尼[Sydney]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-vultr-idc-sydney.html)
