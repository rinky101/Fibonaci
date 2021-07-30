# prime number-> 1,3,5,9..... which has only 2 factors 1 and itself
#3->1 and 3-> prime number
#4-> 1,2,4->not a prime number

'''num=5
count=0

if num>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if count==2:
        print("number is prime")
    else:
        print("number is not prime")'''

#100-101

for i in range(100,200):
    count=0
    for j in range(1,i+1):
        if (i % j==0):
            count=count+1
    if (count == 2):
        print(i)
