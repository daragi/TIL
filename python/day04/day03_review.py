# 3일차 복습

# 변수 ~ 함수까지
# 비교하며, 설명

print("= 변수와 값 =")
# 변수와 값의 개념을 헷갈림
# 식별자 = 리터럴

age = 10
# a -> 데이터를 가리키는 이름 (변수)
# 10 ->  실제 데이터 (값)

age = 20
print(age)
# => 변수명을 값을 잘 나타낼 수 있도록 이름 짓자!


print('== 입력과 출력 ==')
print('1.입력')
# 입력 : input() 내장함수
    # 목적 : 외부로부터 값 받기(사용자가 터미널 상 입력)
    # 반환값 : 문자열(str)

# name = input('이름을 입력해주세요')
# print(name)
# print(type(name))

print('2.출력')
# 출력 : print() 내장함수
    # 목적 : 내부 값(파이썬)을 외부(터미널 상)에서 확인하기 위함
    # 반환값 : 없음

numbers = [1,2,3,4,5]    
len(numbers) # 내부에서 확인
print(len(numbers))

# 데이터 흐름
# input() : 외부(터미널) -> 내부(코드)
# print() : 내부(코드) -> 외부(터미널)

print('== 연산자 비교 ==')
print('= 산술 연산자 =')
    # 연산 대상 : 수치형
    # 반환값 : 숫자 계산 마친 값
    
a = 10 # int
b = 5.0 # float
print(a + b)

print('= 복합 연산자 =')
    # 연산 대상 : 수치형 / 가끔 문자열,리스트(+,*)
    # 반환 대상 : 산술연산 이후, 그 자리에 재할당한 값

# a = a + b
# 연산 축약
a += b
print(a)

print('= 비교 연산자 =')
    # 연산 대상 : 같은 선상에서 비교할 수 있는 것들
    # 반환 값 : True, False (bool 자료형)

# a 비교연산자 b 의 형태
    # 대소비교 : <, <=, >, >=
    # 일치비교 : ==, !=

print(a < b)

c = '오늘은'
d = '12/24'

print(c > d) # 대소 비교는 가능하나, 직관적이지 않을 수 있음
print(a != c) # 같은 자료형이 아니더라도, 일치비교는 가능

print('== 논리 연산자 ==')
    # 연산 대상 : 논리값 (True / False)
    # 반환값 : 논리값 (True/False)

# 형태 
# a and b, a or b, not a
print(True and False)

# 비교 연산과 함께 사용
print(a == b and c != d)

# 아래처럼 변수에 할당하여 사용하는 것도 가능
condition1 = a == b
condition2 = c != d

print(condition1, condition2)
print(condition1 and condition2)

# 논리연산의 단축평가
print(age)
print(age == 100 and age == 200)
# False and 정의되지 않은 변수
# -> 필요이상의 연산 X, 바로 거짓 반환

print('===== 조건문과 반복문 =====')

# 조건문
    # 핵심 질문 : 특정 조건이 맞는가?
    # 실행 횟수 : 1번
    # 판단 기준 : 논리 조건 (True, False)

score = 70

print('~ 조건문 시작 ~')
if score >= 60:
    print('합격')
elif score >= 50:
    print('예비합격')
else:
    print('불합격')
print('~ 조건문 끝 ~')

# 반복문
    # 핵심 질문 : 몇 번 반복할 것인가?
    # 실행 횟수 : 여러 번
    # 판단 기준 : 데이터의 갯수(for문), 조건(while문)

scores = [70, 20, 50, 90, 10]

print('~ 반복문 시작 ~')
for score in scores:
    print(score)
print('~ 반복문 끝 ~')

# 조건문 + 반복문 => 강력한 코드
# 조건문 = 판단, 반복문 = 처리량
print(scores)
for score in scores:
    if score >= 60:
        print('합격')
    elif score >= 50:
        print('예비합격')
    else:
        print('불합격')
        
# 반복문의 종류
# 언제 무엇을 사용해야 하는가?

# for문 : 반복 횟수가 정해진 반복문
# while문 : 반복 횟수가 정해지지 않은 반복문

