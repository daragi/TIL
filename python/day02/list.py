# 컨테이너 자료형

## 리스트 (List)
### 연속되어 있는, 순서가 존재하는, 가변 자료형
### 대괄호 []를 통해 생성

numbers = [10,20,30,40,50]
print(numbers)
print(type(numbers))

example = [10, '20', 30.0, True, []] # => list는 여러가지 자료형이 올 수 있음
print(example)

empty = []
print(empty)
print(type(empty))
print(bool(empty)) # => 빈 리스트는 False임

### 리스트연산
lst_1 = [1,2]
lst_2 = [3,4]
print(lst_1 + lst_2) # => add 가 아닌 concat
print(id(lst_1))
print(id(lst_2))

# * 연산: 같은 리스트를 n번 반복하여 합쳐서 '새로운 리스트' 생성
print(lst_1 * 3)
# print(lst_1 * 1.5) # int만 호환 가능
# print(lst_1 * lst_2) # int만 호환 가능

print('===인덱싱===')
### 특징 1. 순서가 있는 자료형
### 인덱싱 = 인덱스라고 하는 위치를 기준으로 원소에 접근
### 리스트[인덱스] -> 인덱스 위치의 원소를 확인 가능 (0부터 시작, n-1번까지 조냊)
### 음수 인덱싱 가능 (-1이 가장 마지막 원소)

print('===슬라이싱===')
### 리스트의 일부분을 원하는 만큼 자르는 방법을 의미한다.
print(numbers[1:4])
print(numbers[5:2:-1])

# 리스트 뒤집기
print(numbers [::-1])

### 리스트와 관련된 함수들 (=Mutable)
### 객체 자체를 바꾸지 않고도 변경 가능
# 1. 수정
print(numbers)
print(id(numbers)) # -> 주소 값은 변하지 않음
numbers[1] = -1

print(numbers)

# 2. 추가
# 리스트의 가장 마지막 위치에 추가
numbers.append(60)
print(numbers)
print(id(numbers))

# 3. 삭제
numbers.pop()
print(numbers)