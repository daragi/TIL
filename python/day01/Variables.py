# 변수

# 변수란 상자다!
# 할당연산자 (=) 를 통해 값을 변수에 할당
# 변수이름 = 변수에 저장되는 값 -> 항상 고정!!

name = '배지원'   # 문자열 str
age = 20        # 정수 int
is_male = False # 불린형 bool

print('이름은?')
print(name)

print('나이는?')
print(age)

print('남자인가요?')
print(is_male)

# 변수의 장점
# 1. 데이터에 의미를 부여한다.
# 20 -> 의미?? 나이, 갯수, 돈 ...

age = 20
print(age) # 해석이 명확해 진다.

# 2. 재사용성과 가독성
print(name, age, is_male)

print('=========')

# 식별자 (indentiiers) = 리터럴 (literal)
# 변수 이름이 식별자
# 변수에 들어가는 값이 리터럴이다.

# 식별자 작성 규칙
# 1name = 'alex' # 에러
name1 = 'alex'
print(name1)

# 중요! 예약어, 내장함수로 지으면 안됩니다!
# True = '참' -> 아예 할 수 없다.
print(type(name)) # 자료형 확인하는 본연의 역할을 덮어 씌워 버리기 때문에
# type = '자료형' # 할 수는 있지만, 하지 마세요
# print(type)
# print(type(type))

# 재할당
print(name)

# 할당 연산자를 통해, 기존에 존재하는 변수 이름에 다시 할당하면
# 기존 변수를 아예 덮어 써버리게 됩니다.
name = '박하은'
print(name)
print(name)
print(name)

# 객체의 주소
print('===================')
name = '배지원'
print(name)
print(id(name))

name = '박하은'
print(name)
print(id(name))


a = [1,2,3]
b = a
print(a,b)
print(id(a), id(b))

b.append(4)
print(a)

print(f"a의 주소는 {id(a)}, b의 주소는 {id(b)}")