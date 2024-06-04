import pyautogui as pa
import time

pa.PAUSE = 2

pa.hotkey('alt', 'tab')

time.sleep(2)

teams = 'teams.png'


local = pa.locateOnScreen(teams, confidence=0.8)

if local:
    center_x, center_y = pa.center(local)
    pa.click(center_x, center_y)
else:
    print('Não achado')