import pyautogui

# 그림판의 자르기를 통해 순수 이미지만 png 파일로 저장해야 함. 포토스케이프 안됨
file_menu = pyautogui.locateOnScreen("./2_desktop/menu_test.png")
print(file_menu)
# pyautogui.click(file_menu)

# 약간의 시간 소요 됨
# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 없을 경우 None을 출력. 예민한 편임.
# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 화면에 여러개의 목표가 있을 경우 locateAllOnScreen을 이용
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# 화면에 여러개의 목표가 있을 경우 처음 것만 처리
# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale 흑백 모드로 전환해 처리. 정확성이 약간 떨어짐.
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정 빠름. mouseInfo 이용
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881 - 1488, 137))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정 * 사용하기 위해 pip install opencv-python 설치해야 한다.
# 예를 들어 0.1을 주면 엉뚱한 것을 찾아준다.
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
#file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")

# 아래와 같이 계속 기다림으로 처리할 수 있음
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
#pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

#pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 10)
