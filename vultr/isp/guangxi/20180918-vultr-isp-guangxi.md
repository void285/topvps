#  广西到Vultr各机房的测速数据（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![广西到Vultr各机房的测速数据（20180918）](/images/thumbnails/Guangxi_to_vultr.png)

本文的数据视角为 **广西到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在广西且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918广西到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点910个，其中超时点2个。连通概况如下：大陆线路响应均值为239毫秒，最快的三个机房所在地为东京、新加坡、硅谷，最慢的三个为巴黎、伦敦、阿姆斯特丹；东京、洛杉矶有响应超时情况；阿姆斯特丹、巴黎、亚特兰大、法兰克福、洛杉矶等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 广西图表数据

![大陆省份广西到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_isp_guangxi_vultr_20180918.png)

### 全部运营商

广西全部运营商到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 59个 | 1个 | 119ms | 1% | 悉尼 | 62个 | 0 | 243ms | 0  
新加坡 | 62个 | 0 | 164ms | 1% | 亚特兰大 | 59个 | 0 | 268ms | 8%  
硅谷 | 63个 | 0 | 204ms | 2% | 新泽西 | 64个 | 0 | 269ms | 3%  
洛杉矶 | 59个 | 1个 | 207ms | 7% | 迈阿密 | 60个 | 0 | 277ms | 7%  
西雅图 | 63个 | 0 | 218ms | 6% | 法兰克福 | 60个 | 0 | 277ms | 7%  
达拉斯 | 59个 | 0 | 227ms | 1% | 巴黎 | 63个 | 0 | 283ms | 8%  
均值 | 910个 | 2个 | 239ms | 4% | 伦敦 | 59个 | 0 | 287ms | 3%  
芝加哥 | 59个 | 0 | 241ms | 0 | 阿姆斯特丹 | 59个 | 0 | 295ms | 9%  
  
简评：本表展示了广西的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻广西，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **东京、新加坡、硅谷、达拉斯、芝加哥、悉尼** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

广西电信到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 22个 | 0 | 169ms | 2% | 悉尼 | 24个 | 0 | 298ms | 0  
新加坡 | 26个 | 0 | 238ms | 2% | 亚特兰大 | 22个 | 0 | 302ms | 14%  
硅谷 | 24个 | 0 | 220ms | 5% | 新泽西 | 25个 | 0 | 263ms | 0  
洛杉矶 | 23个 | 1个 | 243ms | 16% | 迈阿密 | 23个 | 0 | 308ms | 12%  
西雅图 | 25个 | 0 | 257ms | 15% | 法兰克福 | 23个 | 0 | 281ms | 6%  
达拉斯 | 22个 | 0 | 220ms | 0 | 巴黎 | 25个 | 0 | 293ms | 13%  
均值 | 352个 | 1个 | 262ms | 6% | 伦敦 | 22个 | 0 | 280ms | 0  
芝加哥 | 22个 | 0 | 244ms | 0 | 阿姆斯特丹 | 24个 | 0 | 306ms | 5%  
  
简评：如果你是来自广西的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、硅谷、达拉斯、新加坡、芝加哥** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **洛杉矶** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

广西联通到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 16个 | 1个 | 108ms | 1% | 悉尼 | 16个 | 0 | 257ms | 0  
新加坡 | 14个 | 0 | 170ms | 0 | 亚特兰大 | 16个 | 0 | 270ms | 8%  
硅谷 | 16个 | 0 | 206ms | 1% | 新泽西 | 16个 | 0 | 275ms | 10%  
洛杉矶 | 16个 | 0 | 197ms | 3% | 迈阿密 | 16个 | 0 | 264ms | 6%  
西雅图 | 16个 | 0 | 220ms | 2% | 法兰克福 | 16个 | 0 | 300ms | 6%  
达拉斯 | 16个 | 0 | 221ms | 3% | 巴黎 | 16个 | 0 | 301ms | 3%  
均值 | 235个 | 1个 | 246ms | 4% | 伦敦 | 16个 | 0 | 333ms | 8%  
芝加哥 | 16个 | 0 | 237ms | 0 | 阿姆斯特丹 | 13个 | 0 | 331ms | 15%  
  
简评：如果你是来自广西的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、洛杉矶、硅谷、西雅图、达拉斯、芝加哥** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

广西移动到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 21个 | 0 | 81ms | 1% | 悉尼 | 22个 | 0 | 175ms | 0  
新加坡 | 22个 | 0 | 83ms | 0 | 亚特兰大 | 21个 | 0 | 232ms | 1%  
硅谷 | 23个 | 0 | 188ms | 0 | 新泽西 | 23个 | 0 | 269ms | 1%  
洛杉矶 | 20个 | 0 | 181ms | 0 | 迈阿密 | 21个 | 0 | 261ms | 2%  
西雅图 | 22个 | 0 | 178ms | 0 | 法兰克福 | 21个 | 0 | 250ms | 9%  
达拉斯 | 21个 | 0 | 238ms | 1% | 巴黎 | 22个 | 0 | 254ms | 9%  
均值 | 323个 | 0 | 209ms | 2% | 伦敦 | 21个 | 0 | 249ms | 1%  
芝加哥 | 21个 | 0 | 241ms | 2% | 阿姆斯特丹 | 22个 | 0 | 249ms | 7%  
  
简评：如果你是来自广西的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、悉尼、西雅图、洛杉矶、硅谷、亚特兰大、达拉斯、芝加哥、伦敦** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **阿姆斯特丹、法兰克福** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [贵州](/vultr/isp/guizhou/20180918-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180918")
    * [海南](/vultr/isp/hainan/20180918-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180918")
    * [河北](/vultr/isp/hebei/20180918-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180918")
    * [黑龙江](/vultr/isp/heilongjiang/20180918-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180918")
    * [河南](/vultr/isp/henan/20180918-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180918")
    * [湖北](/vultr/isp/hubei/20180918-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180918")
    * [湖南](/vultr/isp/hunan/20180918-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180918")
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
  * 广西到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/guangxi/20180514-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/guangxi/20180527-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/guangxi/20180622-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/guangxi/20180804-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180804")
  * 本期报告：广西到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/guangxi/20180918-bandwagon-isp-guangxi.md "广西到BandwagonHost各机房的Ping测试 20180918")
    * [Digital Ocean](/digitalocean/isp/guangxi/20180918-digitalocean-isp-guangxi.md "广西到Digital Ocean各机房的Ping测试 20180918")
    * [Linode](/linode/isp/guangxi/20180918-linode-isp-guangxi.md "广西到Linode各机房的Ping测试 20180918")



本文最初发表于[广西到Vultr各机房的测速数据（20180918）](https://vps123.top/pingtest/20180918-vultr-isp-guangxi.html)
