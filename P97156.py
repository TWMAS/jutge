from easyinput import read

num1,num2 = read(int, int)

if num1 > num2:
    b = num2
    num2 = num1
    num1 = b

a = ''
for i in range(num1, num2+1, 1): 
        a = str(i)
print(a, end=",")