# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time


def get_browser(url, alive=False):
    # 브라우저 꺼짐 방지 옵션
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    if alive == True:
        chrome_options.add_experimental_option("detach", True)
    # 크롬드라이버 실행
    driver = webdriver.Chrome(options=chrome_options)

    # 크롬 드라이버에 url 주소 넣고 실행
    driver.get(url)
    return driver  # 웹브라우저 컨트롤 객체


def main():
    url = "https://www.koreabaseball.com/Schedule/Schedule.aspx"
    # 브라우저 시작
    driver = get_browser(url, alive=False)
    time.sleep(3)
    year = driver.find_element(By.CSS_SELECTOR,"#ddlYear").get_attribute("value")
    month = driver.find_element(By.CSS_SELECTOR,"#ddlMonth").get_attribute("value")
    # 일정 달력 검색
    cal = driver.find_element(By.CSS_SELECTOR,"#tblScheduleCal")
    sched_list = cal.find_elements(By.CSS_SELECTOR, "tbody td")
    # print(len(sched_list))
    # sched는 <td> ... </td>를 의미
    for sched in sched_list[4:10]:
        # <td class="endGame">
        class_name = sched.get_attribute("class")
        # print(class_name)
        # 경기날짜
        sched_date = sched.find_element(By.CSS_SELECTOR, ".dayNum").get_attribute("innerText").strip()
        # 치뤄진 경기는 <a>, 취소된 경기는 <li>
        sched_sub_list = sched.find_elements(By.CSS_SELECTOR, "li")
        print("%s년 %s월 %s일의 경기갯수는 %s개" % (year,month,sched_date,len(sched_sub_list)))
        for sched_sub in sched_sub_list[1:]:
            print(sched_sub.get_attribute("innerText").strip())


if __name__ == "__main__":
    main()
