#  多地到Digital Ocean伦敦[London]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean伦敦\[London\]机房的Ping测试（20180426）](/images/thumbnails/to_do_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[英国-伦敦机房](https://vps123.top/digitalocean-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180426-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Digital Ocean英国-伦敦机房的PING测试结果，连通概况如下：大陆31个省市的837个有效测试样本中，共有超时点10个；响应均值为282毫秒，最快的三地区为河北、重庆、北京，最慢的三地区为新疆、黑龙江、西藏；北京、浙江、湖南、天津、辽宁等7处有响应超时情况；江苏、湖北、江西、浙江、上海等9处丢包率较高。海外17个国家地区的77个有效测试样本中，无超时点；响应均值为175毫秒，最快的三地区为法国、荷兰、英国，最慢的三地区为韩国、澳大利亚、柬埔寨；柬埔寨丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_uk-london_20180426_mainland.png)

**大陆各省份到Digital Ocean英国-伦敦机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
河北 | 30个 | 0 | 248ms | 2.5%  
重庆 | 10个 | 0 | 252ms | 0  
北京 | 4个 | 2个 | 256ms | 0  
上海 | 6个 | 0 | 257ms | 7.0%  
青海 | 4个 | 0 | 260ms | 0  
湖北 | 38个 | 0 | 260ms | 12.3%  
天津 | 5个 | 1个 | 262ms | 6.7%  
辽宁 | 35个 | 1个 | 264ms | 2.7%  
广西 | 35个 | 0 | 265ms | 2.5%  
安徽 | 36个 | 0 | 266ms | 6.7%  
甘肃 | 20个 | 1个 | 270ms | 0.4%  
江西 | 22个 | 0 | 271ms | 12.2%  
河南 | 53个 | 0 | 276ms | 0.7%  
浙江 | 36个 | 2个 | 276ms | 9.2%  
广东 | 59个 | 0 | 276ms | 0.4%  
内蒙古 | 31个 | 0 | 276ms | 1.3%  
四川 | 44个 | 0 | 278ms | 0.8%  
陕西 | 29个 | 0 | 282ms | 0.7%  
均值 | 837个 | 10个 | 282ms | 3.9%  
宁夏 | 11个 | 0 | 284ms | 2.8%  
江苏 | 50个 | 1个 | 285ms | 12.5%  
海南 | 10个 | 0 | 285ms | 0.4%  
云南 | 27个 | 0 | 288ms | 2.5%  
山东 | 47个 | 0 | 297ms | 0.3%  
山西 | 32个 | 0 | 297ms | 2.8%  
福建 | 26个 | 0 | 299ms | 3.3%  
湖南 | 41个 | 2个 | 302ms | 4.6%  
贵州 | 22个 | 0 | 311ms | 5.1%  
吉林 | 15个 | 0 | 315ms | 1.7%  
新疆 | 27个 | 0 | 316ms | 0.8%  
黑龙江 | 31个 | 0 | 326ms | 6.8%  
西藏 | 1个 | 0 | 333ms | 3.0%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有837个，其中超时点10个，平均响应时间为282毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的25个，超过300毫秒的6个；  
超时点较多的省份：北京、天津；  
丢包率较高的省份：湖北、江西、江苏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_uk-london_20180426_overseas.png)

**海外线路到Digital Ocean英国-伦敦机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
法国 | 2个 | 0 | 6ms | 0  
荷兰 | 2个 | 0 | 10ms | 0  
英国 | 3个 | 0 | 14ms | 0  
德国 | 1个 | 0 | 17ms | 0  
加拿大 | 4个 | 0 | 86ms | 0  
俄罗斯 | 1个 | 0 | 111ms | 0  
美国 | 16个 | 0 | 132ms | 0  
南非 | 1个 | 0 | 162ms | 0  
均值 | 77个 | 0 | 175ms | 1.7%  
马来西亚 | 3个 | 0 | 180ms | 0  
新加坡 | 5个 | 0 | 189ms | 0  
香港 | 20个 | 0 | 212ms | 0  
越南 | 1个 | 0 | 229ms | 0  
日本 | 3个 | 0 | 250ms | 0.7%  
台湾 | 1个 | 0 | 262ms | -  
韩国 | 12个 | 0 | 280ms | 0  
澳大利亚 | 1个 | 0 | 314ms | 0  
柬埔寨 | 1个 | 0 | 522ms | 27.0%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有77个，其中超时点0个，平均响应时间为175毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的5个，超过300毫秒的2个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180426 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180426 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180426-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180426")
    * [班加罗尔](/digitalocean/idc/bangalore/20180426-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180426")
    * [法兰克福](/digitalocean/idc/frankfurt/20180426-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180426")
    * [纽约](/digitalocean/idc/newyork/20180426-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180426")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180426-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180426")
    * [新加坡](/digitalocean/idc/singapore/20180426-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180426")
    * [多伦多](/digitalocean/idc/toronto/20180426-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180426")
  * 到Digital Ocean伦敦机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/london/20180622-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180426-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180426")
    * [Linode](/linode/idc/london/20180426-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180426")
    * [Vultr](/vultr/idc/london/20180426-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180426")



本文最初发表于[多地到Digital Ocean伦敦[London]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-digitalocean-idc-london.html)
