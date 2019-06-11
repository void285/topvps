#  多地到Vultr巴黎[Paris]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr巴黎\[Paris\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Paris.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[法国-巴黎机房](https://vps123.top/vultr-facilities.html#paris)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的法国-巴黎机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr法国-巴黎机房的PING测试结果，连通概况如下：大陆31个省市的945个有效测试样本中，共有超时点15个；响应均值为288毫秒，最快的三地区为北京、上海、河北，最慢的三地区为吉林、山东、天津；广东、浙江、广西、重庆、北京等7处有响应超时情况；浙江、天津、江苏、贵州、江西等7处丢包率较高。海外18个国家地区的77个有效测试样本中，共有超时点1个；响应均值为205毫秒，最快的三地区为法国、德国、英国，最慢的三地区为台湾、印度尼西亚、柬埔寨；香港有响应超时情况；柬埔寨、印度尼西亚、南非丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于巴黎\[Paris\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_france-paris_20180514_mainland.png)

大陆各省份到Vultr法国-巴黎机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 8个 | 1个 | 220ms | 1.4% | 云南 | 23个 | 0 | 284ms | 0.6%  
上海 | 8个 | 0 | 229ms | 3.3% | 福建 | 33个 | 0 | 287ms | 4.9%  
河北 | 29个 | 0 | 253ms | 4.1% | 广东 | 78个 | 5个 | 288ms | 1.9%  
甘肃 | 20个 | 0 | 261ms | 0.9% | 均值 | 945个 | 15个 | 288ms | 4.4%  
辽宁 | 37个 | 0 | 263ms | 7.0% | 内蒙古 | 33个 | 0 | 291ms | 3.9%  
广西 | 37个 | 2个 | 264ms | 3.2% | 江苏 | 63个 | 1个 | 292ms | 8.7%  
西藏 | 1个 | 0 | 266ms | 0 | 四川 | 48个 | 0 | 295ms | 2.7%  
河南 | 50个 | 0 | 267ms | 4.9% | 陕西 | 33个 | 0 | 298ms | 2.9%  
青海 | 4个 | 0 | 272ms | 0.5% | 浙江 | 53个 | 3个 | 305ms | 13.1%  
安徽 | 37个 | 0 | 273ms | 1.6% | 贵州 | 27个 | 0 | 307ms | 7.7%  
湖南 | 44个 | 0 | 276ms | 2.1% | 山西 | 38个 | 0 | 307ms | 3.6%  
湖北 | 43个 | 0 | 280ms | 4.8% | 黑龙江 | 39个 | 0 | 313ms | 4.5%  
宁夏 | 12个 | 0 | 281ms | 3.3% | 新疆 | 29个 | 0 | 317ms | 2.5%  
海南 | 11个 | 0 | 281ms | 2.7% | 吉林 | 16个 | 0 | 319ms | 4.4%  
重庆 | 16个 | 2个 | 283ms | 0.9% | 山东 | 49个 | 1个 | 326ms | 5.5%  
江西 | 21个 | 0 | 284ms | 7.1% | 天津 | 5个 | 0 | 329ms | 9.0%  
  
简评：如果你考虑在Vultr的巴黎[Paris]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于巴黎[Paris]的机房的连通状况。到此机房的ping监测点共有945个，其中超时点15个，平均响应时间为288毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的23个，超过300毫秒的8个；  
超时点较多的省份：北京、重庆；  
丢包率较高的省份：浙江；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于巴黎\[Paris\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_france-paris_20180514_overseas.png)

海外线路到Vultr法国-巴黎机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
法国 | 2个 | 0 | 7ms | 4.0% | 菲律宾 | 1个 | 0 | 232ms | 0  
德国 | 2个 | 0 | 22ms | 0 | 马来西亚 | 3个 | 0 | 236ms | 4.0%  
英国 | 2个 | 0 | 26ms | 0 | 日本 | 2个 | 0 | 251ms | 1.0%  
俄罗斯 | 1个 | 0 | 97ms | 0 | 香港 | 19个 | 1个 | 267ms | 0  
加拿大 | 3个 | 0 | 105ms | 0 | 韩国 | 13个 | 0 | 278ms | 0  
美国 | 17个 | 0 | 143ms | 0 | 澳大利亚 | 1个 | 0 | 300ms | 0  
巴西 | 1个 | 0 | 205ms | 0 | 台湾 | 1个 | 0 | 317ms | -  
新加坡 | 6个 | 0 | 205ms | 0 | 印度尼西亚 | 1个 | 0 | 336ms | 13.0%  
均值 | 77个 | 1个 | 205ms | 3.9% | 柬埔寨 | 1个 | 0 | 449ms | 39.0%  
南非 | 1个 | 0 | 217ms | 6.0% |  |  |  |  |   
  
简评：如果你考虑在Vultr的巴黎[Paris]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于巴黎[Paris]的机房的连通状况。到此机房的ping监测点共有77个，其中超时点1个，平均响应时间为205毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的1个，在100-200毫秒间的2个，在200-300毫秒间的9个，超过300毫秒的3个；  
丢包率较高的国家/地区：印度尼西亚、柬埔寨；

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
    * [西雅图](/vultr/idc/seattle/20180514-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180514")
    * [硅谷](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr巴黎机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/paris/20180527-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180527")
    * [20180622](/vultr/idc/paris/20180622-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180622")
    * [20180804](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [20180918](/vultr/idc/paris/20180918-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180918")



本文最初发表于[多地到Vultr巴黎[Paris]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-paris.html)
