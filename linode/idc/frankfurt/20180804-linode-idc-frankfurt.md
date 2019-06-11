#  多地到Linode法兰克福[Frankfurt]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode法兰克福\[Frankfurt\]机房的Ping测试（20180804）](/images/thumbnails/to_linode_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[德国-法兰克福机房](https://vps123.top/linode-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180804-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5386个有效测试样本中，共有超时点73个；响应均值为287毫秒，最快的三地区为宁夏、青海、重庆，最慢的三地区为浙江、贵州、西藏；江苏、浙江、上海、江西、广西等9处有响应超时情况；福建、云南、宁夏、江苏、浙江等6处丢包率较高。海外19个国家地区的237个有效测试样本中，共有超时点3个；响应均值为187毫秒，最快的三地区为意大利、巴西、德国，最慢的三地区为法国、澳大利亚、菲律宾；香港有响应超时情况；菲律宾、美国丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_idc_linode_germany-frankfurt_20180804_mainland.png)

大陆各省份到Linode德国-法兰克福机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
宁夏 | 32个 | 0 | 221ms | 6.6% | 湖北 | 209个 | 3个 | 287ms | 3.2%  
青海 | 16个 | 0 | 222ms | 0.8% | 均值 | 5386个 | 73个 | 287ms | 3.8%  
重庆 | 37个 | 0 | 242ms | 2.1% | 河南 | 355个 | 0 | 288ms | 3.7%  
陕西 | 166个 | 0 | 253ms | 1.8% | 山东 | 347个 | 0 | 289ms | 3.0%  
甘肃 | 112个 | 0 | 263ms | 4.0% | 安徽 | 243个 | 0 | 290ms | 4.3%  
河北 | 244个 | 0 | 264ms | 3.6% | 辽宁 | 223个 | 0 | 291ms | 2.9%  
四川 | 285个 | 0 | 270ms | 3.1% | 江苏 | 335个 | 30个 | 295ms | 6.2%  
湖南 | 261个 | 3个 | 270ms | 2.9% | 江西 | 139个 | 7个 | 296ms | 4.3%  
广西 | 239个 | 4个 | 271ms | 4.1% | 云南 | 131个 | 0 | 299ms | 7.3%  
天津 | 20个 | 0 | 276ms | 2.2% | 广东 | 440个 | 3个 | 299ms | 2.5%  
上海 | 31个 | 7个 | 276ms | 2.4% | 黑龙江 | 196个 | 0 | 307ms | 4.6%  
内蒙古 | 220个 | 0 | 280ms | 5.6% | 海南 | 48个 | 0 | 307ms | 3.2%  
北京 | 32个 | 0 | 283ms | 0.4% | 吉林 | 92个 | 0 | 309ms | 3.6%  
山西 | 197个 | 0 | 283ms | 1.4% | 浙江 | 254个 | 13个 | 317ms | 6.0%  
新疆 | 159个 | 0 | 285ms | 2.0% | 贵州 | 155个 | 0 | 319ms | 1.3%  
福建 | 160个 | 3个 | 287ms | 8.3% | 西藏 | 8个 | 0 | 416ms | 4.3%  
  
简评：如果你考虑在Linode的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有5386个，其中超时点73个，平均响应时间为287毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的25个，超过300毫秒的6个；  
超时点较多的省份：上海；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_idc_linode_germany-frankfurt_20180804_overseas.png)

海外线路到Linode德国-法兰克福机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
意大利 | 3个 | 0 | 9ms | - | 香港 | 66个 | 3个 | 193ms | 0  
巴西 | 3个 | 0 | 16ms | 0 | 南非 | 6个 | 0 | 196ms | 1.0%  
德国 | 9个 | 0 | 21ms | 0 | 印度尼西亚 | 6个 | 0 | 213ms | 0  
俄罗斯 | 3个 | 0 | 42ms | - | 马来西亚 | 12个 | 0 | 251ms | 1.0%  
英国 | 6个 | 0 | 48ms | 0 | 台湾 | 3个 | 0 | 266ms | 0  
加拿大 | 15个 | 0 | 97ms | 0 | 日本 | 6个 | 0 | 277ms | 1.7%  
荷兰 | 3个 | 0 | 149ms | 0 | 韩国 | 21个 | 0 | 284ms | 0  
美国 | 48个 | 0 | 166ms | 11.5% | 法国 | 3个 | 0 | 308ms | 0  
新加坡 | 15个 | 0 | 178ms | 0 | 澳大利亚 | 6个 | 0 | 333ms | 0  
均值 | 237个 | 3个 | 187ms | 1.7% | 菲律宾 | 3个 | 0 | 519ms | 13.3%  
  
简评：如果你考虑在Linode的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有237个，其中超时点3个，平均响应时间为187毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的5个，超过300毫秒的3个；  
丢包率较高的国家/地区：美国、菲律宾；

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
    * [佛利蒙](/linode/idc/fremont/20180804-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180804")
    * [伦敦](/linode/idc/london/20180804-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180804")
    * [纽瓦克](/linode/idc/newark/20180804-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180804")
    * [新加坡](/linode/idc/singapore/20180804-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180804")
    * [东京](/linode/idc/tokyo/20180804-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180804")
  * 到Linode法兰克福机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/frankfurt/20180514-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180514")
    * [20180527](/linode/idc/frankfurt/20180527-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180527")
    * [20180622](/linode/idc/frankfurt/20180622-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180622")
    * [20180918](/linode/idc/frankfurt/20180918-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180804-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [Vultr](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")



本文最初发表于[多地到Linode法兰克福[Frankfurt]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-linode-idc-frankfurt.html)
