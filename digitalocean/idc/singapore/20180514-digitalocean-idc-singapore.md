#  多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean新加坡\[Singapore\]机房的Ping测试（20180514）](/images/thumbnails/to_do_Singapore.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[新加坡-新加坡机房](https://vps123.top/digitalocean-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180514-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Digital Ocean新加坡-新加坡机房的PING测试结果，连通概况如下：大陆31个省市的925个有效测试样本中，共有超时点13个；响应均值为195毫秒，最快的三地区为北京、河南、天津，最慢的三地区为湖北、新疆、四川；山东、江苏、浙江、广西、北京等9处有响应超时情况；四川、湖北、辽宁、河北、云南等10处丢包率较高。海外19个国家地区的82个有效测试样本中，无超时点；响应均值为173毫秒，最快的三地区为新加坡、马来西亚、香港，最慢的三地区为俄罗斯、南非、巴西；柬埔寨、印度尼西亚丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_singapore-singapore_20180514_mainland.png)

大陆各省份到Digital Ocean新加坡-新加坡机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 8个 | 1个 | 140ms | 5.7% | 吉林 | 14个 | 0 | 190ms | 0.1%  
河南 | 48个 | 0 | 145ms | 2.7% | 安徽 | 39个 | 0 | 190ms | 1.1%  
天津 | 5个 | 0 | 150ms | 2.3% | 云南 | 22个 | 0 | 192ms | 6.7%  
上海 | 9个 | 1个 | 162ms | 3.1% | 宁夏 | 10个 | 0 | 194ms | 2.3%  
黑龙江 | 36个 | 0 | 163ms | 1.7% | 均值 | 925个 | 13个 | 195ms | 4.2%  
西藏 | 1个 | 0 | 164ms | 0 | 甘肃 | 22个 | 0 | 198ms | 1.1%  
山东 | 50个 | 2个 | 170ms | 4.8% | 海南 | 11个 | 0 | 205ms | 3.0%  
陕西 | 30个 | 1个 | 174ms | 1.0% | 广西 | 37个 | 2个 | 208ms | 6.2%  
江苏 | 56个 | 2个 | 175ms | 1.6% | 贵州 | 28个 | 0 | 212ms | 6.5%  
广东 | 75个 | 1个 | 175ms | 3.9% | 内蒙古 | 32个 | 0 | 214ms | 4.9%  
湖南 | 42个 | 0 | 175ms | 3.6% | 重庆 | 14个 | 0 | 215ms | 2.7%  
江西 | 22个 | 0 | 176ms | 5.2% | 辽宁 | 37个 | 0 | 217ms | 7.2%  
福建 | 34个 | 1个 | 177ms | 2.5% | 河北 | 33个 | 0 | 236ms | 6.9%  
浙江 | 50个 | 2个 | 185ms | 1.3% | 湖北 | 46个 | 0 | 243ms | 8.3%  
青海 | 4个 | 0 | 186ms | 0 | 新疆 | 24个 | 0 | 248ms | 4.5%  
山西 | 37个 | 0 | 186ms | 5.7% | 四川 | 49个 | 0 | 269ms | 9.5%  
  
简评：如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有925个，其中超时点13个，平均响应时间为195毫秒，丢包率为4%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的21个，在200-300毫秒间的10个；  
超时点较多的省份：北京、上海；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_singapore-singapore_20180514_overseas.png)

海外线路到Digital Ocean新加坡-新加坡机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
新加坡 | 6个 | 0 | 1ms | 0 | 英国 | 2个 | 0 | 180ms | 0.5%  
马来西亚 | 3个 | 0 | 44ms | 0 | 美国 | 19个 | 0 | 185ms | 2.2%  
香港 | 19个 | 0 | 55ms | 0 | 澳大利亚 | 2个 | 0 | 196ms | 0  
菲律宾 | 1个 | 0 | 56ms | 0 | 德国 | 2个 | 0 | 227ms | 0  
台湾 | 1个 | 0 | 65ms | - | 柬埔寨 | 1个 | 0 | 245ms | 10.0%  
日本 | 2个 | 0 | 84ms | 0 | 加拿大 | 3个 | 0 | 250ms | 1.5%  
韩国 | 13个 | 0 | 103ms | 0 | 法国 | 2个 | 0 | 275ms | 0  
印度尼西亚 | 1个 | 0 | 134ms | 6.0% | 俄罗斯 | 1个 | 0 | 333ms | 0  
荷兰 | 1个 | 0 | 161ms | 0 | 南非 | 2个 | 0 | 346ms | 0  
均值 | 82个 | 0 | 173ms | 1.1% | 巴西 | 1个 | 0 | 351ms | 0  
  
简评：如果你考虑在Digital Ocean的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有82个，其中超时点0个，平均响应时间为173毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的4个，在100-200毫秒间的6个，在200-300毫秒间的4个，超过300毫秒的3个；  
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
    * [伦敦](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [纽约](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [多伦多](/digitalocean/idc/toronto/20180514-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180514")
  * 到Digital Ocean新加坡机房的 _其他近期报告_ ： 
    * [20180527](/digitalocean/idc/singapore/20180527-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/singapore/20180622-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180514-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [Linode](/linode/idc/singapore/20180514-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180514")
    * [Vultr](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")



本文最初发表于[多地到Digital Ocean新加坡[Singapore]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-digitalocean-idc-singapore.html)
