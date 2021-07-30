# approach reverse method

'''Mylist=[10,11,12,13,14,15]
print(Mylist)

Mylist.reverse()
print(Mylist)

#Approach2 slicing technique
Mylist=[10,11,12,13,14,15]
print(Mylist)

mylist2=Mylist[::-1] #starting:ending:-1 represent reverse order
print(mylist2)'''

# convert two list to dictionary.
'''def list_to_dict():
    keys = ["Naina","kimi","sheena"]
    value=[85246,763567,273889]
    result=dict(zip(keys,value))
    print(result)

list_to_dict()

def dict_to_tuple():
    dict1={"naina":85345,"kimi":76345,"sheena":56789}
    for i in dict1.items():
        print(i)
dict_to_tuple()'''

#Find the common elements between lists



def common_ele_list(list1,list2):
    common=[]
    count=0

    for i in list1:
        for j in list2:
            if (i==j):
                common.append(i)
                count=count+1
    print(common)
    print("common elements between two list is:",count)

l1=[40,50,60,80]
l2=[50,40,100,150,200]
common_ele_list(l1,l2)

#l1.append(l2)
#print(l1)
#l3=["amul"]
l1.extend("amul")
print(l1)
