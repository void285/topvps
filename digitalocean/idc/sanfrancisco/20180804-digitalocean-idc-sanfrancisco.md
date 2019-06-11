#  多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean旧金山\[SanFrancisco\]机房的Ping测试（20180804）](/images/thumbnails/to_do_SanFrancisco.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-旧金山机房](https://vps123.top/digitalocean-facilities.html#sanfrancisco)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-旧金山机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180804-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的9341个有效测试样本中，共有超时点88个；响应均值为263毫秒，最快的三地区为上海、山东、湖南，最慢的三地区为甘肃、青海、西藏；浙江、江苏、江西、上海、辽宁等8处有响应超时情况；西藏、宁夏、青海、甘肃、天津等20处丢包率较高。海外20个国家地区的409个有效测试样本中，共有超时点12个；响应均值为157毫秒，最快的三地区为南非、荷兰、美国，最慢的三地区为印度尼西亚、马来西亚、菲律宾；香港有响应超时情况；菲律宾丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_usa-sanfrancisco_20180804_mainland.png)

大陆各省份到Digital Ocean美国-旧金山机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 62个 | 11个 | 209ms | 0.6% | 陕西 | 271个 | 3个 | 268ms | 3.4%  
山东 | 681个 | 0 | 230ms | 4.9% | 江苏 | 646个 | 18个 | 270ms | 5.6%  
湖南 | 479个 | 0 | 232ms | 3.9% | 福建 | 292个 | 0 | 270ms | 7.1%  
海南 | 64个 | 0 | 241ms | 3.4% | 广西 | 435个 | 0 | 271ms | 7.1%  
贵州 | 260个 | 0 | 244ms | 2.7% | 安徽 | 412个 | 0 | 271ms | 7.3%  
河北 | 416个 | 0 | 244ms | 6.0% | 云南 | 218个 | 0 | 275ms | 7.6%  
北京 | 72个 | 0 | 247ms | 2.9% | 辽宁 | 405个 | 9个 | 278ms | 7.4%  
湖北 | 326个 | 0 | 248ms | 4.8% | 四川 | 502个 | 0 | 279ms | 5.9%  
河南 | 610个 | 0 | 251ms | 6.5% | 内蒙古 | 356个 | 0 | 279ms | 6.4%  
山西 | 327个 | 0 | 257ms | 4.9% | 吉林 | 124个 | 0 | 282ms | 7.3%  
浙江 | 442个 | 25个 | 258ms | 4.6% | 重庆 | 71个 | 3个 | 282ms | 7.0%  
天津 | 44个 | 0 | 259ms | 10.1% | 宁夏 | 48个 | 0 | 328ms | 17.7%  
黑龙江 | 276个 | 0 | 259ms | 5.2% | 新疆 | 186个 | 0 | 332ms | 6.4%  
广东 | 818个 | 3个 | 262ms | 6.0% | 甘肃 | 204个 | 0 | 338ms | 11.3%  
均值 | 9341个 | 88个 | 263ms | 5.9% | 青海 | 32个 | 0 | 353ms | 12.8%  
江西 | 250个 | 16个 | 267ms | 5.0% | 西藏 | 12个 | 0 | 395ms | 20.1%  
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有9341个，其中超时点88个，平均响应时间为263毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的26个，超过300毫秒的5个；  
超时点较多的省份：上海；  
丢包率较高的省份：天津、宁夏、甘肃、青海、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_usa-sanfrancisco_20180804_overseas.png)

海外线路到Digital Ocean美国-旧金山机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
南非 | 6个 | 0 | 13ms | 0 | 德国 | 14个 | 0 | 164ms | 0  
荷兰 | 6个 | 0 | 23ms | 0 | 香港 | 129个 | 12个 | 169ms | 0.8%  
美国 | 88个 | 0 | 59ms | 1.1% | 英国 | 8个 | 0 | 169ms | 0  
加拿大 | 19个 | 0 | 74ms | 0 | 澳大利亚 | 8个 | 0 | 174ms | 0  
日本 | 8个 | 0 | 127ms | 1.5% | 法国 | 3个 | 0 | 178ms | 0  
巴西 | 6个 | 0 | 138ms | 0 | 俄罗斯 | 6个 | 0 | 195ms | -  
新加坡 | 26个 | 0 | 142ms | 0 | 越南 | 2个 | 0 | 198ms | 0  
意大利 | 6个 | 0 | 143ms | - | 印度尼西亚 | 8个 | 0 | 208ms | 0  
韩国 | 42个 | 0 | 146ms | 0 | 马来西亚 | 10个 | 0 | 212ms | 0.3%  
均值 | 409个 | 12个 | 157ms | 0.7% | 菲律宾 | 8个 | 0 | 459ms | 8.8%  
台湾 | 6个 | 0 | 161ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有409个，其中超时点12个，平均响应时间为157毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的2个，在100-200毫秒间的13个，在200-300毫秒间的2个，超过300毫秒的1个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180804 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180804 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180804-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
    * [班加罗尔](/digitalocean/idc/bangalore/20180804-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180804")
    * [法兰克福](/digitalocean/idc/frankfurt/20180804-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [伦敦](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [纽约](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [新加坡](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [多伦多](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")
  * 到Digital Ocean旧金山机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [20180918](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-digitalocean-idc-sanfrancisco.html)
