#  新疆到Vultr各机房的测速数据（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![新疆到Vultr各机房的测速数据（20180514）](/images/thumbnails/Xinjiang_to_vultr.png)

本文的数据视角为 **新疆到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在新疆且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514新疆到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点412个，其中超时点2个。连通概况如下：大陆线路响应均值为310毫秒，最快的三个机房所在地为东京、新加坡、洛杉矶，最慢的三个为伦敦、迈阿密、亚特兰大；东京、亚特兰大有响应超时情况；亚特兰大、东京、硅谷、达拉斯、新加坡等10处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 新疆图表数据

![大陆省份新疆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_isp_xinjiang_vultr_20180514.png)

### 全部运营商

**新疆全部运营商到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 25个 | 1个 | 194ms | 13%  
新加坡 | 28个 | 0 | 260ms | 11%  
洛杉矶 | 27个 | 0 | 270ms | 11%  
西雅图 | 27个 | 0 | 276ms | 9%  
硅谷 | 29个 | 0 | 291ms | 13%  
悉尼 | 28个 | 0 | 301ms | 4%  
均值 | 412个 | 2个 | 310ms | 8%  
达拉斯 | 28个 | 0 | 321ms | 12%  
巴黎 | 29个 | 0 | 323ms | 2%  
阿姆斯特丹 | 28个 | 0 | 325ms | 3%  
芝加哥 | 28个 | 0 | 326ms | 8%  
法兰克福 | 22个 | 0 | 329ms | 5%  
新泽西 | 29个 | 0 | 349ms | 1%  
伦敦 | 28个 | 0 | 351ms | 2%  
迈阿密 | 27个 | 0 | 362ms | 8%  
亚特兰大 | 29个 | 1个 | 364ms | 14%  
  
**简评：** 本表展示了新疆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻新疆，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到，各机房所在城市的响应值、丢包率都较高（TopVPS推荐选用响应值低于250ms，丢包率在5%%以内的机房），请慎重选择；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**新疆电信到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 9个 | 1个 | 173ms | 10%  
新加坡 | 11个 | 0 | 256ms | 12%  
洛杉矶 | 11个 | 0 | 236ms | 1%  
西雅图 | 10个 | 0 | 280ms | 3%  
硅谷 | 12个 | 0 | 291ms | 2%  
悉尼 | 11个 | 0 | 299ms | 0  
均值 | 163个 | 2个 | 290ms | 2%  
达拉斯 | 11个 | 0 | 254ms | 2%  
巴黎 | 12个 | 0 | 280ms | 1%  
阿姆斯特丹 | 12个 | 0 | 291ms | 2%  
芝加哥 | 12个 | 0 | 324ms | 0  
法兰克福 | 6个 | 0 | 291ms | 0  
新泽西 | 12个 | 0 | 361ms | 2%  
伦敦 | 11个 | 0 | 332ms | 0  
迈阿密 | 11个 | 0 | 359ms | 2%  
亚特兰大 | 12个 | 1个 | 305ms | 1%  
  
**简评：** 如果你是来自新疆的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**新疆联通到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 4个 | 0 | 239ms | 25%  
新加坡 | 5个 | 0 | 343ms | 18%  
洛杉矶 | 4个 | 0 | 284ms | 9%  
西雅图 | 5个 | 0 | 268ms | 8%  
硅谷 | 5个 | 0 | 273ms | 8%  
悉尼 | 5个 | 0 | 325ms | 11%  
均值 | 73个 | 0 | 332ms | 10%  
达拉斯 | 5个 | 0 | 324ms | 14%  
巴黎 | 5个 | 0 | 357ms | 4%  
阿姆斯特丹 | 5个 | 0 | 377ms | 7%  
芝加哥 | 5个 | 0 | 329ms | 11%  
法兰克福 | 5个 | 0 | 385ms | 14%  
新泽西 | 5个 | 0 | 349ms | 1%  
伦敦 | 5个 | 0 | 391ms | 5%  
迈阿密 | 5个 | 0 | 351ms | 9%  
亚特兰大 | 5个 | 0 | 356ms | 12%  
  
