#  多地到Vultr达拉斯[Dallas]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr达拉斯\[Dallas\]机房的Ping测试（20180426）](/images/thumbnails/to_vultr_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-达拉斯机房](https://vps123.top/vultr-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180426-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到Vultr美国-达拉斯机房的PING测试结果，连通概况如下：大陆31个省市的775个有效测试样本中，共有超时点5个；响应均值为271毫秒，最快的三地区为吉林、天津、海南，最慢的三地区为甘肃、新疆、西藏；浙江、江苏、北京、重庆有响应超时情况；北京、天津、西藏、云南、甘肃等19处丢包率较高。海外18个国家地区的78个有效测试样本中，无超时点；响应均值为197毫秒，最快的三地区为美国、加拿大、荷兰，最慢的三地区为南非、印度尼西亚、柬埔寨；柬埔寨丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_idc_vultr_usa-dallas_20180426_mainland.png)

大陆各省份到Vultr美国-达拉斯机房的测速数据 [20180426] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
吉林 | 14个 | 0 | 228ms | 2.2% | 广西 | 27个 | 0 | 268ms | 6.9%  
天津 | 5个 | 0 | 233ms | 15.3% | 福建 | 26个 | 0 | 269ms | 4.3%  
海南 | 10个 | 0 | 242ms | 2.6% | 均值 | 775个 | 5个 | 271ms | 5.0%  
江苏 | 49个 | 1个 | 245ms | 3.2% | 四川 | 34个 | 0 | 274ms | 3.6%  
湖北 | 37个 | 0 | 245ms | 2.9% | 河南 | 51个 | 0 | 277ms | 6.9%  
湖南 | 34个 | 0 | 246ms | 3.8% | 陕西 | 27个 | 0 | 284ms | 5.1%  
河北 | 33个 | 0 | 254ms | 3.2% | 云南 | 24个 | 0 | 291ms | 7.0%  
浙江 | 34个 | 2个 | 255ms | 3.4% | 上海 | 8个 | 0 | 291ms | 6.3%  
北京 | 3个 | 1个 | 256ms | 20.0% | 江西 | 20个 | 0 | 294ms | 5.2%  
广东 | 51个 | 0 | 258ms | 4.2% | 内蒙古 | 27个 | 0 | 295ms | 6.3%  
贵州 | 21个 | 0 | 260ms | 5.1% | 宁夏 | 9个 | 0 | 299ms | 6.4%  
辽宁 | 35个 | 0 | 262ms | 6.8% | 安徽 | 38个 | 0 | 305ms | 5.5%  
山东 | 44个 | 0 | 263ms | 4.8% | 青海 | 4个 | 0 | 311ms | 6.5%  
黑龙江 | 29个 | 0 | 265ms | 3.7% | 甘肃 | 21个 | 0 | 323ms | 7.0%  
山西 | 28个 | 0 | 267ms | 5.8% | 新疆 | 22个 | 0 | 338ms | 6.8%  
重庆 | 9个 | 1个 | 268ms | 6.0% | 西藏 | 1个 | 0 | 392ms | 13.0%  
  
简评：如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有775个，其中超时点5个，平均响应时间为271毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的26个，超过300毫秒的5个；  
超时点较多的省份：北京、重庆；  
丢包率较高的省份：天津、北京、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_idc_vultr_usa-dallas_20180426_overseas.png)

海外线路到Vultr美国-达拉斯机房的测速数据 [20180426] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 16个 | 0 | 37ms | 0 | 澳大利亚 | 2个 | 0 | 202ms | 0  
加拿大 | 4个 | 0 | 48ms | 0 | 香港 | 18个 | 0 | 205ms | 0  
荷兰 | 2个 | 0 | 118ms | 0 | 俄罗斯 | 1个 | 0 | 205ms | 0  
法国 | 2个 | 0 | 122ms | 0 | 新加坡 | 5个 | 0 | 206ms | 0  
英国 | 3个 | 0 | 122ms | 0 | 越南 | 1个 | 0 | 231ms | 0  
德国 | 1个 | 0 | 125ms | 0 | 马来西亚 | 4个 | 0 | 265ms | 1.0%  
日本 | 3个 | 0 | 155ms | 1.0% | 南非 | 1个 | 0 | 269ms | 0  
台湾 | 1个 | 0 | 181ms | - | 印度尼西亚 | 1个 | 0 | 367ms | 5.0%  
均值 | 78个 | 0 | 197ms | 2.5% | 柬埔寨 | 1个 | 0 | 487ms | 35.0%  
韩国 | 12个 | 0 | 202ms | 0.3% |  |  |  |  |   
  
简评：如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点0个，平均响应时间为197毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在100-200毫秒间的6个，在200-300毫秒间的8个，超过300毫秒的2个；  
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
    * [法兰克福](/vultr/idc/frankfurt/20180426-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180426")
    * [伦敦](/vultr/idc/london/20180426-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180426")
    * [洛杉矶](/vultr/idc/losangeles/20180426-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180426")
    * [迈阿密](/vultr/idc/miami/20180426-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180426")
    * [新泽西](/vultr/idc/newjersey/20180426-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180426")
    * [巴黎](/vultr/idc/paris/20180426-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180426")
    * [西雅图](/vultr/idc/seattle/20180426-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180426")
    * [硅谷](/vultr/idc/siliconvalley/20180426-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180426")
    * [新加坡](/vultr/idc/singapore/20180426-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180426")
    * [悉尼](/vultr/idc/sydney/20180426-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180426")
    * [东京](/vultr/idc/tokyo/20180426-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180426")
  * 到Vultr达拉斯机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/dallas/20180514-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180514")
    * [20180527](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")
    * [20180622](/vultr/idc/dallas/20180622-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180622")
    * [20180804](/vultr/idc/dallas/20180804-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180804")
    * [20180918](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/dallas/20180426-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180426")



本文最初发表于[多地到Vultr达拉斯[Dallas]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-vultr-idc-dallas.html)
