#  多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![多地到Digital Ocean法兰克福\[Frankfurt\]机房的Ping测试（20180514）](/images/thumbnails/to_do_Frankfurt.png)

本篇的数据视角为全国各地以及海外运营商的网络环境下，到[Digital Ocean](https://vps123.top/go/do)的[德国-法兰克福机房](https://vps123.top/digitalocean-facilities.html#frankfurt)的网络连接；若你有[主要面向大陆用户的站点](https://vps123.top/website-for-mainland-users.html)或[外贸站](https://vps123.top/website-for-internation-trade.html)运行在VPS提供商[Digital Ocean](https://vps123.top/go/do)的德国-法兰克福机房，可以从这些数据中了解用户访问你的站点的响应速度和体验。如果你认为当前使用的主机在主要用户所在地的访问体验不佳，可以查看[Digital Ocean全部机房](/digitalocean/isp/china/20180514-digitalocean-isp-china.md)的数据或其他VPS提供商的机房数据（文末有链接），发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514多地到Digital Ocean德国-法兰克福机房的PING测试结果，连通概况如下：大陆31个省市的972个有效测试样本中，共有超时点16个；响应均值为288毫秒，最快的三地区为天津、上海、北京，最慢的三地区为新疆、山东、西藏；浙江、广东、山东、北京、重庆等11处有响应超时情况；吉林、江苏、浙江、黑龙江、山东等10处丢包率较高。海外19个国家地区的81个有效测试样本中，无超时点；响应均值为183毫秒，最快的三地区为法国、荷兰、德国，最慢的三地区为韩国、澳大利亚、柬埔寨；柬埔寨丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆测速点

![大陆各省份到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_germany-frankfurt_20180514_mainland.png)

大陆各省份到Digital Ocean德国-法兰克福机房的测速数据 [20180514] 省份 | 测速点 | 超时点 | 响应时间 | 丢包率 | 省份 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
天津 | 5个 | 0 | 222ms | 3.0% | 云南 | 25个 | 0 | 284ms | 0.8%  
上海 | 8个 | 0 | 231ms | 0 | 湖北 | 47个 | 0 | 285ms | 5.0%  
北京 | 7个 | 1个 | 238ms | 5.3% | 山西 | 34个 | 0 | 286ms | 6.0%  
重庆 | 15个 | 1个 | 262ms | 0.4% | 福建 | 37个 | 1个 | 288ms | 1.5%  
甘肃 | 22个 | 0 | 262ms | 1.1% | 均值 | 972个 | 16个 | 288ms | 5.1%  
河北 | 31个 | 0 | 263ms | 4.2% | 青海 | 4个 | 0 | 290ms | 0  
安徽 | 43个 | 0 | 264ms | 4.3% | 四川 | 50个 | 1个 | 291ms | 4.5%  
广西 | 39个 | 1个 | 273ms | 1.8% | 陕西 | 33个 | 0 | 298ms | 4.3%  
辽宁 | 37个 | 0 | 274ms | 3.5% | 江苏 | 62个 | 1个 | 305ms | 10.7%  
宁夏 | 12个 | 0 | 275ms | 3.8% | 贵州 | 29个 | 0 | 309ms | 6.3%  
海南 | 11个 | 0 | 277ms | 0.8% | 黑龙江 | 39个 | 0 | 312ms | 8.7%  
广东 | 81个 | 2个 | 278ms | 4.3% | 吉林 | 16个 | 0 | 313ms | 11.9%  
内蒙古 | 31个 | 0 | 278ms | 4.1% | 浙江 | 51个 | 4个 | 318ms | 10.0%  
湖南 | 45个 | 1个 | 281ms | 4.2% | 新疆 | 27个 | 0 | 319ms | 4.0%  
河南 | 55个 | 1个 | 282ms | 5.5% | 山东 | 52个 | 2个 | 325ms | 7.1%  
江西 | 23个 | 0 | 283ms | 6.7% | 西藏 | 1个 | 0 | 358ms | 1.0%  
  
简评：如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向大陆访客的网站](website-for-mainland-users.html)，本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了大陆各省份的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有972个，其中超时点16个，平均响应时间为288毫秒，丢包率为5%，本站评价等级为 **较差** ，不太推荐在位于这里的机房建站。

以下是就各省份数据的统计概要：  
平均响应时间的分布：在200-300毫秒间的23个，超过300毫秒的8个；  
超时点较多的省份：北京；  
丢包率较高的省份：江苏、吉林、浙江；

## 海外测速点

![海外各国家地区到VPS提供商Digital Ocean位于法兰克福\[Frankfurt\]的机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/do_20180514/plot_idc_do_germany-frankfurt_20180514_overseas.png)

