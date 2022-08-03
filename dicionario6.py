
lista_time = list()
dicionario_jogador = dict()
partidas = list()

while True:
    dicionario_jogador.clear()#limpar o dicionario para receber novos valores
    partidas.clear()#limpa as partidas para receber novos valores
    dicionario_jogador['Nome'] =  str(input('Nome do jogador: '))
    total_partida = int(input(f'Quantas partidas {dicionario_jogador["Nome"]} jogou: '))


    for c in range(0, total_partida):#preenchendo os gols por partida
        partidas.append(int(input(f'Quantos gols na partida {c+1}º ')))

    dicionario_jogador['gols'] = partidas[:]
    dicionario_jogador['Total'] = sum(partidas)

    lista_time.append(dicionario_jogador.copy())    #momento em que aliemntamos a lista com o dicionario

    while True: #para forçar a ter a resposta certa
        continua = str(input('Deseja continuar ?  [S|N]  ')).upper()[0]
        if continua in 'SN':
            break
        print('Resposta invalida Digite S ou N')
    if continua == 'N':   #preenchido os dados de um jogador, saimos do laço.
        break        
print('-=' * 30)
#exibindo o cabeçalho da tabela
print('cod  ', end='')
for i in dicionario_jogador.keys():
    print(f' {i:<15}', end='')
print()
#exibindo formato tabela
print('-=' * 30)    
for indice, valor in enumerate(lista_time):
    print(f'{indice:>4}', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()  

print('-=' * 40)

while True:
    busca = 1- (int(input('Digite o codigo do jogador para ver mais detalhes: ')))

    if busca == 999:
        break

    if busca >= len(lista_time):
        print(f'ERRO !! Não existe jogador com código {busca}')
    else:
        print(f'===Levantamento do Jogador {lista_time[busca]["Nome"]}===')    

        for indice, gol in enumerate(lista_time[busca]['gols']):
            print(f'')