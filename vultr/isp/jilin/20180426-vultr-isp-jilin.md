#  吉林到Vultr各机房的测速数据（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![吉林到Vultr各机房的测速数据（20180426）](/images/thumbnails/Jilin_to_vultr.png)

本文的数据视角为 **吉林到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在吉林且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426吉林到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点203个，其中超时点1个。连通概况如下：大陆线路响应均值为265毫秒，最快的三个机房所在地为东京、洛杉矶、硅谷，最慢的三个为迈阿密、阿姆斯特丹、伦敦；新泽西有响应超时情况；东京丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 吉林图表数据

![大陆省份吉林到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_isp_jilin_vultr_20180426.png)

### 全部运营商

**吉林全部运营商到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 12个 | 0 | 163ms | 15%  
洛杉矶 | 14个 | 0 | 207ms | 2%  
硅谷 | 14个 | 0 | 219ms | 0  
新加坡 | 15个 | 0 | 223ms | 3%  
悉尼 | 14个 | 0 | 225ms | 0  
西雅图 | 13个 | 0 | 234ms | 1%  
达拉斯 | 14个 | 0 | 242ms | 3%  
均值 | 203个 | 1个 | 265ms | 2%  
亚特兰大 | 14个 | 0 | 267ms | 2%  
芝加哥 | 12个 | 0 | 299ms | 4%  
法兰克福 | 13个 | 0 | 304ms | 0  
新泽西 | 12个 | 1个 | 306ms | 1%  
巴黎 | 15个 | 0 | 308ms | 0  
迈阿密 | 12个 | 0 | 308ms | 2%  
阿姆斯特丹 | 15个 | 0 | 321ms | 0  
伦敦 | 14个 | 0 | 350ms | 1%  
  
**简评：** 本表展示了吉林的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻吉林，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶、硅谷、新加坡、悉尼、西雅图、达拉斯** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**吉林电信到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 5个 | 0 | 211ms | 14%  
洛杉矶 | 5个 | 0 | 252ms | 6%  
硅谷 | 5个 | 0 | 264ms | 2%  
新加坡 | 5个 | 0 | 206ms | 9%  
悉尼 | 5个 | 0 | 274ms | 0  
西雅图 | 4个 | 0 | 274ms | 4%  
达拉斯 | 5个 | 0 | 248ms | 4%  
均值 | 71个 | 1个 | 283ms | 4%  
亚特兰大 | 5个 | 0 | 291ms | 1%  
芝加哥 | 4个 | 0 | 407ms | 11%  
法兰克福 | 4个 | 0 | 231ms | 0  
新泽西 | 6个 | 1个 | 388ms | 3%  
巴黎 | 5个 | 0 | 246ms | 0  
迈阿密 | 4个 | 0 | 397ms | 7%  
阿姆斯特丹 | 5个 | 0 | 260ms | 0  
伦敦 | 4个 | 0 | 352ms | 1%  
  
**简评：** 如果你是来自吉林的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **法兰克福、巴黎、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **新加坡、东京** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**吉林联通到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 5个 | 0 | 148ms | 22%  
洛杉矶 | 7个 | 0 | 172ms | 0  
硅谷 | 7个 | 0 | 184ms | 0  
新加坡 | 8个 | 0 | 263ms | 0  
悉尼 | 7个 | 0 | 197ms | 0  
西雅图 | 7个 | 0 | 206ms | 0  
达拉斯 | 7个 | 0 | 200ms | 0  
均值 | 103个 | 0 | 256ms | 1%  
亚特兰大 | 7个 | 0 | 224ms | 0  
芝加哥 | 6个 | 0 | 243ms | 0  
法兰克福 | 7个 | 0 | 370ms | 0  
新泽西 | 4个 | 0 | 254ms | 0  
巴黎 | 8个 | 0 | 370ms | 0  
迈阿密 | 7个 | 0 | 241ms | 0  
阿姆斯特丹 | 8个 | 0 | 353ms | 0  
伦敦 | 8个 | 0 | 340ms | 0  
  
