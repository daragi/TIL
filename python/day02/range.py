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

# 2. 반복 횟수가 정해지지 않은 경우 => while

