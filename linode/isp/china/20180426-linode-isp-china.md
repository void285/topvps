#  中国大陆到Linode各机房的测速数据（20180426） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![中国大陆到Linode各机房的测速数据（20180426）](/images/thumbnails/China_to_linode.png)

本文的数据视角为 **中国大陆各省份/运营商到[Linode](https://vps123.top/go/linode)的各机房**的PING响应值、丢包率的比较；若你在大陆，打算在[Linode](https://vps123.top/go/linode)的机房架设代理服务器或进行云计算，后面的图表数据可以帮你形成评估Linode各机房的大概印象，排除一些数据较差的机房，锁定一些潜在的目标机房。要确定最适合你的机房，请通过本文结尾的链接，查看你所在省份的数据，它们更准确、针对性更强；你也可以通过文末链接查看其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

本文提供20180426中国大陆到Linode各机房的PING测试结果，测速点的运营商线路为电信、联通、移动，有效样本点6017个，其中超时点38个。连通概况如下：大陆线路响应均值为260毫秒，最快的三个机房所在地为东京、新加坡、佛利蒙，最慢的三个为亚特兰大、伦敦、法兰克福；伦敦、新加坡、佛利蒙、纽瓦克、亚特兰大等8处有响应超时情况；亚特兰大、法兰克福、伦敦、新加坡、达拉斯等7处丢包率较高。

[注册 Linode](https://vps123.top/go/linode/_btn1)

## 大陆图表数据

![大陆省份大陆到VPS提供商Linode各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180426](/images/pingtests/linode_20180426/plot_isp_china_linode_20180426.png)

### 全部运营商

**大陆全部运营商到Linode各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 805个 | 3个 | 124ms | 5%  
新加坡 | 811个 | 5个 | 173ms | 13%  
佛利蒙 | 292个 | 5个 | 174ms | 4%  
均值 | 6017个 | 38个 | 260ms | 12%  
达拉斯 | 835个 | 3个 | 292ms | 13%  
纽瓦克 | 829个 | 5个 | 296ms | 5%  
亚特兰大 | 825个 | 5个 | 300ms | 18%  
伦敦 | 810个 | 8个 | 314ms | 13%  
法兰克福 | 810个 | 4个 | 350ms | 17%  
  
**简评：** 本表展示了大陆的 **电信、联通、移动** 线路到Linode各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；籍此我们可以快速了解，整个大陆地区到Linode各个机房的平均响应速度以及丢包率：如果某机房的响应值、丢包率较高，那么大概率各省到此机房的网络也不理想，用来建站是不大合适的；而如果此处的响应值、丢包率还不错，我们可再具体了解一个省份的数据。  
在这里， **东京、佛利蒙** 的响应速度小于250ms，且丢包率在5%以内，值得关注。如果你主要关心某运营商的网络概况，后面几个表格的数据更有参考价值。  
如果你打算将VPS用作科学上网、云存储、远程任务、游戏服务器等用途，请 **关注你所在的省份** 到Linode各机房的测速数据，它们可以给你更有益的参考。

### 电信

**大陆电信到Linode各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 321个 | 2个 | 137ms | 9%  
新加坡 | 328个 | 4个 | 219ms | 8%  
佛利蒙 | 141个 | 3个 | 164ms | 1%  
均值 | 2433个 | 26个 | 273ms | 10%  
达拉斯 | 331个 | 2个 | 293ms | 7%  
纽瓦克 | 329个 | 3个 | 320ms | 6%  
亚特兰大 | 331个 | 3个 | 296ms | 15%  
伦敦 | 328个 | 6个 | 280ms | 10%  
法兰克福 | 324个 | 3个 | 414ms | 22%  
  
**简评：** 如果你关注电信的网络到Linode各机房的连通性，此表数据提供了一个不错的概览， **佛利蒙** 的整体的连通速度、丢包率都比较不错， **东京、新加坡** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_1)吧！

### 联通

**大陆联通到Linode各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 232个 | 1个 | 109ms | 2%  
新加坡 | 228个 | 1个 | 150ms | 4%  
佛利蒙 | 87个 | 2个 | 183ms | 9%  
均值 | 1709个 | 10个 | 247ms | 10%  
达拉斯 | 237个 | 1个 | 278ms | 17%  
纽瓦克 | 234个 | 1个 | 280ms | 6%  
亚特兰大 | 234个 | 2个 | 269ms | 13%  
伦敦 | 228个 | 1个 | 333ms | 12%  
法兰克福 | 229个 | 1个 | 334ms | 14%  
  
**简评：** 如果你关注联通的网络到Linode各机房的连通性，此表数据提供了一个不错的概览， **东京、新加坡** 的整体的连通速度、丢包率都比较不错， **佛利蒙** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_2)吧！

