#  江西到Vultr各机房的测速数据（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![江西到Vultr各机房的测速数据（20180527）](/images/thumbnails/Jiangxi_to_vultr.png)

本文的数据视角为 **江西到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在江西且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点361个，其中超时点2个。连通概况如下：大陆线路响应均值为259毫秒，最快的三个机房所在地为东京、新加坡、硅谷，最慢的三个为巴黎、阿姆斯特丹、伦敦；法兰克福有响应超时情况；东京、达拉斯、亚特兰大、悉尼、新加坡等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 江西图表数据

![大陆省份江西到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_isp_jiangxi_vultr_20180527.png)

### 全部运营商

江西全部运营商到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 23个 | 0 | 162ms | 14% | 迈阿密 | 24个 | 0 | 272ms | 4%  
新加坡 | 25个 | 0 | 208ms | 10% | 亚特兰大 | 24个 | 0 | 276ms | 12%  
硅谷 | 25个 | 0 | 213ms | 5% | 新泽西 | 23个 | 0 | 279ms | 1%  
洛杉矶 | 24个 | 0 | 214ms | 2% | 法兰克福 | 23个 | 2个 | 292ms | 3%  
西雅图 | 23个 | 0 | 232ms | 9% | 悉尼 | 24个 | 0 | 294ms | 11%  
均值 | 361个 | 2个 | 259ms | 6% | 巴黎 | 25个 | 0 | 294ms | 1%  
达拉斯 | 25个 | 0 | 270ms | 12% | 阿姆斯特丹 | 23个 | 0 | 305ms | 1%  
芝加哥 | 25个 | 0 | 272ms | 5% | 伦敦 | 25个 | 0 | 318ms | 4%  
  
简评：本表展示了江西的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻江西，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **硅谷、洛杉矶** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

江西电信到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 11个 | 0 | 204ms | 33% | 迈阿密 | 13个 | 0 | 279ms | 2%  
新加坡 | 13个 | 0 | 259ms | 22% | 亚特兰大 | 13个 | 0 | 262ms | 6%  
硅谷 | 13个 | 0 | 219ms | 6% | 新泽西 | 12个 | 0 | 329ms | 4%  
洛杉矶 | 12个 | 0 | 238ms | 3% | 法兰克福 | 12个 | 2个 | 255ms | 1%  
西雅图 | 11个 | 0 | 269ms | 3% | 悉尼 | 12个 | 0 | 354ms | 23%  
均值 | 186个 | 2个 | 270ms | 8% | 巴黎 | 13个 | 0 | 243ms | 0  
达拉斯 | 13个 | 0 | 279ms | 6% | 阿姆斯特丹 | 12个 | 0 | 249ms | 0  
芝加哥 | 13个 | 0 | 322ms | 6% | 伦敦 | 13个 | 0 | 301ms | 1%  
  
简评：如果你是来自江西的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、巴黎、阿姆斯特丹** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、硅谷** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

江西联通到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 3个 | 0 | 155ms | 6% | 迈阿密 | 3个 | 0 | 242ms | 0  
新加坡 | 3个 | 0 | 236ms | 6% | 亚特兰大 | 3个 | 0 | 231ms | 0  
硅谷 | 3个 | 0 | 201ms | 0 | 新泽西 | 3个 | 0 | 240ms | 0  
洛杉矶 | 3个 | 0 | 189ms | 0 | 法兰克福 | 3个 | 0 | 331ms | 5%  
西雅图 | 3个 | 0 | 211ms | 13% | 悉尼 | 3个 | 0 | 263ms | 4%  
均值 | 45个 | 0 | 247ms | 2% | 巴黎 | 3个 | 0 | 338ms | 1%  
达拉斯 | 3个 | 0 | 216ms | 0 | 阿姆斯特丹 | 3个 | 0 | 316ms | 1%  
芝加哥 | 3个 | 0 | 240ms | 0 | 伦敦 | 3个 | 0 | 304ms | 0  
  
简评：如果你是来自江西的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、硅谷、达拉斯、亚特兰大、芝加哥、新泽西、迈阿密** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、西雅图、新加坡** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

江西移动到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 9个 | 0 | 126ms | 4% | 迈阿密 | 8个 | 0 | 294ms | 10%  
新加坡 | 9个 | 0 | 130ms | 3% | 亚特兰大 | 8个 | 0 | 334ms | 29%  
硅谷 | 9个 | 0 | 220ms | 9% | 新泽西 | 8个 | 0 | 270ms | 0  
洛杉矶 | 9个 | 0 | 215ms | 2% | 法兰克福 | 8个 | 0 | 290ms | 3%  
西雅图 | 9个 | 0 | 215ms | 10% | 悉尼 | 9个 | 0 | 266ms | 6%  
均值 | 130个 | 0 | 260ms | 9% | 巴黎 | 9个 | 0 | 301ms | 3%  
达拉斯 | 9个 | 0 | 316ms | 29% | 阿姆斯特丹 | 8个 | 0 | 349ms | 4%  
芝加哥 | 9个 | 0 | 254ms | 8% | 伦敦 | 9个 | 0 | 350ms | 13%  
  
简评：如果你是来自江西的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、洛杉矶** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **西雅图、硅谷** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [重庆](/vultr/isp/chongqing/20180527-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180527")
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
  * 江西到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/jiangxi/20180514-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180514")
    * [20180622](/vultr/isp/jiangxi/20180622-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/jiangxi/20180804-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/jiangxi/20180918-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180918")
  * 本期报告：江西到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/jiangxi/20180527-bandwagon-isp-jiangxi.md "江西到BandwagonHost各机房的Ping测试 20180527")
    * [Digital Ocean](/digitalocean/isp/jiangxi/20180527-digitalocean-isp-jiangxi.md "江西到Digital Ocean各机房的Ping测试 20180527")
    * [Linode](/linode/isp/jiangxi/20180527-linode-isp-jiangxi.md "江西到Linode各机房的Ping测试 20180527")



本文最初发表于[江西到Vultr各机房的测速数据（20180527）](https://vps123.top/pingtest/20180527-vultr-isp-jiangxi.html)
