# 리스트, 딕셔너리, 반복문
# enumerate()
# 딕셔너리의 items 메서드처럼 인덱스와 값을 한번에 받기 가능 

names = ['kyle', 'alex','justin']
for idx, name in enumerate(names):
    print(idx, name)

# 컴프리헨션
## 컴프리헨션 사용x
squares = []
for i in range(1,6):
    if i % 2 ==0:
        squares.append(i ** 2)
print(squares)

## 컴프리헨션 사용
squares = [i ** 2 for i in range(1,6) if i % 2==0]
print(squares)