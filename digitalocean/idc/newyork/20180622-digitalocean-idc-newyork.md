#  多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean纽约\[NewYork\]机房的Ping测试（20180622）](/images/thumbnails/to_do_NewYork.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-纽约机房](https://vps123.top/digitalocean-facilities.html#newyork)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-纽约机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180622-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆32个省市的1960个有效测试样本中，共有超时点52个；响应均值为295毫秒，最快的三地区为河南、广东、山西，最慢的三地区为吉林、西藏、香港；云南、浙江、上海、江苏、辽宁等17处有响应超时情况；西藏、河南丢包率较高。海外19个国家地区的187个有效测试样本中，无超时点；响应均值为174毫秒，最快的三地区为加拿大、美国、德国，最慢的三地区为印度尼西亚、马来西亚、柬埔寨。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_usa-newyork_20180622_mainland.png)

大陆各省份到Digital Ocean美国-纽约机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
河南 | 99个 | 2个 | 261ms | 6.9% | 湖北 | 73个 | 2个 | 299ms | 1.5%  
广东 | 166个 | 0 | 276ms | 2.0% | 福建 | 77个 | 2个 | 300ms | 0.9%  
山西 | 69个 | 0 | 277ms | 3.8% | 湖南 | 78个 | 1个 | 300ms | 1.4%  
上海 | 18个 | 3个 | 279ms | 2.2% | 山东 | 77个 | 0 | 302ms | 2.2%  
北京 | 27个 | 1个 | 282ms | 1.6% | 陕西 | 64个 | 2个 | 304ms | 0.7%  
江苏 | 141个 | 3个 | 284ms | 1.5% | 云南 | 50个 | 21个 | 315ms | 1.1%  
浙江 | 127个 | 5个 | 286ms | 2.8% | 天津 | 6个 | 0 | 319ms | 0.8%  
安徽 | 75个 | 2个 | 288ms | 1.4% | 宁夏 | 28个 | 0 | 319ms | 2.0%  
辽宁 | 78个 | 3个 | 289ms | 1.2% | 重庆 | 28个 | 0 | 319ms | 3.0%  
广西 | 96个 | 0 | 291ms | 1.6% | 四川 | 87个 | 1个 | 320ms | 2.8%  
江西 | 48个 | 1个 | 292ms | 0.4% | 甘肃 | 31个 | 0 | 329ms | 2.0%  
海南 | 23个 | 0 | 292ms | 0.8% | 青海 | 10个 | 0 | 331ms | 2.4%  
均值 | 1960个 | 52个 | 295ms | 2.2% | 新疆 | 48个 | 0 | 338ms | 0.5%  
贵州 | 53个 | 0 | 297ms | 2.6% | 吉林 | 39个 | 1个 | 342ms | 2.2%  
河北 | 66个 | 0 | 297ms | 1.8% | 西藏 | 2个 | 0 | 466ms | 69.5%  
内蒙古 | 64个 | 1个 | 297ms | 2.2% | 香港 | 47个 | 0 | - | -  
黑龙江 | 65个 | 1个 | 298ms | 1.8% |  |  |  |  |   
  
简评：如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有1960个，其中超时点52个，平均响应时间为295毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的19个，超过300毫秒的12个；  
超时点较多的省份：上海、云南；  
丢包率较高的省份：西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于纽约\[NewYork\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_usa-newyork_20180622_overseas.png)

海外线路到Digital Ocean美国-纽约机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 4个 | 0 | 30ms | 0 | 香港 | 47个 | 0 | 185ms | 0  
美国 | 38个 | 0 | 68ms | 0 | 日本 | 4个 | 0 | 191ms | 4.3%  
德国 | 1个 | 0 | 73ms | - | 台湾 | 4个 | 0 | 196ms | 0  
意大利 | 1个 | 0 | 75ms | - | 韩国 | 27个 | 0 | 219ms | 0  
法国 | 3个 | 0 | 81ms | 0 | 澳大利亚 | 3个 | 0 | 231ms | 1.0%  
巴西 | 3个 | 0 | 81ms | 0 | 越南 | 6个 | 0 | 234ms | 0  
英国 | 5个 | 0 | 154ms | 0 | 菲律宾 | 6个 | 0 | 245ms | 0  
均值 | 187个 | 0 | 174ms | 0.6% | 印度尼西亚 | 2个 | 0 | 269ms | 0  
南非 | 6个 | 0 | 177ms | 0.2% | 马来西亚 | 15个 | 0 | 279ms | 0.3%  
新加坡 | 9个 | 0 | 181ms | 3.3% | 柬埔寨 | 3个 | 0 | 343ms | 0.7%  
  
简评：如果你考虑在Digital Ocean的纽约[NewYork]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于纽约[NewYork]的机房的连通状况。到此机房的ping监测点共有187个，其中超时点0个，平均响应时间为174毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的5个，在100-200毫秒间的6个，在200-300毫秒间的6个，超过300毫秒的1个；

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
    * [旧金山](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [新加坡](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [多伦多](/digitalocean/idc/toronto/20180622-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180622")
  * 到Digital Ocean纽约机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/newyork/20180527-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180527")
    * [20180804](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
  * 本期报告：在纽约部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/newyork/20180622-bwg-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180622")
    * [Digital Ocean](do/idc/newyork/20180622-do-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")



本文最初发表于[多地到Digital Ocean纽约[NewYork]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-digitalocean-idc-newyork.html)
