# method1 travesera approach

mylist=[1,2,3,4]
result=1

for x in mylist:
    result=result * x

print(result)

# method 2: using numpy.prod() install numpy

import numpy

mylist=[1,2,3,4]
result=numpy.prod(mylist)
print(result)


