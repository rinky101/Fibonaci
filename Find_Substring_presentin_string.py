str="welcome to python string"

sub_str="python"
print(str.find(sub_str))

if(str.find(sub_str)== -1):
    print("not found")
else:
    print("found")