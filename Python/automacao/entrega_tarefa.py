import pyautogui as pa
import time
import os

pa.PAUSE = 2



teams = 'C:/Users/0220482413040/Documents/pessoal/pessoal/Python/automacao/teams.png'


local = pa.locateCenterOnScreen(teams, confidence=0.8)

pa.click(local.x, local.y)