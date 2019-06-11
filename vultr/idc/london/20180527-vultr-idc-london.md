#  多地到Vultr伦敦[London]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr伦敦\[London\]机房的Ping测试（20180527）](/images/thumbnails/to_vultr_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[英国-伦敦机房](https://vps123.top/vultr-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180527-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的964个有效测试样本中，共有超时点5个；响应均值为320毫秒，最快的三地区为上海、辽宁、内蒙古，最慢的三地区为黑龙江、吉林、新疆；河南、山东、江苏、北京、湖南有响应超时情况；辽宁、湖南、新疆、贵州、重庆等21处丢包率较高。海外21个国家地区的88个有效测试样本中，共有超时点1个；响应均值为171毫秒，最快的三地区为意大利、法国、荷兰，最慢的三地区为韩国、澳大利亚、柬埔寨；韩国有响应超时情况；柬埔寨、香港丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_uk-london_20180527_mainland.png)

大陆各省份到Vultr英国-伦敦机房的测速数据 [20180527] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 7个 | 0 | 264ms | 2.0% | 湖北 | 46个 | 0 | 321ms | 6.2%  
辽宁 | 42个 | 0 | 288ms | 19.2% | 贵州 | 28个 | 0 | 323ms | 9.0%  
内蒙古 | 32个 | 0 | 291ms | 3.4% | 江西 | 25个 | 0 | 323ms | 5.7%  
青海 | 4个 | 0 | 297ms | 6.5% | 福建 | 30个 | 0 | 325ms | 7.2%  
宁夏 | 13个 | 0 | 299ms | 5.4% | 云南 | 20个 | 0 | 326ms | 6.0%  
浙江 | 50个 | 0 | 301ms | 1.8% | 北京 | 8个 | 1个 | 326ms | 2.4%  
天津 | 4个 | 0 | 308ms | 3.5% | 甘肃 | 22个 | 0 | 330ms | 4.9%  
广东 | 73个 | 0 | 312ms | 5.7% | 山西 | 40个 | 0 | 330ms | 7.6%  
河北 | 34个 | 0 | 313ms | 4.4% | 陕西 | 33个 | 0 | 332ms | 5.1%  
海南 | 14个 | 0 | 313ms | 5.4% | 四川 | 47个 | 0 | 333ms | 6.9%  
河南 | 58个 | 1个 | 315ms | 6.6% | 重庆 | 15个 | 0 | 333ms | 8.3%  
安徽 | 38个 | 0 | 316ms | 5.6% | 湖南 | 45个 | 1个 | 333ms | 11.3%  
山东 | 53个 | 1个 | 318ms | 6.2% | 黑龙江 | 38个 | 0 | 338ms | 7.0%  
江苏 | 61个 | 1个 | 318ms | 5.0% | 吉林 | 18个 | 0 | 340ms | 2.6%  
广西 | 38个 | 0 | 320ms | 8.0% | 新疆 | 28个 | 0 | 372ms | 9.3%  
均值 | 964个 | 5个 | 320ms | 6.7% |  |  |  |  |   
  
简评：如果你考虑在Vultr的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有964个，其中超时点5个，平均响应时间为320毫秒，丢包率为6%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的5个，超过300毫秒的25个；  
超时点较多的省份：北京；  
丢包率较高的省份：辽宁、湖南；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_uk-london_20180527_overseas.png)

海外线路到Vultr英国-伦敦机房的测速数据 [20180527] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
意大利 | 1个 | 0 | 4ms | - | 巴西 | 1个 | 0 | 190ms | 0  
法国 | 1个 | 0 | 7ms | 0 | 马来西亚 | 5个 | 0 | 211ms | 0.2%  
荷兰 | 1个 | 0 | 7ms | 0 | 香港 | 19个 | 0 | 228ms | 8.3%  
英国 | 2个 | 0 | 18ms | 0 | 菲律宾 | 1个 | 0 | 228ms | 1.0%  
德国 | 2个 | 0 | 20ms | 0 | 印度尼西亚 | 1个 | 0 | 228ms | 0  
加拿大 | 4个 | 0 | 83ms | 0 | 日本 | 2个 | 0 | 250ms | 1.0%  
俄罗斯 | 1个 | 0 | 102ms | 0 | 越南 | 2个 | 0 | 255ms | 0.5%  
美国 | 21个 | 0 | 134ms | 0.6% | 台湾 | 1个 | 0 | 276ms | -  
新加坡 | 6个 | 0 | 169ms | 0 | 韩国 | 12个 | 1个 | 286ms | 0.6%  
均值 | 88个 | 1个 | 171ms | 1.6% | 澳大利亚 | 2个 | 0 | 291ms | 0  
南非 | 2个 | 0 | 184ms | 1.5% | 柬埔寨 | 1个 | 0 | 426ms | 17.0%  
  
简评：如果你考虑在Vultr的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有88个，其中超时点1个，平均响应时间为171毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的9个，超过300毫秒的1个；  
丢包率较高的国家/地区：柬埔寨；

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
    * [洛杉矶](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [迈阿密](/vultr/idc/miami/20180527-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180527")
    * [新泽西](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [巴黎](/vultr/idc/paris/20180527-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180527")
    * [西雅图](/vultr/idc/seattle/20180527-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180527")
    * [硅谷](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [新加坡](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")
    * [悉尼](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [东京](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
  * 到Vultr伦敦机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/london/20180514-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180514")
    * [20180622](/vultr/idc/london/20180622-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180622")
    * [20180804](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")
    * [20180918](/vultr/idc/london/20180918-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180527-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [Linode](/linode/idc/london/20180527-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180527")



本文最初发表于[多地到Vultr伦敦[London]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-vultr-idc-london.html)
