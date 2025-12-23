# 2일차 리뷰

# 컨테이너 자료형
print('===== 리스트 =====')
# 리스트 (list)

greetings = ['안녕하세요!','니하오!','봉주르!','올라!']
print(greetings)
print(type(greetings))
print(len(greetings)) # 몇개의 값을 가지고 있는지 확인 가능

# +연산, *연산
# + : 이어 붙인다. 리스트끼리
# * : 이어 붙인다. 같은 리스트를 n번

print(greetings + greetings)
print(greetings * 2)
# 연산 결과 새로운 리스트 만든다.


# 리스트의 특징 1 : 순서가 존재
# 순서(위치)로 접근 가능
# 인덱싱       0 ~ n-1번째까지
# 음수 인덱싱  -n ~ -1 번째까지
print(greetings[0])
print(greetings[1])
print(greetings[2])
print(greetings[3])
print(greetings[len(greetings)-1])
# print(greetings[4]) # 에러

print(greetings[1:3]) # 슬라이싱

# 리스트 특징 2 : 가변 자료형 (mutable)
# 변경 -> 추가, 수정, 삭제 가능
# 리스트의 주소값을 바꾸지 않더라도 가능

# 값 수정
print(f'수정 전 인삿말 : {greetings}')
print(f'수정 전 주소값 : {id(greetings)}')

greetings[0] = '좋은 아침!'

print(f'수정 후 인삿말 : {greetings}')
print(f'수정 후 주소값 : {id(greetings)}')

# 값 추가
# greetings[6] = '곤니찌와' # IndexError
greetings.append('곤니찌와!')

print(f'추가 후 인삿말 : {greetings}')
print(f'추가 후 주소값 : {id(greetings)}')

# 값 삭제
greetings.pop()
print(greetings)
print(f'삭제 후 주소값 : {id(greetings)}')

print('===== 문자열 =====')

# 연속적인 문자들의 모음
# "", ''
hello = '안녕하세요! 오늘도 좋은 하루입니다~'
print(hello)
print(type(hello))
print(len(hello))

# 특징 1. 순서가 존재
print(hello[-1]) # 위치 인덱싱 가능
print(hello[:5]) # 슬라이싱 가능

# 특징 2. 불변 자료형 (immutable)
# hello[-1] = '!'
# TypeError: 'str' object does not support item assignment

print(id(hello))

hello = hello[:-1] + '!' # 문자열 자체를 바꾼 것이 아닌 새로 재할당
print(hello)
print(id(hello))

# 레인지 (range)
# 연속된 정수 목록 반환

print(list(range(1, 11, 2))) # [1, 3, 5, 7, 9]

for i in range(1, 11, 2):
    print(i)


print('===== 반복문 =====')
# for문 : 반복 횟수가 정해져 있을 때
# for 변수 in 컨테이너:
    # 코드블럭

print(greetings)
print(len(greetings))

# 예시 1 : 리스트 순회
for greeting in greetings:
    print(greeting)
    

# 예시 2 : range 순회
for idx in range(len(greetings)):
# for idx in range(4): 와 동일하다.
    # range(4) 연속된 정수목록 [0,1,2,3] 반환
    print(idx)
    print(greetings[idx])

# for문 불가능
# 순회할 수 없는 것은 for문의 대상이 될 수 없다.
# for i in 3:
#     print('3번 반복') # TypeError: 'int' object is not iterable


# while문
# 반복 횟수가 정해져 있지 않을때 조건을 기준으로 반복
i = 0 # 조건에서 사용할 변수 생성

print()
while i < len(greetings):
    print(greetings[i])
    i += 1 # 조건에 대한 증감이 필요