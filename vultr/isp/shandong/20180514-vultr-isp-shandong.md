#  山东到Vultr各机房的测速数据（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![山东到Vultr各机房的测速数据（20180514）](/images/thumbnails/Shandong_to_vultr.png)

本文的数据视角为 **山东到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在山东且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514山东到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点762个，其中超时点20个。连通概况如下：大陆线路响应均值为271毫秒，最快的三个机房所在地为东京、新加坡、洛杉矶，最慢的三个为阿姆斯特丹、巴黎、法兰克福；东京、硅谷、芝加哥、迈阿密、阿姆斯特丹等15处有响应超时情况；达拉斯、东京、洛杉矶、亚特兰大、迈阿密等12处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 山东图表数据

![大陆省份山东到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_isp_shandong_vultr_20180514.png)

### 全部运营商

山东全部运营商到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 50个 | 2个 | 154ms | 14% | 芝加哥 | 48个 | 2个 | 290ms | 8%  
新加坡 | 50个 | 1个 | 186ms | 10% | 伦敦 | 52个 | 1个 | 303ms | 4%  
洛杉矶 | 52个 | 1个 | 222ms | 14% | 新泽西 | 52个 | 1个 | 313ms | 2%  
西雅图 | 49个 | 1个 | 223ms | 11% | 亚特兰大 | 53个 | 1个 | 313ms | 13%  
硅谷 | 53个 | 2个 | 242ms | 10% | 迈阿密 | 52个 | 2个 | 313ms | 11%  
悉尼 | 51个 | 1个 | 250ms | 8% | 阿姆斯特丹 | 49个 | 2个 | 315ms | 4%  
均值 | 762个 | 20个 | 271ms | 9% | 巴黎 | 49个 | 1个 | 318ms | 5%  
达拉斯 | 52个 | 1个 | 275ms | 17% | 法兰克福 | 50个 | 1个 | 320ms | 5%  
  
简评：本表展示了山东的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻山东，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到，各机房所在城市的响应值、丢包率都较高（TopVPS推荐选用响应值低于250ms，丢包率在5%%以内的机房），请慎重选择；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

山东电信到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 18个 | 0 | 143ms | 18% | 芝加哥 | 13个 | 0 | 300ms | 2%  
新加坡 | 17个 | 0 | 204ms | 10% | 伦敦 | 16个 | 0 | 326ms | 4%  
洛杉矶 | 16个 | 0 | 229ms | 6% | 新泽西 | 18个 | 0 | 325ms | 3%  
西雅图 | 14个 | 0 | 217ms | 2% | 亚特兰大 | 18个 | 0 | 297ms | 4%  
硅谷 | 17个 | 0 | 257ms | 2% | 迈阿密 | 16个 | 1个 | 318ms | 6%  
悉尼 | 18个 | 0 | 255ms | 7% | 阿姆斯特丹 | 17个 | 0 | 288ms | 4%  
均值 | 247个 | 1个 | 265ms | 6% | 巴黎 | 16个 | 0 | 283ms | 5%  
达拉斯 | 17个 | 0 | 231ms | 6% | 法兰克福 | 16个 | 0 | 285ms | 4%  
  
简评：如果你是来自山东的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **西雅图** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡、洛杉矶、达拉斯** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

山东联通到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 18个 | 1个 | 201ms | 23% | 芝加哥 | 17个 | 0 | 286ms | 7%  
新加坡 | 17个 | 0 | 227ms | 16% | 伦敦 | 18个 | 0 | 333ms | 6%  
洛杉矶 | 18个 | 0 | 195ms | 7% | 新泽西 | 18个 | 0 | 269ms | 0  
西雅图 | 19个 | 0 | 193ms | 6% | 亚特兰大 | 18个 | 0 | 258ms | 5%  
硅谷 | 19个 | 0 | 211ms | 3% | 迈阿密 | 19个 | 0 | 289ms | 6%  
悉尼 | 17个 | 0 | 267ms | 17% | 阿姆斯特丹 | 16个 | 0 | 351ms | 6%  
均值 | 268个 | 1个 | 271ms | 9% | 巴黎 | 18个 | 0 | 362ms | 8%  
达拉斯 | 19个 | 0 | 247ms | 16% | 法兰克福 | 17个 | 0 | 365ms | 10%  
  
简评：如果你是来自山东的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **硅谷** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **西雅图、洛杉矶、东京、新加坡、达拉斯** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

山东移动到Vultr各机房的测速数据 [20180514] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 14个 | 1个 | 118ms | 2% | 芝加哥 | 18个 | 2个 | 285ms | 15%  
新加坡 | 16个 | 1个 | 127ms | 2% | 伦敦 | 18个 | 1个 | 249ms | 1%  
洛杉矶 | 18个 | 1个 | 243ms | 29% | 新泽西 | 16个 | 1个 | 345ms | 3%  
西雅图 | 16个 | 1个 | 260ms | 24% | 亚特兰大 | 17个 | 1个 | 383ms | 30%  
硅谷 | 17个 | 2个 | 258ms | 26% | 迈阿密 | 17个 | 1个 | 334ms | 21%  
悉尼 | 16个 | 1个 | 229ms | 1% | 阿姆斯特丹 | 16个 | 2个 | 308ms | 2%  
均值 | 247个 | 18个 | 277ms | 13% | 巴黎 | 15个 | 1个 | 310ms | 2%  
达拉斯 | 16个 | 1个 | 348ms | 30% | 法兰克福 | 17个 | 1个 | 309ms | 1%  
  
简评：如果你是来自山东的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、悉尼、伦敦** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **洛杉矶** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [上海](/vultr/isp/shanghai/20180514-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180514")
    * [四川](/vultr/isp/sichuan/20180514-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180514")
    * [天津](/vultr/isp/tianjin/20180514-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180514")
    * [西藏](/vultr/isp/tibet/20180514-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180514")
    * [新疆](/vultr/isp/xinjiang/20180514-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180514")
    * [云南](/vultr/isp/yunnan/20180514-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180514")
    * [浙江](/vultr/isp/zhejiang/20180514-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180514")
  * 山东到Vultr各机房的 _其他近期报告_ ： 
    * [20180527](/vultr/isp/shandong/20180527-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/shandong/20180622-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/shandong/20180804-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/shandong/20180918-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180918")
  * 本期报告：山东到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/shandong/20180514-bandwagon-isp-shandong.md "山东到BandwagonHost各机房的Ping测试 20180514")
    * [Digital Ocean](/digitalocean/isp/shandong/20180514-digitalocean-isp-shandong.md "山东到Digital Ocean各机房的Ping测试 20180514")
    * [Linode](/linode/isp/shandong/20180514-linode-isp-shandong.md "山东到Linode各机房的Ping测试 20180514")



本文最初发表于[山东到Vultr各机房的测速数据（20180514）](https://vps123.top/pingtest/20180514-vultr-isp-shandong.html)
