'''import json

# read file
myjsonfile=open("C:\\Users\\rajalaxmi.nayak\\PycharmProjects\\PythonPractice\\PythonProgramming\\Employee.json",'r')

jsondata=myjsonfile.read()
#print(jsondata)

#parse the json data

obj=json.loads(jsondata)

print(str(obj['firstName']))
print(str(obj['lastname']))
print(str(obj['address']))

list=obj['address']

print((list))
print(list[0])

print(len(list)) #2

for i in range(len(list)):
    print("street:",list[i].get("street"))
    print("city:",list[i].get("city"))
    print("state:",list[i].get("state"))'''

# To read a file with multiple lines and split data by lines?also split in to words

file=open("C:\\Users\\rajalaxmi.nayak\\PycharmProjects\\PythonPractice\\PythonProgramming\\Employee.json",'r')
data=file.read()
#print(data)
lines= data.split("\n")
#print(lines)

for line in lines:
    #print(line)

    words=line.split(" ")
    print(words)

    for word in words:
        print(word)

file.close()


