# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 브라우저 꺼짐 방지 옵션
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 크롬드라이버 실행
driver = webdriver.Chrome(options=chrome_options)

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://www.naver.com/')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)
# 네이버 검색어 입력창
search_box = driver.find_element(By.CSS_SELECTOR, "#query")
search_box.send_keys("파이썬")
# search_box.send_keys(Keys.RETURN)

search_button = driver.find_element(By.CSS_SELECTOR, "#search-btn")
btn = search_button.click()
time.sleep(3)