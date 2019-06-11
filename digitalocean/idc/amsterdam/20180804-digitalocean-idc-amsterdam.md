#  多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean阿姆斯特丹\[Amsterdam\]机房的Ping测试（20180804）](/images/thumbnails/to_do_Amsterdam.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[荷兰-阿姆斯特丹机房](https://vps123.top/digitalocean-facilities.html#amsterdam)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的荷兰-阿姆斯特丹机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180804-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的9728个有效测试样本中，共有超时点106个；响应均值为309毫秒，最快的三地区为北京、上海、河北，最慢的三地区为贵州、新疆、西藏；江苏、广东、浙江、辽宁、上海等9处有响应超时情况；西藏、宁夏、甘肃、青海、新疆等16处丢包率较高。海外19个国家地区的465个有效测试样本中，无超时点；响应均值为180毫秒，最快的三地区为意大利、巴西、德国，最慢的三地区为台湾、法国、菲律宾；菲律宾丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_netherlands-amsterdam_20180804_mainland.png)

大陆各省份到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 72个 | 0 | 270ms | 3.7% | 浙江 | 448个 | 14个 | 309ms | 2.4%  
上海 | 59个 | 8个 | 275ms | 3.3% | 均值 | 9728个 | 106个 | 309ms | 5.1%  
河北 | 452个 | 8个 | 280ms | 3.5% | 江苏 | 661个 | 27个 | 311ms | 2.8%  
辽宁 | 428个 | 9个 | 288ms | 9.2% | 宁夏 | 56个 | 0 | 311ms | 18.5%  
江西 | 254个 | 8个 | 290ms | 2.8% | 云南 | 226个 | 0 | 315ms | 5.9%  
内蒙古 | 408个 | 0 | 290ms | 6.9% | 河南 | 642个 | 0 | 318ms | 7.2%  
福建 | 309个 | 0 | 291ms | 4.1% | 四川 | 535个 | 0 | 319ms | 1.4%  
安徽 | 400个 | 0 | 291ms | 5.5% | 山西 | 342个 | 0 | 321ms | 5.9%  
重庆 | 74个 | 0 | 292ms | 11.2% | 广东 | 821个 | 22个 | 324ms | 2.7%  
天津 | 40个 | 0 | 293ms | 9.1% | 山东 | 664个 | 0 | 327ms | 2.9%  
广西 | 436个 | 0 | 293ms | 2.9% | 青海 | 32个 | 0 | 327ms | 13.4%  
湖南 | 482个 | 0 | 300ms | 3.4% | 黑龙江 | 308个 | 0 | 327ms | 5.6%  
海南 | 64个 | 0 | 300ms | 2.6% | 吉林 | 136个 | 0 | 337ms | 6.6%  
湖北 | 346个 | 0 | 306ms | 3.3% | 贵州 | 268个 | 7个 | 338ms | 4.7%  
陕西 | 287个 | 3个 | 306ms | 8.4% | 新疆 | 254个 | 0 | 346ms | 12.9%  
甘肃 | 208个 | 0 | 307ms | 15.0% | 西藏 | 16个 | 0 | 453ms | 34.7%  
  
简评：如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有9728个，其中超时点106个，平均响应时间为309毫秒，丢包率为5%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的13个，超过300毫秒的18个；  
超时点较多的省份：上海；  
丢包率较高的省份：重庆、甘肃、宁夏、青海、新疆、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于阿姆斯特丹\[Amsterdam\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_netherlands-amsterdam_20180804_overseas.png)

海外线路到Digital Ocean荷兰-阿姆斯特丹机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
意大利 | 6个 | 0 | 7ms | - | 印度尼西亚 | 12个 | 0 | 185ms | 0.3%  
巴西 | 6个 | 0 | 8ms | 0 | 香港 | 126个 | 0 | 186ms | 0  
德国 | 18个 | 0 | 23ms | 0 | 南非 | 12个 | 0 | 192ms | 0  
俄罗斯 | 6个 | 0 | 42ms | - | 马来西亚 | 21个 | 0 | 237ms | 1.9%  
英国 | 12个 | 0 | 56ms | 0 | 日本 | 12个 | 0 | 260ms | 0.8%  
加拿大 | 27个 | 0 | 102ms | 0.7% | 韩国 | 42个 | 0 | 274ms | 0  
荷兰 | 6个 | 0 | 138ms | 0 | 澳大利亚 | 12个 | 0 | 297ms | 0  
美国 | 96个 | 0 | 160ms | 2.8% | 台湾 | 6个 | 0 | 307ms | 0  
新加坡 | 30个 | 0 | 165ms | 0 | 法国 | 3个 | 0 | 310ms | 0  
均值 | 465个 | 0 | 180ms | 1.6% | 菲律宾 | 12个 | 0 | 471ms | 20.8%  
  
简评：如果你考虑在Digital Ocean的阿姆斯特丹[Amsterdam]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于阿姆斯特丹[Amsterdam]的机房的连通状况。到此机房的ping监测点共有465个，其中超时点0个，平均响应时间为180毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的1个，在100-200毫秒间的7个，在200-300毫秒间的4个，超过300毫秒的3个；  
丢包率较高的国家/地区：菲律宾；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180804 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180804 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [班加罗尔](/digitalocean/idc/bangalore/20180804-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180804")
    * [法兰克福](/digitalocean/idc/frankfurt/20180804-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [伦敦](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [纽约](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [新加坡](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [多伦多](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")
  * 到Digital Ocean阿姆斯特丹机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/amsterdam/20180527-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/amsterdam/20180622-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180622")
    * [20180918](/digitalocean/idc/amsterdam/20180918-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
  * 本期报告：在阿姆斯特丹部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/amsterdam/20180804-bwg-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180804")
    * [Digital Ocean](do/idc/amsterdam/20180804-do-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
    * [Vultr](/vultr/idc/amsterdam/20180804-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180804")



本文最初发表于[多地到Digital Ocean阿姆斯特丹[Amsterdam]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-digitalocean-idc-amsterdam.html)
