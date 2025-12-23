# 멤버십 연산자
# in / not in

# 특정 값이 '컨테이너 자료형'에 포함이 되어 있는지 검사
numbers = [1,2,3,4,5]
print(3 in numbers)
print(3 not in numbers)

# 질문
# print(3 in 3) TypeError: argument of type 'int' is not iterable (int는 순회 불가)

for num in numbers:
    print(num)
    if num == 3:
        print('3을 찾았습니다.')
        break

colors = {'Red' : '빨강',
          'Blue' : '파랑',
          'Yellow' : '노랑'}
print('빨강' in colors) # 값으로 접근하면 무조건 False
print('Red' in colors) # 키로 접근했을 때 해당하는게 있다면 True

print(colors.values())
print('빨강' in colors.values())