#  多地到Vultr新加坡[Singapore]机房的Ping测试（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr新加坡\[Singapore\]机房的Ping测试（20180918）](/images/thumbnails/to_vultr_Tokyo.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[新加坡-新加坡机房](https://vps123.top/vultr-facilities.html#singapore)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的新加坡-新加坡机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180918-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918多地到Vultr新加坡-新加坡机房的PING测试结果，连通概况如下：大陆31个省市的1459个有效测试样本中，共有超时点14个；响应均值为201毫秒，最快的三地区为上海、湖南、广西，最慢的三地区为新疆、青海、西藏；江苏、广东、浙江、山西、湖北有响应超时情况；天津、河南、山东丢包率较高。海外17个国家地区的78个有效测试样本中，无超时点；响应均值为178毫秒，最快的三地区为印度尼西亚、新加坡、越南，最慢的三地区为澳大利亚、俄罗斯、赞比亚；菲律宾、赞比亚丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_singapore-singapore_20180918_mainland.png)

大陆各省份到Vultr新加坡-新加坡机房的测速数据 [20180918] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 9个 | 0 | 163ms | 2.3% | 江苏 | 94个 | 6个 | 198ms | 2.6%  
湖南 | 72个 | 0 | 166ms | 1.4% | 均值 | 1459个 | 14个 | 201ms | 2.8%  
广西 | 62个 | 0 | 167ms | 1.5% | 云南 | 35个 | 0 | 206ms | 1.4%  
江西 | 42个 | 0 | 173ms | 1.8% | 北京 | 9个 | 0 | 210ms | 5.0%  
山东 | 95个 | 0 | 175ms | 6.2% | 河北 | 62个 | 0 | 224ms | 1.7%  
河南 | 89个 | 0 | 180ms | 6.7% | 重庆 | 9个 | 0 | 225ms | 3.6%  
安徽 | 68个 | 0 | 182ms | 3.2% | 内蒙古 | 56个 | 0 | 226ms | 1.9%  
福建 | 42个 | 0 | 185ms | 2.8% | 山西 | 59个 | 1个 | 227ms | 1.5%  
广东 | 126个 | 4个 | 185ms | 2.0% | 四川 | 73个 | 0 | 234ms | 2.8%  
贵州 | 45个 | 0 | 186ms | 1.5% | 湖北 | 57个 | 1个 | 241ms | 2.6%  
黑龙江 | 58个 | 0 | 186ms | 3.2% | 甘肃 | 34个 | 0 | 242ms | 4.5%  
浙江 | 62个 | 2个 | 188ms | 3.2% | 辽宁 | 66个 | 0 | 250ms | 1.5%  
海南 | 14个 | 0 | 189ms | 1.1% | 宁夏 | 8个 | 0 | 261ms | 2.9%  
天津 | 7个 | 0 | 191ms | 7.0% | 新疆 | 35个 | 0 | 262ms | 1.8%  
陕西 | 44个 | 0 | 193ms | 1.3% | 青海 | 6个 | 0 | 274ms | 4.9%  
吉林 | 20个 | 0 | 194ms | 0.4% | 西藏 | 1个 | 0 | 343ms | 2.0%  
  
简评：如果你考虑在Vultr的新加坡[Singapore]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有1459个，其中超时点14个，平均响应时间为201毫秒，丢包率为2%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在100-200毫秒间的17个，在200-300毫秒间的13个，超过300毫秒的1个；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于新加坡\[Singapore\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_idc_vultr_singapore-singapore_20180918_overseas.png)

海外线路到Vultr新加坡-新加坡机房的测速数据 [20180918] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
印度尼西亚 | 1个 | 0 | 25ms | 0 | 均值 | 78个 | 0 | 178ms | 2.3%  
新加坡 | 5个 | 0 | 37ms | 0 | 荷兰 | 1个 | 0 | 192ms | 0  
越南 | 2个 | 0 | 53ms | 0 | 加拿大 | 3个 | 0 | 257ms | 0  
日本 | 3个 | 0 | 75ms | 0.3% | 菲律宾 | 2个 | 0 | 258ms | 25.0%  
马来西亚 | 6个 | 0 | 87ms | 0.2% | 德国 | 3个 | 0 | 272ms | 1.0%  
香港 | 19个 | 0 | 113ms | 0 | 意大利 | 1个 | 0 | 278ms | -  
台湾 | 2个 | 0 | 114ms | 0 | 澳大利亚 | 2个 | 0 | 290ms | 0  
韩国 | 9个 | 0 | 148ms | 0 | 俄罗斯 | 1个 | 0 | 297ms | -  
美国 | 16个 | 0 | 161ms | 0.2% | 赞比亚 | 2个 | 0 | 365ms | 8.2%  
  
简评：如果你考虑在Vultr的新加坡[Singapore]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于新加坡[Singapore]的机房的连通状况。到此机房的ping监测点共有78个，其中超时点0个，平均响应时间为178毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的3个，在100-200毫秒间的5个，在200-300毫秒间的6个，超过300毫秒的1个；  
丢包率较高的国家/地区：菲律宾；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180918 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180918 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180918-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180918")
    * [亚特兰大](/vultr/idc/atlanta/20180918-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180918")
    * [芝加哥](/vultr/idc/chicago/20180918-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180918")
    * [达拉斯](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
    * [法兰克福](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")
    * [伦敦](/vultr/idc/london/20180918-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180918")
    * [洛杉矶](/vultr/idc/losangeles/20180918-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180918")
    * [迈阿密](/vultr/idc/miami/20180918-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180918")
    * [新泽西](/vultr/idc/newjersey/20180918-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180918")
    * [巴黎](/vultr/idc/paris/20180918-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180918")
    * [西雅图](/vultr/idc/seattle/20180918-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180918")
    * [硅谷](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")
    * [悉尼](/vultr/idc/sydney/20180918-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180918")
    * [东京](/vultr/idc/tokyo/20180918-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180918")
  * 到Vultr新加坡机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/singapore/20180514-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180514")
    * [20180527](/vultr/idc/singapore/20180527-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180527")
    * [20180622](/vultr/idc/singapore/20180622-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180622")
    * [20180804](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
  * 本期报告：在新加坡部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/singapore/20180918-do-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180918")
    * [Linode](/linode/idc/singapore/20180918-linode-idc-singapore.md "多地到Linode新加坡机房的Ping测试 20180918")



本文最初发表于[多地到Vultr新加坡[Singapore]机房的Ping测试（20180918）](https://vps123.top/pingtest/20180918-vultr-idc-singapore.html)