海外线路到Digital Ocean德国-法兰克福机房的测速数据 [20180514] 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率 | 国家地区 | 测速点 | 超时点 | 响应时间 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
法国 | 2个 | 0 | 10ms | 0 | 南非 | 2个 | 0 | 199ms | 0  
荷兰 | 1个 | 0 | 11ms | 0 | 香港 | 19个 | 0 | 220ms | 0  
德国 | 2个 | 0 | 14ms | 0 | 巴西 | 1个 | 0 | 221ms | 0  
英国 | 2个 | 0 | 33ms | 0 | 菲律宾 | 1个 | 0 | 226ms | 0  
俄罗斯 | 1个 | 0 | 90ms | 0 | 马来西亚 | 3个 | 0 | 228ms | 0  
加拿大 | 3个 | 0 | 102ms | 0.5% | 日本 | 2个 | 0 | 256ms | 0  
美国 | 18个 | 0 | 152ms | 0 | 台湾 | 1个 | 0 | 282ms | -  
新加坡 | 6个 | 0 | 174ms | 0 | 韩国 | 13个 | 0 | 287ms | 0  
均值 | 81个 | 0 | 183ms | 1.3% | 澳大利亚 | 2个 | 0 | 325ms | 0  
印度尼西亚 | 1个 | 0 | 191ms | 3.0% | 柬埔寨 | 1个 | 0 | 471ms | 19.0%  
  
简评：如果你考虑在Digital Ocean的法兰克福[Frankfurt]机房部署[主要面向海外访客的网站](https://vps123.top/website-for-internation-trade.html)（例如外贸站），本表可以作为一个很好的参考，它提供了有关响应速度以及丢包率的详细数据，反映了海外各国家/地区的测速点到位于法兰克福[Frankfurt]的机房的连通状况。到此机房的ping监测点共有81个，其中超时点0个，平均响应时间为183毫秒，丢包率为1%，本站评价等级为 **一般** ，可以考虑在位于这里的机房建站。

以下是就各国家/地区数据的统计概要：  
平均响应时间的分布：在50毫秒以内的4个，在50-100毫秒间的1个，在100-200毫秒间的5个，在200-300毫秒间的7个，超过300毫秒的2个；  
丢包率较高的国家/地区：柬埔寨；

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180514 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180514 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期到Digital Ocean _其他机房_ 的报告： 
    * [阿姆斯特丹](/digitalocean/idc/amsterdam/20180514-digitalocean-idc-amsterdam.md "多地到Digital Ocean阿姆斯特丹机房的Ping测试 20180514")
    * [班加罗尔](/digitalocean/idc/bangalore/20180514-digitalocean-idc-bangalore.md "多地到Digital Ocean班加罗尔机房的Ping测试 20180514")
    * [伦敦](/digitalocean/idc/london/20180514-digitalocean-idc-london.md "多地到Digital Ocean伦敦机房的Ping测试 20180514")
    * [纽约](/digitalocean/idc/newyork/20180514-digitalocean-idc-newyork.md "多地到Digital Ocean纽约机房的Ping测试 20180514")
    * [旧金山](/digitalocean/idc/sanfrancisco/20180514-digitalocean-idc-sanfrancisco.md "多地到Digital Ocean旧金山机房的Ping测试 20180514")
    * [新加坡](/digitalocean/idc/singapore/20180514-digitalocean-idc-singapore.md "多地到Digital Ocean新加坡机房的Ping测试 20180514")
    * [多伦多](/digitalocean/idc/toronto/20180514-digitalocean-idc-toronto.md "多地到Digital Ocean多伦多机房的Ping测试 20180514")
  * 到Digital Ocean法兰克福机房的 _其他近期报告_ ： 
    * [20180527](/digitalocean/idc/frankfurt/20180527-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180527")
    * [20180622](/digitalocean/idc/frankfurt/20180622-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180622")
    * [20180804](/digitalocean/idc/frankfurt/20180804-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180804")
    * [20180918](/digitalocean/idc/frankfurt/20180918-digitalocean-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180918")
  * 本期报告：在法兰克福部署机房的 _其他VPS提供商_ ： 
    * [Digital Ocean](do/idc/frankfurt/20180514-do-idc-frankfurt.md "多地到Digital Ocean法兰克福机房的Ping测试 20180514")
    * [Linode](/linode/idc/frankfurt/20180514-linode-idc-frankfurt.md "多地到Linode法兰克福机房的Ping测试 20180514")
    * [Vultr](/vultr/idc/frankfurt/20180514-vultr-idc-frankfurt.md "多地到Vultr法兰克福机房的Ping测试 20180514")



本文最初发表于[多地到Digital Ocean法兰克福[Frankfurt]机房的Ping测试（20180514）](https://vps123.top/pingtest/20180514-digitalocean-idc-frankfurt.html)
