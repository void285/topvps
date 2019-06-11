#  重庆到Vultr各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![重庆到Vultr各机房的测速数据（20180804）](/images/thumbnails/Chongqing_to_vultr.png)

本文的数据视角为 **重庆到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在重庆且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点623个，其中超时点12个。连通概况如下：大陆线路响应均值为263毫秒，最快的三个机房所在地为东京、新加坡、洛杉矶，最慢的三个为法兰克福、亚特兰大、新泽西；洛杉矶、巴黎、芝加哥、新泽西有响应超时情况；迈阿密、芝加哥、硅谷、东京、悉尼等8处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 重庆图表数据

![大陆省份重庆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_isp_chongqing_vultr_20180804.png)

### 全部运营商

**重庆全部运营商到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 45个 | 0 | 178ms | 12%  
新加坡 | 41个 | 0 | 210ms | 6%  
洛杉矶 | 41个 | 3个 | 212ms | 2%  
西雅图 | 37个 | 0 | 220ms | 0  
硅谷 | 41个 | 0 | 242ms | 12%  
均值 | 623个 | 12个 | 263ms | 6%  
巴黎 | 41个 | 3个 | 273ms | 4%  
达拉斯 | 41个 | 0 | 277ms | 0  
悉尼 | 41个 | 0 | 279ms | 8%  
芝加哥 | 41个 | 3个 | 292ms | 13%  
阿姆斯特丹 | 41个 | 0 | 302ms | 5%  
伦敦 | 45个 | 0 | 306ms | 2%  
迈阿密 | 41个 | 0 | 308ms | 17%  
法兰克福 | 45个 | 0 | 312ms | 1%  
亚特兰大 | 41个 | 0 | 313ms | 1%  
新泽西 | 41个 | 3个 | 321ms | 6%  
  
**简评：** 本表展示了重庆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻重庆，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶、西雅图** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**重庆电信到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 19个 | 0 | 216ms | 28%  
新加坡 | 19个 | 0 | 287ms | 20%  
洛杉矶 | 19个 | 3个 | 243ms | 6%  
西雅图 | 15个 | 0 | 271ms | 2%  
硅谷 | 15个 | 0 | 266ms | 5%  
均值 | 269个 | 6个 | 296ms | 8%  
巴黎 | 19个 | 0 | 257ms | 1%  
达拉斯 | 15个 | 0 | 311ms | 0  
悉尼 | 19个 | 0 | 371ms | 25%  
芝加哥 | 19个 | 0 | 295ms | 1%  
阿姆斯特丹 | 19个 | 0 | 329ms | 4%  
伦敦 | 19个 | 0 | 318ms | 4%  
迈阿密 | 19个 | 0 | 357ms | 3%  
法兰克福 | 19个 | 0 | 255ms | 0  
亚特兰大 | 19个 | 0 | 360ms | 3%  
新泽西 | 15个 | 3个 | 376ms | 18%  
  
**简评：** 如果你是来自重庆的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，请慎重选择部署在 **东京、洛杉矶** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**重庆联通到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 14个 | 0 | 172ms | 0  
新加坡 | 14个 | 0 | 226ms | 0  
洛杉矶 | 14个 | 0 | 191ms | 0  
西雅图 | 14个 | 0 | 200ms | 0  
硅谷 | 14个 | 0 | 217ms | 21%  
均值 | 210个 | 6个 | 236ms | 5%  
巴黎 | 14个 | 3个 | 282ms | 8%  
达拉斯 | 14个 | 0 | 230ms | 0  
悉尼 | 14个 | 0 | 270ms | 0  
芝加哥 | 14个 | 3个 | 260ms | 17%  
阿姆斯特丹 | 14个 | 0 | 309ms | 7%  
伦敦 | 14个 | 0 | 302ms | 0  
迈阿密 | 14个 | 0 | 274ms | 26%  
法兰克福 | 14个 | 0 | 352ms | 1%  
亚特兰大 | 14个 | 0 | 294ms | 0  
新泽西 | 14个 | 0 | 258ms | 0  
  
**简评：** 如果你是来自重庆的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、洛杉矶、西雅图、新加坡、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **硅谷** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**重庆移动到Vultr各机房的测速数据 [20180804]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 12个 | 0 | 147ms | 7%  
新加坡 | 8个 | 0 | 116ms | 0  
洛杉矶 | 8个 | 0 | 204ms | 0  
西雅图 | 8个 | 0 | 190ms | 0  
硅谷 | 12个 | 0 | 242ms | 11%  
均值 | 144个 | 0 | 256ms | 5%  
巴黎 | 8个 | 0 | 280ms | 3%  
达拉斯 | 12个 | 0 | 291ms | 2%  
悉尼 | 8个 | 0 | 198ms | 0  
芝加哥 | 8个 | 0 | 323ms | 22%  
阿姆斯特丹 | 8个 | 0 | 270ms | 3%  
伦敦 | 12个 | 0 | 299ms | 2%  
迈阿密 | 8个 | 0 | 294ms | 21%  
法兰克福 | 12个 | 0 | 330ms | 3%  
亚特兰大 | 8个 | 0 | 284ms | 1%  
新泽西 | 12个 | 0 | 329ms | 1%  
  
**简评：** 如果你是来自重庆的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡、西雅图、悉尼、洛杉矶** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、硅谷** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
  * 重庆到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/chongqing/20180514-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/chongqing/20180527-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/chongqing/20180622-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180622")
    * [20180918](/vultr/isp/chongqing/20180918-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180918")
  * 本期报告：重庆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/chongqing/20180804-bandwagon-isp-chongqing.md "重庆到BandwagonHost各机房的Ping测试 20180804")
    * [Digital Ocean](/digitalocean/isp/chongqing/20180804-digitalocean-isp-chongqing.md "重庆到Digital Ocean各机房的Ping测试 20180804")
    * [Linode](/linode/isp/chongqing/20180804-linode-isp-chongqing.md "重庆到Linode各机房的Ping测试 20180804")



本文最初发表于[重庆到Vultr各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-vultr-isp-chongqing.html)
