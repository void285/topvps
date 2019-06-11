#  广西到Vultr各机房的测速数据（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![广西到Vultr各机房的测速数据（20180426）](/images/thumbnails/Guangxi_to_vultr.png)

本文的数据视角为 **广西到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在广西且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426广西到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点457个，其中超时点1个。连通概况如下：大陆线路响应均值为262毫秒，最快的三个机房所在地为东京、新加坡、洛杉矶，最慢的三个为新泽西、迈阿密、伦敦；硅谷有响应超时情况；东京、新加坡、亚特兰大、达拉斯、迈阿密等6处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 广西图表数据

![大陆省份广西到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/vultr_20180426/plot_isp_guangxi_vultr_20180426.png)

### 全部运营商

**广西全部运营商到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 29个 | 0 | 161ms | 13%  
新加坡 | 35个 | 0 | 173ms | 7%  
洛杉矶 | 27个 | 0 | 197ms | 2%  
硅谷 | 27个 | 1个 | 213ms | 4%  
西雅图 | 26个 | 0 | 228ms | 4%  
悉尼 | 29个 | 0 | 233ms | 2%  
均值 | 457个 | 1个 | 262ms | 5%  
达拉斯 | 27个 | 0 | 266ms | 6%  
巴黎 | 35个 | 0 | 285ms | 3%  
法兰克福 | 35个 | 0 | 289ms | 5%  
芝加哥 | 29个 | 0 | 294ms | 2%  
亚特兰大 | 29个 | 0 | 299ms | 7%  
阿姆斯特丹 | 35个 | 0 | 305ms | 4%  
新泽西 | 31个 | 0 | 307ms | 2%  
迈阿密 | 29个 | 0 | 310ms | 6%  
伦敦 | 34个 | 0 | 343ms | 3%  
  
**简评：** 本表展示了广西的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻广西，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶、硅谷、西雅图、悉尼** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**广西电信到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 12个 | 0 | 231ms | 27%  
新加坡 | 15个 | 0 | 194ms | 11%  
洛杉矶 | 10个 | 0 | 214ms | 3%  
硅谷 | 10个 | 0 | 223ms | 3%  
西雅图 | 10个 | 0 | 266ms | 6%  
悉尼 | 12个 | 0 | 291ms | 3%  
均值 | 187个 | 0 | 275ms | 6%  
达拉斯 | 10个 | 0 | 252ms | 6%  
巴黎 | 15个 | 0 | 258ms | 3%  
法兰克福 | 15个 | 0 | 284ms | 5%  
芝加哥 | 12个 | 0 | 358ms | 5%  
亚特兰大 | 12个 | 0 | 294ms | 5%  
阿姆斯特丹 | 15个 | 0 | 245ms | 1%  
新泽西 | 12个 | 0 | 333ms | 2%  
迈阿密 | 12个 | 0 | 340ms | 6%  
伦敦 | 15个 | 0 | 339ms | 3%  
  
**简评：** 如果你是来自广西的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、硅谷、阿姆斯特丹** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **新加坡、东京** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**广西联通到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 7个 | 0 | 140ms | 10%  
新加坡 | 9个 | 0 | 191ms | 8%  
洛杉矶 | 7个 | 0 | 192ms | 3%  
硅谷 | 7个 | 1个 | 221ms | 8%  
西雅图 | 7个 | 0 | 230ms | 7%  
悉尼 | 7个 | 0 | 220ms | 4%  
均值 | 117个 | 1个 | 264ms | 5%  
达拉斯 | 7个 | 0 | 246ms | 6%  
巴黎 | 9个 | 0 | 324ms | 4%  
法兰克福 | 9个 | 0 | 326ms | 5%  
芝加哥 | 7个 | 0 | 276ms | 1%  
亚特兰大 | 7个 | 0 | 269ms | 6%  
阿姆斯特丹 | 9个 | 0 | 327ms | 5%  
新泽西 | 10个 | 0 | 310ms | 3%  
迈阿密 | 7个 | 0 | 285ms | 7%  
伦敦 | 8个 | 0 | 341ms | 4%  
  
**简评：** 如果你是来自广西的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡、硅谷、西雅图、达拉斯** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**广西移动到Vultr各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 10个 | 0 | 111ms | 4%  
新加坡 | 11个 | 0 | 133ms | 2%  
洛杉矶 | 10个 | 0 | 185ms | 0  
硅谷 | 10个 | 0 | 194ms | 0  
西雅图 | 9个 | 0 | 189ms | 0  
悉尼 | 10个 | 0 | 189ms | 0  
均值 | 153个 | 0 | 247ms | 3%  
达拉斯 | 10个 | 0 | 300ms | 7%  
巴黎 | 11个 | 0 | 273ms | 4%  
法兰克福 | 11个 | 0 | 258ms | 4%  
芝加哥 | 10个 | 0 | 247ms | 1%  
亚特兰大 | 10个 | 0 | 334ms | 10%  
阿姆斯特丹 | 11个 | 0 | 344ms | 4%  
新泽西 | 9个 | 0 | 279ms | 0  
迈阿密 | 10个 | 0 | 307ms | 4%  
伦敦 | 11个 | 0 | 347ms | 2%  
  
**简评：** 如果你是来自广西的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、洛杉矶、西雅图、悉尼、硅谷、芝加哥** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
  * 广西到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/guangxi/20180514-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/guangxi/20180527-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/guangxi/20180622-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/guangxi/20180804-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/guangxi/20180918-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180918")
  * 本期报告：广西到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/guangxi/20180426-bandwagon-isp-guangxi.md "广西到BandwagonHost各机房的Ping测试 20180426")
    * [Digital Ocean](/digitalocean/isp/guangxi/20180426-digitalocean-isp-guangxi.md "广西到Digital Ocean各机房的Ping测试 20180426")
    * [Linode](/linode/isp/guangxi/20180426-linode-isp-guangxi.md "广西到Linode各机房的Ping测试 20180426")



本文最初发表于[广西到Vultr各机房的测速数据（20180426）](https://vps123.top/pingtest/20180426-vultr-isp-guangxi.html)
