# 복습
# 다양한 자료를 이용하여, 정보를 구조화하는 방식이 알고리즘에서 중요하다.

print('===== API 구조 실습 =====')
# 복습 실습
# users -> dict
# users['total_user'] -> int
# users['information'] -> list
    # list의 값 -> dict
users = {
        'total_user': 3,
        'information': [
            {'name': 'alex', 'age':3, 'license':True},
            {'name': 'june', 'age':7, 'license':False},
            {'name': 'peter', 'age':4, 'license':False}
        ]
        }

# 구조 확인
print(type(users))
print(users.keys()) # 키-값의 한쌍 구조로 만들어진, 순서가 없는 컨테이너 자료형

print(users['total_user']) # int
print(users['information']) # list -> 순서가 존재하는 컨테이너 자료형

# 사람들의 정보만 뽑아보기
infos = users['information'] # 리스트만 뽑아서 할당
print(infos[0]) # 순서가 존재하기 때문에 숫자(위치)로 값 접근

# Q1. 라이센스가 있는 인원들의 숫자 구하기
# => 라이센스 == True 인 사람의 수 (세기)
cnt = 0 # 초기값

print('= Q1 =')
# for info in users['information']: # 동일
for info in infos:
    # print(type(info))
    if info['license'] == True:
        cnt += 1

print(f'라이센스가 있는 인원 : {cnt} 명') # f-string

# Q2. 모든 사람의 나이 평균 구하기
print('= Q2 =')

# 방법 1 : 숫자형 변수와 복합 연산 활용
age_sum = 0

for info in infos:
    age_sum += info['age'] # 복합연산

ave_age = age_sum / users['total_user']
print(f'나이의 평균은 {ave_age} 살입니다.')

# 내장함수로 반올림 가능
print(f'나이의 평균은 {round(ave_age, 2)} 살입니다.')

# 방법 2 : 리스트와 내장함수 사용
# 평균 = 합산 / 갯수 -> ave = sum() / len()
age_lst = [] # 빈 "리스트" 생성 -> 순서 O, 변경 O, 중복 O

for info in infos:
    age_lst.append(info['age'])

print(age_lst)
print(sum(age_lst)/len(age_lst))

# 방법 3 : 리스트 컴프리헨션 (심화)
age_lst_comp = [info['age'] for info in infos]
print(sum(age_lst_comp)/len(age_lst_comp))

# Q3. 라이센스가 없는 "사람들의 이름 모으기"
# 리스트 -> 컨테이너 자료형 선택
name_lst = [] # 빈 리스트 생성

for info in infos:
    if info['license'] == False:
        name_lst.append(info['name'])
        
print(name_lst)

# 왜 이렇게까지 복잡하게 "구조화"해야 하는가?
# 구조화 된 형태의 장점

print(users)

# 추가 유저가 생길 때, 관리가 용이
# 전체 수 업데이트
print(users['total_user'])
users['total_user'] += 1
print(users['total_user'])

# 유저 정보 업데이트
users['information'].append({'name':'ken','age':10,'license':True}) # 추가
print(users)

print('===== 함수 (function) =====')

students = ['하늘','수빈','동연','강현','선준','예솔']

# 1. 사용자 정의 함수
# 1단계 : 정의 (define)

# 학생 목록과 이름이 들어가면, 출석 여부를 반환하는 함수
def check(students_list, name): # 매개변수
    
    if name in students_list: # 멤버십 연산으로 포함 여부 확인
        return f'{name}님은 출석하셨습니다.'
    else:
        return f'{name}님은 출석하지 않으셨습니다.'
    
# 2단계 : 호출하기 (call)
print(check(students,'수빈')) # 인자 = students, '채원'/'수빈'

# 만약 고정된 학생 목록이 존재한다면, 굳이 매개변수로 빼지 않아도 됨
def check(name): # 매개변수
    students_list = ['하늘','수빈','동연','강현','선준','예솔','하비','동호','채원',
                    '효진','세연']
    if name in students_list: # 멤버십 연산으로 포함 여부 확인
        return f'{name}님은 우리반 학생입니다.'
    else:
        return f'{name}님은 우리반 학생이 아닙니다.'
    
