#  多地到Vultr伦敦[London]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr伦敦\[London\]机房的Ping测试（20180918）](/images/thumbnails/to_vultr_Seattle.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[英国-伦敦机房](https://vps123.top/vultr-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180918-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Vultr英国-伦敦机房的PING测试结果，连通概况如下：大陆31个省市的1393个有效测试样本中，共有超时点11个；响应均值为291毫秒，最快的三地区为河北、甘肃、内蒙古，最慢的三地区为黑龙江、西藏、吉林；江苏、浙江、湖北、广东、贵州等6处有响应超时情况；吉林、山西、重庆、黑龙江、山东等12处丢包率较高。海外16个国家地区的61个有效测试样本中，无超时点；响应均值为194毫秒，最快的三地区为德国、俄罗斯、加拿大，最慢的三地区为澳大利亚、菲律宾、印度尼西亚；菲律宾、赞比亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_uk-london_20180918_mainland.png)

大陆各省份到Vultr英国-伦敦机房的测速数据 [20180918] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
河北 | 55个 | 0 | 263ms | 4.4% | 四川 | 71个 | 0 | 289ms | 2.5%  
甘肃 | 32个 | 0 | 264ms | 0.1% | 湖南 | 72个 | 0 | 289ms | 3.4%  
内蒙古 | 56个 | 0 | 265ms | 6.6% | 均值 | 1393个 | 11个 | 291ms | 5.1%  
天津 | 7个 | 0 | 268ms | 1.4% | 江西 | 38个 | 0 | 292ms | 2.0%  
陕西 | 44个 | 0 | 269ms | 2.6% | 云南 | 33个 | 0 | 301ms | 3.5%  
安徽 | 67个 | 0 | 271ms | 3.3% | 青海 | 6个 | 0 | 303ms | 0  
浙江 | 67个 | 2个 | 274ms | 3.5% | 山东 | 91个 | 0 | 307ms | 9.1%  
宁夏 | 6个 | 0 | 274ms | 0 | 贵州 | 41个 | 1个 | 308ms | 3.3%  
广东 | 118个 | 1个 | 275ms | 2.8% | 河南 | 85个 | 0 | 310ms | 8.5%  
辽宁 | 58个 | 0 | 278ms | 7.1% | 海南 | 14个 | 0 | 310ms | 5.9%  
上海 | 8个 | 0 | 279ms | 5.6% | 重庆 | 8个 | 0 | 316ms | 9.8%  
福建 | 44个 | 0 | 283ms | 3.7% | 新疆 | 33个 | 0 | 321ms | 4.2%  
广西 | 59个 | 0 | 283ms | 3.0% | 山西 | 55个 | 1个 | 323ms | 11.0%  
湖北 | 50个 | 2个 | 284ms | 4.1% | 黑龙江 | 52个 | 0 | 329ms | 9.5%  
北京 | 8个 | 0 | 286ms | 1.4% | 西藏 | 2个 | 0 | 351ms | 8.0%  
江苏 | 91个 | 4个 | 288ms | 5.7% | 吉林 | 22个 | 0 | 371ms | 12.6%  
  
简评：如果你考虑在Vultr的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有1393个，其中超时点11个，平均响应时间为291毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的19个，超过300毫秒的12个；  
丢包率较高的省份：山西、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_uk-london_20180918_overseas.png)

海外线路到Vultr英国-伦敦机房的测速数据 [20180918] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
德国 | 2个 | 0 | 37ms | 0 | 新加坡 | 4个 | 0 | 200ms | 0  
俄罗斯 | 1个 | 0 | 47ms | - | 赞比亚 | 1个 | 0 | 209ms | 9.0%  
加拿大 | 2个 | 0 | 76ms | 0 | 马来西亚 | 6个 | 0 | 220ms | 0.2%  
荷兰 | 1个 | 0 | 105ms | 0 | 韩国 | 8个 | 0 | 234ms | 0  
美国 | 9个 | 0 | 152ms | 0 | 日本 | 3个 | 0 | 246ms | 1.0%  
香港 | 15个 | 0 | 179ms | 0 | 澳大利亚 | 2个 | 0 | 300ms | 0  
均值 | 61个 | 0 | 194ms | 1.6% | 菲律宾 | 2个 | 0 | 316ms | 13.8%  
越南 | 2个 | 0 | 195ms | 0 | 印度尼西亚 | 1个 | 0 | 392ms | 0  
台湾 | 2个 | 0 | 197ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Vultr的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有61个，其中超时点0个，平均响应时间为194毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的1个，在100-200毫秒间的6个，在200-300毫秒间的5个，超过300毫秒的2个；  
丢包率较高的国家/地区：菲律宾；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180918 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180918 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180918-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180918")
    * [亚特兰大](/vultr/idc/atlanta/20180918-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180918")
    * [芝加哥](/vultr/idc/chicago/20180918-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180918")
    * [达拉斯](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
    * [法兰克福](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")
    * [洛杉矶](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
    * [迈阿密](/vultr/idc/miami/20180918-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180918")
    * [新泽西](/vultr/idc/newjersey/20180918-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180918")
    * [巴黎](/vultr/idc/paris/20180918-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180918")
    * [西雅图](/vultr/idc/seattle/20180918-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180918")
    * [硅谷](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")
    * [新加坡](/vultr/idc/singapore/20180918-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180918")
    * [悉尼](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")
    * [东京](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 到Vultr伦敦机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/london/20180514-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180514")
    * [20180527](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")
    * [20180622](/vultr/idc/london/20180622-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180622")
    * [20180804](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180918-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
    * [Linode](/linode/idc/london/20180918-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180918")



本文最初发表于[多地到Vultr伦敦[London]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-vultr-idc-london.html)
