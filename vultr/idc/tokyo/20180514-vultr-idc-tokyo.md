#  多地到Vultr东京[Tokyo]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr东京\[Tokyo\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[日本-东京机房](https://vps123.top/vultr-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr日本-东京机房的PING测试结果，连通概况如下：大陆31个省市的941个有效测试样本中，共有超时点16个；响应均值为139毫秒，最快的三地区为福建、上海、海南，最慢的三地区为西藏、新疆、河北；福建、江苏、浙江、湖北、山东等11处有响应超时情况；河北、天津、吉林、山东、山西等23处丢包率较高。海外18个国家地区的77个有效测试样本中，无超时点；响应均值为171毫秒，最快的三地区为日本、台湾、韩国，最慢的三地区为柬埔寨、俄罗斯、南非；柬埔寨丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_japan-tokyo_20180514_mainland.png)

大陆各省份到Vultr日本-东京机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
福建 | 35个 | 2个 | 94ms | 3.8% | 江西 | 20个 | 0 | 134ms | 11.0%  
上海 | 7个 | 0 | 96ms | 9.1% | 均值 | 941个 | 16个 | 139ms | 10.3%  
海南 | 10个 | 0 | 98ms | 3.3% | 辽宁 | 37个 | 1个 | 140ms | 13.9%  
湖南 | 45个 | 0 | 100ms | 3.1% | 湖北 | 48个 | 2个 | 142ms | 14.5%  
广西 | 34个 | 0 | 107ms | 5.4% | 重庆 | 15个 | 0 | 143ms | 3.7%  
贵州 | 27个 | 0 | 114ms | 5.5% | 陕西 | 33个 | 1个 | 144ms | 13.0%  
安徽 | 41个 | 0 | 116ms | 7.4% | 四川 | 46个 | 0 | 148ms | 11.8%  
宁夏 | 12个 | 0 | 120ms | 6.5% | 山东 | 50个 | 2个 | 161ms | 15.7%  
广东 | 81个 | 1个 | 121ms | 5.4% | 河南 | 51个 | 1个 | 162ms | 12.4%  
江苏 | 64个 | 2个 | 122ms | 8.6% | 山西 | 32个 | 0 | 163ms | 15.6%  
云南 | 20个 | 0 | 123ms | 4.3% | 内蒙古 | 33个 | 0 | 164ms | 14.9%  
青海 | 3个 | 0 | 125ms | 1.3% | 黑龙江 | 38个 | 0 | 168ms | 15.1%  
北京 | 7个 | 1个 | 126ms | 10.0% | 吉林 | 16个 | 0 | 170ms | 18.3%  
浙江 | 53个 | 2个 | 131ms | 7.3% | 西藏 | 1个 | 0 | 176ms | 0  
天津 | 5个 | 0 | 132ms | 18.5% | 新疆 | 25个 | 1个 | 183ms | 10.3%  
甘肃 | 21个 | 0 | 133ms | 4.8% | 河北 | 31个 | 0 | 222ms | 23.6%  
  
简评：如果你考虑在Vultr的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有941个，其中超时点16个，平均响应时间为139毫秒，丢包率为10%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50-100毫秒间的4个，在100-200毫秒间的26个，在200-300毫秒间的1个；  
超时点较多的省份：北京；  
丢包率较高的省份：北京、天津、江西、辽宁、湖北、陕西、四川、山东、河南、山西、内蒙古、黑龙江、吉林、新疆、河北；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_japan-tokyo_20180514_overseas.png)

海外线路到Vultr日本-东京机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
日本 | 2个 | 0 | 12ms | 3.5% | 澳大利亚 | 1个 | 0 | 185ms | 0  
台湾 | 1个 | 0 | 41ms | - | 印度尼西亚 | 1个 | 0 | 205ms | 5.0%  
韩国 | 13个 | 0 | 48ms | 1.4% | 英国 | 2个 | 0 | 241ms | 0  
香港 | 18个 | 0 | 58ms | 0 | 法国 | 2个 | 0 | 244ms | 0  
菲律宾 | 1个 | 0 | 69ms | 0 | 德国 | 1个 | 0 | 259ms | 1.0%  
新加坡 | 6个 | 0 | 91ms | 0 | 巴西 | 1个 | 0 | 263ms | 0  
马来西亚 | 3个 | 0 | 103ms | 0 | 柬埔寨 | 1个 | 0 | 265ms | 29.0%  
美国 | 19个 | 0 | 118ms | 0 | 俄罗斯 | 1个 | 0 | 268ms | 0  
加拿大 | 3个 | 0 | 161ms | 0.5% | 南非 | 1个 | 0 | 444ms | 0  
均值 | 77个 | 0 | 171ms | 2.4% |  |  |  |  |   
  
简评：如果你考虑在Vultr的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有77个，其中超时点0个，平均响应时间为171毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的3个，在100-200毫秒间的4个，在200-300毫秒间的7个，超过300毫秒的1个；  
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
    * [硅谷](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
  * 到Vultr东京机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
    * [20180622](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
    * [20180804](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
    * [20180918](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")



本文最初发表于[多地到Vultr东京[Tokyo]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-tokyo.html)
