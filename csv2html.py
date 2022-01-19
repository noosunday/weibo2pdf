# coding:utf-8

import webbrowser
import csv
# 命名生成的html
GEN_HTML = "weibo.html"
# 打开文件，准备写入
f = open(GEN_HTML, 'w')

# 准备相关变量
str1 = ''
str2 = ''
str3 = ''

message1 = """
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style>
        .imagew{
            margin-top: 5px;
            height:150px;
            border-radius:10px;
        }
        .datew{
            font-family: "Helvetica Neue", serif;
            color: #22c78f;
            font-size: 5px;
        }
        .textw{
            font-family: "Hiragino Sans GB", sans-serif;
            font-size: 15px;
            margin-top: 5px;
        }
        .surl-text{
            color: #eb7340;
        }
        a {text-decoration: none}
        body{margin-left: 20px;}      
        table{
            page-break-inside: avoid; /*一个table内容不跨页*/
            border-spacing: 20px 0px;
            margin-top: 10px;
            margin-left: 10px;
            /*左上与左下角框*/
            background:
            linear-gradient(to bottom,#33cdfa 0px,#33cdfa 1px,transparent 1px,transparent 100%) left top no-repeat,
            linear-gradient(to right,#33cdfa 0px,#33cdfa 1px,transparent 1px,transparent 100%) left top no-repeat,
            linear-gradient(to top,#33cdfa 0px,#33cdfa 1px,transparent 1px,transparent 100%) left bottom no-repeat,
            linear-gradient(to right,#33cdfa 0px,#33cdfa 1px,transparent 1px,transparent 100%) left bottom no-repeat;
            background-size: 5px 5px;
            padding:4px;
        }
        td p{margin:0px;padding:0px;}
    </style>
</head>
<body>
"""
message2 = """
</body>
</html>"""

with open('data/weibo.csv', 'r') as f1:
    reader = csv.reader(f1)

    messageM=''
    for row in reader:
        datew = row[0]
        textw = row[1]
        picw = row[2]
        print(datew,textw,picw)
        messageM+="""
        <table>
            <tr>
                <td class="datew">%s</td>
            </tr>
            <tr>
                <td class="textw">%s️</td>
            </tr>
            <tr>
                <td>%s</td>
            </tr>
        </table>
        """ % (datew, textw, picw)
    print(messageM)



# 写入文件
message = message1+messageM+message2
f.write(message)
# 关闭文件
f.close()

