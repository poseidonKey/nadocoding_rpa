import pyautogui
# 동작을 멈추기 위해 모니터 4개 귀퉁이에 갖다 대면 프로그램이 멈춘다.
#
#pyautogui.FAILSAFE = False 로 하면 위의 기능을 스톱, 사용하지 않는 게 좋다.
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
#pyautogui.mouseInfo()

for i in range(5):
    pyautogui.move(100, 100)