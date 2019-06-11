#  广东到Vultr各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![广东到Vultr各机房的测速数据（20180622）](/images/thumbnails/Guangdong_to_vultr.png)

本文的数据视角为 **广东到[Vultr](https://vps123.top/go/vultr)的各机房**的PING响应值、丢包率的比较；若你在广东且打算运行[Vultr](https://vps123.top/go/vultr)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Vultr的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点1117个，其中超时点27个。连通概况如下：大陆线路响应均值为244毫秒，最快的三个机房所在地为东京、新加坡、洛杉矶，最慢的三个为迈阿密、阿姆斯特丹、伦敦；法兰克福、新泽西、东京、芝加哥、新加坡等11处有响应超时情况；亚特兰大、芝加哥、迈阿密、伦敦、东京等6处丢包率较高。

[注册 Vultr](https://vps123.top/go/vultr/_btn1)

## 广东图表数据

![大陆省份广东到VPS提供商Vultr各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/vultr_20180622/plot_isp_guangdong_vultr_20180622.png)

### 全部运营商

广东全部运营商到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 75个 | 2个 | 135ms | 6% | 巴黎 | 75个 | 1个 | 261ms | 0  
新加坡 | 78个 | 1个 | 179ms | 5% | 法兰克福 | 80个 | 13个 | 263ms | 0  
洛杉矶 | 75个 | 0 | 192ms | 1% | 芝加哥 | 73个 | 2个 | 288ms | 17%  
西雅图 | 70个 | 1个 | 199ms | 3% | 亚特兰大 | 70个 | 0 | 288ms | 19%  
硅谷 | 80个 | 1个 | 215ms | 1% | 新泽西 | 74个 | 3个 | 289ms | 2%  
达拉斯 | 71个 | 1个 | 229ms | 1% | 迈阿密 | 70个 | 1个 | 303ms | 15%  
均值 | 1117个 | 27个 | 244ms | 6% | 阿姆斯特丹 | 75个 | 0 | 308ms | 1%  
悉尼 | 76个 | 1个 | 247ms | 5% | 伦敦 | 75个 | 0 | 310ms | 11%  
  
简评：本表展示了广东的 **电信、联通、移动** 线路到Vultr各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻广东，可从此表了解你常用的网络到Vultr各个机房的平均响应速度以及丢包率。从表中数据可以看到， **新加坡、洛杉矶、西雅图、硅谷、达拉斯、悉尼** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

广东电信到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 41个 | 2个 | 214ms | 15% | 巴黎 | 44个 | 1个 | 247ms | 0  
新加坡 | 45个 | 1个 | 286ms | 10% | 法兰克福 | 43个 | 10个 | 239ms | 0  
洛杉矶 | 44个 | 0 | 213ms | 4% | 芝加哥 | 44个 | 1个 | 308ms | 5%  
西雅图 | 43个 | 0 | 237ms | 8% | 亚特兰大 | 43个 | 0 | 279ms | 7%  
硅谷 | 42个 | 1个 | 241ms | 2% | 新泽西 | 43个 | 3个 | 320ms | 2%  
达拉斯 | 42个 | 1个 | 241ms | 3% | 迈阿密 | 42个 | 0 | 297ms | 3%  
均值 | 647个 | 21个 | 264ms | 5% | 阿姆斯特丹 | 44个 | 0 | 312ms | 1%  
悉尼 | 45个 | 1个 | 332ms | 10% | 伦敦 | 42个 | 0 | 303ms | 2%  
  
简评：如果你是来自广东的 **电信** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **洛杉矶、法兰克福、硅谷、达拉斯、巴黎** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **东京、西雅图** 的机房，即使这几个城市离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_1)吧！

### 联通

广东联通到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 16个 | 0 | 113ms | 2% | 巴黎 | 14个 | 0 | 299ms | 0  
新加坡 | 14个 | 0 | 192ms | 5% | 法兰克福 | 17个 | 1个 | 311ms | 0  
洛杉矶 | 13个 | 0 | 188ms | 0 | 芝加哥 | 17个 | 1个 | 338ms | 46%  
西雅图 | 17个 | 1个 | 206ms | 0 | 亚特兰大 | 16个 | 0 | 328ms | 46%  
硅谷 | 16个 | 0 | 206ms | 0 | 新泽西 | 17个 | 0 | 312ms | 3%  
达拉斯 | 16个 | 0 | 236ms | 0 | 迈阿密 | 16个 | 1个 | 351ms | 43%  
均值 | 233个 | 4个 | 274ms | 13% | 阿姆斯特丹 | 14个 | 0 | 355ms | 1%  
悉尼 | 14个 | 0 | 247ms | 4% | 伦敦 | 16个 | 0 | 374ms | 31%  
  
简评：如果你是来自广东的 **联通** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **东京、洛杉矶、新加坡、西雅图、硅谷、达拉斯、悉尼** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_2)吧！

