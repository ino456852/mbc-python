import cr_01_naver_weather as nw

html = nw.web_get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8+%EC%84%9C%EC%9A%B8&ackey=c2x9vmop")
t = nw.find_text(html,".temperature_text")
print(t)

r_list = nw.find_text_list(html, ".week_list")
for r in r_list:
    print(r)

