#  多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean旧金山\[SanFrancisco\]机房的Ping测试（20180918）](/images/thumbnails/to_do_SanFrancisco.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[美国-旧金山机房](https://vps123.top/digitalocean-facilities.html#sanfrancisco)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的美国-旧金山机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180918-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Digital Ocean美国-旧金山机房的PING测试结果，连通概况如下：大陆31个省市的2916个有效测试样本中，共有超时点46个；响应均值为252毫秒，最快的三地区为上海、海南、宁夏，最慢的三地区为吉林、新疆、西藏；江苏、浙江、广东、山西、湖北等12处有响应超时情况；重庆、吉林、河南、辽宁、内蒙古等27处丢包率较高。海外17个国家地区的151个有效测试样本中，共有超时点2个；响应均值为180毫秒，最快的三地区为美国、加拿大、台湾，最慢的三地区为越南、菲律宾、赞比亚；香港有响应超时情况；菲律宾、赞比亚丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_usa-sanfrancisco_20180918_mainland.png)

大陆各省份到Digital Ocean美国-旧金山机房的测速数据 [20180918] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 14个 | 0 | 192ms | 2.4% | 河北 | 123个 | 0 | 250ms | 10.0%  
海南 | 26个 | 0 | 221ms | 8.4% | 江西 | 82个 | 0 | 251ms | 6.4%  
宁夏 | 13个 | 0 | 223ms | 2.4% | 均值 | 2916个 | 46个 | 252ms | 9.6%  
广西 | 125个 | 0 | 227ms | 5.9% | 云南 | 61个 | 0 | 260ms | 7.0%  
安徽 | 142个 | 1个 | 227ms | 4.8% | 辽宁 | 123个 | 1个 | 261ms | 14.9%  
山东 | 191个 | 1个 | 231ms | 12.1% | 陕西 | 87个 | 2个 | 262ms | 6.8%  
江苏 | 187个 | 12个 | 235ms | 8.3% | 山西 | 117个 | 5个 | 263ms | 10.7%  
广东 | 241个 | 6个 | 235ms | 8.2% | 河南 | 184个 | 0 | 269ms | 15.0%  
福建 | 89个 | 1个 | 239ms | 6.8% | 四川 | 148个 | 3个 | 273ms | 9.3%  
贵州 | 88个 | 0 | 240ms | 9.6% | 内蒙古 | 118个 | 0 | 278ms | 12.7%  
湖北 | 112个 | 4个 | 240ms | 8.1% | 青海 | 10个 | 0 | 279ms | 11.8%  
浙江 | 135个 | 9个 | 242ms | 7.7% | 黑龙江 | 123个 | 0 | 280ms | 12.6%  
北京 | 17个 | 0 | 243ms | 10.1% | 甘肃 | 69个 | 0 | 280ms | 7.4%  
湖南 | 139个 | 1个 | 245ms | 8.0% | 吉林 | 43个 | 0 | 282ms | 17.0%  
天津 | 12个 | 0 | 249ms | 4.1% | 新疆 | 73个 | 0 | 300ms | 10.9%  
重庆 | 16个 | 0 | 249ms | 17.0% | 西藏 | 8个 | 0 | 401ms | 8.0%  
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有2916个，其中超时点46个，平均响应时间为252毫秒，丢包率为9%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的1个，在200-300毫秒间的29个，超过300毫秒的1个；  
丢包率较高的省份：山东、北京、重庆、河北、辽宁、山西、河南、内蒙古、青海、黑龙江、吉林、新疆；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于旧金山\[SanFrancisco\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/do_20180918/plot_idc_do_usa-sanfrancisco_20180918_overseas.png)

海外线路到Digital Ocean美国-旧金山机房的测速数据 [20180918] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 30个 | 0 | 36ms | 0 | 均值 | 151个 | 2个 | 180ms | 2.7%  
加拿大 | 4个 | 0 | 64ms | - | 澳大利亚 | 4个 | 0 | 182ms | 1.1%  
台湾 | 4个 | 0 | 93ms | 0 | 俄罗斯 | 2个 | 0 | 190ms | -  
韩国 | 24个 | 0 | 127ms | 0 | 印度尼西亚 | 2个 | 0 | 202ms | 0  
日本 | 6个 | 0 | 138ms | 1.7% | 荷兰 | 2个 | 0 | 236ms | 0  
意大利 | 2个 | 0 | 142ms | - | 马来西亚 | 6个 | 0 | 241ms | 0.2%  
新加坡 | 10个 | 0 | 158ms | 0 | 越南 | 4个 | 0 | 266ms | 0  
香港 | 39个 | 2个 | 160ms | 0 | 菲律宾 | 4个 | 0 | 317ms | 28.3%  
德国 | 6个 | 0 | 165ms | 0 | 赞比亚 | 2个 | 0 | 350ms | 7.0%  
  
简评：如果你考虑在Digital Ocean的旧金山[SanFrancisco]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于旧金山[SanFrancisco]的机房的连通状况。到此机房的ping监测点共有151个，其中超时点2个，平均响应时间为180毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的2个，在100-200毫秒间的8个，在200-300毫秒间的4个，超过300毫秒的2个；  
丢包率较高的国家/地区：菲律宾；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180918 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180918 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180918-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180918")
    * [班加罗尔](/digitalocean/idc/bangalore/20180918-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180918")
    * [法兰克福](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
    * [伦敦](/digitalocean/idc/london/20180918-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180918")
    * [纽约](/digitalocean/idc/newyork/20180918-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180918")
    * [新加坡](/digitalocean/idc/singapore/20180918-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
    * [多伦多](/digitalocean/idc/toronto/20180918-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180918")
  * 到Digital Ocean旧金山机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/sanfrancisco/20180527-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/sanfrancisco/20180622-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")



本文最初发表于[多地到Digital Ocean旧金山[SanFrancisco]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-digitalocean-idc-sanfrancisco.html)
