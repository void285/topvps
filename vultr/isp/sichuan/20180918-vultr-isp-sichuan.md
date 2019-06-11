#  四川到Vultr各机房的测速数据（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![四川到Vultr各机房的测速数据（20180918）](/images/thumbnails/Sichuan_to_vultr.png)

本文的数据视角为 **四川到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在四川且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918四川到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点1112个，其中超时点9个。连通概况如下：大陆线路响应均值为267毫秒，最快的三个机房所在地为东京、洛杉矶、硅谷，最慢的三个为法兰克福、巴黎、阿姆斯特丹；西雅图、亚特兰大、东京、洛杉矶、迈阿密等7处有响应超时情况；法兰克福、巴黎、亚特兰大、西雅图、阿姆斯特丹等6处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 四川图表数据

![大陆省份四川到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_isp_sichuan_vultr_20180918.png)

### 全部运营商

**四川全部运营商到Vultr各机房的测速数据 [20180918]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 72个 | 1个 | 161ms | 2%  
洛杉矶 | 77个 | 1个 | 224ms | 5%  
硅谷 | 71个 | 0 | 231ms | 3%  
新加坡 | 73个 | 0 | 231ms | 2%  
西雅图 | 75个 | 2个 | 240ms | 7%  
达拉斯 | 73个 | 0 | 243ms | 2%  
芝加哥 | 78个 | 0 | 263ms | 1%  
均值 | 1112个 | 9个 | 267ms | 4%  
迈阿密 | 76个 | 1个 | 284ms | 2%  
悉尼 | 73个 | 0 | 286ms | 1%  
亚特兰大 | 76个 | 2个 | 287ms | 8%  
新泽西 | 71个 | 1个 | 293ms | 4%  
伦敦 | 71个 | 0 | 297ms | 3%  
法兰克福 | 76个 | 0 | 314ms | 8%  
巴黎 | 77个 | 0 | 316ms | 8%  
阿姆斯特丹 | 73个 | 1个 | 324ms | 6%  
  
**简评：** 本表展示了四川的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻四川，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **东京、洛杉矶、硅谷、新加坡、达拉斯** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**四川电信到Vultr各机房的测速数据 [20180918]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 35个 | 1个 | 205ms | 5%  
洛杉矶 | 38个 | 1个 | 239ms | 9%  
硅谷 | 35个 | 0 | 236ms | 5%  
新加坡 | 39个 | 0 | 278ms | 4%  
西雅图 | 38个 | 2个 | 251ms | 9%  
达拉斯 | 35个 | 0 | 240ms | 1%  
芝加哥 | 38个 | 0 | 265ms | 2%  
均值 | 553个 | 9个 | 279ms | 6%  
迈阿密 | 37个 | 1个 | 289ms | 5%  
悉尼 | 37个 | 0 | 341ms | 1%  
亚特兰大 | 37个 | 2个 | 308ms | 13%  
新泽西 | 35个 | 1个 | 275ms | 1%  
伦敦 | 36个 | 0 | 286ms | 1%  
法兰克福 | 37个 | 0 | 316ms | 16%  
巴黎 | 38个 | 0 | 310ms | 14%  
阿姆斯特丹 | 38个 | 1个 | 328ms | 2%  
  
**简评：** 如果你是来自四川的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、硅谷、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **洛杉矶** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**四川联通到Vultr各机房的测速数据 [20180918]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 13个 | 0 | 138ms | 1%  
洛杉矶 | 15个 | 0 | 212ms | 4%  
硅谷 | 13个 | 0 | 223ms | 2%  
新加坡 | 12个 | 0 | 265ms | 0  
西雅图 | 14个 | 0 | 231ms | 7%  
达拉斯 | 14个 | 0 | 235ms | 6%  
芝加哥 | 15个 | 0 | 255ms | 0  
均值 | 206个 | 0 | 272ms | 4%  
迈阿密 | 14个 | 0 | 267ms | 0  
悉尼 | 14个 | 0 | 274ms | 2%  
亚特兰大 | 15个 | 0 | 269ms | 4%  
新泽西 | 12个 | 0 | 312ms | 9%  
伦敦 | 13个 | 0 | 349ms | 8%  
法兰克福 | 15个 | 0 | 337ms | 5%  
巴黎 | 15个 | 0 | 354ms | 4%  
阿姆斯特丹 | 12个 | 0 | 358ms | 14%  
  
**简评：** 如果你是来自四川的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、洛杉矶、硅谷** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **西雅图、达拉斯** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**四川移动到Vultr各机房的测速数据 [20180918]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 24个 | 0 | 139ms | 1%  
洛杉矶 | 24个 | 0 | 221ms | 2%  
硅谷 | 23个 | 0 | 232ms | 2%  
新加坡 | 22个 | 0 | 151ms | 1%  
西雅图 | 23个 | 0 | 237ms | 5%  
达拉斯 | 24个 | 0 | 255ms | 0  
芝加哥 | 25个 | 0 | 269ms | 0  
均值 | 353个 | 0 | 250ms | 2%  
迈阿密 | 25个 | 0 | 295ms | 2%  
悉尼 | 22个 | 0 | 244ms | 0  
亚特兰大 | 24个 | 0 | 284ms | 5%  
新泽西 | 24个 | 0 | 291ms | 0  
伦敦 | 22个 | 0 | 258ms | 0  
法兰克福 | 24个 | 0 | 287ms | 5%  
巴黎 | 24个 | 0 | 284ms | 6%  
阿姆斯特丹 | 23个 | 0 | 285ms | 1%  
  
**简评：** 如果你是来自四川的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、洛杉矶、硅谷、西雅图、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [广西](/vultr/isp/guangxi/20180918-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180918")
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
    * [天津](/vultr/isp/tianjin/20180918-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180918")
    * [西藏](/vultr/isp/tibet/20180918-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180918")
    * [新疆](/vultr/isp/xinjiang/20180918-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180918")
    * [云南](/vultr/isp/yunnan/20180918-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180918")
    * [浙江](/vultr/isp/zhejiang/20180918-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180918")
  * 四川到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/sichuan/20180514-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/sichuan/20180527-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/sichuan/20180622-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/sichuan/20180804-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180804")
  * 本期报告：四川到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/sichuan/20180918-bandwagon-isp-sichuan.md "四川到BandwagonHost各机房的Ping测试 20180918")
    * [Digital Ocean](/digitalocean/isp/sichuan/20180918-digitalocean-isp-sichuan.md "四川到Digital Ocean各机房的Ping测试 20180918")
    * [Linode](/linode/isp/sichuan/20180918-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180918")



本文最初发表于[四川到Vultr各机房的测速数据（20180918）](https://vps123.top/pingtest/20180918-vultr-isp-sichuan.html)
