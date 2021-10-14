from random import randint
from time import sleep
itens=("pedra!","papel!","tesoura!")
computador=randint(0, 2)
print('''Suas Opções
[0] pedra
[1] papel
[2] tesoura''')

jogador = int(input('Qual é a sua jogada?'))
print('jo')
sleep (1)
print('ken')
sleep (1)
print('po!!!')
sleep (1)
print('-='*15)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print("Empate")
    elif jogador == 1 :
        print("jogador Vence")
    elif jogador == 2:
        print("computador Vence")
    else:
        print("jogada Invalida")
elif computador == 1: #computador papel
     if jogador == 0:
        print('computador Vence')
     elif jogador == 1:
        print('Empate')
     elif jogador == 2:
        print('jogador vence')
     else:
        print('jogada Invalida')
elif computador  == 2:   #computador jogou tesoura
    if jogador == 0:
        print('jogador Vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('jogada invalida')
