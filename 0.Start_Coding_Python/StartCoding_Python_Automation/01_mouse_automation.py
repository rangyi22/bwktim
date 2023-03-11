import pyautogui
import time

# 1. Print the size of the screen
# print(pyautogui.size())

# 2. Print the position of the mouse
#time.sleep(2)
#print(pyautogui.position())

# 3. Move the mouse
# Mac: 손쉬운 사용 vscode 사용 권한  설정
# pyautogui.moveTo(31, 261)
pyautogui.moveTo(31, 261, 2)

# 4. Mouse Click
pyautogui.click()
pyautogui.click(button='right')
pyautogui.doubleClick()
pyautogui.click(clicks=3, interval=1) # click three times per 1 sec'

# 5. Mouse Drag
