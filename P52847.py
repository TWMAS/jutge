from easyinput import read

num1,num2,num3 = read(int,int,int)

if num1 > num2 and num1 > num3:
    print (num3)
elif num2 > num1 and num2 > num3:
    print (num2)
else num3 > num1 and num3 > num2:
    print (num1)
