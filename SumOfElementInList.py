#method 1: using loop with range()

mylist=[5,10,15,20]
total=0

for i in range(0,len(mylist)):
    total=total+mylist[i]

print(total)
print("sum of all element in list:",total)

#method2 :using sum() method

mylist=[5,10,15,20]
total=sum(mylist)
print(total)