#  大陆到Vultr各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![大陆到Vultr各机房的测速数据（20180622）](/images/thumbnails/China_to_vultr.png)

本文的数据视角为 **中国大陆各省份/运营商到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在大陆，打算在[Vultr](https://vps123.top/go/vultr)的机房架设代理服务器或进行云计算，后面的图表数据可以帮你形成评估Vultr各机房的大概印象，排除一些数据较差的机房，锁定一些潜在的目标机房。要确定最适合你的机房，请通过本文结尾的链接，查看你所在省份的数据，它们更准确、针对性更强；你也可以通过文末链接查看其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点13235个，其中超时点420个。连通概况如下：大陆线路响应均值为263毫秒，最快的三个机房所在地为东京、洛杉矶、硅谷，最慢的三个为迈阿密、伦敦、阿姆斯特丹；法兰克福、西雅图、新加坡、悉尼、东京等15处有响应超时情况；芝加哥、亚特兰大、迈阿密、东京、伦敦等7处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 大陆图表数据

![大陆省份大陆到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_isp_china_vultr_20180622.png)

### 全部运营商

**大陆全部运营商到Vultr各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 901个 | 29个 | 181ms | 11%  
洛杉矶 | 858个 | 26个 | 212ms | 2%  
硅谷 | 908个 | 6个 | 216ms | 1%  
西雅图 | 890个 | 36个 | 221ms | 3%  
新加坡 | 868个 | 35个 | 235ms | 9%  
达拉斯 | 862个 | 21个 | 247ms | 1%  
均值 | 13235个 | 420个 | 263ms | 7%  
巴黎 | 862个 | 20个 | 265ms | 0  
法兰克福 | 906个 | 78个 | 269ms | 1%  
芝加哥 | 900个 | 23个 | 284ms | 17%  
亚特兰大 | 869个 | 27个 | 287ms | 16%  
新泽西 | 882个 | 26个 | 298ms | 2%  
悉尼 | 865个 | 31个 | 304ms | 7%  
迈阿密 | 903个 | 22个 | 305ms | 16%  
伦敦 | 898个 | 17个 | 308ms | 10%  
阿姆斯特丹 | 863个 | 23个 | 317ms | 1%  
  
**简评：** 本表展示了大陆的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；籍此我们可以快速了解，整个大陆地区到Vultr各个机房的平均响应速度以及丢包率：如果某机房的响应值、丢包率较高，那么大概率各省到此机房的网络也不理想，用来建站是不大合适的；而如果此处的响应值、丢包率还不错，我们可再具体了解一个省份的数据。  
在这里， **洛杉矶、硅谷、西雅图、达拉斯** 的响应速度小于250ms，且丢包率在5%以内，值得关注。如果你主要关心某运营商的网络概况，后面几个表格的数据更有参考价值。  
如果你打算将VPS用作科学上网、云存储、远程任务、游戏服务器等用途，请 **关注你所在的省份** 到Vultr各机房的测速数据，它们可以给你更有益的参考。

### 电信

**大陆电信到Vultr各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 401个 | 18个 | 219ms | 20%  
洛杉矶 | 393个 | 12个 | 231ms | 4%  
硅谷 | 411个 | 4个 | 231ms | 2%  
西雅图 | 403个 | 15个 | 237ms | 4%  
新加坡 | 397个 | 17个 | 282ms | 16%  
达拉斯 | 387个 | 9个 | 264ms | 2%  
均值 | 5982个 | 217个 | 277ms | 6%  
巴黎 | 394个 | 8个 | 241ms | 0  
法兰克福 | 411个 | 54个 | 242ms | 1%  
芝加哥 | 403个 | 10个 | 295ms | 7%  
亚特兰大 | 393个 | 16个 | 291ms | 7%  
新泽西 | 394个 | 14个 | 328ms | 2%  
悉尼 | 401个 | 15个 | 364ms | 12%  
迈阿密 | 406个 | 8个 | 315ms | 7%  
伦敦 | 397个 | 6个 | 318ms | 4%  
阿姆斯特丹 | 391个 | 11个 | 333ms | 1%  
  
**简评：** 如果你关注电信的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **洛杉矶、硅谷、西雅图、巴黎、法兰克福** 的整体的连通速度、丢包率都比较不错， **东京** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

**大陆联通到Vultr各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 243个 | 5个 | 180ms | 6%  
洛杉矶 | 235个 | 7个 | 200ms | 0  
硅谷 | 248个 | 1个 | 198ms | 0  
西雅图 | 245个 | 10个 | 209ms | 1%  
新加坡 | 234个 | 11个 | 245ms | 6%  
达拉斯 | 235个 | 6个 | 229ms | 0  
均值 | 3599个 | 106个 | 265ms | 12%  
巴黎 | 237个 | 6个 | 293ms | 0  
法兰克福 | 243个 | 18个 | 316ms | 3%  
芝加哥 | 244个 | 7个 | 299ms | 43%  
亚特兰大 | 233个 | 4个 | 291ms | 42%  
新泽西 | 240个 | 5个 | 284ms | 2%  
悉尼 | 234个 | 8个 | 284ms | 4%  
迈阿密 | 243个 | 6个 | 306ms | 41%  
伦敦 | 246个 | 5个 | 331ms | 29%  
阿姆斯特丹 | 239个 | 7个 | 325ms | 1%  
  
**简评：** 如果你关注联通的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **硅谷、洛杉矶、西雅图、达拉斯** 的整体的连通速度、丢包率都比较不错， **东京、新加坡** 也值得关注，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

**大陆移动到Vultr各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
东京 | 257个 | 6个 | 128ms | 3%  
洛杉矶 | 230个 | 7个 | 206ms | 1%  
硅谷 | 249个 | 1个 | 221ms | 0  
西雅图 | 242个 | 11个 | 212ms | 4%  
新加坡 | 237个 | 7个 | 155ms | 3%  
达拉斯 | 240个 | 6个 | 248ms | 1%  
均值 | 3654个 | 97个 | 241ms | 3%  
巴黎 | 231个 | 6个 | 273ms | 0  
法兰克福 | 252个 | 6个 | 264ms | 0  
芝加哥 | 253个 | 6个 | 263ms | 8%  
亚特兰大 | 243个 | 7个 | 281ms | 6%  
新泽西 | 248个 | 7个 | 278ms | 3%  
悉尼 | 230个 | 8个 | 226ms | 2%  
迈阿密 | 254个 | 8个 | 292ms | 7%  
伦敦 | 255个 | 6个 | 275ms | 3%  
阿姆斯特丹 | 233个 | 5个 | 290ms | 1%  
  
**简评：** 如果你关注移动的网络到Vultr各机房的连通性，此表数据提供了一个不错的概览， **东京、新加坡、洛杉矶、西雅图、硅谷、悉尼、达拉斯** 的整体的连通速度、丢包率都比较不错，如果要选择一个机房用于科学上网、云存储、远程任务、游戏服务器等用途，请查看你所在的省份的更具体的测评。如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

[注册 Vultr](https://vps123.top/go/vultr/_btn2)

## 相关测速报告

  * 本期测速报告归档 (20180622) 
    * [全部](https://vps123.top/pingtests/20180622 "本期各VPS提供商全部测速报告")
    * [Vultr](https://vps123.top/pingtests/idc-vultr/20180622 "本期Vultr的全部测速报告")
    * [各地到Vultr某机房](https://vps123.top/pingtests/idc-vultr/isp-global/20180622 "以Vultr某机房为关注对象的视角，横向比较大陆各省份、海外各国家地区")
    * [某地到Vultr各机房](https://vps123.top/pingtests/idc-vultr/facility-all/20180622 "以大陆某省份为关注对象的视角，横向比较Vultr各机房")
  * 本期 _其他省份_ 到Vultr各机房的报告： 
    * [安徽](/vultr/isp/anhui/20180622-vultr-isp-anhui.md "安徽到Vultr各机房的Ping测试 20180622")
    * [北京](/vultr/isp/beijing/20180622-vultr-isp-beijing.md "北京到Vultr各机房的Ping测试 20180622")
    * [重庆](/vultr/isp/chongqing/20180622-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180622")
    * [福建](/vultr/isp/fujian/20180622-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180622")
    * [甘肃](/vultr/isp/gansu/20180622-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180622")
    * [广东](/vultr/isp/guangdong/20180622-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180622")
    * [广西](/vultr/isp/guangxi/20180622-vultr-isp-guangxi.md "广西到Vultr各机房的Ping测试 20180622")
    * [贵州](/vultr/isp/guizhou/20180622-vultr-isp-guizhou.md "贵州到Vultr各机房的Ping测试 20180622")
    * [海南](/vultr/isp/hainan/20180622-vultr-isp-hainan.md "海南到Vultr各机房的Ping测试 20180622")
    * [河北](/vultr/isp/hebei/20180622-vultr-isp-hebei.md "河北到Vultr各机房的Ping测试 20180622")
    * [黑龙江](/vultr/isp/heilongjiang/20180622-vultr-isp-heilongjiang.md "黑龙江到Vultr各机房的Ping测试 20180622")
    * [河南](/vultr/isp/henan/20180622-vultr-isp-henan.md "河南到Vultr各机房的Ping测试 20180622")
    * [湖北](/vultr/isp/hubei/20180622-vultr-isp-hubei.md "湖北到Vultr各机房的Ping测试 20180622")
    * [湖南](/vultr/isp/hunan/20180622-vultr-isp-hunan.md "湖南到Vultr各机房的Ping测试 20180622")
    * [内蒙古](/vultr/isp/innermongolia/20180622-vultr-isp-innermongolia.md "内蒙古到Vultr各机房的Ping测试 20180622")
    * [江苏](/vultr/isp/jiangsu/20180622-vultr-isp-jiangsu.md "江苏到Vultr各机房的Ping测试 20180622")
    * [江西](/vultr/isp/jiangxi/20180622-vultr-isp-jiangxi.md "江西到Vultr各机房的Ping测试 20180622")
    * [吉林](/vultr/isp/jilin/20180622-vultr-isp-jilin.md "吉林到Vultr各机房的Ping测试 20180622")
    * [辽宁](/vultr/isp/liaoning/20180622-vultr-isp-liaoning.md "辽宁到Vultr各机房的Ping测试 20180622")
    * [宁夏](/vultr/isp/ningxia/20180622-vultr-isp-ningxia.md "宁夏到Vultr各机房的Ping测试 20180622")
    * [青海](/vultr/isp/qinghai/20180622-vultr-isp-qinghai.md "青海到Vultr各机房的Ping测试 20180622")
    * [山西](/vultr/isp/shan1xi/20180622-vultr-isp-shan1xi.md "山西到Vultr各机房的Ping测试 20180622")
    * [陕西](/vultr/isp/shan3xi/20180622-vultr-isp-shan3xi.md "陕西到Vultr各机房的Ping测试 20180622")
    * [山东](/vultr/isp/shandong/20180622-vultr-isp-shandong.md "山东到Vultr各机房的Ping测试 20180622")
    * [上海](/vultr/isp/shanghai/20180622-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180622")
    * [四川](/vultr/isp/sichuan/20180622-vultr-isp-sichuan.md "四川到Vultr各机房的Ping测试 20180622")
    * [天津](/vultr/isp/tianjin/20180622-vultr-isp-tianjin.md "天津到Vultr各机房的Ping测试 20180622")
    * [西藏](/vultr/isp/tibet/20180622-vultr-isp-tibet.md "西藏到Vultr各机房的Ping测试 20180622")
    * [新疆](/vultr/isp/xinjiang/20180622-vultr-isp-xinjiang.md "新疆到Vultr各机房的Ping测试 20180622")
    * [云南](/vultr/isp/yunnan/20180622-vultr-isp-yunnan.md "云南到Vultr各机房的Ping测试 20180622")
    * [浙江](/vultr/isp/zhejiang/20180622-vultr-isp-zhejiang.md "浙江到Vultr各机房的Ping测试 20180622")
  * 大陆到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/china/20180514-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/china/20180527-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180527")
    * [20180804](/vultr/isp/china/20180804-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/china/20180918-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180918")
  * 本期报告：大陆到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/china/20180622-bandwagon-isp-china.md "大陆到BandwagonHost各机房的Ping测试 20180622")
    * [Digital Ocean](/digitalocean/isp/china/20180622-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180622")
    * [Linode](/linode/isp/china/20180622-linode-isp-china.md "大陆到Linode各机房的Ping测试 20180622")



本文最初发表于[大陆到Vultr各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-vultr-isp-china.html)
