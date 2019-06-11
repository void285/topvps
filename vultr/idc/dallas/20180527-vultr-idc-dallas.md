#  多地到Vultr达拉斯[Dallas]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr达拉斯\[Dallas\]机房的Ping测试（20180527）](/images/thumbnails/to_vultr_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-达拉斯机房](https://vps123.top/vultr-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180527-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的973个有效测试样本中，共有超时点10个；响应均值为276毫秒，最快的三地区为北京、江苏、吉林，最慢的三地区为甘肃、新疆、青海；江苏、河南、北京、山东、福建等8处有响应超时情况；青海、湖南、新疆、安徽、重庆等26处丢包率较高。海外21个国家地区的87个有效测试样本中，共有超时点1个；响应均值为182毫秒，最快的三地区为美国、加拿大、意大利，最慢的三地区为印度尼西亚、南非、柬埔寨；香港有响应超时情况；柬埔寨、马来西亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_usa-dallas_20180527_mainland.png)

大陆各省份到Vultr美国-达拉斯机房的测速数据 [20180527] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 8个 | 1个 | 234ms | 2.4% | 广西 | 40个 | 0 | 280ms | 15.3%  
江苏 | 63个 | 2个 | 244ms | 2.2% | 重庆 | 15个 | 0 | 284ms | 15.7%  
吉林 | 19个 | 0 | 249ms | 4.3% | 湖南 | 47个 | 1个 | 284ms | 17.2%  
山东 | 52个 | 1个 | 252ms | 12.0% | 内蒙古 | 31个 | 0 | 284ms | 11.7%  
浙江 | 53个 | 0 | 252ms | 3.2% | 江西 | 25个 | 0 | 285ms | 14.8%  
河北 | 34个 | 0 | 258ms | 9.2% | 陕西 | 32个 | 0 | 285ms | 11.8%  
福建 | 35个 | 1个 | 263ms | 9.8% | 贵州 | 25个 | 0 | 287ms | 14.1%  
辽宁 | 41个 | 0 | 263ms | 9.5% | 宁夏 | 13个 | 0 | 288ms | 12.1%  
天津 | 4个 | 0 | 265ms | 13.7% | 四川 | 45个 | 1个 | 290ms | 11.1%  
上海 | 7个 | 0 | 265ms | 7.6% | 黑龙江 | 38个 | 0 | 290ms | 14.8%  
海南 | 14个 | 0 | 271ms | 12.4% | 安徽 | 39个 | 0 | 293ms | 15.8%  
山西 | 40个 | 0 | 272ms | 14.1% | 云南 | 20个 | 0 | 305ms | 15.4%  
河南 | 58个 | 2个 | 273ms | 13.8% | 甘肃 | 22个 | 0 | 311ms | 14.6%  
广东 | 78个 | 0 | 273ms | 13.7% | 新疆 | 29个 | 0 | 335ms | 17.0%  
均值 | 973个 | 10个 | 276ms | 11.9% | 青海 | 3个 | 0 | 345ms | 19.3%  
湖北 | 43个 | 1个 | 280ms | 12.9% |  |  |  |  |   
  
简评：如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有973个，其中超时点10个，平均响应时间为276毫秒，丢包率为11%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的26个，超过300毫秒的4个；  
超时点较多的省份：北京；  
丢包率较高的省份：山东、天津、海南、山西、河南、广东、湖北、广西、重庆、湖南、内蒙古、江西、陕西、贵州、宁夏、四川、黑龙江、安徽、云南、甘肃、新疆、青海；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_idc_vultr_usa-dallas_20180527_overseas.png)

海外线路到Vultr美国-达拉斯机房的测速数据 [20180527] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 21个 | 0 | 34ms | 4.0% | 均值 | 87个 | 1个 | 182ms | 1.5%  
加拿大 | 4个 | 0 | 52ms | 0 | 香港 | 20个 | 1个 | 198ms | 0  
意大利 | 1个 | 0 | 111ms | - | 澳大利亚 | 2个 | 0 | 202ms | 0  
荷兰 | 1个 | 0 | 123ms | 0 | 俄罗斯 | 1个 | 0 | 206ms | 0  
法国 | 1个 | 0 | 126ms | 0 | 新加坡 | 5个 | 0 | 210ms | 0  
德国 | 3个 | 0 | 134ms | 0 | 越南 | 2个 | 0 | 221ms | 0.5%  
巴西 | 1个 | 0 | 135ms | 0 | 菲律宾 | 1个 | 0 | 227ms | 0  
英国 | 2个 | 0 | 138ms | 0 | 马来西亚 | 4个 | 0 | 256ms | 6.3%  
日本 | 2个 | 0 | 157ms | 0.5% | 印度尼西亚 | 1个 | 0 | 260ms | 0  
韩国 | 11个 | 0 | 175ms | 0 | 南非 | 2个 | 0 | 289ms | 1.0%  
台湾 | 1个 | 0 | 181ms | - | 柬埔寨 | 1个 | 0 | 387ms | 17.0%  
  
简评：如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有87个，其中超时点1个，平均响应时间为182毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的10个，在200-300毫秒间的8个，超过300毫秒的1个；  
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
    * [法兰克福](/vultr/idc/frankfurt/20180527-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180527")
    * [伦敦](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")
    * [洛杉矶](/vultr/idc/losangeles/20180527-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180527")
    * [迈阿密](/vultr/idc/miami/20180527-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180527")
    * [新泽西](/vultr/idc/newjersey/20180527-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180527")
    * [巴黎](/vultr/idc/paris/20180527-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180527")
    * [西雅图](/vultr/idc/seattle/20180527-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180527")
    * [硅谷](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [新加坡](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")
    * [悉尼](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [东京](/vultr/idc/tokyo/20180527-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180527")
  * 到Vultr达拉斯机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/dallas/20180514-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180514")
    * [20180622](/vultr/idc/dallas/20180622-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180622")
    * [20180804](/vultr/idc/dallas/20180804-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180804")
    * [20180918](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/dallas/20180527-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180527")



本文最初发表于[多地到Vultr达拉斯[Dallas]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-vultr-idc-dallas.html)
