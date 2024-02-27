precos = [('1001', 1.50),
          ('1002', 2.50),
          ('1003', 3.50),
          ('1004', 4.50), 
          ('1005', 5.50)]
valor_total = []
qtd = int(input())
for i in range(qtd):
    pedido = input().split()
    lista_pedido = [pedido]
    for i in lista_pedido:
        for chave, valor in precos:
            if i[0] == chave:
                valor_total.append(valor*int(i[1]))
result = sum(valor_total)
print(f'{result:.2f}')