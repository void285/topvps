#  上海到Digital Ocean各机房的测速数据（20180622） 

## 导读

本文是[TopVPS主机网络测试报告系列](https://vps123.top/pingtest)的一部分，主要提供PING测试的响应速度、丢包率等数据，关于PING指令以及响应速度、丢包率的指标意义，请看[这里](https://vps123.top/what-is-ping.html)。

![上海到Digital Ocean各机房的测速数据（20180622）](/images/thumbnails/Shanghai_to_digitalocean.png)

本文的数据视角为 **上海到[Digital Ocean](https://vps123.top/go/do)的各机房**的PING响应值、丢包率的比较；若你在上海且打算运行[Digital Ocean](https://vps123.top/go/do)的云主机，用作代理服务器、云存储、云计算等，下面的内容很值得你深入了解。若有响应值接近、丢包率差距大的多个机房可选择，请优先选择丢包率低的；若Digital Ocean的这些机房的数据都不理想，你可以查看本文结尾链接的其他VPS提供商的数据，发现可用性更好的机房。

**数据地图：**[我应该关注哪类VPS测速数据？](https://vps123.top/find-pingtest-data-you-need.html)

## 概要

测速点的运营商线路为电信、联通、移动，有效样本点77个，其中超时点11个。连通概况如下：大陆线路响应均值为251毫秒，最快的三个机房所在地为旧金山、多伦多、新加坡，最慢的三个为纽约、伦敦、班加罗尔；纽约、旧金山、阿姆斯特丹、多伦多、新加坡等7处有响应超时情况；新加坡、纽约丢包率较高。

[注册 Digital Ocean](https://vps123.top/go/do/_btn1)

## 上海图表数据

![大陆省份上海到VPS提供商Digital Ocean各机房的ping测试数据统计图，包含响应值的柱状图以及丢包率的散点图，数据日期为20180622](/images/pingtests/do_20180622/plot_isp_shanghai_do_20180622.png)

### 全部运营商

**上海全部运营商到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 15个 | 2个 | 201ms | 4%  
多伦多 | 7个 | 1个 | 238ms | 0  
新加坡 | 3个 | 1个 | 246ms | 11%  
均值 | 77个 | 11个 | 251ms | 4%  
阿姆斯特丹 | 14个 | 2个 | 257ms | 3%  
法兰克福 | 8个 | 1个 | 260ms | 3%  
纽约 | 18个 | 3个 | 261ms | 6%  
伦敦 | 5个 | 0 | 264ms | 0  
班加罗尔 | 7个 | 1个 | 317ms | 0  
  
**简评：** 本表展示了上海的 **电信、联通、移动** 线路到Digital Ocean各机房的平均测速数据，这些数据绘制在前面柱状图的 **绿色** 柱位上；如果你常驻上海，可从此表了解你常用的网络到Digital Ocean各个机房的平均响应速度以及丢包率。从表中数据可以看到， **旧金山、多伦多** 的响应速度小于250ms，且丢包率在5%以内，值得关注；如果你多数时间只使用某运营商的网络，后面的分运营商的表格数据对你更有参考价值。

### 电信

**上海电信到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 12个 | 2个 | 217ms | 3%  
多伦多 | 6个 | 1个 | 227ms | 0  
新加坡 | 3个 | 1个 | 246ms | 11%  
均值 | 64个 | 11个 | 260ms | 1%  
阿姆斯特丹 | 12个 | 2个 | 263ms | 0  
法兰克福 | 6个 | 1个 | 258ms | 0  
纽约 | 15个 | 3个 | 287ms | 0  
伦敦 | 4个 | 0 | 213ms | 0  
班加罗尔 | 6个 | 1个 | 357ms | 0  
  
**简评：** 如果你是来自上海的 **电信** 用户，想运行Digital Ocean的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **伦敦、旧金山、多伦多** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **新加坡** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/do/_1)吧！

### 联通

**上海联通到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 2个 | 0 | 198ms | 10%  
多伦多 | 1个 | 0 | 249ms | 0  
新加坡 | - | - | - | -  
均值 | 7个 | 0 | 245ms | 4%  
阿姆斯特丹 | - | - | - | -  
法兰克福 | 1个 | 0 | 259ms | 0  
纽约 | 2个 | 0 | 249ms | 5%  
伦敦 | 1个 | 0 | 315ms | 1%  
班加罗尔 | - | - | - | -  
  
**简评：** 如果你是来自上海的 **联通** 用户，想运行Digital Ocean的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **多伦多、纽约** 的机房；从数据看，你的网络到这几处的连通速度、丢包率都比较不错。请慎重选择部署在 **旧金山** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/do/_2)吧！

### 移动

**上海移动到Digital Ocean各机房的测速数据 [20180622]**

机房所在地 | 测速点 | 超时点 | 响应均值 | 丢包率  
---|---|---|---|---  
旧金山 | 1个 | 0 | 187ms | 1%  
多伦多 | - | - | - | -  
新加坡 | - | - | - | -  
均值 | 6个 | 0 | 246ms | 6%  
阿姆斯特丹 | 2个 | 0 | 251ms | 7%  
法兰克福 | 1个 | 0 | 265ms | 11%  
纽约 | 1个 | 0 | 249ms | 13%  
伦敦 | - | - | - | -  
班加罗尔 | 1个 | 0 | 278ms | 0  
  
**简评：** 如果你是来自上海的 **移动** 用户，想运行Digital Ocean的VPS产品，用作科学上网、云存储、远程任务、游戏服务器等用途，建议重点关注部署在 **旧金山** 的机房；从数据看，你的网络到这里的连通速度、丢包率都比较不错。请慎重选择部署在 **纽约** 的机房，即使此处离你较近；因为响应均值虽然还不错，但丢包率较高。文章结尾处有本文视角的其他近期测评的链接，建议你多看几期以提升判断的准确度；如果看好了，就果断[去让机器跑起来](https://vps123.top/go/do/_3)吧！

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
    * [大陆](/digitalocean/isp/china/20180622-digitalocean-isp-china.md "大陆到Digital Ocean各机房的Ping测试 20180622")
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
    * [四川](/digitalocean/isp/sichuan/20180622-digitalocean-isp-sichuan.md "四川到Digital Ocean各机房的Ping测试 20180622")
    * [天津](/digitalocean/isp/tianjin/20180622-digitalocean-isp-tianjin.md "天津到Digital Ocean各机房的Ping测试 20180622")
    * [西藏](/digitalocean/isp/tibet/20180622-digitalocean-isp-tibet.md "西藏到Digital Ocean各机房的Ping测试 20180622")
    * [新疆](/digitalocean/isp/xinjiang/20180622-digitalocean-isp-xinjiang.md "新疆到Digital Ocean各机房的Ping测试 20180622")
    * [云南](/digitalocean/isp/yunnan/20180622-digitalocean-isp-yunnan.md "云南到Digital Ocean各机房的Ping测试 20180622")
    * [浙江](/digitalocean/isp/zhejiang/20180622-digitalocean-isp-zhejiang.md "浙江到Digital Ocean各机房的Ping测试 20180622")
  * 上海到Digital Ocean各机房的 _其他近期报告_ ： 
    * [20180514](/digitalocean/isp/shanghai/20180514-digitalocean-isp-shanghai.md "上海到Digital Ocean各机房的Ping测试 20180514")
    * [20180527](/digitalocean/isp/shanghai/20180527-digitalocean-isp-shanghai.md "上海到Digital Ocean各机房的Ping测试 20180527")
    * [20180804](/digitalocean/isp/shanghai/20180804-digitalocean-isp-shanghai.md "上海到Digital Ocean各机房的Ping测试 20180804")
    * [20180918](/digitalocean/isp/shanghai/20180918-digitalocean-isp-shanghai.md "上海到Digital Ocean各机房的Ping测试 20180918")
  * 本期报告：上海到 _其他VPS提供商_ 各机房的测速报告： 
    * [Vultr](/vultr/isp/shanghai/20180622-vultr-isp-shanghai.md "上海到Vultr各机房的Ping测试 20180622")
    * [BandwagonHost](/bandwagon/isp/shanghai/20180622-bandwagon-isp-shanghai.md "上海到BandwagonHost各机房的Ping测试 20180622")
    * [Linode](/linode/isp/shanghai/20180622-linode-isp-shanghai.md "上海到Linode各机房的Ping测试 20180622")



本文最初发表于[上海到Digital Ocean各机房的测速数据（20180622）](https://vps123.top/pingtest/20180622-digitalocean-isp-shanghai.html)
