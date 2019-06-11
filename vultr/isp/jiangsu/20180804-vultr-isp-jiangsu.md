#  江苏到Vultr各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![江苏到Vultr各机房的测速数据（20180804）](/images/thumbnails/Jiangsu_to_vultr.png)

本文的数据视角为 **江苏到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在江苏且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点4198个，其中超时点195个。连通概况如下：大陆线路响应均值为274毫秒，最快的三个机房所在地为东京、洛杉矶、西雅图，最慢的三个为新泽西、悉尼、阿姆斯特丹；悉尼、新加坡、阿姆斯特丹、东京、法兰克福等15处有响应超时情况；东京、新加坡、悉尼、硅谷、芝加哥等8处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 江苏图表数据

![大陆省份江苏到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_isp_jiangsu_vultr_20180804.png)

### 全部运营商

江苏全部运营商到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 346个 | 12个 | 198ms | 23% | 法兰克福 | 343个 | 12个 | 297ms | 1%  
洛杉矶 | 235个 | 9个 | 214ms | 3% | 亚特兰大 | 234个 | 12个 | 304ms | 3%  
西雅图 | 238个 | 9个 | 223ms | 4% | 迈阿密 | 242个 | 12个 | 309ms | 6%  
新加坡 | 242个 | 24个 | 233ms | 23% | 伦敦 | 338个 | 12个 | 311ms | 5%  
硅谷 | 343个 | 9个 | 235ms | 10% | 巴黎 | 238个 | 9个 | 316ms | 2%  
达拉斯 | 350个 | 9个 | 261ms | 4% | 新泽西 | 331个 | 9个 | 318ms | 6%  
芝加哥 | 238个 | 9个 | 272ms | 9% | 悉尼 | 238个 | 33个 | 336ms | 22%  
均值 | 4198个 | 195个 | 274ms | 8% | 阿姆斯特丹 | 242个 | 15个 | 342ms | 3%  
  
简评：本表展示了江苏的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻江苏，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶、西雅图** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

江苏电信到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 162个 | 12个 | 207ms | 41% | 法兰克福 | 162个 | 12个 | 301ms | 2%  
洛杉矶 | 118个 | 9个 | 236ms | 5% | 亚特兰大 | 118个 | 9个 | 334ms | 4%  
西雅图 | 118个 | 9个 | 242ms | 2% | 迈阿密 | 118个 | 9个 | 347ms | 5%  
新加坡 | 118个 | 18个 | 268ms | 39% | 伦敦 | 162个 | 9个 | 319ms | 9%  
硅谷 | 162个 | 9个 | 249ms | 7% | 巴黎 | 118个 | 9个 | 299ms | 3%  
达拉斯 | 162个 | 9个 | 300ms | 6% | 新泽西 | 162个 | 9个 | 369ms | 8%  
芝加哥 | 118个 | 9个 | 286ms | 5% | 悉尼 | 118个 | 27个 | 380ms | 38%  
均值 | 2034个 | 174个 | 295ms | 12% | 阿姆斯特丹 | 118个 | 15个 | 342ms | 4%  
  
简评：如果你是来自江苏的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、西雅图** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、硅谷** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

江苏联通到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 97个 | 0 | 241ms | 22% | 法兰克福 | 97个 | 0 | 268ms | 1%  
洛杉矶 | 62个 | 0 | 207ms | 3% | 亚特兰大 | 61个 | 0 | 307ms | 4%  
西雅图 | 65个 | 0 | 213ms | 8% | 迈阿密 | 65个 | 3个 | 281ms | 3%  
新加坡 | 65个 | 3个 | 284ms | 22% | 伦敦 | 89个 | 3个 | 335ms | 3%  
硅谷 | 97个 | 0 | 217ms | 5% | 巴黎 | 61个 | 0 | 324ms | 1%  
达拉斯 | 97个 | 0 | 238ms | 6% | 新泽西 | 93个 | 0 | 312ms | 9%  
芝加哥 | 65个 | 0 | 262ms | 7% | 悉尼 | 65个 | 3个 | 375ms | 22%  
均值 | 1144个 | 12个 | 276ms | 8% | 阿姆斯特丹 | 65个 | 0 | 345ms | 2%  
  
