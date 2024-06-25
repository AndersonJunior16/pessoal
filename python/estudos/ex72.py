tupla = ('zero', 'um', 'dois', 'tres', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezecete', 'dezoito',
          'dezenove', 'vinte' )

while True:
    num = int(input('Digite um numero entre 1 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {tupla[num]}')
    else:
        print('Tente novamente. ', end = '')
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break

