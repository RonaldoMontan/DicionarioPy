nome = str(input('Nome: '))
media = float(input(f'A média de {nome}: '))

dicionario_dados = {'nome': nome, 'media': media}#chaves representa dicionario

#Nos mesmo atribuimos o indice, e mps referimos a ele através de colchetes.
if dicionario_dados['media'] >= 7:
    print(f'{dicionario_dados["nome"]} está APROVADO !')

elif 5 < dicionario_dados['media']  <7:
    print(f'{dicionario_dados["nome"]} está RECUPERAÇÃO')   

else:
    print(f'{dicionario_dados["nome"]} está REPROVADO !')


#=====Modelo igual do professor=====

aluno = dict()
#declaração do indice (que chamamos de KEYS/chave) e atribuindo o valor
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'A média de {aluno["nome"]}: '))

if aluno['media'] >=7:
    aluno['situação'] = 'Aprovado'

elif 5 < aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'

else:
    aluno['situação'] = 'Reprovado'

print()
for chave, valor in aluno.items():
    print(f'O {chave} é igual a {valor}')


