class Pessoa:
    def __init__(self, x, y):
        self.x = x
        self.y = y


teste = int(input("Digite quantos testes seram feitos: "))

for i in range(teste):
    qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
    soma  = 0
    pessoas = []
    for j in range(qtd_pessoas):
        pessoa = Pessoa(0, 0)
        pessoa.x = int(input("Digite o valor de x: "))
        pessoa.y = int(input("Digite o valor de y: "))
        pessoas.append(pessoa)
        if j > 0:    
            d = ((pessoas[j].x - pessoas[j - 1].x)**2 + (pessoas[j].y - pessoas[j - 1].y)**2)**0.5  
            soma += d
    soma = soma / 100
    print(f"{soma:.2f}")