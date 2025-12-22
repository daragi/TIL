# range
# range(start, end, step)

# 특징 1: 순서가 존재 - 인덱싱/슬라이싱 가능
print(range(1, 10, 2))
print(type(range(1,11)))

numbers = range(1,11)
print(numbers[1])
print(numbers[1:4]) # 눈으로 보이지 않기에 확인이 불편함

# range는 보통 list로 형변환하여 확인
print(list(numbers))

# 주요 사용법
for i in range(1,11,2):
    print(i)
    
# !반복문!
# 1. 반복 횟수가 정해져 있는 경우 => for
# for 변수 in 컨테이너:    => 컨테이너에 bool은 해당 안됨 => 문자열, list, range, tuple .....순회 가능한 것들

# 1) 리스트 순회
names = ['jun','kyle','alex','ken']
for name in names:
    print(f'안녕하세요! {name}님')
    
# 2) 문자열 순회
subject ='python'
for char in subject:
    print(char)
    
# 3) 조건문 활용
numbers = list(range(1,11))
print(numbers)
for number in numbers:
    if number % 2 == 0:
        print(number)

# 반복횟수는?
print(len(names))

# !현재 반복은 마지막으로 종료된 시점에서 유지된다.!
print(number)

# 인덱스 순회
subjects = ['python', 'sql', 'BI', 'product_da', 'ML']
for subject in subjects:
    print(subject)

for i in range(len(subjects)):
    print(subjects[i])
    
# for 문 간단실습
# 1~10 더한 값 55 출력하기

total = 0
for i in range(1,11):
    total += i

print(total)

# 2. 반복 횟수가 정해지지 않은 경우 => while
# while True = 무한 반복

# while True:
#     print('영원히 반복.......!')

# while문에서 중요한 지점! 조건을 변화시킬 수 있는 무언가가 중요하다.
numbers = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(numbers):
    print(numbers[i])
    # 무한 루프, 조건을 변화시킬 수 있는 식이 꼭 필요하다.
    i += 1
print(i)

i = 0
# while i < len(numbers):
#     if i % 2 == 1: # 홀수 인덱스 케이스만 출력
#         print(numbers[i])
#         i += 1
# if 문을 만족한 경우에만 조건이 바뀌지 않도록 주의

# while 연습
# 1~ 10 더한 값
total = 0
while True:
    i += 1
    total += i
    if i == 10:
        break
print(total)