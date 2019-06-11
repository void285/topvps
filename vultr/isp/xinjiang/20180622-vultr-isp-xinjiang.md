#  新疆到Vultr各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![新疆到Vultr各机房的测速数据（20180622）](/images/thumbnails/Xinjiang_to_vultr.png)

本文的数据视角为 **新疆到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在新疆且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点328个，其中超时点4个。连通概况如下：大陆线路响应均值为307毫秒，最快的三个机房所在地为东京、西雅图、洛杉矶，最慢的三个为悉尼、迈阿密、阿姆斯特丹；东京、新加坡、法兰克福、悉尼有响应超时情况；芝加哥、亚特兰大、迈阿密、伦敦、东京等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 新疆图表数据

![大陆省份新疆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_isp_xinjiang_vultr_20180622.png)

### 全部运营商

**新疆全部运营商到Vultr各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 19个 | 1个 | 235ms | 12%  
西雅图 | 20个 | 0 | 266ms | 1%  
洛杉矶 | 24个 | 0 | 271ms | 1%  
硅谷 | 26个 | 0 | 273ms | 1%  
达拉斯 | 20个 | 0 | 284ms | 1%  
新加坡 | 25个 | 1个 | 297ms | 7%  
法兰克福 | 27个 | 1个 | 306ms | 1%  
均值 | 328个 | 4个 | 307ms | 9%  
巴黎 | 24个 | 0 | 314ms | 0  
芝加哥 | 18个 | 0 | 323ms | 30%  
亚特兰大 | 18个 | 0 | 330ms | 28%  
新泽西 | 20个 | 0 | 336ms | 1%  
伦敦 | 19个 | 0 | 337ms | 19%  
悉尼 | 24个 | 1个 | 344ms | 5%  
迈阿密 | 20个 | 0 | 350ms | 27%  
阿姆斯特丹 | 24个 | 0 | 368ms | 2%  
  
**简评：** 本表展示了新疆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻新疆，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到，各机房所在城市的响应值、丢包率都较高（TopVPS推荐选用响应值低于250ms，丢包率在5%%以内的机房），请慎重选择；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**新疆电信到Vultr各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 10个 | 1个 | 291ms | 25%  
西雅图 | 11个 | 0 | 287ms | 0  
洛杉矶 | 12个 | 0 | 298ms | 0  
硅谷 | 13个 | 0 | 287ms | 2%  
达拉斯 | 11个 | 0 | 304ms | 1%  
新加坡 | 12个 | 1个 | 351ms | 17%  
法兰克福 | 13个 | 1个 | 259ms | 5%  
均值 | 167个 | 4个 | 321ms | 6%  
巴黎 | 11个 | 0 | 257ms | 0  
芝加哥 | 9个 | 0 | 331ms | 9%  
亚特兰大 | 9个 | 0 | 343ms | 8%  
新泽西 | 11个 | 0 | 361ms | 0  
伦敦 | 10个 | 0 | 318ms | 5%  
悉尼 | 12个 | 1个 | 454ms | 10%  
迈阿密 | 11个 | 0 | 360ms | 6%  
阿姆斯特丹 | 12个 | 0 | 390ms | 4%  
  
**简评：** 如果你是来自新疆的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，很遗憾从本次测试来看，没有值得你关注的机房；请查看往期的测试，如果数据一直不乐观，你应考虑换用其他VPS提供商如[BandwagonHost](https://vps123.top/go/bandwagon/_1)、[Digital Ocean](https://vps123.top/go/digitalocean/_2)、[Linode](https://vps123.top/go/linode/_3)等。

### 联通

**新疆联通到Vultr各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 3个 | 0 | 247ms | 5%  
西雅图 | 3个 | 0 | 255ms | 0  
洛杉矶 | 2个 | 0 | 256ms | 0  
硅谷 | 3个 | 0 | 275ms | 2%  
达拉斯 | 3个 | 0 | 262ms | 0  
新加坡 | 3个 | 0 | 325ms | 0  
法兰克福 | 4个 | 0 | 368ms | 0  
均值 | 43个 | 0 | 322ms | 17%  
巴黎 | 3个 | 0 | 376ms | 0  
芝加哥 | 3个 | 0 | 342ms | 69%  
亚特兰大 | 3个 | 0 | 329ms | 66%  
新泽西 | 3个 | 0 | 337ms | 0  
伦敦 | 3个 | 0 | 388ms | 45%  
悉尼 | 2个 | 0 | 313ms | 2%  
迈阿密 | 3个 | 0 | 356ms | 60%  
阿姆斯特丹 | 2个 | 0 | 391ms | 0  
  
**简评：** 如果你是来自新疆的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_4)吧！

