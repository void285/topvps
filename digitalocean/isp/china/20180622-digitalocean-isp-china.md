#  大陆到Digital Ocean各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![大陆到Digital Ocean各机房的测速数据（20180622）](/images/thumbnails/China_to_digitalocean.png)

本文的数据视角为 **中国大陆各省份/运营商到[Digital Ocean](https://vps123.top/go/do)的各机房**的PING响应值、丢包率的比较；若你在大陆，打算在[Digital Ocean](https://vps123.top/go/do)的机房架设代理服务器或进行云计算，后面的图表数据可以帮你形成评估Digital Ocean各机房的大概印象，排除一些数据较差的机房，锁定一些潜在的目标机房。要确定最适合你的机房，请通过本文结尾的链接，查看你所在省份的数据，它们更准确、针对性更强；你也可以通过文末链接查看其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点9057个，其中超时点246个。连通概况如下：大陆线路响应均值为280毫秒，最快的三个机房所在地为旧金山、多伦多、伦敦，最慢的三个为纽约、阿姆斯特丹、班加罗尔；纽约、旧金山、阿姆斯特丹、多伦多、法兰克福等8处有响应超时情况；新加坡丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 大陆图表数据

![大陆省份大陆到VPS提供商Digital Ocean各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_isp_china_do_20180622.png)

### 全部运营商

**大陆全部运营商到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 1724个 | 48个 | 233ms | 2%  
多伦多 | 872个 | 25个 | 255ms | 1%  
伦敦 | 833个 | 16个 | 268ms | 0  
新加坡 | 263个 | 19个 | 270ms | 15%  
法兰克福 | 884个 | 21个 | 279ms | 1%  
均值 | 9057个 | 246个 | 280ms | 2%  
纽约 | 1916个 | 52个 | 295ms | 2%  
阿姆斯特丹 | 1701个 | 44个 | 296ms | 3%  
班加罗尔 | 864个 | 21个 | 347ms | 1%  
  
**简评：** 本表展示了大陆的 **电信、联通、移动** 线路到Digital Ocean各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；籍此我们可以快速了解，整个大陆地区到Digital Ocean各个机房的平均响应速度以及丢包率：如果某机房的响应值、丢包率较高，那么大概率各省到此机房的网络也不理想，用来建站是不大合适的；而如果此处的响应值、丢包率还不错，我们可再具体了解一个省份的数据。  
在这里， **旧金山** 的响应速度小于250ms，且丢包率在5%以内，值得关注。如果你主要关心某运营商的网络概况，后面几个表格的数据更有参考价值。  
如果你打算将VPS用作科学上网、云存储、远程任务、游戏服务器等用途，请 **关注你所在的省份** 到Digital Ocean各机房的测速数据，它们可以给你更有益的参考。

### 电信

**大陆电信到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 777个 | 27个 | 253ms | 3%  
多伦多 | 397个 | 12个 | 245ms | 1%  
伦敦 | 367个 | 6个 | 244ms | 1%  
新加坡 | 165个 | 14个 | 320ms | 24%  
法兰克福 | 386个 | 7个 | 251ms | 1%  
均值 | 4142个 | 118个 | 283ms | 3%  
纽约 | 889个 | 20个 | 304ms | 1%  
阿姆斯特丹 | 771个 | 20个 | 284ms | 2%  
班加罗尔 | 390个 | 12个 | 395ms | 1%  
  
**简评：** 如果你关注电信的网络到Digital Ocean各机房的连通性，此表数据提供了一个不错的概览， **伦敦、多伦多** 的整体的连通速度、丢包率都比较不错，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/do/_1)吧！

### 联通

**大陆联通到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 465个 | 11个 | 217ms | 2%  
多伦多 | 238个 | 8个 | 258ms | 1%  
伦敦 | 229个 | 5个 | 295ms | 0  
新加坡 | 62个 | 4个 | 278ms | 0  
法兰克福 | 242个 | 8个 | 308ms | 2%  
均值 | 2441个 | 67个 | 285ms | 1%  
纽约 | 519个 | 17个 | 306ms | 2%  
阿姆斯特丹 | 454个 | 10个 | 313ms | 2%  
班加罗尔 | 232个 | 4个 | 339ms | 1%  
  
