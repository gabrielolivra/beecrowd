contador = 0
qtd = int(input())
lista_resultados = []
while contador < qtd:
    valores = [float(x) for x in input().split()]
    media_ponderada = (valores[0] * 2 + valores[1] * 3 + valores[2] * 5) / 10
    lista_resultados.append(round(media_ponderada, 1))
    contador += 1
for i in lista_resultados:
    print(i)