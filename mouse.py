import pyautogui

class Mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveX(self, step):
        pyautogui.moveTo((self.x + step), self.y)
        self.x = self.x + step

    def moveY(self, step):
        pyautogui.moveTo(self.x, (self.y + step))
        self.y = self.y + step
