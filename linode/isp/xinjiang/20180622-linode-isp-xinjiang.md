#  新疆到Linode各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![新疆到Linode各机房的测速数据（20180622）](/images/thumbnails/Xinjiang_to_linode.png)

本文的数据视角为 **新疆到[Linode](https://vps123.top/go/linode)的各机房**的PING响应值、丢包率的比较；若你在新疆且打算运行[Linode](https://vps123.top/go/linode)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Linode的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点163个，其中超时点2个。连通概况如下：大陆线路响应均值为302毫秒，最快的三个机房所在地为东京、佛利蒙、均值，最慢的三个为新加坡、纽瓦克、法兰克福；东京、新加坡有响应超时情况；新加坡、东京丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 新疆图表数据

![大陆省份新疆到VPS提供商Linode各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_isp_xinjiang_linode_20180622.png)

### 全部运营商

**新疆全部运营商到Linode各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 24个 | 1个 | 223ms | 8%  
佛利蒙 | 21个 | 0 | 242ms | 2%  
均值 | 163个 | 2个 | 302ms | 4%  
亚特兰大 | 18个 | 0 | 309ms | 4%  
达拉斯 | 23个 | 0 | 315ms | 2%  
伦敦 | 20个 | 0 | 316ms | 1%  
新加坡 | 18个 | 1个 | 318ms | 13%  
纽瓦克 | 20个 | 0 | 330ms | 3%  
法兰克福 | 19个 | 0 | 365ms | 4%  
  
**简评：** 本表展示了新疆的 **电信、联通、移动** 线路到Linode各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻新疆，可从此表了解你常用的网络到Linode各个机房的平均响应速度以及丢包率。从表中数据可以看到， **佛利蒙** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**新疆电信到Linode各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 12个 | 1个 | 278ms | 21%  
佛利蒙 | 11个 | 0 | 236ms | 0  
均值 | 83个 | 2个 | 326ms | 8%  
亚特兰大 | 9个 | 0 | 328ms | 7%  
达拉斯 | 11个 | 0 | 296ms | 0  
伦敦 | 10个 | 0 | 274ms | 1%  
新加坡 | 9个 | 1个 | 419ms | 23%  
纽瓦克 | 11个 | 0 | 380ms | 4%  
法兰克福 | 10个 | 0 | 410ms | 13%  
  
**简评：** 如果你是来自新疆的 **电信** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **佛利蒙** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_1)吧！

### 联通

**新疆联通到Linode各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 2个 | 0 | 226ms | 2%  
佛利蒙 | 2个 | 0 | 237ms | 0  
均值 | 20个 | 0 | 312ms | 3%  
亚特兰大 | 3个 | 0 | 272ms | 1%  
达拉斯 | 2个 | 0 | 340ms | 2%  
伦敦 | 2个 | 0 | 364ms | 2%  
新加坡 | 3个 | 0 | 333ms | 14%  
纽瓦克 | 3个 | 0 | 301ms | 0  
法兰克福 | 3个 | 0 | 395ms | 0  
  
**简评：** 如果你是来自新疆的 **联通** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、佛利蒙** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_2)吧！

### 移动

**新疆移动到Linode各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 10个 | 0 | 166ms | 1%  
佛利蒙 | 8个 | 0 | 255ms | 5%  
均值 | 60个 | 0 | 267ms | 2%  
亚特兰大 | 6个 | 0 | 328ms | 4%  
达拉斯 | 10个 | 0 | 309ms | 4%  
伦敦 | 8个 | 0 | 309ms | 0  
新加坡 | 6个 | 0 | 202ms | 1%  
纽瓦克 | 6个 | 0 | 308ms | 4%  
法兰克福 | 6个 | 0 | 291ms | 0  
  
