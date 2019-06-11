#  甘肃到Vultr各机房的测速数据（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![甘肃到Vultr各机房的测速数据（20180426）](/images/thumbnails/Gansu_to_vultr.png)

本文的数据视角为 **甘肃到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在甘肃且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426甘肃到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点307个，其中超时点4个。连通概况如下：大陆线路响应均值为275毫秒，最快的三个机房所在地为东京、新加坡、洛杉矶，最慢的三个为迈阿密、阿姆斯特丹、伦敦；洛杉矶、硅谷、芝加哥、伦敦有响应超时情况；东京、达拉斯丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 甘肃图表数据

![大陆省份甘肃到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_isp_gansu_vultr_20180426.png)

### 全部运营商

**甘肃全部运营商到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 21个 | 0 | 168ms | 7%  
新加坡 | 20个 | 0 | 218ms | 4%  
洛杉矶 | 21个 | 1个 | 227ms | 1%  
硅谷 | 21个 | 1个 | 240ms | 1%  
悉尼 | 21个 | 0 | 242ms | 1%  
西雅图 | 20个 | 0 | 251ms | 2%  
巴黎 | 20个 | 0 | 275ms | 0  
均值 | 307个 | 4个 | 275ms | 2%  
法兰克福 | 20个 | 0 | 286ms | 0  
达拉斯 | 21个 | 0 | 294ms | 5%  
芝加哥 | 21个 | 1个 | 307ms | 2%  
亚特兰大 | 21个 | 0 | 307ms | 4%  
新泽西 | 20个 | 0 | 313ms | 1%  
迈阿密 | 20个 | 0 | 319ms | 3%  
阿姆斯特丹 | 20个 | 0 | 328ms | 0  
伦敦 | 20个 | 1个 | 352ms | 2%  
  
**简评：** 本表展示了甘肃的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻甘肃，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **新加坡、洛杉矶、硅谷、悉尼** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**甘肃电信到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 12个 | 0 | 219ms | 20%  
新加坡 | 12个 | 0 | 208ms | 10%  
洛杉矶 | 12个 | 1个 | 265ms | 4%  
硅谷 | 12个 | 1个 | 271ms | 4%  
悉尼 | 12个 | 0 | 275ms | 1%  
西雅图 | 11个 | 0 | 296ms | 6%  
巴黎 | 12个 | 0 | 244ms | 0  
均值 | 177个 | 4个 | 292ms | 4%  
法兰克福 | 12个 | 0 | 253ms | 1%  
达拉斯 | 12个 | 0 | 309ms | 6%  
芝加哥 | 12个 | 1个 | 405ms | 5%  
亚特兰大 | 12个 | 0 | 305ms | 3%  
新泽西 | 11个 | 0 | 360ms | 3%  
迈阿密 | 11个 | 0 | 364ms | 4%  
阿姆斯特丹 | 12个 | 0 | 276ms | 0  
伦敦 | 12个 | 1个 | 360ms | 1%  
  
**简评：** 如果你是来自甘肃的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **巴黎** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **新加坡、东京** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**甘肃联通到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 1个 | 0 | 153ms | 0  
新加坡 | 1个 | 0 | 285ms | 0  
洛杉矶 | 1个 | 0 | 188ms | 0  
硅谷 | 1个 | 0 | 208ms | 0  
悉尼 | 1个 | 0 | 218ms | 0  
西雅图 | 1个 | 0 | 221ms | 0  
巴黎 | 1个 | 0 | 329ms | 0  
均值 | 15个 | 0 | 259ms | 0  
法兰克福 | 1个 | 0 | 356ms | 0  
达拉斯 | 1个 | 0 | 218ms | 0  
芝加哥 | 1个 | 0 | 233ms | 0  
亚特兰大 | 1个 | 0 | 238ms | 1%  
新泽西 | 1个 | 0 | 284ms | 0  
迈阿密 | 1个 | 0 | 264ms | 0  
阿姆斯特丹 | 1个 | 0 | 360ms | 1%  
伦敦 | 1个 | 0 | 340ms | 2%  
  
**简评：** 如果你是来自甘肃的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、洛杉矶、硅谷、悉尼、达拉斯、西雅图、芝加哥、亚特兰大** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**甘肃移动到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 8个 | 0 | 133ms | 1%  
新加坡 | 7个 | 0 | 160ms | 1%  
洛杉矶 | 8个 | 0 | 230ms | 0  
硅谷 | 8个 | 0 | 242ms | 1%  
悉尼 | 8个 | 0 | 233ms | 2%  
西雅图 | 8个 | 0 | 238ms | 0  
巴黎 | 7个 | 0 | 252ms | 0  
均值 | 115个 | 0 | 272ms | 2%  
法兰克福 | 7个 | 0 | 250ms | 0  
达拉斯 | 8个 | 0 | 356ms | 9%  
芝加哥 | 8个 | 0 | 284ms | 1%  
亚特兰大 | 8个 | 0 | 380ms | 8%  
新泽西 | 8个 | 0 | 295ms | 0  
迈阿密 | 8个 | 0 | 329ms | 5%  
阿姆斯特丹 | 7个 | 0 | 348ms | 0  
伦敦 | 7个 | 0 | 357ms | 4%  
  
**简评：** 如果你是来自甘肃的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、洛杉矶、悉尼、西雅图、硅谷、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [吉林](/vultr/isp/jilin/20180426-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180426")
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
  * 甘肃到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/gansu/20180514-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/gansu/20180527-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/gansu/20180622-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/gansu/20180804-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/gansu/20180918-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180918")
  * 本期报告：甘肃到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/gansu/20180426-bandwagon-isp-gansu.md "甘肃到BandwagonHost各机房的Ping测试 20180426")
    * [Digital Ocean](/digitalocean/isp/gansu/20180426-digitalocean-isp-gansu.md "甘肃到Digital Ocean各机房的Ping测试 20180426")
    * [Linode](/linode/isp/gansu/20180426-linode-isp-gansu.md "甘肃到Linode各机房的Ping测试 20180426")



本文最初发表于[甘肃到Vultr各机房的测速数据（20180426）](https://vps123.top/pingtest/20180426-vultr-isp-gansu.html)
