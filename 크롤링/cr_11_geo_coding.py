# pip install geopy
from geopy.geocoders import Nominatim
def select_w():
    addr = "한국 서울"
    geoloc = Nominatim(user_agent = 'South Korea', timeout=None)    # 사용자 에이전트를 설정
    geo = geoloc.geocode(addr)
    return geo
    print(geo)
    print(geo.latitude, geo.longitude )

    ###################

    import requests
    import json

    # OpenWeatherMap API 키
    API_KEY = "1bbec8a0df58cf1d049ae054d5192c39"

    # 강동구 암사동의 좌표 (위도, 경도)
    LATITUDE = geo.latitude
    LONGITUDE = geo.longitude

    # API 요청 URL
    URL = f"http://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric&lang=ko"
    # API 요청 및 결과 처리
    try:
        response = requests.get(URL)
        response.raise_for_status() # 오류 발생 시 예외 처리
        data = response.json()

        # 날씨 정보 추출
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        

        # 결과 출력
        print(f"{addr}의 현재 날씨:")
        print(f"기온: {temperature}°C")
        print(f"습도: {humidity}%")
        print(f"날씨: {description}")

    except requests.exceptions.RequestException as e:
        print(f"API 요청 중 오류 발생: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON 파싱 중 오류 발생: {e}")