#  云南到Vultr各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![云南到Vultr各机房的测速数据（20180622）](/images/thumbnails/Yunnan_to_vultr.png)

本文的数据视角为 **云南到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在云南且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点329个，其中超时点130个。连通概况如下：大陆线路响应均值为283毫秒，最快的三个机房所在地为东京、洛杉矶、西雅图，最慢的三个为芝加哥、阿姆斯特丹、悉尼；洛杉矶、迈阿密、东京、西雅图、新加坡等13处有响应超时情况；芝加哥、亚特兰大、迈阿密、新加坡、东京等6处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 云南图表数据

![大陆省份云南到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_isp_yunnan_vultr_20180622.png)

### 全部运营商

云南全部运营商到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 25个 | 10个 | 183ms | 7% | 达拉斯 | 24个 | 10个 | 284ms | 0  
洛杉矶 | 22个 | 11个 | 212ms | 1% | 亚特兰大 | 24个 | 10个 | 319ms | 27%  
西雅图 | 24个 | 10个 | 238ms | 1% | 迈阿密 | 25个 | 11个 | 321ms | 26%  
硅谷 | 14个 | 0 | 254ms | 3% | 伦敦 | 23个 | 9个 | 331ms | 5%  
法兰克福 | 14个 | 0 | 257ms | 0 | 新泽西 | 22个 | 10个 | 332ms | 0  
新加坡 | 22个 | 10个 | 266ms | 9% | 芝加哥 | 25个 | 10个 | 332ms | 29%  
巴黎 | 22个 | 10个 | 281ms | 0 | 阿姆斯特丹 | 21个 | 9个 | 335ms | 1%  
均值 | 329个 | 130个 | 283ms | 13% | 悉尼 | 22个 | 10个 | 346ms | 2%  
  
简评：本表展示了云南的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻云南，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶、西雅图** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

云南电信到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 13个 | 3个 | 263ms | 17% | 达拉斯 | 13个 | 3个 | 297ms | 0  
洛杉矶 | 12个 | 4个 | 218ms | 1% | 亚特兰大 | 13个 | 4个 | 305ms | 0  
西雅图 | 13个 | 3个 | 252ms | 3% | 迈阿密 | 13个 | 4个 | 318ms | 1%  
硅谷 | 9个 | 0 | 266ms | 5% | 伦敦 | 12个 | 2个 | 330ms | 0  
法兰克福 | 9个 | 0 | 270ms | 0 | 新泽西 | 11个 | 3个 | 352ms | 1%  
新加坡 | 12个 | 3个 | 316ms | 12% | 芝加哥 | 13个 | 3个 | 313ms | 2%  
巴黎 | 12个 | 3个 | 273ms | 0 | 阿姆斯特丹 | 12个 | 3个 | 327ms | 0  
均值 | 179个 | 41个 | 300ms | 3% | 悉尼 | 12个 | 3个 | 406ms | 4%  
  
简评：如果你是来自云南的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

云南联通到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 4个 | 3个 | 99ms | 0 | 达拉斯 | 3个 | 3个 | - | -  
洛杉矶 | 3个 | 3个 | - | - | 亚特兰大 | 3个 | 2个 | 336ms | 65%  
西雅图 | 3个 | 3个 | - | - | 迈阿密 | 4个 | 3个 | 303ms | 62%  
硅谷 | 1个 | 0 | 294ms | 3% | 伦敦 | 3个 | 3个 | - | -  
法兰克福 | 1个 | 0 | 256ms | 0 | 新泽西 | 3个 | 3个 | - | -  
新加坡 | 3个 | 3个 | - | - | 芝加哥 | 4个 | 3个 | 362ms | 66%  
巴黎 | 3个 | 3个 | - | - | 阿姆斯特丹 | 3个 | 3个 | - | -  
均值 | 44个 | 38个 | 275ms | 32% | 悉尼 | 3个 | 3个 | - | -  
  
简评：如果你是来自云南的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

