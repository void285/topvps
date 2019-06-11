#  甘肃到Vultr各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![甘肃到Vultr各机房的测速数据（20180804）](/images/thumbnails/Gansu_to_vultr.png)

本文的数据视角为 **甘肃到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在甘肃且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点1208个，无超时点。连通概况如下：大陆线路响应均值为293毫秒，最快的三个机房所在地为东京、硅谷、洛杉矶，最慢的三个为新泽西、伦敦、阿姆斯特丹；新加坡、东京、西雅图、悉尼、硅谷等8处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 甘肃图表数据

![大陆省份甘肃到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_isp_gansu_vultr_20180804.png)

### 全部运营商

甘肃全部运营商到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 112个 | 0 | 194ms | 18% | 巴黎 | 60个 | 0 | 294ms | 2%  
硅谷 | 108个 | 0 | 243ms | 10% | 芝加哥 | 60个 | 0 | 299ms | 10%  
洛杉矶 | 60个 | 0 | 255ms | 4% | 悉尼 | 60个 | 0 | 327ms | 14%  
新加坡 | 60个 | 0 | 269ms | 18% | 迈阿密 | 60个 | 0 | 333ms | 7%  
西雅图 | 60个 | 0 | 274ms | 14% | 亚特兰大 | 60个 | 0 | 335ms | 1%  
达拉斯 | 112个 | 0 | 286ms | 5% | 新泽西 | 112个 | 0 | 339ms | 2%  
法兰克福 | 112个 | 0 | 293ms | 4% | 伦敦 | 112个 | 0 | 341ms | 2%  
均值 | 1208个 | 0 | 293ms | 7% | 阿姆斯特丹 | 60个 | 0 | 351ms | 4%  
  
简评：本表展示了甘肃的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻甘肃，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到，各机房所在城市的响应值、丢包率都较高（TopVPS推荐选用响应值低于250ms，丢包率在5%%以内的机房），请慎重选择；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

甘肃电信到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 72个 | 0 | 258ms | 36% | 巴黎 | 36个 | 0 | 251ms | 0  
硅谷 | 68个 | 0 | 276ms | 3% | 芝加哥 | 36个 | 0 | 354ms | 6%  
洛杉矶 | 36个 | 0 | 284ms | 9% | 悉尼 | 36个 | 0 | 444ms | 30%  
新加坡 | 36个 | 0 | 328ms | 44% | 迈阿密 | 36个 | 0 | 406ms | 6%  
西雅图 | 36个 | 0 | 300ms | 1% | 亚特兰大 | 36个 | 0 | 363ms | 2%  
达拉斯 | 72个 | 0 | 332ms | 4% | 新泽西 | 72个 | 0 | 412ms | 3%  
法兰克福 | 72个 | 0 | 225ms | 0 | 伦敦 | 72个 | 0 | 361ms | 4%  
均值 | 752个 | 0 | 325ms | 10% | 阿姆斯特丹 | 36个 | 0 | 373ms | 4%  
  
简评：如果你是来自甘肃的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **法兰克福** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

甘肃联通到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 4个 | 0 | 168ms | 10% | 巴黎 | 4个 | 0 | 361ms | 1%  
硅谷 | 4个 | 0 | 187ms | 4% | 芝加哥 | 4个 | 0 | 249ms | 18%  
洛杉矶 | 4个 | 0 | 229ms | 3% | 悉尼 | 4个 | 0 | 277ms | 8%  
新加坡 | 4个 | 0 | 292ms | 0 | 迈阿密 | 4个 | 0 | 257ms | 7%  
西雅图 | 4个 | 0 | 251ms | 13% | 亚特兰大 | 4个 | 0 | 291ms | 2%  
达拉斯 | 4个 | 0 | 232ms | 7% | 新泽西 | 4个 | 0 | 281ms | 2%  
法兰克福 | 4个 | 0 | 375ms | 11% | 伦敦 | 4个 | 0 | 341ms | 2%  
均值 | 60个 | 0 | 275ms | 6% | 阿姆斯特丹 | 4个 | 0 | 342ms | 3%  
  
简评：如果你是来自甘肃的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **硅谷、洛杉矶** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、达拉斯、芝加哥** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

甘肃移动到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 36个 | 0 | 156ms | 7% | 巴黎 | 20个 | 0 | 272ms | 5%  
硅谷 | 36个 | 0 | 268ms | 23% | 芝加哥 | 20个 | 0 | 294ms | 6%  
洛杉矶 | 20个 | 0 | 253ms | 2% | 悉尼 | 20个 | 0 | 261ms | 3%  
新加坡 | 20个 | 0 | 187ms | 10% | 迈阿密 | 20个 | 0 | 338ms | 8%  
西雅图 | 20个 | 0 | 272ms | 29% | 亚特兰大 | 20个 | 0 | 353ms | 0  
达拉斯 | 36个 | 0 | 293ms | 5% | 新泽西 | 36个 | 0 | 326ms | 0  
法兰克福 | 36个 | 0 | 278ms | 2% | 伦敦 | 36个 | 0 | 322ms | 1%  
均值 | 396个 | 0 | 279ms | 7% | 阿姆斯特丹 | 20个 | 0 | 338ms | 6%  
  
简评：如果你是来自甘肃的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，请慎重选择部署在 **东京、新加坡** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
  * 甘肃到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/gansu/20180514-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/gansu/20180527-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/gansu/20180622-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180622")
    * [20180918](/vultr/isp/gansu/20180918-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180918")
  * 本期报告：甘肃到 _其他VPS提供商_ 各机房的测速报告： 
    * [Digital Ocean](/digitalocean/isp/gansu/20180804-digitalocean-isp-gansu.md "甘肃到Digital Ocean各机房的Ping测试 20180804")
    * [Linode](/linode/isp/gansu/20180804-linode-isp-gansu.md "甘肃到Linode各机房的Ping测试 20180804")



本文最初发表于[甘肃到Vultr各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-vultr-isp-gansu.html)
