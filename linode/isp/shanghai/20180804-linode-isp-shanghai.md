#  上海到Linode各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![上海到Linode各机房的测速数据（20180804）](/images/thumbnails/Shanghai_to_linode.png)

本文的数据视角为 **上海到[Linode](https://vps123.top/go/linode)的各机房**的PING响应值、丢包率的比较；若你在上海且打算运行[Linode](https://vps123.top/go/linode)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Linode的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点227个，其中超时点37个。连通概况如下：大陆线路响应均值为259毫秒，最快的三个机房所在地为东京、佛利蒙、伦敦，最慢的三个为纽瓦克、新加坡、亚特兰大；法兰克福、东京、佛利蒙、伦敦、达拉斯等8处有响应超时情况；新加坡、东京、达拉斯、亚特兰大丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 上海图表数据

![大陆省份上海到VPS提供商Linode各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/linode_20180804/plot_isp_shanghai_linode_20180804.png)

### 全部运营商

上海全部运营商到Linode各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 26个 | 6个 | 155ms | 24% | 法兰克福 | 31个 | 7个 | 276ms | 2%  
佛利蒙 | 27个 | 4个 | 220ms | 0 | 纽瓦克 | 30个 | 4个 | 279ms | 0  
伦敦 | 27个 | 4个 | 239ms | 0 | 新加坡 | 27个 | 4个 | 285ms | 28%  
均值 | 227个 | 37个 | 259ms | 6% | 亚特兰大 | 31个 | 4个 | 292ms | 5%  
达拉斯 | 28个 | 4个 | 266ms | 7% |  |  |  |  |   
  
简评：本表展示了上海的 **电信、联通、移动** 线路到Linode各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻上海，可从此表了解你常用的网络到Linode各个机房的平均响应速度以及丢包率。从表中数据可以看到， **佛利蒙、伦敦** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

上海电信到Linode各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 18个 | 6个 | 226ms | 48% | 法兰克福 | 19个 | 7个 | 273ms | 3%  
佛利蒙 | 19个 | 4个 | 166ms | 0 | 纽瓦克 | 18个 | 4个 | 288ms | 1%  
伦敦 | 19个 | 4个 | 257ms | 0 | 新加坡 | 19个 | 4个 | 285ms | 49%  
均值 | 147个 | 37个 | 265ms | 16% | 亚特兰大 | 19个 | 4个 | 335ms | 17%  
达拉斯 | 16个 | 4个 | 297ms | 15% |  |  |  |  |   
  
简评：如果你是来自上海的 **电信** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **佛利蒙** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_1)吧！

### 联通

上海联通到Linode各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | - | - | - | - | 法兰克福 | 4个 | 0 | 275ms | 3%  
佛利蒙 | - | - | - | - | 纽瓦克 | 4个 | 0 | 292ms | 0  
伦敦 | - | - | - | - | 新加坡 | - | - | - | -  
均值 | 16个 | 0 | 274ms | 2% | 亚特兰大 | 4个 | 0 | 277ms | 0  
达拉斯 | 4个 | 0 | 253ms | 6% |  |  |  |  |   
  
简评：如果你是来自上海的 **联通** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，很遗憾从本次测试来看，没有值得你关注的机房；请查看往期的测试，如果数据一直不乐观，你应考虑换用其他VPS提供商如[Vultr](https://vps123.top/go/vultr/_2)、[BandwagonHost](https://vps123.top/go/bandwagon/_3)、[Digital Ocean](https://vps123.top/go/digitalocean/_4)等。

### 移动

上海移动到Linode各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 8个 | 0 | 84ms | 0 | 法兰克福 | 8个 | 0 | 281ms | 0  
佛利蒙 | 8个 | 0 | 275ms | 0 | 纽瓦克 | 8个 | 0 | 256ms | 0  
伦敦 | 8个 | 0 | 221ms | 0 | 新加坡 | 8个 | 0 | 286ms | 7%  
均值 | 64个 | 0 | 239ms | 0 | 亚特兰大 | 8个 | 0 | 265ms | 0  
达拉斯 | 8个 | 0 | 249ms | 0 |  |  |  |  |   
  
简评：如果你是来自上海的 **移动** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、伦敦、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_5)吧！

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
    * [四川](/linode/isp/sichuan/20180804-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180804")
    * [天津](/linode/isp/tianjin/20180804-linode-isp-tianjin.md "天津到Linode各机房的Ping测试 20180804")
    * [西藏](/linode/isp/tibet/20180804-linode-isp-tibet.md "西藏到Linode各机房的Ping测试 20180804")
    * [新疆](/linode/isp/xinjiang/20180804-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180804")
    * [云南](/linode/isp/yunnan/20180804-linode-isp-yunnan.md "云南到Linode各机房的Ping测试 20180804")
    * [浙江](/linode/isp/zhejiang/20180804-linode-isp-zhejiang.md "浙江到Linode各机房的Ping测试 20180804")
  * 上海到Linode各机房的 _其他近期报告_ ： 
    * [20180514](/linode/isp/shanghai/20180514-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180514")
    * [20180527](/linode/isp/shanghai/20180527-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180527")
    * [20180622](/linode/isp/shanghai/20180622-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180622")
    * [20180918](/linode/isp/shanghai/20180918-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180918")
  * 本期报告：上海到 _其他VPS提供商_ 各机房的测速报告： 
    * [Vultr](/vultr/isp/shanghai/20180804-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180804")
    * [BandwagonHost](/bandwagon/isp/shanghai/20180804-bandwagon-isp-shanghai.md "上海到BandwagonHost各机房的Ping测试 20180804")
    * [Digital Ocean](/digitalocean/isp/shanghai/20180804-digitalocean-isp-shanghai.md "上海到Digital Ocean各机房的Ping测试 20180804")



本文最初发表于[上海到Linode各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-linode-isp-shanghai.html)
