#  大陆到Vultr各机房的测速数据（20180527） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![大陆到Vultr各机房的测速数据（20180527）](/images/thumbnails/China_to_vultr.png)

本文的数据视角为 **中国大陆各省份/运营商到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在大陆，打算在[Vultr](https://vps123.top/go/vultr)的机房架设代理服务器或进行云计算，后面的图表数据可以帮你形成评估Vultr各机房的大概印象，排除一些数据较差的机房，锁定一些潜在的目标机房。要确定最适合你的机房，请通过本文结尾的链接，查看你所在省份的数据，它们更准确、针对性更强；你也可以通过文末链接查看其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点14559个，其中超时点221个。连通概况如下：大陆线路响应均值为265毫秒，最快的三个机房所在地为东京、硅谷、洛杉矶，最慢的三个为阿姆斯特丹、悉尼、伦敦；法兰克福、新加坡、东京、亚特兰大、迈阿密等15处有响应超时情况；新加坡、悉尼、东京、亚特兰大、达拉斯等12处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆图表数据

![大陆省份大陆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180527](/images/pingtests/vultr_20180527/plot_isp_china_vultr_20180527.png)

### 全部运营商

大陆全部运营商到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 954个 | 16个 | 177ms | 12% | 巴黎 | 981个 | 10个 | 279ms | 5%  
硅谷 | 971个 | 15个 | 216ms | 11% | 法兰克福 | 962个 | 34个 | 280ms | 3%  
洛杉矶 | 975个 | 15个 | 220ms | 3% | 亚特兰大 | 981个 | 16个 | 282ms | 12%  
新加坡 | 972个 | 22个 | 230ms | 13% | 迈阿密 | 965个 | 16个 | 282ms | 10%  
西雅图 | 970个 | 12个 | 231ms | 9% | 新泽西 | 962个 | 12个 | 293ms | 7%  
均值 | 14559个 | 221个 | 265ms | 8% | 阿姆斯特丹 | 980个 | 12个 | 299ms | 3%  
芝加哥 | 975个 | 13个 | 276ms | 8% | 悉尼 | 974个 | 13个 | 316ms | 13%  
达拉斯 | 973个 | 10个 | 276ms | 11% | 伦敦 | 964个 | 5个 | 320ms | 6%  
  
简评：本表展示了大陆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；籍此我们可以快速了解，整个大陆地区到Vultr各个机房的平均响应速度以及丢包率：如果某机房的响应值、丢包率较高，那么大概率各省到此机房的网络也不理想，用来建站是不大合适的；而如果此处的响应值、丢包率还不错，我们可再具体了解一个省份的数据。  
在这里， **洛杉矶** 的响应速度小于250ms，且丢包率在5%以内，值得关注。如果你主要关心某运营商的网络概况，后面几个表格的数据更有参考价值。  
如果你打算将VPS用作科学上网、云存储、远程任务、游戏服务器等用途，请 **关注你所在的省份** 到Vultr各机房的测速数据，它们可以给你更有益的参考。

### 电信

大陆电信到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 398个 | 12个 | 206ms | 19% | 巴黎 | 417个 | 4个 | 253ms | 2%  
硅谷 | 412个 | 8个 | 228ms | 7% | 法兰克福 | 400个 | 28个 | 260ms | 2%  
洛杉矶 | 413个 | 9个 | 247ms | 5% | 亚特兰大 | 419个 | 9个 | 274ms | 7%  
新加坡 | 412个 | 15个 | 273ms | 20% | 迈阿密 | 405个 | 9个 | 286ms | 6%  
西雅图 | 411个 | 6个 | 257ms | 6% | 新泽西 | 404个 | 5个 | 329ms | 6%  
均值 | 6143个 | 136个 | 274ms | 8% | 阿姆斯特丹 | 414个 | 6个 | 254ms | 2%  
芝加哥 | 414个 | 7个 | 311ms | 6% | 悉尼 | 415个 | 8个 | 357ms | 20%  
达拉斯 | 406个 | 7个 | 279ms | 6% | 伦敦 | 403个 | 3个 | 294ms | 3%  
  
简评：如果你关注电信的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **洛杉矶** 的整体的连通速度、丢包率都比较不错， **东京、硅谷** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

大陆联通到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 281个 | 1个 | 192ms | 11% | 巴黎 | 282个 | 3个 | 317ms | 9%  
硅谷 | 280个 | 5个 | 200ms | 16% | 法兰克福 | 284个 | 3个 | 321ms | 6%  
洛杉矶 | 282个 | 4个 | 205ms | 2% | 亚特兰大 | 284个 | 3个 | 253ms | 4%  
新加坡 | 285个 | 4个 | 279ms | 13% | 迈阿密 | 284个 | 3个 | 255ms | 14%  
西雅图 | 284个 | 4个 | 216ms | 17% | 新泽西 | 282个 | 5个 | 268ms | 12%  
均值 | 4252个 | 46个 | 262ms | 9% | 阿姆斯特丹 | 286个 | 4个 | 323ms | 6%  
芝加哥 | 285个 | 4个 | 254ms | 13% | 悉尼 | 282个 | 3个 | 310ms | 11%  
达拉斯 | 287个 | 0 | 232ms | 3% | 伦敦 | 284个 | 0 | 324ms | 5%  
  
简评：如果你关注联通的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **洛杉矶、达拉斯** 的整体的连通速度、丢包率都比较不错， **东京、硅谷、西雅图** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

大陆移动到Vultr各机房的测速数据 [20180527] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 275个 | 3个 | 121ms | 4% | 巴黎 | 282个 | 3个 | 281ms | 4%  
硅谷 | 279个 | 2个 | 214ms | 10% | 法兰克福 | 278个 | 3个 | 276ms | 2%  
洛杉矶 | 280个 | 2个 | 207ms | 2% | 亚特兰大 | 278个 | 4个 | 327ms | 26%  
新加坡 | 275个 | 3个 | 123ms | 3% | 迈阿密 | 276个 | 4个 | 302ms | 12%  
西雅图 | 275个 | 2个 | 212ms | 6% | 新泽西 | 276个 | 2个 | 275ms | 1%  
均值 | 4164个 | 39个 | 258ms | 8% | 阿姆斯特丹 | 280个 | 2个 | 338ms | 3%  
芝加哥 | 276个 | 2个 | 257ms | 7% | 悉尼 | 277个 | 2个 | 261ms | 4%  
达拉斯 | 280个 | 3个 | 314ms | 26% | 伦敦 | 277个 | 2个 | 347ms | 12%  
  
简评：如果你关注移动的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **东京、新加坡、洛杉矶** 的整体的连通速度、丢包率都比较不错， **西雅图、硅谷** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [山东](/vultr/isp/shandong/20180527-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180527")
    * [上海](/vultr/isp/shanghai/20180527-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180527")
    * [四川](/vultr/isp/sichuan/20180527-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180527")
    * [天津](/vultr/isp/tianjin/20180527-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180527")
    * [新疆](/vultr/isp/xinjiang/20180527-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180527")
    * [云南](/vultr/isp/yunnan/20180527-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180527")
    * [浙江](/vultr/isp/zhejiang/20180527-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180527")
  * 大陆到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/china/20180514-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180514")
    * [20180622](/vultr/isp/china/20180622-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/china/20180804-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/china/20180918-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180918")
  * 本期报告：大陆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/china/20180527-bandwagon-isp-china.md "大陆到BandwagonHost各机房的Ping测试 20180527")
    * [Digital Ocean](/digitalocean/isp/china/20180527-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180527")
    * [Linode](/linode/isp/china/20180527-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180527")



本文最初发表于[大陆到Vultr各机房的测速数据（20180527）](https://vps123.top/pingtest/20180527-vultr-isp-china.html)
