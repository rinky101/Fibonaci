
Mylist=["geeks","for","geeks"]
word="geeks"
n=2
#n=3

count=0

for i in range(0,len(Mylist)):
#for i in range(0, len(Mylist-1)):
    if(Mylist[i]==word):
        count=count+1 # 1 2
        if (count==n):
            del Mylist[i]

print(Mylist)
