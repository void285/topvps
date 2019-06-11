#  多地到BandwagonHost洛杉矶[LosAngeles]机房的Ping测试（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到BandwagonHost洛杉矶\[LosAngeles\]机房的Ping测试（20180426）](/images/thumbnails/to_bwg_LosAngeles.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[BandwagonHost](https://vps123.top/go/bwg)的[美国-洛杉矶机房](https://vps123.top/bandwagon-facilities.html#losangeles)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[BandwagonHost](https://vps123.top/go/bwg)的美国-洛杉矶机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[BandwagonHost全部机房](/bandwagon/isp/china/20180426-bandwagon-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426多地到BandwagonHost美国-洛杉矶机房的PING测试结果，连通概况如下：大陆28个省市的465个有效测试样本中，共有超时点12个；响应均值为202毫秒，最快的三地区为江苏、广东、北京，最慢的三地区为重庆、甘肃、新疆；浙江、陕西、北京、海南、福建有响应超时情况；黑龙江、安徽、重庆、北京、福建等6处丢包率较高。海外15个国家地区的266个有效测试样本中，共有超时点3个；响应均值为156毫秒，最快的三地区为美国、加拿大、日本，最慢的三地区为马来西亚、俄罗斯、南非；美国、加拿大、香港有响应超时情况。

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商BandwagonHost位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/bwg_20180426/plot_idc_bwg_usa-losangeles_20180426_mainland.png)

大陆各省份到BandwagonHost美国-洛杉矶机房的测速数据 [20180426] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
江苏 | 32个 | 0 | 176ms | 3.5% | 江西 | 8个 | 0 | 205ms | 4.2%  
广东 | 40个 | 0 | 180ms | 2.9% | 内蒙古 | 16个 | 0 | 209ms | 3.6%  
北京 | 16个 | 2个 | 183ms | 5.5% | 辽宁 | 24个 | 0 | 210ms | 4.9%  
上海 | 12个 | 0 | 185ms | 2.8% | 黑龙江 | 12个 | 0 | 212ms | 6.9%  
湖北 | 12个 | 0 | 189ms | 3.6% | 云南 | 8个 | 0 | 212ms | 4.2%  
广西 | 12个 | 0 | 189ms | 3.6% | 贵州 | 16个 | 0 | 214ms | 3.3%  
海南 | 4个 | 1个 | 192ms | 2.2% | 安徽 | 19个 | 0 | 214ms | 5.6%  
吉林 | 4个 | 0 | 193ms | 3.3% | 天津 | 12个 | 0 | 217ms | 0.8%  
湖南 | 12个 | 0 | 194ms | 5.4% | 山东 | 4个 | 0 | 218ms | 5.0%  
河北 | 8个 | 0 | 197ms | 3.8% | 河南 | 31个 | 0 | 219ms | 2.4%  
福建 | 40个 | 1个 | 198ms | 5.5% | 陕西 | 24个 | 4个 | 219ms | 2.7%  
四川 | 8个 | 0 | 200ms | 5.0% | 重庆 | 12个 | 0 | 229ms | 5.6%  
均值 | 465个 | 12个 | 202ms | 4.0% | 甘肃 | 4个 | 0 | 272ms | 2.5%  
山西 | 8个 | 0 | 203ms | 1.7% | 新疆 | 4个 | 0 | 281ms | 5.0%  
浙江 | 63个 | 4个 | 205ms | 4.2% |  |  |  |  |   
  
简评：如果你考虑在BandwagonHost的洛杉矶[LosAngeles]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有465个，其中超时点12个，平均响应时间为202毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的12个，在200-300毫秒间的16个；  
超时点较多的省份：北京、海南、陕西；

## 海外测速点

