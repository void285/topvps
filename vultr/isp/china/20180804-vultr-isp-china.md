#  大陆到Vultr各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![大陆到Vultr各机房的测速数据（20180804）](/images/thumbnails/China_to_vultr.png)

本文的数据视角为 **中国大陆各省份/运营商到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在大陆，打算在[Vultr](https://vps123.top/go/vultr)的机房架设代理服务器或进行云计算，后面的图表数据可以帮你形成评估Vultr各机房的大概印象，排除一些数据较差的机房，锁定一些潜在的目标机房。要确定最适合你的机房，请通过本文结尾的链接，查看你所在省份的数据，它们更准确、针对性更强；你也可以通过文末链接查看其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点59932个，其中超时点697个。连通概况如下：大陆线路响应均值为278毫秒，最快的三个机房所在地为东京、洛杉矶、硅谷，最慢的三个为新泽西、迈阿密、阿姆斯特丹；悉尼、东京、新加坡、硅谷、亚特兰大等15处有响应超时情况；新加坡、东京、悉尼、西雅图、硅谷等8处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆图表数据

![大陆省份大陆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_isp_china_vultr_20180804.png)

### 全部运营商

**大陆全部运营商到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 5257个 | 72个 | 192ms | 18%  
洛杉矶 | 3120个 | 44个 | 221ms | 3%  
硅谷 | 5228个 | 60个 | 239ms | 9%  
西雅图 | 3089个 | 29个 | 239ms | 9%  
新加坡 | 3157个 | 68个 | 243ms | 18%  
达拉斯 | 5268个 | 33个 | 264ms | 3%  
均值 | 59932个 | 697个 | 278ms | 7%  
芝加哥 | 3113个 | 32个 | 283ms | 7%  
法兰克福 | 5282个 | 33个 | 293ms | 3%  
巴黎 | 3157个 | 36个 | 294ms | 2%  
伦敦 | 5305个 | 42个 | 309ms | 3%  
亚特兰大 | 3170个 | 45个 | 318ms | 4%  
悉尼 | 3089个 | 83个 | 320ms | 15%  
新泽西 | 5208个 | 44个 | 324ms | 4%  
迈阿密 | 3245个 | 38个 | 325ms | 7%  
阿姆斯特丹 | 3244个 | 38个 | 330ms | 5%  
  
**简评：** 本表展示了大陆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；籍此我们可以快速了解，整个大陆地区到Vultr各个机房的平均响应速度以及丢包率：如果某机房的响应值、丢包率较高，那么大概率各省到此机房的网络也不理想，用来建站是不大合适的；而如果此处的响应值、丢包率还不错，我们可再具体了解一个省份的数据。  
在这里， **洛杉矶** 的响应速度小于250ms，且丢包率在5%以内，值得关注。如果你主要关心某运营商的网络概况，后面几个表格的数据更有参考价值。  
如果你打算将VPS用作科学上网、云存储、远程任务、游戏服务器等用途，请 **关注你所在的省份** 到Vultr各机房的测速数据，它们可以给你更有益的参考。

### 电信

**大陆电信到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 2175个 | 61个 | 225ms | 28%  
洛杉矶 | 1306个 | 37个 | 241ms | 4%  
硅谷 | 2166个 | 46个 | 253ms | 5%  
西雅图 | 1311个 | 19个 | 260ms | 4%  
新加坡 | 1327个 | 58个 | 285ms | 32%  
达拉斯 | 2166个 | 22个 | 291ms | 3%  
均值 | 25107个 | 510个 | 299ms | 8%  
芝加哥 | 1344个 | 25个 | 305ms | 5%  
法兰克福 | 2203个 | 22个 | 276ms | 2%  
巴黎 | 1335个 | 19个 | 276ms | 2%  
伦敦 | 2203个 | 22个 | 323ms | 3%  
亚特兰大 | 1357个 | 19个 | 341ms | 3%  
悉尼 | 1307个 | 67个 | 376ms | 24%  
新泽西 | 2158个 | 34个 | 365ms | 4%  
迈阿密 | 1375个 | 28个 | 368ms | 6%  
阿姆斯特丹 | 1374个 | 31个 | 335ms | 6%  
  
**简评：** 如果你关注电信的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **洛杉矶** 的整体的连通速度、丢包率都比较不错， **东京** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**大陆联通到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 1459个 | 3个 | 212ms | 15%  
洛杉矶 | 903个 | 3个 | 205ms | 2%  
硅谷 | 1490个 | 0 | 222ms | 5%  
西雅图 | 887个 | 6个 | 221ms | 10%  
新加坡 | 899个 | 3个 | 283ms | 12%  
达拉斯 | 1475个 | 3个 | 240ms | 3%  
均值 | 16961个 | 89个 | 274ms | 6%  
芝加哥 | 898个 | 3个 | 268ms | 6%  
法兰克福 | 1479个 | 3个 | 306ms | 3%  
巴黎 | 895个 | 10个 | 305ms | 1%  
伦敦 | 1467个 | 12个 | 327ms | 3%  
亚特兰大 | 902个 | 19个 | 298ms | 5%  
悉尼 | 883个 | 9个 | 326ms | 14%  
新泽西 | 1490个 | 6个 | 304ms | 6%  
迈阿密 | 915个 | 6个 | 288ms | 4%  
阿姆斯特丹 | 919个 | 3个 | 335ms | 3%  
  
**简评：** 如果你关注联通的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **洛杉矶、硅谷、达拉斯** 的整体的连通速度、丢包率都比较不错， **东京、西雅图** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**大陆移动到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 1623个 | 8个 | 133ms | 6%  
洛杉矶 | 911个 | 4个 | 208ms | 2%  
硅谷 | 1572个 | 14个 | 237ms | 17%  
西雅图 | 891个 | 4个 | 229ms | 16%  
新加坡 | 931个 | 7个 | 153ms | 7%  
达拉斯 | 1627个 | 8个 | 250ms | 2%  
均值 | 17864个 | 98个 | 254ms | 6%  
芝加哥 | 871个 | 4个 | 268ms | 10%  
法兰克福 | 1600个 | 8个 | 304ms | 3%  
巴黎 | 927个 | 7个 | 309ms | 4%  
伦敦 | 1635个 | 8个 | 279ms | 2%  
亚特兰大 | 911个 | 7个 | 309ms | 3%  
悉尼 | 899个 | 7个 | 238ms | 5%  
新泽西 | 1560个 | 4个 | 289ms | 2%  
迈阿密 | 955个 | 4个 | 305ms | 10%  
阿姆斯特丹 | 951个 | 4个 | 319ms | 6%  
  
**简评：** 如果你关注移动的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **洛杉矶、悉尼、达拉斯** 的整体的连通速度、丢包率都比较不错， **东京、新加坡、西雅图、硅谷** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180804 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180804 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180804-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180804")
    * [北京](/vultr/isp/beijing/20180804-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180804")
    * [重庆](/vultr/isp/chongqing/20180804-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180804")
    * [福建](/vultr/isp/fujian/20180804-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180804")
    * [甘肃](/vultr/isp/gansu/20180804-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180804")
    * [广东](/vultr/isp/guangdong/20180804-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180804")
    * [广西](/vultr/isp/guangxi/20180804-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180804")
    * [贵州](/vultr/isp/guizhou/20180804-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180804")
    * [海南](/vultr/isp/hainan/20180804-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180804")
    * [河北](/vultr/isp/hebei/20180804-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180804")
    * [黑龙江](/vultr/isp/heilongjiang/20180804-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180804")
    * [河南](/vultr/isp/henan/20180804-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180804")
    * [湖北](/vultr/isp/hubei/20180804-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180804")
    * [湖南](/vultr/isp/hunan/20180804-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180804")
    * [内蒙古](/vultr/isp/innermongolia/20180804-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180804")
    * [江苏](/vultr/isp/jiangsu/20180804-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180804")
    * [江西](/vultr/isp/jiangxi/20180804-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180804")
    * [吉林](/vultr/isp/jilin/20180804-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180804")
    * [辽宁](/vultr/isp/liaoning/20180804-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180804")
    * [宁夏](/vultr/isp/ningxia/20180804-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180804")
    * [青海](/vultr/isp/qinghai/20180804-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180804")
    * [山西](/vultr/isp/shan1xi/20180804-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180804")
    * [陕西](/vultr/isp/shan3xi/20180804-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180804")
    * [山东](/vultr/isp/shandong/20180804-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180804")
    * [上海](/vultr/isp/shanghai/20180804-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180804")
    * [四川](/vultr/isp/sichuan/20180804-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180804")
    * [天津](/vultr/isp/tianjin/20180804-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180804")
    * [西藏](/vultr/isp/tibet/20180804-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180804")
    * [新疆](/vultr/isp/xinjiang/20180804-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180804")
    * [云南](/vultr/isp/yunnan/20180804-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180804")
    * [浙江](/vultr/isp/zhejiang/20180804-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180804")
  * 大陆到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/china/20180514-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/china/20180527-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/china/20180622-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180622")
    * [20180918](/vultr/isp/china/20180918-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180918")
  * 本期报告：大陆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/china/20180804-bandwagon-isp-china.md "大陆到BandwagonHost各机房的Ping测试 20180804")
    * [Digital Ocean](/digitalocean/isp/china/20180804-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180804")
    * [Linode](/linode/isp/china/20180804-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180804")



本文最初发表于[大陆到Vultr各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-vultr-isp-china.html)
