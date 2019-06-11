#  大陆到Linode各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![大陆到Linode各机房的测速数据（20180622）](/images/thumbnails/China_to_linode.png)

本文的数据视角为 **中国大陆各省份/运营商到[Linode](https://vps123.top/go/linode)的各机房**的PING响应值、丢包率的比较；若你在大陆，打算在[Linode](https://vps123.top/go/linode)的机房架设代理服务器或进行云计算，后面的图表数据可以帮你形成评估Linode各机房的大概印象，排除一些数据较差的机房，锁定一些潜在的目标机房。要确定最适合你的机房，请通过本文结尾的链接，查看你所在省份的数据，它们更准确、针对性更强；你也可以通过文末链接查看其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点6991个，其中超时点183个。连通概况如下：大陆线路响应均值为261毫秒，最快的三个机房所在地为东京、佛利蒙、达拉斯，最慢的三个为亚特兰大、纽瓦克、法兰克福；东京、新加坡、达拉斯、伦敦、亚特兰大等8处有响应超时情况；新加坡、东京、法兰克福丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆图表数据

![大陆省份大陆到VPS提供商Linode各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/linode_20180622/plot_isp_china_linode_20180622.png)

### 全部运营商

大陆全部运营商到Linode各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 850个 | 39个 | 181ms | 8% | 伦敦 | 867个 | 22个 | 267ms | 1%  
佛利蒙 | 885个 | 16个 | 196ms | 1% | 亚特兰大 | 884个 | 20个 | 275ms | 4%  
达拉斯 | 839个 | 22个 | 244ms | 1% | 纽瓦克 | 919个 | 17个 | 283ms | 4%  
均值 | 6991个 | 183个 | 261ms | 5% | 法兰克福 | 863个 | 18个 | 370ms | 6%  
新加坡 | 884个 | 29个 | 264ms | 12% |  |  |  |  |   
  
简评：本表展示了大陆的 **电信、联通、移动** 线路到Linode各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；籍此我们可以快速了解，整个大陆地区到Linode各个机房的平均响应速度以及丢包率：如果某机房的响应值、丢包率较高，那么大概率各省到此机房的网络也不理想，用来建站是不大合适的；而如果此处的响应值、丢包率还不错，我们可再具体了解一个省份的数据。  
在这里， **佛利蒙、达拉斯** 的响应速度小于250ms，且丢包率在5%以内，值得关注。如果你主要关心某运营商的网络概况，后面几个表格的数据更有参考价值。  
如果你打算将VPS用作科学上网、云存储、远程任务、游戏服务器等用途，请 **关注你所在的省份** 到Linode各机房的测速数据，它们可以给你更有益的参考。

### 电信

大陆电信到Linode各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 389个 | 23个 | 221ms | 15% | 伦敦 | 394个 | 12个 | 243ms | 0  
佛利蒙 | 398个 | 7个 | 187ms | 1% | 亚特兰大 | 398个 | 7个 | 269ms | 5%  
达拉斯 | 376个 | 7个 | 240ms | 1% | 纽瓦克 | 407个 | 6个 | 306ms | 5%  
均值 | 3140个 | 86个 | 280ms | 7% | 法兰克福 | 387个 | 7个 | 419ms | 11%  
新加坡 | 391个 | 17个 | 321ms | 18% |  |  |  |  |   
  
简评：如果你关注电信的网络到Linode各机房的连通性，此表数据提供了一个不错的概览， **佛利蒙、达拉斯、伦敦** 的整体的连通速度、丢包率都比较不错， **东京** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_1)吧！

### 联通

大陆联通到Linode各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 229个 | 10个 | 172ms | 5% | 伦敦 | 232个 | 5个 | 298ms | 1%  
佛利蒙 | 236个 | 4个 | 195ms | 1% | 亚特兰大 | 237个 | 7个 | 249ms | 2%  
达拉斯 | 229个 | 8个 | 238ms | 1% | 纽瓦克 | 250个 | 5个 | 261ms | 3%  
均值 | 1886个 | 50个 | 254ms | 3% | 法兰克福 | 230个 | 5个 | 356ms | 3%  
新加坡 | 243个 | 6个 | 258ms | 11% |  |  |  |  |   
  
简评：如果你关注联通的网络到Linode各机房的连通性，此表数据提供了一个不错的概览， **东京、佛利蒙、达拉斯、亚特兰大** 的整体的连通速度、丢包率都比较不错，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_2)吧！

### 移动

大陆移动到Linode各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 232个 | 6个 | 126ms | 2% | 伦敦 | 241个 | 5个 | 269ms | 2%  
佛利蒙 | 251个 | 5个 | 210ms | 3% | 亚特兰大 | 249个 | 6个 | 298ms | 3%  
达拉斯 | 234个 | 7个 | 254ms | 1% | 纽瓦克 | 262个 | 6个 | 278ms | 4%  
均值 | 1965个 | 47个 | 238ms | 3% | 法兰克福 | 246个 | 6个 | 274ms | 3%  
新加坡 | 250个 | 6个 | 186ms | 4% |  |  |  |  |   
  