### 移动

**大陆移动到Linode各机房的测速数据 [20180426]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 252个 | 0 | 121ms | 3%  
新加坡 | 255个 | 0 | 135ms | 27%  
佛利蒙 | 64个 | 0 | 187ms | 3%  
均值 | 1875个 | 2个 | 255ms | 15%  
达拉斯 | 267个 | 0 | 305ms | 16%  
纽瓦克 | 266个 | 1个 | 280ms | 1%  
亚特兰大 | 260个 | 0 | 333ms | 27%  
伦敦 | 254个 | 1个 | 341ms | 19%  
法兰克福 | 257个 | 0 | 283ms | 12%  
  
**简评：** 如果你关注移动的网络到Linode各机房的连通性，此表数据提供了一个不错的概览， **东京、佛利蒙** 的整体的连通速度、丢包率都比较不错， **新加坡** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/linode/_3)吧！

[注册 Linode](https://vps123.top/go/linode/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180426) 
    * [全部](https://vps123.top/pingtests/20180426 "本期各VPS提供商全部测速报告")
    * [Linode](https://vps123.top/pingtests/idc-linode/20180426 "本期Linode的全部测速报告")
    * [各地到Linode某机房](https://vps123.top/pingtests/idc-linode/isp-global/20180426 "以Linode某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Linode各机房](https://vps123.top/pingtests/idc-linode/facility-all/20180426 "以大陆某省份为关注对象的视角，横向比较Linode各机房")
  * 本期 _其他省份_ 到Linode各机房的报告： 
    * [安徽](/linode/isp/anhui/20180426-linode-isp-anhui.md "安徽到Linode各机房的Ping测试 20180426")
    * [北京](/linode/isp/beijing/20180426-linode-isp-beijing.md "北京到Linode各机房的Ping测试 20180426")
    * [重庆](/linode/isp/chongqing/20180426-linode-isp-chongqing.md "重庆到Linode各机房的Ping测试 20180426")
    * [福建](/linode/isp/fujian/20180426-linode-isp-fujian.md "福建到Linode各机房的Ping测试 20180426")
    * [甘肃](/linode/isp/gansu/20180426-linode-isp-gansu.md "甘肃到Linode各机房的Ping测试 20180426")
    * [广东](/linode/isp/guangdong/20180426-linode-isp-guangdong.md "广东到Linode各机房的Ping测试 20180426")
    * [广西](/linode/isp/guangxi/20180426-linode-isp-guangxi.md "广西到Linode各机房的Ping测试 20180426")
    * [贵州](/linode/isp/guizhou/20180426-linode-isp-guizhou.md "贵州到Linode各机房的Ping测试 20180426")
    * [海南](/linode/isp/hainan/20180426-linode-isp-hainan.md "海南到Linode各机房的Ping测试 20180426")
    * [河北](/linode/isp/hebei/20180426-linode-isp-hebei.md "河北到Linode各机房的Ping测试 20180426")
    * [黑龙江](/linode/isp/heilongjiang/20180426-linode-isp-heilongjiang.md "黑龙江到Linode各机房的Ping测试 20180426")
    * [河南](/linode/isp/henan/20180426-linode-isp-henan.md "河南到Linode各机房的Ping测试 20180426")
    * [湖北](/linode/isp/hubei/20180426-linode-isp-hubei.md "湖北到Linode各机房的Ping测试 20180426")
    * [湖南](/linode/isp/hunan/20180426-linode-isp-hunan.md "湖南到Linode各机房的Ping测试 20180426")
    * [内蒙古](/linode/isp/innermongolia/20180426-linode-isp-innermongolia.md "内蒙古到Linode各机房的Ping测试 20180426")
    * [江苏](/linode/isp/jiangsu/20180426-linode-isp-jiangsu.md "江苏到Linode各机房的Ping测试 20180426")
    * [江西](/linode/isp/jiangxi/20180426-linode-isp-jiangxi.md "江西到Linode各机房的Ping测试 20180426")
    * [吉林](/linode/isp/jilin/20180426-linode-isp-jilin.md "吉林到Linode各机房的Ping测试 20180426")
    * [辽宁](/linode/isp/liaoning/20180426-linode-isp-liaoning.md "辽宁到Linode各机房的Ping测试 20180426")
    * [宁夏](/linode/isp/ningxia/20180426-linode-isp-ningxia.md "宁夏到Linode各机房的Ping测试 20180426")
    * [青海](/linode/isp/qinghai/20180426-linode-isp-qinghai.md "青海到Linode各机房的Ping测试 20180426")
    * [山西](/linode/isp/shan1xi/20180426-linode-isp-shan1xi.md "山西到Linode各机房的Ping测试 20180426")
    * [陕西](/linode/isp/shan3xi/20180426-linode-isp-shan3xi.md "陕西到Linode各机房的Ping测试 20180426")
    * [山东](/linode/isp/shandong/20180426-linode-isp-shandong.md "山东到Linode各机房的Ping测试 20180426")
    * [上海](/linode/isp/shanghai/20180426-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180426")
    * [四川](/linode/isp/sichuan/20180426-linode-isp-sichuan.md "四川到Linode各机房的Ping测试 20180426")
    * [天津](/linode/isp/tianjin/20180426-linode-isp-tianjin.md "天津到Linode各机房的Ping测试 20180426")
    * [西藏](/linode/isp/tibet/20180426-linode-isp-tibet.md "西藏到Linode各机房的Ping测试 20180426")
    * [新疆](/linode/isp/xinjiang/20180426-linode-isp-xinjiang.md "新疆到Linode各机房的Ping测试 20180426")
    * [云南](/linode/isp/yunnan/20180426-linode-isp-yunnan.md "云南到Linode各机房的Ping测试 20180426")
    * [浙江](/linode/isp/zhejiang/20180426-linode-isp-zhejiang.md "浙江到Linode各机房的Ping测试 20180426")
  * 大陆到Linode各机房的 _其他近期报告_ ： 
    * [20180514](/linode/isp/china/20180514-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180514")
    * [20180527](/linode/isp/china/20180527-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180527")
    * [20180622](/linode/isp/china/20180622-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180622")
    * [20180804](/linode/isp/china/20180804-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180804")
    * [20180918](/linode/isp/china/20180918-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180918")
  * 本期报告：大陆到 _其他VPS提供商_ 各机房的测速报告： 
    * [Vultr](/vultr/isp/china/20180426-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180426")
    * [BandwagonHost](/bandwagon/isp/china/20180426-bandwagon-isp-china.md "大陆到BandwagonHost各机房的Ping测试 20180426")
    * [Digital Ocean](/digitalocean/isp/china/20180426-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180426")



本文最初发表于[中国大陆到Linode各机房的测速数据（20180426）](https://vps123.top/pingtest/20180426-linode-isp-china.html)
