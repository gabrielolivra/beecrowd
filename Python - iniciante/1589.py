contador = 0
resultados = []
qtd_valores = int(input())
while contador < qtd_valores:
    valores = input().split()
    valor1 = int(valores[0])
    valor2 = int(valores[1])
    resultado = valor1 + valor2
    resultados.append(resultado)
    contador+=1
for i in resultados:
    print(i)