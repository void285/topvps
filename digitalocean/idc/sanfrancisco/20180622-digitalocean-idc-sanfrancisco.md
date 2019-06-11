#  多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean旧金山\[SanFrancisco\]机房的Ping测试（20180622）](/images/thumbnails/to_do_SanFrancisco.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-旧金山机房](https://vps123.top/digitalocean-facilities.html#sanfrancisco)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-旧金山机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180622-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的1755个有效测试样本中，共有超时点48个；响应均值为233毫秒，最快的三地区为北京、河南、天津，最慢的三地区为青海、新疆、香港；云南、浙江、河南、江苏、新疆等16处有响应超时情况；贵州丢包率较高。海外19个国家地区的127个有效测试样本中，无超时点；响应均值为159毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为印度尼西亚、马来西亚、柬埔寨。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_usa-sanfrancisco_20180622_mainland.png)

大陆各省份到Digital Ocean美国-旧金山机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 20个 | 0 | 202ms | 2.6% | 贵州 | 44个 | 2个 | 234ms | 5.2%  
河南 | 98个 | 3个 | 208ms | 4.0% | 湖北 | 69个 | 0 | 234ms | 1.5%  
天津 | 6个 | 0 | 210ms | 0.2% | 陕西 | 53个 | 2个 | 235ms | 2.5%  
上海 | 15个 | 2个 | 212ms | 4.1% | 内蒙古 | 68个 | 1个 | 235ms | 1.7%  
海南 | 19个 | 0 | 215ms | 3.2% | 江西 | 47个 | 1个 | 236ms | 1.9%  
福建 | 61个 | 1个 | 220ms | 1.6% | 重庆 | 24个 | 0 | 237ms | 3.1%  
河北 | 63个 | 0 | 223ms | 1.5% | 辽宁 | 68个 | 1个 | 237ms | 2.6%  
湖南 | 74个 | 0 | 226ms | 1.5% | 吉林 | 26个 | 0 | 240ms | 0.7%  
江苏 | 127个 | 3个 | 227ms | 4.5% | 黑龙江 | 52个 | 1个 | 242ms | 2.4%  
广东 | 145个 | 2个 | 228ms | 3.2% | 宁夏 | 28个 | 0 | 247ms | 1.0%  
山西 | 69个 | 0 | 228ms | 2.6% | 四川 | 79个 | 0 | 264ms | 1.9%  
山东 | 76个 | 0 | 229ms | 2.3% | 云南 | 44个 | 19个 | 264ms | 1.9%  
浙江 | 102个 | 4个 | 229ms | 2.2% | 甘肃 | 34个 | 0 | 267ms | 1.0%  
广西 | 86个 | 1个 | 229ms | 2.5% | 青海 | 10个 | 0 | 270ms | 0.4%  
安徽 | 73个 | 2个 | 231ms | 3.4% | 新疆 | 42个 | 3个 | 273ms | 3.0%  
均值 | 1755个 | 48个 | 233ms | 2.5% | 香港 | 33个 | 0 | - | -  
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有1755个，其中超时点48个，平均响应时间为233毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的30个；  
超时点较多的省份：上海、云南；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_usa-sanfrancisco_20180622_overseas.png)

海外线路到Digital Ocean美国-旧金山机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 28个 | 0 | 36ms | 0.1% | 均值 | 127个 | 0 | 159ms | 0.5%  
加拿大 | 3个 | 0 | 79ms | 0 | 巴西 | 2个 | 0 | 163ms | 0  
日本 | 3个 | 0 | 119ms | 4.0% | 韩国 | 20个 | 0 | 168ms | 0.1%  
南非 | 3个 | 0 | 130ms | 0.3% | 澳大利亚 | 2个 | 0 | 170ms | 0  
台湾 | 2个 | 0 | 132ms | 0 | 英国 | 3个 | 0 | 173ms | 0  
新加坡 | 7个 | 0 | 134ms | 0 | 菲律宾 | 4个 | 0 | 181ms | 0.5%  
香港 | 33个 | 0 | 136ms | 0 | 越南 | 4个 | 0 | 187ms | 0  
德国 | 1个 | 0 | 144ms | - | 印度尼西亚 | 1个 | 0 | 204ms | 0  
意大利 | 1个 | 0 | 151ms | - | 马来西亚 | 6个 | 0 | 264ms | 3.2%  
法国 | 2个 | 0 | 153ms | 0 | 柬埔寨 | 2个 | 0 | 309ms | 0  
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有127个，其中超时点0个，平均响应时间为159毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的14个，在200-300毫秒间的2个，超过300毫秒的1个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180622 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180622 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180622-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180622")
    * [班加罗尔](/digitalocean/idc/bangalore/20180622-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180622")
    * [法兰克福](/digitalocean/idc/frankfurt/20180622-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [伦敦](/digitalocean/idc/london/20180622-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [纽约](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [新加坡](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [多伦多](/digitalocean/idc/toronto/20180622-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180622")
  * 到Digital Ocean旧金山机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [20180804](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-digitalocean-idc-sanfrancisco.html)
