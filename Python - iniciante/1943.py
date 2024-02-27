posicao = int(input())
if posicao == 1:
    print('Top 1')
elif posicao > 1 and posicao <= 3:
    print('Top 3')
elif posicao > 3 and posicao <= 5:
    print('Top 5')
elif posicao > 5 and posicao <= 10:
    print('Top 10')
elif posicao > 10 and posicao <= 25:
    print('Top 25')
elif posicao > 25 and posicao <= 50:
    print('Top 50')
elif posicao > 50:
    print('Top 100')