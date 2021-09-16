# 正则表达式
# 在此导入python正则库
"""
re.search('正则','')
re.findall('正则','')
字符组
    字符组允许匹配一组可能出现的字符，在正则表达式中用[]表示字符组标志
[可选]
[区间]
[^]取反
快捷方式：
    快捷方式	描述
    \w	与任意单词字符匹配
    \d	与任意数字匹配
    \s	匹配空白字符，比如空格，换行等
    \b	匹配一个长度为0的子串
\b: a = re.findall(r'\bmaster\b', 'masterxiao-master-xxx master abc')  # 前后与字母或数字不直接相邻的master
    a = re.findall(r'\Bmaster\B', '432masterxiao master xxx master abc')  # 前后与字母或数字直接相邻的master
快捷方式取反：
    快捷方式也可以取反， 例如对于 \w的取反为\W，可以发现将小写改写成大写即可。
    注意：这里\B 有所不同，
    \b 匹配的是在单词开始或结束位置长度为0的子字符串，而\B匹配不在单词开始和结束位置的长度为0的子字符串。

字符串的开始与结束
    在正则表达式中 用^ 可以表示开始，用 $表示结束
    对于^ 在[]里表示取反，在外面表示开始

通配符
    在生活中我们经常会有这么一种场景，我们记得某个人名为孙x者，就是不记得他叫孙行者，
    在正则表达式中针对此类场景，产生了通配符的概念，用符号.表示。它代表匹配任何单个字符，不过值得注意的是，它只能出现在方括号字符组以外。
    值得注意的是：.字符只有一个不能匹配的字符，也就是换行（\n），不过让.字符与换行符匹配也是可能的，以后会讨论。

可选字符
    不过有时，我们可能想要匹配一个单词的不同写法，比如color和colour，或者honor与honour。
    这个时候我们可以使用 ? 符号指定一个字符、字符组或其他基本单元可选，这意味着正则表达式引擎将会期望该字符出现零次或一次。
    a = re.search(r'honou?r','He Served with honor and distinction')
    b = re.search(r'honou?r','He Served with honour and distinction')
    c = re.search(r'honou?r','He Served with honou and distinction')
    print(a)
    print(b)
    print(c)
    <re.Match object; span=(15, 20), match='honor'>
    <re.Match object; span=(15, 21), match='honour'>
    None


重复区间
    我们可能期望一个字符组连续匹配好几次。
    在正则表达式在一个字符组后加上{N} 就可以表示 {N} 之前的字符组出现N次。
    可能有时候，我们不知道具体匹配字符组要重复的次数，比如身份证有15位也有18位的。
    这里重复区间就可以出场了，语法：{M,N}，M是下界而N是上界。
    通过上述代码，我们发现[\d]{3,4} 既可以匹配3个数字也可以匹配4个数字，
    不过当有4个数字的时候，优先匹配的是4个数字，
    这是因为正则表达式默认是贪婪模式，即尽可能的匹配更多字符，
    而要使用非贪婪模式，我们要在表达式后面加上 ?号。
    ‘+’	重复匹配1个或多个
    ‘*’	重复匹配0个或多个

分组
    要实现分组很简单，使用()即可。从正则表达式的左边开始看，看到的第一个左括号(表示第一个分组，第二个表示第二个分组，依次类推。
    a=<div><a href="https://support.google.com/chrome/?p=ui_hotword_search" target="_blank">python正则表达式之分组</a>
    <p>dfsl</p></div>
    print(re.search(r'<a.*>(.*)</a>', a).group(1))
    需要注意的是，有一个隐含的全局分组（就是索引号为0的分组），就是整个正则表达式匹配的结果。
命名分组
    命名分组就是给具体有默认分组编号的组另外再起一个别名，方便以后的引用。
    命令分组的语法格式如下：
    (?P<name>正则表达式)
    语法格式中的字符P必须是大写的P，name是一个合法的标识符，表示分组的别名。如下例子：

先行断言
    正向先行断言
        (?=pattern)表示正向先行断言，整个括号里的内容（包括括号本身）代表字符串中的一个位置，紧接该位置之后的字符序列能够匹配pattern
    反向先行断言
        (?!pattern)表示反向先行断言，与正向先行断言相反，紧接该位置之后的字符序列不能够匹配pattern
        注意：反向断言不支持匹配不定长的表达式，也就是说+、*字符不适用于反向断言的前后。

后发断言
    正向后发断言
        (?<=pattern)正向后发断言代表字符串中的一个位置，紧接该位置之前的字符序列只能够匹配pattern。
    反向后发断言
        (?<!pattern)负向后发断言 代表字符串中的一个位置，紧接该位置之前的字符序列不能匹配pattern。

正则表达式标记
    不区分大小写
        re.IGNORECASE也可以简写为re.I，使用该标记，可以使正则表达式变为不区分大小写。
    点匹配换行符
        re.DOTALL标记（别名为re.S）可以让.字符除了匹配其他字符之外，还匹配换行符。
    多行模式
        re.MULTILINE标记（别名为re.M）可以匹配多行，使用该标记可以使得仅能够匹配字符串开始与结束的^与$字符可以匹配字符串内任意行的开始与结束。
    详细模式
        re.VERBOSE标记(别名为re.X)允许复杂的正则表达式以更容易的方式表示。
        该标记做两件事，首先，它会使所有的空白（除了字符组中）被忽略，包括换行符。其次，它将#字符（同样，除非在字符组内）当做注释字符。
    调试模式
        re.DEBUG标记（没有别名）在编译正则表达式时将一些调试信息输出到 sys.stderr。
    使用多个标记
        有时候我们可能需要同时使用多个标记，为了完成这点，可以使用|操作符。
        示例： re.DOTALL|re.MULTILINE 或 re.S | re.M 。
正则表达式替换
    re.sub('','','')
匹配函数: match(str)    # 决定RE是否在字符串刚开始的位置匹配。如果满足，则返回一个match对象；如果不满足，返回空
"""
import urllib.request as req
from lxml import etree
import requests
import re

