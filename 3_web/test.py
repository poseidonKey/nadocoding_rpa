import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome("chromedriver.exe")
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

# cars 에 해당하는 element 를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
elem = browser.find_element(by=By.ID,value='cars')
# option[1] : 첫번째 항목 
# option[2] : 두번째 항목 
# ...
elem.click()