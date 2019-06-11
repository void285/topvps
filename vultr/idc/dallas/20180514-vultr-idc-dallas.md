#  多地到Vultr达拉斯[Dallas]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr达拉斯\[Dallas\]机房的Ping测试（20180514）](/images/thumbnails/to_vultr_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-达拉斯机房](https://vps123.top/vultr-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180514-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Vultr美国-达拉斯机房的PING测试结果，连通概况如下：大陆31个省市的938个有效测试样本中，共有超时点14个；响应均值为289毫秒，最快的三地区为天津、北京、江苏，最慢的三地区为新疆、云南、西藏；广东、浙江、福建、贵州、北京等9处有响应超时情况；西藏、云南、贵州、山东、广西等29处丢包率较高。海外18个国家地区的77个有效测试样本中，无超时点；响应均值为191毫秒，最快的三地区为美国、加拿大、法国，最慢的三地区为印度尼西亚、南非、柬埔寨；柬埔寨丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-dallas_20180514_mainland.png)

**大陆各省份到Vultr美国-达拉斯机房的测速数据 [20180514]**

省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
天津 | 5个 | 0 | 222ms | 15.6%  
北京 | 8个 | 1个 | 226ms | 1.0%  
江苏 | 58个 | 1个 | 246ms | 12.2%  
浙江 | 49个 | 2个 | 251ms | 9.2%  
吉林 | 16个 | 0 | 252ms | 11.2%  
辽宁 | 38个 | 0 | 260ms | 13.0%  
福建 | 34个 | 2个 | 271ms | 10.3%  
河北 | 34个 | 0 | 271ms | 15.8%  
上海 | 7个 | 0 | 271ms | 1.3%  
陕西 | 30个 | 0 | 272ms | 12.9%  
宁夏 | 12个 | 0 | 273ms | 12.3%  
山东 | 52个 | 1个 | 277ms | 17.5%  
黑龙江 | 38个 | 0 | 280ms | 14.7%  
江西 | 22个 | 0 | 283ms | 12.6%  
河南 | 49个 | 0 | 285ms | 16.6%  
安徽 | 38个 | 0 | 288ms | 11.9%  
均值 | 938个 | 14个 | 289ms | 14.0%  
内蒙古 | 32个 | 0 | 291ms | 14.7%  
山西 | 35个 | 1个 | 299ms | 17.4%  
湖北 | 48个 | 0 | 300ms | 13.1%  
广东 | 76个 | 3个 | 302ms | 14.5%  
青海 | 4个 | 0 | 307ms | 14.5%  
海南 | 12个 | 0 | 309ms | 11.8%  
甘肃 | 17个 | 0 | 311ms | 15.9%  
湖南 | 47个 | 0 | 311ms | 14.6%  
贵州 | 27个 | 2个 | 313ms | 18.9%  
广西 | 36个 | 0 | 315ms | 17.5%  
重庆 | 15个 | 1个 | 316ms | 10.6%  
四川 | 48个 | 0 | 324ms | 13.4%  
新疆 | 28个 | 0 | 324ms | 13.0%  
云南 | 22个 | 0 | 353ms | 19.6%  
西藏 | 1个 | 0 | 421ms | 29.0%  
  
**简评：** 如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有938个，其中超时点14个，平均响应时间为289毫秒，丢包率为14%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的19个，超过300毫秒的12个；  
超时点较多的省份：北京；  
丢包率较高的省份：天津、江苏、吉林、辽宁、福建、河北、陕西、宁夏、山东、黑龙江、江西、河南、安徽、内蒙古、山西、湖北、广东、青海、海南、甘肃、湖南、贵州、广西、重庆、四川、新疆、云南、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_idc_vultr_usa-dallas_20180514_overseas.png)

**海外线路到Vultr美国-达拉斯机房的测速数据 [20180514]**

国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---  
美国 | 19个 | 0 | 34ms | 0.4%  
加拿大 | 3个 | 0 | 52ms | 0.5%  
法国 | 2个 | 0 | 112ms | 0  
巴西 | 1个 | 0 | 136ms | 0  
德国 | 2个 | 0 | 145ms | 0  
日本 | 2个 | 0 | 158ms | 2.0%  
英国 | 1个 | 0 | 174ms | 0  
台湾 | 1个 | 0 | 184ms | -  
韩国 | 13个 | 0 | 185ms | 0.3%  
均值 | 77个 | 0 | 191ms | 2.3%  
澳大利亚 | 1个 | 0 | 192ms | 0  
新加坡 | 6个 | 0 | 206ms | 0  
菲律宾 | 1个 | 0 | 207ms | 1.0%  
俄罗斯 | 1个 | 0 | 207ms | 0  
香港 | 18个 | 0 | 209ms | 0  
马来西亚 | 3个 | 0 | 235ms | 1.3%  
印度尼西亚 | 1个 | 0 | 272ms | 3.0%  
南非 | 1个 | 0 | 326ms | 0  
柬埔寨 | 1个 | 0 | 414ms | 30.0%  
  
**简评：** 如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有77个，其中超时点0个，平均响应时间为191毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的8个，在200-300毫秒间的6个，超过300毫秒的2个；  
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
  * 到Vultr达拉斯机房的 _其他近期报告_ ： 
    * [20180527](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")
    * [20180622](/vultr/idc/dallas/20180622-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180622")
    * [20180804](/vultr/idc/dallas/20180804-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180804")
    * [20180918](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/dallas/20180514-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180514")



本文最初发表于[多地到Vultr达拉斯[Dallas]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-vultr-idc-dallas.html)
