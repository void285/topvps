#  多地到Vultr达拉斯[Dallas]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr达拉斯\[Dallas\]机房的Ping测试（20180804）](/images/thumbnails/to_vultr_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-达拉斯机房](https://vps123.top/vultr-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180804-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的5268个有效测试样本中，共有超时点33个；响应均值为264毫秒，最快的三地区为北京、天津、广东，最慢的三地区为青海、新疆、西藏；浙江、江苏、上海、江西、广东等6处有响应超时情况；西藏、青海、上海、安徽、内蒙古等7处丢包率较高。海外18个国家地区的237个有效测试样本中，共有超时点3个；响应均值为165毫秒，最快的三地区为荷兰、加拿大、美国，最慢的三地区为马来西亚、印度尼西亚、菲律宾；香港有响应超时情况；菲律宾丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-dallas_20180804_mainland.png)

大陆各省份到Vultr美国-达拉斯机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
北京 | 36个 | 0 | 234ms | 1.7% | 河南 | 367个 | 0 | 264ms | 3.4%  
天津 | 16个 | 0 | 236ms | 5.3% | 均值 | 5268个 | 33个 | 264ms | 3.1%  
广东 | 430个 | 3个 | 241ms | 1.4% | 福建 | 148个 | 0 | 265ms | 5.6%  
山东 | 346个 | 0 | 243ms | 1.0% | 江苏 | 350个 | 9个 | 266ms | 4.7%  
海南 | 48个 | 0 | 247ms | 1.6% | 安徽 | 224个 | 0 | 269ms | 6.5%  
湖北 | 201个 | 0 | 250ms | 2.7% | 吉林 | 92个 | 0 | 270ms | 2.4%  
湖南 | 253个 | 3个 | 251ms | 1.7% | 内蒙古 | 212个 | 0 | 272ms | 6.3%  
河北 | 260个 | 0 | 253ms | 2.5% | 四川 | 285个 | 0 | 274ms | 1.2%  
浙江 | 238个 | 10个 | 256ms | 1.7% | 辽宁 | 213个 | 0 | 277ms | 3.0%  
上海 | 31个 | 4个 | 256ms | 6.7% | 云南 | 119个 | 0 | 279ms | 4.4%  
陕西 | 149个 | 0 | 258ms | 1.0% | 重庆 | 41个 | 0 | 283ms | 1.0%  
贵州 | 154个 | 0 | 259ms | 2.7% | 宁夏 | 32个 | 0 | 297ms | 3.9%  
广西 | 248个 | 0 | 259ms | 2.8% | 甘肃 | 112个 | 0 | 316ms | 4.4%  
黑龙江 | 172个 | 0 | 262ms | 4.9% | 青海 | 16个 | 0 | 330ms | 12.5%  
山西 | 197个 | 0 | 262ms | 1.1% | 新疆 | 135个 | 0 | 337ms | 4.0%  
江西 | 135个 | 4个 | 263ms | 4.8% | 西藏 | 8个 | 0 | 455ms | 14.8%  
  
简评：如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有5268个，其中超时点33个，平均响应时间为264毫秒，丢包率为3%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的27个，超过300毫秒的4个；  
超时点较多的省份：上海；  
丢包率较高的省份：青海、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_idc_vultr_usa-dallas_20180804_overseas.png)

海外线路到Vultr美国-达拉斯机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
荷兰 | 3个 | 0 | 28ms | 0 | 新加坡 | 15个 | 0 | 177ms | 0  
加拿大 | 15个 | 0 | 49ms | 0 | 南非 | 6个 | 0 | 178ms | 0.5%  
美国 | 48个 | 0 | 70ms | 5.0% | 香港 | 66个 | 3个 | 186ms | 0  
巴西 | 3个 | 0 | 110ms | 0 | 韩国 | 21个 | 0 | 191ms | 0  
意大利 | 3个 | 0 | 115ms | - | 台湾 | 3个 | 0 | 202ms | 0  
德国 | 9个 | 0 | 134ms | 0 | 澳大利亚 | 6个 | 0 | 204ms | 0  
日本 | 6个 | 0 | 155ms | 3.8% | 马来西亚 | 12个 | 0 | 250ms | 0.5%  
俄罗斯 | 3个 | 0 | 160ms | - | 印度尼西亚 | 6个 | 0 | 264ms | 0  
均值 | 237个 | 3个 | 165ms | 2.5% | 菲律宾 | 6个 | 0 | 321ms | 30.0%  
英国 | 6个 | 0 | 175ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有237个，其中超时点3个，平均响应时间为165毫秒，丢包率为2%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的2个，在50-100毫秒间的1个，在100-200毫秒间的10个，在200-300毫秒间的4个，超过300毫秒的1个；  
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
    * [法兰克福](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")
    * [伦敦](/vultr/idc/london/20180804-vultr-idc-london.md "多地到Vultr伦敦机房的Ping测试 20180804")
    * [洛杉矶](/vultr/idc/losangeles/20180804-vultr-idc-losangeles.md "多地到Vultr洛杉矶机房的Ping测试 20180804")
    * [迈阿密](/vultr/idc/miami/20180804-vultr-idc-miami.md "多地到Vultr迈阿密机房的Ping测试 20180804")
    * [新泽西](/vultr/idc/newjersey/20180804-vultr-idc-newjersey.md "多地到Vultr新泽西机房的Ping测试 20180804")
    * [巴黎](/vultr/idc/paris/20180804-vultr-idc-paris.md "多地到Vultr巴黎机房的Ping测试 20180804")
    * [西雅图](/vultr/idc/seattle/20180804-vultr-idc-seattle.md "多地到Vultr西雅图机房的Ping测试 20180804")
    * [硅谷](/vultr/idc/siliconvalley/20180804-vultr-idc-siliconvalley.md "多地到Vultr硅谷机房的Ping测试 20180804")
    * [新加坡](/vultr/idc/singapore/20180804-vultr-idc-singapore.md "多地到Vultr新加坡机房的Ping测试 20180804")
    * [悉尼](/vultr/idc/sydney/20180804-vultr-idc-sydney.md "多地到Vultr悉尼机房的Ping测试 20180804")
    * [东京](/vultr/idc/tokyo/20180804-vultr-idc-tokyo.md "多地到Vultr东京机房的Ping测试 20180804")
  * 到Vultr达拉斯机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/dallas/20180514-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180514")
    * [20180527](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")
    * [20180622](/vultr/idc/dallas/20180622-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180622")
    * [20180918](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/dallas/20180804-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180804")



本文最初发表于[多地到Vultr达拉斯[Dallas]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-vultr-idc-dallas.html)