![海外各国家地区到VPS提供商BandwagonHost位于洛杉矶\[LosAngeles\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/bwg_20180426/plot_idc_bwg_usa-losangeles_20180426_overseas.png)

海外线路到BandwagonHost美国-洛杉矶机房的测速数据 [20180426] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 76个 | 1个 | 12ms | 0.3% | 台湾 | 4个 | 0 | 155ms | -  
加拿大 | 4个 | 1个 | 69ms | - | 韩国 | 44个 | 0 | 156ms | 0.2%  
日本 | 4个 | 0 | 114ms | 2.5% | 均值 | 266个 | 3个 | 156ms | 0.3%  
英国 | 8个 | 0 | 140ms | 0 | 香港 | 74个 | 1个 | 172ms | 0  
荷兰 | 8个 | 0 | 143ms | 0 | 新加坡 | 20个 | 0 | 183ms | 1.3%  
德国 | 4个 | 0 | 153ms | 0 | 马来西亚 | 4个 | 0 | 188ms | 0  
法国 | 4个 | 0 | 155ms | 0 | 俄罗斯 | 4个 | 0 | 250ms | 0  
澳大利亚 | 4个 | 0 | 155ms | 0 | 南非 | 4个 | 0 | 293ms | 0  
  
简评：如果你考虑在BandwagonHost的洛杉矶[LosAngeles]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于洛杉矶[LosAngeles]的机房的连通状况。到此机房的ping监测点共有266个，其中超时点3个，平均响应时间为156毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的11个，在200-300毫秒间的2个；  
超时点较多的国家/地区：加拿大；

[注册 BandwagonHost](https://vps123.top/go/bwg/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [BandwagonHost](https://vps123.top/pingtests/idc-bandwagon/20180426 "本期BandwagonHost的全部测速报告")
    * [各地到BandwagonHost某机房](https://vps123.top/pingtests/idc-bandwagon/isp-global/20180426 "以BandwagonHost某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到BandwagonHost各机房](https://vps123.top/pingtests/idc-bandwagon/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较BandwagonHost各机房")
  * 本期到BandwagonHost _其他机房_ 的报告： 
    * [阿姆斯特丹](/bandwagon/idc/amsterdam/20180426-bandwagon-idc-amsterdam.md "多地到BandwagonHost阿姆斯特丹机房的Ping测试 20180426")
    * [佛罗里达](/bandwagon/idc/florida/20180426-bandwagon-idc-florida.md "多地到BandwagonHost佛罗里达机房的Ping测试 20180426")
    * [佛利蒙](/bandwagon/idc/fremont/20180426-bandwagon-idc-fremont.md "多地到BandwagonHost佛利蒙机房的Ping测试 20180426")
    * [香港](/bandwagon/idc/hongkong/20180426-bandwagon-idc-hongkong.md "多地到BandwagonHost香港机房的Ping测试 20180426")
    * [纽约](/bandwagon/idc/newyork/20180426-bandwagon-idc-newyork.md "多地到BandwagonHost纽约机房的Ping测试 20180426")
    * [凤凰城](/bandwagon/idc/phoenix/20180426-bandwagon-idc-phoenix.md "多地到BandwagonHost凤凰城机房的Ping测试 20180426")
    * [温哥华](/bandwagon/idc/vancouver/20180426-bandwagon-idc-vancouver.md "多地到BandwagonHost温哥华机房的Ping测试 20180426")
  * 到BandwagonHost洛杉矶机房的 _其他近期报告_ ： 
    * [20180514](/bandwagon/idc/losangeles/20180514-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180514")
    * [20180527](/bandwagon/idc/losangeles/20180527-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180527")
    * [20180622](/bandwagon/idc/losangeles/20180622-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180622")
    * [20180804](/bandwagon/idc/losangeles/20180804-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180804")
    * [20180918](/bandwagon/idc/losangeles/20180918-bandwagon-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180918")
  * 本期报告：在洛杉矶部署机房的 _其他VPS提供商_ ： 
    * [BandwagonHost](/bandwagon/idc/losangeles/20180426-bwg-idc-losangeles.md "多地到BandwagonHost洛杉矶机房的Ping测试 20180426")
    * [Vultr](/vultr/idc/losangeles/20180426-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180426")



本文最初发表于[多地到BandwagonHost洛杉矶[LosAngeles]机房的Ping测试（20180426）](https://vps123.top/pingtest/20180426-bandwagon-idc-losangeles.html)
