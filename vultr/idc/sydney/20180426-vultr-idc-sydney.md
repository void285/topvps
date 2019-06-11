#  多地到Vultr悉尼[Sydney]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr悉尼\[Sydney\]机房的Ping测试（20180426）](/images/thumbnails/to_vultr_Sydney.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[澳大利亚-悉尼机房](https://vps123.top/vultr-facilities.html#sydney)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的澳大利亚-悉尼机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180426-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Vultr澳大利亚-悉尼机房的PING测试结果，连通概况如下：大陆31个省市的781个有效测试样本中，共有超时点7个；响应均值为240毫秒，最快的三地区为天津、北京、山西，最慢的三地区为四川、河北、新疆；浙江、上海、江苏、黑龙江、内蒙古等6处有响应超时情况；上海丢包率较高。海外17个国家地区的76个有效测试样本中，共有超时点1个；响应均值为245毫秒，最快的三地区为澳大利亚、新加坡、台湾，最慢的三地区为德国、南非、柬埔寨；韩国有响应超时情况；柬埔寨丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_idc_vultr_australia-sydney_20180426_mainland.png)

大陆各省份到Vultr澳大利亚-悉尼机房的测速数据 [20180426] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
天津 | 5个 | 0 | 192ms | 2.5% | 内蒙古 | 26个 | 1个 | 238ms | 1.3%  
北京 | 4个 | 0 | 202ms | 4.0% | 广西 | 29个 | 0 | 239ms | 2.8%  
山西 | 28个 | 0 | 213ms | 1.0% | 山东 | 43个 | 0 | 240ms | 3.8%  
湖南 | 36个 | 0 | 224ms | 1.0% | 均值 | 781个 | 7个 | 240ms | 1.8%  
吉林 | 14个 | 0 | 225ms | 0 | 安徽 | 35个 | 0 | 241ms | 1.0%  
河南 | 51个 | 0 | 226ms | 3.0% | 云南 | 24个 | 0 | 246ms | 1.5%  
上海 | 8个 | 1个 | 227ms | 7.1% | 西藏 | 1个 | 0 | 247ms | 0  
江苏 | 49个 | 1个 | 228ms | 1.0% | 青海 | 4个 | 0 | 248ms | 0.8%  
黑龙江 | 29个 | 1个 | 228ms | 1.8% | 宁夏 | 9个 | 0 | 249ms | 2.4%  
福建 | 28个 | 0 | 229ms | 2.0% | 湖北 | 38个 | 0 | 251ms | 1.6%  
浙江 | 35个 | 2个 | 229ms | 1.2% | 重庆 | 9个 | 1个 | 253ms | 1.0%  
辽宁 | 36个 | 0 | 232ms | 2.4% | 甘肃 | 21个 | 0 | 257ms | 2.1%  
陕西 | 26个 | 0 | 233ms | 1.7% | 贵州 | 21个 | 0 | 262ms | 2.4%  
广东 | 51个 | 0 | 234ms | 1.7% | 四川 | 34个 | 0 | 267ms | 2.2%  
海南 | 10个 | 0 | 235ms | 1.5% | 河北 | 33个 | 0 | 280ms | 1.0%  
江西 | 21个 | 0 | 237ms | 1.4% | 新疆 | 23个 | 0 | 287ms | 1.5%  
  
简评：如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有781个，其中超时点7个，平均响应时间为240毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的1个，在200-300毫秒间的30个；  
超时点较多的省份：上海、重庆；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于悉尼\[Sydney\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_idc_vultr_australia-sydney_20180426_overseas.png)

海外线路到Vultr澳大利亚-悉尼机房的测速数据 [20180426] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
澳大利亚 | 2个 | 0 | 6ms | 0 | 加拿大 | 3个 | 0 | 249ms | 0.7%  
新加坡 | 5个 | 0 | 129ms | 0 | 越南 | 1个 | 0 | 287ms | 0  
台湾 | 1个 | 0 | 161ms | - | 荷兰 | 2个 | 0 | 306ms | 0  
日本 | 2个 | 0 | 162ms | 0.5% | 俄罗斯 | 1个 | 0 | 310ms | 0  
香港 | 20个 | 0 | 163ms | 0 | 法国 | 2个 | 0 | 314ms | 0  
美国 | 16个 | 0 | 168ms | 0 | 英国 | 3个 | 0 | 317ms | 0  
马来西亚 | 3个 | 0 | 174ms | 0 | 德国 | 1个 | 0 | 319ms | 0  
韩国 | 12个 | 1个 | 187ms | 4.8% | 南非 | 1个 | 0 | 457ms | 0  
均值 | 76个 | 1个 | 245ms | 1.8% | 柬埔寨 | 1个 | 0 | 470ms | 23.0%  
  
简评：如果你考虑在Vultr的悉尼[Sydney]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于悉尼[Sydney]的机房的连通状况。到此机房的ping监测点共有76个，其中超时点1个，平均响应时间为245毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的7个，在200-300毫秒间的2个，超过300毫秒的7个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180426 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180426 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180426-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180426")
    * [亚特兰大](/vultr/idc/atlanta/20180426-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180426")
    * [芝加哥](/vultr/idc/chicago/20180426-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180426")
    * [达拉斯](/vultr/idc/dallas/20180426-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180426")
    * [法兰克福](/vultr/idc/frankfurt/20180426-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180426")
    * [伦敦](/vultr/idc/london/20180426-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180426")
    * [洛杉矶](/vultr/idc/losangeles/20180426-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180426")
    * [迈阿密](/vultr/idc/miami/20180426-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180426")
    * [新泽西](/vultr/idc/newjersey/20180426-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180426")
    * [巴黎](/vultr/idc/paris/20180426-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180426")
    * [西雅图](/vultr/idc/seattle/20180426-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180426")
    * [硅谷](/vultr/idc/siliconvalley/20180426-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180426")
    * [新加坡](/vultr/idc/singapore/20180426-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180426")
    * [东京](/vultr/idc/tokyo/20180426-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180426")
  * 到Vultr悉尼机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [20180527](/vultr/idc/sydney/20180527-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180527")
    * [20180622](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [20180804](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [20180918](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")



本文最初发表于[多地到Vultr悉尼[Sydney]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-vultr-idc-sydney.html)
