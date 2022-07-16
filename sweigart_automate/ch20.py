# 20 CONTROLLING THE KEYBOARD AND MOUSE WITH GUI AUTOMATION

#! Installing the pyautogui Module
import pyautogui
# import os
# os.environ['DISPLAY'] = ':0'


wh = pyautogui.size()  # Obtain the screen resolution.
print(wh)
# Size(width=1920, height=1080)
print(wh[0])
# 1920
print(wh.width)
1920
