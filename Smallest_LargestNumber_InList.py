# Method1 -> sort the list in ascending order then print the first and last element.

mylist=[20,100,20,1,10]
mylist.sort() # sorting
print(mylist) # [1, 10, 20, 20, 100]

print("smallest element is:",mylist[0])
print("largest element is:",mylist[-1])

# method2 using min() and max() methods

mylist=[20,100,20,1,10]
print("smalles element is:",min(mylist))
print("largets element is:",max(mylist))

# Method 3 using function

mylist=[20,100,20,1,10]


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list(mylist))


