from operator import itemgetter
import random
from time import sleep

dicionario_dado = {}

#quatro lançamento de dados 
dicionario_dado = { 'jogador 1': random.randint(1,6),
                    'jogador 2': random.randint(1,6),
                    'jogador 3': random.randint(1,6),
                    'jogador 4': random.randint(1,6)}

for chave, valor in dicionario_dado.items():
    print(f'O {chave} tirou {valor} no dado') 
    sleep(1)
   
# Deixando em ordem
print('\n\n=== Ordem ganhador ===')
# este for vai organizar os valores pertencendo ao valor utilizando o metodo sorted() junto com itemgetter que utiliza 1, se utilizar 0 ele organiza pela chave
for chave, valor in sorted(dicionario_dado.items(), key=itemgetter(1), reverse=True):
    print(f'    {chave} -> {valor}')
    print()

# Queria tentar de outra maneira mas ainda não consegui uma solução
print('-=' * 22)

for lances in range(1,5):
    dic = {'jogador': lances, 'dado': random.randint(1,6)}
    print(dic)

print('====Resultado====')
for c, v in sorted(dic.items(), key=itemgetter(1), reverse=True):
    print(f'    {c} e {v}')    