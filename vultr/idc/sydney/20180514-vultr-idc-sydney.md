#  多地到Vultr悉尼[Sydney]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr悉尼\[Sydney\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Sydney.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[澳大利亚-悉尼机房](https://vps123.top/vultr-facilities.html#sydney)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的澳大利亚-悉尼机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr澳大利亚-悉尼机房的PING测试结果，连通概况如下：大陆31个省市的948个有效测试样本中，共有超时点11个；响应均值为244毫秒，最快的三地区为天津、上海、福建，最慢的三地区为新疆、西藏、河北；浙江、广东、江苏、福建、北京等7处有响应超时情况；河北、上海、山东、河南、黑龙江等8处丢包率较高。海外17个国家地区的78个有效测试样本中，无超时点；响应均值为243毫秒，最快的三地区为澳大利亚、台湾、日本，最慢的三地区为俄罗斯、柬埔寨、南非；柬埔寨丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_australia-sydney_20180514_mainland.png)

**大陆各省份到Vultr澳大利亚-悉尼机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 4个 | 0 | 197ms | 3.8%  
上海 | 9个 | 0 | 209ms | 9.0%  
福建 | 36个 | 1个 | 212ms | 1.7%  
广东 | 74个 | 2个 | 217ms | 2.0%  
北京 | 8个 | 1个 | 221ms | 4.9%  
湖南 | 42个 | 0 | 225ms | 0.3%  
海南 | 12个 | 0 | 227ms | 0.1%  
江苏 | 62个 | 2个 | 229ms | 2.7%  
贵州 | 26个 | 0 | 232ms | 2.8%  
广西 | 38个 | 1个 | 232ms | 1.0%  
浙江 | 47个 | 3个 | 235ms | 2.9%  
辽宁 | 37个 | 0 | 236ms | 3.5%  
安徽 | 40个 | 0 | 237ms | 1.7%  
江西 | 21个 | 0 | 238ms | 5.5%  
陕西 | 32个 | 0 | 238ms | 3.0%  
山西 | 38个 | 0 | 241ms | 4.7%  
重庆 | 13个 | 0 | 243ms | 1.7%  
宁夏 | 12个 | 0 | 244ms | 0.1%  
内蒙古 | 32个 | 0 | 244ms | 3.8%  
均值 | 948个 | 11个 | 244ms | 3.8%  
吉林 | 17个 | 0 | 246ms | 5.5%  
云南 | 22个 | 0 | 247ms | 0.5%  
湖北 | 45个 | 0 | 251ms | 5.5%  
山东 | 51个 | 1个 | 255ms | 8.6%  
河南 | 56个 | 0 | 256ms | 7.9%  
黑龙江 | 39个 | 0 | 257ms | 7.3%  
青海 | 4个 | 0 | 260ms | 0.8%  
四川 | 49个 | 0 | 261ms | 2.4%  
甘肃 | 20个 | 0 | 263ms | 0.8%  
新疆 | 28个 | 0 | 296ms | 3.1%  
西藏 | 1个 | 0 | 313ms | 0  
河北 | 33个 | 0 | 323ms | 9.8%  
  
**简评：** 如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有948个，其中超时点11个，平均响应时间为244毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的1个，在200-300毫秒间的28个，超过300毫秒的2个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_australia-sydney_20180514_overseas.png)

**海外线路到Vultr澳大利亚-悉尼机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
澳大利亚 | 2个 | 0 | 5ms | 0  
台湾 | 1个 | 0 | 156ms | -  
日本 | 2个 | 0 | 163ms | 0.5%  
韩国 | 13个 | 0 | 164ms | 0  
美国 | 18个 | 0 | 167ms | 0  
香港 | 19个 | 0 | 174ms | 0  
印度尼西亚 | 1个 | 0 | 201ms | 1.0%  
马来西亚 | 3个 | 0 | 222ms | 0  
加拿大 | 3个 | 0 | 237ms | 0.5%  
均值 | 78个 | 0 | 243ms | 0.7%  
新加坡 | 6个 | 0 | 266ms | 0  
菲律宾 | 1个 | 0 | 277ms | 0  
法国 | 2个 | 0 | 299ms | 0.5%  
英国 | 2个 | 0 | 312ms | 0  
德国 | 2个 | 0 | 315ms | 0  
俄罗斯 | 1个 | 0 | 335ms | 0  
柬埔寨 | 1个 | 0 | 351ms | 8.0%  
南非 | 1个 | 0 | 495ms | 1.0%  
  
**简评：** 如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点0个，平均响应时间为243毫秒，丢包率为0%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的5个，在200-300毫秒间的6个，超过300毫秒的5个；

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
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr悉尼机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [20180622](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [20180804](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [20180918](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")



本文最初发表于[多地到Vultr悉尼[Sydney]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-sydney.html)
