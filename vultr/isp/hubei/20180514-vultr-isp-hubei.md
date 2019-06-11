#  湖北到Vultr各机房的测速数据（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![湖北到Vultr各机房的测速数据（20180514）](/images/thumbnails/Hubei_to_vultr.png)

本文的数据视角为 **湖北到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在湖北且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514湖北到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点692个，其中超时点6个。连通概况如下：大陆线路响应均值为271毫秒，最快的三个机房所在地为东京、新加坡、西雅图，最慢的三个为迈阿密、伦敦、亚特兰大；洛杉矶、东京、阿姆斯特丹有响应超时情况；伦敦、新泽西、亚特兰大、芝加哥、迈阿密等12处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 湖北图表数据

![大陆省份湖北到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_isp_hubei_vultr_20180514.png)

### 全部运营商

**湖北全部运营商到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 48个 | 2个 | 147ms | 15%  
新加坡 | 47个 | 0 | 198ms | 11%  
西雅图 | 46个 | 0 | 220ms | 3%  
悉尼 | 45个 | 0 | 253ms | 6%  
洛杉矶 | 48个 | 3个 | 259ms | 17%  
硅谷 | 47个 | 0 | 266ms | 10%  
均值 | 692个 | 6个 | 271ms | 14%  
芝加哥 | 48个 | 0 | 285ms | 22%  
巴黎 | 43个 | 0 | 288ms | 5%  
法兰克福 | 42个 | 0 | 292ms | 4%  
阿姆斯特丹 | 45个 | 1个 | 295ms | 4%  
达拉斯 | 48个 | 0 | 297ms | 13%  
新泽西 | 48个 | 0 | 310ms | 23%  
迈阿密 | 44个 | 0 | 319ms | 21%  
伦敦 | 47个 | 0 | 330ms | 26%  
亚特兰大 | 46个 | 0 | 340ms | 23%  
  
**简评：** 本表展示了湖北的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻湖北，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **西雅图** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**湖北电信到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 26个 | 2个 | 123ms | 11%  
新加坡 | 25个 | 0 | 192ms | 8%  
西雅图 | 24个 | 0 | 228ms | 2%  
悉尼 | 24个 | 0 | 259ms | 1%  
洛杉矶 | 25个 | 3个 | 273ms | 18%  
硅谷 | 25个 | 0 | 289ms | 9%  
均值 | 368个 | 6个 | 273ms | 9%  
芝加哥 | 26个 | 0 | 311ms | 8%  
巴黎 | 22个 | 0 | 254ms | 1%  
法兰克福 | 23个 | 0 | 262ms | 0  
阿姆斯特丹 | 25个 | 1个 | 260ms | 0  
达拉斯 | 26个 | 0 | 314ms | 11%  
新泽西 | 25个 | 0 | 351ms | 15%  
迈阿密 | 23个 | 0 | 355ms | 15%  
伦敦 | 25个 | 0 | 349ms | 14%  
亚特兰大 | 24个 | 0 | 351ms | 19%  
  
**简评：** 如果你是来自湖北的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **西雅图** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**湖北联通到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 11个 | 0 | 174ms | 26%  
新加坡 | 11个 | 0 | 250ms | 18%  
西雅图 | 11个 | 0 | 215ms | 3%  
悉尼 | 10个 | 0 | 257ms | 10%  
洛杉矶 | 11个 | 0 | 225ms | 9%  
硅谷 | 11个 | 0 | 230ms | 4%  
均值 | 160个 | 0 | 266ms | 18%  
芝加哥 | 11个 | 0 | 281ms | 41%  
巴黎 | 10个 | 0 | 315ms | 7%  
法兰克福 | 9个 | 0 | 326ms | 6%  
阿姆斯特丹 | 11个 | 0 | 309ms | 4%  
达拉斯 | 11个 | 0 | 239ms | 6%  
新泽西 | 11个 | 0 | 287ms | 39%  
迈阿密 | 11个 | 0 | 294ms | 30%  
伦敦 | 10个 | 0 | 338ms | 49%  
亚特兰大 | 11个 | 0 | 273ms | 15%  
  
**简评：** 如果你是来自湖北的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **西雅图、硅谷** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、洛杉矶、达拉斯、新加坡** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**湖北移动到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 11个 | 0 | 143ms | 7%  
新加坡 | 11个 | 0 | 152ms | 8%  
西雅图 | 11个 | 0 | 217ms | 5%  
悉尼 | 11个 | 0 | 242ms | 8%  
洛杉矶 | 12个 | 0 | 281ms | 24%  
硅谷 | 11个 | 0 | 278ms | 18%  
均值 | 164个 | 0 | 274ms | 15%  
芝加哥 | 11个 | 0 | 264ms | 17%  
巴黎 | 11个 | 0 | 295ms | 8%  
法兰克福 | 10个 | 0 | 288ms | 6%  
阿姆斯特丹 | 9个 | 0 | 317ms | 8%  
达拉斯 | 11个 | 0 | 338ms | 22%  
新泽西 | 12个 | 0 | 291ms | 16%  
迈阿密 | 10个 | 0 | 309ms | 18%  
伦敦 | 12个 | 0 | 303ms | 15%  
亚特兰大 | 11个 | 0 | 396ms | 34%  
  
**简评：** 如果你是来自湖北的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **西雅图** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡、悉尼** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [新疆](/vultr/isp/xinjiang/20180514-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180514")
    * [云南](/vultr/isp/yunnan/20180514-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180514")
    * [浙江](/vultr/isp/zhejiang/20180514-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180514")
  * 湖北到Vultr各机房的 _其他近期报告_ ： 
    * [20180527](/vultr/isp/hubei/20180527-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/hubei/20180622-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/hubei/20180804-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/hubei/20180918-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180918")
  * 本期报告：湖北到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/hubei/20180514-bandwagon-isp-hubei.md "湖北到BandwagonHost各机房的Ping测试 20180514")
    * [Digital Ocean](/digitalocean/isp/hubei/20180514-digitalocean-isp-hubei.md "湖北到Digital Ocean各机房的Ping测试 20180514")
    * [Linode](/linode/isp/hubei/20180514-linode-isp-hubei.md "湖北到Linode各机房的Ping测试 20180514")



本文最初发表于[湖北到Vultr各机房的测速数据（20180514）](https://vps123.top/pingtest/20180514-vultr-isp-hubei.html)
