import requests
from pprint import pprint

import os
from dotenv import load_dotenv

# TMDB API 키 작성
load_dotenv()
api_key = os.getenv('datagokr_API_KEY')


# 오픈 API 서비스키(Decoding) 작성
serviceKey = "F4RlXL5VPX2Us/vi6k3j/rd8VGnhm7eEs2SJZU51bJAGoaeT7oCeQ3Ge94gjafT160Vy+eNyJ+4aStYMXezOzA=="

base_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"
endpoint = "getUltraSrtFcst"

# 요청 추가 정보(파라미터)
base_data = "20251228"  # ex) 20250616
base_time = "1200"  # ex) 0100
nx = "55"  # ex) 55
ny = "127"  # ex) 127

params = {
    "serviceKey": serviceKey,
    "pageNo": "1",
    "numOfRows": "1000",
    "dataType": "JSON",
    "base_date": base_data,
    "base_time": base_time,
    "nx": nx,
    "ny": ny,
}

request_url = f"{base_url}/{endpoint}"

# API 요청
response = requests.get(request_url, params=params)

# 응답 데이터 처리
response_data = response.json()
pprint(response_data)