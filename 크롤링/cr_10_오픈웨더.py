import json
import requests
api_source = "eceec3f578e4e993f53baf397e47cba8"
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

def main():
    weather = get_weather()
    print(weather)

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