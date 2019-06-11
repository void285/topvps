#  青海到Vultr各机房的测速数据（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![青海到Vultr各机房的测速数据（20180527）](/images/thumbnails/Qinghai_to_vultr.png)

本文的数据视角为 **青海到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在青海且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点56个，无超时点。连通概况如下：大陆线路响应均值为275毫秒，最快的三个机房所在地为东京、新加坡、硅谷，最慢的三个为新泽西、悉尼、达拉斯；达拉斯、东京、新加坡、亚特兰大、芝加哥等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 青海图表数据

![大陆省份青海到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_isp_qinghai_vultr_20180527.png)

### 全部运营商

青海全部运营商到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 4个 | 0 | 182ms | 11% | 均值 | 56个 | 0 | 275ms | 5%  
新加坡 | 4个 | 0 | 219ms | 11% | 迈阿密 | 3个 | 0 | 291ms | 3%  
硅谷 | 3个 | 0 | 241ms | 3% | 伦敦 | 4个 | 0 | 294ms | 4%  
法兰克福 | 4个 | 0 | 250ms | 1% | 亚特兰大 | 4个 | 0 | 308ms | 10%  
洛杉矶 | 4个 | 0 | 264ms | 1% | 芝加哥 | 4个 | 0 | 310ms | 9%  
巴黎 | 4个 | 0 | 267ms | 1% | 新泽西 | 4个 | 0 | 322ms | 2%  
西雅图 | 4个 | 0 | 268ms | 5% | 悉尼 | 3个 | 0 | 331ms | 7%  
阿姆斯特丹 | 4个 | 0 | 274ms | 0 | 达拉斯 | 3个 | 0 | 333ms | 14%  
  
简评：本表展示了青海的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻青海，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **硅谷、法兰克福** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

青海电信到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 1个 | 0 | 207ms | 13% | 均值 | 15个 | 0 | 274ms | 4%  
新加坡 | 1个 | 0 | 272ms | 16% | 迈阿密 | 1个 | 0 | 268ms | 0  
硅谷 | 1个 | 0 | 242ms | 0 | 伦敦 | 1个 | 0 | 289ms | 1%  
法兰克福 | 1个 | 0 | 253ms | 0 | 亚特兰大 | 1个 | 0 | 258ms | 0  
洛杉矶 | 1个 | 0 | 286ms | 3% | 芝加哥 | 1个 | 0 | 296ms | 8%  
巴黎 | 1个 | 0 | 250ms | 0 | 新泽西 | 1个 | 0 | 312ms | 8%  
西雅图 | 1个 | 0 | 302ms | 0 | 悉尼 | 1个 | 0 | 388ms | 15%  
阿姆斯特丹 | 1个 | 0 | 201ms | 0 | 达拉斯 | 1个 | 0 | 299ms | 1%  
  
简评：如果你是来自青海的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **阿姆斯特丹、硅谷、巴黎** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

青海联通到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 1个 | 0 | 209ms | 20% | 均值 | 11个 | 0 | 278ms | 4%  
新加坡 | 1个 | 0 | 277ms | 17% | 迈阿密 | - | - | - | -  
硅谷 | - | - | - | - | 伦敦 | 1个 | 0 | 284ms | 0  
法兰克福 | 1个 | 0 | 265ms | 0 | 亚特兰大 | 1个 | 0 | 293ms | 1%  
洛杉矶 | 1个 | 0 | 283ms | 2% | 芝加哥 | 1个 | 0 | 342ms | 0  
巴黎 | 1个 | 0 | 252ms | 0 | 新泽西 | 1个 | 0 | 365ms | 0  
西雅图 | 1个 | 0 | 241ms | 7% | 悉尼 | - | - | - | -  
阿姆斯特丹 | 1个 | 0 | 251ms | 0 | 达拉斯 | - | - | - | -  
  
简评：如果你是来自青海的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，请慎重选择部署在 **东京、西雅图** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

青海移动到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 2个 | 0 | 131ms | 0 | 均值 | 30个 | 0 | 273ms | 8%  
新加坡 | 2个 | 0 | 108ms | 0 | 迈阿密 | 2个 | 0 | 315ms | 6%  
硅谷 | 2个 | 0 | 240ms | 7% | 伦敦 | 2个 | 0 | 309ms | 12%  
法兰克福 | 2个 | 0 | 234ms | 4% | 亚特兰大 | 2个 | 0 | 374ms | 29%  
洛杉矶 | 2个 | 0 | 225ms | 0 | 芝加哥 | 2个 | 0 | 293ms | 19%  
巴黎 | 2个 | 0 | 300ms | 3% | 新泽西 | 2个 | 0 | 291ms | 0  
西雅图 | 2个 | 0 | 262ms | 10% | 悉尼 | 2个 | 0 | 275ms | 0  
阿姆斯特丹 | 2个 | 0 | 370ms | 1% | 达拉斯 | 2个 | 0 | 368ms | 28%  
  
简评：如果你是来自青海的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡、东京、洛杉矶、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **硅谷** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [山西](/vultr/isp/shan1xi/20180527-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180527")
    * [陕西](/vultr/isp/shan3xi/20180527-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180527")
    * [山东](/vultr/isp/shandong/20180527-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180527")
    * [上海](/vultr/isp/shanghai/20180527-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180527")
    * [四川](/vultr/isp/sichuan/20180527-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180527")
    * [天津](/vultr/isp/tianjin/20180527-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180527")
    * [新疆](/vultr/isp/xinjiang/20180527-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180527")
    * [云南](/vultr/isp/yunnan/20180527-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180527")
    * [浙江](/vultr/isp/zhejiang/20180527-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180527")
  * 青海到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/qinghai/20180514-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180514")
    * [20180622](/vultr/isp/qinghai/20180622-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/qinghai/20180804-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/qinghai/20180918-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180918")
  * 本期报告：青海到 _其他VPS提供商_ 各机房的测速报告： 
    * [Digital Ocean](/digitalocean/isp/qinghai/20180527-digitalocean-isp-qinghai.md "青海到Digital Ocean各机房的Ping测试 20180527")
    * [Linode](/linode/isp/qinghai/20180527-linode-isp-qinghai.md "青海到Linode各机房的Ping测试 20180527")



本文最初发表于[青海到Vultr各机房的测速数据（20180527）](https://vps123.top/pingtest/20180527-vultr-isp-qinghai.html)
