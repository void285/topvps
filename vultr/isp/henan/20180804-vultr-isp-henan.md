#  河南到Vultr各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![河南到Vultr各机房的测速数据（20180804）](/images/thumbnails/Henan_to_vultr.png)

本文的数据视角为 **河南到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在河南且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点3905个，其中超时点12个。连通概况如下：大陆线路响应均值为279毫秒，最快的三个机房所在地为东京、洛杉矶、新加坡，最慢的三个为新泽西、阿姆斯特丹、迈阿密；悉尼、亚特兰大、伦敦、阿姆斯特丹有响应超时情况；西雅图、硅谷、新加坡、东京、悉尼等10处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 河南图表数据

![大陆省份河南到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_isp_henan_vultr_20180804.png)

### 全部运营商

**河南全部运营商到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 339个 | 0 | 189ms | 14%  
洛杉矶 | 191个 | 0 | 217ms | 3%  
新加坡 | 199个 | 0 | 222ms | 14%  
西雅图 | 195个 | 0 | 239ms | 22%  
达拉斯 | 367个 | 0 | 266ms | 3%  
法兰克福 | 355个 | 0 | 270ms | 3%  
巴黎 | 199个 | 0 | 271ms | 3%  
硅谷 | 355个 | 0 | 279ms | 16%  
均值 | 3905个 | 12个 | 279ms | 9%  
悉尼 | 195个 | 3个 | 306ms | 14%  
芝加哥 | 195个 | 0 | 310ms | 8%  
亚特兰大 | 199个 | 3个 | 319ms | 6%  
伦敦 | 339个 | 3个 | 323ms | 4%  
新泽西 | 367个 | 0 | 326ms | 5%  
阿姆斯特丹 | 203个 | 3个 | 331ms | 10%  
迈阿密 | 207个 | 0 | 340ms | 10%  
  
**简评：** 本表展示了河南的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻河南，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**河南电信到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 108个 | 0 | 209ms | 21%  
洛杉矶 | 48个 | 0 | 256ms | 3%  
新加坡 | 60个 | 0 | 244ms | 25%  
西雅图 | 60个 | 0 | 269ms | 19%  
达拉斯 | 112个 | 0 | 320ms | 5%  
法兰克福 | 108个 | 0 | 265ms | 2%  
巴黎 | 60个 | 0 | 289ms | 2%  
硅谷 | 104个 | 0 | 306ms | 11%  
均值 | 1176个 | 0 | 299ms | 9%  
悉尼 | 60个 | 0 | 349ms | 24%  
芝加哥 | 56个 | 0 | 335ms | 5%  
亚特兰大 | 60个 | 0 | 349ms | 2%  
伦敦 | 104个 | 0 | 298ms | 1%  
新泽西 | 108个 | 0 | 339ms | 2%  
阿姆斯特丹 | 64个 | 0 | 301ms | 9%  
迈阿密 | 64个 | 0 | 380ms | 7%  
  
**简评：** 如果你是来自河南的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，请慎重选择部署在 **东京、新加坡** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**河南联通到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 107个 | 0 | 228ms | 16%  
洛杉矶 | 79个 | 0 | 187ms | 1%  
新加坡 | 75个 | 0 | 278ms | 9%  
西雅图 | 75个 | 0 | 208ms | 13%  
达拉斯 | 127个 | 0 | 223ms | 0  
法兰克福 | 135个 | 0 | 284ms | 2%  
巴黎 | 79个 | 0 | 255ms | 0  
硅谷 | 131个 | 0 | 279ms | 13%  
均值 | 1441个 | 12个 | 291ms | 8%  
悉尼 | 75个 | 3个 | 330ms | 10%  
芝加哥 | 79个 | 0 | 327ms | 10%  
亚特兰大 | 79个 | 3个 | 287ms | 6%  
伦敦 | 115个 | 3个 | 397ms | 10%  
新泽西 | 131个 | 0 | 351ms | 11%  
阿姆斯特丹 | 75个 | 3个 | 400ms | 11%  
迈阿密 | 79个 | 0 | 331ms | 11%  
  
**简评：** 如果你是来自河南的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **西雅图、东京** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**河南移动到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 124个 | 0 | 130ms | 5%  
洛杉矶 | 64个 | 0 | 207ms | 6%  
新加坡 | 64个 | 0 | 144ms | 8%  
西雅图 | 60个 | 0 | 240ms | 34%  
达拉斯 | 128个 | 0 | 255ms | 4%  
法兰克福 | 112个 | 0 | 260ms | 5%  
巴黎 | 60个 | 0 | 268ms | 7%  
硅谷 | 120个 | 0 | 253ms | 23%  
均值 | 1288个 | 0 | 248ms | 9%  
悉尼 | 60个 | 0 | 238ms | 8%  
芝加哥 | 60个 | 0 | 268ms | 7%  
亚特兰大 | 60个 | 0 | 320ms | 8%  
伦敦 | 120个 | 0 | 275ms | 2%  
新泽西 | 128个 | 0 | 289ms | 2%  
阿姆斯特丹 | 64个 | 0 | 291ms | 10%  
迈阿密 | 64个 | 0 | 310ms | 10%  
  
**简评：** 如果你是来自河南的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **新加坡、洛杉矶、悉尼、西雅图** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
  * 河南到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/henan/20180514-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/henan/20180527-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/henan/20180622-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180622")
    * [20180918](/vultr/isp/henan/20180918-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180918")
  * 本期报告：河南到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/henan/20180804-bandwagon-isp-henan.md "河南到BandwagonHost各机房的Ping测试 20180804")
    * [Digital Ocean](/digitalocean/isp/henan/20180804-digitalocean-isp-henan.md "河南到Digital Ocean各机房的Ping测试 20180804")
    * [Linode](/linode/isp/henan/20180804-linode-isp-henan.md "河南到Linode各机房的Ping测试 20180804")



本文最初发表于[河南到Vultr各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-vultr-isp-henan.html)
