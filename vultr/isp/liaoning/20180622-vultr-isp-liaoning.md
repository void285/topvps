#  辽宁到Vultr各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![辽宁到Vultr各机房的测速数据（20180622）](/images/thumbnails/Liaoning_to_vultr.png)

本文的数据视角为 **辽宁到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在辽宁且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点519个，其中超时点12个。连通概况如下：大陆线路响应均值为267毫秒，最快的三个机房所在地为东京、硅谷、西雅图，最慢的三个为新泽西、阿姆斯特丹、悉尼；法兰克福、新加坡、东京、洛杉矶、芝加哥等8处有响应超时情况；芝加哥、亚特兰大、迈阿密、伦敦、法兰克福等8处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 辽宁图表数据

![大陆省份辽宁到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_isp_liaoning_vultr_20180622.png)

### 全部运营商

辽宁全部运营商到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 35个 | 1个 | 185ms | 9% | 法兰克福 | 29个 | 4个 | 285ms | 13%  
硅谷 | 36个 | 0 | 215ms | 0 | 芝加哥 | 35个 | 1个 | 292ms | 24%  
西雅图 | 35个 | 0 | 224ms | 4% | 亚特兰大 | 34个 | 1个 | 297ms | 22%  
洛杉矶 | 36个 | 1个 | 226ms | 4% | 伦敦 | 33个 | 1个 | 301ms | 15%  
达拉斯 | 33个 | 0 | 253ms | 2% | 迈阿密 | 35个 | 0 | 308ms | 21%  
新加坡 | 36个 | 2个 | 253ms | 11% | 新泽西 | 35个 | 0 | 309ms | 3%  
巴黎 | 36个 | 0 | 266ms | 1% | 阿姆斯特丹 | 35个 | 1个 | 316ms | 2%  
均值 | 519个 | 12个 | 267ms | 9% | 悉尼 | 36个 | 0 | 316ms | 8%  
  
简评：本表展示了辽宁的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻辽宁，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **硅谷、西雅图、洛杉矶** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

辽宁电信到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 13个 | 1个 | 222ms | 16% | 法兰克福 | 10个 | 2个 | 246ms | 12%  
硅谷 | 13个 | 0 | 223ms | 1% | 芝加哥 | 13个 | 1个 | 333ms | 24%  
西雅图 | 12个 | 0 | 239ms | 3% | 亚特兰大 | 13个 | 1个 | 312ms | 20%  
洛杉矶 | 12个 | 1个 | 244ms | 3% | 伦敦 | 11个 | 1个 | 326ms | 17%  
达拉斯 | 12个 | 0 | 276ms | 2% | 迈阿密 | 13个 | 0 | 339ms | 21%  
新加坡 | 12个 | 1个 | 293ms | 18% | 新泽西 | 13个 | 0 | 345ms | 5%  
巴黎 | 12个 | 0 | 243ms | 0 | 阿姆斯特丹 | 12个 | 1个 | 326ms | 0  
均值 | 183个 | 9个 | 284ms | 10% | 悉尼 | 12个 | 0 | 372ms | 11%  
  
简评：如果你是来自辽宁的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **硅谷、西雅图、巴黎、洛杉矶** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、法兰克福** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

辽宁联通到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 13个 | 0 | 190ms | 5% | 法兰克福 | 11个 | 2个 | 308ms | 29%  
硅谷 | 15个 | 0 | 193ms | 0 | 芝加哥 | 13个 | 0 | 275ms | 44%  
西雅图 | 14个 | 0 | 208ms | 0 | 亚特兰大 | 13个 | 0 | 288ms | 42%  
洛杉矶 | 16个 | 0 | 205ms | 0 | 伦敦 | 13个 | 0 | 283ms | 28%  
达拉斯 | 12个 | 0 | 223ms | 0 | 迈阿密 | 13个 | 0 | 277ms | 39%  
新加坡 | 16个 | 1个 | 287ms | 5% | 新泽西 | 13个 | 0 | 283ms | 0  
巴黎 | 16个 | 0 | 262ms | 0 | 阿姆斯特丹 | 15个 | 0 | 278ms | 0  
均值 | 209个 | 3个 | 255ms | 12% | 悉尼 | 16个 | 0 | 295ms | 3%  
  
简评：如果你是来自辽宁的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、硅谷、洛杉矶、西雅图、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

辽宁移动到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 9个 | 0 | 142ms | 7% | 法兰克福 | 8个 | 0 | 300ms | 0  
硅谷 | 8个 | 0 | 229ms | 1% | 芝加哥 | 9个 | 0 | 270ms | 5%  
西雅图 | 9个 | 0 | 224ms | 9% | 亚特兰大 | 8个 | 0 | 291ms | 2%  
洛杉矶 | 8个 | 0 | 228ms | 9% | 伦敦 | 9个 | 0 | 294ms | 0  
达拉斯 | 9个 | 0 | 261ms | 5% | 迈阿密 | 9个 | 0 | 307ms | 4%  
新加坡 | 8个 | 0 | 178ms | 11% | 新泽西 | 9个 | 0 | 300ms | 4%  
巴黎 | 8个 | 0 | 293ms | 3% | 阿姆斯特丹 | 8个 | 0 | 343ms | 7%  
均值 | 127个 | 0 | 262ms | 5% | 悉尼 | 8个 | 0 | 282ms | 10%  
  
简评：如果你是来自辽宁的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **硅谷** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡、西雅图、洛杉矶** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [云南](/vultr/isp/yunnan/20180622-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180622")
    * [浙江](/vultr/isp/zhejiang/20180622-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180622")
  * 辽宁到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/liaoning/20180514-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/liaoning/20180527-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180527")
    * [20180804](/vultr/isp/liaoning/20180804-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/liaoning/20180918-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180918")
  * 本期报告：辽宁到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/liaoning/20180622-bandwagon-isp-liaoning.md "辽宁到BandwagonHost各机房的Ping测试 20180622")
    * [Digital Ocean](/digitalocean/isp/liaoning/20180622-digitalocean-isp-liaoning.md "辽宁到Digital Ocean各机房的Ping测试 20180622")
    * [Linode](/linode/isp/liaoning/20180622-linode-isp-liaoning.md "辽宁到Linode各机房的Ping测试 20180622")



本文最初发表于[辽宁到Vultr各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-vultr-isp-liaoning.html)
