#  多地到Vultr伦敦[London]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr伦敦\[London\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[英国-伦敦机房](https://vps123.top/vultr-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr英国-伦敦机房的PING测试结果，连通概况如下：大陆31个省市的947个有效测试样本中，共有超时点20个；响应均值为321毫秒，最快的三地区为宁夏、上海、天津，最慢的三地区为四川、西藏、河北；广东、浙江、江苏、福建、北京等13处有响应超时情况；湖北、浙江、江苏、河北、江西等11处丢包率较高。海外18个国家地区的78个有效测试样本中，共有超时点1个；响应均值为187毫秒，最快的三地区为法国、英国、德国，最慢的三地区为韩国、澳大利亚、柬埔寨；美国有响应超时情况；柬埔寨丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_uk-london_20180514_mainland.png)

大陆各省份到Vultr英国-伦敦机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
宁夏 | 11个 | 0 | 270ms | 2.4% | 黑龙江 | 38个 | 1个 | 320ms | 5.3%  
上海 | 7个 | 0 | 280ms | 2.4% | 广西 | 36个 | 1个 | 320ms | 1.6%  
天津 | 5个 | 0 | 285ms | 4.6% | 均值 | 947个 | 20个 | 321ms | 7.0%  
北京 | 8个 | 1个 | 288ms | 0 | 青海 | 3个 | 0 | 326ms | 0.3%  
内蒙古 | 34个 | 0 | 291ms | 5.3% | 浙江 | 51个 | 3个 | 326ms | 16.7%  
山东 | 52个 | 1个 | 302ms | 4.2% | 海南 | 12个 | 0 | 326ms | 4.8%  
辽宁 | 37个 | 0 | 304ms | 5.0% | 湖北 | 47个 | 0 | 331ms | 23.1%  
江苏 | 57个 | 2个 | 305ms | 14.3% | 河南 | 57个 | 0 | 332ms | 7.7%  
安徽 | 37个 | 1个 | 311ms | 8.1% | 吉林 | 14个 | 0 | 339ms | 3.3%  
山西 | 36个 | 1个 | 313ms | 7.7% | 福建 | 35个 | 2个 | 340ms | 5.0%  
湖南 | 45个 | 1个 | 314ms | 2.8% | 贵州 | 28个 | 0 | 341ms | 7.3%  
广东 | 75个 | 4个 | 315ms | 3.8% | 新疆 | 28个 | 0 | 341ms | 1.3%  
陕西 | 31个 | 0 | 316ms | 1.9% | 重庆 | 15个 | 1个 | 349ms | 1.2%  
甘肃 | 22个 | 0 | 317ms | 1.5% | 四川 | 48个 | 1个 | 351ms | 3.2%  
江西 | 22个 | 0 | 318ms | 12.8% | 西藏 | 1个 | 0 | 365ms | 0  
云南 | 23个 | 0 | 319ms | 4.5% | 河北 | 32个 | 0 | 373ms | 14.0%  
  
简评：如果你考虑在Vultr的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有947个，其中超时点20个，平均响应时间为321毫秒，丢包率为7%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的5个，超过300毫秒的26个；  
超时点较多的省份：北京；  
丢包率较高的省份：江苏、江西、浙江、湖北、河北；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_uk-london_20180514_overseas.png)

海外线路到Vultr英国-伦敦机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
法国 | 2个 | 0 | 7ms | 0 | 南非 | 1个 | 0 | 217ms | 0  
英国 | 2个 | 0 | 17ms | 0 | 菲律宾 | 1个 | 0 | 220ms | 0  
德国 | 2个 | 0 | 26ms | 0 | 印度尼西亚 | 1个 | 0 | 222ms | 2.0%  
加拿大 | 3个 | 0 | 85ms | 0.5% | 香港 | 18个 | 0 | 227ms | 0  
俄罗斯 | 1个 | 0 | 106ms | 0 | 日本 | 2个 | 0 | 244ms | 3.0%  
美国 | 19个 | 1个 | 132ms | 3.7% | 台湾 | 1个 | 0 | 263ms | -  
新加坡 | 6个 | 0 | 167ms | 0 | 韩国 | 13个 | 0 | 277ms | 0  
均值 | 78个 | 1个 | 187ms | 2.3% | 澳大利亚 | 1个 | 0 | 294ms | 0  
巴西 | 1个 | 0 | 197ms | 0 | 柬埔寨 | 1个 | 0 | 454ms | 30.0%  
马来西亚 | 3个 | 0 | 212ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Vultr的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点1个，平均响应时间为187毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的1个，在100-200毫秒间的4个，在200-300毫秒间的9个，超过300毫秒的1个；  
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
    * [洛杉矶](/vultr/idc/losangeles/20180514-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180514")
    * [迈阿密](/vultr/idc/miami/20180514-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180514")
    * [新泽西](/vultr/idc/newjersey/20180514-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180514")
    * [巴黎](/vultr/idc/paris/20180514-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180514")
    * [西雅图](/vultr/idc/seattle/20180514-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180514")
    * [硅谷](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr伦敦机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")
    * [20180622](/vultr/idc/london/20180622-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180622")
    * [20180804](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")
    * [20180918](/vultr/idc/london/20180918-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180514-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [Linode](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")



本文最初发表于[多地到Vultr伦敦[London]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-london.html)
