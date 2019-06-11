#  多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean旧金山\[SanFrancisco\]机房的Ping测试（20180426）](/images/thumbnails/to_do_SanFrancisco.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-旧金山机房](https://vps123.top/digitalocean-facilities.html#sanfrancisco)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-旧金山机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180426-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Digital Ocean美国-旧金山机房的PING测试结果，连通概况如下：大陆31个省市的1622个有效测试样本中，共有超时点14个；响应均值为245毫秒，最快的三地区为北京、河南、山西，最慢的三地区为青海、甘肃、新疆；浙江、河南、江苏、云南、北京等9处有响应超时情况；北京、上海、海南、天津、青海等9处丢包率较高。海外18个国家地区的160个有效测试样本中，共有超时点2个；响应均值为179毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为俄罗斯、南非、柬埔寨；香港有响应超时情况；英国丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_usa-sanfrancisco_20180426_mainland.png)

**大陆各省份到Digital Ocean美国-旧金山机房的测速数据 [20180426]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
北京 | 7个 | 1个 | 213ms | 12.8%  
河南 | 104个 | 2个 | 216ms | 3.6%  
山西 | 62个 | 0 | 222ms | 3.3%  
山东 | 86个 | 0 | 225ms | 2.8%  
上海 | 12个 | 0 | 229ms | 8.9%  
湖北 | 75个 | 0 | 233ms | 2.3%  
重庆 | 17个 | 1个 | 233ms | 1.2%  
天津 | 10个 | 1个 | 235ms | 6.4%  
湖南 | 80个 | 0 | 235ms | 4.7%  
河北 | 56个 | 1个 | 238ms | 3.5%  
黑龙江 | 59个 | 0 | 239ms | 5.4%  
江苏 | 99个 | 2个 | 242ms | 3.1%  
广东 | 108个 | 0 | 243ms | 2.6%  
福建 | 46个 | 0 | 245ms | 3.3%  
广西 | 68个 | 0 | 245ms | 5.7%  
辽宁 | 70个 | 0 | 245ms | 5.6%  
均值 | 1622个 | 14个 | 245ms | 4.0%  
江西 | 46个 | 1个 | 246ms | 2.4%  
浙江 | 73个 | 3个 | 248ms | 5.2%  
陕西 | 56个 | 0 | 248ms | 3.4%  
安徽 | 71个 | 0 | 248ms | 3.7%  
海南 | 20个 | 0 | 254ms | 6.8%  
云南 | 50个 | 2个 | 255ms | 5.0%  
吉林 | 32个 | 0 | 256ms | 3.2%  
贵州 | 47个 | 0 | 262ms | 4.7%  
内蒙古 | 60个 | 0 | 262ms | 4.5%  
宁夏 | 21个 | 0 | 265ms | 5.0%  
西藏 | 2个 | 0 | 267ms | 0.5%  
四川 | 85个 | 0 | 268ms | 3.8%  
青海 | 8个 | 0 | 282ms | 5.8%  
甘肃 | 38个 | 0 | 285ms | 4.7%  
新疆 | 54个 | 0 | 289ms | 4.3%  
  
**简评：** 如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有1622个，其中超时点14个，平均响应时间为245毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的31个；  
超时点较多的省份：北京；  
丢包率较高的省份：北京；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_usa-sanfrancisco_20180426_overseas.png)

**海外线路到Digital Ocean美国-旧金山机房的测速数据 [20180426]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
美国 | 32个 | 0 | 20ms | 0  
加拿大 | 8个 | 0 | 74ms | 0  
日本 | 6个 | 0 | 116ms | 0.8%  
荷兰 | 4个 | 0 | 144ms | 0  
韩国 | 24个 | 0 | 150ms | 1.1%  
香港 | 40个 | 2个 | 151ms | 0  
法国 | 4个 | 0 | 152ms | 0  
台湾 | 2个 | 0 | 163ms | -  
德国 | 2个 | 0 | 169ms | 0  
澳大利亚 | 4个 | 0 | 174ms | 0  
英国 | 6个 | 0 | 176ms | 6.0%  
新加坡 | 10个 | 0 | 179ms | 0  
均值 | 160个 | 2个 | 179ms | 0.7%  
越南 | 2个 | 0 | 205ms | 0  
马来西亚 | 8个 | 0 | 213ms | 0.4%  
印度尼西亚 | 2个 | 0 | 218ms | 3.5%  
俄罗斯 | 2个 | 0 | 243ms | 0  
南非 | 2个 | 0 | 295ms | 0  
柬埔寨 | 2个 | 0 | 389ms | 0.5%  
  
**简评：** 如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有160个，其中超时点2个，平均响应时间为179毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的10个，在200-300毫秒间的5个，超过300毫秒的1个；

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
    * [伦敦](/digitalocean/idc/london/20180426-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180426")
    * [纽约](/digitalocean/idc/newyork/20180426-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180426")
    * [新加坡](/digitalocean/idc/singapore/20180426-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180426")
    * [多伦多](/digitalocean/idc/toronto/20180426-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180426")
  * 到Digital Ocean旧金山机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/sanfrancisco/20180918-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180918")



本文最初发表于[多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-digitalocean-idc-sanfrancisco.html)
