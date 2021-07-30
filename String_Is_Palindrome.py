#Method1
#1-> find reverse of string
#2->check if reverse or original are same or not

'''s=input("enter a string") # abcde

print(s[:]) # abcde
print(s[0:5]) #abcde
print(s[0:5:1])#abcde
print(s[::]) #abcde

revstr=(s[::-1]) #edcba reverse string

if revstr==s:
    print("pallindrome")
else:
    print("not palindrome")'''

#write a program to count the frequency of words appearing in a string

def frequency_word():
    str=input("enter the string")
    str2=str.split()
    d={}
    for i in str2:
         if i not in d.keys():
             d[i] = 0
             d[i]=d[i]+1

    print(d)
frequency_word()

