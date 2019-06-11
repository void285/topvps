#  多地到Vultr洛杉矶[LosAngeles]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr洛杉矶\[LosAngeles\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_LosAngeles.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-洛杉矶机房](https://vps123.top/vultr-facilities.html#losangeles)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-洛杉矶机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr美国-洛杉矶机房的PING测试结果，连通概况如下：大陆31个省市的966个有效测试样本中，共有超时点19个；响应均值为235毫秒，最快的三地区为上海、天津、辽宁，最慢的三地区为四川、云南、西藏；浙江、广东、湖北、湖南、贵州等11处有响应超时情况；云南、西藏、广西、海南、湖北等30处丢包率较高。海外18个国家地区的78个有效测试样本中，共有超时点2个；响应均值为180毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为印度尼西亚、南非、柬埔寨；香港有响应超时情况；柬埔寨、香港丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-losangeles_20180514_mainland.png)

**大陆各省份到Vultr美国-洛杉矶机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 7个 | 0 | 174ms | 7.9%  
天津 | 5个 | 0 | 190ms | 5.6%  
辽宁 | 40个 | 0 | 205ms | 10.0%  
河北 | 30个 | 0 | 206ms | 9.6%  
宁夏 | 10个 | 0 | 206ms | 11.3%  
河南 | 60个 | 0 | 207ms | 11.3%  
北京 | 7个 | 1个 | 210ms | 8.5%  
吉林 | 15个 | 0 | 211ms | 4.1%  
山西 | 37个 | 0 | 214ms | 10.8%  
江苏 | 63个 | 1个 | 215ms | 9.1%  
福建 | 34个 | 1个 | 219ms | 6.8%  
内蒙古 | 34个 | 0 | 219ms | 10.5%  
青海 | 4个 | 0 | 220ms | 14.0%  
黑龙江 | 37个 | 0 | 221ms | 10.2%  
浙江 | 51个 | 3个 | 222ms | 8.3%  
山东 | 52个 | 1个 | 223ms | 14.6%  
陕西 | 33个 | 0 | 223ms | 11.8%  
安徽 | 37个 | 0 | 229ms | 11.1%  
甘肃 | 20个 | 0 | 233ms | 14.5%  
均值 | 966个 | 19个 | 235ms | 12.8%  
江西 | 23个 | 0 | 249ms | 12.0%  
湖南 | 46个 | 2个 | 253ms | 15.0%  
广东 | 79个 | 3个 | 254ms | 16.2%  
贵州 | 28个 | 2个 | 256ms | 17.5%  
广西 | 37个 | 1个 | 262ms | 21.4%  
湖北 | 48个 | 3个 | 263ms | 17.7%  
新疆 | 27个 | 0 | 265ms | 12.9%  
海南 | 12个 | 0 | 268ms | 20.9%  
重庆 | 16个 | 1个 | 274ms | 8.5%  
四川 | 50个 | 0 | 279ms | 15.2%  
云南 | 23个 | 0 | 285ms | 23.0%  
西藏 | 1个 | 0 | 317ms | 23.0%  
  
**简评：** 如果你考虑在Vultr的洛杉矶[LosAngeles]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有966个，其中超时点19个，平均响应时间为235毫秒，丢包率为12%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的2个，在200-300毫秒间的28个，超过300毫秒的1个；  
超时点较多的省份：北京；  
丢包率较高的省份：辽宁、宁夏、河南、山西、内蒙古、青海、黑龙江、山东、陕西、安徽、甘肃、江西、湖南、广东、贵州、广西、湖北、新疆、海南、四川、云南、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-losangeles_20180514_overseas.png)

**海外线路到Vultr美国-洛杉矶机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
美国 | 18个 | 0 | 8ms | 3.3%  
加拿大 | 3个 | 0 | 72ms | 0.5%  
日本 | 2个 | 0 | 121ms | 0  
韩国 | 13个 | 0 | 138ms | 0  
法国 | 2个 | 0 | 147ms | 0  
英国 | 2个 | 0 | 159ms | 0  
台湾 | 1个 | 0 | 161ms | -  
澳大利亚 | 2个 | 0 | 163ms | 0.5%  
德国 | 1个 | 0 | 167ms | 0  
巴西 | 1个 | 0 | 172ms | 0  
均值 | 78个 | 2个 | 180ms | 1.3%  
菲律宾 | 1个 | 0 | 181ms | 0  
香港 | 19个 | 2个 | 184ms | 6.0%  
新加坡 | 6个 | 0 | 187ms | 0  
马来西亚 | 3个 | 0 | 193ms | 0  
俄罗斯 | 1个 | 0 | 226ms | 0  
印度尼西亚 | 1个 | 0 | 234ms | 0  
南非 | 1个 | 0 | 359ms | 0  
柬埔寨 | 1个 | 0 | 381ms | 11.0%  
  
**简评：** 如果你考虑在Vultr的洛杉矶[LosAngeles]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点2个，平均响应时间为180毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的12个，在200-300毫秒间的2个，超过300毫秒的2个；  
超时点较多的国家/地区：香港；  
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
    * [迈阿密](/vultr/idc/miami/20180514-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180514")
    * [新泽西](/vultr/idc/newjersey/20180514-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180514")
    * [巴黎](/vultr/idc/paris/20180514-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180514")
    * [西雅图](/vultr/idc/seattle/20180514-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180514")
    * [硅谷](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr洛杉矶机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [20180622](/vultr/idc/losangeles/20180622-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180622")
    * [20180804](/vultr/idc/losangeles/20180804-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180804")
    * [20180918](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
  * 本期报告：在洛杉矶部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/losangeles/20180514-bwg-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180514")



本文最初发表于[多地到Vultr洛杉矶[LosAngeles]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-losangeles.html)
