celular = {
    1: ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w', ' '],
    2: ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x'],
    3: ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y'],
    4: ['s', 'z', 'A', 'D', 'G', 'J', 'M', 'T'],
    5: ['B', 'E', 'H', 'K', 'N', 'Q', 'P', 'W', 'U', 'X'],
    6: ['C', 'F', 'I', 'L', 'O', 'R', 'V', 'Y'],
    8: ['S', 'Z']

}

soma = 0
palavra = str(input("Digite sua palavra: "))

for letra in palavra:
    for key, value in celular.items():
        if letra in value:
            print(key, end='')
            soma += key


print("\nSoma dos números: ", soma)