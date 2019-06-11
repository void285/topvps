#  云南到Digital Ocean各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![云南到Digital Ocean各机房的测速数据（20180622）](/images/thumbnails/Yunnan_to_digitalocean.png)

本文的数据视角为 **云南到[Digital Ocean](https://vps123.top/go/do)的各机房**的PING响应值、丢包率的比较；若你在云南且打算运行[Digital Ocean](https://vps123.top/go/do)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Digital Ocean的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点231个，其中超时点94个。连通概况如下：大陆线路响应均值为299毫秒，最快的三个机房所在地为旧金山、新加坡、多伦多，最慢的三个为纽约、阿姆斯特丹、班加罗尔；纽约、旧金山、阿姆斯特丹、多伦多、伦敦等7处有响应超时情况；新加坡丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 云南图表数据

![大陆省份云南到VPS提供商Digital Ocean各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_isp_yunnan_do_20180622.png)

### 全部运营商

**云南全部运营商到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 44个 | 19个 | 253ms | 1%  
新加坡 | 2个 | 0 | 271ms | 33%  
多伦多 | 23个 | 10个 | 271ms | 0  
伦敦 | 21个 | 10个 | 275ms | 0  
法兰克福 | 23个 | 9个 | 291ms | 1%  
均值 | 231个 | 94个 | 299ms | 1%  
纽约 | 50个 | 21个 | 318ms | 0  
阿姆斯特丹 | 46个 | 17个 | 333ms | 1%  
班加罗尔 | 22个 | 8个 | 389ms | 1%  
  
**简评：** 本表展示了云南的 **电信、联通、移动** 线路到Digital Ocean各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻云南，可从此表了解你常用的网络到Digital Ocean各个机房的平均响应速度以及丢包率。从表中数据可以看到，各机房所在城市的响应值、丢包率都较高（TopVPS推荐选用响应值低于250ms，丢包率在5%%以内的机房），请慎重选择；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**云南电信到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 24个 | 8个 | 267ms | 2%  
新加坡 | 2个 | 0 | 271ms | 33%  
多伦多 | 13个 | 3个 | 267ms | 0  
伦敦 | 11个 | 3个 | 264ms | 0  
法兰克福 | 12个 | 2个 | 276ms | 1%  
均值 | 129个 | 32个 | 303ms | 2%  
纽约 | 28个 | 7个 | 310ms | 1%  
阿姆斯特丹 | 26个 | 6个 | 321ms | 0  
班加罗尔 | 13个 | 3个 | 408ms | 2%  
  
**简评：** 如果你是来自云南的 **电信** 用户，想运行Digital Ocean的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，很遗憾从本次测试来看，没有值得你关注的机房；请查看往期的测试，如果数据一直不乐观，你应考虑换用其他VPS提供商如[Vultr](https://vps123.top/go/vultr/_1)、[BandwagonHost](https://vps123.top/go/bandwagon/_2)、[Linode](https://vps123.top/go/linode/_3)等。

### 联通

**云南联通到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 6个 | 5个 | 228ms | 1%  
新加坡 | - | - | - | -  
多伦多 | 3个 | 3个 | - | -  
伦敦 | 3个 | 3个 | - | -  
法兰克福 | 3个 | 3个 | - | -  
均值 | 28个 | 26个 | 285ms | 1%  
纽约 | 5个 | 5个 | - | -  
阿姆斯特丹 | 6个 | 5个 | 343ms | 1%  
班加罗尔 | 2个 | 2个 | - | -  
  
**简评：** 如果你是来自云南的 **联通** 用户，想运行Digital Ocean的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **旧金山** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/do/_4)吧！

### 移动

**云南移动到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 14个 | 6个 | 264ms | 1%  
新加坡 | - | - | - | -  
多伦多 | 7个 | 4个 | 275ms | 0  
伦敦 | 7个 | 4个 | 286ms | 0  
法兰克福 | 8个 | 4个 | 306ms | 0  
均值 | 74个 | 36个 | 310ms | 0  
纽约 | 17个 | 9个 | 326ms | 0  
阿姆斯特丹 | 14个 | 6个 | 335ms | 1%  
班加罗尔 | 7个 | 3个 | 370ms | 1%  
  
**简评：** 如果你是来自云南的 **移动** 用户，想运行Digital Ocean的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，很遗憾从本次测试来看，没有值得你关注的机房；请查看往期的测试，如果数据一直不乐观，你应考虑换用其他VPS提供商如[Vultr](https://vps123.top/go/vultr/_5)、[BandwagonHost](https://vps123.top/go/bandwagon/_6)、[Linode](https://vps123.top/go/linode/_7)等。

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180622 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180622 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期 _其他省份_ 到Digital Ocean各机房的报告： 
    * [安徽](/digitalocean/isp/anhui/20180622-digitalocean-isp-anhui.md "安徽到Digital Ocean各机房的Ping测试 20180622")
    * [北京](/digitalocean/isp/beijing/20180622-digitalocean-isp-beijing.md "北京到Digital Ocean各机房的Ping测试 20180622")
    * [大陆](/digitalocean/isp/china/20180622-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180622")
    * [重庆](/digitalocean/isp/chongqing/20180622-digitalocean-isp-chongqing.md "重庆到Digital Ocean各机房的Ping测试 20180622")
    * [福建](/digitalocean/isp/fujian/20180622-digitalocean-isp-fujian.md "福建到Digital Ocean各机房的Ping测试 20180622")
    * [甘肃](/digitalocean/isp/gansu/20180622-digitalocean-isp-gansu.md "甘肃到Digital Ocean各机房的Ping测试 20180622")
    * [广东](/digitalocean/isp/guangdong/20180622-digitalocean-isp-guangdong.md "广东到Digital Ocean各机房的Ping测试 20180622")
    * [广西](/digitalocean/isp/guangxi/20180622-digitalocean-isp-guangxi.md "广西到Digital Ocean各机房的Ping测试 20180622")
    * [贵州](/digitalocean/isp/guizhou/20180622-digitalocean-isp-guizhou.md "贵州到Digital Ocean各机房的Ping测试 20180622")
    * [海南](/digitalocean/isp/hainan/20180622-digitalocean-isp-hainan.md "海南到Digital Ocean各机房的Ping测试 20180622")
    * [河北](/digitalocean/isp/hebei/20180622-digitalocean-isp-hebei.md "河北到Digital Ocean各机房的Ping测试 20180622")
    * [黑龙江](/digitalocean/isp/heilongjiang/20180622-digitalocean-isp-heilongjiang.md "黑龙江到Digital Ocean各机房的Ping测试 20180622")
    * [河南](/digitalocean/isp/henan/20180622-digitalocean-isp-henan.md "河南到Digital Ocean各机房的Ping测试 20180622")
    * [湖北](/digitalocean/isp/hubei/20180622-digitalocean-isp-hubei.md "湖北到Digital Ocean各机房的Ping测试 20180622")
    * [湖南](/digitalocean/isp/hunan/20180622-digitalocean-isp-hunan.md "湖南到Digital Ocean各机房的Ping测试 20180622")
    * [内蒙古](/digitalocean/isp/innermongolia/20180622-digitalocean-isp-innermongolia.md "内蒙古到Digital Ocean各机房的Ping测试 20180622")
    * [江苏](/digitalocean/isp/jiangsu/20180622-digitalocean-isp-jiangsu.md "江苏到Digital Ocean各机房的Ping测试 20180622")
    * [江西](/digitalocean/isp/jiangxi/20180622-digitalocean-isp-jiangxi.md "江西到Digital Ocean各机房的Ping测试 20180622")
    * [吉林](/digitalocean/isp/jilin/20180622-digitalocean-isp-jilin.md "吉林到Digital Ocean各机房的Ping测试 20180622")
    * [辽宁](/digitalocean/isp/liaoning/20180622-digitalocean-isp-liaoning.md "辽宁到Digital Ocean各机房的Ping测试 20180622")
    * [宁夏](/digitalocean/isp/ningxia/20180622-digitalocean-isp-ningxia.md "宁夏到Digital Ocean各机房的Ping测试 20180622")
    * [青海](/digitalocean/isp/qinghai/20180622-digitalocean-isp-qinghai.md "青海到Digital Ocean各机房的Ping测试 20180622")
    * [山西](/digitalocean/isp/shan1xi/20180622-digitalocean-isp-shan1xi.md "山西到Digital Ocean各机房的Ping测试 20180622")
    * [陕西](/digitalocean/isp/shan3xi/20180622-digitalocean-isp-shan3xi.md "陕西到Digital Ocean各机房的Ping测试 20180622")
    * [山东](/digitalocean/isp/shandong/20180622-digitalocean-isp-shandong.md "山东到Digital Ocean各机房的Ping测试 20180622")
    * [上海](/digitalocean/isp/shanghai/20180622-digitalocean-isp-shanghai.md "上海到Digital Ocean各机房的Ping测试 20180622")
    * [四川](/digitalocean/isp/sichuan/20180622-digitalocean-isp-sichuan.md "四川到Digital Ocean各机房的Ping测试 20180622")
    * [天津](/digitalocean/isp/tianjin/20180622-digitalocean-isp-tianjin.md "天津到Digital Ocean各机房的Ping测试 20180622")
    * [西藏](/digitalocean/isp/tibet/20180622-digitalocean-isp-tibet.md "西藏到Digital Ocean各机房的Ping测试 20180622")
    * [新疆](/digitalocean/isp/xinjiang/20180622-digitalocean-isp-xinjiang.md "新疆到Digital Ocean各机房的Ping测试 20180622")
    * [浙江](/digitalocean/isp/zhejiang/20180622-digitalocean-isp-zhejiang.md "浙江到Digital Ocean各机房的Ping测试 20180622")
  * 云南到Digital Ocean各机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/isp/yunnan/20180514-digitalocean-isp-yunnan.md "云南到Digital Ocean各机房的Ping测试 20180514")
    * [20180527](/digitalocean/isp/yunnan/20180527-digitalocean-isp-yunnan.md "云南到Digital Ocean各机房的Ping测试 20180527")
    * [20180804](/digitalocean/isp/yunnan/20180804-digitalocean-isp-yunnan.md "云南到Digital Ocean各机房的Ping测试 20180804")
    * [20180918](/digitalocean/isp/yunnan/20180918-digitalocean-isp-yunnan.md "云南到Digital Ocean各机房的Ping测试 20180918")
  * 本期报告：云南到 _其他VPS提供商_ 各机房的测速报告： 
    * [Vultr](/vultr/isp/yunnan/20180622-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180622")
    * [BandwagonHost](/bandwagon/isp/yunnan/20180622-bandwagon-isp-yunnan.md "云南到BandwagonHost各机房的Ping测试 20180622")
    * [Linode](/linode/isp/yunnan/20180622-linode-isp-yunnan.md "云南到Linode各机房的Ping测试 20180622")



本文最初发表于[云南到Digital Ocean各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-digitalocean-isp-yunnan.html)
