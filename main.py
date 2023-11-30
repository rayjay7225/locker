import pyautogui, keyboard
from time import sleep

pyautogui.FAILSAFE = False

scr = pyautogui.size()

print("LOCKED")
i = 0
while True:
    try:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('h'):
            print("UNLOCKED")
            exit()
        pyautogui.moveTo(scr[0]/2, scr[1]/2)
        pyautogui.hotkey("win", "pgdn")
        sleep(1/50)
    except KeyboardInterrupt:
        continue
