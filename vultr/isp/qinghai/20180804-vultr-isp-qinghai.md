#  青海到Vultr各机房的测速数据（20180804） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![青海到Vultr各机房的测速数据（20180804）](/images/thumbnails/Qinghai_to_vultr.png)

本文的数据视角为 **青海到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在青海且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通，有效样本点168个，无超时点。连通概况如下：大陆线路响应均值为310毫秒，最快的三个机房所在地为洛杉矶、巴黎、法兰克福，最慢的三个为新泽西、亚特兰大、迈阿密；新加坡、东京、悉尼、达拉斯、迈阿密等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 青海图表数据

![大陆省份青海到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180804](/images/pingtests/vultr_20180804/plot_isp_qinghai_vultr_20180804.png)

### 全部运营商

青海全部运营商到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
洛杉矶 | 8个 | 0 | 209ms | 0 | 达拉斯 | 16个 | 0 | 330ms | 12%  
巴黎 | 8个 | 0 | 220ms | 0 | 芝加哥 | 8个 | 0 | 343ms | 5%  
法兰克福 | 16个 | 0 | 221ms | 0 | 伦敦 | 16个 | 0 | 346ms | 3%  
东京 | 16个 | 0 | 237ms | 31% | 阿姆斯特丹 | 8个 | 0 | 359ms | 6%  
西雅图 | 8个 | 0 | 262ms | 1% | 悉尼 | 8个 | 0 | 382ms | 21%  
硅谷 | 16个 | 0 | 265ms | 3% | 新泽西 | 16个 | 0 | 404ms | 3%  
新加坡 | 8个 | 0 | 308ms | 36% | 亚特兰大 | 8个 | 0 | 406ms | 5%  
均值 | 168个 | 0 | 310ms | 9% | 迈阿密 | 8个 | 0 | 418ms | 7%  
  
简评：本表展示了青海的 **电信、联通** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻青海，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **洛杉矶、巴黎、法兰克福** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

青海电信到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
洛杉矶 | 4个 | 0 | 232ms | 0 | 达拉斯 | 8个 | 0 | 393ms | 21%  
巴黎 | 4个 | 0 | 242ms | 0 | 芝加哥 | 4个 | 0 | 340ms | 5%  
法兰克福 | 8个 | 0 | 242ms | 0 | 伦敦 | 8个 | 0 | 338ms | 5%  
东京 | 8个 | 0 | 241ms | 30% | 阿姆斯特丹 | 4个 | 0 | 355ms | 6%  
西雅图 | 4个 | 0 | 292ms | 0 | 悉尼 | 4个 | 0 | 368ms | 23%  
硅谷 | 8个 | 0 | 258ms | 3% | 新泽西 | 8个 | 0 | 387ms | 3%  
新加坡 | 4个 | 0 | 305ms | 29% | 亚特兰大 | 4个 | 0 | 391ms | 5%  
均值 | 84个 | 0 | 316ms | 9% | 迈阿密 | 4个 | 0 | 398ms | 7%  
  
简评：如果你是来自青海的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、巴黎、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

青海联通到Vultr各机房的测速数据 [20180804] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
洛杉矶 | 4个 | 0 | 186ms | 0 | 达拉斯 | 8个 | 0 | 268ms | 3%  
巴黎 | 4个 | 0 | 199ms | 0 | 芝加哥 | 4个 | 0 | 347ms | 6%  
法兰克福 | 8个 | 0 | 201ms | 0 | 伦敦 | 8个 | 0 | 354ms | 1%  
东京 | 8个 | 0 | 234ms | 32% | 阿姆斯特丹 | 4个 | 0 | 363ms | 6%  
西雅图 | 4个 | 0 | 232ms | 3% | 悉尼 | 4个 | 0 | 396ms | 19%  
硅谷 | 8个 | 0 | 272ms | 4% | 新泽西 | 8个 | 0 | 421ms | 3%  
新加坡 | 4个 | 0 | 311ms | 43% | 亚特兰大 | 4个 | 0 | 421ms | 5%  
均值 | 84个 | 0 | 304ms | 8% | 迈阿密 | 4个 | 0 | 439ms | 8%  
  
简评：如果你是来自青海的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、巴黎、法兰克福、西雅图** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180804) 
    * [全部](https://vps123.top/pingtests/20180804 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180804 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180804 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180804 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180804-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180804")
    * [北京](/vultr/isp/beijing/20180804-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180804")
    * [大陆](/vultr/isp/china/20180804-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180804")
    * [重庆](/vultr/isp/chongqing/20180804-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180804")
    * [福建](/vultr/isp/fujian/20180804-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180804")
    * [甘肃](/vultr/isp/gansu/20180804-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180804")
    * [广东](/vultr/isp/guangdong/20180804-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180804")
    * [广西](/vultr/isp/guangxi/20180804-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180804")
    * [贵州](/vultr/isp/guizhou/20180804-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180804")
    * [海南](/vultr/isp/hainan/20180804-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180804")
    * [河北](/vultr/isp/hebei/20180804-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180804")
    * [黑龙江](/vultr/isp/heilongjiang/20180804-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180804")
    * [河南](/vultr/isp/henan/20180804-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180804")
    * [湖北](/vultr/isp/hubei/20180804-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180804")
    * [湖南](/vultr/isp/hunan/20180804-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180804")
    * [内蒙古](/vultr/isp/innermongolia/20180804-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180804")
    * [江苏](/vultr/isp/jiangsu/20180804-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180804")
    * [江西](/vultr/isp/jiangxi/20180804-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180804")
    * [吉林](/vultr/isp/jilin/20180804-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180804")
    * [辽宁](/vultr/isp/liaoning/20180804-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180804")
    * [宁夏](/vultr/isp/ningxia/20180804-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180804")
    * [山西](/vultr/isp/shan1xi/20180804-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180804")
    * [陕西](/vultr/isp/shan3xi/20180804-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180804")
    * [山东](/vultr/isp/shandong/20180804-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180804")
    * [上海](/vultr/isp/shanghai/20180804-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180804")
    * [四川](/vultr/isp/sichuan/20180804-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180804")
    * [天津](/vultr/isp/tianjin/20180804-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180804")
    * [西藏](/vultr/isp/tibet/20180804-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180804")
    * [新疆](/vultr/isp/xinjiang/20180804-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180804")
    * [云南](/vultr/isp/yunnan/20180804-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180804")
    * [浙江](/vultr/isp/zhejiang/20180804-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180804")
  * 青海到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/qinghai/20180514-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/qinghai/20180527-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/qinghai/20180622-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180622")
    * [20180918](/vultr/isp/qinghai/20180918-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180918")
  * 本期报告：青海到 _其他VPS提供商_ 各机房的测速报告： 
    * [Digital Ocean](/digitalocean/isp/qinghai/20180804-digitalocean-isp-qinghai.md "青海到Digital Ocean各机房的Ping测试 20180804")
    * [Linode](/linode/isp/qinghai/20180804-linode-isp-qinghai.md "青海到Linode各机房的Ping测试 20180804")



本文最初发表于[青海到Vultr各机房的测速数据（20180804）](https://vps123.top/pingtest/20180804-vultr-isp-qinghai.html)
