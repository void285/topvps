#  湖南到Vultr各机房的测速数据（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![湖南到Vultr各机房的测速数据（20180918）](/images/thumbnails/Hunan_to_vultr.png)

本文的数据视角为 **湖南到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在湖南且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918湖南到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点1038个，其中超时点3个。连通概况如下：大陆线路响应均值为241毫秒，最快的三个机房所在地为东京、新加坡、洛杉矶，最慢的三个为伦敦、迈阿密、阿姆斯特丹；芝加哥、迈阿密、阿姆斯特丹有响应超时情况；巴黎、阿姆斯特丹、法兰克福、迈阿密、亚特兰大等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 湖南图表数据

![大陆省份湖南到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_isp_hunan_vultr_20180918.png)

### 全部运营商

湖南全部运营商到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 71个 | 0 | 135ms | 2% | 悉尼 | 65个 | 0 | 260ms | 0  
新加坡 | 72个 | 0 | 167ms | 1% | 亚特兰大 | 66个 | 0 | 265ms | 5%  
洛杉矶 | 69个 | 0 | 207ms | 5% | 新泽西 | 71个 | 0 | 266ms | 5%  
硅谷 | 71个 | 0 | 208ms | 2% | 巴黎 | 67个 | 0 | 275ms | 9%  
西雅图 | 68个 | 0 | 208ms | 4% | 法兰克福 | 71个 | 0 | 283ms | 7%  
达拉斯 | 67个 | 0 | 228ms | 1% | 伦敦 | 72个 | 0 | 289ms | 3%  
均值 | 1038个 | 3个 | 241ms | 4% | 迈阿密 | 72个 | 1个 | 289ms | 6%  
芝加哥 | 65个 | 1个 | 252ms | 1% | 阿姆斯特丹 | 71个 | 1个 | 294ms | 8%  
  
简评：本表展示了湖南的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻湖南，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **东京、新加坡、洛杉矶、硅谷、西雅图、达拉斯** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

湖南电信到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 25个 | 0 | 170ms | 6% | 悉尼 | 24个 | 0 | 300ms | 1%  
新加坡 | 26个 | 0 | 222ms | 2% | 亚特兰大 | 22个 | 0 | 266ms | 6%  
洛杉矶 | 25个 | 0 | 229ms | 13% | 新泽西 | 26个 | 0 | 263ms | 2%  
硅谷 | 25个 | 0 | 214ms | 5% | 巴黎 | 23个 | 0 | 284ms | 17%  
西雅图 | 26个 | 0 | 223ms | 9% | 法兰克福 | 26个 | 0 | 297ms | 7%  
达拉斯 | 24个 | 0 | 224ms | 2% | 伦敦 | 26个 | 0 | 279ms | 3%  
均值 | 370个 | 2个 | 253ms | 6% | 迈阿密 | 26个 | 1个 | 295ms | 14%  
芝加哥 | 22个 | 0 | 251ms | 4% | 阿姆斯特丹 | 24个 | 1个 | 292ms | 4%  
  
简评：如果你是来自湖南的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **硅谷、新加坡、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、西雅图、洛杉矶** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

湖南联通到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 25个 | 0 | 113ms | 0 | 悉尼 | 23个 | 0 | 246ms | 0  
新加坡 | 25个 | 0 | 148ms | 1% | 亚特兰大 | 25个 | 0 | 255ms | 5%  
洛杉矶 | 24个 | 0 | 195ms | 2% | 新泽西 | 25个 | 0 | 274ms | 13%  
硅谷 | 26个 | 0 | 200ms | 0 | 巴黎 | 23个 | 0 | 283ms | 3%  
西雅图 | 23个 | 0 | 193ms | 0 | 法兰克福 | 25个 | 0 | 300ms | 6%  
达拉斯 | 23个 | 0 | 225ms | 2% | 伦敦 | 25个 | 0 | 322ms | 6%  
均值 | 366个 | 1个 | 239ms | 4% | 迈阿密 | 25个 | 0 | 267ms | 1%  
芝加哥 | 23个 | 1个 | 244ms | 0 | 阿姆斯特丹 | 26个 | 0 | 325ms | 16%  
  
简评：如果你是来自湖南的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、西雅图、洛杉矶、硅谷、达拉斯、芝加哥、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

