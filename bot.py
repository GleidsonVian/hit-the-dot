import pyautogui
import keyboard
import time


time.sleep(3)
#caso entre em um loop infinito e queira encerrar, aperte a letra Q
while keyboard.is_pressed('q') == False:
# acha a imagem para poder hitar
    loc = pyautogui.locateCenterOnScreen('C:\\pasta4\\python\\hit the dot\\hit.png', confidence=0.8)
    pyautogui.moveTo(loc)
    pyautogui.click()