# d = re.findall(r'[0-9\-]', '0edu 007-edu')
# print(d)
# b = re.search(r'[^0-9]', 'xxx007abc')

# a = re.findall(r'\bmaster\b', 'masterxiao-master-xxx master abc')  # 单词字符后面或前面不与另一个单词字符直接相邻
# b = re.search(r'\bmaster\b', 'master')
# print(a)
# print(b)
# a = re.findall(r'\Bmaster\B', '432masterxiao master xxx master abc')
# print(a)
# a = """
#     <div><a href="https://support.google.com/chrome/?p=ui_hotword_search" target="_blank">python正则表达式之分组</a>
# <p>dfsl</p></div>"""
# print(re.search(r'<a.*>(.*)</a>', a).group(1))
# import re
#
# a = input()
#
# # *********** Begin **********#
# result = re.findall(r'\w+(?=ing)', a)
# # *********** End **********#
# print(result)
# a = re.findall(r'.+','hello\npython')
# print(a)
# a = re.findall(r'.+','hello\npython',re.S)
# print(a)
# str = '2016-2019 信息科技有限公司'
# dd = re.findall('(\\d+)\\W(\\d+).*(\W+)', str)
# print(dd)
# def re_Regex():
#     # *********** Begin **********#
#     path = "./test.txt"
#     # 读取数据文件
#     string = r'cs_item_sk[\s=]*(?P<first>\d*?1+)\s+.+?\s+?true\s*?(?P<second>\d+)'
#     # 根据日志数据编写正则表达式提取数据内容
#     pattern = re.compile(string)
#     # 提取以cs_item_sk开头,中间数值以1结尾的并且布尔值为true的值。(提取值为:中间值以1结尾,布尔值为true后的数值)
#     with open(path, 'r') as f:
#         line = f.read()
#         print(line)
#         print('--------------------------------')
#         m = pattern.search(line)
#         print(m.group('second'))
#
#
# re_Regex()
input_data = """
abc123@.
 good123...
666educoder^
hello123@
123456789
"""

