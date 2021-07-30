# Approach:Temporary Variable
#swap first and last element

mylist=[12,35,9,56,24]
size=len(mylist)

temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp

print("list after swapping:",mylist)

#approach2

mylist=[12,35,9,56,24]

mylist[0],mylist[-1]=mylist[-1],mylist[0]


print("list after swapping:",mylist)

#Approach3 using tuple variable

mylist=[12,35,9,56,24]
get=(mylist[-1],mylist[0]) # packing 24  12
mylist[0],mylist[-1]=get

print("list after swapping:",mylist)

#approach4 using pop() function

mylist=[12,35,9,56,24]

first=mylist.pop(0)  #12
last=mylist.pop(-1)  #24

mylist.insert(0,last)
mylist.append(first)

print("list after swapping:",mylist)