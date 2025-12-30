import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# 
# 전체 html 텍스트 출력

doc = response.text
print(type(doc))

data = response.json()
print(data)
print(type(data))