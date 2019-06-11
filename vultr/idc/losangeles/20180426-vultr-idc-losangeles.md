#  多地到Vultr洛杉矶[LosAngeles]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr洛杉矶\[LosAngeles\]机房的Ping测试（20180426）](/images/thumbnails/to_vultr_LosAngeles.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-洛杉矶机房](https://vps123.top/vultr-facilities.html#losangeles)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-洛杉矶机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180426-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Vultr美国-洛杉矶机房的PING测试结果，连通概况如下：大陆31个省市的786个有效测试样本中，共有超时点6个；响应均值为208毫秒，最快的三地区为海南、山西、广东，最慢的三地区为甘肃、西藏、新疆；浙江、河北、江苏、甘肃、新疆有响应超时情况；北京丢包率较高。海外14个国家地区的54个有效测试样本中，无超时点；响应均值为159毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为马来西亚、越南、柬埔寨。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_idc_vultr_usa-losangeles_20180426_mainland.png)

**大陆各省份到Vultr美国-洛杉矶机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
海南 | 10个 | 0 | 179ms | 0  
山西 | 29个 | 0 | 188ms | 1.1%  
广东 | 58个 | 0 | 190ms | 0.8%  
湖南 | 33个 | 0 | 190ms | 1.5%  
天津 | 5个 | 0 | 193ms | 4.0%  
北京 | 4个 | 0 | 193ms | 7.5%  
上海 | 8个 | 0 | 194ms | 1.3%  
湖北 | 37个 | 0 | 196ms | 1.1%  
河北 | 35个 | 1个 | 196ms | 1.9%  
河南 | 50个 | 0 | 198ms | 1.4%  
广西 | 27个 | 0 | 198ms | 2.3%  
吉林 | 14个 | 0 | 204ms | 2.4%  
陕西 | 28个 | 0 | 206ms | 0.8%  
辽宁 | 36个 | 0 | 206ms | 3.2%  
黑龙江 | 29个 | 0 | 207ms | 1.9%  
均值 | 786个 | 6个 | 208ms | 1.7%  
山东 | 40个 | 0 | 209ms | 0.9%  
江苏 | 49个 | 1个 | 212ms | 1.6%  
云南 | 23个 | 0 | 212ms | 3.6%  
重庆 | 10个 | 0 | 213ms | 1.2%  
四川 | 33个 | 0 | 214ms | 1.1%  
青海 | 4个 | 0 | 216ms | 0  
福建 | 27个 | 0 | 216ms | 1.0%  
江西 | 22个 | 0 | 216ms | 1.1%  
贵州 | 22个 | 0 | 218ms | 2.2%  
内蒙古 | 26个 | 0 | 220ms | 1.9%  
浙江 | 35个 | 2个 | 223ms | 1.9%  
安徽 | 38个 | 0 | 226ms | 1.4%  
宁夏 | 9个 | 0 | 229ms | 4.7%  
甘肃 | 21个 | 1个 | 247ms | 2.7%  
西藏 | 1个 | 0 | 255ms | 0  
新疆 | 23个 | 1个 | 265ms | 1.5%  
  
**简评：** 如果你考虑在Vultr的洛杉矶[LosAngeles]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有786个，其中超时点6个，平均响应时间为208毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的11个，在200-300毫秒间的20个；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_idc_vultr_usa-losangeles_20180426_overseas.png)

**海外线路到Vultr美国-洛杉矶机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
美国 | 10个 | 0 | 14ms | -  
加拿大 | 3个 | 0 | 77ms | 0  
日本 | 2个 | 0 | 130ms | 0.5%  
荷兰 | 1个 | 0 | 136ms | -  
法国 | 1个 | 0 | 139ms | 0  
香港 | 16个 | 0 | 148ms | 0  
台湾 | 1个 | 0 | 153ms | -  
英国 | 2个 | 0 | 154ms | 0  
均值 | 54个 | 0 | 159ms | 0.2%  
韩国 | 8个 | 0 | 160ms | 0  
澳大利亚 | 1个 | 0 | 172ms | 0  
新加坡 | 4个 | 0 | 180ms | 0  
马来西亚 | 3个 | 0 | 204ms | 0  
越南 | 1个 | 0 | 205ms | 0  
柬埔寨 | 1个 | 0 | 362ms | 2.0%  
  
**简评：** 如果你考虑在Vultr的洛杉矶[LosAngeles]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有54个，其中超时点0个，平均响应时间为159毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的9个，在200-300毫秒间的2个，超过300毫秒的1个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180426 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180426 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180426-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180426")
    * [亚特兰大](/vultr/idc/atlanta/20180426-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180426")
    * [芝加哥](/vultr/idc/chicago/20180426-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180426")
    * [达拉斯](/vultr/idc/dallas/20180426-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180426")
    * [法兰克福](/vultr/idc/frankfurt/20180426-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180426")
    * [伦敦](/vultr/idc/london/20180426-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180426")
    * [迈阿密](/vultr/idc/miami/20180426-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180426")
    * [新泽西](/vultr/idc/newjersey/20180426-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180426")
    * [巴黎](/vultr/idc/paris/20180426-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180426")
    * [西雅图](/vultr/idc/seattle/20180426-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180426")
    * [硅谷](/vultr/idc/siliconvalley/20180426-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180426")
    * [新加坡](/vultr/idc/singapore/20180426-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180426")
    * [悉尼](/vultr/idc/sydney/20180426-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180426")
    * [东京](/vultr/idc/tokyo/20180426-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180426")
  * 到Vultr洛杉矶机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/losangeles/20180514-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180514")
    * [20180527](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [20180622](/vultr/idc/losangeles/20180622-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180622")
    * [20180804](/vultr/idc/losangeles/20180804-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180804")
    * [20180918](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
  * 本期报告：在洛杉矶部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/losangeles/20180426-bwg-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180426")



本文最初发表于[多地到Vultr洛杉矶[LosAngeles]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-vultr-idc-losangeles.html)
