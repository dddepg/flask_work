import re
import time
from flask import Flask, request, Response, json
str="https://www.dddepg.top/graduate_back/static/pdf/ceshiwenjian8.pdf"
rest=re.split(r'\/',str)
filen=re.split(r'\.',rest[-1])
# iszn=True
# for ch in str:
#     if ch<u'\u4e00' or ch > u'\u9fff':
#         iszn=False
print(filen[0])
# print(rest[1]+"2"+"."+rest[2])
# print(rest[0]=="" and rest[4]=="" and rest[3]=="com")
# print(iszn)
# print(time.strftime("%Y.%m.%d", time.localtime()))
# print(all(ord(c) < 128 for c in str))
# string="asdasdasd"
# iszn=True
# isen=True
# for ch in string:
#     if ch<u'\u4e00' or ch > u'\u9fff':
#         iszn=False
# if not iszn:
#     for en in string:
#         if ord(en)<65 or 90<ord(en)<97 or ord(en)>122:
#             isen=False
#     if isen:
#         print(1)
#     else:
#         print(2)
# else:
#     print(0)

# res = {}
# results=[["tit1","url1"],["tit2","url2"],["tit3","url3"],["tit4","url4"]]
# reslist = list()
# for row in results:
#     res["title"] = row[0]
#     res["URL"] = row[1]
#     reslist.append(res.copy())
# data=json.dumps(reslist)
# res2={}
# res2["result"]="1"
# res2["data"]=reslist
# print(json.dumps(res2))