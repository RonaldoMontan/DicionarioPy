dicionario_jogador = dict() #dados individuasi que será armazenado na lista_time suas chaves são "nome", "gols", "total gols" 
lista_time = list() #pode conter mais que um jogador
partidas = list() #alocado dentro do dicionario_jogador


#este while responsavel pela alimentação do dicionario_jogador e da lista_time 
while True:
    dicionario_jogador.clear()#limpar o dicionario para receber novos valores
    partidas.clear()#limpa as partidas para receber novos valores
    dicionario_jogador['Nome'] =  str(input('Nome do jogador: '))
    total_partida = int(input(f'Quantas partidas {dicionario_jogador["Nome"]} jogou: '))


    for c in range(0, total_partida):#preenchendo os gols por partida no formato lista
        partidas.append(int(input(f'Quantos gols na partida {c+1}º ')))

    #momento para alimentar o dicionario com os dados informado na lista
    dicionario_jogador['gols'] = partidas[:]
    dicionario_jogador['Total'] = sum(partidas)

    lista_time.append(dicionario_jogador.copy())    #momento em que vamos agregando jogadores ao time

    while True: #para forçar a ter a resposta certa
        continua = str(input('Deseja continuar ?  [S|N]  ')).upper()[0]
        if continua in 'SN':
            break # encerra o while linha 23
        print('Resposta invalida Digite S ou N')
    if continua == 'N':   #preenchido os dados de um jogador, saimos do laço.
        break   #encerra while linha 7

print('-=' * 30)
#exibindo o cabeçalho da tabela, vamos imprimir as chaves registradas no dicionario conforme apresentado na linha 1
print('cod  ', end='')
for i in dicionario_jogador.keys():
    print(f' {i:<15}', end='')
print()
#exibindo os dados registrados na lista, caso tenha mais que um registro na lista será exibido um abaixo do outro.
print('-=' * 30)    
for indice, valor in enumerate(lista_time):
    print(f'{indice:>4}', end='')
    for dado in valor.values(): #esse for responsavel para apresentar apenas os valores de sua coluna sem precisar passar o indice
        print(f'{str(dado):<15}', end='')
    print()  

print('-=' * 40)

#while responsavel por entrar na lista do time e buscar pelo dicionario do jogador e apresentar seus dados
while True:

    busca = int(input('Digite o codigo do jogador para ver mais detalhes: '))
    if busca == 999:
        break #encerra o while linha 48

    if busca >= len(lista_time):
        print(f'ERRO !! Não existe jogador com código {busca}')
    else:
        print(f'===Levantamento do Jogador {lista_time[busca]["Nome"]}===')    

        for indice, gol in enumerate(lista_time[busca]['gols']):
            print(f'    no jogo {indice+1} fez {gol} gols.')

    print('-' * 40) 
print('>>> Até a Proxíma <<<')   # mensagem final, acabou a execução do programa            