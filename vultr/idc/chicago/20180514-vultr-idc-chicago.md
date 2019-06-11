#  多地到Vultr芝加哥[Chicago]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr芝加哥\[Chicago\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Chicago.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-芝加哥机房](https://vps123.top/vultr-facilities.html#chicago)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-芝加哥机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr美国-芝加哥机房的PING测试结果，连通概况如下：大陆31个省市的958个有效测试样本中，共有超时点16个；响应均值为290毫秒，最快的三地区为北京、上海、广东，最慢的三地区为新疆、河北、西藏；浙江、广东、江苏、山东、北京等9处有响应超时情况；西藏、湖北、江苏、河北、浙江等24处丢包率较高。海外17个国家地区的78个有效测试样本中，无超时点；响应均值为178毫秒，最快的三地区为加拿大、美国、法国，最慢的三地区为印度尼西亚、马来西亚、南非；印度尼西亚、马来西亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于芝加哥\[Chicago\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-chicago_20180514_mainland.png)

大陆各省份到Vultr美国-芝加哥机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 8个 | 1个 | 252ms | 2.5% | 湖北 | 48个 | 0 | 289ms | 19.0%  
上海 | 9个 | 0 | 260ms | 8.2% | 山西 | 34个 | 0 | 289ms | 14.3%  
广东 | 79个 | 2个 | 272ms | 2.1% | 海南 | 12个 | 0 | 289ms | 8.0%  
陕西 | 33个 | 0 | 273ms | 3.2% | 均值 | 958个 | 16个 | 290ms | 9.3%  
广西 | 38个 | 1个 | 278ms | 1.7% | 重庆 | 16个 | 0 | 293ms | 2.9%  
江苏 | 58个 | 2个 | 279ms | 17.9% | 云南 | 25个 | 0 | 296ms | 5.4%  
福建 | 33个 | 1个 | 281ms | 5.2% | 甘肃 | 20个 | 0 | 296ms | 9.9%  
黑龙江 | 39个 | 1个 | 282ms | 12.0% | 湖南 | 42个 | 0 | 296ms | 8.8%  
吉林 | 16个 | 0 | 282ms | 5.1% | 辽宁 | 41个 | 0 | 298ms | 8.4%  
浙江 | 53个 | 5个 | 284ms | 16.5% | 青海 | 4个 | 0 | 300ms | 1.8%  
安徽 | 39个 | 1个 | 285ms | 8.6% | 贵州 | 28个 | 0 | 301ms | 6.9%  
天津 | 5个 | 0 | 286ms | 6.6% | 河南 | 55个 | 0 | 302ms | 11.0%  
内蒙古 | 33个 | 0 | 286ms | 8.4% | 四川 | 47个 | 0 | 303ms | 3.2%  
江西 | 23个 | 0 | 287ms | 15.2% | 新疆 | 28个 | 0 | 323ms | 7.5%  
宁夏 | 11个 | 0 | 287ms | 10.4% | 河北 | 32个 | 0 | 329ms | 17.7%  
山东 | 48个 | 2个 | 288ms | 9.1% | 西藏 | 1个 | 0 | 353ms | 32.0%  
  
简评：如果你考虑在Vultr的芝加哥[Chicago]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于芝加哥[Chicago]的机房的连通状况。到此机房的ping监测点共有958个，其中超时点16个，平均响应时间为290毫秒，丢包率为9%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的25个，超过300毫秒的6个；  
超时点较多的省份：北京；  
丢包率较高的省份：江苏、黑龙江、浙江、江西、宁夏、湖北、山西、河南、河北、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于芝加哥\[Chicago\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-chicago_20180514_overseas.png)

海外线路到Vultr美国-芝加哥机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
加拿大 | 3个 | 0 | 33ms | 3.0% | 俄罗斯 | 1个 | 0 | 201ms | 0  
美国 | 19个 | 0 | 51ms | 0.4% | 香港 | 19个 | 0 | 206ms | 0  
法国 | 2个 | 0 | 96ms | 0 | 澳大利亚 | 2个 | 0 | 212ms | 0.5%  
英国 | 2个 | 0 | 107ms | 0 | 新加坡 | 6个 | 0 | 225ms | 0  
德国 | 1个 | 0 | 127ms | 0 | 台湾 | 1个 | 0 | 237ms | -  
巴西 | 1个 | 0 | 136ms | 0 | 菲律宾 | 1个 | 0 | 240ms | 0  
日本 | 2个 | 0 | 156ms | 0.5% | 印度尼西亚 | 1个 | 0 | 259ms | 8.0%  
均值 | 78个 | 0 | 178ms | 1.1% | 马来西亚 | 3个 | 0 | 260ms | 6.0%  
韩国 | 13个 | 0 | 184ms | 0 | 南非 | 1个 | 0 | 300ms | 0  
  
简评：如果你考虑在Vultr的芝加哥[Chicago]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于芝加哥[Chicago]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点0个，平均响应时间为178毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的2个，在100-200毫秒间的5个，在200-300毫秒间的9个；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180514 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180514 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180514-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180514")
    * [亚特兰大](/vultr/idc/atlanta/20180514-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180514")
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
  * 到Vultr芝加哥机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/chicago/20180527-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180527")
    * [20180622](/vultr/idc/chicago/20180622-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180622")
    * [20180804](/vultr/idc/chicago/20180804-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180804")
    * [20180918](/vultr/idc/chicago/20180918-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180918")



本文最初发表于[多地到Vultr芝加哥[Chicago]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-chicago.html)
