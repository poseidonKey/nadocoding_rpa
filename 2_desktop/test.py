import pyautogui
# file_menu = pyautogui.locateOnScreen("./trash_icon.png")
# print(file_menu)
# # pyautogui.click(file_menu)
# pyautogui.moveTo(file_menu)
file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
if file_menu_notepad:
    pyautogui.click(file_menu_notepad)
else:
    print("발견 실패")