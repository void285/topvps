#  多地到Digital Ocean伦敦[London]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean伦敦\[London\]机房的Ping测试（20180622）](/images/thumbnails/to_do_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[英国-伦敦机房](https://vps123.top/digitalocean-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180622-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆32个省市的846个有效测试样本中，共有超时点17个；响应均值为268毫秒，最快的三地区为上海、河北、广东，最慢的三地区为吉林、西藏、香港；云南、浙江、江苏、福建、安徽等7处有响应超时情况。海外17个国家地区的64个有效测试样本中，共有超时点1个；响应均值为189毫秒，最快的三地区为德国、意大利、英国，最慢的三地区为韩国、澳大利亚、柬埔寨；香港有响应超时情况。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_uk-london_20180622_mainland.png)

**大陆各省份到Digital Ocean英国-伦敦机房的测速数据 [20180622]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 5个 | 0 | 233ms | 0.2%  
河北 | 31个 | 0 | 241ms | 0.2%  
广东 | 73个 | 0 | 243ms | 0.6%  
天津 | 2个 | 0 | 245ms | 0  
甘肃 | 15个 | 0 | 256ms | 0.7%  
辽宁 | 35个 | 0 | 258ms | 1.4%  
江苏 | 58个 | 1个 | 259ms | 2.2%  
浙江 | 46个 | 2个 | 259ms | 0  
广西 | 40个 | 0 | 259ms | 1.4%  
福建 | 27个 | 1个 | 263ms | 1.0%  
山西 | 31个 | 0 | 263ms | 3.6%  
湖南 | 36个 | 0 | 264ms | 1.0%  
安徽 | 36个 | 1个 | 265ms | 0.2%  
内蒙古 | 27个 | 0 | 266ms | 3.5%  
青海 | 5个 | 0 | 267ms | 0.2%  
均值 | 846个 | 17个 | 268ms | 0.9%  
云南 | 21个 | 10个 | 270ms | 0.1%  
重庆 | 10个 | 0 | 270ms | 0.3%  
湖北 | 31个 | 0 | 271ms | 0.4%  
宁夏 | 13个 | 0 | 272ms | 0.2%  
河南 | 43个 | 0 | 274ms | 0.6%  
江西 | 25个 | 0 | 274ms | 0.1%  
陕西 | 24个 | 0 | 274ms | 0.1%  
北京 | 5个 | 0 | 275ms | 0.6%  
四川 | 41个 | 0 | 277ms | 0.7%  
海南 | 12个 | 0 | 278ms | 0.3%  
山东 | 42个 | 0 | 287ms | 0.2%  
黑龙江 | 32个 | 0 | 289ms | 0.6%  
贵州 | 22个 | 0 | 290ms | 3.2%  
新疆 | 25个 | 1个 | 302ms | 0  
吉林 | 18个 | 0 | 302ms | 0.6%  
西藏 | 1个 | 0 | 371ms | 4.0%  
香港 | 14个 | 1个 | - | -  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有846个，其中超时点17个，平均响应时间为268毫秒，丢包率为0%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的28个，超过300毫秒的3个；  
超时点较多的省份：云南；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_uk-london_20180622_overseas.png)

**海外线路到Digital Ocean英国-伦敦机房的测速数据 [20180622]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
德国 | 1个 | 0 | 9ms | -  
意大利 | 1个 | 0 | 14ms | -  
英国 | 1个 | 0 | 34ms | 0  
加拿大 | 2个 | 0 | 86ms | 0  
美国 | 16个 | 0 | 126ms | 0  
新加坡 | 4个 | 0 | 184ms | 0  
均值 | 64个 | 1个 | 189ms | 0.4%  
印度尼西亚 | 1个 | 0 | 204ms | 0  
南非 | 1个 | 0 | 207ms | 0  
香港 | 14个 | 1个 | 215ms | -  
菲律宾 | 2个 | 0 | 231ms | 0  
马来西亚 | 5个 | 0 | 237ms | 1.2%  
日本 | 2个 | 0 | 265ms | 4.0%  
越南 | 2个 | 0 | 265ms | 0  
台湾 | 1个 | 0 | 270ms | -  
韩国 | 9个 | 0 | 271ms | 0  
澳大利亚 | 1个 | 0 | 295ms | 0  
柬埔寨 | 1个 | 0 | 304ms | 0  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有64个，其中超时点1个，平均响应时间为189毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的1个，在100-200毫秒间的2个，在200-300毫秒间的10个，超过300毫秒的1个；

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
    * [纽约](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [新加坡](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [多伦多](/digitalocean/idc/toronto/20180622-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180622")
  * 到Digital Ocean伦敦机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [20180804](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180622-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [Linode](/linode/idc/london/20180622-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180622")
    * [Vultr](/vultr/idc/london/20180622-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180622")



本文最初发表于[多地到Digital Ocean伦敦[London]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-digitalocean-idc-london.html)
