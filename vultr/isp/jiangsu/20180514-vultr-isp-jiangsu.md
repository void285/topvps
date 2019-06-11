#  江苏到Vultr各机房的测速数据（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![江苏到Vultr各机房的测速数据（20180514）](/images/thumbnails/Jiangsu_to_vultr.png)

本文的数据视角为 **江苏到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在江苏且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514江苏到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点910个，其中超时点27个。连通概况如下：大陆线路响应均值为253毫秒，最快的三个机房所在地为东京、新加坡、西雅图，最慢的三个为伦敦、法兰克福、阿姆斯特丹；新加坡、硅谷、东京、悉尼、芝加哥等15处有响应超时情况；迈阿密、亚特兰大、新泽西、芝加哥、伦敦等13处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 江苏图表数据

![大陆省份江苏到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_isp_jiangsu_vultr_20180514.png)

### 全部运营商

江苏全部运营商到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 64个 | 2个 | 119ms | 8% | 芝加哥 | 58个 | 2个 | 278ms | 17%  
新加坡 | 63个 | 5个 | 169ms | 6% | 亚特兰大 | 61个 | 2个 | 280ms | 19%  
西雅图 | 63个 | 1个 | 211ms | 4% | 新泽西 | 62个 | 2个 | 291ms | 17%  
洛杉矶 | 63个 | 1个 | 215ms | 9% | 迈阿密 | 61个 | 1个 | 300ms | 19%  
悉尼 | 62个 | 2个 | 228ms | 2% | 巴黎 | 63个 | 1个 | 303ms | 9%  
达拉斯 | 58个 | 1个 | 238ms | 13% | 伦敦 | 57个 | 2个 | 304ms | 15%  
硅谷 | 62个 | 3个 | 243ms | 11% | 法兰克福 | 60个 | 1个 | 307ms | 12%  
均值 | 910个 | 27个 | 253ms | 11% | 阿姆斯特丹 | 53个 | 1个 | 312ms | 10%  
  
简评：本表展示了江苏的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻江苏，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **西雅图、悉尼** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

江苏电信到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 30个 | 2个 | 106ms | 7% | 芝加哥 | 25个 | 1个 | 284ms | 1%  
新加坡 | 29个 | 4个 | 171ms | 5% | 亚特兰大 | 30个 | 1个 | 282ms | 2%  
西雅图 | 30个 | 1个 | 207ms | 1% | 新泽西 | 29个 | 1个 | 322ms | 1%  
洛杉矶 | 30个 | 1个 | 199ms | 0 | 迈阿密 | 29个 | 1个 | 312ms | 2%  
悉尼 | 29个 | 2个 | 232ms | 1% | 巴黎 | 31个 | 1个 | 243ms | 0  
达拉斯 | 28个 | 1个 | 216ms | 0 | 伦敦 | 28个 | 2个 | 324ms | 0  
硅谷 | 29个 | 2个 | 253ms | 1% | 法兰克福 | 30个 | 1个 | 253ms | 4%  
均值 | 433个 | 22个 | 242ms | 2% | 阿姆斯特丹 | 26个 | 1个 | 236ms | 0  
  
简评：如果你是来自江苏的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡、洛杉矶、西雅图、达拉斯、悉尼、阿姆斯特丹、巴黎** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

江苏联通到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 18个 | 0 | 145ms | 18% | 芝加哥 | 18个 | 1个 | 270ms | 37%  
新加坡 | 18个 | 1个 | 214ms | 12% | 亚特兰大 | 16个 | 0 | 256ms | 33%  
西雅图 | 17个 | 0 | 194ms | 5% | 新泽西 | 16个 | 1个 | 269ms | 44%  
洛杉矶 | 18个 | 0 | 208ms | 9% | 迈阿密 | 17个 | 0 | 287ms | 42%  
悉尼 | 17个 | 0 | 230ms | 5% | 巴黎 | 17个 | 0 | 346ms | 9%  
达拉斯 | 16个 | 0 | 240ms | 15% | 伦敦 | 15个 | 0 | 327ms | 44%  
硅谷 | 16个 | 0 | 219ms | 5% | 法兰克福 | 17个 | 0 | 347ms | 11%  
均值 | 247个 | 3个 | 262ms | 20% | 阿姆斯特丹 | 11个 | 0 | 369ms | 10%  
  
简评：如果你是来自江苏的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **西雅图、硅谷、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、洛杉矶、新加坡、达拉斯** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

江苏移动到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 16个 | 0 | 105ms | 0 | 芝加哥 | 15个 | 0 | 280ms | 13%  
新加坡 | 16个 | 0 | 123ms | 0 | 亚特兰大 | 15个 | 1个 | 302ms | 21%  
西雅图 | 16个 | 0 | 232ms | 6% | 新泽西 | 17个 | 0 | 282ms | 6%  
洛杉矶 | 15个 | 0 | 237ms | 18% | 迈阿密 | 15个 | 0 | 300ms | 14%  
悉尼 | 16个 | 0 | 222ms | 1% | 巴黎 | 15个 | 0 | 321ms | 18%  
达拉斯 | 14个 | 0 | 257ms | 24% | 伦敦 | 14个 | 0 | 260ms | 0  
硅谷 | 17个 | 1个 | 256ms | 27% | 法兰克福 | 13个 | 0 | 323ms | 22%  
均值 | 230个 | 2个 | 254ms | 12% | 阿姆斯特丹 | 16个 | 0 | 331ms | 19%  
  
简评：如果你是来自江苏的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **西雅图、洛杉矶** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
  * 江苏到Vultr各机房的 _其他近期报告_ ： 
    * [20180527](/vultr/isp/jiangsu/20180527-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/jiangsu/20180622-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/jiangsu/20180804-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/jiangsu/20180918-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180918")
  * 本期报告：江苏到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/jiangsu/20180514-bandwagon-isp-jiangsu.md "江苏到BandwagonHost各机房的Ping测试 20180514")
    * [Digital Ocean](/digitalocean/isp/jiangsu/20180514-digitalocean-isp-jiangsu.md "江苏到Digital Ocean各机房的Ping测试 20180514")
    * [Linode](/linode/isp/jiangsu/20180514-linode-isp-jiangsu.md "江苏到Linode各机房的Ping测试 20180514")



本文最初发表于[江苏到Vultr各机房的测速数据（20180514）](https://vps123.top/pingtest/20180514-vultr-isp-jiangsu.html)
