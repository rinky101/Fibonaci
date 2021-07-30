#input:arr[]={10,20,30}
#max=30
#min=10

arr=[1,20,30,4,15]

max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print(max)

#minimum number

arr=[1,20,30,4,15]

min=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print(min)
