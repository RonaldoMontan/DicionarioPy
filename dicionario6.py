lista_resumo = list()
continua = ''
totalgols = 0

print('\n===Informações de um jogador===\n')

while continua in 'S':
    lista_gol = []
    dicionario = dict()


    dicionario['Nome jogador'] = str(input('Nome: '))
    partidas = int(input('Quantas partidas ele jogou: '))
    
    #Armazena apenas os gols da partida em uma lista
    for controle in range(0, partidas):
        lista_gol.append(int(input(f'Gol da {controle+1}º partida: ')))
        
    #lista finalizada de acordo com a quantidade de partidas, vamos salvar no dicionario a lista    
    dicionario['gol partida'] = lista_gol
    dicionario['total gols'] = sum(lista_gol)
    print(sum(lista_gol))
    lista_resumo.append(dicionario)#Cada indiciduo sera um dicionario armazendaos em uma lista    
    continua = str(input('Deseja continuar?')).upper()[0]
    
cod = 1    
print('Cod    |   Nome          | Gols       |  Total')
print('----------------------------------------------')
for indice, valor in enumerate(lista_resumo):
    print(f'{indice:>3}', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}         {valor}', end='')
    print()    
    cod +=1







# #são tres tipos de saida:
# print('      ===Saidas===\n\n')
# print('=-'*18)
# print()
# for chave, valor in dicionario.items():
#     print(f'O campo  {chave}  tem o  {valor}')  
# print()

# print('=-'*18)
# print(f'\n{dicionario}\n')

# print('=-'*18)
# print()
# print(f'O jogador {dicionario["Nome jogador"]} jogou {partidas}, acompanhe o resdultado:')
# for controle in range(0, len(lista_gol)):
#     print(f'-> Na partida {controle+1}, ele fez {lista_gol[controle]} gols') 
# print(f'Foi um total de {dicionario["total gols"]} gols')   
# print()    