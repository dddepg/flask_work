import re

str="https://www.dddepg.top/graduate_back/static/pdf/buhuo.PNG"
rest=re.split(r'\/',str)
print(rest[-1])
# print(rest[1]+"2"+"."+rest[2])
# print(rest[0]=="" and rest[4]=="" and rest[3]=="com")

# print(len(str))