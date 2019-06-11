#  四川到Linode各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![四川到Linode各机房的测速数据（20180804）](/images/thumbnails/Sichuan_to_linode.png)

本文的数据视角为 **四川到[Linode](https://vps123.top/go/linode)的各机房**的PING响应值、丢包率的比较；若你在四川且打算运行[Linode](https://vps123.top/go/linode)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Linode的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点2270个，其中超时点5个。连通概况如下：大陆线路响应均值为269毫秒，最快的三个机房所在地为佛利蒙、东京、均值，最慢的三个为法兰克福、亚特兰大、伦敦；亚特兰大、东京有响应超时情况；东京、新加坡、伦敦丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 四川图表数据

![大陆省份四川到VPS提供商Linode各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_isp_sichuan_linode_20180804.png)

### 全部运营商

四川全部运营商到Linode各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
佛利蒙 | 285个 | 0 | 215ms | 2% | 纽瓦克 | 286个 | 0 | 286ms | 1%  
东京 | 282个 | 2个 | 216ms | 15% | 法兰克福 | 285个 | 0 | 288ms | 3%  
均值 | 2270个 | 5个 | 269ms | 6% | 亚特兰大 | 285个 | 3个 | 297ms | 4%  
达拉斯 | 289个 | 0 | 271ms | 1% | 伦敦 | 289个 | 0 | 300ms | 8%  
新加坡 | 269个 | 0 | 277ms | 12% |  |  |  |  |   
  
简评：本表展示了四川的 **电信、联通、移动** 线路到Linode各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻四川，可从此表了解你常用的网络到Linode各个机房的平均响应速度以及丢包率。从表中数据可以看到， **佛利蒙** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

四川电信到Linode各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
佛利蒙 | 149个 | 0 | 207ms | 2% | 纽瓦克 | 146个 | 0 | 269ms | 0  
东京 | 146个 | 2个 | 235ms | 22% | 法兰克福 | 149个 | 0 | 272ms | 2%  
均值 | 1182个 | 5个 | 262ms | 6% | 亚特兰大 | 149个 | 3个 | 283ms | 4%  
达拉斯 | 149个 | 0 | 241ms | 1% | 伦敦 | 149个 | 0 | 264ms | 2%  
新加坡 | 145个 | 0 | 332ms | 14% |  |  |  |  |   
  
简评：如果你是来自四川的 **电信** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **佛利蒙、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_1)吧！

### 联通

四川联通到Linode各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
佛利蒙 | 44个 | 0 | 217ms | 3% | 纽瓦克 | 48个 | 0 | 318ms | 4%  
东京 | 48个 | 0 | 276ms | 18% | 法兰克福 | 44个 | 0 | 365ms | 5%  
均值 | 372个 | 0 | 306ms | 7% | 亚特兰大 | 44个 | 0 | 319ms | 6%  
达拉斯 | 48个 | 0 | 316ms | 4% | 伦敦 | 48个 | 0 | 327ms | 1%  
新加坡 | 48个 | 0 | 306ms | 11% |  |  |  |  |   
  
简评：如果你是来自四川的 **联通** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **佛利蒙** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_2)吧！

### 移动

四川移动到Linode各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
佛利蒙 | 92个 | 0 | 221ms | 1% | 纽瓦克 | 92个 | 0 | 272ms | 0  
东京 | 88个 | 0 | 137ms | 5% | 法兰克福 | 92个 | 0 | 226ms | 2%  
均值 | 716个 | 0 | 239ms | 5% | 亚特兰大 | 92个 | 0 | 289ms | 1%  
达拉斯 | 92个 | 0 | 256ms | 0 | 伦敦 | 92个 | 0 | 310ms | 20%  
新加坡 | 76个 | 0 | 193ms | 10% |  |  |  |  |   
  
