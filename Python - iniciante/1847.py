temp = input().split()
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])
if(a > b):
    if c > b:
        print(':)')
    else:
        if(b-c < a-b):
            print(':)')
        else:
            print(':(')   
elif(a < b):
    if c < b:
        print(':(')
    else:
        if(b-c > a-b):
            print(':(')
        else:
            print(':)')   
else:
    if c > a:
        print(':)')
    else:
        print(':(')