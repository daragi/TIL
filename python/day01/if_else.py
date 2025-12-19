# 조건문

# 1) 비교연산을 조건으로 사용하기
if 2 > 5: # if True 혹은 False로 해석될 수 있는 조건이 와야 함
    print('조건이 참입니다.')
    print('같은 들여쓰기 수준이라면,')
    print('동일한 코드블럭입니다.')

print('여기는? 조건문과 상관없이 무조건 실행됩니다.')

# 2) 비교연산 + 산술연산 조합
number = 6
if number % 2 == 1: # 2로 나눈 나머지가 1 (홀수)
    print(f'{number}는 홀수입니다.')
    
# 3) 논리 연산 결과
name = ""
if not name:
    print('이름이 비었습니다.')
    

# A라면 B하고, A가 아니라면 C 하겠다.
print('=== if - else 조건문 ===')
number = 6
if number % 2 == 1: # 2로 나눈 나머지가 1 (홀수)
    print(f'{number}는 홀수입니다.')
else:
    print(f'{number}는 짝수입니다.')
    

print('=== if - elif - else 조건문 ===')
# 다중 조건문
# if 조건1: 
    # 조건1이 만족할 때, 실행되는 코드
# elif 조건2:
    # 조건2가 만족할 때, 실행되는 코드
# else:
    # 그외 모든 경우

temperature = int(input('오늘의 날씨 : '))

if temperature >= 30: 
    print('아이스티')
elif temperature >= 10:
    print('아이스 아메리카노')
else:
    print('따뜻한 아메리카노')
    

age = int(input("나이를 입력하세요: "))
if age>=20:
    print('어른')
elif age>=10:
    print('청소년기')
elif age>=5:
    print('어린이')
else:
    print('영유아기')