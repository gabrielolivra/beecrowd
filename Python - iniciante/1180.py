tamanho = int(input())
entrada = input()
valores = entrada.split()[:tamanho]  
vetor = [int(valor) for valor in valores] 
print('Menor valor:',min(vetor))
print('Posicao:',vetor.index(min(vetor)))