**简评：** 如果你是来自新疆的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**新疆移动到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 12个 | 0 | 170ms | 5%  
新加坡 | 12个 | 0 | 180ms | 4%  
洛杉矶 | 12个 | 0 | 289ms | 23%  
西雅图 | 12个 | 0 | 281ms | 18%  
硅谷 | 12个 | 0 | 309ms | 27%  
悉尼 | 12个 | 0 | 280ms | 1%  
均值 | 176个 | 0 | 309ms | 11%  
达拉斯 | 12个 | 0 | 383ms | 21%  
巴黎 | 12个 | 0 | 332ms | 2%  
阿姆斯特丹 | 11个 | 0 | 308ms | 0  
芝加哥 | 11个 | 0 | 326ms | 13%  
法兰克福 | 11个 | 0 | 309ms | 2%  
新泽西 | 12个 | 0 | 339ms | 0  
伦敦 | 12个 | 0 | 329ms | 0  
迈阿密 | 11个 | 0 | 378ms | 13%  
亚特兰大 | 12个 | 0 | 430ms | 30%  
  
**简评：** 如果你是来自新疆的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180514 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180514 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180514-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180514")
    * [北京](/vultr/isp/beijing/20180514-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180514")
    * [大陆](/vultr/isp/china/20180514-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180514")
    * [重庆](/vultr/isp/chongqing/20180514-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180514")
    * [福建](/vultr/isp/fujian/20180514-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180514")
    * [甘肃](/vultr/isp/gansu/20180514-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180514")
    * [广东](/vultr/isp/guangdong/20180514-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180514")
    * [广西](/vultr/isp/guangxi/20180514-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180514")
    * [贵州](/vultr/isp/guizhou/20180514-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180514")
    * [海南](/vultr/isp/hainan/20180514-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180514")
    * [河北](/vultr/isp/hebei/20180514-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180514")
    * [黑龙江](/vultr/isp/heilongjiang/20180514-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180514")
    * [河南](/vultr/isp/henan/20180514-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180514")
    * [湖北](/vultr/isp/hubei/20180514-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180514")
    * [湖南](/vultr/isp/hunan/20180514-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180514")
    * [内蒙古](/vultr/isp/innermongolia/20180514-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180514")
    * [江苏](/vultr/isp/jiangsu/20180514-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180514")
    * [江西](/vultr/isp/jiangxi/20180514-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180514")
    * [吉林](/vultr/isp/jilin/20180514-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180514")
    * [辽宁](/vultr/isp/liaoning/20180514-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180514")
    * [宁夏](/vultr/isp/ningxia/20180514-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180514")
    * [青海](/vultr/isp/qinghai/20180514-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180514")
    * [山西](/vultr/isp/shan1xi/20180514-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180514")
    * [陕西](/vultr/isp/shan3xi/20180514-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180514")
    * [山东](/vultr/isp/shandong/20180514-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180514")
    * [上海](/vultr/isp/shanghai/20180514-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180514")
    * [四川](/vultr/isp/sichuan/20180514-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180514")
    * [天津](/vultr/isp/tianjin/20180514-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180514")
    * [西藏](/vultr/isp/tibet/20180514-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180514")
    * [云南](/vultr/isp/yunnan/20180514-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180514")
    * [浙江](/vultr/isp/zhejiang/20180514-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180514")
  * 新疆到Vultr各机房的 _其他近期报告_ ： 
    * [20180527](/vultr/isp/xinjiang/20180527-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/xinjiang/20180622-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/xinjiang/20180804-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/xinjiang/20180918-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180918")
  * 本期报告：新疆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/xinjiang/20180514-bandwagon-isp-xinjiang.md "新疆到BandwagonHost各机房的Ping测试 20180514")
    * [Digital Ocean](/digitalocean/isp/xinjiang/20180514-digitalocean-isp-xinjiang.md "新疆到Digital Ocean各机房的Ping测试 20180514")
    * [Linode](/linode/isp/xinjiang/20180514-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180514")



本文最初发表于[新疆到Vultr各机房的测速数据（20180514）](https://vps123.top/pingtest/20180514-vultr-isp-xinjiang.html)