云南移动到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 8个 | 4个 | 188ms | 5% | 达拉斯 | 8个 | 4个 | 271ms | 0  
洛杉矶 | 7个 | 4个 | 205ms | 0 | 亚特兰大 | 8个 | 4个 | 316ms | 17%  
西雅图 | 8个 | 4个 | 223ms | 0 | 迈阿密 | 8个 | 4个 | 342ms | 16%  
硅谷 | 4个 | 0 | 201ms | 0 | 伦敦 | 8个 | 4个 | 333ms | 11%  
法兰克福 | 4个 | 0 | 247ms | 0 | 新泽西 | 8个 | 4个 | 313ms | 0  
新加坡 | 7个 | 4个 | 217ms | 6% | 芝加哥 | 8个 | 4个 | 322ms | 19%  
巴黎 | 7个 | 4个 | 289ms | 0 | 阿姆斯特丹 | 6个 | 3个 | 343ms | 1%  
均值 | 106个 | 51个 | 273ms | 5% | 悉尼 | 7个 | 4个 | 287ms | 0  
  
简评：如果你是来自云南的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、硅谷、洛杉矶、西雅图、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **新加坡** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180622 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180622 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180622-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180622")
    * [北京](/vultr/isp/beijing/20180622-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180622")
    * [大陆](/vultr/isp/china/20180622-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180622")
    * [重庆](/vultr/isp/chongqing/20180622-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180622")
    * [福建](/vultr/isp/fujian/20180622-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180622")
    * [甘肃](/vultr/isp/gansu/20180622-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180622")
    * [广东](/vultr/isp/guangdong/20180622-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180622")
    * [广西](/vultr/isp/guangxi/20180622-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180622")
    * [贵州](/vultr/isp/guizhou/20180622-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180622")
    * [海南](/vultr/isp/hainan/20180622-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180622")
    * [河北](/vultr/isp/hebei/20180622-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180622")
    * [黑龙江](/vultr/isp/heilongjiang/20180622-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180622")
    * [河南](/vultr/isp/henan/20180622-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180622")
    * [湖北](/vultr/isp/hubei/20180622-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180622")
    * [湖南](/vultr/isp/hunan/20180622-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180622")
    * [内蒙古](/vultr/isp/innermongolia/20180622-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180622")
    * [江苏](/vultr/isp/jiangsu/20180622-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180622")
    * [江西](/vultr/isp/jiangxi/20180622-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180622")
    * [吉林](/vultr/isp/jilin/20180622-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180622")
    * [辽宁](/vultr/isp/liaoning/20180622-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180622")
    * [宁夏](/vultr/isp/ningxia/20180622-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180622")
    * [青海](/vultr/isp/qinghai/20180622-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180622")
    * [山西](/vultr/isp/shan1xi/20180622-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180622")
    * [陕西](/vultr/isp/shan3xi/20180622-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180622")
    * [山东](/vultr/isp/shandong/20180622-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180622")
    * [上海](/vultr/isp/shanghai/20180622-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180622")
    * [四川](/vultr/isp/sichuan/20180622-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180622")
    * [天津](/vultr/isp/tianjin/20180622-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180622")
    * [西藏](/vultr/isp/tibet/20180622-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180622")
    * [新疆](/vultr/isp/xinjiang/20180622-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180622")
    * [浙江](/vultr/isp/zhejiang/20180622-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180622")
  * 云南到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/yunnan/20180514-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/yunnan/20180527-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180527")
    * [20180804](/vultr/isp/yunnan/20180804-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/yunnan/20180918-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180918")
  * 本期报告：云南到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/yunnan/20180622-bandwagon-isp-yunnan.md "云南到BandwagonHost各机房的Ping测试 20180622")
    * [Digital Ocean](/digitalocean/isp/yunnan/20180622-digitalocean-isp-yunnan.md "云南到Digital Ocean各机房的Ping测试 20180622")
    * [Linode](/linode/isp/yunnan/20180622-linode-isp-yunnan.md "云南到Linode各机房的Ping测试 20180622")



本文最初发表于[云南到Vultr各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-vultr-isp-yunnan.html)
