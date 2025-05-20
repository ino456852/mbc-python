from cr_01_naver_news import *

html = web_get("https://news.daum.net/tech",encoding='utf-8')
# print(html)
tit_list = find_text_list(html, ".list_newsheadline2 .tit_txt, .list_newsblock .tit_txt")
print("응답갯수=%s" %len(tit_list))
for t in tit_list:
    print(t)