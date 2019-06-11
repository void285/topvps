#  多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean旧金山\[SanFrancisco\]机房的Ping测试（20180527）](/images/thumbnails/to_do_SanFrancisco.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-旧金山机房](https://vps123.top/digitalocean-facilities.html#sanfrancisco)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-旧金山机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180527-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的1964个有效测试样本中，共有超时点28个；响应均值为223毫秒，最快的三地区为上海、河南、北京，最慢的三地区为甘肃、青海、新疆；河南、山东、浙江、江苏、北京等12处有响应超时情况；湖南、宁夏丢包率较高。海外21个国家地区的171个有效测试样本中，共有超时点2个；响应均值为171毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为俄罗斯、菲律宾、南非；香港有响应超时情况。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_usa-sanfrancisco_20180527_mainland.png)

大陆各省份到Digital Ocean美国-旧金山机房的测速数据 [20180527] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 16个 | 0 | 195ms | 3.3% | 安徽 | 78个 | 1个 | 224ms | 3.2%  
河南 | 118个 | 6个 | 204ms | 1.8% | 宁夏 | 24个 | 0 | 226ms | 5.7%  
北京 | 16个 | 2个 | 209ms | 1.4% | 辽宁 | 77个 | 1个 | 226ms | 4.1%  
海南 | 28个 | 0 | 210ms | 3.6% | 湖北 | 84个 | 0 | 227ms | 3.2%  
山东 | 108个 | 4个 | 212ms | 1.6% | 陕西 | 65个 | 1个 | 227ms | 4.0%  
河北 | 70个 | 0 | 216ms | 2.4% | 重庆 | 29个 | 1个 | 227ms | 2.5%  
广东 | 162个 | 2个 | 217ms | 3.2% | 黑龙江 | 78个 | 0 | 228ms | 2.7%  
广西 | 78个 | 0 | 217ms | 3.9% | 吉林 | 37个 | 0 | 228ms | 3.3%  
贵州 | 55个 | 0 | 218ms | 3.0% | 云南 | 44个 | 2个 | 234ms | 3.3%  
山西 | 77个 | 0 | 218ms | 2.1% | 内蒙古 | 68个 | 0 | 235ms | 2.8%  
湖南 | 89个 | 2个 | 219ms | 6.1% | 四川 | 98个 | 0 | 236ms | 3.4%  
江西 | 46个 | 0 | 220ms | 0.8% | 天津 | 10个 | 0 | 239ms | 2.8%  
浙江 | 102个 | 3个 | 221ms | 2.3% | 甘肃 | 46个 | 0 | 246ms | 3.7%  
福建 | 72个 | 0 | 222ms | 3.7% | 青海 | 6个 | 0 | 251ms | 2.3%  
均值 | 1964个 | 28个 | 223ms | 3.1% | 新疆 | 54个 | 0 | 265ms | 3.9%  
江苏 | 129个 | 3个 | 224ms | 3.5% |  |  |  |  |   
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有1964个，其中超时点28个，平均响应时间为223毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的1个，在200-300毫秒间的29个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/do_20180527/plot_idc_do_usa-sanfrancisco_20180527_overseas.png)

海外线路到Digital Ocean美国-旧金山机房的测速数据 [20180527] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 42个 | 0 | 18ms | 0.7% | 巴西 | 2个 | 0 | 171ms | 0  
加拿大 | 8个 | 0 | 77ms | 0 | 澳大利亚 | 3个 | 0 | 171ms | 0.7%  
日本 | 2个 | 0 | 101ms | 0 | 均值 | 171个 | 2个 | 171ms | 0.1%  
意大利 | 2个 | 0 | 140ms | - | 新加坡 | 10个 | 0 | 181ms | 0  
荷兰 | 2个 | 0 | 145ms | 0 | 越南 | 4个 | 0 | 182ms | 0.3%  
台湾 | 2个 | 0 | 146ms | - | 印度尼西亚 | 2个 | 0 | 210ms | 0  
韩国 | 24个 | 0 | 148ms | 0 | 马来西亚 | 8个 | 0 | 212ms | 0  
法国 | 2个 | 0 | 155ms | 0 | 柬埔寨 | 2个 | 0 | 228ms | 0  
德国 | 6个 | 0 | 159ms | 0 | 俄罗斯 | 2个 | 0 | 239ms | 0  
香港 | 38个 | 2个 | 165ms | 0 | 菲律宾 | 2个 | 0 | 250ms | 0  
英国 | 4个 | 0 | 167ms | 0 | 南非 | 4个 | 0 | 324ms | 0.8%  
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有171个，其中超时点2个，平均响应时间为171毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的13个，在200-300毫秒间的5个，超过300毫秒的1个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180527 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180527 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180527-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180527")
    * [班加罗尔](/digitalocean/idc/bangalore/20180527-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180527")
    * [法兰克福](/digitalocean/idc/frankfurt/20180527-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [伦敦](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [纽约](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [新加坡](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [多伦多](/digitalocean/idc/toronto/20180527-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180527")
  * 到Digital Ocean旧金山机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [20180622](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-digitalocean-idc-sanfrancisco.html)
