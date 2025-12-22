# 튜플
## 1. 순서가 존재하는 자료형
## 2. 불변 자료형

# 튜플 생성(값, 값, 값)
# 소괄호 내부에 값을 입력
numbers = (10,20,30,40,50)
print(numbers)
print(type(numbers))

# 연산 가능 (+, *)
tuple_1 = (1,2)
tuple_2 = (3,4)
print(tuple_1 + tuple_2) # => not plus, concat

# 특징 1: 순서가 있는 자료형
# 인덱스로 값에 접근, 슬라이싱 가능
print(numbers[1])
print(numbers[-1])
print(numbers[1:4:2])
print(numbers[::-1])

# 특징 2: 불변 자료형
# 수정, 추가 불가
