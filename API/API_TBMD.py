import requests
from pprint import pprint

# TMDB API 키 작성
api_key = "bfaeb3d3282b4a89984c861bdbc46bd0"

# API 요청을 위한 기본 URL
base_url = "https://api.themoviedb.org/3"

# 어떤 API를 요청할지 결정하는 url(엔드포인트)
endpoint = "movie/now_playing" # 1번. 첫 번째 범주의 데이터 필터링

# API 요청에 포함할 추가 정보(파라미터)
params = {
    "language": "ko-KR",
    "api_key": api_key,
}

headers = {"accept": "application/json"} #

# API 요청 URL 조합
request_url = f"{base_url}/{endpoint}"

# API 요청 함수 호출
response = requests.get(request_url, params=params, headers=headers)


# 응답 데이터 처리(json -> python)
response_data = response.json()

# 응답 데이터 자료형 출력
print(type(response_data))

# 응답 데이터 출력
# pprint(response_data)

# 현재 상영중인 영화의 정보만을 추출
pprint(response_data['results']) # 2. 결과 자료로만 출력하여 필터링
pprint(type(response_data['results'])) 

# 현재 상영중인 영화 목록 중 첫 3개의 영화 출력하기
pprint(response_data['results'][:3]) # 3. 상위 3개로 필터링

# 현재 상영 중인 영화 목록을 1페이지부터 5페이지까지 요청하기
    # request를 하는데, page =1 ,2 .... 5 까지 반복 요청
# 응답 데이터 리스트에 저장하고, 출력하기
response_lst = []

for i in range(1, 6):
    params = {
        "language": "ko-KR",
        "api_key" : api_key,
        "page": i
    }
    response = requests.get(
        request_url,
        params=params,
        headers=headers)
    data = response.json()
    response_lst.extend(data['results'])
    
pprint(response_lst)
pprint(len(response_lst))

# 현재 상영중인 영화 중, 평균 평점이 가장 높은 영화 찾기
max = - 9999
max_title = ''

for movie in response_lst:
    if movie['vote_average'] > max:
        max = movie['vote_average']
        max_title = movie['title']
        max_id = movie['id']
        
print(max_title, max)
print(max_id)

movie_id = max_id
url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews'

response = requests.get(url, params=params, headers=headers)
review = response.json()
pprint(review)