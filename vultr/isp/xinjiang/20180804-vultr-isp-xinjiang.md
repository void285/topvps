#  新疆到Vultr各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![新疆到Vultr各机房的测速数据（20180804）](/images/thumbnails/Xinjiang_to_vultr.png)

本文的数据视角为 **新疆到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在新疆且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点1501个，其中超时点6个。连通概况如下：大陆线路响应均值为322毫秒，最快的三个机房所在地为东京、洛杉矶、硅谷，最慢的三个为悉尼、亚特兰大、迈阿密；东京、悉尼有响应超时情况；新加坡、东京、西雅图、悉尼、芝加哥等8处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 新疆图表数据

![大陆省份新疆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_isp_xinjiang_vultr_20180804.png)

### 全部运营商

新疆全部运营商到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 135个 | 3个 | 256ms | 19% | 均值 | 1501个 | 6个 | 322ms | 8%  
洛杉矶 | 75个 | 0 | 264ms | 2% | 芝加哥 | 79个 | 0 | 335ms | 9%  
硅谷 | 127个 | 0 | 273ms | 9% | 伦敦 | 135个 | 0 | 355ms | 1%  
西雅图 | 79个 | 0 | 295ms | 16% | 新泽西 | 131个 | 0 | 366ms | 5%  
巴黎 | 79个 | 0 | 296ms | 2% | 阿姆斯特丹 | 79个 | 0 | 367ms | 7%  
新加坡 | 75个 | 0 | 307ms | 23% | 悉尼 | 79个 | 3个 | 376ms | 16%  
法兰克福 | 135个 | 0 | 309ms | 2% | 亚特兰大 | 79个 | 0 | 381ms | 3%  
达拉斯 | 135个 | 0 | 318ms | 3% | 迈阿密 | 79个 | 0 | 384ms | 4%  
  
简评：本表展示了新疆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻新疆，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到，各机房所在城市的响应值、丢包率都较高（TopVPS推荐选用响应值低于250ms，丢包率在5%%以内的机房），请慎重选择；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

新疆电信到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 87个 | 3个 | 285ms | 31% | 均值 | 933个 | 6个 | 334ms | 9%  
洛杉矶 | 43个 | 0 | 289ms | 5% | 芝加哥 | 47个 | 0 | 344ms | 3%  
硅谷 | 83个 | 0 | 272ms | 1% | 伦敦 | 87个 | 0 | 363ms | 2%  
西雅图 | 47个 | 0 | 299ms | 2% | 新泽西 | 87个 | 0 | 388ms | 3%  
巴黎 | 47个 | 0 | 251ms | 0 | 阿姆斯特丹 | 47个 | 0 | 365ms | 11%  
新加坡 | 43个 | 0 | 347ms | 42% | 悉尼 | 47个 | 3个 | 457ms | 27%  
法兰克福 | 87个 | 0 | 263ms | 0 | 亚特兰大 | 47个 | 0 | 379ms | 3%  
达拉斯 | 87个 | 0 | 357ms | 4% | 迈阿密 | 47个 | 0 | 425ms | 5%  
  
简评：如果你是来自新疆的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，很遗憾从本次测试来看，没有值得你关注的机房；请查看往期的测试，如果数据一直不乐观，你应考虑换用其他VPS提供商如[BandwagonHost](https://vps123.top/go/bandwagon/_1)、[Digital Ocean](https://vps123.top/go/digitalocean/_2)、[Linode](https://vps123.top/go/linode/_3)等。

### 联通

新疆联通到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 20个 | 0 | 295ms | 22% | 均值 | 188个 | 0 | 326ms | 7%  
洛杉矶 | 8个 | 0 | 242ms | 0 | 芝加哥 | 8个 | 0 | 333ms | 5%  
硅谷 | 20个 | 0 | 252ms | 2% | 伦敦 | 20个 | 0 | 392ms | 1%  
西雅图 | 8个 | 0 | 260ms | 6% | 新泽西 | 16个 | 0 | 370ms | 10%  
巴黎 | 8个 | 0 | 312ms | 0 | 阿姆斯特丹 | 8个 | 0 | 379ms | 4%  
新加坡 | 8个 | 0 | 389ms | 26% | 悉尼 | 8个 | 0 | 413ms | 21%  
法兰克福 | 20个 | 0 | 323ms | 1% | 亚特兰大 | 8个 | 0 | 395ms | 4%  
达拉斯 | 20个 | 0 | 279ms | 3% | 迈阿密 | 8个 | 0 | 359ms | 2%  
  
简评：如果你是来自新疆的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_4)吧！

### 移动

新疆移动到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 28个 | 0 | 189ms | 5% | 均值 | 380个 | 0 | 305ms | 8%  
洛杉矶 | 24个 | 0 | 260ms | 0 | 芝加哥 | 24个 | 0 | 330ms | 19%  
硅谷 | 24个 | 0 | 294ms | 23% | 伦敦 | 28个 | 0 | 309ms | 0  
西雅图 | 24个 | 0 | 327ms | 41% | 新泽西 | 28个 | 0 | 341ms | 1%  
巴黎 | 24个 | 0 | 324ms | 5% | 阿姆斯特丹 | 24个 | 0 | 356ms | 5%  
新加坡 | 24个 | 0 | 187ms | 2% | 悉尼 | 24个 | 0 | 259ms | 0  
法兰克福 | 28个 | 0 | 342ms | 6% | 亚特兰大 | 24个 | 0 | 370ms | 3%  
达拉斯 | 28个 | 0 | 317ms | 3% | 迈阿密 | 24个 | 0 | 370ms | 5%  
  
简评：如果你是来自新疆的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡、东京** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_5)吧！

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
    * [大陆](/vultr/isp/china/20180804-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180804")
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
    * [云南](/vultr/isp/yunnan/20180804-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180804")
    * [浙江](/vultr/isp/zhejiang/20180804-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180804")
  * 新疆到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/xinjiang/20180514-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/xinjiang/20180527-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/xinjiang/20180622-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180622")
    * [20180918](/vultr/isp/xinjiang/20180918-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180918")
  * 本期报告：新疆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/xinjiang/20180804-bandwagon-isp-xinjiang.md "新疆到BandwagonHost各机房的Ping测试 20180804")
    * [Digital Ocean](/digitalocean/isp/xinjiang/20180804-digitalocean-isp-xinjiang.md "新疆到Digital Ocean各机房的Ping测试 20180804")
    * [Linode](/linode/isp/xinjiang/20180804-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180804")



本文最初发表于[新疆到Vultr各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-vultr-isp-xinjiang.html)
