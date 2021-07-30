def pal(num):
    x = num[::-1]
    if num == x:
        print("pallindrome")
    else:
        print("not pallendrome")

pal("122")


'''list=[40,277,20,10,245,66]
list.sort()
print(list)
list.reverse()
print(list)
list.sort(reverse=True)
print(list)

list2=[]
num=int(input("howmany number you want to enter:"))
print("enter values:")
for k in range(num):
    list2.append(int(input()))
print("unsorted list:",list2)

arr=[1,2,3,4,5]
sum1=sum(arr)
print(sum1)


def sum(arr):
  sum=0
  for i in arr:
    sum=sum+i
  return sum
arr=[1,5,4,3,6]
ans=sum(arr)
print(ans)

#find the nearest pallendrome number of number

def is_palindrome(num):
    temp=str(num)
    if temp == temp[::-1]:
        return True

def nearest_palindrome(number):
    while True:
        if is_palindrome(number):
            return number
        else:
            number+=1
number=123456
print(nearest_palindrome(number))'''





