#  多地到Vultr法兰克福[Frankfurt]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr法兰克福\[Frankfurt\]机房的Ping测试（20180622）](/images/thumbnails/to_vultr_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[德国-法兰克福机房](https://vps123.top/vultr-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180622-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆32个省市的925个有效测试样本中，共有超时点79个；响应均值为269毫秒，最快的三地区为天津、内蒙古、甘肃，最慢的三地区为山东、西藏、香港；江苏、广东、浙江、福建、辽宁等21处有响应超时情况；西藏、河北、辽宁丢包率较高。海外17个国家地区的76个有效测试样本中，共有超时点3个；响应均值为174毫秒，最快的三地区为法国、巴西、德国，最慢的三地区为日本、台湾、澳大利亚；香港、美国有响应超时情况；澳大利亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_germany-frankfurt_20180622_mainland.png)

**大陆各省份到Vultr德国-法兰克福机房的测速数据 [20180622]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 3个 | 0 | 226ms | 0  
内蒙古 | 32个 | 0 | 242ms | 1.7%  
甘肃 | 21个 | 0 | 244ms | 0  
宁夏 | 13个 | 0 | 245ms | 0  
青海 | 3个 | 0 | 248ms | 0  
北京 | 10个 | 1个 | 248ms | 0.4%  
广西 | 44个 | 2个 | 249ms | 1.2%  
广东 | 80个 | 13个 | 256ms | 0.1%  
安徽 | 36个 | 3个 | 256ms | 2.1%  
湖北 | 36个 | 3个 | 258ms | 0.1%  
陕西 | 32个 | 2个 | 261ms | 0.1%  
海南 | 12个 | 0 | 261ms | 0  
云南 | 14个 | 0 | 262ms | 0  
上海 | 7个 | 1个 | 264ms | 0  
重庆 | 12个 | 2个 | 265ms | 0  
江西 | 23个 | 1个 | 267ms | 0.3%  
均值 | 925个 | 79个 | 269ms | 1.8%  
河南 | 51个 | 2个 | 270ms | 0.2%  
山西 | 37个 | 3个 | 270ms | 0  
江苏 | 70个 | 14个 | 272ms | 0.7%  
浙江 | 52个 | 10个 | 273ms | 2.5%  
湖南 | 39个 | 3个 | 273ms | 0.9%  
福建 | 32个 | 5个 | 276ms | 1.1%  
四川 | 40个 | 3个 | 277ms | 0.6%  
贵州 | 25个 | 1个 | 278ms | 0.3%  
河北 | 28个 | 0 | 281ms | 18.7%  
黑龙江 | 32个 | 0 | 283ms | 0.1%  
辽宁 | 29个 | 4个 | 286ms | 14.5%  
新疆 | 27个 | 1个 | 288ms | 2.3%  
吉林 | 19个 | 0 | 295ms | 0.2%  
山东 | 45个 | 3个 | 300ms | 0.3%  
西藏 | 1个 | 0 | 328ms | 58.0%  
香港 | 20个 | 2个 | - | -  
  
**简评：** 如果你考虑在Vultr的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有925个，其中超时点79个，平均响应时间为269毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的30个，超过300毫秒的1个；  
超时点较多的省份：广东、上海、重庆、江苏、浙江、福建、辽宁；  
丢包率较高的省份：河北、辽宁、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_germany-frankfurt_20180622_overseas.png)

**海外线路到Vultr德国-法兰克福机房的测速数据 [20180622]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
法国 | 1个 | 0 | 0 | 0  
巴西 | 1个 | 0 | 15ms | 0  
德国 | 1个 | 0 | 17ms | -  
意大利 | 1个 | 0 | 19ms | -  
加拿大 | 2个 | 0 | 114ms | 0  
美国 | 20个 | 1个 | 142ms | 0  
新加坡 | 5个 | 0 | 169ms | 0  
均值 | 76个 | 3个 | 174ms | 0.6%  
南非 | 2个 | 0 | 179ms | 0  
英国 | 2个 | 0 | 182ms | 0  
香港 | 20个 | 2个 | 223ms | 0  
菲律宾 | 1个 | 0 | 247ms | 0  
印度尼西亚 | 1个 | 0 | 248ms | 0  
越南 | 2个 | 0 | 266ms | 0.5%  
韩国 | 12个 | 0 | 266ms | 0  
日本 | 2个 | 0 | 277ms | 2.0%  
台湾 | 2个 | 0 | 300ms | 0  
澳大利亚 | 1个 | 0 | 308ms | 6.0%  
  
**简评：** 如果你考虑在Vultr的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有76个，其中超时点3个，平均响应时间为174毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在100-200毫秒间的5个，在200-300毫秒间的7个，超过300毫秒的1个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180622 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180622 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180622-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180622")
    * [亚特兰大](/vultr/idc/atlanta/20180622-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180622")
    * [芝加哥](/vultr/idc/chicago/20180622-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180622")
    * [达拉斯](/vultr/idc/dallas/20180622-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180622")
    * [伦敦](/vultr/idc/london/20180622-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180622")
    * [洛杉矶](/vultr/idc/losangeles/20180622-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180622")
    * [迈阿密](/vultr/idc/miami/20180622-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180622")
    * [新泽西](/vultr/idc/newjersey/20180622-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180622")
    * [巴黎](/vultr/idc/paris/20180622-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180622")
    * [西雅图](/vultr/idc/seattle/20180622-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180622")
    * [硅谷](/vultr/idc/siliconvalley/20180622-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180622")
    * [新加坡](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [悉尼](/vultr/idc/sydney/20180622-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180622")
    * [东京](/vultr/idc/tokyo/20180622-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180622")
  * 到Vultr法兰克福机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/frankfurt/20180514-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180514")
    * [20180527](/vultr/idc/frankfurt/20180527-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180527")
    * [20180804](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")
    * [20180918](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180622-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [Linode](/linode/idc/frankfurt/20180622-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180622")



本文最初发表于[多地到Vultr法兰克福[Frankfurt]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-vultr-idc-frankfurt.html)