**简评：** 如果你是来自吉林的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、硅谷、悉尼、达拉斯、西雅图、亚特兰大、迈阿密、芝加哥** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**吉林移动到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 2个 | 0 | 129ms | 10%  
洛杉矶 | 2个 | 0 | 196ms | 0  
硅谷 | 2个 | 0 | 208ms | 0  
新加坡 | 2个 | 0 | 199ms | 0  
悉尼 | 2个 | 0 | 206ms | 0  
西雅图 | 2个 | 0 | 222ms | 0  
达拉斯 | 2个 | 0 | 278ms | 5%  
均值 | 29个 | 0 | 257ms | 1%  
亚特兰大 | 2个 | 0 | 288ms | 5%  
芝加哥 | 2个 | 0 | 248ms | 0  
法兰克福 | 2个 | 0 | 311ms | 0  
新泽西 | 2个 | 0 | 275ms | 0  
巴黎 | 2个 | 0 | 310ms | 0  
迈阿密 | 1个 | 0 | 288ms | 0  
阿姆斯特丹 | 2个 | 0 | 352ms | 0  
伦敦 | 2个 | 0 | 359ms | 1%  
  
**简评：** 如果你是来自吉林的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、新加坡、悉尼、硅谷、西雅图、芝加哥** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180426 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180426 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180426-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180426")
    * [北京](/vultr/isp/beijing/20180426-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180426")
    * [大陆](/vultr/isp/china/20180426-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180426")
    * [重庆](/vultr/isp/chongqing/20180426-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180426")
    * [福建](/vultr/isp/fujian/20180426-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180426")
    * [甘肃](/vultr/isp/gansu/20180426-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180426")
    * [广东](/vultr/isp/guangdong/20180426-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180426")
    * [广西](/vultr/isp/guangxi/20180426-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180426")
    * [贵州](/vultr/isp/guizhou/20180426-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180426")
    * [海南](/vultr/isp/hainan/20180426-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180426")
    * [河北](/vultr/isp/hebei/20180426-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180426")
    * [黑龙江](/vultr/isp/heilongjiang/20180426-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180426")
    * [河南](/vultr/isp/henan/20180426-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180426")
    * [湖北](/vultr/isp/hubei/20180426-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180426")
    * [湖南](/vultr/isp/hunan/20180426-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180426")
    * [内蒙古](/vultr/isp/innermongolia/20180426-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180426")
    * [江苏](/vultr/isp/jiangsu/20180426-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180426")
    * [江西](/vultr/isp/jiangxi/20180426-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180426")
    * [辽宁](/vultr/isp/liaoning/20180426-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180426")
    * [宁夏](/vultr/isp/ningxia/20180426-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180426")
    * [青海](/vultr/isp/qinghai/20180426-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180426")
    * [山西](/vultr/isp/shan1xi/20180426-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180426")
    * [陕西](/vultr/isp/shan3xi/20180426-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180426")
    * [山东](/vultr/isp/shandong/20180426-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180426")
    * [上海](/vultr/isp/shanghai/20180426-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180426")
    * [四川](/vultr/isp/sichuan/20180426-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180426")
    * [天津](/vultr/isp/tianjin/20180426-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180426")
    * [西藏](/vultr/isp/tibet/20180426-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180426")
    * [新疆](/vultr/isp/xinjiang/20180426-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180426")
    * [云南](/vultr/isp/yunnan/20180426-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180426")
    * [浙江](/vultr/isp/zhejiang/20180426-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180426")
  * 吉林到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/jilin/20180514-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/jilin/20180527-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/jilin/20180622-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/jilin/20180804-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/jilin/20180918-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180918")
  * 本期报告：吉林到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/jilin/20180426-bandwagon-isp-jilin.md "吉林到BandwagonHost各机房的Ping测试 20180426")
    * [Digital Ocean](/digitalocean/isp/jilin/20180426-digitalocean-isp-jilin.md "吉林到Digital Ocean各机房的Ping测试 20180426")
    * [Linode](/linode/isp/jilin/20180426-linode-isp-jilin.md "吉林到Linode各机房的Ping测试 20180426")



本文最初发表于[吉林到Vultr各机房的测速数据（20180426）](https://vps123.top/pingtest/20180426-vultr-isp-jilin.html)
