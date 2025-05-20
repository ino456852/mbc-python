# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time


def get_browser(url):
    # 브라우저 꺼짐 방지 옵션
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # 크롬드라이버 실행
    driver = webdriver.Chrome(options=chrome_options)

    #크롬 드라이버에 url 주소 넣고 실행
    driver.get(url)
    return driver # 웹브라우저 컨트롤 객체

def find_text(driver, selector):
    t = driver.find_element(By.CSS_SELECTOR,selector).text
    return t

def find_text_list(driver, selector):
    result_list = []
    e_list = driver.find_elements(By.CSS_SELECTOR,selector)
    for e in e_list:
        result_list.append(e.text)
    return result_list

driver = get_browser("https://dhlottery.co.kr/common.do?method=main")
time.sleep(3) # 페이지 로딩시간 필요
# t = find_text(driver,".card_data_now") # 지금 온도
# print(t)
# 오늘 날씨 요약
# t = find_text(driver,'.day_data') # 
# print(t)
t_list = find_text_list(driver,'.result_prize_wrap img') # 
for t in t_list:
    print(t)

# # 페이지가 완전히 로딩되도록 3초동안 기다림
# time.sleep(3)
# # 네이버 검색어 입력창
# search_box = driver.find_element(By.CSS_SELECTOR, "#query")
# search_box.send_keys("파이썬")
# # search_box.send_keys(Keys.RETURN)

# search_button = driver.find_element(By.CSS_SELECTOR, "#search-btn")
# btn = search_button.click()
# time.sleep(3)