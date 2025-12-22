 # 1일차 복습

# 변수 = 상자
# 할당연산자 (=) 를 통해 변수를 할당

name = 'alex' 
print(name) # 이제 name을 부르면, alex라는 문자열이 나온다!
print('alex')

# => 변수는 사용자가 사용하기 편하라고 만든다

variable_1 = 10
variable_2 = 30 # 의미없는 변수

age = 10
money = 30 # 의미있는 변수
# 변수명 설정 시에는 의미를 담아야 사용이 편하다

print(variable_1)
print(age)

# 자료형
# 자료형이란? 데이터의 특성

print('===== 자료형 =====')

name = 'alex'
age = 20     # 정수형
money = 31.5 # 실수형
is_male = True

# 1. 숫자
print(type(age))   # int : 정수형 (0, 1, -1)
print(type(money)) # float : 실수형 (소수점이 있는 모든 숫자)

print(type(2.0)) # 컴퓨터는 . 소수점이 있으면, 바로 float로 여김

# 2. 문자

# "",'' 를 통해 글자들의 모음을 만든다
# 쌍따옴표, 따옴표 안에 있는 모든 것들이 문자열이 된다
print(name)
print(type(name))

# 아래 두 케이스 모두 문자열이다.
print("")
print(" ")

# 3. 불린형
# 참(True) / 거짓(False)
# true, TRUE -> 불린형이 아님! 대소문자에 유의
print(is_male)
print(type(is_male))

# 명시적 형변환
# 내장함수 사용하여 변환
    # int(변환하고 싶은 값)
    # float(변환하고 싶은 값)
    # str(변환하고 싶은 값)
    # bool(변환하고 싶은 값)

print(type(int('3')))   # 가능
# print(type(int('3.0'))) # 불가능
print(type(int(float('3.0')))) # 가능하게 만들 수 있다.

# 연산자
# 연산의 목적 "처리"

print('===== 연산자 =====')

# 1. 산술 연산자 (+,-,*,/,//,%,**) -> 수치형 자료 계산
print(3 ** 5 + 10) # 값을 계산하기 위함

# 2. 복합연산자 
# 산술연산 후, (+,-,*,/,//,%,**) 재할당 (=)
# a = a + b 
# a += b -> 복합 연산자의 사용
a = 3
b = 5

a += b
print(a)

# 3. 비교연산자
# 두 값을 비교 -> True, False

# (1) 대소 비교 : <, >, <=, >= (수치형 자료를 위주로 사용)
print(a)
print(b)
print(a < b) # False

print('Alex' < 'Aun') # 같은 자료형 끼리 가능은 하나, 직관적인 이해가 어려움
# => 수치형 자료를 위주로 사용

# (2) 일치 비교 : == (같다), != (같지 않다)
# 자료형을 크게 타지 않는다.
print(is_male)
print(age)

print(is_male == age) # 다른 자료형 끼리도 비교 가능하다.

# => 불린형으로 연산 결과가 도출되기 때문에 "조건문 / 반복문" 내에서 많이 사용


# 4. 논리연산자
# 논리연산의 대상이 되는 a, b는 불린형이여야 한다.
# a and b : a,b가 모두 True일 때만 True
# a or b : a,b 둘중 하나라도 True일 때, True
# not a : a의 반대 

print(name == 'alex')
print(age > 20)

print(name == 'alex' and age > 20) # 조건문에서 주로 사용하는 형태

# 조건문
# if 조건1:
    # 조건1을 만족할 때 실행되는 코드블럭
# elif 조건2:
    # 조건1을 만족하지 않으면서, 조건 2를 만족할때 실행되는 코드블럭
# else:
    # 그외 모든 케이스에 대해 실행하는 블럭

print('===== 조건문 =====')
name = 'jun'

print(age)
print(money)

if name == 'alex' and money > 10: # False and True -> if False와 같다.
    print('부자 alex, 안녕하세요!')
elif name == 'alex': # False
    print('그냥 alex, 안녕하세요!')
else:
    print('누구세요?')
    print('1번 케이스: 장난입니다~') # 1번 케이스

# 조건문과 무관히 실행되는 케이스
print('2번 케이스: 장난입니다~') # 2번 케이스

# 들여쓰기에 따라, 의도와 다르게 작동할 수도 있다.