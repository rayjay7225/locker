import pyautogui, keyboard
from time import sleep

pyautogui.FAILSAFE = False

scr = pyautogui.size()

i = 0
while True:
    try:
        pyautogui.moveTo(scr[0]/2, scr[1]/2)
        sleep(1/50)
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('h'):
            exit()
    except KeyboardInterrupt:
        continue