湖南移动到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 21个 | 0 | 123ms | 1% | 悉尼 | 18个 | 0 | 235ms | 0  
新加坡 | 21个 | 0 | 130ms | 0 | 亚特兰大 | 19个 | 0 | 274ms | 5%  
洛杉矶 | 20个 | 0 | 197ms | 0 | 新泽西 | 20个 | 0 | 262ms | 0  
硅谷 | 20个 | 0 | 210ms | 0 | 巴黎 | 21个 | 0 | 257ms | 9%  
西雅图 | 19个 | 0 | 208ms | 4% | 法兰克福 | 20个 | 0 | 254ms | 8%  
达拉斯 | 20个 | 0 | 235ms | 0 | 伦敦 | 21个 | 0 | 266ms | 0  
均值 | 302个 | 0 | 232ms | 2% | 迈阿密 | 21个 | 0 | 305ms | 2%  
芝加哥 | 20个 | 0 | 260ms | 0 | 阿姆斯特丹 | 21个 | 0 | 266ms | 5%  
  
简评：如果你是来自湖南的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、洛杉矶、西雅图、硅谷、达拉斯、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180918) 
    * [全部](https://vps123.top/pingtests/20180918 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180918 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180918 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180918 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180918-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180918")
    * [北京](/vultr/isp/beijing/20180918-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180918")
    * [大陆](/vultr/isp/china/20180918-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180918")
    * [重庆](/vultr/isp/chongqing/20180918-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180918")
    * [福建](/vultr/isp/fujian/20180918-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180918")
    * [甘肃](/vultr/isp/gansu/20180918-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180918")
    * [广东](/vultr/isp/guangdong/20180918-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180918")
    * [广西](/vultr/isp/guangxi/20180918-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180918")
    * [贵州](/vultr/isp/guizhou/20180918-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180918")
    * [海南](/vultr/isp/hainan/20180918-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180918")
    * [河北](/vultr/isp/hebei/20180918-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180918")
    * [黑龙江](/vultr/isp/heilongjiang/20180918-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180918")
    * [河南](/vultr/isp/henan/20180918-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180918")
    * [湖北](/vultr/isp/hubei/20180918-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180918")
    * [内蒙古](/vultr/isp/innermongolia/20180918-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180918")
    * [江苏](/vultr/isp/jiangsu/20180918-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180918")
    * [江西](/vultr/isp/jiangxi/20180918-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180918")
    * [吉林](/vultr/isp/jilin/20180918-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180918")
    * [辽宁](/vultr/isp/liaoning/20180918-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180918")
    * [宁夏](/vultr/isp/ningxia/20180918-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180918")
    * [青海](/vultr/isp/qinghai/20180918-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180918")
    * [山西](/vultr/isp/shan1xi/20180918-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180918")
    * [陕西](/vultr/isp/shan3xi/20180918-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180918")
    * [山东](/vultr/isp/shandong/20180918-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180918")
    * [上海](/vultr/isp/shanghai/20180918-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180918")
    * [四川](/vultr/isp/sichuan/20180918-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180918")
    * [天津](/vultr/isp/tianjin/20180918-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180918")
    * [西藏](/vultr/isp/tibet/20180918-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180918")
    * [新疆](/vultr/isp/xinjiang/20180918-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180918")
    * [云南](/vultr/isp/yunnan/20180918-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180918")
    * [浙江](/vultr/isp/zhejiang/20180918-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180918")
  * 湖南到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/hunan/20180514-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/hunan/20180527-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/hunan/20180622-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/hunan/20180804-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180804")
  * 本期报告：湖南到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/hunan/20180918-bandwagon-isp-hunan.md "湖南到BandwagonHost各机房的Ping测试 20180918")
    * [Digital Ocean](/digitalocean/isp/hunan/20180918-digitalocean-isp-hunan.md "湖南到Digital Ocean各机房的Ping测试 20180918")
    * [Linode](/linode/isp/hunan/20180918-linode-isp-hunan.md "湖南到Linode各机房的Ping测试 20180918")



本文最初发表于[湖南到Vultr各机房的测速数据（20180918）](https://vps123.top/pingtest/20180918-vultr-isp-hunan.html)
