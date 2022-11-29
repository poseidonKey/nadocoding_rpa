import pyautogui
file_menu = pyautogui.locateOnScreen("./trash_icon.png")
print(file_menu)
# pyautogui.click(file_menu)
pyautogui.moveTo(file_menu)