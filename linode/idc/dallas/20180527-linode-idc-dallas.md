#  多地到Linode达拉斯[Dallas]机房的Ping测试（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Linode达拉斯\[Dallas\]机房的Ping测试（20180527）](/images/thumbnails/to_linode_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Linode](https://vps123.top/go/linode)的[美国-达拉斯机房](https://vps123.top/linode-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Linode](https://vps123.top/go/linode)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Linode全部机房](/linode/isp/china/20180527-linode-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆30个省市的975个有效测试样本中，共有超时点7个；响应均值为247毫秒，最快的三地区为上海、江苏、广东，最慢的三地区为吉林、黑龙江、新疆；江苏、北京、山东、河南、重庆等7处有响应超时情况；天津、内蒙古、黑龙江、吉林、陕西等18处丢包率较高。海外17个国家地区的66个有效测试样本中，共有超时点1个；响应均值为152毫秒，最快的三地区为美国、加拿大、意大利，最慢的三地区为马来西亚、南非、日本；日本有响应超时情况。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Linode位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/linode_20180527/plot_idc_linode_usa-dallas_20180527_mainland.png)

**大陆各省份到Linode美国-达拉斯机房的测速数据 [20180527]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
上海 | 8个 | 0 | 212ms | 2.5%  
江苏 | 62个 | 1个 | 218ms | 0.9%  
广东 | 79个 | 0 | 219ms | 5.1%  
北京 | 8个 | 1个 | 223ms | 0.5%  
浙江 | 49个 | 0 | 225ms | 0.3%  
福建 | 37个 | 0 | 232ms | 3.4%  
山东 | 52个 | 1个 | 233ms | 4.5%  
广西 | 39个 | 0 | 233ms | 6.3%  
河北 | 35个 | 0 | 235ms | 6.4%  
海南 | 14个 | 0 | 235ms | 6.5%  
辽宁 | 38个 | 0 | 235ms | 4.8%  
山西 | 37个 | 0 | 237ms | 4.1%  
湖北 | 43个 | 0 | 238ms | 4.1%  
河南 | 56个 | 1个 | 240ms | 5.7%  
云南 | 22个 | 0 | 242ms | 2.6%  
湖南 | 48个 | 0 | 242ms | 7.3%  
安徽 | 38个 | 0 | 246ms | 8.2%  
江西 | 24个 | 0 | 247ms | 4.7%  
均值 | 975个 | 7个 | 247ms | 6.2%  
重庆 | 15个 | 1个 | 254ms | 5.3%  
贵州 | 27个 | 0 | 255ms | 6.6%  
天津 | 5个 | 0 | 255ms | 15.0%  
青海 | 4个 | 0 | 265ms | 8.8%  
宁夏 | 12个 | 0 | 265ms | 8.7%  
甘肃 | 23个 | 0 | 268ms | 4.7%  
四川 | 48个 | 0 | 270ms | 8.8%  
陕西 | 32个 | 1个 | 276ms | 10.7%  
内蒙古 | 34个 | 0 | 283ms | 13.4%  
吉林 | 19个 | 0 | 287ms | 12.5%  
黑龙江 | 40个 | 1个 | 292ms | 13.3%  
新疆 | 27个 | 0 | 311ms | 10.2%  
  
**简评：** 如果你考虑在Linode的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有975个，其中超时点7个，平均响应时间为247毫秒，丢包率为6%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的29个，超过300毫秒的1个；  
超时点较多的省份：北京；  
丢包率较高的省份：天津、陕西、内蒙古、吉林、黑龙江、新疆；

## 海外测速点

![海外各国家地区到VPS提供商Linode位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/linode_20180527/plot_idc_linode_usa-dallas_20180527_overseas.png)

**海外线路到Linode美国-达拉斯机房的测速数据 [20180527]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
美国 | 18个 | 0 | 32ms | 0  
加拿大 | 1个 | 0 | 37ms | -  
意大利 | 1个 | 0 | 106ms | -  
英国 | 1个 | 0 | 109ms | 0  
法国 | 1个 | 0 | 116ms | 0  
德国 | 2个 | 0 | 119ms | 0  
荷兰 | 1个 | 0 | 124ms | 0  
巴西 | 1个 | 0 | 139ms | 0  
均值 | 66个 | 1个 | 152ms | 0  
台湾 | 1个 | 0 | 181ms | -  
韩国 | 10个 | 0 | 184ms | 0  
澳大利亚 | 1个 | 0 | 197ms | 0  
俄罗斯 | 1个 | 0 | 200ms | 0  
香港 | 20个 | 0 | 203ms | 0  
新加坡 | 4个 | 0 | 206ms | 0  
马来西亚 | 1个 | 0 | 215ms | 0  
南非 | 1个 | 0 | 265ms | 0  
日本 | 1个 | 1个 | - | -  
  
**简评：** 如果你考虑在Linode的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有66个，其中超时点1个，平均响应时间为152毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在100-200毫秒间的10个，在200-300毫秒间的4个；

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180527 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180527 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期到Linode _其他机房_ 的报告： 
    * [亚特兰大](/linode/idc/atlanta/20180527-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180527")
    * [法兰克福](/linode/idc/frankfurt/20180527-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180527")
    * [佛利蒙](/linode/idc/fremont/20180527-linode-idc-fremont.md "多地到Linode佛利蒙机房的Ping测试 20180527")
    * [伦敦](/linode/idc/london/20180527-linode-idc-london.md "多地到Linode伦敦机房的Ping测试 20180527")
    * [纽瓦克](/linode/idc/newark/20180527-linode-idc-newark.md "多地到Linode纽瓦克机房的Ping测试 20180527")
    * [新加坡](/linode/idc/singapore/20180527-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180527")
    * [东京](/linode/idc/tokyo/20180527-linode-idc-tokyo.md "多地到Linode东京机房的Ping测试 20180527")
  * 到Linode达拉斯机房的 _其他近期报告_ ： 
    * [20180514](/linode/idc/dallas/20180514-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180514")
    * [20180622](/linode/idc/dallas/20180622-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180622")
    * [20180804](/linode/idc/dallas/20180804-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180804")
    * [20180918](/linode/idc/dallas/20180918-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180918")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Vultr](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")



本文最初发表于[多地到Linode达拉斯[Dallas]机房的Ping测试（20180527）](https://vps123.top/pingtest/20180527-linode-idc-dallas.html)
