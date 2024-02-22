valor1 = int(input())
valor2 = int(input())
valores =[]
if valor1 < valor2:
    for i in range(valor1 +1, valor2):
        valores.append(i)
    for val in valores:
        if val %5 == 2 or val %5 == 3:
            print(val)
else:
    for i in range(valor2 +1, valor1):
        valores.append(i)
    for val in valores:
        if val %5 == 2 or val %5 == 3:
            print(val)