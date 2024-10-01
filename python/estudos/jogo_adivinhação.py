import random  
from time import sleep
from os import system


def limpar_tela():
    system('cls')
    

def menu_principal():
    print("Olá, bem vindo ao jogo!")
    print(20 * "-=")
    sleep(1)

    opc_menu = ""
    ctd_usuario = ctd_pc = ctd_menu= 0

    while True:
        if ctd_menu > 0:
            limpar_tela()
        print("Opção 1 - Começar a partida")
        print("Opção 2 - Ver resultados")
        print("Opção 3 - Encerrar o game")
        menu = int(input())

        if menu == 1:
            ctd_usuario, ctd_pc = jogar(ctd_usuario, ctd_pc)
            ctd_menu += 1
        elif menu == 2:
            mostrar_resultado(ctd_usuario, ctd_pc)
            ctd_menu += 1
        elif menu == 3:
            print("Obrigador por jogar!")
            break
        else:
            limpar_tela()
            print("Opção inválida")

def jogar(ctd_usuario, ctd_pc):
    opc_menu = ""

    while opc_menu.lower() not in ["n", "não", "nao"]:
        num_pc = random.randint(0,6)
        num_usuario = -1

        limpar_tela()
        print("Vamos começar!")

        while num_usuario != num_pc:
            num_usuario = int(input("Adivinhe o número que estou pensando (De 0 a 6): ")) 
            print(40* "-")  

            for i in range(3, 0, -1):
                print(i)
                sleep(0.3)

            print(40* "-")

            if num_usuario == num_pc:
                print("Parabéns, Você acertou!")
                ctd_usuario += 1
            else:
                if num_usuario > num_pc:
                    print("Você errou! O numero que estou pensando é MENOR")
                else:
                    print("Você errou! O numero que estou pensando é MAIOR")
                ctd_pc += 1      
        opc_menu = str(input("Deseja continuar jogando? Caso não apenas digite \"n\": "))

    return ctd_usuario, ctd_pc

def mostrar_resultado(ctd_usuario, ctd_pc):
    limpar_tela()
    opc_menu = -1

    while opc_menu != 0:
        if ctd_pc > ctd_usuario:
            print("Estou ganhando HAHAHAHAHA")
        elif ctd_pc == ctd_usuario:
            print("Estamos empatados!")
        else:
            print("Parabéns, você está ganhando!")

        print(20*"-=")
        print(f"Seus pontos: {ctd_usuario}")
        print(f"Meus pontos: {ctd_pc}")
        print(20* "-=")
        opc_menu = int(input("Para voltar ao menu digite 0: "))
        print(20* "-=")
        

if __name__ == "__main__":
    menu_principal()
            