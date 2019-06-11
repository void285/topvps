#  重庆到Vultr各机房的测速数据（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![重庆到Vultr各机房的测速数据（20180527）](/images/thumbnails/Chongqing_to_vultr.png)

本文的数据视角为 **重庆到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在重庆且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点216个，其中超时点13个。连通概况如下：大陆线路响应均值为273毫秒，最快的三个机房所在地为东京、硅谷、洛杉矶，最慢的三个为阿姆斯特丹、悉尼、伦敦；洛杉矶、巴黎、东京、硅谷、新加坡等11处有响应超时情况；新加坡、悉尼、东京、达拉斯、迈阿密等12处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 重庆图表数据

![大陆省份重庆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_isp_chongqing_vultr_20180527.png)

### 全部运营商

**重庆全部运营商到Vultr各机房的测速数据 [20180527]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 14个 | 1个 | 200ms | 14%  
硅谷 | 15个 | 1个 | 215ms | 11%  
洛杉矶 | 14个 | 2个 | 237ms | 4%  
西雅图 | 13个 | 0 | 241ms | 7%  
新加坡 | 14个 | 1个 | 259ms | 17%  
均值 | 216个 | 13个 | 273ms | 9%  
达拉斯 | 15个 | 0 | 277ms | 14%  
法兰克福 | 15个 | 1个 | 279ms | 4%  
迈阿密 | 15个 | 0 | 280ms | 13%  
芝加哥 | 14个 | 1个 | 289ms | 8%  
亚特兰大 | 15个 | 1个 | 292ms | 11%  
巴黎 | 14个 | 2个 | 293ms | 6%  
新泽西 | 15个 | 1个 | 302ms | 9%  
阿姆斯特丹 | 15个 | 1个 | 307ms | 1%  
悉尼 | 13个 | 1个 | 326ms | 14%  
伦敦 | 15个 | 0 | 334ms | 8%  
  
**简评：** 本表展示了重庆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻重庆，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**重庆电信到Vultr各机房的测速数据 [20180527]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 5个 | 1个 | 241ms | 17%  
硅谷 | 6个 | 1个 | 213ms | 3%  
洛杉矶 | 5个 | 1个 | 251ms | 8%  
西雅图 | 4个 | 0 | 283ms | 5%  
新加坡 | 5个 | 0 | 277ms | 12%  
均值 | 81个 | 8个 | 281ms | 8%  
达拉斯 | 6个 | 0 | 299ms | 19%  
法兰克福 | 6个 | 1个 | 247ms | 4%  
迈阿密 | 6个 | 0 | 279ms | 8%  
芝加哥 | 5个 | 0 | 309ms | 3%  
亚特兰大 | 6个 | 0 | 309ms | 18%  
巴黎 | 5个 | 1个 | 245ms | 0  
新泽西 | 6个 | 1个 | 358ms | 9%  
阿姆斯特丹 | 6个 | 1个 | 244ms | 0  
悉尼 | 4个 | 1个 | 354ms | 18%  
伦敦 | 6个 | 0 | 304ms | 4%  
  
**简评：** 如果你是来自重庆的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **硅谷、阿姆斯特丹、巴黎、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**重庆联通到Vultr各机房的测速数据 [20180527]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 5个 | 0 | 213ms | 20%  
硅谷 | 5个 | 0 | 219ms | 22%  
洛杉矶 | 5个 | 1个 | 245ms | 2%  
西雅图 | 5个 | 0 | 230ms | 15%  
新加坡 | 5个 | 1个 | 347ms | 33%  
均值 | 75个 | 5个 | 276ms | 13%  
达拉斯 | 5个 | 0 | 233ms | 3%  
法兰克福 | 5个 | 0 | 338ms | 7%  
迈阿密 | 5个 | 0 | 241ms | 21%  
芝加哥 | 5个 | 1个 | 292ms | 13%  
亚特兰大 | 5个 | 1个 | 270ms | 0  
巴黎 | 5个 | 1个 | 335ms | 13%  
新泽西 | 5个 | 0 | 265ms | 17%  
阿姆斯特丹 | 5个 | 0 | 359ms | 2%  
悉尼 | 5个 | 0 | 346ms | 21%  
伦敦 | 5个 | 0 | 330ms | 7%  
  
**简评：** 如果你是来自重庆的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **达拉斯、洛杉矶** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、硅谷、西雅图、迈阿密** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**重庆移动到Vultr各机房的测速数据 [20180527]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 4个 | 0 | 145ms | 5%  
硅谷 | 4个 | 0 | 215ms | 9%  
洛杉矶 | 4个 | 0 | 216ms | 1%  
西雅图 | 4个 | 0 | 208ms | 2%  
新加坡 | 4个 | 0 | 155ms | 5%  
均值 | 60个 | 0 | 262ms | 7%  
达拉斯 | 4个 | 0 | 301ms | 20%  
法兰克福 | 4个 | 0 | 253ms | 1%  
迈阿密 | 4个 | 0 | 321ms | 10%  
芝加哥 | 4个 | 0 | 267ms | 8%  
亚特兰大 | 4个 | 0 | 298ms | 15%  
巴黎 | 4个 | 0 | 301ms | 6%  
新泽西 | 4个 | 0 | 284ms | 1%  
阿姆斯特丹 | 4个 | 0 | 319ms | 3%  
悉尼 | 4个 | 0 | 278ms | 4%  
伦敦 | 4个 | 0 | 369ms | 13%  
  
**简评：** 如果你是来自重庆的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、西雅图、洛杉矶** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **硅谷** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [云南](/vultr/isp/yunnan/20180527-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180527")
    * [浙江](/vultr/isp/zhejiang/20180527-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180527")
  * 重庆到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/chongqing/20180514-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180514")
    * [20180622](/vultr/isp/chongqing/20180622-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/chongqing/20180804-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/chongqing/20180918-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180918")
  * 本期报告：重庆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/chongqing/20180527-bandwagon-isp-chongqing.md "重庆到BandwagonHost各机房的Ping测试 20180527")
    * [Digital Ocean](/digitalocean/isp/chongqing/20180527-digitalocean-isp-chongqing.md "重庆到Digital Ocean各机房的Ping测试 20180527")
    * [Linode](/linode/isp/chongqing/20180527-linode-isp-chongqing.md "重庆到Linode各机房的Ping测试 20180527")



本文最初发表于[重庆到Vultr各机房的测速数据（20180527）](https://vps123.top/pingtest/20180527-vultr-isp-chongqing.html)
