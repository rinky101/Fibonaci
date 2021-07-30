#list:[15,6,7,10,12,20,10,28,10]
#x=10
#O/P=3
#10 apperas 3times in give list

#method1:using loop

mylist=[15,6,7,10,12,20,10,28,10]
x=10
count=0

for ele in mylist:
    if(ele==x):
        count=count+1

print("{} has occured {} times".format(x,count))


#method2:use count method

mylist=[15,6,7,10,12,20,10,28,10]
x=10
print("{} has occured {} times".format(x,mylist.count(x)))
#print(mylist.count(x))

#method