简评：如果你关注移动的网络到Linode各机房的连通性，此表数据提供了一个不错的概览， **东京、新加坡、佛利蒙** 的整体的连通速度、丢包率都比较不错，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_3)吧！

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180622 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180622 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期 _其他省份_ 到Linode各机房的报告： 
    * [安徽](/linode/isp/anhui/20180622-linode-isp-anhui.md "安徽到Linode各机房的Ping测试 20180622")
    * [北京](/linode/isp/beijing/20180622-linode-isp-beijing.md "北京到Linode各机房的Ping测试 20180622")
    * [重庆](/linode/isp/chongqing/20180622-linode-isp-chongqing.md "重庆到Linode各机房的Ping测试 20180622")
    * [福建](/linode/isp/fujian/20180622-linode-isp-fujian.md "福建到Linode各机房的Ping测试 20180622")
    * [甘肃](/linode/isp/gansu/20180622-linode-isp-gansu.md "甘肃到Linode各机房的Ping测试 20180622")
    * [广东](/linode/isp/guangdong/20180622-linode-isp-guangdong.md "广东到Linode各机房的Ping测试 20180622")
    * [广西](/linode/isp/guangxi/20180622-linode-isp-guangxi.md "广西到Linode各机房的Ping测试 20180622")
    * [贵州](/linode/isp/guizhou/20180622-linode-isp-guizhou.md "贵州到Linode各机房的Ping测试 20180622")
    * [海南](/linode/isp/hainan/20180622-linode-isp-hainan.md "海南到Linode各机房的Ping测试 20180622")
    * [河北](/linode/isp/hebei/20180622-linode-isp-hebei.md "河北到Linode各机房的Ping测试 20180622")
    * [黑龙江](/linode/isp/heilongjiang/20180622-linode-isp-heilongjiang.md "黑龙江到Linode各机房的Ping测试 20180622")
    * [河南](/linode/isp/henan/20180622-linode-isp-henan.md "河南到Linode各机房的Ping测试 20180622")
    * [湖北](/linode/isp/hubei/20180622-linode-isp-hubei.md "湖北到Linode各机房的Ping测试 20180622")
    * [湖南](/linode/isp/hunan/20180622-linode-isp-hunan.md "湖南到Linode各机房的Ping测试 20180622")
    * [内蒙古](/linode/isp/innermongolia/20180622-linode-isp-innermongolia.md "内蒙古到Linode各机房的Ping测试 20180622")
    * [江苏](/linode/isp/jiangsu/20180622-linode-isp-jiangsu.md "江苏到Linode各机房的Ping测试 20180622")
    * [江西](/linode/isp/jiangxi/20180622-linode-isp-jiangxi.md "江西到Linode各机房的Ping测试 20180622")
    * [吉林](/linode/isp/jilin/20180622-linode-isp-jilin.md "吉林到Linode各机房的Ping测试 20180622")
    * [辽宁](/linode/isp/liaoning/20180622-linode-isp-liaoning.md "辽宁到Linode各机房的Ping测试 20180622")
    * [宁夏](/linode/isp/ningxia/20180622-linode-isp-ningxia.md "宁夏到Linode各机房的Ping测试 20180622")
    * [青海](/linode/isp/qinghai/20180622-linode-isp-qinghai.md "青海到Linode各机房的Ping测试 20180622")
    * [山西](/linode/isp/shan1xi/20180622-linode-isp-shan1xi.md "山西到Linode各机房的Ping测试 20180622")
    * [陕西](/linode/isp/shan3xi/20180622-linode-isp-shan3xi.md "陕西到Linode各机房的Ping测试 20180622")
    * [山东](/linode/isp/shandong/20180622-linode-isp-shandong.md "山东到Linode各机房的Ping测试 20180622")
    * [上海](/linode/isp/shanghai/20180622-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180622")
    * [四川](/linode/isp/sichuan/20180622-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180622")
    * [天津](/linode/isp/tianjin/20180622-linode-isp-tianjin.md "天津到Linode各机房的Ping测试 20180622")
    * [新疆](/linode/isp/xinjiang/20180622-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180622")
    * [云南](/linode/isp/yunnan/20180622-linode-isp-yunnan.md "云南到Linode各机房的Ping测试 20180622")
    * [浙江](/linode/isp/zhejiang/20180622-linode-isp-zhejiang.md "浙江到Linode各机房的Ping测试 20180622")
  * 大陆到Linode各机房的 _其他近期报告_ ： 
    * [20180514](/linode/isp/china/20180514-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180514")
    * [20180527](/linode/isp/china/20180527-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180527")
    * [20180804](/linode/isp/china/20180804-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180804")
    * [20180918](/linode/isp/china/20180918-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180918")
  * 本期报告：大陆到 _其他VPS提供商_ 各机房的测速报告： 
    * [Vultr](/vultr/isp/china/20180622-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180622")
    * [BandwagonHost](/bandwagon/isp/china/20180622-bandwagon-isp-china.md "大陆到BandwagonHost各机房的Ping测试 20180622")
    * [Digital Ocean](/digitalocean/isp/china/20180622-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180622")



本文最初发表于[大陆到Linode各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-linode-isp-china.html)
