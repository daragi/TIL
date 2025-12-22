# for 문 간단실습
# 1~10 더한 값 55 출력하기

total = 0
for i in range(1,11):
    total += i

print(total)

# while 연습
# 1~ 10 더한 값
i = 0
total = 0
while i < 10:
    i += 1
    total += i
print(total)

# while 문과 조건문을 사용, 짝수인 경우만 더한 값을 출력

i = 0
total = 0

while i < 11:
    i += 1
    if i%2 == 0:
        total += i
print(total)