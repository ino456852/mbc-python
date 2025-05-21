import requests
import json

def get_kbo_schedule(year, month):
    url = "https://www.koreabaseball.com/ws/Schedule.asmx/GetMonthlyGameSchedule"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "Mozilla/5.0",
    }
    payload = {
        "leagueId": "0",
        "seriesId": "0",
        "teamId": "0",
        "month": f"{year}-{month:02d}"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    html = data['d']  # 경기일정 HTML이 문자열로 들어있음

    # 이제 BeautifulSoup으로 HTML 파싱
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    days = soup.select("td")
    for day in days:
        date_tag = day.select_one(".dayNum")
        if not date_tag:
            continue
        date = date_tag.text.strip()
        games = day.select("li")
        print(f"{date}일의 경기 수: {len(games)}")
        for g in games:
            print("  -", g.text.strip())

get_kbo_schedule(2024, 5)  # 원하는 년도와 월 입력