### 移动

**新疆移动到Vultr各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 6个 | 0 | 168ms | 6%  
西雅图 | 6个 | 0 | 255ms | 4%  
洛杉矶 | 10个 | 0 | 259ms | 2%  
硅谷 | 10个 | 0 | 257ms | 0  
达拉斯 | 6个 | 0 | 287ms | 2%  
新加坡 | 10个 | 0 | 215ms | 4%  
法兰克福 | 10个 | 0 | 290ms | 0  
均值 | 118个 | 0 | 279ms | 4%  
巴黎 | 10个 | 0 | 310ms | 2%  
芝加哥 | 6个 | 0 | 296ms | 13%  
亚特兰大 | 6个 | 0 | 319ms | 10%  
新泽西 | 6个 | 0 | 312ms | 5%  
伦敦 | 6个 | 0 | 306ms | 7%  
悉尼 | 10个 | 0 | 267ms | 3%  
迈阿密 | 6个 | 0 | 335ms | 14%  
阿姆斯特丹 | 10个 | 0 | 323ms | 2%  
  
**简评：** 如果你是来自新疆的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_5)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180622 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180622 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180622-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180622")
    * [北京](/vultr/isp/beijing/20180622-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180622")
    * [大陆](/vultr/isp/china/20180622-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180622")
    * [重庆](/vultr/isp/chongqing/20180622-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180622")
    * [福建](/vultr/isp/fujian/20180622-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180622")
    * [甘肃](/vultr/isp/gansu/20180622-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180622")
    * [广东](/vultr/isp/guangdong/20180622-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180622")
    * [广西](/vultr/isp/guangxi/20180622-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180622")
    * [贵州](/vultr/isp/guizhou/20180622-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180622")
    * [海南](/vultr/isp/hainan/20180622-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180622")
    * [河北](/vultr/isp/hebei/20180622-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180622")
    * [黑龙江](/vultr/isp/heilongjiang/20180622-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180622")
    * [河南](/vultr/isp/henan/20180622-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180622")
    * [湖北](/vultr/isp/hubei/20180622-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180622")
    * [湖南](/vultr/isp/hunan/20180622-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180622")
    * [内蒙古](/vultr/isp/innermongolia/20180622-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180622")
    * [江苏](/vultr/isp/jiangsu/20180622-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180622")
    * [江西](/vultr/isp/jiangxi/20180622-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180622")
    * [吉林](/vultr/isp/jilin/20180622-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180622")
    * [辽宁](/vultr/isp/liaoning/20180622-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180622")
    * [宁夏](/vultr/isp/ningxia/20180622-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180622")
    * [青海](/vultr/isp/qinghai/20180622-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180622")
    * [山西](/vultr/isp/shan1xi/20180622-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180622")
    * [陕西](/vultr/isp/shan3xi/20180622-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180622")
    * [山东](/vultr/isp/shandong/20180622-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180622")
    * [上海](/vultr/isp/shanghai/20180622-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180622")
    * [四川](/vultr/isp/sichuan/20180622-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180622")
    * [天津](/vultr/isp/tianjin/20180622-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180622")
    * [西藏](/vultr/isp/tibet/20180622-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180622")
    * [云南](/vultr/isp/yunnan/20180622-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180622")
    * [浙江](/vultr/isp/zhejiang/20180622-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180622")
  * 新疆到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/xinjiang/20180514-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/xinjiang/20180527-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180527")
    * [20180804](/vultr/isp/xinjiang/20180804-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/xinjiang/20180918-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180918")
  * 本期报告：新疆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/xinjiang/20180622-bandwagon-isp-xinjiang.md "新疆到BandwagonHost各机房的Ping测试 20180622")
    * [Digital Ocean](/digitalocean/isp/xinjiang/20180622-digitalocean-isp-xinjiang.md "新疆到Digital Ocean各机房的Ping测试 20180622")
    * [Linode](/linode/isp/xinjiang/20180622-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180622")



本文最初发表于[新疆到Vultr各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-vultr-isp-xinjiang.html)
