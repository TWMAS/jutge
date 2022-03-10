a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)


num1 = int(input("Introduce un número: " ))
num2 = int(input("Introduce otro número: " ))

for i in range( num1, num2 + 1 ):
    print(i)