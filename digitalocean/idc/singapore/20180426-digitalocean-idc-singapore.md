#  多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean新加坡\[Singapore\]机房的Ping测试（20180426）](/images/thumbnails/to_do_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[新加坡-新加坡机房](https://vps123.top/digitalocean-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180426-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Digital Ocean新加坡-新加坡机房的PING测试结果，连通概况如下：大陆31个省市的813个有效测试样本中，共有超时点7个；响应均值为190毫秒，最快的三地区为天津、广东、河南，最慢的三地区为新疆、宁夏、四川；浙江、北京、上海、江苏、山西等6处有响应超时情况；北京、辽宁丢包率较高。海外17个国家地区的73个有效测试样本中，无超时点；响应均值为176毫秒，最快的三地区为新加坡、马来西亚、台湾，最慢的三地区为俄罗斯、柬埔寨、南非；柬埔寨丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_singapore-singapore_20180426_mainland.png)

大陆各省份到Digital Ocean新加坡-新加坡机房的测速数据 [20180426] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
天津 | 5个 | 0 | 143ms | 2.0% | 青海 | 4个 | 0 | 190ms | 0  
广东 | 57个 | 0 | 154ms | 0.2% | 海南 | 10个 | 0 | 190ms | 0.1%  
河南 | 50个 | 0 | 157ms | 2.1% | 均值 | 813个 | 7个 | 190ms | 2.4%  
湖南 | 37个 | 0 | 163ms | 1.0% | 重庆 | 9个 | 0 | 192ms | 0  
北京 | 4个 | 1个 | 173ms | 6.0% | 湖北 | 38个 | 0 | 194ms | 1.8%  
广西 | 35个 | 0 | 174ms | 2.4% | 陕西 | 27个 | 0 | 197ms | 1.6%  
西藏 | 1个 | 0 | 174ms | 1.0% | 河北 | 29个 | 0 | 206ms | 4.1%  
山东 | 44个 | 0 | 177ms | 3.7% | 山西 | 33个 | 1个 | 206ms | 2.8%  
安徽 | 37个 | 0 | 177ms | 4.3% | 吉林 | 15个 | 0 | 210ms | 0.2%  
上海 | 6个 | 1个 | 177ms | 1.8% | 甘肃 | 20个 | 0 | 219ms | 1.7%  
浙江 | 35个 | 2个 | 179ms | 1.8% | 辽宁 | 34个 | 0 | 219ms | 5.2%  
江西 | 22个 | 0 | 181ms | 2.8% | 贵州 | 22个 | 0 | 220ms | 1.5%  
云南 | 28个 | 0 | 182ms | 1.9% | 内蒙古 | 31个 | 1个 | 221ms | 2.3%  
福建 | 24个 | 0 | 185ms | 2.5% | 新疆 | 26个 | 0 | 223ms | 2.0%  
黑龙江 | 31个 | 0 | 187ms | 3.3% | 宁夏 | 11个 | 0 | 229ms | 3.3%  
江苏 | 47个 | 1个 | 189ms | 4.1% | 四川 | 41个 | 0 | 233ms | 1.2%  
  
简评：如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有813个，其中超时点7个，平均响应时间为190毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的21个，在200-300毫秒间的10个；  
超时点较多的省份：北京、上海；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/do_20180426/plot_idc_do_singapore-singapore_20180426_overseas.png)

海外线路到Digital Ocean新加坡-新加坡机房的测速数据 [20180426] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
新加坡 | 5个 | 0 | 1ms | 0 | 美国 | 16个 | 0 | 184ms | 0  
马来西亚 | 2个 | 0 | 27ms | 0 | 英国 | 2个 | 0 | 187ms | 0  
台湾 | 1个 | 0 | 65ms | - | 德国 | 1个 | 0 | 202ms | 0  
香港 | 20个 | 0 | 69ms | 0 | 荷兰 | 2个 | 0 | 218ms | 0  
日本 | 2个 | 0 | 78ms | 0 | 加拿大 | 3个 | 0 | 245ms | 0  
越南 | 1个 | 0 | 79ms | 0 | 法国 | 2个 | 0 | 292ms | 0  
韩国 | 12个 | 0 | 105ms | 3.2% | 俄罗斯 | 1个 | 0 | 344ms | 0  
澳大利亚 | 1个 | 0 | 141ms | 0 | 柬埔寨 | 1个 | 0 | 363ms | 12.0%  
均值 | 73个 | 0 | 176ms | 0.9% | 南非 | 1个 | 0 | 396ms | 0  
  
简评：如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有73个，其中超时点0个，平均响应时间为176毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的4个，在100-200毫秒间的4个，在200-300毫秒间的4个，超过300毫秒的3个；  
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
    * [伦敦](/digitalocean/idc/london/20180426-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180426")
    * [纽约](/digitalocean/idc/newyork/20180426-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180426")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180426-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180426")
    * [多伦多](/digitalocean/idc/toronto/20180426-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180426")
  * 到Digital Ocean新加坡机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180426-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180426")
    * [Linode](/linode/idc/singapore/20180426-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180426")
    * [Vultr](/vultr/idc/singapore/20180426-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180426")



本文最初发表于[多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-digitalocean-idc-singapore.html)
