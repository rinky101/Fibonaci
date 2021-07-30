import re

str="welcome@@2t%$#&iooop"
regex=re.compile('[@_!#$%}{]')

if(regex.search(str)==None):
    print("No special character present in a string")
else:
    print("string contain special chracter")
    