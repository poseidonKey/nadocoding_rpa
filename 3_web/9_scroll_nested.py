import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(5)

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()
# 엘리먼트가 나타 나도록 위치를 이동

# 방법 2 : 좌표 정보 이용
xy = elem.location_once_scrolled_into_view # 함수가 아니니까 () 쓰지 마세요
print("type : ", type(xy))  # dict
print("value : ", xy)
# 화면에 보이지 않아도 처리 된다.
elem.click()

time.sleep(5)
browser.quit()