#  多地到Vultr洛杉矶[LosAngeles]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr洛杉矶\[LosAngeles\]机房的Ping测试（20180622）](/images/thumbnails/to_vultr_LosAngeles.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-洛杉矶机房](https://vps123.top/vultr-facilities.html#losangeles)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-洛杉矶机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180622-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的881个有效测试样本中，共有超时点26个；响应均值为212毫秒，最快的三地区为广西、广东、安徽，最慢的三地区为甘肃、新疆、香港；云南、浙江、江苏、安徽、湖南等11处有响应超时情况；天津、上海、贵州丢包率较高。海外19个国家地区的88个有效测试样本中，无超时点；响应均值为156毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为印度尼西亚、马来西亚、柬埔寨；日本丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-losangeles_20180622_mainland.png)

大陆各省份到Vultr美国-洛杉矶机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
广西 | 40个 | 0 | 189ms | 2.6% | 江西 | 24个 | 1个 | 211ms | 1.6%  
广东 | 75个 | 0 | 190ms | 2.7% | 均值 | 881个 | 26个 | 212ms | 2.5%  
安徽 | 30个 | 1个 | 193ms | 3.2% | 辽宁 | 36个 | 1个 | 214ms | 3.4%  
湖南 | 36个 | 1个 | 196ms | 1.4% | 云南 | 22个 | 11个 | 215ms | 1.4%  
海南 | 12个 | 0 | 196ms | 3.0% | 浙江 | 52个 | 5个 | 217ms | 3.6%  
上海 | 7个 | 1个 | 197ms | 6.2% | 四川 | 42个 | 0 | 220ms | 1.3%  
河南 | 44个 | 1个 | 200ms | 4.1% | 宁夏 | 13个 | 0 | 220ms | 0.8%  
天津 | 3个 | 0 | 200ms | 6.7% | 北京 | 10个 | 0 | 222ms | 4.1%  
重庆 | 12个 | 0 | 201ms | 0.8% | 吉林 | 20个 | 0 | 224ms | 1.6%  
山东 | 40个 | 0 | 202ms | 1.8% | 内蒙古 | 28个 | 0 | 230ms | 2.9%  
河北 | 30个 | 1个 | 202ms | 1.3% | 青海 | 5个 | 0 | 236ms | 0.8%  
山西 | 33个 | 0 | 204ms | 0.3% | 黑龙江 | 32个 | 0 | 239ms | 1.9%  
贵州 | 24个 | 0 | 207ms | 5.6% | 陕西 | 23个 | 0 | 240ms | 2.6%  
福建 | 26个 | 1个 | 208ms | 3.4% | 甘肃 | 15个 | 0 | 256ms | 1.5%  
江苏 | 69个 | 2个 | 211ms | 2.5% | 新疆 | 24个 | 0 | 274ms | 1.3%  
湖北 | 30个 | 0 | 211ms | 3.3% | 香港 | 24个 | 0 | - | -  
  
简评：如果你考虑在Vultr的洛杉矶[LosAngeles]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有881个，其中超时点26个，平均响应时间为212毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的8个，在200-300毫秒间的22个；  
超时点较多的省份：上海、云南；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-losangeles_20180622_overseas.png)

海外线路到Vultr美国-洛杉矶机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 20个 | 0 | 22ms | 0 | 巴西 | 1个 | 0 | 154ms | 0  
加拿大 | 2个 | 0 | 75ms | 0 | 均值 | 88个 | 0 | 156ms | 0.5%  
日本 | 2个 | 0 | 125ms | 7.0% | 英国 | 2个 | 0 | 160ms | 0  
意大利 | 1个 | 0 | 135ms | - | 澳大利亚 | 1个 | 0 | 166ms | 0  
德国 | 1个 | 0 | 137ms | - | 南非 | 2个 | 0 | 170ms | 0.5%  
台湾 | 2个 | 0 | 140ms | 0 | 菲律宾 | 2个 | 0 | 176ms | 0.5%  
新加坡 | 5个 | 0 | 143ms | 0 | 越南 | 2个 | 0 | 181ms | 0  
香港 | 24个 | 0 | 145ms | 0 | 印度尼西亚 | 1个 | 0 | 210ms | 0  
韩国 | 13个 | 0 | 150ms | 0 | 马来西亚 | 5个 | 0 | 232ms | 0.2%  
法国 | 1个 | 0 | 154ms | 0 | 柬埔寨 | 1个 | 0 | 287ms | 0  
  
简评：如果你考虑在Vultr的洛杉矶[LosAngeles]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有88个，其中超时点0个，平均响应时间为156毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的14个，在200-300毫秒间的3个；

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
    * [迈阿密](/vultr/idc/miami/20180622-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180622")
    * [新泽西](/vultr/idc/newjersey/20180622-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180622")
    * [巴黎](/vultr/idc/paris/20180622-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180622")
    * [西雅图](/vultr/idc/seattle/20180622-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180622")
    * [硅谷](/vultr/idc/siliconvalley/20180622-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180622")
    * [新加坡](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [悉尼](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [东京](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
  * 到Vultr洛杉矶机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/losangeles/20180514-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180514")
    * [20180527](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [20180804](/vultr/idc/losangeles/20180804-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180804")
    * [20180918](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
  * 本期报告：在洛杉矶部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/losangeles/20180622-bwg-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180622")



本文最初发表于[多地到Vultr洛杉矶[LosAngeles]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-vultr-idc-losangeles.html)
