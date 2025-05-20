import cr_01_naver_news as nn
import pandas as pd

html = nn.web_get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%ED%99%98%EC%9C%A8")

df = pd.read_html(html)
# print((df[0])) # 첫 번째 테이블
print((df[1])) # 두 번째 테이블
df[1].to_csv("환율.csv")