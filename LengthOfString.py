#Approach -> for loop

'''str="welcome"
count=0

for i in str:
    count=count+1
print(count)

#Approach 2 -> using while loop and slicing
str="welcome"

counter=0
while str[counter]:
    counter=counter+1
print(counter)

#method 3
str="welcome"
print(len(str))'''

# multiplication of two string

def multi_twostring(str1,str2):
    len1=len(str1)
    len2=len(str2)

    str1=list(map(int,reversed(str1)))
    str2=list(map(int,reversed(str2)))
    print(str1,str2)

str1="78"
str2="45"
multi_twostring(str1,str2)