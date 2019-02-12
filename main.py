import pyautogui

width, height = pyautogui.size()

for i in range(10):
    pyautogui.moveRel(100, 100, duration=0.25)
    pyautogui.moveRel(200, 100, duration=0.25)
    pyautogui.moveRel(200, 200, duration=0.25)
    pyautogui.moveRel(100, 200, duration=0.25)