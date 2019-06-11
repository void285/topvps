#  多地到Digital Ocean多伦多[Toronto]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean多伦多\[Toronto\]机房的Ping测试（20180514）](/images/thumbnails/to_do_Toronto.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[加拿大-多伦多机房](https://vps123.top/digitalocean-facilities.html#toronto)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的加拿大-多伦多机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180514-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Digital Ocean加拿大-多伦多机房的PING测试结果，连通概况如下：大陆31个省市的945个有效测试样本中，共有超时点11个；响应均值为281毫秒，最快的三地区为上海、天津、北京，最慢的三地区为青海、新疆、西藏；浙江、北京、广东、重庆、广西等9处有响应超时情况；浙江、山西、西藏、辽宁、江西等29处丢包率较高。海外18个国家地区的79个有效测试样本中，无超时点；响应均值为184毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为菲律宾、南非、印度尼西亚；印度尼西亚丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于多伦多\[Toronto\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_canada-toronto_20180514_mainland.png)

**大陆各省份到Digital Ocean加拿大-多伦多机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 8个 | 0 | 229ms | 0.1%  
天津 | 4个 | 0 | 251ms | 10.3%  
北京 | 8个 | 1个 | 258ms | 6.4%  
安徽 | 41个 | 0 | 263ms | 5.3%  
广东 | 75个 | 1个 | 264ms | 6.7%  
重庆 | 16个 | 1个 | 267ms | 1.8%  
吉林 | 13个 | 0 | 268ms | 10.2%  
广西 | 37个 | 1个 | 269ms | 6.4%  
江苏 | 61个 | 1个 | 271ms | 11.4%  
河北 | 33个 | 0 | 271ms | 11.4%  
福建 | 32个 | 1个 | 273ms | 5.6%  
海南 | 11个 | 0 | 273ms | 6.0%  
山东 | 53个 | 1个 | 274ms | 7.0%  
湖北 | 49个 | 0 | 277ms | 8.9%  
宁夏 | 11个 | 0 | 277ms | 8.5%  
陕西 | 31个 | 1个 | 278ms | 10.0%  
河南 | 53个 | 0 | 279ms | 10.5%  
辽宁 | 35个 | 0 | 281ms | 14.8%  
均值 | 945个 | 11个 | 281ms | 9.7%  
浙江 | 48个 | 3个 | 284ms | 16.1%  
四川 | 46个 | 0 | 288ms | 8.3%  
甘肃 | 20个 | 0 | 289ms | 6.1%  
江西 | 22个 | 0 | 290ms | 14.3%  
湖南 | 45个 | 0 | 292ms | 10.4%  
内蒙古 | 33个 | 0 | 296ms | 12.1%  
山西 | 38个 | 0 | 296ms | 15.1%  
云南 | 25个 | 0 | 297ms | 7.5%  
黑龙江 | 38个 | 0 | 298ms | 12.7%  
贵州 | 28个 | 0 | 305ms | 12.6%  
青海 | 3个 | 0 | 307ms | 7.3%  
新疆 | 27个 | 0 | 332ms | 9.7%  
西藏 | 1个 | 0 | 387ms | 15.0%  
  
**简评：** 如果你考虑在Digital Ocean的多伦多[Toronto]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于多伦多[Toronto]的机房的连通状况。到此机房的ping监测点共有945个，其中超时点11个，平均响应时间为281毫秒，丢包率为9%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的27个，超过300毫秒的4个；  
超时点较多的省份：北京；  
丢包率较高的省份：天津、吉林、江苏、河北、陕西、河南、辽宁、浙江、江西、湖南、内蒙古、山西、黑龙江、贵州、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于多伦多\[Toronto\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_canada-toronto_20180514_overseas.png)

**海外线路到Digital Ocean加拿大-多伦多机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
加拿大 | 3个 | 0 | 14ms | 1.0%  
美国 | 18个 | 0 | 62ms | 0.8%  
法国 | 2个 | 0 | 91ms | 0  
荷兰 | 1个 | 0 | 100ms | 0  
英国 | 2个 | 0 | 107ms | 0  
德国 | 1个 | 0 | 125ms | 0  
巴西 | 1个 | 0 | 139ms | 0  
日本 | 2个 | 0 | 164ms | 0  
均值 | 79个 | 0 | 184ms | 1.7%  
俄罗斯 | 1个 | 0 | 200ms | 0  
台湾 | 1个 | 0 | 201ms | -  
韩国 | 13个 | 0 | 211ms | 0  
香港 | 19个 | 0 | 230ms | 0  
新加坡 | 6个 | 0 | 236ms | 0  
澳大利亚 | 2个 | 0 | 241ms | 0  
马来西亚 | 3个 | 0 | 258ms | 0  
菲律宾 | 1个 | 0 | 264ms | 1.0%  
南非 | 2个 | 0 | 274ms | 0.5%  
印度尼西亚 | 1个 | 0 | 397ms | 26.0%  
  
**简评：** 如果你考虑在Digital Ocean的多伦多[Toronto]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于多伦多[Toronto]的机房的连通状况。到此机房的ping监测点共有79个，其中超时点0个，平均响应时间为184毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的3个，在100-200毫秒间的5个，在200-300毫秒间的8个，超过300毫秒的1个；  
丢包率较高的国家/地区：印度尼西亚；

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
    * [旧金山](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [新加坡](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
  * 到Digital Ocean多伦多机房的 _其他近期报告_ ： 
    * [20180527](/digitalocean/idc/toronto/20180527-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/toronto/20180622-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/toronto/20180918-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean多伦多[Toronto]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-digitalocean-idc-toronto.html)
