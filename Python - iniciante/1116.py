contador = 0
qtd_calculo = int(input())
lista_resultado =[]
while contador < qtd_calculo:
    valor = input().split()
    valor1 = int(valor[0])
    valor2 = int(valor[1])
    if valor2 == 0:
        lista_resultado.append('divisao impossivel')
    else:
        divisao = valor1/valor2
        lista_resultado.append(divisao)
    contador+=1
for i in lista_resultado:
    print(i)