# print(check(['지원','하은','근표'],'하은')) # 설계한대로 사용하지 않으면, 에러 발생

# 2. 내장함수
print(students) # 터미널 상에 출력
print(len(students)) # 컨테이너 자료형 값의 갯수를 반환 -> 길이

# print(sum(students)) # 에러 발생
# 모든 함수가 모든 자료형에 사용 가능한 것은 아니다.

# 내장함수 sorted()
# -> 컨테이너 자료형에만 적용됨
print(sorted(students)) # (기본) 오름차순 정렬
print(sorted(students, reverse=True)) # 내림차순 정렬

# print(sorted([1,2,3,-100,'hello']))
# TypeError: '<' not supported between instances of 'str' and 'int'
# 설계된 대로 사용해야 작동한다.

# 익명함수 lambda
# 사용자 정의 함수 중, 이름을 붙일 필요가 없다고 판단
# -> 일회성으로 사용

a =  (lambda x:-x)(-1)
print(a)

# 흔한 사용 방식
example = [(0,2),(2,3),(1,4),(0,-1),(100,-5)]

print(type(example)) # <class 'list'>
print(type(example[0])) # <class 'tuple'>
# 리스트 안에 튜플이 존재!

print(len(example))

# 정렬하려고 합니다!
example_a = sorted(example)

print(example)

# 정렬 -> 기준이 필요
# 2번째 값 기준, 내림차순 정렬
example_b = sorted(example, key=lambda x:-x[1])

# example 
# [(0, 2), (2, 3), (1, 4), (0, -1), (100, -5)]

# 첫 번째 (0, 2) -> -2 (이걸 기준으로 삼겠다!)
# 두 번째 (2, 3) -> -3
# 세 번째 (1, 4) -> -4
# 네 번째 (0, -1) -> 1
# 다섯 번째 (100, -5) -> 5
# => 람다함수를 거쳐서 나온 값을 기준으로 "오름차순"

print(example_b)
# [(1, 4), (2, 3), (0, 2), (0, -1), (100, -5)]


# 메서드
# 메서드는 함수에 포함된다.
# 함수 != 메서드
# => "특정 자료형"에 딸린 함수

# 자료형마다 특징이 다 달라서!

# 리스트 메서드
# 순서 O, 변경 O, 중복 O
numbers = [10,20,30,40,50]

# 추가 : 순서가 있게 추가 (맨 끝에)
numbers.append(60)
print(numbers) 
# 나 자신을 바꿀 수가 있기 때문에 (변경 O)
# 새로 반환되는 리스트가 아닌 기존 numbers 에 추가

# 삭제 : 위치(순서 O)를 기준으로 삭제
numbers.pop(1)
print(numbers)

# 추가 : 위치를 기준으로 추가
numbers.insert(1, 200)
print(numbers)

# 추가 여러개
# numbers.append(1,2,3,4)
# numbers.append([1,2,3,4])
numbers.extend([1,2,3,4])

print(numbers)


# 문자열
# 순서 O, 변경 X, 중복 O

word = 'helllllllo'
print(word[0])

# 순서 O
print(word.index('o'))

# 중복 O
print(word.count('l'))

# 변경 X
word_lst = word.split('e')

print(word)
print(word_lst)

new_word = word.replace('l','x')
print(new_word)

word_join = '~'.join(word_lst)
print(word_join)

# 딕셔너리
# 순서 X (키-값), 변경 O, 중복 X (키의 중복이 안됨)

students = {'kyle':10,'jun':23,'alex':30}
print(students['kyle'])
# print(students['ken']) # KeyError: 'ken'

# 순서 X
# 값 조회
print(students.get('kyle'))
print(students.get('ken')) # 조회하고자 하는 값이 없더라도 작동됨

# 변경 O
students.update({'ken':40})
print(students)

# 집합
# 수학 집합 연산을 그대로 따름
# 순서 X, 변경 O, 중복X

numbers = {1,2,3,4,5}
numbers_2 = {3,4,5,6,7}

numbers.add(10000)
numbers.add(10000)
numbers.add(10000)
numbers.add(10000)
print(numbers)

# 집합연산 메서드
print(numbers.intersection(numbers_2))
print(numbers.union(numbers_2))
print(numbers.difference(numbers_2))