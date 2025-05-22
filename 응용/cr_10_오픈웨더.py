import json
import requests
api_source = "1bbec8a0df58cf1d049ae054d5192c39"
url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_source}"
#################
def get_weather(city = "Seoul"):
    apikey = "1bbec8a0df58cf1d049ae054d5192c39"
    lang = "kr"

    api = f"""http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

    result = requests.get(api)
    print(result.text)
    # JSON글자를 객체로 변환
    data = json.loads(result.text)

    result = dict()
    result["weather"] = data["weather"][0]["description"]
    result["temp"] = data["main"]["temp"]
    result["feels_like"] = data["main"]["feels_like"]
    result["temp_min"] = data["main"]["temp_min"]
    result["temp_max"] = data["main"]["temp_max"]
    result["humidity"] = data["main"]["humidity"]
    result["pressure"] = data["main"]["pressure"]
    result["deg"] = data["wind"]["deg"]
    result["speed"] = data["wind"]["speed"]
    return result

import requests
import json

def get_forecast(city="Seoul"):
    apikey = "1bbec8a0df58cf1d049ae054d5192c39"
    lang = "kr"
    api = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&lang={lang}&units=metric"

    headers = {
        "User-Agent": "Mozilla/5.0"  # 서버에서 브라우저처럼 보이도록
    }

    response = requests.get(api, headers=headers)
    print("[예보 응답 상태]:", response.status_code)
    print("[예보 응답 내용]:", response.text)

    if response.status_code != 200:
        return [f"오류 발생: {response.status_code}"]

    data = json.loads(response.text)
    forecast_list = []

    # 하루에 8번 (3시간 간격), 5일 * 8 = 40개
    for item in data["list"]:
        dt_txt = item["dt_txt"]  # 날짜+시간
        desc = item["weather"][0]["description"]
        temp = item["main"]["temp"]
        temp_min = item["main"]["temp_min"]
        temp_max = item["main"]["temp_max"]
        forecast_str = f"{dt_txt} - {desc} - {int(temp)}°C ({int(temp_min)}°~{int(temp_max)}°)"
        forecast_list.append(forecast_str)

    return forecast_list


def main():
    # weather = get_weather()
    # print(weather)
    forecast = get_forecast("Seoul")
    for f in forecast[:5]:  # 앞 5개만 출력
        print(f)
        



    # # 지역 : name
    # print(data["name"], "의 날씨입니다.")
    # # 자세한 날씨 : weather - description
    # print("날씨는 ", data["weather"][0]["description"], "입니다.")
    # # 현재 온도 : main - temp
    # print("현재 온도는 ", data["main"]["temp"], "입니다.")
    # # 체감 온도 : main - feels_like
    # print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
    # # 최저 기온 : main - temp_min
    # print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
    # # 최고 기온 : main - temp_max
    # print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
    # # 습도 : main - humidity
    # print("습도는 ", data["main"]["humidity"], "입니다.")
    # # 기압 : main - pressure
    # print("기압은 ", data["main"]["pressure"], "입니다.")
    # # 풍향 : wind - deg
    # print("풍향은 ", data["wind"]["deg"], "입니다.")
    # # 풍속 : wind - speed
    # print("풍속은 ", data["wind"]["speed"], "입니다.")




if __name__ == "__main__":
    main()