**简评：** 如果你关注联通的网络到Digital Ocean各机房的连通性，此表数据提供了一个不错的概览， **旧金山** 的整体的连通速度、丢包率都比较不错，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/do/_2)吧！

### 移动

**大陆移动到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 482个 | 10个 | 221ms | 1%  
多伦多 | 237个 | 5个 | 266ms | 0  
伦敦 | 237个 | 5个 | 277ms | 1%  
新加坡 | 36个 | 1个 | 103ms | 0  
法兰克福 | 256个 | 6个 | 290ms | 3%  
均值 | 2474个 | 61个 | 270ms | 2%  
纽约 | 508个 | 15个 | 280ms | 2%  
阿姆斯特丹 | 476个 | 14个 | 297ms | 3%  
班加罗尔 | 242个 | 5个 | 289ms | 1%  
  
**简评：** 如果你关注移动的网络到Digital Ocean各机房的连通性，此表数据提供了一个不错的概览， **新加坡、旧金山** 的整体的连通速度、丢包率都比较不错，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/do/_3)吧！

[注册 Digital Ocean](https://vps123.top/go/do/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Digital Ocean](https://vps123.top/pingtests/idc-digitalocean/20180622 "本期Digital Ocean的全部测速报告")
    * [各地到Digital Ocean某机房](https://vps123.top/pingtests/idc-digitalocean/isp-global/20180622 "以Digital Ocean某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Digital Ocean各机房](https://vps123.top/pingtests/idc-digitalocean/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Digital Ocean各机房")
  * 本期 _其他省份_ 到Digital Ocean各机房的报告： 
    * [安徽](/digitalocean/isp/anhui/20180622-digitalocean-isp-anhui.md "安徽到Digital Ocean各机房的Ping测试 20180622")
    * [北京](/digitalocean/isp/beijing/20180622-digitalocean-isp-beijing.md "北京到Digital Ocean各机房的Ping测试 20180622")
    * [重庆](/digitalocean/isp/chongqing/20180622-digitalocean-isp-chongqing.md "重庆到Digital Ocean各机房的Ping测试 20180622")
    * [福建](/digitalocean/isp/fujian/20180622-digitalocean-isp-fujian.md "福建到Digital Ocean各机房的Ping测试 20180622")
    * [甘肃](/digitalocean/isp/gansu/20180622-digitalocean-isp-gansu.md "甘肃到Digital Ocean各机房的Ping测试 20180622")
    * [广东](/digitalocean/isp/guangdong/20180622-digitalocean-isp-guangdong.md "广东到Digital Ocean各机房的Ping测试 20180622")
    * [广西](/digitalocean/isp/guangxi/20180622-digitalocean-isp-guangxi.md "广西到Digital Ocean各机房的Ping测试 20180622")
    * [贵州](/digitalocean/isp/guizhou/20180622-digitalocean-isp-guizhou.md "贵州到Digital Ocean各机房的Ping测试 20180622")
    * [海南](/digitalocean/isp/hainan/20180622-digitalocean-isp-hainan.md "海南到Digital Ocean各机房的Ping测试 20180622")
    * [河北](/digitalocean/isp/hebei/20180622-digitalocean-isp-hebei.md "河北到Digital Ocean各机房的Ping测试 20180622")
    * [黑龙江](/digitalocean/isp/heilongjiang/20180622-digitalocean-isp-heilongjiang.md "黑龙江到Digital Ocean各机房的Ping测试 20180622")
    * [河南](/digitalocean/isp/henan/20180622-digitalocean-isp-henan.md "河南到Digital Ocean各机房的Ping测试 20180622")
    * [湖北](/digitalocean/isp/hubei/20180622-digitalocean-isp-hubei.md "湖北到Digital Ocean各机房的Ping测试 20180622")
    * [湖南](/digitalocean/isp/hunan/20180622-digitalocean-isp-hunan.md "湖南到Digital Ocean各机房的Ping测试 20180622")
    * [内蒙古](/digitalocean/isp/innermongolia/20180622-digitalocean-isp-innermongolia.md "内蒙古到Digital Ocean各机房的Ping测试 20180622")
    * [江苏](/digitalocean/isp/jiangsu/20180622-digitalocean-isp-jiangsu.md "江苏到Digital Ocean各机房的Ping测试 20180622")
    * [江西](/digitalocean/isp/jiangxi/20180622-digitalocean-isp-jiangxi.md "江西到Digital Ocean各机房的Ping测试 20180622")
    * [吉林](/digitalocean/isp/jilin/20180622-digitalocean-isp-jilin.md "吉林到Digital Ocean各机房的Ping测试 20180622")
    * [辽宁](/digitalocean/isp/liaoning/20180622-digitalocean-isp-liaoning.md "辽宁到Digital Ocean各机房的Ping测试 20180622")
    * [宁夏](/digitalocean/isp/ningxia/20180622-digitalocean-isp-ningxia.md "宁夏到Digital Ocean各机房的Ping测试 20180622")
    * [青海](/digitalocean/isp/qinghai/20180622-digitalocean-isp-qinghai.md "青海到Digital Ocean各机房的Ping测试 20180622")
    * [山西](/digitalocean/isp/shan1xi/20180622-digitalocean-isp-shan1xi.md "山西到Digital Ocean各机房的Ping测试 20180622")
    * [陕西](/digitalocean/isp/shan3xi/20180622-digitalocean-isp-shan3xi.md "陕西到Digital Ocean各机房的Ping测试 20180622")
    * [山东](/digitalocean/isp/shandong/20180622-digitalocean-isp-shandong.md "山东到Digital Ocean各机房的Ping测试 20180622")
    * [上海](/digitalocean/isp/shanghai/20180622-digitalocean-isp-shanghai.md "上海到Digital Ocean各机房的Ping测试 20180622")
    * [四川](/digitalocean/isp/sichuan/20180622-digitalocean-isp-sichuan.md "四川到Digital Ocean各机房的Ping测试 20180622")
    * [天津](/digitalocean/isp/tianjin/20180622-digitalocean-isp-tianjin.md "天津到Digital Ocean各机房的Ping测试 20180622")
    * [西藏](/digitalocean/isp/tibet/20180622-digitalocean-isp-tibet.md "西藏到Digital Ocean各机房的Ping测试 20180622")
    * [新疆](/digitalocean/isp/xinjiang/20180622-digitalocean-isp-xinjiang.md "新疆到Digital Ocean各机房的Ping测试 20180622")
    * [云南](/digitalocean/isp/yunnan/20180622-digitalocean-isp-yunnan.md "云南到Digital Ocean各机房的Ping测试 20180622")
    * [浙江](/digitalocean/isp/zhejiang/20180622-digitalocean-isp-zhejiang.md "浙江到Digital Ocean各机房的Ping测试 20180622")
  * 大陆到Digital Ocean各机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/isp/china/20180514-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180514")
    * [20180527](/digitalocean/isp/china/20180527-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180527")
    * [20180804](/digitalocean/isp/china/20180804-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180804")
    * [20180918](/digitalocean/isp/china/20180918-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180918")
  * 本期报告：大陆到 _其他VPS提供商_ 各机房的测速报告： 
    * [Vultr](/vultr/isp/china/20180622-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180622")
    * [BandwagonHost](/bandwagon/isp/china/20180622-bandwagon-isp-china.md "大陆到BandwagonHost各机房的Ping测试 20180622")
    * [Linode](/linode/isp/china/20180622-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180622")



本文最初发表于[大陆到Digital Ocean各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-digitalocean-isp-china.html)
