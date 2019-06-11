#  多地到Linode达拉斯[Dallas]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode达拉斯\[Dallas\]机房的Ping测试（20180622）](/images/thumbnails/to_linode_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-达拉斯机房](https://vps123.top/linode-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180622-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的860个有效测试样本中，共有超时点23个；响应均值为244毫秒，最快的三地区为天津、上海、北京，最慢的三地区为宁夏、新疆、香港；云南、浙江、江苏、安徽、上海等10处有响应超时情况。海外18个国家地区的83个有效测试样本中，共有超时点1个；响应均值为162毫秒，最快的三地区为美国、加拿大、德国，最慢的三地区为越南、马来西亚、柬埔寨；香港有响应超时情况。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_idc_linode_usa-dallas_20180622_mainland.png)

大陆各省份到Linode美国-达拉斯机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
天津 | 2个 | 0 | 200ms | 0 | 均值 | 860个 | 23个 | 244ms | 1.2%  
上海 | 7个 | 1个 | 213ms | 0.2% | 浙江 | 51个 | 3个 | 245ms | 0.9%  
北京 | 9个 | 0 | 220ms | 0.3% | 内蒙古 | 27个 | 0 | 247ms | 0.8%  
河北 | 29个 | 0 | 225ms | 2.0% | 江西 | 23个 | 0 | 249ms | 1.2%  
广东 | 69个 | 0 | 226ms | 0.9% | 重庆 | 12个 | 0 | 251ms | 0.3%  
广西 | 41个 | 0 | 227ms | 2.2% | 黑龙江 | 32个 | 1个 | 254ms | 0.6%  
海南 | 12个 | 0 | 227ms | 0.5% | 吉林 | 19个 | 0 | 254ms | 0.5%  
山东 | 42个 | 0 | 229ms | 0.2% | 云南 | 18个 | 10个 | 257ms | 0.5%  
山西 | 31个 | 1个 | 229ms | 0.4% | 河南 | 43个 | 1个 | 265ms | 4.1%  
福建 | 29个 | 1个 | 232ms | 0.5% | 四川 | 42个 | 0 | 265ms | 1.5%  
湖北 | 32个 | 0 | 232ms | 0.5% | 陕西 | 24个 | 0 | 269ms | 0.5%  
江苏 | 64个 | 2个 | 234ms | 1.2% | 青海 | 5个 | 0 | 270ms | 0.2%  
贵州 | 25个 | 0 | 237ms | 3.3% | 甘肃 | 15个 | 0 | 273ms | 1.0%  
湖南 | 35个 | 0 | 238ms | 1.2% | 宁夏 | 13个 | 0 | 274ms | 1.3%  
安徽 | 30个 | 2个 | 243ms | 1.4% | 新疆 | 23个 | 0 | 308ms | 2.4%  
辽宁 | 34个 | 0 | 243ms | 1.1% | 香港 | 22个 | 1个 | - | -  
  
简评：如果你考虑在Linode的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有860个，其中超时点23个，平均响应时间为244毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在100-200毫秒间的1个，在200-300毫秒间的28个，超过300毫秒的1个；  
超时点较多的省份：上海、云南；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_idc_linode_usa-dallas_20180622_overseas.png)

海外线路到Linode美国-达拉斯机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 20个 | 0 | 42ms | 0 | 新加坡 | 5个 | 0 | 170ms | 0  
加拿大 | 2个 | 0 | 57ms | 0 | 香港 | 22个 | 1个 | 172ms | 0  
德国 | 1个 | 0 | 111ms | - | 台湾 | 2个 | 0 | 174ms | 0  
巴西 | 1个 | 0 | 112ms | 0 | 韩国 | 13个 | 0 | 195ms | 0  
意大利 | 1个 | 0 | 115ms | - | 澳大利亚 | 1个 | 0 | 203ms | 0  
法国 | 1个 | 0 | 122ms | 0 | 菲律宾 | 2个 | 0 | 205ms | 0  
英国 | 1个 | 0 | 142ms | 0 | 越南 | 2个 | 0 | 227ms | 0  
日本 | 2个 | 0 | 153ms | 0 | 马来西亚 | 4个 | 0 | 255ms | 0  
均值 | 83个 | 1个 | 162ms | 0 | 柬埔寨 | 1个 | 0 | 304ms | 0  
南非 | 2个 | 0 | 167ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Linode的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有83个，其中超时点1个，平均响应时间为162毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的11个，在200-300毫秒间的4个，超过300毫秒的1个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180622 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180622 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180622-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180622")
    * [法兰克福](/linode/idc/frankfurt/20180622-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180622")
    * [佛利蒙](/linode/idc/fremont/20180622-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180622")
    * [伦敦](/linode/idc/london/20180622-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180622")
    * [纽瓦克](/linode/idc/newark/20180622-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180622")
    * [新加坡](/linode/idc/singapore/20180622-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180622")
    * [东京](/linode/idc/tokyo/20180622-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180622")
  * 到Linode达拉斯机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/dallas/20180514-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180514")
    * [20180527](/linode/idc/dallas/20180527-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180527")
    * [20180804](/linode/idc/dallas/20180804-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180804")
    * [20180918](/linode/idc/dallas/20180918-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180918")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/dallas/20180622-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180622")



本文最初发表于[多地到Linode达拉斯[Dallas]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-linode-idc-dallas.html)
