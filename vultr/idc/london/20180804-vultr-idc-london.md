#  多地到Vultr伦敦[London]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr伦敦\[London\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_London.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[英国-伦敦机房](https://vps123.top/vultr-facilities.html#london)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的英国-伦敦机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5305个有效测试样本中，共有超时点42个；响应均值为309毫秒，最快的三地区为天津、河北、内蒙古，最慢的三地区为甘肃、新疆、西藏；江苏、广东、浙江、江西、上海等7处有响应超时情况；西藏、北京、江苏、福建、山东丢包率较高。海外19个国家地区的240个有效测试样本中，无超时点；响应均值为174毫秒，最快的三地区为巴西、意大利、德国，最慢的三地区为法国、澳大利亚、菲律宾；菲律宾、美国丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_uk-london_20180804_mainland.png)

大陆各省份到Vultr英国-伦敦机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
天津 | 20个 | 0 | 251ms | 0.7% | 海南 | 48个 | 0 | 310ms | 3.5%  
河北 | 260个 | 0 | 264ms | 2.2% | 福建 | 160个 | 0 | 313ms | 6.1%  
内蒙古 | 208个 | 0 | 287ms | 2.1% | 山东 | 358个 | 3个 | 315ms | 5.1%  
安徽 | 208个 | 0 | 291ms | 2.6% | 广西 | 248个 | 0 | 317ms | 2.3%  
湖北 | 201个 | 0 | 293ms | 2.1% | 山西 | 189个 | 0 | 317ms | 1.5%  
陕西 | 161个 | 0 | 297ms | 2.8% | 四川 | 285个 | 0 | 319ms | 1.6%  
重庆 | 45个 | 0 | 298ms | 2.5% | 宁夏 | 32个 | 0 | 320ms | 4.6%  
广东 | 446个 | 9个 | 300ms | 2.2% | 河南 | 339个 | 3个 | 323ms | 4.8%  
湖南 | 245个 | 0 | 300ms | 2.2% | 贵州 | 158个 | 0 | 331ms | 2.4%  
辽宁 | 226个 | 0 | 300ms | 1.6% | 浙江 | 246个 | 7个 | 331ms | 3.1%  
云南 | 123个 | 0 | 303ms | 2.1% | 北京 | 36个 | 0 | 332ms | 7.5%  
江西 | 139个 | 4个 | 304ms | 2.7% | 吉林 | 100个 | 0 | 344ms | 3.9%  
上海 | 31个 | 4个 | 306ms | 0.6% | 青海 | 16个 | 0 | 346ms | 3.7%  
黑龙江 | 184个 | 0 | 308ms | 1.7% | 甘肃 | 112个 | 0 | 348ms | 3.1%  
江苏 | 338个 | 12个 | 309ms | 6.2% | 新疆 | 135个 | 0 | 355ms | 1.8%  
均值 | 5305个 | 42个 | 309ms | 3.1% | 西藏 | 8个 | 0 | 436ms | 42.0%  
  
简评：如果你考虑在Vultr的伦敦[London]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有5305个，其中超时点42个，平均响应时间为309毫秒，丢包率为3%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的10个，超过300毫秒的21个；  
超时点较多的省份：上海；  
丢包率较高的省份：西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于伦敦\[London\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_uk-london_20180804_overseas.png)

海外线路到Vultr英国-伦敦机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
巴西 | 3个 | 0 | 0 | 0 | 香港 | 66个 | 0 | 194ms | 0  
意大利 | 3个 | 0 | 4ms | - | 南非 | 6个 | 0 | 213ms | 0.5%  
德国 | 9个 | 0 | 25ms | 0 | 印度尼西亚 | 6个 | 0 | 234ms | 0  
英国 | 6个 | 0 | 35ms | 0 | 马来西亚 | 12个 | 0 | 243ms | 0  
俄罗斯 | 3个 | 0 | 49ms | - | 韩国 | 21个 | 0 | 263ms | 0  
加拿大 | 15个 | 0 | 88ms | 0 | 台湾 | 3个 | 0 | 263ms | 0  
荷兰 | 3个 | 0 | 128ms | 0 | 日本 | 6个 | 0 | 267ms | 3.3%  
美国 | 48个 | 0 | 153ms | 5.7% | 法国 | 3个 | 0 | 296ms | 0  
均值 | 240个 | 0 | 174ms | 2.7% | 澳大利亚 | 6个 | 0 | 299ms | 0  
新加坡 | 15个 | 0 | 183ms | 0 | 菲律宾 | 6个 | 0 | 373ms | 36.0%  
  
简评：如果你考虑在Vultr的伦敦[London]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于伦敦[London]的机房的连通状况。到此机房的ping监测点共有240个，其中超时点0个，平均响应时间为174毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在50-100毫秒间的1个，在100-200毫秒间的4个，在200-300毫秒间的8个，超过300毫秒的1个；  
丢包率较高的国家/地区：菲律宾；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180804 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180804 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180804-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180804")
    * [亚特兰大](/vultr/idc/atlanta/20180804-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180804")
    * [芝加哥](/vultr/idc/chicago/20180804-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180804")
    * [达拉斯](/vultr/idc/dallas/20180804-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180804")
    * [法兰克福](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")
    * [洛杉矶](/vultr/idc/losangeles/20180804-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180804")
    * [迈阿密](/vultr/idc/miami/20180804-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180804")
    * [新泽西](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr伦敦机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/london/20180514-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180514")
    * [20180527](/vultr/idc/london/20180527-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180527")
    * [20180622](/vultr/idc/london/20180622-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180622")
    * [20180918](/vultr/idc/london/20180918-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180918")
  * 本期报告：在伦敦部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/london/20180804-do-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [Linode](/linode/idc/london/20180804-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180804")



本文最初发表于[多地到Vultr伦敦[London]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-london.html)
