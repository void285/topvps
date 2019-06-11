#  山东到Vultr各机房的测速数据（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![山东到Vultr各机房的测速数据（20180918）](/images/thumbnails/Shandong_to_vultr.png)

本文的数据视角为 **山东到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在山东且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918山东到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点1383个，其中超时点2个。连通概况如下：大陆线路响应均值为241毫秒，最快的三个机房所在地为东京、新加坡、硅谷，最慢的三个为法兰克福、伦敦、阿姆斯特丹；西雅图有响应超时情况；阿姆斯特丹、伦敦、新泽西、悉尼、东京等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 山东图表数据

![大陆省份山东到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_isp_shandong_vultr_20180918.png)

### 全部运营商

山东全部运营商到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 92个 | 0 | 129ms | 7% | 亚特兰大 | 93个 | 0 | 251ms | 5%  
新加坡 | 95个 | 0 | 177ms | 6% | 迈阿密 | 90个 | 0 | 266ms | 3%  
硅谷 | 93个 | 0 | 200ms | 2% | 悉尼 | 91个 | 0 | 267ms | 7%  
洛杉矶 | 93个 | 0 | 201ms | 4% | 巴黎 | 90个 | 0 | 268ms | 2%  
西雅图 | 92个 | 2个 | 213ms | 3% | 新泽西 | 94个 | 0 | 269ms | 7%  
达拉斯 | 90个 | 0 | 220ms | 4% | 法兰克福 | 92个 | 0 | 302ms | 3%  
均值 | 1383个 | 2个 | 241ms | 5% | 伦敦 | 91个 | 0 | 303ms | 8%  
芝加哥 | 90个 | 0 | 243ms | 1% | 阿姆斯特丹 | 97个 | 0 | 312ms | 9%  
  
简评：本表展示了山东的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻山东，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **硅谷、洛杉矶、西雅图、达拉斯、芝加哥** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

山东电信到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 30个 | 0 | 148ms | 6% | 亚特兰大 | 30个 | 0 | 272ms | 9%  
新加坡 | 31个 | 0 | 210ms | 6% | 迈阿密 | 29个 | 0 | 271ms | 6%  
硅谷 | 30个 | 0 | 210ms | 2% | 悉尼 | 29个 | 0 | 300ms | 3%  
洛杉矶 | 30个 | 0 | 211ms | 6% | 巴黎 | 29个 | 0 | 283ms | 4%  
西雅图 | 29个 | 0 | 218ms | 3% | 新泽西 | 30个 | 0 | 265ms | 7%  
达拉斯 | 28个 | 0 | 213ms | 1% | 法兰克福 | 30个 | 0 | 286ms | 1%  
均值 | 445个 | 0 | 249ms | 4% | 伦敦 | 29个 | 0 | 297ms | 6%  
芝加哥 | 30个 | 0 | 245ms | 2% | 阿姆斯特丹 | 31个 | 0 | 314ms | 4%  
  
简评：如果你是来自山东的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **硅谷、达拉斯、西雅图、芝加哥** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡、洛杉矶** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

山东联通到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 35个 | 0 | 128ms | 9% | 亚特兰大 | 36个 | 0 | 226ms | 1%  
新加坡 | 36个 | 0 | 198ms | 7% | 迈阿密 | 36个 | 0 | 246ms | 0  
硅谷 | 35个 | 0 | 179ms | 1% | 悉尼 | 36个 | 0 | 281ms | 6%  
洛杉矶 | 35个 | 0 | 182ms | 0 | 巴黎 | 35个 | 0 | 313ms | 0  
西雅图 | 35个 | 2个 | 193ms | 0 | 新泽西 | 36个 | 0 | 274ms | 14%  
达拉斯 | 34个 | 0 | 213ms | 5% | 法兰克福 | 36个 | 0 | 345ms | 4%  
均值 | 530个 | 2个 | 245ms | 5% | 伦敦 | 36个 | 0 | 338ms | 16%  
芝加哥 | 33个 | 0 | 230ms | 1% | 阿姆斯特丹 | 36个 | 0 | 345ms | 14%  
  
简评：如果你是来自山东的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **硅谷、洛杉矶、西雅图、达拉斯、亚特兰大、芝加哥、迈阿密** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、新加坡** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

山东移动到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 27个 | 0 | 112ms | 5% | 亚特兰大 | 27个 | 0 | 254ms | 6%  
新加坡 | 28个 | 0 | 121ms | 5% | 迈阿密 | 25个 | 0 | 282ms | 3%  
硅谷 | 28个 | 0 | 211ms | 5% | 悉尼 | 26个 | 0 | 221ms | 12%  
洛杉矶 | 28个 | 0 | 208ms | 7% | 巴黎 | 26个 | 0 | 209ms | 4%  
西雅图 | 28个 | 0 | 227ms | 6% | 新泽西 | 28个 | 0 | 269ms | 1%  
达拉斯 | 28个 | 0 | 236ms | 5% | 法兰克福 | 26个 | 0 | 273ms | 5%  
均值 | 408个 | 0 | 228ms | 5% | 伦敦 | 26个 | 0 | 273ms | 2%  
芝加哥 | 27个 | 0 | 254ms | 0 | 阿姆斯特丹 | 30个 | 0 | 277ms | 8%  
  
简评：如果你是来自山东的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、新加坡、巴黎、硅谷、达拉斯** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **洛杉矶、悉尼、西雅图** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [上海](/vultr/isp/shanghai/20180918-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180918")
    * [四川](/vultr/isp/sichuan/20180918-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180918")
    * [天津](/vultr/isp/tianjin/20180918-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180918")
    * [西藏](/vultr/isp/tibet/20180918-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180918")
    * [新疆](/vultr/isp/xinjiang/20180918-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180918")
    * [云南](/vultr/isp/yunnan/20180918-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180918")
    * [浙江](/vultr/isp/zhejiang/20180918-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180918")
  * 山东到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/shandong/20180514-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/shandong/20180527-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/shandong/20180622-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/shandong/20180804-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180804")
  * 本期报告：山东到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/shandong/20180918-bandwagon-isp-shandong.md "山东到BandwagonHost各机房的Ping测试 20180918")
    * [Digital Ocean](/digitalocean/isp/shandong/20180918-digitalocean-isp-shandong.md "山东到Digital Ocean各机房的Ping测试 20180918")
    * [Linode](/linode/isp/shandong/20180918-linode-isp-shandong.md "山东到Linode各机房的Ping测试 20180918")



本文最初发表于[山东到Vultr各机房的测速数据（20180918）](https://vps123.top/pingtest/20180918-vultr-isp-shandong.html)
