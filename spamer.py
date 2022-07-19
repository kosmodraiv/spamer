import time
import pyautogui

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read().split('\n')

time.sleep(5)

while True:
    pyautogui.typewrite('text')
    pyautogui.press('enter')
    time.sleep(1)