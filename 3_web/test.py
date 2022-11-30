import time
from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/home/p/index.nhn')

# '무선마우스' 입력
elem = browser.find_element(
    by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/input')
# elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('무선마우스')

time.sleep(1)

elem.send_keys(Keys.ENTER)  # 검색 버튼 클릭을 위해 Enter 처리
=======

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://flight.naver.com/flights/')
time.sleep(5)
# 가는 날 클릭
browser.find_element(by=By.XPATH,value='//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
# browser.find_element(by=By.LINK_TEXT,value='가는 날').click()
# browser.find_element_by_link_text('가는날 선택').click()
>>>>>>> 661768ac9b8aab6ef98e75a2fe26f1871189b8be