# result = re.findall(r'^\S\d*(?!\d)[a-z]*(?![a-z])\W*\D*\S*(?![\W\D])', input_data, re.M)
#
# result = re.findall(r'^(?![a-zA-z]+$)(?!\d+$)(?![!@#$%^&*.?]+$)[a-zA-Z\d!@#$%.?^&*]+$', input_data, re.M)
# print(result)
# '<i.*board-index.*>(?P<board-index>\d+)</i>.*<img.*data-src[=\s]*"(?P<data-src>https?://.*)"[\s]*alt[=\s]"(?P<title>.*)".*<p.*"star".*>(?P<star>.*)</p>.*<p.*releasetime,*>(?P<releasetime>.*)</p>.*<i.*integer.*>(?P<integer>.*)</i>.*<i.*fraction,*>(?P<fraction>.*)</i>'
# text = """
# <dd>
#     <i class="board-index board-index-1">1</i>
#     <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
#         <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#         <img data-src="https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
#     </a>
#     <div class="board-item-main">
#         <div class="board-item-content">
#               <div class="movie-item-info">
#                     <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
#                     <p class="star">主演：张国荣,张丰毅,巩俐</p>
#                     <p class="releasetime">上映时间：1993-01-01</p>
#               </div>
#         <div class="movie-item-number score-num">
#             <p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>
#         </div>
#       </div>
#     </div>
# </dd>
# """
# data = re.search(
#     r'<i.*board-index.*?>(?P<board_index>\d+)</i>.*<img.*data-src[=\s]*"(?P<data_src>https?://.*)"[\s]*alt[=\s]"(?P<title>.*?)".*<p.*?"star".*?>(?P<star>.*)</p>.*<p.*?releasetime.*?>(?P<releasetime>.*?)</p>.*<i.*integer.*?>(?P<integer>.*)</i>.*<i.*fraction.*>(?P<fraction>.*?)</i>',
#     text, re.S)
# print(data.groups())

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/"
#                   "537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
#
# # get请求网页
# res = requests.get(url="http://www.qstheory.cn/dukan/qs/2014/2019-01/01/c_1123924172.htm", headers=headers)
# res.encoding = "utf-8"
# html = res.text
# # print(type(html))
# urls = re.findall(r'<!--视频代码结束-->.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url>https?://.*?htm).*?strong', html, re.S)
# print(urls)
# # def geturls():
#     # ********** Begin ********** #
#     # 补充请求头
#     headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/"
#                   "537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
#
#     # get请求网页
#     # res=requests.get(url="http://www.qstheory.cn/dukan/qs/2014/2019-01/01/c_1123924172.htm",headers=headers)
#     # res.encoding="utf-8"
#     # html=res.text
#     # urls = re.findall(r'<!--视频代码结束-->.*?<a.*?href.*?(?P<url1>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url2>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url3>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url4>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url5>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url6>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url7>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url8>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url9>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url10>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url11>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url12>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url13>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url14>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url15>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url16>https?://.*?htm).*?strong', html, re.S)
#     # print(urls)
#     # urls = urls[0]
#     # urls=[i for i in urls]
#     # print(urls)
#
#     # ********** End ********** #
#
#     return urls
#
#
# if __name__ == "__main__":
#     urls = geturls()
"""
<!DOCTYPE html>
<html lang="zh-cn">
<body>
<div id="wx_pic" style="display: none;"> <img src="http://www.qstheory.cn/n6/images/zt_weixin_share.png" /> </div>
<header class="wp_top">
<div class="icon"><a href="http://www.qstheory.cn" target="_blank"><img src="http://www.qstheory.cn/n7/images/v7_qsdd_20171208_08.png" alt="" /></a></div>
<div class="menu"><a href="http://www.qstheory.cn" target="_blank">求是网首页</a> | <a href="http://www.qstheory.cn/sitemap/" target="_blank">网站地图</a></div>
</header>
<div class="clear"></div>
<section class="container">
<div class="row">
<div class="col-sm-12">
<div class="content">
<div class="inner">
<h1>
《求是》2019年第1期
</h1>
<h2>

</h2>
<span class="appellation">
来源：《求是》2019/01
</span>
<span class="appellation">

</span>
<span class="pubtime">
2019-01-01 09:00:00
</span>
<span class="line"></span>
<div class="text">
<div class="clipboard_text">
<div class="highlight">
<!--视频代码-->
<div id="videoArea">
<span style="display:none;">
r'<!--视频代码结束-->.*?[<a.*?href.*?(https?://.*htm).*?]{16}'
</span>
</div>
<!--视频代码结束-->
<p style="TEXT-ALIGN: center" align="center"><font style="FONT-SIZE: 18pt" face="微软雅黑"><strong><font style="COLOR: #993300; FONT-SIZE: 20pt"><font color="#993300"><font style="FONT-SIZE: 20pt"><font style="FONT-SIZE: 20pt" size="1"><font style="FONT-SIZE: 20pt">目  </font>录</font></font></font></font></strong></font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123924154.htm" target="_blank"><strong>本期导读</strong></a></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2018-12/31/c_1123923896.htm" target="_blank"><strong>辩证唯物主义是中国共产党人的世界观和方法论</strong></a> <font face="楷体">/习近平</font></p>
<p></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123923886.htm" target="_blank"><strong>学好用好马克思主义哲学这个看家本领</strong></a> <font face="楷体">/本刊编辑部</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123923852.htm" target="_blank"><strong>增强脚力眼力脑力笔力 守正创新做好新形势下宣传思想工作</strong></a> <font face="楷体">/黄坤明</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123923828.htm" target="_blank"><strong>以习近平外交思想为引领 不断开创中国特色大国外交新局面</strong></a> <font face="楷体">/王 毅</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123923817.htm" target="_blank"><strong>社论：砥砺奋进 开拓创新 以优异成绩迎接中华人民共和国成立70周年</strong></a></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123923778.htm" target="_blank"><strong>论新时代</strong></a> <font face="楷体">/同 心</font></p>
<p></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123923740.htm" target="_blank"><strong>重温《关于若干历史问题的决议》 坚定“两个维护”的自觉</strong></a> <font face="楷体">/王均伟</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123923715.htm" target="_blank"><strong>新时代中国文艺的前进方向</strong></a> <font face="楷体">/铁 凝</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123923686.htm" target="_blank"><strong>改革开放进行时</strong></a> <font face="楷体">/新华社改革开放40周年专题调研组</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123922609.htm" target="_blank"><strong>兰考：会它千顷澄碧</strong></a> <font face="楷体">/刘雅鸣 陈聪 李亚楠 宋晓东</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123922550.htm" target="_blank"><strong>古代丝绸之路的历史价值及对共建“一带一路”的启示</strong></a> <font face="楷体">/李国强</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123922484.htm" target="_blank"><strong>电视理论节目的创新</strong></a> <font face="楷体">/董 城</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123922467.htm" target="_blank"><strong>学理论是党员领导干部的责任（党员来信）</strong></a> <font face="楷体">/李 君</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123922434.htm" target="_blank"><strong>多敲警钟才能少敲丧钟（党刊精选）</strong></a> <font face="楷体">/《中直党建》评论员</font></p>
<p>　　<a href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123924169.htm" target="_blank"><strong>经济社会发展统计：改革开放40年辉煌成就（经济篇）</strong></a> <font face="楷体">/国家统计局</font></p>
<p align="center"> </p>
<p align="center"><a title="" href="http://www.qstheory.cn/dukan/qs/2019-01/01/c_1123932149.htm" target="_blank"><img style="BOX-SIZING: border-box; BORDER-BOTTOM: 0px; TEXT-ALIGN: center; BORDER-LEFT: 0px; WIDOWS: 2; TEXT-TRANSFORM: none; FONT-STYLE: normal; TEXT-INDENT: 0px; WIDTH: 160px; FONT-FAMILY: 'Classic Grotesque W01', 'Avenir Next', 'Segoe UI', 'Helvetica Neue', Arial, 'Hiragino Sans GB', 'PingFang SC', 'Heiti SC', 'Microsoft YaHei UI', 宋体, 'Source Han Sans', sans-serif; MAX-WIDTH: 100%; WHITE-SPACE: normal; ORPHANS: 2; LETTER-SPACING: normal; HEIGHT: 50px; COLOR: rgb(51,51,51); FONT-SIZE: 16px; VERTICAL-ALIGN: middle; BORDER-TOP: 0px; FONT-WEIGHT: 400; BORDER-RIGHT: 0px; WORD-SPACING: 0px; font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial" id="{F25A7C2C-D0B4-44F9-B9F0-FA063CD456D5}" title="" border="0" align="center" src="1123924172_15462891947441n.jpg" sourcename="本地文件" sourcedescription="编辑提供的本地文件" /></a></p>
</div>
<script src="http://www.qstheory.cn/n7/js/docs.min.0828.js"></script>
</div>
<div class="xl_ewm hidden-xs">
<div class="pic"><img src="http://www.qstheory.cn/n7/images/v7_index_1223_25.jpg" /></div>
<div class="text">扫描二维码分享到手机</div>
</div>
<div class="fs-text"></div>
<div class="fs-line"></div>
<div class="fs-text pull-left">
标签 -  
</div>
<div class="fs-text pull-right">
网站编辑 - 乔雪 
</div>
<div class="clear"></div>
<div class="fs-line"></div>
<div class="fs-text pull-right hidden-xs"><a href="http://www.qstheory.cn/qssyggw/2014-08/12/c_1112042256.htm" target="_blank">【网站声明】</a><a href="http://www.qstheory.cn/qssyggw/2014-08/06/c_1111961674.htm" target="_blank">【纠错】</a><a href="#" onClick="return printit();">【打印】</a></div>
<div class="fs-line_b"></div>
<div class="fs-pinglun"> <span class="big">评论</span> <span class="small">登录新浪微博 <a href="http://www.weibo.com/qstheory">@求是</a> 发表评论。请您文明上网、理性发言并遵守相关规定。</span> </div>
<div class="clear"></div>
</div>
<div class="sharebox">
<div class="con wx"><img src="http://www.qstheory.cn/n7/images/v7_qsdd_20171208_05.png" /></div>
<div class="wxcon"><img src="http://www.qstheory.cn/n7/images/v7_index_1223_25.jpg" /></div>
<div class="con"><a class="weibo" href=""><img src="http://www.qstheory.cn/n7/images/v7_qsdd_20171208_06.png" /></a></div>
<div class="con"><a class="qzone" href=""><img src="http://www.qstheory.cn/n7/images/v7_qsdd_20171208_07.png" /></a></div>
</div>
<footer class="footer">
<script type="text/javascript" src="http://www.qstheory.cn/n7/js/v7_xlbottom_20170707.js"></script>
</footer>
</div>
</div>
</div>
</div>
</section>
<script type="text/javascript">
$(function() {
//reset rem
  function setbaseFont() {
        var w_width = $(window).width();
        var baseFontSize = w_width / 10;
        $('html').css('font-size', baseFontSize + 'px');
    }
    setbaseFont();
    $(window).on('resize', function(e) {
        setbaseFont();
    });
//二维码
  function ewm(){
    var href = window.location.href;
    var _src = href.replace("c_","ewm_").replace(".htm","1n.jpg");
    $(".xl_ewm .pic img").attr("src",_src);
    $(".wxcon img").attr("src",_src);
  };
  ewm();
  $(".wx").hover(function(){
    $(".wxcon").show();
  },function(){
    $(".wxcon").delay(1000).hide(0);
  });
//分享
  var page = {
    render: function () {
      this.share();
    },
    share: function () {
      var href = window.location.href;
      var title = $("h1").html();
      $(".weibo").on("click", function () {
          window.open('http://service.weibo.com/share/share.php?url=' + href + "&title=" + title)
      });
      $(".qzone").on("click", function () {
          window.open('http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=' + href + "&title=" + title)
      })
    }
  };
  page.render();
});
</script>
<!--视频及分享JS-->
<script type="text/javascript" src="http://www.qstheory.cn/n5/js/shipin_fenxiang.js"></script>
<!--统计代码JS-->
<script src="http://w.cnzz.com/c.php?id=30019853" language="JavaScript"></script>
<script src="http://w.cnzz.com/c.php?id=30019853" language="JavaScript"></script>
<script src="http://w.cnzz.com/c.php?id=30019853" language="JavaScript"></script>
</body>
</html>
"""

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# }
# # get请求网页
# res = requests.get(url="http://www.qstheory.cn/dukan/qs/2014/2019-01/01/c_1123924172.htm", headers=headers)
# res.encoding = "utf-8"
# html = res.text
# urls = re.findall(
#     r'<!--视频代码结束-->.*?<a.*?href.*?(?P<url1>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url2>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url3>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url4>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url5>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url6>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url7>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url8>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url9>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url10>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url11>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url12>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url13>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url14>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url15>https?://.*?htm).*?strong.*?<a.*?href.*?(?P<url16>https?://.*?htm).*?strong',
#     html, re.S)
# urls = urls[0]
# urls = [i for i in urls]
# # print(urls)
#
# mainbody = []  # 保存新闻内容
# for url in urls:
#     data={}
#     response = requests.get(url=url, headers=headers)
#     response.encoding = 'utf-8'
#     html = response.text
#     # print(html)
#     tree = etree.HTML(html)
#     title = tree.xpath('//div[@class="inner"]/h1/text()')
#     title = title[0][2:-2]
#     # print(title)
#     author = tree.xpath('//div[@class="inner"]/span[@class="appellation"][2]/text()')
#     author = author[0][5:-2]
#     # print(author)
#     content = tree.xpath('//div[@class="highlight"]/p/text()')
#     # print(content)
#     content_data = ''
#     for i in content:
#         content_data = content_data + i
#     content_data = content_data[2:-2]
#     # print(content_data)
#     img_src = tree.xpath('//div[@class="highlight"]/descendant::img/@src')
#     # print(img_src)
#     data["title"]=title
#     data["author"]=author
#     data["content"] = content_data
#     data["imgsrc"] = img_src
#     mainbody.append(data)
# print(mainbody)
# response = requests.get(url=urls[0], headers=headers)
# response.encoding = 'utf-8'
# html = response.text
# # print(html)
# tree = etree.HTML(html)
# title=tree.xpath('//div[@class="inner"]/h1/text()')
# title=title[0][2:-2]
# print(title)
# author=tree.xpath('//div[@class="inner"]/span[@class="appellation"][2]/text()')
# author = author[0][5:-2]
# print(author)
# content = tree.xpath('//div[@class="highlight"]/p/text()')
# # print(content)
# content_data=''
# for i in content:
#     content_data=content_data+i
# content_data=content_data[2:-2]
# print(content_data)
# img_src = tree.xpath('//div[@class="highlight"]/descendant::img/@src')
# print(img_src)
# import urllib.request as req
#
# # 国防科技大学本科招生信息网中录取分数网页URL：
# url = 'http://www.gotonudt.cn/site/gfkdbkzsxxw/lqfs/index.html'  # 录取分数网页URL
# webpage = req.urlopen(url)  # 按照类文件的方式打开网页
# data = webpage.read()  # 一次性读取网页的所有数据
#
# data = data.decode('utf-8')  # 将byte类型的data解码为字符串（否则后面查找就要另外处理了）
# # print(data)
# res = re.findall(r'<a.*?href=.*?"(/.*?html).*?国防科技大学201[2-6]年录取分数统计', data)
# print(res)

