nome = []
codigo = []

print('Vamos começar o cadastro')
print('-' * 30)

while True:
    nome.append(str(input('Digite o nome da peça: ')))
    codigo.append(int(input('Digite o codigo da peça: ')))
    print('-' * 30)
    continuar = str(input('Quer cadastrar outra peça? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

print('Peças cadastradas com sucesso!')
while True:
    pergunta = int(input('Qual indice de peça você quer saber? '))
    if pergunta > len(nome):
        print('Indice não encontrado')
    elif 0 <= pergunta <= len(nome):
        print(f'Peça {nome[pergunta - 1]} de codigo {codigo [pergunta- 1]}.')