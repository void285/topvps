#  安徽到Vultr各机房的测速数据（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![安徽到Vultr各机房的测速数据（20180514）](/images/thumbnails/Anhui_to_vultr.png)

本文的数据视角为 **安徽到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在安徽且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514安徽到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点573个，其中超时点7个。连通概况如下：大陆线路响应均值为256毫秒，最快的三个机房所在地为东京、新加坡、西雅图，最慢的三个为伦敦、迈阿密、亚特兰大；西雅图、阿姆斯特丹、芝加哥、新泽西、伦敦等7处有响应超时情况；迈阿密、亚特兰大、达拉斯、新泽西、伦敦等10处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 安徽图表数据

![大陆省份安徽到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_isp_anhui_vultr_20180514.png)

### 全部运营商

安徽全部运营商到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 41个 | 0 | 119ms | 8% | 法兰克福 | 32个 | 0 | 272ms | 3%  
新加坡 | 39个 | 0 | 154ms | 7% | 巴黎 | 37个 | 0 | 278ms | 1%  
西雅图 | 37个 | 1个 | 220ms | 2% | 芝加哥 | 39个 | 1个 | 288ms | 10%  
洛杉矶 | 37个 | 0 | 227ms | 10% | 达拉斯 | 38个 | 0 | 294ms | 14%  
悉尼 | 40个 | 0 | 235ms | 2% | 新泽西 | 42个 | 1个 | 295ms | 13%  
硅谷 | 42个 | 0 | 249ms | 10% | 伦敦 | 37个 | 1个 | 311ms | 11%  
均值 | 573个 | 7个 | 256ms | 8% | 迈阿密 | 39个 | 1个 | 318ms | 16%  
阿姆斯特丹 | 37个 | 1个 | 268ms | 2% | 亚特兰大 | 36个 | 1个 | 323ms | 15%  
  
简评：本表展示了安徽的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻安徽，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **西雅图、悉尼** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

安徽电信到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 18个 | 0 | 104ms | 8% | 法兰克福 | 17个 | 0 | 241ms | 0  
新加坡 | 17个 | 0 | 163ms | 9% | 巴黎 | 14个 | 0 | 248ms | 0  
西雅图 | 14个 | 0 | 206ms | 1% | 芝加哥 | 15个 | 0 | 295ms | 0  
洛杉矶 | 14个 | 0 | 208ms | 1% | 达拉斯 | 17个 | 0 | 247ms | 2%  
悉尼 | 18个 | 0 | 233ms | 0 | 新泽西 | 19个 | 0 | 308ms | 1%  
硅谷 | 19个 | 0 | 254ms | 2% | 伦敦 | 17个 | 0 | 308ms | 0  
均值 | 243个 | 0 | 240ms | 2% | 迈阿密 | 16个 | 0 | 305ms | 1%  
阿姆斯特丹 | 15个 | 0 | 225ms | 0 | 亚特兰大 | 13个 | 0 | 303ms | 1%  
  
简评：如果你是来自安徽的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **西雅图、洛杉矶、阿姆斯特丹、悉尼、法兰克福、达拉斯、巴黎** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

安徽联通到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 8个 | 0 | 137ms | 14% | 法兰克福 | 6个 | 0 | 333ms | 7%  
新加坡 | 7个 | 0 | 176ms | 9% | 巴黎 | 9个 | 0 | 304ms | 4%  
西雅图 | 9个 | 0 | 219ms | 4% | 芝加哥 | 9个 | 1个 | 293ms | 26%  
洛杉矶 | 9个 | 0 | 234ms | 10% | 达拉斯 | 7个 | 0 | 301ms | 21%  
悉尼 | 9个 | 0 | 241ms | 5% | 新泽西 | 8个 | 1个 | 292ms | 31%  
硅谷 | 8个 | 0 | 234ms | 7% | 伦敦 | 8个 | 1个 | 315ms | 26%  
均值 | 121个 | 6个 | 268ms | 14% | 迈阿密 | 8个 | 1个 | 325ms | 29%  
阿姆斯特丹 | 8个 | 1个 | 314ms | 6% | 亚特兰大 | 8个 | 1个 | 302ms | 17%  
  
简评：如果你是来自安徽的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **西雅图、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡、洛杉矶、硅谷** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

安徽移动到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 15个 | 0 | 115ms | 3% | 法兰克福 | 9个 | 0 | 243ms | 1%  
新加坡 | 15个 | 0 | 123ms | 3% | 巴黎 | 14个 | 0 | 282ms | 1%  
西雅图 | 14个 | 1个 | 234ms | 2% | 芝加哥 | 15个 | 0 | 277ms | 6%  
洛杉矶 | 14个 | 0 | 241ms | 20% | 达拉斯 | 14个 | 0 | 333ms | 18%  
悉尼 | 13个 | 0 | 232ms | 1% | 新泽西 | 15个 | 0 | 287ms | 8%  
硅谷 | 15个 | 0 | 259ms | 19% | 伦敦 | 12个 | 0 | 310ms | 7%  
均值 | 209个 | 1个 | 259ms | 9% | 迈阿密 | 15个 | 0 | 325ms | 18%  
阿姆斯特丹 | 14个 | 0 | 264ms | 1% | 亚特兰大 | 15个 | 0 | 364ms | 27%  
  
简评：如果你是来自安徽的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、悉尼、西雅图、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **洛杉矶** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180514) 
    * [全部](https://vps123.top/pingtests/20180514 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180514 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180514 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180514 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
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
    * [新疆](/vultr/isp/xinjiang/20180514-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180514")
    * [云南](/vultr/isp/yunnan/20180514-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180514")
    * [浙江](/vultr/isp/zhejiang/20180514-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180514")
  * 安徽到Vultr各机房的 _其他近期报告_ ： 
    * [20180527](/vultr/isp/anhui/20180527-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/anhui/20180622-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/anhui/20180804-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/anhui/20180918-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180918")
  * 本期报告：安徽到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/anhui/20180514-bandwagon-isp-anhui.md "安徽到BandwagonHost各机房的Ping测试 20180514")
    * [Digital Ocean](/digitalocean/isp/anhui/20180514-digitalocean-isp-anhui.md "安徽到Digital Ocean各机房的Ping测试 20180514")
    * [Linode](/linode/isp/anhui/20180514-linode-isp-anhui.md "安徽到Linode各机房的Ping测试 20180514")



本文最初发表于[安徽到Vultr各机房的测速数据（20180514）](https://vps123.top/pingtest/20180514-vultr-isp-anhui.html)
