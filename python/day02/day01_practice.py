# practice_operator
money = int(input('고객이 가진 돈은 얼마입니까?'))

ice = 2000

count = money // ice
change = money % ice

print(count)
print(change)

# practice_ if

age = int(input('나이를 입력해 주세요 : '))
card_type = input('결제 수단을 입력해 주세요 : ')

if card_type == '정기권':
    print('0원')
else:
    if age <7 or age>= 65:
        print('무료')
    elif 7<= age <= 19:
        print('청소년 요금')
    else:
        print('성인 요금')