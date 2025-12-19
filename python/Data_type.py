print('Hello World!')

# 자료형

# 1. 숫자
## 1) 정수
print(1)
print(-1)
print(0)
print(type(1))
print(type(0))
print(type(-1))

## 2) 실수
print(3.141592)
print(-12.3)
print(type(3.0))

# 2. 문자
print('강동호')
print('이지원')
print("'서채원'")

## 공백도 문자다.
print(' ')
## 숫자와 문자는 다르다
print(type(123))
print(type('123'))

# 3. 불린 -> 대소문자 구분하기
print(type(True))
print(type(False))

# 정리!
# 1. 숫자: 정수(int), 실수(float)
# 2. 문자: 문자열(str) -> '12345', '!@#!@$#@' 문자들의 모음
# 3. 불린: 불린형(bool) -> True, False (주의! 대소문자 구분 주의)


print('=== 명시적 형변환 ===')
# 정수형으로 변환 : int()
print(1.23)
print(int(1.23))
print(type(int(1.23)))

# 정수로 바로 변환 가능한 형태일 때 가능
print('20')
print(int('20'))

print(int('20'))
# print(int('20.0')) -> 실수 => 정수 불가

# 실수형 변환 : float()
print(float(-10))
print(float('20.0'))

# 문자열 변환 : str()
print(type(str(True)))

# 불린형 : bool()
# True / False
print(bool(0.0))
print(bool(0.0000000000000001))


# 자료형 정리
# 1. 숫자형
# 정수 (int) : 소수점이 없는 숫자 (0,+,-)
# 실수 (float) : 소수점이 있는 숫자 (3.14)

# 2. 문자열 (str)
# 문자의 형태를 가진 모든 글자의 모음
# "쌍따옴표", '따옴표' 를 통해 만든다 (단, 짝이 맞아야 함)
print('따옴표 "안"에 따옴표')
print('따옴표 \'안\'에 따옴표')

# 3. 불린형 (bool)
# True, False -> 대소문자 주의

# 각 자료형들은 내장함수 int(),float(),str(),bool()을 통해
# 명시적 형변환을 할 수 있습니다!