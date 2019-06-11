#  多地到Vultr亚特兰大[Atlanta]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr亚特兰大\[Atlanta\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Atlanta.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-亚特兰大机房](https://vps123.top/vultr-facilities.html#atlanta)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-亚特兰大机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr美国-亚特兰大机房的PING测试结果，连通概况如下：大陆31个省市的945个有效测试样本中，共有超时点14个；响应均值为330毫秒，最快的三地区为北京、天津、吉林，最慢的三地区为新疆、云南、西藏；浙江、江苏、北京、福建、山东等10处有响应超时情况；西藏、湖北、云南、河北、海南等30处丢包率较高。海外17个国家地区的75个有效测试样本中，共有超时点1个；响应均值为184毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为马来西亚、南非、印度尼西亚；香港有响应超时情况；印度尼西亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于亚特兰大\[Atlanta\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-atlanta_20180514_mainland.png)

大陆各省份到Vultr美国-亚特兰大机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 9个 | 1个 | 255ms | 3.7% | 江西 | 20个 | 0 | 336ms | 18.1%  
天津 | 5个 | 0 | 267ms | 13.0% | 山西 | 37个 | 0 | 336ms | 17.1%  
吉林 | 17个 | 0 | 269ms | 5.6% | 湖北 | 46个 | 0 | 342ms | 22.2%  
江苏 | 61个 | 2个 | 281ms | 17.8% | 贵州 | 27个 | 0 | 344ms | 18.3%  
上海 | 8个 | 0 | 294ms | 13.4% | 河南 | 55个 | 0 | 348ms | 19.8%  
浙江 | 50个 | 4个 | 301ms | 18.4% | 广西 | 34个 | 0 | 350ms | 13.9%  
福建 | 37个 | 1个 | 305ms | 8.5% | 河北 | 29个 | 0 | 351ms | 21.3%  
辽宁 | 40个 | 0 | 307ms | 14.6% | 湖南 | 41个 | 1个 | 353ms | 14.7%  
陕西 | 33个 | 0 | 308ms | 10.5% | 海南 | 10个 | 0 | 354ms | 20.5%  
山东 | 53个 | 1个 | 313ms | 13.3% | 重庆 | 15个 | 1个 | 356ms | 9.8%  
黑龙江 | 36个 | 0 | 314ms | 13.7% | 四川 | 47个 | 0 | 361ms | 13.3%  
宁夏 | 10个 | 0 | 316ms | 14.1% | 青海 | 4个 | 0 | 362ms | 15.0%  
内蒙古 | 34个 | 0 | 317ms | 14.2% | 甘肃 | 22个 | 0 | 367ms | 15.9%  
安徽 | 36个 | 1个 | 320ms | 16.4% | 新疆 | 29个 | 1个 | 368ms | 15.9%  
均值 | 945个 | 14个 | 330ms | 15.6% | 云南 | 23个 | 1个 | 404ms | 21.7%  
广东 | 76个 | 0 | 334ms | 14.1% | 西藏 | 1个 | 0 | 485ms | 37.0%  
  
简评：如果你考虑在Vultr的亚特兰大[Atlanta]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于亚特兰大[Atlanta]的机房的连通状况。到此机房的ping监测点共有945个，其中超时点14个，平均响应时间为330毫秒，丢包率为15%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的5个，超过300毫秒的26个；  
超时点较多的省份：北京；  
丢包率较高的省份：天津、江苏、上海、浙江、辽宁、陕西、山东、黑龙江、宁夏、内蒙古、安徽、广东、江西、山西、湖北、贵州、河南、广西、河北、湖南、海南、四川、青海、甘肃、新疆、云南、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于亚特兰大\[Atlanta\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-atlanta_20180514_overseas.png)

海外线路到Vultr美国-亚特兰大机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 3个 | 0 | 37ms | 0 | 日本 | 2个 | 0 | 200ms | 0.5%  
美国 | 17个 | 0 | 48ms | 0 | 台湾 | 1个 | 0 | 202ms | -  
法国 | 2个 | 0 | 91ms | 0 | 澳大利亚 | 2个 | 0 | 217ms | 0  
英国 | 2个 | 0 | 101ms | 0 | 香港 | 18个 | 1个 | 223ms | 0  
巴西 | 1个 | 0 | 120ms | 0 | 新加坡 | 6个 | 0 | 240ms | 0  
德国 | 1个 | 0 | 120ms | 0 | 菲律宾 | 1个 | 0 | 263ms | 0  
均值 | 75个 | 1个 | 184ms | 0.5% | 马来西亚 | 3个 | 0 | 275ms | 0  
俄罗斯 | 1个 | 0 | 193ms | 0 | 南非 | 1个 | 0 | 296ms | 0  
韩国 | 13个 | 0 | 195ms | 0 | 印度尼西亚 | 1个 | 0 | 318ms | 7.0%  
  
简评：如果你考虑在Vultr的亚特兰大[Atlanta]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于亚特兰大[Atlanta]的机房的连通状况。到此机房的ping监测点共有75个，其中超时点1个，平均响应时间为184毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的1个，在100-200毫秒间的6个，在200-300毫秒间的7个，超过300毫秒的1个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180514 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180514 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180514-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180514")
    * [芝加哥](/vultr/idc/chicago/20180514-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180514")
    * [达拉斯](/vultr/idc/dallas/20180514-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180514")
    * [法兰克福](/vultr/idc/frankfurt/20180514-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180514")
    * [伦敦](/vultr/idc/london/20180514-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180514")
    * [洛杉矶](/vultr/idc/losangeles/20180514-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180514")
    * [迈阿密](/vultr/idc/miami/20180514-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180514")
    * [新泽西](/vultr/idc/newjersey/20180514-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180514")
    * [巴黎](/vultr/idc/paris/20180514-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180514")
    * [西雅图](/vultr/idc/seattle/20180514-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180514")
    * [硅谷](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [新加坡](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [悉尼](/vultr/idc/sydney/20180514-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180514")
    * [东京](/vultr/idc/tokyo/20180514-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180514")
  * 到Vultr亚特兰大机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/atlanta/20180527-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180527")
    * [20180622](/vultr/idc/atlanta/20180622-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180622")
    * [20180804](/vultr/idc/atlanta/20180804-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180804")
    * [20180918](/vultr/idc/atlanta/20180918-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180918")
  * 本期报告：在亚特兰大部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/atlanta/20180514-linode-idc-atlanta.md "多地到Linode亚特兰大机房的Ping测试 20180514")



本文最初发表于[多地到Vultr亚特兰大[Atlanta]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-atlanta.html)
