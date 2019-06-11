#  多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean班加罗尔\[Bangalore\]机房的Ping测试（20180622）](/images/thumbnails/to_do_Bangalore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[印度-班加罗尔机房](https://vps123.top/digitalocean-facilities.html#bangalore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的印度-班加罗尔机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180622-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的888个有效测试样本中，共有超时点21个；响应均值为347毫秒，最快的三地区为北京、辽宁、江西，最慢的三地区为云南、新疆、香港；云南、江苏、浙江、陕西、河南等11处有响应超时情况。海外18个国家地区的88个有效测试样本中，无超时点；响应均值为187毫秒，最快的三地区为新加坡、菲律宾、马来西亚，最慢的三地区为加拿大、澳大利亚、南非。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_india-bangalore_20180622_mainland.png)

大陆各省份到Digital Ocean印度-班加罗尔机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 11个 | 0 | 308ms | 0 | 广西 | 44个 | 0 | 348ms | 1.0%  
辽宁 | 35个 | 0 | 308ms | 2.6% | 湖北 | 34个 | 0 | 350ms | 1.0%  
江西 | 23个 | 0 | 311ms | 1.0% | 甘肃 | 17个 | 1个 | 353ms | 0.3%  
陕西 | 28个 | 1个 | 326ms | 0.8% | 贵州 | 22个 | 1个 | 356ms | 3.1%  
江苏 | 65个 | 3个 | 327ms | 3.7% | 内蒙古 | 32个 | 0 | 359ms | 0.8%  
浙江 | 52个 | 2个 | 327ms | 1.6% | 宁夏 | 14个 | 0 | 368ms | 0.2%  
河南 | 51个 | 1个 | 328ms | 4.5% | 山东 | 37个 | 0 | 369ms | 2.2%  
广东 | 74个 | 0 | 331ms | 0.7% | 黑龙江 | 25个 | 1个 | 376ms | 1.1%  
山西 | 31个 | 0 | 334ms | 4.3% | 重庆 | 12个 | 1个 | 376ms | 0.5%  
安徽 | 38个 | 1个 | 339ms | 2.8% | 青海 | 5个 | 0 | 380ms | 0  
海南 | 9个 | 0 | 339ms | 0.6% | 福建 | 31个 | 0 | 384ms | 2.6%  
天津 | 3个 | 0 | 341ms | 0 | 吉林 | 13个 | 0 | 384ms | 0.4%  
湖南 | 35个 | 0 | 341ms | 1.7% | 四川 | 40个 | 0 | 390ms | 1.6%  
上海 | 7个 | 1个 | 344ms | 0.3% | 云南 | 22个 | 8个 | 397ms | 2.0%  
河北 | 32个 | 0 | 346ms | 0.7% | 新疆 | 21个 | 0 | 398ms | 1.4%  
均值 | 888个 | 21个 | 347ms | 1.8% | 香港 | 25个 | 0 | - | -  
  
简评：如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有888个，其中超时点21个，平均响应时间为347毫秒，丢包率为1%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，超过300毫秒的30个；  
超时点较多的省份：上海、云南；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_india-bangalore_20180622_overseas.png)

海外线路到Digital Ocean印度-班加罗尔机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
新加坡 | 5个 | 0 | 77ms | 0 | 法国 | 1个 | 0 | 190ms | 0  
菲律宾 | 2个 | 0 | 102ms | 1.0% | 巴西 | 1个 | 0 | 190ms | 0  
马来西亚 | 5个 | 0 | 114ms | 0.6% | 香港 | 25个 | 0 | 200ms | 0  
越南 | 2个 | 0 | 120ms | 1.0% | 台湾 | 2个 | 0 | 232ms | 0  
日本 | 2个 | 0 | 125ms | 4.0% | 美国 | 19个 | 0 | 236ms | 0  
意大利 | 1个 | 0 | 149ms | - | 英国 | 2个 | 0 | 250ms | 0  
柬埔寨 | 1个 | 0 | 157ms | 1.0% | 加拿大 | 2个 | 0 | 268ms | 0  
德国 | 1个 | 0 | 173ms | - | 澳大利亚 | 1个 | 0 | 290ms | 0  
韩国 | 14个 | 0 | 180ms | 0 | 南非 | 2个 | 0 | 311ms | 1.0%  
均值 | 88个 | 0 | 187ms | 0.5% |  |  |  |  |   
  
简评：如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有88个，其中超时点0个，平均响应时间为187毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50-100毫秒间的1个，在100-200毫秒间的11个，在200-300毫秒间的5个，超过300毫秒的1个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180622 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180622 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180622-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180622")
    * [法兰克福](/digitalocean/idc/frankfurt/20180622-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [伦敦](/digitalocean/idc/london/20180622-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [纽约](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [新加坡](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [多伦多](/digitalocean/idc/toronto/20180622-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180622")
  * 到Digital Ocean班加罗尔机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/bangalore/20180514-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/bangalore/20180527-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180527")
    * [20180804](/digitalocean/idc/bangalore/20180804-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/bangalore/20180918-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-digitalocean-idc-bangalore.html)
