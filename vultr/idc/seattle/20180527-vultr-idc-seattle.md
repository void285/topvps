#  多地到Vultr西雅图[Seattle]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr西雅图\[Seattle\]机房的Ping测试（20180527）](/images/thumbnails/to_vultr_Seattle.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-西雅图机房](https://vps123.top/vultr-facilities.html#seattle)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-西雅图机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180527-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的970个有效测试样本中，共有超时点12个；响应均值为231毫秒，最快的三地区为河南、山西、浙江，最慢的三地区为甘肃、青海、新疆；河南、江苏、浙江、山东、陕西等9处有响应超时情况；山东、吉林、河北、黑龙江、山西等29处丢包率较高。海外21个国家地区的87个有效测试样本中，无超时点；响应均值为173毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为印度尼西亚、柬埔寨、南非。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于西雅图\[Seattle\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_usa-seattle_20180527_mainland.png)

大陆各省份到Vultr美国-西雅图机房的测速数据 [20180527] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
河南 | 56个 | 3个 | 213ms | 11.8% | 江西 | 23个 | 0 | 235ms | 8.0%  
山西 | 37个 | 0 | 214ms | 12.6% | 黑龙江 | 39个 | 0 | 235ms | 12.7%  
浙江 | 51个 | 1个 | 216ms | 5.9% | 云南 | 20个 | 0 | 241ms | 7.0%  
广东 | 79个 | 0 | 217ms | 6.4% | 贵州 | 27个 | 0 | 242ms | 10.9%  
山东 | 51个 | 1个 | 218ms | 14.4% | 湖北 | 45个 | 1个 | 242ms | 8.0%  
海南 | 14个 | 0 | 219ms | 6.6% | 内蒙古 | 33个 | 0 | 242ms | 10.8%  
陕西 | 35个 | 1个 | 221ms | 12.3% | 重庆 | 13个 | 0 | 244ms | 6.7%  
湖南 | 43个 | 0 | 221ms | 11.6% | 上海 | 8个 | 0 | 245ms | 3.0%  
广西 | 41个 | 0 | 222ms | 9.2% | 四川 | 45个 | 0 | 247ms | 9.2%  
福建 | 36个 | 0 | 224ms | 8.6% | 宁夏 | 13个 | 0 | 247ms | 10.1%  
北京 | 8个 | 1个 | 224ms | 10.8% | 天津 | 5个 | 0 | 258ms | 12.2%  
河北 | 35个 | 0 | 226ms | 13.7% | 安徽 | 38个 | 1个 | 258ms | 5.2%  
江苏 | 62个 | 2个 | 229ms | 6.8% | 甘肃 | 22个 | 0 | 260ms | 8.2%  
均值 | 970个 | 12个 | 231ms | 9.7% | 青海 | 4个 | 0 | 267ms | 6.8%  
吉林 | 19个 | 1个 | 233ms | 13.9% | 新疆 | 28个 | 0 | 271ms | 10.6%  
辽宁 | 40个 | 0 | 234ms | 10.4% |  |  |  |  |   
  
简评：如果你考虑在Vultr的西雅图[Seattle]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于西雅图[Seattle]的机房的连通状况。到此机房的ping监测点共有970个，其中超时点12个，平均响应时间为231毫秒，丢包率为9%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的30个；  
超时点较多的省份：北京；  
丢包率较高的省份：河南、山西、山东、陕西、湖南、北京、河北、吉林、辽宁、黑龙江、贵州、内蒙古、宁夏、天津、新疆；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于西雅图\[Seattle\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_usa-seattle_20180527_overseas.png)

海外线路到Vultr美国-西雅图机房的测速数据 [20180527] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 21个 | 0 | 31ms | 2.9% | 德国 | 3个 | 0 | 165ms | 0  
加拿大 | 3个 | 0 | 80ms | 0 | 法国 | 1个 | 0 | 166ms | 0  
日本 | 2个 | 0 | 120ms | 1.5% | 巴西 | 1个 | 0 | 173ms | 0  
台湾 | 1个 | 0 | 140ms | - | 均值 | 87个 | 0 | 173ms | 0.6%  
香港 | 19个 | 0 | 143ms | 0 | 澳大利亚 | 2个 | 0 | 192ms | 0  
越南 | 2个 | 0 | 154ms | 0 | 新加坡 | 5个 | 0 | 196ms | 0  
英国 | 2个 | 0 | 156ms | 0 | 马来西亚 | 5个 | 0 | 201ms | 0.2%  
韩国 | 12个 | 0 | 160ms | 0 | 俄罗斯 | 1个 | 0 | 229ms | 0  
荷兰 | 1个 | 0 | 162ms | 0 | 印度尼西亚 | 1个 | 0 | 235ms | 3.0%  
意大利 | 1个 | 0 | 162ms | - | 柬埔寨 | 1个 | 0 | 293ms | 1.0%  
菲律宾 | 1个 | 0 | 163ms | 1.0% | 南非 | 2个 | 0 | 322ms | 1.5%  
  
简评：如果你考虑在Vultr的西雅图[Seattle]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于西雅图[Seattle]的机房的连通状况。到此机房的ping监测点共有87个，其中超时点0个，平均响应时间为173毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的14个，在200-300毫秒间的4个，超过300毫秒的1个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180527 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180527 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180527-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180527")
    * [亚特兰大](/vultr/idc/atlanta/20180527-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180527")
    * [芝加哥](/vultr/idc/chicago/20180527-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180527")
    * [达拉斯](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")
    * [法兰克福](/vultr/idc/frankfurt/20180527-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180527")
    * [伦敦](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")
    * [洛杉矶](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [迈阿密](/vultr/idc/miami/20180527-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180527")
    * [新泽西](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [巴黎](/vultr/idc/paris/20180527-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180527")
    * [硅谷](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [新加坡](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")
    * [悉尼](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [东京](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
  * 到Vultr西雅图机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/seattle/20180514-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180514")
    * [20180622](/vultr/idc/seattle/20180622-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180622")
    * [20180804](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [20180918](/vultr/idc/seattle/20180918-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180918")



本文最初发表于[多地到Vultr西雅图[Seattle]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-vultr-idc-seattle.html)