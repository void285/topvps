#  多地到Vultr达拉斯[Dallas]机房的Ping测试（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Vultr达拉斯\[Dallas\]机房的Ping测试（20180622）](/images/thumbnails/to_vultr_Dallas.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Vultr](https://vps123.top/go/vultr)的[美国-达拉斯机房](https://vps123.top/vultr-facilities.html#dallas)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Vultr](https://vps123.top/go/vultr)的美国-达拉斯机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Vultr全部机房](/vultr/isp/china/20180622-vultr-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的879个有效测试样本中，共有超时点23个；响应均值为247毫秒，最快的三地区为上海、广东、北京，最慢的三地区为新疆、云南、香港；云南、江苏、浙江、香港、上海等9处有响应超时情况；贵州丢包率较高。海外17个国家地区的74个有效测试样本中，共有超时点2个；响应均值为156毫秒，最快的三地区为美国、加拿大、德国，最慢的三地区为菲律宾、越南、印度尼西亚；香港有响应超时情况。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-dallas_20180622_mainland.png)

大陆各省份到Vultr美国-达拉斯机房的测速数据 [20180622] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
上海 | 8个 | 1个 | 215ms | 0.4% | 均值 | 879个 | 23个 | 247ms | 1.6%  
广东 | 71个 | 1个 | 229ms | 2.1% | 陕西 | 28个 | 1个 | 248ms | 1.0%  
北京 | 9个 | 0 | 229ms | 3.3% | 重庆 | 12个 | 0 | 250ms | 5.0%  
河北 | 29个 | 0 | 230ms | 0.9% | 山西 | 35个 | 0 | 250ms | 0.1%  
山东 | 37个 | 0 | 231ms | 1.9% | 内蒙古 | 33个 | 0 | 254ms | 0.7%  
广西 | 41个 | 0 | 235ms | 1.4% | 浙江 | 49个 | 3个 | 255ms | 2.9%  
福建 | 32个 | 0 | 238ms | 1.2% | 宁夏 | 14个 | 0 | 255ms | 0.4%  
天津 | 3个 | 0 | 239ms | 0 | 吉林 | 18个 | 0 | 256ms | 1.3%  
湖南 | 33个 | 0 | 239ms | 0.4% | 黑龙江 | 30个 | 0 | 262ms | 0.3%  
安徽 | 33个 | 1个 | 241ms | 1.0% | 四川 | 42个 | 0 | 264ms | 1.2%  
江苏 | 67个 | 3个 | 243ms | 3.5% | 江西 | 21个 | 0 | 264ms | 2.2%  
河南 | 51个 | 1个 | 244ms | 1.6% | 青海 | 5个 | 0 | 273ms | 0  
贵州 | 23个 | 0 | 244ms | 5.4% | 甘肃 | 17个 | 0 | 278ms | 0.1%  
海南 | 9个 | 0 | 245ms | 0.2% | 新疆 | 20个 | 0 | 289ms | 1.6%  
辽宁 | 33个 | 0 | 246ms | 2.4% | 云南 | 24个 | 10个 | 290ms | 0.3%  
湖北 | 34个 | 0 | 247ms | 2.4% | 香港 | 18个 | 2个 | - | -  
  
简评：如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有879个，其中超时点23个，平均响应时间为247毫秒，丢包率为1%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在200-300毫秒间的30个；  
超时点较多的省份：上海、云南、香港；

## 海外测速点

![海外各国家地区到VPS提供商Vultr位于达拉斯\[Dallas\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_idc_vultr_usa-dallas_20180622_overseas.png)

海外线路到Vultr美国-达拉斯机房的测速数据 [20180622] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
美国 | 19个 | 0 | 37ms | 0 | 新加坡 | 5个 | 0 | 170ms | 0  
加拿大 | 1个 | 0 | 66ms | 0 | 香港 | 18个 | 2个 | 171ms | 0  
德国 | 1个 | 0 | 112ms | - | 南非 | 2个 | 0 | 171ms | 0  
意大利 | 1个 | 0 | 121ms | - | 英国 | 2个 | 0 | 172ms | 0  
巴西 | 1个 | 0 | 125ms | 0 | 韩国 | 14个 | 0 | 186ms | 0  
法国 | 1个 | 0 | 126ms | 0 | 澳大利亚 | 1个 | 0 | 199ms | 4.0%  
日本 | 2个 | 0 | 145ms | 1.0% | 菲律宾 | 2个 | 0 | 209ms | 0.5%  
均值 | 74个 | 2个 | 156ms | 0.6% | 越南 | 2个 | 0 | 219ms | 0  
台湾 | 1个 | 0 | 166ms | 0 | 印度尼西亚 | 1个 | 0 | 265ms | 4.0%  
  
简评：如果你考虑在Vultr的达拉斯[Dallas]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于达拉斯[Dallas]的机房的连通状况。到此机房的ping监测点共有74个，其中超时点2个，平均响应时间为156毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的1个，在50-100毫秒间的1个，在100-200毫秒间的12个，在200-300毫秒间的3个；  
超时点较多的国家/地区：香港；

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
    * [法兰克福](/vultr/idc/frankfurt/20180622-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180622")
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
  * 到Vultr达拉斯机房的 _其他近期报告_ ： 
    * [20180514](/vultr/idc/dallas/20180514-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180514")
    * [20180527](/vultr/idc/dallas/20180527-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180527")
    * [20180804](/vultr/idc/dallas/20180804-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180804")
    * [20180918](/vultr/idc/dallas/20180918-vultr-idc-dallas.md "多地到Vultr达拉斯机房的Ping测试 20180918")
  * 本期报告：在达拉斯部署机房的 _其他VPS提供商_ ： 
    * [Linode](/linode/idc/dallas/20180622-linode-idc-dallas.md "多地到Linode达拉斯机房的Ping测试 20180622")



本文最初发表于[多地到Vultr达拉斯[Dallas]机房的Ping测试（20180622）](https://vps123.top/pingtest/20180622-vultr-idc-dallas.html)
