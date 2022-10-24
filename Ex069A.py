from time import sleep
print('...' * 20)
print('CADASTRO DE PESSOAS')
print('...' * 20)
maioridade = 0
mulher = 0
homem = 0
while True:
    nome = str(input('Digite o nome: '))
    sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Digite a idade: '))
    continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('---' * 20)
    if idade >= 18:
        maioridade += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    if continua == 'N':
        print('FINALIZANDO O PROGRAMA...')
        print('---' * 20)
        sleep(1)
        break
print(f'Maiores de idades cadastrados: {maioridade}.')
print(f'Homens cadastrados: {homem}.')
print(f'Mulheres com menos de 20 anos: {mulher}.')
