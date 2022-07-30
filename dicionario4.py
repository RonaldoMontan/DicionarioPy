dicionario = dict()
lista = list()

print('\n===Informações de um jogador===\n')

dicionario['Nome jogador'] = str(input('Nome: '))
partidas = int(input('Quantas partidas ele jogou: '))
dicionario['total gols'] = 0

#Armazena apenas os gols da partida em uma lista
for controle in range(0, partidas):
    lista.append(int(input(f'Gol da {controle+1}º partida: ')))
    #abaixo vamos a alimentar o dicionario com os valores da lista utilizando a posição da lista
    dicionario['total gols'] += lista[controle]
    
#lista finalizada de acordo com a quantidade de partidas, vamos salvar no dicionario a lista    
dicionario['gol partida'] = lista

#são tres tipos de saida:
print('      ===Saidas===\n\n')
print('=-'*18)
print()
for chave, valor in dicionario.items():
    print(f'O campo  {chave}  tem o  {valor}')  
print()

print('=-'*18)
print(f'\n{dicionario}\n')

print('=-'*18)
print()
print(f'O jogador {dicionario["Nome jogador"]} jogou {partidas}, acompanhe o resdultado:')
for controle in range(0, len(lista)):
    print(f'-> Na partida {controle+1}, ele fez {lista[controle]} gols') 
print(f'Foi um total de {dicionario["total gols"]} gols')   
print()    