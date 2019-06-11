#  多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean班加罗尔\[Bangalore\]机房的Ping测试（20180918）](/images/thumbnails/to_do_Bangalore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[印度-班加罗尔机房](https://vps123.top/digitalocean-facilities.html#bangalore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的印度-班加罗尔机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180918-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Digital Ocean印度-班加罗尔机房的PING测试结果，连通概况如下：大陆31个省市的1339个有效测试样本中，共有超时点10个；响应均值为341毫秒，最快的三地区为广西、上海、北京，最慢的三地区为西藏、宁夏、青海；江苏、浙江、广东、山西、陕西有响应超时情况；青海、西藏丢包率较高。海外16个国家地区的75个有效测试样本中，无超时点；响应均值为202毫秒，最快的三地区为新加坡、马来西亚、香港，最慢的三地区为韩国、澳大利亚、赞比亚；菲律宾、赞比亚丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_india-bangalore_20180918_mainland.png)

大陆各省份到Digital Ocean印度-班加罗尔机房的测速数据 [20180918] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
广西 | 55个 | 0 | 301ms | 0.4% | 山西 | 48个 | 1个 | 339ms | 0  
上海 | 8个 | 0 | 304ms | 0 | 均值 | 1339个 | 10个 | 341ms | 1.1%  
北京 | 8个 | 0 | 316ms | 0.1% | 云南 | 26个 | 0 | 342ms | 0.9%  
浙江 | 63个 | 2个 | 319ms | 1.3% | 陕西 | 42个 | 1个 | 344ms | 0.4%  
天津 | 6个 | 0 | 323ms | 0 | 河北 | 56个 | 0 | 350ms | 0  
江西 | 39个 | 0 | 324ms | 2.9% | 福建 | 46个 | 0 | 352ms | 1.1%  
重庆 | 7个 | 0 | 324ms | 0.2% | 黑龙江 | 52个 | 0 | 355ms | 0.3%  
辽宁 | 57个 | 0 | 325ms | 0.8% | 四川 | 69个 | 0 | 363ms | 1.2%  
江苏 | 85个 | 4个 | 329ms | 1.4% | 海南 | 13个 | 0 | 363ms | 0.5%  
湖南 | 67个 | 0 | 330ms | 0.5% | 贵州 | 39个 | 0 | 365ms | 3.1%  
广东 | 111个 | 2个 | 333ms | 1.1% | 吉林 | 22个 | 0 | 369ms | 0.7%  
河南 | 79个 | 0 | 335ms | 0.1% | 甘肃 | 32个 | 0 | 376ms | 1.5%  
山东 | 88个 | 0 | 335ms | 0 | 新疆 | 34个 | 0 | 391ms | 0.5%  
湖北 | 49个 | 0 | 335ms | 0 | 西藏 | 4个 | 0 | 407ms | 6.6%  
安徽 | 69个 | 0 | 335ms | 4.6% | 宁夏 | 7个 | 0 | 422ms | 0.4%  
内蒙古 | 53个 | 0 | 338ms | 0.6% | 青海 | 5个 | 0 | 461ms | 17.3%  
  
简评：如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有1339个，其中超时点10个，平均响应时间为341毫秒，丢包率为1%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：超过300毫秒的31个；  
丢包率较高的省份：青海；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_india-bangalore_20180918_overseas.png)

海外线路到Digital Ocean印度-班加罗尔机房的测速数据 [20180918] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
新加坡 | 5个 | 0 | 86ms | 0 | 俄罗斯 | 1个 | 0 | 204ms | -  
马来西亚 | 3个 | 0 | 96ms | 0 | 美国 | 15个 | 0 | 214ms | 0  
香港 | 19个 | 0 | 151ms | 0 | 加拿大 | 2个 | 0 | 227ms | -  
意大利 | 1个 | 0 | 164ms | - | 越南 | 2个 | 0 | 246ms | 0  
日本 | 3个 | 0 | 174ms | 0 | 荷兰 | 1个 | 0 | 251ms | 0  
台湾 | 2个 | 0 | 176ms | 0 | 韩国 | 12个 | 0 | 253ms | 0  
德国 | 3个 | 0 | 182ms | 0 | 澳大利亚 | 2个 | 0 | 287ms | 0  
菲律宾 | 2个 | 0 | 200ms | 8.3% | 赞比亚 | 2个 | 0 | 326ms | 7.2%  
均值 | 75个 | 0 | 202ms | 1.2% |  |  |  |  |   
  
简评：如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有75个，其中超时点0个，平均响应时间为202毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50-100毫秒间的2个，在100-200毫秒间的6个，在200-300毫秒间的7个，超过300毫秒的1个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180918 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180918 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180918-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
    * [法兰克福](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
    * [伦敦](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
    * [纽约](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")
    * [新加坡](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
    * [多伦多](/digitalocean/idc/toronto/20180918-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180918")
  * 到Digital Ocean班加罗尔机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/bangalore/20180514-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/bangalore/20180527-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/bangalore/20180622-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/bangalore/20180804-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180804")



本文最初发表于[多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-digitalocean-idc-bangalore.html)