### 移动

广东移动到Vultr各机房的测速数据 [20180622] 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率 | 机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---|---|---|---|---|---  
东京 | 18个 | 0 | 78ms | 0 | 巴黎 | 17个 | 0 | 238ms | 0  
新加坡 | 19个 | 0 | 58ms | 0 | 法兰克福 | 20个 | 2个 | 241ms | 0  
洛杉矶 | 18个 | 0 | 173ms | 0 | 芝加哥 | 12个 | 0 | 219ms | 0  
西雅图 | 10个 | 0 | 153ms | 0 | 亚特兰大 | 11个 | 0 | 256ms | 5%  
硅谷 | 22个 | 0 | 198ms | 0 | 新泽西 | 14个 | 0 | 234ms | 0  
达拉斯 | 13个 | 0 | 210ms | 0 | 迈阿密 | 12个 | 0 | 260ms | 0  
均值 | 237个 | 2个 | 194ms | 0 | 阿姆斯特丹 | 17个 | 0 | 257ms | 0  
悉尼 | 17个 | 0 | 163ms | 0 | 伦敦 | 17个 | 0 | 254ms | 0  
  
简评：如果你是来自广东的 **移动** 用户，想运行Vultr的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **新加坡、东京、西雅图、悉尼、洛杉矶、硅谷、达拉斯、芝加哥、新泽西、巴黎、法兰克福** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/vultr/_3)吧！

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
    * [大陆](/vultr/isp/china/20180622-vultr-isp-china.md "大陆到Vultr各机房的Ping测试 20180622")
    * [重庆](/vultr/isp/chongqing/20180622-vultr-isp-chongqing.md "重庆到Vultr各机房的Ping测试 20180622")
    * [福建](/vultr/isp/fujian/20180622-vultr-isp-fujian.md "福建到Vultr各机房的Ping测试 20180622")
    * [甘肃](/vultr/isp/gansu/20180622-vultr-isp-gansu.md "甘肃到Vultr各机房的Ping测试 20180622")
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
  * 广东到Vultr各机房的 _其他近期报告_ ： 
    * [20180514](/vultr/isp/guangdong/20180514-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180514")
    * [20180527](/vultr/isp/guangdong/20180527-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180527")
    * [20180804](/vultr/isp/guangdong/20180804-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180804")
    * [20180918](/vultr/isp/guangdong/20180918-vultr-isp-guangdong.md "广东到Vultr各机房的Ping测试 20180918")
  * 本期报告：广东到 _其他VPS提供商_ 各机房的测速报告： 
    * [BandwagonHost](/bandwagon/isp/guangdong/20180622-bandwagon-isp-guangdong.md "广东到BandwagonHost各机房的Ping测试 20180622")
    * [Digital Ocean](/digitalocean/isp/guangdong/20180622-digitalocean-isp-guangdong.md "广东到Digital Ocean各机房的Ping测试 20180622")
    * [Linode](/linode/isp/guangdong/20180622-linode-isp-guangdong.md "广东到Linode各机房的Ping测试 20180622")



本文最初发表于[广东到Vultr各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-vultr-isp-guangdong.html)
