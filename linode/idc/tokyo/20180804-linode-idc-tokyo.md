#  多地到Linode东京[Tokyo]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode东京\[Tokyo\]机房的Ping测试（20180804）](/images/thumbnails/to_linode_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[日本-东京机房](https://vps123.top/linode-facilities.html#tokyo)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的日本-东京机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180804-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5342个有效测试样本中，共有超时点72个；响应均值为201毫秒，最快的三地区为广东、湖南、上海，最慢的三地区为青海、新疆、吉林；浙江、江苏、上海、贵州、江西等14处有响应超时情况；安徽、福建、青海、江西、江苏等31处丢包率较高。海外19个国家地区的237个有效测试样本中，共有超时点3个；响应均值为167毫秒，最快的三地区为日本、台湾、韩国，最慢的三地区为俄罗斯、英国、菲律宾；韩国有响应超时情况；菲律宾丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_idc_linode_japan-tokyo_20180804_mainland.png)

大陆各省份到Linode日本-东京机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
广东 | 442个 | 2个 | 156ms | 7.8% | 河北 | 252个 | 0 | 204ms | 14.9%  
湖南 | 242个 | 4个 | 169ms | 11.3% | 重庆 | 34个 | 2个 | 204ms | 20.8%  
上海 | 26个 | 6个 | 169ms | 28.8% | 北京 | 32个 | 0 | 207ms | 20.9%  
海南 | 52个 | 0 | 178ms | 17.3% | 江苏 | 328个 | 14个 | 209ms | 30.0%  
贵州 | 156个 | 6个 | 180ms | 14.0% | 四川 | 282个 | 2个 | 211ms | 16.1%  
福建 | 168个 | 2个 | 183ms | 34.6% | 山西 | 186个 | 2个 | 211ms | 20.2%  
江西 | 134个 | 6个 | 184ms | 32.8% | 宁夏 | 32个 | 0 | 216ms | 29.8%  
河南 | 350个 | 0 | 188ms | 19.3% | 黑龙江 | 204个 | 0 | 222ms | 16.8%  
浙江 | 228个 | 16个 | 188ms | 25.7% | 陕西 | 174个 | 4个 | 223ms | 15.7%  
山东 | 368个 | 0 | 193ms | 25.5% | 甘肃 | 112个 | 0 | 230ms | 23.9%  
广西 | 232个 | 0 | 193ms | 14.6% | 西藏 | 8个 | 0 | 231ms | 5.5%  
安徽 | 234个 | 0 | 197ms | 36.7% | 内蒙古 | 224个 | 0 | 236ms | 20.5%  
湖北 | 206个 | 2个 | 199ms | 18.5% | 辽宁 | 224个 | 4个 | 246ms | 25.9%  
云南 | 126个 | 0 | 199ms | 19.3% | 青海 | 16个 | 0 | 254ms | 34.3%  
均值 | 5342个 | 72个 | 201ms | 20.7% | 新疆 | 162个 | 0 | 255ms | 21.1%  
天津 | 12个 | 0 | 202ms | 23.7% | 吉林 | 96个 | 0 | 261ms | 25.6%  
  
简评：如果你考虑在Linode的东京[Tokyo]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有5342个，其中超时点72个，平均响应时间为201毫秒，丢包率为20%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的14个，在200-300毫秒间的17个；  
超时点较多的省份：上海；  
丢包率较高的省份：湖南、上海、海南、贵州、福建、江西、河南、浙江、山东、广西、安徽、湖北、云南、天津、河北、重庆、北京、江苏、四川、山西、宁夏、黑龙江、陕西、甘肃、内蒙古、辽宁、青海、新疆、吉林；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于东京\[Tokyo\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_idc_linode_japan-tokyo_20180804_overseas.png)

海外线路到Linode日本-东京机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
日本 | 6个 | 0 | 18ms | 0 | 法国 | 3个 | 0 | 113ms | 0  
台湾 | 3个 | 0 | 58ms | 0 | 均值 | 237个 | 3个 | 167ms | 0.5%  
韩国 | 21个 | 3个 | 72ms | 0 | 加拿大 | 15个 | 0 | 175ms | 0  
印度尼西亚 | 6个 | 0 | 95ms | 0 | 巴西 | 3个 | 0 | 224ms | 0  
香港 | 66个 | 0 | 96ms | 0 | 意大利 | 3个 | 0 | 233ms | -  
新加坡 | 15个 | 0 | 106ms | 0 | 南非 | 6个 | 0 | 254ms | 0.5%  
马来西亚 | 12个 | 0 | 108ms | 1.0% | 德国 | 9个 | 0 | 263ms | 0  
美国 | 48个 | 0 | 109ms | 0.5% | 俄罗斯 | 3个 | 0 | 276ms | -  
澳大利亚 | 6个 | 0 | 110ms | 0 | 英国 | 6个 | 0 | 280ms | 0  
荷兰 | 3个 | 0 | 112ms | 0 | 菲律宾 | 3个 | 0 | 470ms | 6.7%  
  
简评：如果你考虑在Linode的东京[Tokyo]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于东京[Tokyo]的机房的连通状况。到此机房的ping监测点共有237个，其中超时点3个，平均响应时间为167毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的4个，在100-200毫秒间的7个，在200-300毫秒间的6个，超过300毫秒的1个；  
超时点较多的国家/地区：韩国；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180804 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180804 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180804-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180804")
    * [达拉斯](/linode/idc/dallas/20180804-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180804")
    * [法兰克福](/linode/idc/frankfurt/20180804-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180804")
    * [佛利蒙](/linode/idc/fremont/20180804-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180804")
    * [伦敦](/linode/idc/london/20180804-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180804")
    * [纽瓦克](/linode/idc/newark/20180804-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180804")
    * [新加坡](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")
  * 到Linode东京机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/tokyo/20180514-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180514")
    * [20180527](/linode/idc/tokyo/20180527-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180527")
    * [20180622](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")
    * [20180918](/linode/idc/tokyo/20180918-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180918")
  * 本期报告：在东京部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")



本文最初发表于[多地到Linode东京[Tokyo]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-linode-idc-tokyo.html)
