#find missing number in an array

'''arr=[2,3,4,5,6]
n=arr[-1]
sum1=0
total=n*(n+1)//2
sum2=sum(arr)
total1=total-sum2
print(total1)'''

#find out pairs with given sum value of array


'''def twosum(arr,sum):
    left=0
    right=len(arr)-1
    arr.sort()

    while left<=right:
        if(arr[left]+arr[right] > sum):
            right=right -1

        elif(arr[left]+arr[right] < sum):
            left=left+1

        elif(arr[left] +arr[right] == sum):
            print("values of pair are",arr[left],"&",arr[right])
            left=left+1
            right=right-1

arr=[3,7,9,8,4,19,11,5]
sum=17
twosum(arr,sum)'''

#print minium difference of an array

'''arr=[4,12,5,18,25,35,32]

def min_diff(arr):
    arr.sort()
    arr_size=len(arr)-1
    min_difference=9999*999

    for i in range(arr_size):
        if arr[i+1] - arr[i] < min_difference:
            min_difference=arr[i+1] - arr[i]
     return min_difference

print(min_diff(arr))'''

#find the maximum difference of an array

'''def max_diff(arr):
    arr.sort()
    arr_size=len(arr)-1
    max_difference= -999*999

    for i in range(arr_size):
        if (arr[i+1] - arr[i] > max_difference):
            max_difference = arr[i+1] - arr[i]
    return max_difference

arr=[4,12,5,18,25,35,32]
print(max_diff(arr))'''

# find length of last word




def length_last_word(a):
    arr=a.split(' ')
    size=len(arr)
    if (size==1):
        return len(a)
    last_word=arr[-1]
    print(last_word)

a="rinky"
print(length_last_word(a))





