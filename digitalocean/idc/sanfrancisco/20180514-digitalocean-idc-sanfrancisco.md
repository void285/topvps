#  多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean旧金山\[SanFrancisco\]机房的Ping测试（20180514）](/images/thumbnails/to_do_SanFrancisco.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-旧金山机房](https://vps123.top/digitalocean-facilities.html#sanfrancisco)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-旧金山机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180514-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Digital Ocean美国-旧金山机房的PING测试结果，连通概况如下：大陆31个省市的1939个有效测试样本中，共有超时点26个；响应均值为238毫秒，最快的三地区为北京、河南、山西，最慢的三地区为新疆、青海、西藏；浙江、广东、江苏、北京、福建等12处有响应超时情况；上海、云南、山东、安徽、浙江等8处丢包率较高。海外19个国家地区的161个有效测试样本中，共有超时点3个；响应均值为182毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为印度尼西亚、南非、柬埔寨；香港有响应超时情况；柬埔寨丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_usa-sanfrancisco_20180514_mainland.png)

大陆各省份到Digital Ocean美国-旧金山机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 15个 | 2个 | 201ms | 0.4% | 辽宁 | 78个 | 0 | 238ms | 5.8%  
河南 | 113个 | 0 | 212ms | 2.4% | 均值 | 1939个 | 26个 | 238ms | 4.1%  
山西 | 77个 | 0 | 216ms | 1.4% | 广东 | 153个 | 3个 | 240ms | 3.4%  
陕西 | 67个 | 1个 | 227ms | 2.4% | 上海 | 16个 | 0 | 240ms | 8.9%  
河北 | 65个 | 0 | 227ms | 2.7% | 江苏 | 123个 | 3个 | 241ms | 6.8%  
福建 | 73个 | 2个 | 228ms | 2.2% | 浙江 | 96个 | 5个 | 242ms | 6.9%  
海南 | 22个 | 0 | 228ms | 3.7% | 内蒙古 | 70个 | 0 | 244ms | 2.8%  
山东 | 101个 | 2个 | 229ms | 7.6% | 贵州 | 55个 | 2个 | 247ms | 6.0%  
湖南 | 93个 | 0 | 230ms | 1.7% | 湖北 | 90个 | 1个 | 252ms | 4.6%  
江西 | 46个 | 0 | 231ms | 2.3% | 甘肃 | 43个 | 0 | 254ms | 2.5%  
安徽 | 81个 | 0 | 232ms | 7.3% | 四川 | 96个 | 0 | 261ms | 3.5%  
天津 | 10个 | 0 | 233ms | 3.1% | 重庆 | 29个 | 2个 | 265ms | 3.6%  
广西 | 72个 | 1个 | 233ms | 3.2% | 云南 | 54个 | 2个 | 267ms | 8.7%  
黑龙江 | 79个 | 0 | 235ms | 2.1% | 新疆 | 56个 | 0 | 269ms | 3.5%  
吉林 | 33个 | 0 | 236ms | 3.5% | 青海 | 8个 | 0 | 270ms | 2.8%  
宁夏 | 23个 | 0 | 237ms | 2.1% | 西藏 | 2个 | 0 | 289ms | 0  
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有1939个，其中超时点26个，平均响应时间为238毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的31个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_usa-sanfrancisco_20180514_overseas.png)

海外线路到Digital Ocean美国-旧金山机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 36个 | 0 | 19ms | 1.3% | 澳大利亚 | 4个 | 0 | 171ms | 0.3%  
加拿大 | 6个 | 0 | 75ms | 0.5% | 巴西 | 1个 | 0 | 172ms | 0  
日本 | 4个 | 0 | 119ms | 0 | 新加坡 | 12个 | 0 | 182ms | 0  
韩国 | 26个 | 0 | 141ms | 0 | 均值 | 161个 | 3个 | 182ms | 1.2%  
荷兰 | 2个 | 0 | 146ms | 0 | 菲律宾 | 2个 | 0 | 184ms | 0.5%  
法国 | 4个 | 0 | 155ms | 0 | 马来西亚 | 6个 | 0 | 206ms | 0.2%  
台湾 | 2个 | 0 | 157ms | - | 俄罗斯 | 2个 | 0 | 248ms | 0  
英国 | 4个 | 0 | 161ms | 0.5% | 印度尼西亚 | 2个 | 0 | 270ms | 4.0%  
香港 | 38个 | 3个 | 163ms | 0 | 南非 | 4个 | 0 | 327ms | 0  
德国 | 4个 | 0 | 167ms | 0 | 柬埔寨 | 2个 | 0 | 393ms | 15.0%  
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有161个，其中超时点3个，平均响应时间为182毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的12个，在200-300毫秒间的3个，超过300毫秒的2个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180514 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180514 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [班加罗尔](/digitalocean/idc/bangalore/20180514-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180514")
    * [法兰克福](/digitalocean/idc/frankfurt/20180514-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [伦敦](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [纽约](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [新加坡](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [多伦多](/digitalocean/idc/toronto/20180514-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180514")
  * 到Digital Ocean旧金山机房的 _其他近期报告_ ： 
    * [20180527](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-digitalocean-idc-sanfrancisco.html)
