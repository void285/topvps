#  多地到Vultr法兰克福[Frankfurt]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr法兰克福\[Frankfurt\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[德国-法兰克福机房](https://vps123.top/vultr-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr德国-法兰克福机房的PING测试结果，连通概况如下：大陆31个省市的868个有效测试样本中，共有超时点9个；响应均值为293毫秒，最快的三地区为甘肃、天津、安徽，最慢的三地区为黑龙江、吉林、西藏；浙江、广东、重庆、福建、江苏等6处有响应超时情况；江苏、天津、辽宁、浙江、山西等10处丢包率较高。海外17个国家地区的75个有效测试样本中，无超时点；响应均值为199毫秒，最快的三地区为法国、德国、英国，最慢的三地区为韩国、澳大利亚、柬埔寨；柬埔寨丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_germany-frankfurt_20180514_mainland.png)

**大陆各省份到Vultr德国-法兰克福机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
甘肃 | 14个 | 0 | 239ms | 0.6%  
天津 | 4个 | 0 | 240ms | 9.0%  
安徽 | 32个 | 0 | 256ms | 1.8%  
青海 | 3个 | 0 | 261ms | 0  
宁夏 | 12个 | 0 | 261ms | 0.3%  
内蒙古 | 30个 | 0 | 272ms | 3.1%  
重庆 | 15个 | 1个 | 275ms | 0.4%  
海南 | 11个 | 0 | 275ms | 3.8%  
北京 | 6个 | 0 | 276ms | 1.7%  
广东 | 75个 | 2个 | 279ms | 2.5%  
湖北 | 42个 | 0 | 280ms | 3.4%  
上海 | 7个 | 0 | 282ms | 1.4%  
江西 | 17个 | 0 | 283ms | 7.0%  
广西 | 31个 | 0 | 283ms | 4.1%  
湖南 | 42个 | 0 | 284ms | 3.3%  
云南 | 19个 | 0 | 285ms | 1.5%  
河南 | 50个 | 0 | 286ms | 3.4%  
河北 | 31个 | 0 | 290ms | 4.4%  
均值 | 868个 | 9个 | 293ms | 4.7%  
辽宁 | 31个 | 0 | 296ms | 8.8%  
福建 | 33个 | 1个 | 298ms | 5.3%  
四川 | 44个 | 0 | 299ms | 4.1%  
浙江 | 51个 | 3个 | 304ms | 8.8%  
江苏 | 60个 | 1个 | 306ms | 11.6%  
山西 | 31个 | 0 | 306ms | 7.4%  
贵州 | 26个 | 0 | 309ms | 5.2%  
陕西 | 26个 | 0 | 310ms | 4.2%  
新疆 | 22个 | 0 | 320ms | 4.8%  
山东 | 50个 | 1个 | 323ms | 5.5%  
黑龙江 | 35个 | 0 | 329ms | 5.9%  
吉林 | 17个 | 0 | 329ms | 2.1%  
西藏 | 1个 | 0 | 371ms | 0  
  
**简评：** 如果你考虑在Vultr的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有868个，其中超时点9个，平均响应时间为293毫秒，丢包率为4%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的21个，超过300毫秒的10个；  
丢包率较高的省份：江苏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_germany-frankfurt_20180514_overseas.png)

**海外线路到Vultr德国-法兰克福机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
法国 | 2个 | 0 | 11ms | 0  
德国 | 1个 | 0 | 27ms | 0  
英国 | 2个 | 0 | 33ms | 0  
俄罗斯 | 1个 | 0 | 91ms | 0  
加拿大 | 3个 | 0 | 111ms | 0  
美国 | 18个 | 0 | 153ms | 0  
新加坡 | 6个 | 0 | 177ms | 0  
均值 | 75个 | 0 | 199ms | 2.3%  
马来西亚 | 3个 | 0 | 218ms | 1.0%  
南非 | 1个 | 0 | 222ms | 0  
香港 | 18个 | 0 | 226ms | 0  
菲律宾 | 1个 | 0 | 247ms | 0  
日本 | 2个 | 0 | 266ms | 2.0%  
印度尼西亚 | 1个 | 0 | 275ms | 2.0%  
台湾 | 1个 | 0 | 282ms | -  
韩国 | 13个 | 0 | 286ms | 0  
澳大利亚 | 1个 | 0 | 307ms | 0  
柬埔寨 | 1个 | 0 | 457ms | 32.0%  
  
**简评：** 如果你考虑在Vultr的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有75个，其中超时点0个，平均响应时间为199毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的3个，在50-100毫秒间的1个，在100-200毫秒间的3个，在200-300毫秒间的8个，超过300毫秒的2个；  
丢包率较高的国家/地区：柬埔寨；

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
    * [芝加哥](/vultr/idc/chicago/20180514-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180514")
    * [达拉斯](/vultr/idc/dallas/20180514-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180514")
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
  * 到Vultr法兰克福机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/frankfurt/20180527-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180527")
    * [20180622](/vultr/idc/frankfurt/20180622-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180622")
    * [20180804](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")
    * [20180918](/vultr/idc/frankfurt/20180918-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180514-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [Linode](/linode/idc/frankfurt/20180514-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180514")



本文最初发表于[多地到Vultr法兰克福[Frankfurt]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-frankfurt.html)
