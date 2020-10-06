from openpyxl import load_workbook
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#엑셀 데이터 불러오기
load_wb = load_workbook("C:\Users\GL\Desktop/application_info.xlsx", data_only=True)
#시트 이름으로 불러오기
load_ws = load_wb['Sheet1']
#크롬exe 실행
driver = webdriver.Chrome('C:/Users/GIGM/Desktop/chromedriver.exe')
#해당 사이트 접속
driver.get(str(load_ws['B1'].value))
sleep(1)
#사이트 이름 확인
assert "지원서" in driver.title

#인풋값 입력 시작


elem = driver.find_element_by_id("englishName")
elem.send_keys(load_ws['B6'].value)

elem = driver.find_element_by_id("chineseName")
elem.send_keys(load_ws['B7'].value)

elem = driver.find_element_by_id("genderFlag")
elem.click()

elem = driver.find_element_by_id("birthday")
elem.send_keys(load_ws['B8'].value)

# elem = driver.find_element_by_id("email")
# elem.send_keys(load_ws['B4'].value)

# elem = driver.find_element_by_id("emailConfirm")
# elem.send_keys(load_ws['B4'].value)

# elem = driver.find_element_by_id("password")
# elem.send_keys(load_ws['B5'].value)

# elem = driver.find_element_by_id("passwordConfirm")
# elem.send_keys(load_ws['B5'].value)

