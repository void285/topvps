#  多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean法兰克福\[Frankfurt\]机房的Ping测试（20180804）](/images/thumbnails/to_do_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[德国-法兰克福机房](https://vps123.top/digitalocean-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180804-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

大陆31个省市的4635个有效测试样本中，共有超时点49个；响应均值为302毫秒，最快的三地区为青海、甘肃、辽宁，最慢的三地区为贵州、吉林、西藏；浙江、江苏、江西、上海、辽宁等9处有响应超时情况；西藏、宁夏、海南、福建、河南等7处丢包率较高。海外20个国家地区的209个有效测试样本中，共有超时点6个；响应均值为181毫秒，最快的三地区为意大利、巴西、德国，最慢的三地区为澳大利亚、法国、菲律宾；香港、韩国有响应超时情况；菲律宾丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_germany-frankfurt_20180804_mainland.png)

大陆各省份到Digital Ocean德国-法兰克福机房的测速数据 [20180804] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
青海 | 16个 | 0 | 242ms | 0.3% | 均值 | 4635个 | 49个 | 302ms | 3.3%  
甘肃 | 104个 | 0 | 243ms | 1.1% | 云南 | 111个 | 0 | 303ms | 4.3%  
辽宁 | 206个 | 3个 | 256ms | 1.8% | 湖南 | 225个 | 0 | 304ms | 3.0%  
重庆 | 34个 | 0 | 260ms | 3.0% | 浙江 | 202个 | 13个 | 305ms | 2.6%  
河北 | 212个 | 0 | 270ms | 3.0% | 江苏 | 326个 | 9个 | 310ms | 2.8%  
北京 | 36个 | 0 | 271ms | 0.7% | 新疆 | 99个 | 0 | 310ms | 2.5%  
陕西 | 129个 | 0 | 276ms | 2.0% | 广东 | 409个 | 3个 | 312ms | 2.6%  
内蒙古 | 184个 | 0 | 277ms | 1.6% | 山东 | 343个 | 0 | 313ms | 1.5%  
宁夏 | 24个 | 0 | 279ms | 14.6% | 河南 | 291个 | 3个 | 317ms | 5.4%  
天津 | 20个 | 0 | 282ms | 1.7% | 黑龙江 | 136个 | 0 | 320ms | 3.4%  
广西 | 219个 | 0 | 289ms | 3.8% | 湖北 | 165个 | 0 | 321ms | 5.3%  
福建 | 152个 | 0 | 291ms | 6.0% | 四川 | 257个 | 0 | 322ms | 3.7%  
江西 | 127个 | 8个 | 296ms | 1.6% | 安徽 | 190个 | 3个 | 325ms | 5.1%  
上海 | 27个 | 4个 | 301ms | 3.1% | 贵州 | 122个 | 0 | 327ms | 2.8%  
海南 | 32个 | 0 | 301ms | 8.4% | 吉林 | 72个 | 0 | 329ms | 3.8%  
山西 | 157个 | 3个 | 302ms | 3.5% | 西藏 | 8个 | 0 | 481ms | 20.5%  
  
简评：如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有4635个，其中超时点49个，平均响应时间为302毫秒，丢包率为3%，本站评价等级为 **很差** ，十分不推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的13个，超过300毫秒的18个；  
超时点较多的省份：上海；  
丢包率较高的省份：宁夏、西藏；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/do_20180804/plot_idc_do_germany-frankfurt_20180804_overseas.png)

海外线路到Digital Ocean德国-法兰克福机房的测速数据 [20180804] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
意大利 | 3个 | 0 | 11ms | - | 均值 | 209个 | 6个 | 181ms | 0.7%  
巴西 | 3个 | 0 | 16ms | 0 | 香港 | 66个 | 3个 | 191ms | 0  
德国 | 7个 | 0 | 20ms | 0 | 马来西亚 | 5个 | 0 | 205ms | 0.2%  
英国 | 4个 | 0 | 49ms | 0 | 越南 | 1个 | 0 | 236ms | 0  
俄罗斯 | 3个 | 0 | 49ms | - | 韩国 | 21个 | 3个 | 271ms | 0  
加拿大 | 11个 | 0 | 112ms | 0.2% | 日本 | 4个 | 0 | 274ms | 0  
荷兰 | 3个 | 0 | 147ms | 0 | 台湾 | 3个 | 0 | 303ms | 0  
南非 | 3个 | 0 | 148ms | 0 | 澳大利亚 | 4个 | 0 | 307ms | 0  
新加坡 | 13个 | 0 | 167ms | 0 | 法国 | 3个 | 0 | 320ms | 0  
美国 | 44个 | 0 | 168ms | 0 | 菲律宾 | 4个 | 0 | 452ms | 12.5%  
印度尼西亚 | 4个 | 0 | 177ms | 0 |  |  |  |  |   
  
简评：如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有209个，其中超时点6个，平均响应时间为181毫秒，丢包率为0%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的5个，在100-200毫秒间的7个，在200-300毫秒间的4个，超过300毫秒的4个；  
超时点较多的国家/地区：韩国；  
丢包率较高的国家/地区：菲律宾；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180804 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180804 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180804-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180804")
    * [班加罗尔](/digitalocean/idc/bangalore/20180804-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180804")
    * [伦敦](/digitalocean/idc/london/20180804-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180804")
    * [纽约](/digitalocean/idc/newyork/20180804-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180804")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180804-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180804")
    * [新加坡](/digitalocean/idc/singapore/20180804-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180804")
    * [多伦多](/digitalocean/idc/toronto/20180804-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180804")
  * 到Digital Ocean法兰克福机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/idc/frankfurt/20180514-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [20180527](/digitalocean/idc/frankfurt/20180527-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/frankfurt/20180622-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [20180918](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180804-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [Linode](/linode/idc/frankfurt/20180804-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180804")
    * [Vultr](/vultr/idc/frankfurt/20180804-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180804")



本文最初发表于[多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180804）](https://vps123.top/pingtest/20180804-digitalocean-idc-frankfurt.html)
