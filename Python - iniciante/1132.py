valor1 =  int(input())
valor2 = int(input())
lista_valores = []
if valor1<valor2:
    for i in range(valor1, valor2+1):
        if i % 13 != 0:
            lista_valores.append(i)
else:
    for i in range(valor2, valor1+1):
        if i % 13 != 0:
            lista_valores.append(i)
print(sum(lista_valores))