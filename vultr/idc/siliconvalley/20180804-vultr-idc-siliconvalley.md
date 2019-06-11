#  多地到Vultr硅谷[SiliconValley]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr硅谷\[SiliconValley\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_SiliconValley.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-硅谷机房](https://vps123.top/vultr-facilities.html#siliconvalley)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-硅谷机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5228个有效测试样本中，共有超时点60个；响应均值为239毫秒，最快的三地区为海南、山东、湖北，最慢的三地区为河南、宁夏、西藏；浙江、江苏、广东、四川、江西等11处有响应超时情况；西藏、河南、黑龙江、宁夏、天津等28处丢包率较高。海外19个国家地区的240个有效测试样本中，无超时点；响应均值为164毫秒，最快的三地区为荷兰、美国、加拿大，最慢的三地区为马来西亚、印度尼西亚、菲律宾；菲律宾丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于硅谷\[SiliconValley\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-siliconvalley_20180804_mainland.png)

大陆各省份到Vultr美国-硅谷机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
海南 | 48个 | 0 | 215ms | 6.2% | 均值 | 5228个 | 60个 | 239ms | 9.1%  
山东 | 338个 | 0 | 218ms | 9.3% | 吉林 | 96个 | 0 | 242ms | 3.7%  
湖北 | 189个 | 3个 | 220ms | 7.1% | 江西 | 139个 | 4个 | 244ms | 9.7%  
河北 | 260个 | 0 | 225ms | 12.3% | 陕西 | 149个 | 0 | 245ms | 10.5%  
湖南 | 241个 | 0 | 226ms | 7.8% | 云南 | 119个 | 4个 | 246ms | 11.7%  
广东 | 441个 | 8个 | 227ms | 2.2% | 重庆 | 41个 | 0 | 246ms | 11.8%  
山西 | 189个 | 3个 | 228ms | 8.7% | 黑龙江 | 192个 | 0 | 247ms | 15.2%  
贵州 | 158个 | 0 | 229ms | 5.2% | 内蒙古 | 208个 | 0 | 252ms | 8.4%  
广西 | 248个 | 0 | 229ms | 6.6% | 四川 | 281个 | 6个 | 254ms | 8.4%  
安徽 | 211个 | 0 | 230ms | 12.1% | 上海 | 27个 | 4个 | 261ms | 5.7%  
福建 | 156个 | 3个 | 233ms | 7.6% | 青海 | 16个 | 0 | 265ms | 3.8%  
浙江 | 234个 | 13个 | 233ms | 9.6% | 甘肃 | 108个 | 0 | 270ms | 10.0%  
天津 | 16个 | 0 | 234ms | 13.2% | 新疆 | 127个 | 0 | 271ms | 6.1%  
北京 | 32个 | 0 | 235ms | 12.0% | 河南 | 355个 | 0 | 278ms | 16.3%  
江苏 | 343个 | 9个 | 236ms | 10.3% | 宁夏 | 32个 | 0 | 281ms | 13.7%  
辽宁 | 226个 | 3个 | 238ms | 5.9% | 西藏 | 8个 | 0 | 399ms | 60.5%  
  
简评：如果你考虑在Vultr的硅谷[SiliconValley]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于硅谷[SiliconValley]的机房的连通状况。到此机房的ping监测点共有5228个，其中超时点60个，平均响应时间为239毫秒，丢包率为9%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的30个，超过300毫秒的1个；  
超时点较多的省份：上海；  
丢包率较高的省份：河北、安徽、天津、北京、江苏、陕西、云南、重庆、黑龙江、甘肃、河南、宁夏、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于硅谷\[SiliconValley\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-siliconvalley_20180804_overseas.png)

海外线路到Vultr美国-硅谷机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
荷兰 | 3个 | 0 | 21ms | 0 | 均值 | 240个 | 0 | 164ms | 2.2%  
美国 | 48个 | 0 | 50ms | 4.7% | 澳大利亚 | 6个 | 0 | 166ms | 0  
加拿大 | 15个 | 0 | 78ms | 0 | 德国 | 9个 | 0 | 170ms | 0  
日本 | 6个 | 0 | 133ms | 2.2% | 法国 | 3个 | 0 | 181ms | 0  
巴西 | 3个 | 0 | 140ms | 0 | 南非 | 6个 | 0 | 189ms | 0.5%  
新加坡 | 15个 | 0 | 142ms | 0 | 俄罗斯 | 3个 | 0 | 193ms | -  
韩国 | 21个 | 0 | 149ms | 0 | 英国 | 6个 | 0 | 197ms | 0  
意大利 | 3个 | 0 | 156ms | - | 马来西亚 | 12个 | 0 | 218ms | 0.5%  
香港 | 66个 | 0 | 163ms | 0 | 印度尼西亚 | 6个 | 0 | 276ms | 0  
台湾 | 3个 | 0 | 164ms | 0 | 菲律宾 | 6个 | 0 | 342ms | 30.0%  
  
简评：如果你考虑在Vultr的硅谷[SiliconValley]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于硅谷[SiliconValley]的机房的连通状况。到此机房的ping监测点共有240个，其中超时点0个，平均响应时间为164毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的1个，在100-200毫秒间的13个，在200-300毫秒间的2个，超过300毫秒的1个；  
丢包率较高的国家/地区：菲律宾；

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180804 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180804 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期到Vultr _其他机房_ 的报告： 
    * [阿姆斯特丹](/vultr/idc/amsterdam/20180804-vultr-idc-amsterdam.md "多地到Vultr阿姆斯特丹机房的Ping测试 20180804")
    * [亚特兰大](/vultr/idc/atlanta/20180804-vultr-idc-atlanta.md "多地到Vultr亚特兰大机房的Ping测试 20180804")
    * [芝加哥](/vultr/idc/chicago/20180804-vultr-idc-chicago.md "多地到Vultr芝加哥机房的Ping测试 20180804")
    * [达拉斯](/vultr/idc/dallas/20180804-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180804")
    * [法兰克福](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")
    * [伦敦](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")
    * [洛杉矶](/vultr/idc/losangeles/20180804-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180804")
    * [迈阿密](/vultr/idc/miami/20180804-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180804")
    * [新泽西](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr硅谷机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/siliconvalley/20180514-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180514")
    * [20180527](/vultr/idc/siliconvalley/20180527-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180527")
    * [20180622](/vultr/idc/siliconvalley/20180622-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180622")
    * [20180918](/vultr/idc/siliconvalley/20180918-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180918")



本文最初发表于[多地到Vultr硅谷[SiliconValley]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-siliconvalley.html)
