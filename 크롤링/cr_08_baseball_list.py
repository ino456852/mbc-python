# selenium의 웹드라이버를 사용하기 위한 import
from selenium import webdriver

# CSS 선택자 지정을 위한 By 모듈 import
from selenium.webdriver.common.by import By

# 크롬 브라우저 실행 옵션을 조정하기 위한 모듈 import
from selenium.webdriver.chrome.options import Options

# 웹페이지 로딩을 기다리기 위한 time 모듈 import
import time


# 웹 브라우저를 실행하고, 해당 URL로 접속한 뒤, 드라이버 객체를 반환하는 함수
def get_browser(url):
    # 브라우저가 자동으로 닫히지 않도록 옵션 설정
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # 크롬 드라이버 실행 (옵션 포함)
    driver = webdriver.Chrome(options=chrome_options)

    # 주어진 URL에 접속
    driver.get(url)

    # 드라이버(브라우저 제어 객체) 반환
    return driver


# 주어진 CSS 선택자에 해당하는 모든 요소를 찾아 텍스트만 리스트로 반환하는 함수
def find_text_list(driver, selector):
    result_list = []  # 결과 저장용 리스트 생성

    # selector에 해당하는 모든 요소 가져오기
    e_list = driver.find_elements(By.CSS_SELECTOR, selector)

    # 각 요소에서 텍스트만 추출하여 리스트에 추가
    for e in e_list:
        result_list.append(e.text)

    return result_list  # 텍스트 리스트 반환


# 웹 브라우저 실행 및 대상 페이지 접속
driver = get_browser("https://www.koreabaseball.com/Schedule/Schedule.aspx")

# 페이지가 완전히 로드될 때까지 3초 대기
time.sleep(3)

# #boxList 안에 있는 각 경기 항목(li)을 모두 선택하여 텍스트 리스트로 저장
t_list = find_text_list(driver, "#boxList")

# 추출된 경기 정보를 한 줄씩 출력
for t in t_list:
    print(t)
