from datetime import date, datetime


dicionario_dados = {}

dicionario_dados['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano nascimento: '))
ano_atual = date.today().strftime('%Y') #a letra 'y' em maiusculo faz toda a diferença para 4 digitos do ano
dicionario_dados['Idade'] = (int(ano_atual) - ano_nascimento)
dicionario_dados['CTPS'] = int(input('Sua CTPS, caso não lembre o numero insira [ 0 ]:  '))

if dicionario_dados['CTPS'] == 0:
    print(f"{dicionario_dados['nome']}  tem {dicionario_dados['ano']} anos e não informou CTPS")

#se indormar valor de CTPS terá mais dados
else:
    dicionario_dados['ano inicio trabalho'] = int(input('Qual ano do seu primeiro emprego com carteira assinada: '))
    
    dicionario_dados['Tempo ja trabalhado (em anos)'] = (datetime.now().year - dicionario_dados['ano inicio trabalho'])

    dicionario_dados['Anos faltantes para aposentar'] = (35 - dicionario_dados['Tempo ja trabalhado (em anos)'])
print()
print('=-' * 20)
for chave, valor in dicionario_dados.items():
    print(f'{chave} :: {valor}')    

