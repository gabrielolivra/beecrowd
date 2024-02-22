valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor4 = float(input())
valor5 = float(input())
valor6 = float(input())

lista_valor = [valor1, valor2, valor3, valor4, valor5, valor6]
valor_positivo = []
for valor in lista_valor:
    if valor >= 0:
       valor_positivo.append(valor)
print(len(valor_positivo), 'valores positivos')