#  云南到Vultr各机房的测速数据（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![云南到Vultr各机房的测速数据（20180527）](/images/thumbnails/Yunnan_to_vultr.png)

本文的数据视角为 **云南到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在云南且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点293个，其中超时点5个。连通概况如下：大陆线路响应均值为272毫秒，最快的三个机房所在地为东京、新加坡、硅谷，最慢的三个为悉尼、亚特兰大、伦敦；硅谷、洛杉矶、芝加哥、迈阿密、亚特兰大有响应超时情况；亚特兰大、达拉斯、迈阿密、芝加哥、悉尼等11处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 云南图表数据

![大陆省份云南到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_isp_yunnan_vultr_20180527.png)

### 全部运营商

云南全部运营商到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 21个 | 0 | 174ms | 9% | 芝加哥 | 18个 | 1个 | 284ms | 11%  
新加坡 | 20个 | 0 | 205ms | 10% | 达拉斯 | 20个 | 0 | 300ms | 16%  
硅谷 | 20个 | 1个 | 222ms | 8% | 阿姆斯特丹 | 18个 | 0 | 307ms | 2%  
洛杉矶 | 20个 | 1个 | 229ms | 4% | 迈阿密 | 18个 | 1个 | 307ms | 15%  
西雅图 | 20个 | 0 | 232ms | 7% | 新泽西 | 20个 | 0 | 308ms | 4%  
均值 | 293个 | 5个 | 272ms | 9% | 悉尼 | 20个 | 0 | 315ms | 10%  
巴黎 | 20个 | 0 | 279ms | 5% | 亚特兰大 | 19个 | 1个 | 318ms | 20%  
法兰克福 | 19个 | 0 | 279ms | 1% | 伦敦 | 20个 | 0 | 334ms | 6%  
  
简评：本表展示了云南的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻云南，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

云南电信到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 10个 | 0 | 216ms | 17% | 芝加哥 | 9个 | 1个 | 328ms | 13%  
新加坡 | 10个 | 0 | 282ms | 23% | 达拉斯 | 10个 | 0 | 308ms | 9%  
硅谷 | 10个 | 1个 | 247ms | 7% | 阿姆斯特丹 | 9个 | 0 | 273ms | 0  
洛杉矶 | 10个 | 1个 | 267ms | 11% | 迈阿密 | 9个 | 1个 | 303ms | 7%  
西雅图 | 10个 | 0 | 275ms | 9% | 新泽西 | 10个 | 0 | 336ms | 3%  
均值 | 146个 | 5个 | 289ms | 10% | 悉尼 | 10个 | 0 | 363ms | 23%  
巴黎 | 10个 | 0 | 270ms | 6% | 亚特兰大 | 10个 | 1个 | 309ms | 16%  
法兰克福 | 9个 | 0 | 264ms | 1% | 伦敦 | 10个 | 0 | 302ms | 2%  
  
简评：如果你是来自云南的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，请慎重选择部署在 **东京、硅谷** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

云南联通到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 4个 | 0 | 175ms | 4% | 芝加哥 | 3个 | 0 | 273ms | 10%  
新加坡 | 4个 | 0 | 220ms | 5% | 达拉斯 | 4个 | 0 | 270ms | 10%  
硅谷 | 4个 | 0 | 217ms | 11% | 阿姆斯特丹 | 3个 | 0 | 318ms | 2%  
洛杉矶 | 4个 | 0 | 219ms | 0 | 迈阿密 | 3个 | 0 | 290ms | 13%  
西雅图 | 4个 | 0 | 230ms | 11% | 新泽西 | 4个 | 0 | 295ms | 10%  
均值 | 56个 | 0 | 272ms | 7% | 悉尼 | 4个 | 0 | 312ms | 5%  
巴黎 | 4个 | 0 | 309ms | 9% | 亚特兰大 | 3个 | 0 | 312ms | 14%  
法兰克福 | 4个 | 0 | 324ms | 2% | 伦敦 | 4个 | 0 | 349ms | 4%  
  
简评：如果你是来自云南的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、洛杉矶、新加坡** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **硅谷、西雅图** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

