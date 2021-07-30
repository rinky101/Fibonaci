#fibonaci->add sum of 2 preceding numbers
#0 1 1 2 3 5 8 13(0+1=1,1+1=2,1+2=3,2+3=5.....

'''n1=0
n2=1

print(n1)
print(n2)

for i in range(2,10):
    sum=n1+n2 #1
    print(sum) #1
    n1=n2
    n2=sum'''

#approach2

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))
