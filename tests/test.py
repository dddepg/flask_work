import re
import time
str="阿斯顿aaa"
rest=re.split(r'\/',str)
iszn=True
for ch in str:
    if ch<u'\u4e00' or ch > u'\u9fff':
        iszn=False
# print(rest[-1])
# print(rest[1]+"2"+"."+rest[2])
# print(rest[0]=="" and rest[4]=="" and rest[3]=="com")
print(iszn)
# print(time.strftime("%Y.%m.%d", time.localtime()))
# print(all(ord(c) < 128 for c in str))
string="asdasdasd"
iszn=True
isen=True
for ch in string:
    if ch<u'\u4e00' or ch > u'\u9fff':
        iszn=False
if not iszn:
    for en in string:
        if ord(en)<65 or 90<ord(en)<97 or ord(en)>122:
            isen=False
    if isen:
        print(1)
    else:
        print(2)
else:
    print(0)