#  多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean新加坡\[Singapore\]机房的Ping测试（20180622）](/images/thumbnails/to_do_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[新加坡-新加坡机房](https://vps123.top/digitalocean-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180622-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的286个有效测试样本中，共有超时点19个；响应均值为270毫秒，最快的三地区为宁夏、江西、广东，最慢的三地区为吉林、内蒙古、香港；江苏、浙江、河南、陕西、四川等10处有响应超时情况；云南、天津、甘肃、新疆、内蒙古等28处丢包率较高。海外19个国家地区的88个有效测试样本中，共有超时点1个；响应均值为145毫秒，最快的三地区为新加坡、印度尼西亚、越南，最慢的三地区为加拿大、德国、意大利；韩国有响应超时情况；越南丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_singapore-singapore_20180622_mainland.png)

大陆各省份到Digital Ocean新加坡-新加坡机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
宁夏 | 3个 | 0 | 183ms | 10.0% | 云南 | 2个 | 0 | 271ms | 33.3%  
江西 | 5个 | 0 | 200ms | 12.5% | 贵州 | 7个 | 1个 | 283ms | 15.3%  
广东 | 29个 | 0 | 212ms | 12.8% | 湖南 | 9个 | 0 | 283ms | 7.0%  
山西 | 4个 | 0 | 227ms | 15.0% | 湖北 | 7个 | 0 | 284ms | 22.5%  
海南 | 4个 | 0 | 227ms | 4.2% | 天津 | 1个 | 0 | 284ms | 30.0%  
广西 | 14个 | 1个 | 239ms | 16.9% | 安徽 | 9个 | 0 | 284ms | 20.9%  
黑龙江 | 12个 | 0 | 240ms | 10.0% | 陕西 | 8个 | 2个 | 285ms | 19.6%  
福建 | 16个 | 1个 | 245ms | 11.8% | 河北 | 4个 | 0 | 287ms | 14.6%  
上海 | 3个 | 1个 | 246ms | 11.7% | 浙江 | 27个 | 4个 | 313ms | 14.0%  
河南 | 11个 | 2个 | 257ms | 8.3% | 甘肃 | 6个 | 0 | 331ms | 26.1%  
北京 | 6个 | 0 | 257ms | 11.7% | 新疆 | 9个 | 0 | 335ms | 25.4%  
辽宁 | 13个 | 1个 | 259ms | 17.1% | 四川 | 6个 | 2个 | 354ms | 9.3%  
重庆 | 5个 | 0 | 265ms | 21.1% | 吉林 | 2个 | 0 | 358ms | 16.7%  
江苏 | 26个 | 4个 | 270ms | 18.1% | 内蒙古 | 7个 | 0 | 364ms | 22.6%  
均值 | 286个 | 19个 | 270ms | 15.4% | 香港 | 24个 | 0 | - | -  
山东 | 7个 | 0 | 271ms | 12.5% |  |  |  |  |   
  
简评：如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有286个，其中超时点19个，平均响应时间为270毫秒，丢包率为15%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的2个，在200-300毫秒间的21个，超过300毫秒的6个；  
超时点较多的省份：上海、河南、江苏、贵州、陕西、浙江、四川；  
丢包率较高的省份：宁夏、江西、广东、山西、广西、黑龙江、福建、上海、北京、辽宁、重庆、江苏、山东、云南、贵州、湖北、天津、安徽、陕西、河北、浙江、甘肃、新疆、吉林、内蒙古；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_idc_do_singapore-singapore_20180622_overseas.png)

海外线路到Digital Ocean新加坡-新加坡机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
新加坡 | 5个 | 0 | 37ms | 0 | 马来西亚 | 5个 | 0 | 140ms | 1.6%  
印度尼西亚 | 1个 | 0 | 47ms | 0 | 英国 | 2个 | 0 | 143ms | 0  
越南 | 2个 | 0 | 50ms | 16.0% | 均值 | 88个 | 1个 | 145ms | 1.2%  
菲律宾 | 2个 | 0 | 59ms | 0 | 法国 | 1个 | 0 | 183ms | 0  
日本 | 2个 | 0 | 80ms | 2.0% | 美国 | 19个 | 0 | 194ms | 0  
香港 | 24个 | 0 | 85ms | 0 | 巴西 | 1个 | 0 | 199ms | 0  
台湾 | 2个 | 0 | 92ms | 0 | 南非 | 2个 | 0 | 235ms | 0  
韩国 | 14个 | 1个 | 100ms | 0 | 加拿大 | 2个 | 0 | 253ms | 0  
澳大利亚 | 1个 | 0 | 109ms | 0 | 德国 | 1个 | 0 | 314ms | -  
柬埔寨 | 1个 | 0 | 117ms | 0 | 意大利 | 1个 | 0 | 317ms | -  
  
简评：如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有88个，其中超时点1个，平均响应时间为145毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的5个，在100-200毫秒间的7个，在200-300毫秒间的2个，超过300毫秒的2个；  
丢包率较高的国家/地区：越南；

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
    * [纽约](/digitalocean/idc/newyork/20180622-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180622")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [多伦多](/digitalocean/idc/toronto/20180622-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180622")
  * 到Digital Ocean新加坡机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [20180804](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180622-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [Linode](/linode/idc/singapore/20180622-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180622")
    * [Vultr](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")



本文最初发表于[多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-digitalocean-idc-singapore.html)
