#approach using loop

mylist=[1,6,3,5,3,1,4]

ele=4
flag=0

for i in mylist:
    if(i==ele):
        print("element found")
        flag=1
        break
if(flag==0):
    print("element not found")

# how to use in operator

mylist=[1,6,3,5,3,1,4]

ele=5

if(ele in mylist):
    print("element found")
else:
    print("element not found")
    
