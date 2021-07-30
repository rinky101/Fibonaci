# Approach1 using clear()

Mylist=[6,1,2,3]
print(Mylist)

Mylist.clear()
print(Mylist)

#approach2
Mylist=[6,1,2,3]
print(Mylist)

Mylist=[]
print(Mylist)

#approach3 del method

Mylist=[6,1,2,3]
print(Mylist)

del Mylist[1:3] #0 2 will be deleted
print(Mylist)

del Mylist[:]
print(Mylist)
