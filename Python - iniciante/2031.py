def jogo(jog1, jog2):
    plac_jog1 = 0
    plac_jog2 = 0
    if jog1 == 'ataque' and jog2 == 'pedra':
        print('Jogador 1 venceu')
        plac_jog1+=1
    elif jog1 == 'ataque' and jog2 == 'papel':
        print('Jogador 1 venceu')
        plac_jog1+=1
    elif jog1 == 'pedra' and jog2 == 'papel':
        print('Jogador 1 venceu')
        plac_jog1+=1
    if jog2 == 'ataque' and jog1 == 'pedra':
        print('Jogador 2 venceu')
        plac_jog2+=1
    elif jog2 == 'ataque' and jog1 == 'papel':
        print('Jogador 2 venceu')
        plac_jog2+=1
    elif jog2 == 'pedra' and jog1 == 'papel':
        print('Jogador 2 venceu')
        plac_jog2+=1

qtd = int(input())
for i in range(qtd):
    jogador1 = input()
    jogador2 = input()
    if jogador1 == 'ataque' and jogador2 == 'ataque':
        print('Aniquilacao mutua')
    elif jogador1 == 'papel' and jogador2 == 'papel':
        print('Ambos venceram')
    elif jogador1 == jogador2:
        print('Sem ganhador')
    else:
        jogo(jogador1, jogador2)
