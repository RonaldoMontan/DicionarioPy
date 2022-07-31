dicionario = {}
lista = []
controle = ''
media_idade = total_idade = 0

print(' ====Armazenamento de dados====')
while controle in 'Ss':

    dicionario['nome'] = str(input('Nome: '))
    #dicionario['sexo'] = ''

    while True:     #==Validação do sexo

        dicionario['sexo'] = str(input('Sexo: ')).upper()[0]
   
        if dicionario['sexo'] in 'MF':
            break
        else:
            print('Valor informado E R R A D O !!\n Digite [M | F]')   

    while True:     #==Validação idade

        dicionario['idade'] = int(input('Idade: '))

        if dicionario['idade'] < 0:
            print('Valor informado E R R A D O !!\n Digite um valor inteiro')
        else:
            total_idade += dicionario['idade']
            break    

    lista.append(dicionario) #==Alimento a lista com os valores de dicionario
    controle = str(input('Deseja continuar ? '))[0]#Vou pegar apenas a primeira letra

print(lista)
print(f'Quantidade de pessoas cadastradas {len(lista)}\n')
media_idade = float(( total_idade / len(lista)))
print(f'A media de idade cadastrada foi {media_idade}\n')        