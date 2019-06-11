#  大陆到Vultr各机房的测速数据（20180918） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![大陆到Vultr各机房的测速数据（20180918）](/images/thumbnails/China_to_vultr.png)

本文的数据视角为 **中国大陆各省份/运营商到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在大陆，打算在[Vultr](https://vps123.top/go/vultr)的机房架设代理服务器或进行云计算，后面的图表数据可以帮你形成评估Vultr各机房的大概印象，排除一些数据较差的机房，锁定一些潜在的目标机房。要确定最适合你的机房，请通过本文结尾的链接，查看你所在省份的数据，它们更准确、针对性更强；你也可以通过文末链接查看其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180918大陆到Vultr各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点21251个，其中超时点214个。连通概况如下：大陆线路响应均值为247毫秒，最快的三个机房所在地为东京、新加坡、洛杉矶，最慢的三个为迈阿密、伦敦、阿姆斯特丹；迈阿密、洛杉矶、西雅图、东京、亚特兰大等15处有响应超时情况；亚特兰大、阿姆斯特丹、西雅图、洛杉矶、迈阿密等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆图表数据

![大陆省份大陆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180918](/images/pingtests/vultr_20180918/plot_isp_china_vultr_20180918.png)

### 全部运营商

大陆全部运营商到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 1406个 | 18个 | 139ms | 2% | 亚特兰大 | 1388个 | 15个 | 268ms | 7%  
新加坡 | 1459个 | 14个 | 201ms | 2% | 悉尼 | 1410个 | 12个 | 272ms | 1%  
洛杉矶 | 1418个 | 22个 | 210ms | 5% | 新泽西 | 1439个 | 11个 | 273ms | 5%  
硅谷 | 1426个 | 10个 | 212ms | 2% | 巴黎 | 1430个 | 12个 | 273ms | 4%  
西雅图 | 1434个 | 21个 | 223ms | 6% | 法兰克福 | 1408个 | 9个 | 273ms | 4%  
达拉斯 | 1371个 | 11个 | 232ms | 2% | 迈阿密 | 1413个 | 25个 | 284ms | 5%  
均值 | 21251个 | 214个 | 247ms | 4% | 伦敦 | 1393个 | 11个 | 291ms | 5%  
芝加哥 | 1399个 | 11个 | 251ms | 1% | 阿姆斯特丹 | 1457个 | 12个 | 303ms | 6%  
  
简评：本表展示了大陆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；籍此我们可以快速了解，整个大陆地区到Vultr各个机房的平均响应速度以及丢包率：如果某机房的响应值、丢包率较高，那么大概率各省到此机房的网络也不理想，用来建站是不大合适的；而如果此处的响应值、丢包率还不错，我们可再具体了解一个省份的数据。  
在这里， **东京、新加坡、洛杉矶、硅谷、达拉斯** 的响应速度小于250ms，且丢包率在5%以内，值得关注。如果你主要关心某运营商的网络概况，后面几个表格的数据更有参考价值。  
如果你打算将VPS用作科学上网、云存储、远程任务、游戏服务器等用途，请 **关注你所在的省份** 到Vultr各机房的测速数据，它们可以给你更有益的参考。

### 电信

大陆电信到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 589个 | 14个 | 176ms | 3% | 亚特兰大 | 575个 | 13个 | 291ms | 11%  
新加坡 | 603个 | 11个 | 250ms | 3% | 悉尼 | 593个 | 9个 | 313ms | 1%  
洛杉矶 | 589个 | 16个 | 228ms | 9% | 新泽西 | 599个 | 8个 | 262ms | 2%  
硅谷 | 588个 | 6个 | 217ms | 3% | 巴黎 | 587个 | 6个 | 269ms | 6%  
西雅图 | 595个 | 13个 | 241ms | 10% | 法兰克福 | 587个 | 6个 | 267ms | 5%  
达拉斯 | 574个 | 8个 | 229ms | 1% | 迈阿密 | 591个 | 21个 | 297ms | 10%  
均值 | 8834个 | 153个 | 257ms | 5% | 伦敦 | 583个 | 7个 | 274ms | 2%  
芝加哥 | 580个 | 6个 | 252ms | 0 | 阿姆斯特丹 | 601个 | 9个 | 299ms | 3%  
  
简评：如果你关注电信的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **东京、硅谷、达拉斯、新加坡** 的整体的连通速度、丢包率都比较不错， **洛杉矶、西雅图** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

大陆联通到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 413个 | 4个 | 119ms | 2% | 亚特兰大 | 418个 | 2个 | 249ms | 3%  
新加坡 | 433个 | 2个 | 216ms | 2% | 悉尼 | 421个 | 2个 | 274ms | 1%  
洛杉矶 | 419个 | 6个 | 197ms | 3% | 新泽西 | 422个 | 3个 | 293ms | 13%  
硅谷 | 428个 | 4个 | 201ms | 1% | 巴黎 | 428个 | 6个 | 306ms | 2%  
西雅图 | 426个 | 7个 | 211ms | 2% | 法兰克福 | 422个 | 3个 | 300ms | 3%  
达拉斯 | 407个 | 3个 | 224ms | 4% | 迈阿密 | 423个 | 4个 | 264ms | 2%  
均值 | 6324个 | 55个 | 251ms | 4% | 伦敦 | 415个 | 2个 | 335ms | 11%  
芝加哥 | 419个 | 5个 | 245ms | 0 | 阿姆斯特丹 | 430个 | 2个 | 339ms | 11%  
  
简评：如果你关注联通的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **东京、洛杉矶、硅谷、西雅图、新加坡、达拉斯、芝加哥、亚特兰大** 的整体的连通速度、丢包率都比较不错，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

大陆移动到Vultr各机房的测速数据 [20180918] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 404个 | 0 | 116ms | 2% | 亚特兰大 | 395个 | 0 | 259ms | 4%  
新加坡 | 423个 | 1个 | 128ms | 1% | 悉尼 | 396个 | 1个 | 218ms | 2%  
洛杉矶 | 410个 | 0 | 204ms | 3% | 新泽西 | 418个 | 0 | 270ms | 1%  
硅谷 | 410个 | 0 | 211ms | 2% | 巴黎 | 415个 | 0 | 242ms | 4%  
西雅图 | 413个 | 1个 | 215ms | 4% | 法兰克福 | 399个 | 0 | 251ms | 4%  
达拉斯 | 390个 | 0 | 245ms | 2% | 迈阿密 | 399个 | 0 | 288ms | 3%  
均值 | 6093个 | 6个 | 229ms | 3% | 伦敦 | 395个 | 2个 | 265ms | 1%  
芝加哥 | 400个 | 0 | 258ms | 1% | 阿姆斯特丹 | 426个 | 1个 | 272ms | 5%  
  
简评：如果你关注移动的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **东京、新加坡、洛杉矶、硅谷、西雅图、悉尼、巴黎、达拉斯** 的整体的连通速度、丢包率都比较不错，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [四川](/vultr/isp/sichuan/20180918-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180918")
    * [天津](/vultr/isp/tianjin/20180918-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180918")
    * [西藏](/vultr/isp/tibet/20180918-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180918")
    * [新疆](/vultr/isp/xinjiang/20180918-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180918")
    * [云南](/vultr/isp/yunnan/20180918-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180918")
    * [浙江](/vultr/isp/zhejiang/20180918-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180918")
  * 大陆到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/china/20180514-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/china/20180527-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180527")
    * [20180622](/vultr/isp/china/20180622-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180622")
    * [20180804](/vultr/isp/china/20180804-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180804")
  * 本期报告：大陆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/china/20180918-bandwagon-isp-china.md "大陆到BandwagonHost各机房的Ping测试 20180918")
    * [Digital Ocean](/digitalocean/isp/china/20180918-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180918")
    * [Linode](/linode/isp/china/20180918-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180918")



本文最初发表于[大陆到Vultr各机房的测速数据（20180918）](https://vps123.top/pingtest/20180918-vultr-isp-china.html)
