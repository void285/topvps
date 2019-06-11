#  山东到Vultr各机房的测速数据（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![山东到Vultr各机房的测速数据（20180527）](/images/thumbnails/Shandong_to_vultr.png)

本文的数据视角为 **山东到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在山东且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点786个，其中超时点21个。连通概况如下：大陆线路响应均值为260毫秒，最快的三个机房所在地为东京、洛杉矶、硅谷，最慢的三个为悉尼、阿姆斯特丹、伦敦；阿姆斯特丹、东京、新加坡、新泽西、巴黎等15处有响应超时情况；西雅图、硅谷、达拉斯、迈阿密、亚特兰大等11处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 山东图表数据

![大陆省份山东到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_isp_shandong_vultr_20180527.png)

### 全部运营商

**山东全部运营商到Vultr各机房的测速数据 [20180527]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 52个 | 2个 | 179ms | 10%  
洛杉矶 | 53个 | 1个 | 201ms | 2%  
硅谷 | 51个 | 1个 | 203ms | 13%  
西雅图 | 51个 | 1个 | 218ms | 14%  
新加坡 | 52个 | 2个 | 221ms | 11%  
达拉斯 | 52个 | 1个 | 255ms | 12%  
芝加哥 | 53个 | 1个 | 260ms | 5%  
均值 | 786个 | 21个 | 260ms | 8%  
亚特兰大 | 53个 | 1个 | 270ms | 11%  
迈阿密 | 53个 | 1个 | 271ms | 11%  
新泽西 | 52个 | 2个 | 279ms | 5%  
巴黎 | 53个 | 2个 | 299ms | 8%  
法兰克福 | 52个 | 1个 | 304ms | 2%  
悉尼 | 53个 | 1个 | 308ms | 11%  
阿姆斯特丹 | 53个 | 3个 | 315ms | 2%  
伦敦 | 53个 | 1个 | 319ms | 6%  
  
**简评：** 本表展示了山东的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻山东，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**山东电信到Vultr各机房的测速数据 [20180527]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 17个 | 1个 | 205ms | 17%  
洛杉矶 | 17个 | 0 | 217ms | 2%  
硅谷 | 16个 | 0 | 214ms | 11%  
西雅图 | 17个 | 0 | 235ms | 11%  
新加坡 | 17个 | 1个 | 272ms | 19%  
达拉斯 | 16个 | 0 | 238ms | 2%  
芝加哥 | 17个 | 0 | 282ms | 6%  
均值 | 251个 | 2个 | 262ms | 8%  
亚特兰大 | 17个 | 0 | 233ms | 0  
迈阿密 | 17个 | 0 | 263ms | 6%  
新泽西 | 16个 | 0 | 306ms | 6%  
巴黎 | 17个 | 0 | 275ms | 7%  
法兰克福 | 17个 | 0 | 285ms | 0  
悉尼 | 17个 | 0 | 344ms | 19%  
阿姆斯特丹 | 17个 | 0 | 266ms | 3%  
伦敦 | 16个 | 0 | 301ms | 4%  
  
**简评：** 如果你是来自山东的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、亚特兰大、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、硅谷、西雅图** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**山东联通到Vultr各机房的测速数据 [20180527]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 19个 | 0 | 212ms | 10%  
洛杉矶 | 19个 | 0 | 181ms | 2%  
硅谷 | 18个 | 0 | 182ms | 19%  
西雅图 | 18个 | 0 | 189ms | 19%  
新加坡 | 19个 | 0 | 273ms | 13%  
达拉斯 | 19个 | 0 | 207ms | 2%  
芝加哥 | 19个 | 0 | 239ms | 4%  
均值 | 281个 | 4个 | 254ms | 8%  
亚特兰大 | 19个 | 0 | 234ms | 2%  
迈阿密 | 19个 | 0 | 243ms | 12%  
新泽西 | 19个 | 1个 | 256ms | 7%  
巴黎 | 19个 | 1个 | 331ms | 16%  
法兰克福 | 18个 | 0 | 332ms | 2%  
悉尼 | 18个 | 0 | 321ms | 12%  
阿姆斯特丹 | 19个 | 2个 | 329ms | 2%  
伦敦 | 19个 | 0 | 319ms | 2%  
  
**简评：** 如果你是来自山东的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、达拉斯、亚特兰大、芝加哥** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **硅谷、西雅图、东京、迈阿密** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**山东移动到Vultr各机房的测速数据 [20180527]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 16个 | 1个 | 121ms | 4%  
洛杉矶 | 17个 | 1个 | 206ms | 3%  
硅谷 | 17个 | 1个 | 214ms | 10%  
西雅图 | 16个 | 1个 | 231ms | 11%  
新加坡 | 16个 | 1个 | 119ms | 1%  
达拉斯 | 17个 | 1个 | 321ms | 31%  
芝加哥 | 17个 | 1个 | 260ms | 5%  
均值 | 254个 | 15个 | 264ms | 9%  
亚特兰大 | 17个 | 1个 | 341ms | 31%  
迈阿密 | 17个 | 1个 | 308ms | 16%  
新泽西 | 17个 | 1个 | 275ms | 0  
巴黎 | 17个 | 1个 | 291ms | 2%  
法兰克福 | 17个 | 1个 | 293ms | 3%  
悉尼 | 18个 | 1个 | 260ms | 2%  
阿姆斯特丹 | 17个 | 1个 | 351ms | 2%  
伦敦 | 18个 | 1个 | 338ms | 12%  
  
**简评：** 如果你是来自山东的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡、东京、洛杉矶** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **硅谷、西雅图** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [江西](/vultr/isp/jiangxi/20180527-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180527")
    * [吉林](/vultr/isp/jilin/20180527-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180527")
    * [辽宁](/vultr/isp/liaoning/20180527-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180527")
    * [宁夏](/vultr/isp/ningxia/20180527-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180527")
    * [青海](/vultr/isp/qinghai/20180527-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180527")
    * [山西](/vultr/isp/shan1xi/20180527-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180527")
    * [陕西](/vultr/isp/shan3xi/20180527-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180527")
    * [上海](/vultr/isp/shanghai/20180527-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180527")
    * [四川](/vultr/isp/sichuan/20180527-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180527")
    * [天津](/vultr/isp/tianjin/20180527-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180527")
    * [新疆](/vultr/isp/xinjiang/20180527-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180527")
    * [云南](/vultr/isp/yunnan/20180527-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180527")
    * [浙江](/vultr/isp/zhejiang/20180527-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180527")
  * 山东到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/shandong/20180514-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180514")
    * [20180622](/vultr/isp/shandong/20180622-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/shandong/20180804-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/shandong/20180918-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180918")
  * 本期报告：山东到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/shandong/20180527-bandwagon-isp-shandong.md "山东到BandwagonHost各机房的Ping测试 20180527")
    * [Digital Ocean](/digitalocean/isp/shandong/20180527-digitalocean-isp-shandong.md "山东到Digital Ocean各机房的Ping测试 20180527")
    * [Linode](/linode/isp/shandong/20180527-linode-isp-shandong.md "山东到Linode各机房的Ping测试 20180527")



本文最初发表于[山东到Vultr各机房的测速数据（20180527）](https://vps123.top/pingtest/20180527-vultr-isp-shandong.html)
