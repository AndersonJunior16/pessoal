import pyautogui as pa
import time

pa.PAUSE = 3

# Trocar para a próxima janela usando alt+tab
pa.hotkey('alt', 'tab')

# Flag para indicar se deve continuar procurando
procurar = True

# Tentar encontrar e clicar no ícone do Teams
while procurar:
    try:
        # Localizar o ícone do Teams na tela
        teams = pa.locateOnScreen('teams.png', confidence=0.6)
        
        if teams:
            # Clicar no centro da imagem localizada
            pa.click(teams.x + teams.width // 2, teams.y + teams.height // 2)
            time.sleep(2)
            procurar = False
        else:
            print("Ícone do Teams não encontrado, tentando novamente...")
            time.sleep(2)
        
    except Exception as e:
        print(f'Erro: {e}')
        time.sleep(2)

