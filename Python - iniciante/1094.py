contador = 0
lista_ratos = []
lista_coelhos = []
lista_sapos = []
qtd = int(input())
while contador < qtd:
    valores = [(x) for x in input().split()]
    if valores[1].upper() == 'C':
        lista_coelhos.append(int(valores[0]))
    elif valores[1].upper() == 'R':
        lista_ratos.append(int(valores[0]))
    elif valores[1].upper() == 'S':
        lista_sapos.append(int(valores[0]))
    contador += 1
total = sum(lista_ratos) + sum(lista_coelhos) + sum(lista_sapos)
print('Total:',total,'cobaias')
print('Total de coelhos:', sum(lista_coelhos))
print('Total de ratos:',sum(lista_ratos))
print('Total de sapos:', sum(lista_sapos))
print(f'Percentual de coelhos: {(sum(lista_coelhos) /total)* 100:.2f} %')
print(f'Percentual de ratos: {(sum(lista_ratos) /total)* 100:.2f} %')
print(f'Percentual de sapos: {(sum(lista_sapos) /total)* 100:.2f} %')