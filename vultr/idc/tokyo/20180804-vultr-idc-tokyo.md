#  多地到Vultr东京[Tokyo]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr东京\[Tokyo\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[日本-东京机房](https://vps123.top/vultr-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5257个有效测试样本中，共有超时点72个；响应均值为192毫秒，最快的三地区为广东、湖南、贵州，最慢的三地区为吉林、新疆、西藏；浙江、江苏、辽宁、上海、江西等10处有响应超时情况；西藏、安徽、青海、上海、江西等31处丢包率较高。海外19个国家地区的240个有效测试样本中，共有超时点3个；响应均值为176毫秒，最快的三地区为日本、韩国、台湾，最慢的三地区为澳大利亚、菲律宾、意大利；香港有响应超时情况；菲律宾、日本丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_japan-tokyo_20180804_mainland.png)

**大陆各省份到Vultr日本-东京机房的测速数据 [20180804]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
广东 | 454个 | 0 | 144ms | 6.7%  
湖南 | 249个 | 3个 | 147ms | 10.0%  
贵州 | 150个 | 3个 | 159ms | 12.7%  
福建 | 144个 | 0 | 159ms | 25.6%  
海南 | 48个 | 0 | 162ms | 16.9%  
重庆 | 45个 | 0 | 169ms | 15.2%  
广西 | 236个 | 0 | 175ms | 15.4%  
上海 | 31个 | 7个 | 175ms | 30.4%  
江西 | 131个 | 7个 | 176ms | 28.4%  
云南 | 123个 | 0 | 176ms | 12.1%  
安徽 | 224个 | 0 | 176ms | 32.9%  
北京 | 36个 | 0 | 177ms | 21.2%  
河南 | 339个 | 0 | 185ms | 14.0%  
湖北 | 197个 | 0 | 188ms | 12.4%  
浙江 | 242个 | 19个 | 191ms | 23.1%  
山东 | 366个 | 0 | 192ms | 18.4%  
均值 | 5257个 | 72个 | 192ms | 18.0%  
河北 | 244个 | 0 | 194ms | 12.4%  
江苏 | 346个 | 12个 | 201ms | 26.3%  
黑龙江 | 180个 | 0 | 209ms | 14.2%  
四川 | 281个 | 3个 | 210ms | 16.0%  
陕西 | 149个 | 6个 | 210ms | 15.0%  
山西 | 193个 | 0 | 212ms | 17.2%  
天津 | 16个 | 0 | 213ms | 18.7%  
甘肃 | 112个 | 0 | 222ms | 26.2%  
宁夏 | 32个 | 0 | 223ms | 26.0%  
内蒙古 | 208个 | 0 | 236ms | 22.5%  
青海 | 16个 | 0 | 237ms | 31.6%  
辽宁 | 222个 | 9个 | 239ms | 22.0%  
吉林 | 100个 | 0 | 263ms | 24.4%  
新疆 | 135个 | 3个 | 266ms | 24.5%  
西藏 | 8个 | 0 | 360ms | 44.5%  
  
**简评：** 如果你考虑在Vultr的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有5257个，其中超时点72个，平均响应时间为192毫秒，丢包率为18%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的17个，在200-300毫秒间的13个，超过300毫秒的1个；  
超时点较多的省份：上海；  
丢包率较高的省份：湖南、贵州、福建、海南、重庆、广西、上海、江西、云南、安徽、北京、河南、湖北、浙江、山东、河北、江苏、黑龙江、四川、陕西、山西、天津、甘肃、宁夏、内蒙古、青海、辽宁、吉林、新疆、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_japan-tokyo_20180804_overseas.png)

**海外线路到Vultr日本-东京机房的测速数据 [20180804]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
日本 | 6个 | 0 | 23ms | 6.5%  
韩国 | 21个 | 0 | 53ms | 0  
台湾 | 3个 | 0 | 59ms | 0  
香港 | 66个 | 3个 | 96ms | 0  
新加坡 | 15个 | 0 | 101ms | 0  
美国 | 48个 | 0 | 113ms | 1.2%  
荷兰 | 3个 | 0 | 113ms | 0  
马来西亚 | 12个 | 0 | 114ms | 0.5%  
法国 | 3个 | 0 | 143ms | 0  
均值 | 240个 | 3个 | 176ms | 2.7%  
加拿大 | 15个 | 0 | 200ms | 0.3%  
俄罗斯 | 3个 | 0 | 202ms | -  
印度尼西亚 | 6个 | 0 | 208ms | 3.2%  
巴西 | 3个 | 0 | 225ms | 0  
英国 | 6个 | 0 | 268ms | 0.5%  
德国 | 9个 | 0 | 269ms | 0  
南非 | 6个 | 0 | 272ms | 2.5%  
澳大利亚 | 6个 | 0 | 284ms | 0  
菲律宾 | 6个 | 0 | 288ms | 30.5%  
意大利 | 3个 | 0 | 315ms | -  
  
**简评：** 如果你考虑在Vultr的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有240个，其中超时点3个，平均响应时间为176毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的3个，在100-200毫秒间的6个，在200-300毫秒间的8个，超过300毫秒的1个；  
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
    * [新泽西](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
  * 到Vultr东京机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
    * [20180527](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
    * [20180622](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
    * [20180918](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")



本文最初发表于[多地到Vultr东京[Tokyo]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-tokyo.html)