print('== for문 ==')
    # 사용 기준 : 반복 횟수 명확
    # 사용처   : 컨테이너 자료형의 순회 
    #          (리스트, 딕셔너리, 문자열, range ...)
    # 안정성 : 높음

for i in range(5):
    print(i)
    
print('== while문 ==')
    # 사용 기준 : 종료 조건 중요
    # 사용처 : 상태 변화 추적
    # 안정성 : 낮음 (주의!) -> 무한루프 가능성 존재

number = 1
while number < 5:
    print(number)
    number += 1 # 조건에 대한 증감식

print('===== 컨테이너 자료형 비교 =====')

# 리스트 []
    # 핵심목적 : 여러 값을 순서대로 관리
    # 순서 : O
    # 수정 : O
    # 중복 : O
    # 접근 방식 : 인덱스 (위치기반)

numbers = [1,2,3,4,5,6,6,6,6,6,6]
print(numbers)
print(numbers[0])
numbers[0] = 10
print(numbers)

# 튜플 ()
    # 핵심목적 : 변하지 않는 묶음
    # 순서 : O
    # 수정 : X
    # 중복 : O
    # 접근 방식 : 인덱스 (위치 기반)

numbers = (1,2,3,3)
print(numbers)

print(numbers[0])
# numbers[0] = 10 # TypeError

# 집합 {}
    # 핵심목적 : 중복 제거, 집합 연산
    # 순서 : X
    # 수정 : O
    # 중복 : X
    # 접근 방식 : 포함 여부 확인 가능 (멤버십 연산자)
    
numbers = {1,2,3,4,5}
print(numbers)

# numbers[0] # TypeError: 'set' object is not subscriptable

print(1 in numbers)
numbers.add(10000)
numbers.add(300)
numbers.add(6)
print(numbers)

# 딕셔너리 {}
    # 핵심목적 : key-value 매핑하여 사용
    # 순서 : X (단, 파이썬 3.7 이상인 경우 입력 순서 유지 경향)
    # 수정 : O
    # 중복 : X (key가 중복되지 않는다.)
    # 접근방식 : key

user = {'name':'jun','age':30,'is_male':True}

user['city'] = 'seoul'
user['city'] = 'busan' # 중복 불가능, 재할당
user['license'] = True
print(user)

for k in user.keys():
    print(user[k])
    
# print(user[0])  # KeyError: 0
# 순서가 유지되는 경향이 있다고 하여, 
# 인덱스로 접근 가능한 것은 아님

# 리스트 [] vs. 튜플 ()
# 리스트 : 실수로 수정 가능
point = [10,20,30]
point[0] = 99 # 가능
print(point)

# 튜플 : 실수 방지 -> 이건 바뀌면 안된다는 신호
# point = (10,20,30)
# point[0] = 99 # 불가능

# 리스트 [] vs. 집합 {}
# 의문점 : 리스트를 그냥 사용하고, 중복만 없으면 되는거 아닌가요?

# 리스트는 "데이터 보관"을 목적으로 한다.
names = ['A','B','C','D','A','C']
print(names)
print(len(names))

# 집합은 조건 판단 도구로 활용
names_set = set(names)
print(names_set)
print(len(names_set))
# => DAU 등

# 리스트 [] vs. 딕셔너리 {key:value}
# 리스트 : 순서를 알아야 의미가 있음
user = ['jun',25,'개발자',True]
print(user)

# 딕셔너리 : 의미가 코드에 그대로 드러남
user = {'name':'jun',
        'age':25,
        'occupation':'개발자',
        'live_seoul':True}
print(user)

# 반복문 + 컨테이너
# 리스트 반복
numbers = [1,2,3,4,5]

for variable in numbers:
    print(variable)

# 딕셔너리 반복
user = {'name':'jun',
        'age':25,
        'occupation':'개발자',
        'live_seoul':True}

for variable in user: # key만 할당
    print(variable)

for k, v in user.items(): # 한쌍을 그대로 쓰기
    print(k, v)
    

tags = {'python','data','bi','sql'}
print(tags)
tags.add('python')
print(tags)

for tag in tags:
    print(tag) # 순서가 없기 때문에 무작위로 불러와 짐

# => 같은 for문인데, 자료형에 따라 꺼내지는 단위가 달라진다!