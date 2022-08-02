dicionario = {}
lista = []
controle = ''
media_idade = total_idade = 0

print(' ====Armazenamento de dados====')
while controle in 'Ss':

    dicionario['nome'] = str(input('Nome: '))

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

    lista.append(dicionario.copy()) #==Alimento a lista com os valores de dicionario, que são copias para não repetirem
    controle = str(input('Deseja continuar ? '))[0]#Vou pegar apenas a primeira letra

print()
#item A - quantidade de pessoas cadastradas
print(f'->  Quantidade de pessoas cadastradas {len(lista)}\n')

#item B - media de idade entre todas as pessoas cadastradas
media_idade = float(( total_idade / len(lista)))
print(f'->  A media de idade cadastrada foi {media_idade}\n')    

#item C - relção das mulheres cadastradas
print('->  As mulheres cadastradas foram: ', end='')  
for acha_mulher in lista:
    if acha_mulher['sexo'] in 'Ff':
        print(f'    |{acha_mulher["nome"]}', end='')  

if acha_mulher['sexo'] in 'Mm':
    print('0')    
print()

#item D - relação de pessoas com idade acima da media
print(f'->  As pessoas que tem idade acima da media são: ', end='')
for acha_idade_maior_media in lista:
    if acha_idade_maior_media['idade'] > media_idade:
        print(f'    {acha_idade_maior_media["nome"]} ', end='')

if acha_idade_maior_media['idade'] == media_idade:
    print('Não tem idade maior que a media para exibir!')    
