#  多地到Vultr硅谷[SiliconValley]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr硅谷\[SiliconValley\]机房的Ping测试（20180622）](/images/thumbnails/to_vultr_SiliconValley.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-硅谷机房](https://vps123.top/vultr-facilities.html#siliconvalley)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-硅谷机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180622-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆32个省市的929个有效测试样本中，共有超时点9个；响应均值为216毫秒，最快的三地区为山东、北京、海南，最慢的三地区为新疆、西藏、香港；香港、江苏、上海、浙江、广东等7处有响应超时情况。海外17个国家地区的78个有效测试样本中，共有超时点3个；响应均值为149毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为南非、越南、印度尼西亚；香港有响应超时情况。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于硅谷\[SiliconValley\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-siliconvalley_20180622_mainland.png)

**大陆各省份到Vultr美国-硅谷机房的测速数据 [20180622]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
山东 | 42个 | 0 | 188ms | 0.4%  
北京 | 9个 | 0 | 189ms | 0  
海南 | 12个 | 0 | 192ms | 0.6%  
河北 | 34个 | 0 | 193ms | 0.2%  
江苏 | 69个 | 1个 | 201ms | 1.4%  
上海 | 8个 | 1个 | 201ms | 0.7%  
河南 | 52个 | 0 | 206ms | 0.7%  
浙江 | 53个 | 1个 | 206ms | 1.5%  
天津 | 3个 | 0 | 206ms | 3.3%  
辽宁 | 36个 | 0 | 207ms | 0.8%  
广东 | 80个 | 1个 | 208ms | 1.6%  
广西 | 43个 | 0 | 214ms | 1.9%  
山西 | 38个 | 0 | 214ms | 1.2%  
福建 | 30个 | 0 | 216ms | 3.3%  
湖南 | 37个 | 0 | 216ms | 1.0%  
均值 | 929个 | 9个 | 216ms | 1.5%  
内蒙古 | 32个 | 0 | 217ms | 1.3%  
重庆 | 12个 | 0 | 219ms | 1.9%  
吉林 | 18个 | 0 | 221ms | 1.1%  
湖北 | 36个 | 0 | 222ms | 1.9%  
黑龙江 | 33个 | 0 | 224ms | 1.8%  
安徽 | 34个 | 1个 | 225ms | 2.2%  
贵州 | 25个 | 1个 | 228ms | 1.8%  
江西 | 23个 | 0 | 228ms | 1.8%  
四川 | 40个 | 0 | 230ms | 1.7%  
宁夏 | 13个 | 0 | 231ms | 2.2%  
陕西 | 30个 | 0 | 233ms | 1.6%  
甘肃 | 21个 | 0 | 241ms | 1.2%  
云南 | 14个 | 0 | 250ms | 3.8%  
青海 | 3个 | 0 | 252ms | 1.7%  
新疆 | 26个 | 0 | 268ms | 1.6%  
西藏 | 1个 | 0 | 303ms | 5.0%  
香港 | 22个 | 3个 | - | -  
  
**简评：** 如果你考虑在Vultr的硅谷[SiliconValley]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于硅谷[SiliconValley]的机房的连通状况。到此机房的ping监测点共有929个，其中超时点9个，平均响应时间为216毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的4个，在200-300毫秒间的26个，超过300毫秒的1个；  
超时点较多的省份：上海、香港；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于硅谷\[SiliconValley\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-siliconvalley_20180622_overseas.png)

**海外线路到Vultr美国-硅谷机房的测速数据 [20180622]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
美国 | 19个 | 0 | 30ms | 0  
加拿大 | 2个 | 0 | 77ms | 0  
日本 | 2个 | 0 | 119ms | 1.0%  
香港 | 22个 | 3个 | 134ms | 0  
台湾 | 2个 | 0 | 137ms | 0  
巴西 | 1个 | 0 | 141ms | 0  
新加坡 | 5个 | 0 | 144ms | 0  
均值 | 78个 | 3个 | 149ms | 0.1%  
德国 | 1个 | 0 | 152ms | -  
意大利 | 1个 | 0 | 156ms | -  
韩国 | 13个 | 0 | 158ms | 0  
法国 | 1个 | 0 | 159ms | 0  
澳大利亚 | 1个 | 0 | 167ms | 0  
菲律宾 | 2个 | 0 | 175ms | 0  
英国 | 1个 | 0 | 176ms | 0  
南非 | 2个 | 0 | 180ms | 0  
越南 | 2个 | 0 | 183ms | 0  
印度尼西亚 | 1个 | 0 | 256ms | 1.0%  
  
**简评：** 如果你考虑在Vultr的硅谷[SiliconValley]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于硅谷[SiliconValley]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点3个，平均响应时间为149毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的14个，在200-300毫秒间的1个；  
超时点较多的国家/地区：香港；

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
    * [新加坡](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [悉尼](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [东京](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
  * 到Vultr硅谷机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [20180527](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [20180804](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [20180918](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")



本文最初发表于[多地到Vultr硅谷[SiliconValley]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-vultr-idc-siliconvalley.html)
