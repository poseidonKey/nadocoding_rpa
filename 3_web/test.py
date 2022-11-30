import time
from selenium import webdriver

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