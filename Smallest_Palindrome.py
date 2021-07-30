def smallest_pallindrome(number):
    size=len(number)
    odd=size %2
    if odd:
        center=number[size/2]
    else:
        center=" "
    left= number[:size/2]
    right=left[::-1]
    pallindrome=left+center+right
    if pallindrome>number:
        print(pallindrome)
    else:
        if center:
            if center<'9':
                center=str(int(center)+ 1)
                print (left+center +right)
            else:
                center='0'
        if left == len(left)*'9':
            print ('1'+(len(number)-1)*'0' +'1')
        else:
            left = inc(left)




