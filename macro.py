# ! made by YoungDragonBoot
# ! for: Trimutri Online

import keyboard as kb
import time as t
import pyautogui

RUNNING = True

t.sleep(5)
while RUNNING:
    if kb.is_pressed('q'):
        RUNNING = False
        break
    else:
        pyautogui.press('e')
        print('Macro Update | Pressed E')
        pyautogui.press('r')
        pyautogui.press('r')
        pyautogui.press('r')
        pyautogui.press('r')
        print('Macro Update | Pressed R')
        t.sleep(15)