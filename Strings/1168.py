lista_numeros =[('1', 2), ('2', 5), ('3',5),( '4', 4), ('5',5), ('6',6), ('7',3), ('8',7), ('9',6), ('0',6)]
contador = 0
resultado = 0
lista_de_testes = []
lista_results = []
qtd = int(input())
while contador < qtd:
    val = input()
    lista_de_testes.append(val)
    contador+=1
for l in lista_de_testes:
    for k in l:
        for chave, valor in lista_numeros:
            if k == chave:
                resultado+=valor
    print(resultado, 'leds')
    resultado = 0