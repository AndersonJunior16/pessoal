idade_18 = homens = mulheres = 0
mulher_20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('IDADE: '))
    sexo = ''
    while sexo not in 'FM':
        sexo = str(input('SEXO[M/F]: ')).strip().upper()[0]
    if idade > 18:
        idade_18 += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        mulheres += 1
        if sexo == 'F' and idade > 20:
            mulher_20 += 1
    print('-' * 30)
    opção = ''
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if opção == 'N':
        break

print(f'''Ao todo temos {idade_18} pessoas com mais de 18 anos.
{homens} homens cadastrados
E {mulher_20} mulheres com mais de 20 anos''')