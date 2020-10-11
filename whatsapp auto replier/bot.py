import pyautogui

s = open("bee.txt",'r')

for word in s:
    pyautogui.typewrite(word)
    pyautogui.press("enter")