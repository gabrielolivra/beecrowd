valor1 = int(input())
valor2 = int(input())
valor3 = int(input()) 
valor4 = int(input())
valor5 = int(input())
lista_valor = [valor1, valor2, valor3, valor4, valor5]
contador_par = 0
for val in lista_valor:
    if val %2 == 0:
        contador_par+=1
print(contador_par, 'valores pares')