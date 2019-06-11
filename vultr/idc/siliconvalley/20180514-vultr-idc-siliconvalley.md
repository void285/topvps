#  多地到Vultr硅谷[SiliconValley]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr硅谷\[SiliconValley\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_SiliconValley.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-硅谷机房](https://vps123.top/vultr-facilities.html#siliconvalley)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-硅谷机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr美国-硅谷机房的PING测试结果，连通概况如下：大陆31个省市的972个有效测试样本中，共有超时点15个；响应均值为258毫秒，最快的三地区为北京、天津、上海，最慢的三地区为青海、新疆、西藏；浙江、江苏、山东、广东、北京等8处有响应超时情况；西藏、河南、甘肃、河北、江西等29处丢包率较高。海外16个国家地区的55个有效测试样本中，共有超时点1个；响应均值为187毫秒，最快的三地区为美国、加拿大、韩国，最慢的三地区为印度尼西亚、南非、柬埔寨；香港有响应超时情况；柬埔寨、印度尼西亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于硅谷\[SiliconValley\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-siliconvalley_20180514_mainland.png)

大陆各省份到Vultr美国-硅谷机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 8个 | 1个 | 196ms | 10.2% | 均值 | 972个 | 15个 | 258ms | 11.3%  
天津 | 5个 | 0 | 200ms | 4.2% | 海南 | 12个 | 0 | 260ms | 9.3%  
上海 | 7个 | 0 | 223ms | 6.7% | 广西 | 36个 | 0 | 263ms | 6.6%  
吉林 | 16个 | 0 | 226ms | 4.1% | 贵州 | 27个 | 0 | 264ms | 10.2%  
山东 | 53个 | 2个 | 237ms | 10.5% | 江西 | 21个 | 0 | 265ms | 16.3%  
江苏 | 62个 | 3个 | 240ms | 10.8% | 湖南 | 47个 | 0 | 268ms | 11.8%  
陕西 | 33个 | 0 | 240ms | 10.9% | 湖北 | 47个 | 0 | 270ms | 10.4%  
福建 | 36个 | 1个 | 243ms | 5.6% | 河南 | 57个 | 0 | 271ms | 20.5%  
辽宁 | 38个 | 0 | 243ms | 15.4% | 重庆 | 14个 | 1个 | 278ms | 8.9%  
黑龙江 | 40个 | 0 | 244ms | 11.5% | 四川 | 47个 | 0 | 279ms | 7.3%  
浙江 | 49个 | 4个 | 247ms | 10.2% | 云南 | 24个 | 1个 | 282ms | 10.1%  
内蒙古 | 34个 | 0 | 248ms | 11.6% | 河北 | 33个 | 0 | 285ms | 16.5%  
安徽 | 42个 | 0 | 254ms | 10.2% | 甘肃 | 22个 | 0 | 288ms | 17.3%  
宁夏 | 11个 | 0 | 255ms | 12.5% | 青海 | 4个 | 0 | 292ms | 15.8%  
山西 | 39个 | 0 | 255ms | 14.1% | 新疆 | 29个 | 0 | 294ms | 14.6%  
广东 | 78个 | 2个 | 256ms | 6.1% | 西藏 | 1个 | 0 | 369ms | 31.0%  
  
简评：如果你考虑在Vultr的硅谷[SiliconValley]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于硅谷[SiliconValley]的机房的连通状况。到此机房的ping监测点共有972个，其中超时点15个，平均响应时间为258毫秒，丢包率为11%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的2个，在200-300毫秒间的28个，超过300毫秒的1个；  
超时点较多的省份：北京；  
丢包率较高的省份：北京、山东、江苏、陕西、辽宁、黑龙江、浙江、内蒙古、安徽、宁夏、山西、贵州、江西、湖南、湖北、河南、云南、河北、甘肃、青海、新疆、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于硅谷\[SiliconValley\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-siliconvalley_20180514_overseas.png)

海外线路到Vultr美国-硅谷机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 13个 | 0 | 18ms | 0 | 德国 | 1个 | 0 | 171ms | 0  
加拿大 | 3个 | 0 | 75ms | 0 | 新加坡 | 5个 | 0 | 187ms | 0  
韩国 | 9个 | 0 | 138ms | 0 | 均值 | 55个 | 1个 | 187ms | 3.0%  
日本 | 1个 | 0 | 139ms | 0 | 菲律宾 | 1个 | 0 | 194ms | 0  
法国 | 1个 | 0 | 148ms | 0 | 马来西亚 | 2个 | 0 | 211ms | 0.5%  
香港 | 13个 | 1个 | 152ms | - | 印度尼西亚 | 1个 | 0 | 288ms | 6.0%  
台湾 | 1个 | 0 | 157ms | - | 南非 | 1个 | 0 | 382ms | 0  
澳大利亚 | 1个 | 0 | 165ms | 1.0% | 柬埔寨 | 1个 | 0 | 396ms | 35.0%  
英国 | 1个 | 0 | 170ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Vultr的硅谷[SiliconValley]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于硅谷[SiliconValley]的机房的连通状况。到此机房的ping监测点共有55个，其中超时点1个，平均响应时间为187毫秒，丢包率为3%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的10个，在200-300毫秒间的2个，超过300毫秒的2个；  
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
    * [新泽西](/vultr/idc/newjersey/20180514-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180514")
    * [巴黎](/vultr/idc/paris/20180514-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180514")
    * [西雅图](/vultr/idc/seattle/20180514-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180514")
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr硅谷机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [20180622](/vultr/idc/siliconvalley/20180622-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180622")
    * [20180804](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [20180918](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")



本文最初发表于[多地到Vultr硅谷[SiliconValley]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-siliconvalley.html)
