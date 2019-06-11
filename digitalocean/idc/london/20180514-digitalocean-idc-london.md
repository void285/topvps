#  多地到Digital Ocean伦敦[London]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean伦敦\[London\]机房的Ping测试（20180514）](/images/thumbnails/to_do_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[英国-伦敦机房](https://vps123.top/digitalocean-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180514-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Digital Ocean英国-伦敦机房的PING测试结果，连通概况如下：大陆31个省市的903个有效测试样本中，共有超时点10个；响应均值为283毫秒，最快的三地区为北京、天津、上海，最慢的三地区为山东、新疆、吉林；浙江、广东、北京、广西、江苏等7处有响应超时情况；浙江、江苏、吉林、辽宁、贵州等6处丢包率较高。海外19个国家地区的81个有效测试样本中，无超时点；响应均值为178毫秒，最快的三地区为荷兰、法国、英国，最慢的三地区为台湾、澳大利亚、柬埔寨；柬埔寨丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_uk-london_20180514_mainland.png)

**大陆各省份到Digital Ocean英国-伦敦机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
北京 | 7个 | 1个 | 222ms | 0  
天津 | 4个 | 0 | 226ms | 4.8%  
上海 | 6个 | 0 | 245ms | 0.2%  
宁夏 | 11个 | 0 | 246ms | 2.5%  
重庆 | 17个 | 0 | 256ms | 0.5%  
青海 | 4个 | 0 | 257ms | 0  
甘肃 | 16个 | 0 | 257ms | 0.2%  
河北 | 31个 | 0 | 257ms | 4.5%  
安徽 | 34个 | 0 | 265ms | 1.0%  
广西 | 34个 | 1个 | 268ms | 1.2%  
内蒙古 | 32个 | 0 | 271ms | 3.2%  
辽宁 | 37个 | 0 | 274ms | 7.3%  
广东 | 74个 | 2个 | 275ms | 2.4%  
浙江 | 53个 | 3个 | 280ms | 10.9%  
四川 | 49个 | 0 | 283ms | 3.2%  
湖北 | 43个 | 0 | 283ms | 4.5%  
均值 | 903个 | 10个 | 283ms | 4.1%  
海南 | 10个 | 0 | 284ms | 2.8%  
河南 | 49个 | 0 | 285ms | 4.1%  
江苏 | 62个 | 1个 | 286ms | 8.0%  
江西 | 21个 | 0 | 287ms | 3.5%  
湖南 | 40个 | 0 | 287ms | 3.9%  
陕西 | 27个 | 0 | 290ms | 3.3%  
云南 | 23个 | 0 | 292ms | 1.8%  
福建 | 33个 | 0 | 297ms | 3.8%  
山西 | 35个 | 0 | 297ms | 5.2%  
贵州 | 26个 | 1个 | 304ms | 6.4%  
西藏 | 1个 | 0 | 306ms | 0  
黑龙江 | 34个 | 0 | 308ms | 3.6%  
山东 | 49个 | 1个 | 309ms | 4.1%  
新疆 | 27个 | 0 | 311ms | 2.0%  
吉林 | 14个 | 0 | 316ms | 7.6%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有903个，其中超时点10个，平均响应时间为283毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的25个，超过300毫秒的6个；  
超时点较多的省份：北京；  
丢包率较高的省份：浙江；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_uk-london_20180514_overseas.png)

**海外线路到Digital Ocean英国-伦敦机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
荷兰 | 1个 | 0 | 6ms | 0  
法国 | 2个 | 0 | 8ms | 0  
英国 | 2个 | 0 | 18ms | 0  
德国 | 2个 | 0 | 26ms | 0  
加拿大 | 3个 | 0 | 86ms | 0.5%  
俄罗斯 | 1个 | 0 | 109ms | 0  
美国 | 19个 | 0 | 133ms | 2.6%  
新加坡 | 6个 | 0 | 174ms | 0  
均值 | 81个 | 0 | 178ms | 2.0%  
南非 | 2个 | 0 | 186ms | 0  
巴西 | 1个 | 0 | 197ms | 0  
印度尼西亚 | 1个 | 0 | 208ms | 3.0%  
马来西亚 | 3个 | 0 | 215ms | 0.3%  
香港 | 19个 | 0 | 219ms | 0  
菲律宾 | 1个 | 0 | 238ms | 0  
韩国 | 13个 | 0 | 274ms | 0  
日本 | 1个 | 0 | 277ms | 1.0%  
台湾 | 1个 | 0 | 285ms | -  
澳大利亚 | 2个 | 0 | 294ms | 0  
柬埔寨 | 1个 | 0 | 437ms | 29.0%  
  
**简评：** 如果你考虑在Digital Ocean的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有81个，其中超时点0个，平均响应时间为178毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的8个，超过300毫秒的1个；  
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
    * [纽约](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [新加坡](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [多伦多](/digitalocean/idc/toronto/20180514-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180514")
  * 到Digital Ocean伦敦机房的 _其他近期报告_ ： 
    * [20180527](/digitalocean/idc/london/20180527-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/london/20180622-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180514-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [Linode](/linode/idc/london/20180514-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180514")
    * [Vultr](/vultr/idc/london/20180514-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180514")



本文最初发表于[多地到Digital Ocean伦敦[London]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-digitalocean-idc-london.html)
