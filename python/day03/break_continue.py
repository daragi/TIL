# 반복문 제어

# break
print('===break===')

# numbers = [1,2,3,4,5]
numbers = list(range(1,6))
print(numbers)
# print(len(numbers))

for num in numbers:
    print(num) # 전체를 반복
    
    if num == 3:
        print('3을 만났습니다!')
        print('반복을 종료합니다')
        break

i = 0
while True:
    print(numbers[i])
    i += 1
    if numbers[i] == 3:
        print('3')
        print('3을 만났습니다!')
        break
    
print('===else===')

target = int(input('숫자를 입력해주세요 : '))
for num in numbers:
    print(num)
    if num == target:
        print('3을 찾았습니다.')
else:
    print(f'{target}을 찾지 못했습니다.')
    
# 반복이 break로 제어되지 않으면, 조건문을 통해 해당하는 반복을 건너뛰고 다음 반복 실행    
print('===continue===')

number = 0
while number <10:
    number += 1
    
    if number % 2 == 0: # 짝수라면
        print('넘어가')
        continue
    
    print(number)

# 증감식의 위치 및 조건문을 항상 신경 쓸것

print('===pass===')

def solution(number):
    pass # pass 생략 시 오류 발생

for num in numbers:
    if num == 3:
        pass
else:
    print('3이 아닙니다.')