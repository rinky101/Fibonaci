#iterative approach, 5!=1*2*3*4*5=120

factorial=1
num=5

if num<0:
    print("factorial doesnot exist for negative number")
elif num==0:
    print("the factorial of 0is 0")
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print("the factorial of", num ,"is", factorial)

#recursive Function

def fact(num):
    if num>1:
        num=num*fact(num-1)
    return num
print(fact(4))


def sum(a,b):
    return a+b

n1= input("enter first name")
n1=int(n1)
n2=input("enter first name: ")
n2=int(n2)
print("sum is:",sum(n1,n2))

#Approach3

def fact(num):
    if(num==0 or num==1):
        return 1
    else:
        return num * fact(num-1)
num=5
print("factorial of",num,"is",fact(num))




