# 모듈 
# 함수의 정의와 호출을 분리하기 위한 목적

# 기본 사용법
# import 모듈 -> 모듈을 불러와서 사용할 수 있다.
# import module_A

# print(module_A.add(1,2)) # 호출 (call)
# print(module_A.subtract(1,10000)) # 호출 

# # 일부만 불러오고 싶을 때는?
# from module_A import subtract
# # from module_A import * # 함수를 다 불러올 수도 있음

# print(subtract(1, 10000))

# # 함수 이름이 너무 길 때?
# from module_A import subtract as sb

# print(sb(1, 10000))


# 파이썬 내장 모듈

import random

# 무작위 정수 값 1개 추출
number = random.randint(1, 5) # 1,2,3,4,5 중 무작위 1개 반환
print(number)

# 주어진 리스트 내 무작위 1개 추출
numbers = ['십','이십',30.0,40,[]]

print(random.choice(numbers)) # 1개 추출
print(random.sample(numbers, 3)) # k개 추출

random.shuffle(numbers) # 전체를 섞기
print(numbers)


import time

# time.time()
print(time.time()) # 초 단위 시간 확인
start = time.time()
result = 0

for number in range(0, 10^6):
    result += number
end = time.time()
print(end - start)

# time.sleep()
time.sleep(3) # 일정 시간동안 프로그램의 동작 정지
print('3초가 지났습니다.')

for i in range(5):
    time.sleep(1)
    print(f'1초 기다린 후, {i} 출력')
    
# 로또 번호 추첨기 만들기 - random/time module practice
import random
import time

for i in range(5):
    time.sleep(1)
    print(f'{5 - i}초 남았습니다.')
numbers = list(range(1,46))
lotto_number = random.sample(numbers, 6)
print(lotto_number)