# 国防科技大学本科招生信息网中2016年录取分数网页URL：
url = 'http://www.gotonudt.cn/site/gfkdbkzsxxw/lqfs/info/2017/717.html'

webpage = req.urlopen(url)  # 根据超链访问链接的网页
data = webpage.read()  # 读取超链网页数据
data = data.decode('utf-8')  # byte类型解码为字符串

# 获取网页中的第一个表格中所有内容：
table = re.findall(r'<table(.*?)</table>', data, re.S)
firsttable = table[0]  # 取网页中的第一个表格
# 数据清洗，将表中的&nbsp，\u3000，和空格号去掉
firsttable = firsttable.replace('&nbsp;', '')
firsttable = firsttable.replace('\u3000', '')
firsttable = firsttable.replace(' ', '')
# print(firsttable)
score = []
# 请按下面的注释提示添加代码，完成相应功能，若要查看详细html代码，可在浏览器中打开url，查看页面源代码。
# ********** Begin *********#
# 1.按tr标签对获取表格中所有行，保存在列表rows中：
# print(data)
rows = re.findall(r'<tr.*?>(.*?)</tr>', data, re.S)
# print(len(rows))
rows = rows[3:]
# print(rows)
row = rows[0]
row = row.replace('&nbsp;', '')
row = row.replace('\u3000', '')
row = row.replace(' ', '')
# print(row)
row_item = re.findall(r'<spanstyle="font-size.*?>(.*?)</span>', row)
print(row_item)
# 2.迭代rows中的所有元素，获取每一行的td标签内的数据，并把数据组成item列表，将每一个item添加到scorelist列表：

# 3.将由省份，分数组成的8元列表（分数不存在的用/代替）作为元素保存到新列表score中，不要保存多余信息


# ********** End **********#
