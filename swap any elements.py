#Approach1 simple swap

mylist=[23,65,19,99]
print(mylist)

pos1,pos2=1,3

mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)

#approach2 p,mylist using tupl

mylist=[23,65,19,99]
print(mylist)

pos1,pos2=1,3

get=mylist[pos1].mylist[pos2]
mylist[pos2],mylist[pos1]=get

print(mylist)