**简评：** 如果你是来自新疆的 **移动** 用户，想运行Linode的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_3)吧！

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180622 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180622 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期 _其他省份_ 到Linode各机房的报告： 
    * [安徽](/linode/isp/anhui/20180622-linode-isp-anhui.md "安徽到Linode各机房的Ping测试 20180622")
    * [北京](/linode/isp/beijing/20180622-linode-isp-beijing.md "北京到Linode各机房的Ping测试 20180622")
    * [大陆](/linode/isp/china/20180622-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180622")
    * [重庆](/linode/isp/chongqing/20180622-linode-isp-chongqing.md "重庆到Linode各机房的Ping测试 20180622")
    * [福建](/linode/isp/fujian/20180622-linode-isp-fujian.md "福建到Linode各机房的Ping测试 20180622")
    * [甘肃](/linode/isp/gansu/20180622-linode-isp-gansu.md "甘肃到Linode各机房的Ping测试 20180622")
    * [广东](/linode/isp/guangdong/20180622-linode-isp-guangdong.md "广东到Linode各机房的Ping测试 20180622")
    * [广西](/linode/isp/guangxi/20180622-linode-isp-guangxi.md "广西到Linode各机房的Ping测试 20180622")
    * [贵州](/linode/isp/guizhou/20180622-linode-isp-guizhou.md "贵州到Linode各机房的Ping测试 20180622")
    * [海南](/linode/isp/hainan/20180622-linode-isp-hainan.md "海南到Linode各机房的Ping测试 20180622")
    * [河北](/linode/isp/hebei/20180622-linode-isp-hebei.md "河北到Linode各机房的Ping测试 20180622")
    * [黑龙江](/linode/isp/heilongjiang/20180622-linode-isp-heilongjiang.md "黑龙江到Linode各机房的Ping测试 20180622")
    * [河南](/linode/isp/henan/20180622-linode-isp-henan.md "河南到Linode各机房的Ping测试 20180622")
    * [湖北](/linode/isp/hubei/20180622-linode-isp-hubei.md "湖北到Linode各机房的Ping测试 20180622")
    * [湖南](/linode/isp/hunan/20180622-linode-isp-hunan.md "湖南到Linode各机房的Ping测试 20180622")
    * [内蒙古](/linode/isp/innermongolia/20180622-linode-isp-innermongolia.md "内蒙古到Linode各机房的Ping测试 20180622")
    * [江苏](/linode/isp/jiangsu/20180622-linode-isp-jiangsu.md "江苏到Linode各机房的Ping测试 20180622")
    * [江西](/linode/isp/jiangxi/20180622-linode-isp-jiangxi.md "江西到Linode各机房的Ping测试 20180622")
    * [吉林](/linode/isp/jilin/20180622-linode-isp-jilin.md "吉林到Linode各机房的Ping测试 20180622")
    * [辽宁](/linode/isp/liaoning/20180622-linode-isp-liaoning.md "辽宁到Linode各机房的Ping测试 20180622")
    * [宁夏](/linode/isp/ningxia/20180622-linode-isp-ningxia.md "宁夏到Linode各机房的Ping测试 20180622")
    * [青海](/linode/isp/qinghai/20180622-linode-isp-qinghai.md "青海到Linode各机房的Ping测试 20180622")
    * [山西](/linode/isp/shan1xi/20180622-linode-isp-shan1xi.md "山西到Linode各机房的Ping测试 20180622")
    * [陕西](/linode/isp/shan3xi/20180622-linode-isp-shan3xi.md "陕西到Linode各机房的Ping测试 20180622")
    * [山东](/linode/isp/shandong/20180622-linode-isp-shandong.md "山东到Linode各机房的Ping测试 20180622")
    * [上海](/linode/isp/shanghai/20180622-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180622")
    * [四川](/linode/isp/sichuan/20180622-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180622")
    * [天津](/linode/isp/tianjin/20180622-linode-isp-tianjin.md "天津到Linode各机房的Ping测试 20180622")
    * [云南](/linode/isp/yunnan/20180622-linode-isp-yunnan.md "云南到Linode各机房的Ping测试 20180622")
    * [浙江](/linode/isp/zhejiang/20180622-linode-isp-zhejiang.md "浙江到Linode各机房的Ping测试 20180622")
  * 新疆到Linode各机房的 _其他近期报告_ ： 
    * [20180514](/linode/isp/xinjiang/20180514-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180514")
    * [20180527](/linode/isp/xinjiang/20180527-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180527")
    * [20180804](/linode/isp/xinjiang/20180804-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180804")
    * [20180918](/linode/isp/xinjiang/20180918-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180918")
  * 本期报告：新疆到 _其他VPS提供商_ 各机房的测速报告： 
    * [Vultr](/vultr/isp/xinjiang/20180622-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180622")
    * [BandwagonHost](/bandwagon/isp/xinjiang/20180622-bandwagon-isp-xinjiang.md "新疆到BandwagonHost各机房的Ping测试 20180622")
    * [Digital Ocean](/digitalocean/isp/xinjiang/20180622-digitalocean-isp-xinjiang.md "新疆到Digital Ocean各机房的Ping测试 20180622")



本文最初发表于[新疆到Linode各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-linode-isp-xinjiang.html)
