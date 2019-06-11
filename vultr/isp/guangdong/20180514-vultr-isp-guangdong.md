#  广东到Vultr各机房的测速数据（20180514） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![广东到Vultr各机房的测速数据（20180514）](/images/thumbnails/Guangdong_to_vultr.png)

本文的数据视角为 **广东到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在广东且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180514广东到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点1158个，其中超时点30个。连通概况如下：大陆线路响应均值为255毫秒，最快的三个机房所在地为东京、新加坡、西雅图，最慢的三个为迈阿密、伦敦、亚特兰大；巴黎、伦敦、洛杉矶、达拉斯、悉尼等14处有响应超时情况；达拉斯、洛杉矶、亚特兰大、迈阿密、硅谷丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 广东图表数据

![大陆省份广东到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180514](/images/pingtests/vultr_20180514/plot_isp_guangdong_vultr_20180514.png)

### 全部运营商

**广东全部运营商到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 81个 | 1个 | 105ms | 4%  
新加坡 | 83个 | 1个 | 138ms | 2%  
西雅图 | 76个 | 1个 | 198ms | 1%  
悉尼 | 74个 | 2个 | 206ms | 1%  
洛杉矶 | 79个 | 3个 | 246ms | 15%  
硅谷 | 78个 | 2个 | 247ms | 7%  
均值 | 1158个 | 30个 | 255ms | 6%  
芝加哥 | 79个 | 2个 | 271ms | 2%  
阿姆斯特丹 | 75个 | 1个 | 285ms | 3%  
法兰克福 | 75个 | 2个 | 288ms | 2%  
新泽西 | 78个 | 2个 | 289ms | 1%  
达拉斯 | 76个 | 3个 | 300ms | 16%  
巴黎 | 78个 | 5个 | 302ms | 2%  
迈阿密 | 75个 | 1个 | 316ms | 9%  
伦敦 | 75个 | 4个 | 317ms | 4%  
亚特兰大 | 76个 | 0 | 330ms | 15%  
  
**简评：** 本表展示了广东的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻广东，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **东京、新加坡、西雅图、悉尼** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**广东电信到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 43个 | 1个 | 144ms | 9%  
新加坡 | 44个 | 1个 | 188ms | 5%  
西雅图 | 43个 | 1个 | 224ms | 2%  
悉尼 | 43个 | 2个 | 235ms | 3%  
洛杉矶 | 44个 | 3个 | 263ms | 15%  
硅谷 | 42个 | 1个 | 275ms | 2%  
均值 | 626个 | 22个 | 268ms | 5%  
芝加哥 | 42个 | 1个 | 293ms | 0  
阿姆斯特丹 | 39个 | 0 | 275ms | 2%  
法兰克福 | 40个 | 2个 | 276ms | 1%  
新泽西 | 42个 | 0 | 336ms | 1%  
达拉斯 | 42个 | 3个 | 298ms | 8%  
巴黎 | 42个 | 4个 | 259ms | 0  
迈阿密 | 41个 | 1个 | 349ms | 10%  
伦敦 | 38个 | 2个 | 328ms | 0  
亚特兰大 | 41个 | 0 | 326ms | 10%  
  
**简评：** 如果你是来自广东的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡、西雅图、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**广东联通到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 19个 | 0 | 94ms | 2%  
新加坡 | 17个 | 0 | 143ms | 0  
西雅图 | 16个 | 0 | 201ms | 2%  
悉尼 | 17个 | 0 | 191ms | 0  
洛杉矶 | 16个 | 0 | 222ms | 7%  
硅谷 | 18个 | 0 | 237ms | 2%  
均值 | 259个 | 2个 | 263ms | 6%  
芝加哥 | 17个 | 0 | 296ms | 7%  
阿姆斯特丹 | 18个 | 1个 | 335ms | 7%  
法兰克福 | 17个 | 0 | 347ms | 6%  
新泽西 | 18个 | 0 | 285ms | 2%  
达拉斯 | 17个 | 0 | 266ms | 13%  
巴黎 | 16个 | 1个 | 351ms | 6%  
迈阿密 | 18个 | 0 | 302ms | 11%  
伦敦 | 17个 | 0 | 371ms | 14%  
亚特兰大 | 18个 | 0 | 281ms | 4%  
  
**简评：** 如果你是来自广东的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、悉尼、西雅图、硅谷** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **洛杉矶** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**广东移动到Vultr各机房的测速数据 [20180514]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 19个 | 0 | 78ms | 0  
新加坡 | 22个 | 0 | 83ms | 0  
西雅图 | 17个 | 0 | 168ms | 0  
悉尼 | 14个 | 0 | 192ms | 0  
洛杉矶 | 19个 | 0 | 251ms | 24%  
硅谷 | 18个 | 1个 | 228ms | 16%  
均值 | 273个 | 6个 | 234ms | 6%  
芝加哥 | 20个 | 1个 | 222ms | 0  
阿姆斯特丹 | 18个 | 0 | 245ms | 0  
法兰克福 | 18个 | 0 | 240ms | 0  
新泽西 | 18个 | 2个 | 246ms | 0  
达拉斯 | 17个 | 0 | 336ms | 26%  
巴黎 | 20个 | 0 | 296ms | 0  
迈阿密 | 16个 | 0 | 297ms | 6%  
伦敦 | 20个 | 2个 | 251ms | 0  
亚特兰大 | 17个 | 0 | 383ms | 31%  
  
**简评：** 如果你是来自广东的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、西雅图、悉尼、芝加哥、法兰克福、阿姆斯特丹、新泽西** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **硅谷** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
  * 广东到Vultr各机房的 _其他近期报告_ ： 
    * [20180527](/vultr/isp/guangdong/20180527-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/guangdong/20180622-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/guangdong/20180804-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/guangdong/20180918-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180918")
  * 本期报告：广东到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/guangdong/20180514-bandwagon-isp-guangdong.md "广东到BandwagonHost各机房的Ping测试 20180514")
    * [Digital Ocean](/digitalocean/isp/guangdong/20180514-digitalocean-isp-guangdong.md "广东到Digital Ocean各机房的Ping测试 20180514")
    * [Linode](/linode/isp/guangdong/20180514-linode-isp-guangdong.md "广东到Linode各机房的Ping测试 20180514")



本文最初发表于[广东到Vultr各机房的测速数据（20180514）](https://vps123.top/pingtest/20180514-vultr-isp-guangdong.html)
