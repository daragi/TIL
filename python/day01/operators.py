print('===== 연산자 =====')

# 연산 -> 처리를 하기 위한 목적
# 1. 산술 연산자
print('==산술연산자==')
a = 5
b = 2

# 사칙연산 (+,-,*,/)
print(a+b) # 7 -> int
print(a-b) # 3 -> int
print(a*b) # 10 -> int
print(a/b) # 2.5 -> float

# 몫, 나머지, 제곱 -> //, %, **
print(a//b)
print(a%b)
print(a**b)

# print(12/0) # 수학적으로 할 수 없는 연산은 파이썬도 할 수 없다. cant divide zero

# 2. 복합 연산자 - 축약형
# a = a+b => a+=b
# 산술연산자 & 할당연산자를 함께 쓰는 연산
# +=, **=, //=, %=
print('==복합연산자==')
print(a)
a += 1
print(a)

# 3. 비교 연산자

# 값과 값을 비교한다. -> True, False
# A와 B를 비교, 딱 두개만 비교
print('==비교연산자==')
print(a,b)

print(a>b)
print(a<b)
#==: 같다
#!=: 같지 않다.
print(a==b)
print(a!=b)

# 숫자 외 자료형의 경우
c = '123'
d = '456'

print(c<d)

# 같은 자료형이 아니면 비교 연산자 사용 불가, but 일치 비교는 가능

# 4. 논리연산자
print('==논리연산자==')
e = 0
print(a,b,c,d,e)

# False로 해석될 수 있는 변수 e 작성
print(bool(e)) #False

# A,B 둘다 True여야 True
# A or B : A, B 둘중 하나라도 True이면, True
# not A: A가 False이면, True

print(a > b) # True
print(c == d) # False

print(a>b and c==d) # True and False -> False
condition_1 = a > b
condition_2 = c == d
print(condition_1 and condition_2) # False
print(condition_1 or condition_2) # True

# 논리연산과 단축평가
print('==단축평가==')
print(True or False) #True
print(True or sdf)   #True
print(False and a)   #False

# 1. 산술 연산자 (+,-,*,/,//,%,**)
# 2. 복합 연산자 (+=, -=, *= ...)
# 3. 비교 연산자 (==, !=, <, >, >=)
# 4. 논리 연산자 (and, or, not)