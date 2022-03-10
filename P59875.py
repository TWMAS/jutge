from easyinput import read

entrada,entrada2 = read(int, int)

if entrada < entrada2:
    b = entrada2
    entrada2 = entrada
    entrada = b

a = ''
for i in range(entrada, entrada2-1, -1):
    if a == '':
        a = str(i)
    else:
        a += '\n' + str(i)  
print(a)