简评：如果你是来自江苏的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、硅谷** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **西雅图、达拉斯、东京** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

江苏移动到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 87个 | 0 | 145ms | 7% | 法兰克福 | 84个 | 0 | 322ms | 2%  
洛杉矶 | 55个 | 0 | 200ms | 0 | 亚特兰大 | 55个 | 3个 | 272ms | 1%  
西雅图 | 55个 | 0 | 213ms | 1% | 迈阿密 | 59个 | 0 | 298ms | 11%  
新加坡 | 59个 | 3个 | 148ms | 7% | 伦敦 | 87个 | 0 | 279ms | 4%  
硅谷 | 84个 | 0 | 240ms | 19% | 巴黎 | 59个 | 0 | 326ms | 1%  
达拉斯 | 91个 | 0 | 245ms | 0 | 新泽西 | 76个 | 0 | 272ms | 1%  
芝加哥 | 55个 | 0 | 269ms | 14% | 悉尼 | 55个 | 3个 | 252ms | 6%  
均值 | 1020个 | 9个 | 253ms | 5% | 阿姆斯特丹 | 59个 | 0 | 339ms | 3%  
  
简评：如果你是来自江苏的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、西雅图、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡、硅谷** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180804 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180804 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180804-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180804")
    * [北京](/vultr/isp/beijing/20180804-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180804")
    * [大陆](/vultr/isp/china/20180804-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180804")
    * [重庆](/vultr/isp/chongqing/20180804-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180804")
    * [福建](/vultr/isp/fujian/20180804-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180804")
    * [甘肃](/vultr/isp/gansu/20180804-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180804")
    * [广东](/vultr/isp/guangdong/20180804-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180804")
    * [广西](/vultr/isp/guangxi/20180804-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180804")
    * [贵州](/vultr/isp/guizhou/20180804-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180804")
    * [海南](/vultr/isp/hainan/20180804-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180804")
    * [河北](/vultr/isp/hebei/20180804-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180804")
    * [黑龙江](/vultr/isp/heilongjiang/20180804-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180804")
    * [河南](/vultr/isp/henan/20180804-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180804")
    * [湖北](/vultr/isp/hubei/20180804-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180804")
    * [湖南](/vultr/isp/hunan/20180804-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180804")
    * [内蒙古](/vultr/isp/innermongolia/20180804-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180804")
    * [江西](/vultr/isp/jiangxi/20180804-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180804")
    * [吉林](/vultr/isp/jilin/20180804-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180804")
    * [辽宁](/vultr/isp/liaoning/20180804-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180804")
    * [宁夏](/vultr/isp/ningxia/20180804-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180804")
    * [青海](/vultr/isp/qinghai/20180804-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180804")
    * [山西](/vultr/isp/shan1xi/20180804-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180804")
    * [陕西](/vultr/isp/shan3xi/20180804-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180804")
    * [山东](/vultr/isp/shandong/20180804-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180804")
    * [上海](/vultr/isp/shanghai/20180804-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180804")
    * [四川](/vultr/isp/sichuan/20180804-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180804")
    * [天津](/vultr/isp/tianjin/20180804-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180804")
    * [西藏](/vultr/isp/tibet/20180804-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180804")
    * [新疆](/vultr/isp/xinjiang/20180804-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180804")
    * [云南](/vultr/isp/yunnan/20180804-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180804")
    * [浙江](/vultr/isp/zhejiang/20180804-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180804")
  * 江苏到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/jiangsu/20180514-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/jiangsu/20180527-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/jiangsu/20180622-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180622")
    * [20180918](/vultr/isp/jiangsu/20180918-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180918")
  * 本期报告：江苏到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/jiangsu/20180804-bandwagon-isp-jiangsu.md "江苏到BandwagonHost各机房的Ping测试 20180804")
    * [Digital Ocean](/digitalocean/isp/jiangsu/20180804-digitalocean-isp-jiangsu.md "江苏到Digital Ocean各机房的Ping测试 20180804")
    * [Linode](/linode/isp/jiangsu/20180804-linode-isp-jiangsu.md "江苏到Linode各机房的Ping测试 20180804")



本文最初发表于[江苏到Vultr各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-vultr-isp-jiangsu.html)
