#  多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean班加罗尔\[Bangalore\]机房的Ping测试（20180514）](/images/thumbnails/to_do_Bangalore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[印度-班加罗尔机房](https://vps123.top/digitalocean-facilities.html#bangalore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的印度-班加罗尔机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180514-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Digital Ocean印度-班加罗尔机房的PING测试结果，连通概况如下：大陆31个省市的891个有效测试样本中，共有超时点17个；响应均值为365毫秒，最快的三地区为浙江、辽宁、山西，最慢的三地区为重庆、四川、广西；江苏、湖北、浙江、福建、北京等11处有响应超时情况；广西、云南、辽宁、四川丢包率较高。海外18个国家地区的81个有效测试样本中，无超时点；响应均值为188毫秒，最快的三地区为新加坡、马来西亚、菲律宾，最慢的三地区为南非、俄罗斯、巴西。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_india-bangalore_20180514_mainland.png)

**大陆各省份到Digital Ocean印度-班加罗尔机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
浙江 | 50个 | 2个 | 294ms | 0.5%  
辽宁 | 32个 | 0 | 321ms | 5.4%  
山西 | 31个 | 0 | 326ms | 1.9%  
江苏 | 55个 | 3个 | 327ms | 0.7%  
河南 | 53个 | 0 | 335ms | 0.9%  
北京 | 7个 | 1个 | 338ms | 0  
天津 | 5个 | 0 | 341ms | 0  
山东 | 48个 | 1个 | 345ms | 1.0%  
江西 | 24个 | 0 | 351ms | 4.2%  
陕西 | 30个 | 1个 | 354ms | 1.0%  
安徽 | 39个 | 0 | 359ms | 1.2%  
黑龙江 | 36个 | 0 | 361ms | 0.7%  
西藏 | 1个 | 0 | 363ms | 0  
均值 | 891个 | 17个 | 365ms | 2.5%  
宁夏 | 12个 | 0 | 367ms | 0.1%  
湖南 | 43个 | 0 | 368ms | 3.2%  
青海 | 4个 | 0 | 370ms | 0  
内蒙古 | 29个 | 0 | 370ms | 1.8%  
湖北 | 41个 | 3个 | 373ms | 4.4%  
甘肃 | 19个 | 0 | 380ms | 0.6%  
广东 | 74个 | 1个 | 381ms | 3.5%  
云南 | 24个 | 0 | 381ms | 6.8%  
上海 | 8个 | 0 | 381ms | 0  
海南 | 11个 | 0 | 385ms | 0.7%  
河北 | 28个 | 0 | 391ms | 3.1%  
贵州 | 24个 | 1个 | 392ms | 3.3%  
吉林 | 13个 | 0 | 394ms | 1.3%  
福建 | 33个 | 2个 | 397ms | 1.2%  
新疆 | 26个 | 0 | 403ms | 2.1%  
重庆 | 14个 | 0 | 409ms | 1.3%  
四川 | 45个 | 1个 | 417ms | 5.1%  
广西 | 32个 | 1个 | 432ms | 8.5%  
  
**简评：** 如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有891个，其中超时点17个，平均响应时间为365毫秒，丢包率为2%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的1个，超过300毫秒的30个；  
超时点较多的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于班加罗尔\[Bangalore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_india-bangalore_20180514_overseas.png)

**海外线路到Digital Ocean印度-班加罗尔机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
新加坡 | 6个 | 0 | 39ms | 0  
马来西亚 | 3个 | 0 | 61ms | 0  
菲律宾 | 1个 | 0 | 93ms | 0  
台湾 | 1个 | 0 | 103ms | -  
日本 | 2个 | 0 | 118ms | 0.5%  
香港 | 19个 | 0 | 123ms | 0  
韩国 | 13个 | 0 | 149ms | 0.3%  
荷兰 | 1个 | 0 | 149ms | 0  
印度尼西亚 | 1个 | 0 | 167ms | 5.0%  
德国 | 2个 | 0 | 181ms | 0  
均值 | 81个 | 0 | 188ms | 0.4%  
法国 | 2个 | 0 | 205ms | 0  
英国 | 2个 | 0 | 213ms | 0  
美国 | 19个 | 0 | 236ms | 0.4%  
澳大利亚 | 2个 | 0 | 256ms | 0  
加拿大 | 3个 | 0 | 259ms | 1.0%  
南非 | 2个 | 0 | 336ms | 0  
俄罗斯 | 1个 | 0 | 344ms | 0  
巴西 | 1个 | 0 | 352ms | 0  
  
**简评：** 如果你考虑在Digital Ocean的班加罗尔[Bangalore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于班加罗尔[Bangalore]的机房的连通状况。到此机房的ping监测点共有81个，其中超时点0个，平均响应时间为188毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的2个，在100-200毫秒间的7个，在200-300毫秒间的5个，超过300毫秒的3个；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180514 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180514 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [法兰克福](/digitalocean/idc/frankfurt/20180514-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [伦敦](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [纽约](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [新加坡](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [多伦多](/digitalocean/idc/toronto/20180514-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180514")
  * 到Digital Ocean班加罗尔机房的 _其他近期报告_ ： 
    * [20180527](/digitalocean/idc/bangalore/20180527-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/bangalore/20180622-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/bangalore/20180804-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/bangalore/20180918-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean班加罗尔[Bangalore]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-digitalocean-idc-bangalore.html)
