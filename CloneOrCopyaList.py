#approach1 using slicing technique

'''mylist=[4,8,2,10,15,16]
mylist_copy=mylist[:]
print(mylist)'''''

#approach2:using extend method

mylist=[4,8,2,10,19,23]
mylist_copy=[2,4,5,7]
mylist_copy.extend(mylist)
print(mylist_copy)


# Approach3:List method

mylist=[4,8,2,10,19,23]
mylist_copy=list(mylist)
print(mylist_copy)

#approach4: copy method
mylist=[4,8,2,10,19,23]
mylist_copy=mylist.copy()
print(mylist_copy)