简评：如果你是来自四川的 **移动** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、佛利蒙、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **新加坡** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_3)吧！

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180804 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180804 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期 _其他省份_ 到Linode各机房的报告： 
    * [安徽](/linode/isp/anhui/20180804-linode-isp-anhui.md "安徽到Linode各机房的Ping测试 20180804")
    * [北京](/linode/isp/beijing/20180804-linode-isp-beijing.md "北京到Linode各机房的Ping测试 20180804")
    * [大陆](/linode/isp/china/20180804-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180804")
    * [重庆](/linode/isp/chongqing/20180804-linode-isp-chongqing.md "重庆到Linode各机房的Ping测试 20180804")
    * [福建](/linode/isp/fujian/20180804-linode-isp-fujian.md "福建到Linode各机房的Ping测试 20180804")
    * [甘肃](/linode/isp/gansu/20180804-linode-isp-gansu.md "甘肃到Linode各机房的Ping测试 20180804")
    * [广东](/linode/isp/guangdong/20180804-linode-isp-guangdong.md "广东到Linode各机房的Ping测试 20180804")
    * [广西](/linode/isp/guangxi/20180804-linode-isp-guangxi.md "广西到Linode各机房的Ping测试 20180804")
    * [贵州](/linode/isp/guizhou/20180804-linode-isp-guizhou.md "贵州到Linode各机房的Ping测试 20180804")
    * [海南](/linode/isp/hainan/20180804-linode-isp-hainan.md "海南到Linode各机房的Ping测试 20180804")
    * [河北](/linode/isp/hebei/20180804-linode-isp-hebei.md "河北到Linode各机房的Ping测试 20180804")
    * [黑龙江](/linode/isp/heilongjiang/20180804-linode-isp-heilongjiang.md "黑龙江到Linode各机房的Ping测试 20180804")
    * [河南](/linode/isp/henan/20180804-linode-isp-henan.md "河南到Linode各机房的Ping测试 20180804")
    * [湖北](/linode/isp/hubei/20180804-linode-isp-hubei.md "湖北到Linode各机房的Ping测试 20180804")
    * [湖南](/linode/isp/hunan/20180804-linode-isp-hunan.md "湖南到Linode各机房的Ping测试 20180804")
    * [内蒙古](/linode/isp/innermongolia/20180804-linode-isp-innermongolia.md "内蒙古到Linode各机房的Ping测试 20180804")
    * [江苏](/linode/isp/jiangsu/20180804-linode-isp-jiangsu.md "江苏到Linode各机房的Ping测试 20180804")
    * [江西](/linode/isp/jiangxi/20180804-linode-isp-jiangxi.md "江西到Linode各机房的Ping测试 20180804")
    * [吉林](/linode/isp/jilin/20180804-linode-isp-jilin.md "吉林到Linode各机房的Ping测试 20180804")
    * [辽宁](/linode/isp/liaoning/20180804-linode-isp-liaoning.md "辽宁到Linode各机房的Ping测试 20180804")
    * [宁夏](/linode/isp/ningxia/20180804-linode-isp-ningxia.md "宁夏到Linode各机房的Ping测试 20180804")
    * [青海](/linode/isp/qinghai/20180804-linode-isp-qinghai.md "青海到Linode各机房的Ping测试 20180804")
    * [山西](/linode/isp/shan1xi/20180804-linode-isp-shan1xi.md "山西到Linode各机房的Ping测试 20180804")
    * [陕西](/linode/isp/shan3xi/20180804-linode-isp-shan3xi.md "陕西到Linode各机房的Ping测试 20180804")
    * [山东](/linode/isp/shandong/20180804-linode-isp-shandong.md "山东到Linode各机房的Ping测试 20180804")
    * [上海](/linode/isp/shanghai/20180804-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180804")
    * [天津](/linode/isp/tianjin/20180804-linode-isp-tianjin.md "天津到Linode各机房的Ping测试 20180804")
    * [西藏](/linode/isp/tibet/20180804-linode-isp-tibet.md "西藏到Linode各机房的Ping测试 20180804")
    * [新疆](/linode/isp/xinjiang/20180804-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180804")
    * [云南](/linode/isp/yunnan/20180804-linode-isp-yunnan.md "云南到Linode各机房的Ping测试 20180804")
    * [浙江](/linode/isp/zhejiang/20180804-linode-isp-zhejiang.md "浙江到Linode各机房的Ping测试 20180804")
  * 四川到Linode各机房的 _其他近期报告_ ： 
    * [20180514](/linode/isp/sichuan/20180514-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180514")
    * [20180527](/linode/isp/sichuan/20180527-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180527")
    * [20180622](/linode/isp/sichuan/20180622-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180622")
    * [20180918](/linode/isp/sichuan/20180918-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180918")
  * 本期报告：四川到 _其他VPS提供商_ 各机房的测速报告： 
    * [Vultr](/vultr/isp/sichuan/20180804-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180804")
    * [BandwagonHost](/bandwagon/isp/sichuan/20180804-bandwagon-isp-sichuan.md "四川到BandwagonHost各机房的Ping测试 20180804")
    * [Digital Ocean](/digitalocean/isp/sichuan/20180804-digitalocean-isp-sichuan.md "四川到Digital Ocean各机房的Ping测试 20180804")



本文最初发表于[四川到Linode各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-linode-isp-sichuan.html)