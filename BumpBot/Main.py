import pyautogui, time

def Bump(self):
    script = open('C:/Users/morga/Desktop/Python files/Projects(not complete)/BumpBot/BumpMsg.txt', 'r')
    for char in script:
        pyautogui.typewrite(char)
        pyautogui.press('enter')

