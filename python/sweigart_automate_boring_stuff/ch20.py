# 20 CONTROLLING THE KEYBOARD AND MOUSE WITH GUI AUTOMATION

#! Installing the pyautogui Module
import pyautogui
# import os
# os.environ['DISPLAY'] = ':0'

#? Controlling Mouse Movement

# wh = pyautogui.size()  # Obtain the screen resolution.
# print(wh)
# # Size(width=1920, height=1080)
# print(wh[0])
# # 1920
# print(wh.width)
# # 1920

#? Moving the Mouse

# import pyautogui
# for i in range(10): # Move mouse in a square.
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# import pyautogui
# for i in range(10):
#     pyautogui.move(500, 0, duration=0.25)   # right
#     pyautogui.move(0, 500, duration=0.25)   # down
#     pyautogui.move(-500, 0, duration=0.25)  # left
#     pyautogui.move(0, -500, duration=0.25)  # up

## Getting the Mouse Position

# print(pyautogui.position()) # Get current mouse position.
# # Point(x=311, y=622)
# p = pyautogui.position() # And again.
# print(p)
# # Point(x=1536, y=637)
# print(p[0]) # The x-coordinate is at index 0.
# # 1536
# print(p.x) # The x-coordinate is also in the x attribute.
# # 1536

#! Controlling Mouse Interaction

## Clicking the Mouse

# import pyautogui
# pyautogui.click(10, 5)

## Dragging the Mouse

import pyautogui, time
# time.sleep(5)
# pyautogui.click()    # Click to make the window active.
# distance = 300
# change = 20
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2)   # Move right.
#     distance = distance - change
#     pyautogui.drag(0, distance, duration=0.2)   # Move down.
#     pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
#     distance = distance - change
#     pyautogui.drag(0, -distance, duration=0.2)  # Move up.

## Scrolling the Mouse

# pyautogui.scroll(200)

#! Planning Your Mouse Movements

# import pyautogui
# pyautogui.mouseInfo()

#! Working with the Screen

## Getting a Screenshot

# import pyautogui
# im = pyautogui.screenshot()

## Analyzing the Screenshot

# import pyautogui
# pyautogui.pixel((0, 0))
# # (176, 176, 175)
# pyautogui.pixel((50, 200))
# # (130, 135, 144)


# import pyautogui
# pyautogui.pixel((50, 200))
# # (130, 135, 144)
# pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
# # True
# pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
# # False

## Image Recognition

# import pyautogui
# time.sleep(5)
# b = pyautogui.locateOnScreen('submit.png')
# print(b)
# # Box(left=643, top=745, width=70, height=29)
# print(b[0])
# # 643
# print(b.left)
# 643

# print(list(pyautogui.locateAllOnScreen('submit.png')))
# [(643, 745, 70, 29), (1007, 801, 70, 29)]

# pyautogui.click(b)

# pyautogui.click('submit.png')

#! Getting Window Information

## Obtaining the Active Window

# import pyautogui
# fw = pyautogui.getActiveWindow()
# print(type(fw))
# # <class 'pygetwindow._pygetwindow_win.Win32Window'>
# print(fw)
# # <Win32Window left="-9", top="-9", width="1938", height="1060", title="ch20.py - GIT - Visual Studio Code">
# print(fw.title)
# # ch20.py - GIT - Visual Studio Code
# print(fw.size)
# # Size(width=1938, height=1060)
# print(fw.left, fw.top, fw.right, fw.bottom)
# # -9 -9 1929 1051
# print(fw.topleft)
# # Point(x=-9, y=-9)
# print(fw.area)
# # 2054280
# pyautogui.click(fw.left + 10, fw.top + 20)


## Other Ways of Obtaining Windows

# winds = pyautogui.getAllWindows()
# print(winds)
# # winds = pyautogui.getWindows()
# for win in winds:
#     print(win)

# print(pyautogui.getAllTitles())

## Manipulating Windows

# import pyautogui
# fw = pyautogui.getActiveWindow()
# print(fw.width) # Gets the current width of the window.
# # 1938
# print(fw.topleft) # Gets the current position of the window.
# # (174, 153)
# fw.width = 1000 # Resizes the width.
# fw.topleft = (800, 400) # Moves the window.

# import pyautogui
# time.sleep(5)
# fw = pyautogui.getActiveWindow()
# print(fw.isMaximized) # Returns True if window is maximized.
# # False
# print(fw.isMinimized) # Returns True if window is minimized.
# # False
# fw.isActive # Returns True if window is the active window.
# # True

# fw.maximize() # Maximizes the window.
# print(fw.isMaximized)
# # True

# time.sleep(2)
# fw.restore() # Undoes a minimize/maximize action.

# time.sleep(2)
# fw.minimize() # Minimizes the window.

# # Wait 5 seconds while you activate a different window:
# time.sleep(5)

# # It getting lost here
# fw.activate()
# fw.maximize()
# time.sleep(2)
# fw.close() # This will close the window you're typing in.


#! Controlling the Keyboard

## Sending a String from the Keyboard

# time.sleep(5)
# pyautogui.click(100, 200)
# pyautogui.write('Hello, world!') # Type the full string instantly.
# pyautogui.write('Hello, world!', interval=0.25) # interval - integer or float value of the number of seconds to pause.


## Key Names

# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

## Pressing and Releasing the Keyboard

# time.sleep(5)
# pyautogui.click(100, 200)
# pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

## Hotkey Combinations

# pyautogui.hotkey('ctrl', 'c')
# pyautogui.hotkey('ctrl', 'v')


## sleep() and countdown() functions

# import pyautogui
# pyautogui.sleep(3) # Pauses the program for 3 seconds.
# pyautogui.countdown(10) # Counts down over 10 seconds.
# # 10 9 8 7 6 5 4 3 2 1
# print('Starting in ', end=''); pyautogui.countdown(3)
# # Starting in 3 2 1

#! Project: Automatic Form Filler

## Displaying Message Boxes

import pyautogui
pyautogui.alert('This is a message.', 'Important')
# 'OK'
pyautogui.confirm('Do you want to continue?') # Click Cancel
# 'Cancel'
pyautogui.prompt("What is your cat's name?")
# 'Zophie'
pyautogui.password('What is the password?')
# 'hunter2'