云南移动到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 7个 | 0 | 133ms | 6% | 芝加哥 | 6个 | 0 | 251ms | 9%  
新加坡 | 6个 | 0 | 113ms | 3% | 达拉斯 | 6个 | 0 | 323ms | 28%  
硅谷 | 6个 | 0 | 203ms | 7% | 阿姆斯特丹 | 6个 | 0 | 331ms | 4%  
洛杉矶 | 6个 | 0 | 202ms | 1% | 迈阿密 | 6个 | 0 | 327ms | 25%  
西雅图 | 6个 | 0 | 190ms | 0 | 新泽西 | 6个 | 0 | 293ms | 0  
均值 | 91个 | 0 | 254ms | 8% | 悉尼 | 6个 | 0 | 272ms | 3%  
巴黎 | 6个 | 0 | 259ms | 1% | 亚特兰大 | 6个 | 0 | 333ms | 29%  
法兰克福 | 6个 | 0 | 249ms | 0 | 伦敦 | 6个 | 0 | 351ms | 11%  
  
简评：如果你是来自云南的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡、西雅图、洛杉矶、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、硅谷** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180527) 
    * [全部](https://vps123.top/pingtests/20180527 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180527 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180527 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180527 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180527-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180527")
    * [北京](/vultr/isp/beijing/20180527-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180527")
    * [大陆](/vultr/isp/china/20180527-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180527")
    * [重庆](/vultr/isp/chongqing/20180527-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180527")
    * [福建](/vultr/isp/fujian/20180527-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180527")
    * [甘肃](/vultr/isp/gansu/20180527-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180527")
    * [广东](/vultr/isp/guangdong/20180527-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180527")
    * [广西](/vultr/isp/guangxi/20180527-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180527")
    * [贵州](/vultr/isp/guizhou/20180527-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180527")
    * [海南](/vultr/isp/hainan/20180527-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180527")
    * [河北](/vultr/isp/hebei/20180527-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180527")
    * [黑龙江](/vultr/isp/heilongjiang/20180527-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180527")
    * [河南](/vultr/isp/henan/20180527-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180527")
    * [湖北](/vultr/isp/hubei/20180527-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180527")
    * [湖南](/vultr/isp/hunan/20180527-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180527")
    * [内蒙古](/vultr/isp/innermongolia/20180527-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180527")
    * [江苏](/vultr/isp/jiangsu/20180527-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180527")
    * [江西](/vultr/isp/jiangxi/20180527-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180527")
    * [吉林](/vultr/isp/jilin/20180527-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180527")
    * [辽宁](/vultr/isp/liaoning/20180527-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180527")
    * [宁夏](/vultr/isp/ningxia/20180527-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180527")
    * [青海](/vultr/isp/qinghai/20180527-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180527")
    * [山西](/vultr/isp/shan1xi/20180527-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180527")
    * [陕西](/vultr/isp/shan3xi/20180527-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180527")
    * [山东](/vultr/isp/shandong/20180527-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180527")
    * [上海](/vultr/isp/shanghai/20180527-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180527")
    * [四川](/vultr/isp/sichuan/20180527-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180527")
    * [天津](/vultr/isp/tianjin/20180527-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180527")
    * [新疆](/vultr/isp/xinjiang/20180527-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180527")
    * [浙江](/vultr/isp/zhejiang/20180527-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180527")
  * 云南到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/yunnan/20180514-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180514")
    * [20180622](/vultr/isp/yunnan/20180622-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/yunnan/20180804-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/yunnan/20180918-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180918")
  * 本期报告：云南到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/yunnan/20180527-bandwagon-isp-yunnan.md "云南到BandwagonHost各机房的Ping测试 20180527")
    * [Digital Ocean](/digitalocean/isp/yunnan/20180527-digitalocean-isp-yunnan.md "云南到Digital Ocean各机房的Ping测试 20180527")
    * [Linode](/linode/isp/yunnan/20180527-linode-isp-yunnan.md "云南到Linode各机房的Ping测试 20180527")



本文最初发表于[云南到Vultr各机房的测速数据（20180527）](https://vps123.top/pingtest/20180527-vultr-isp-yunnan.html)
