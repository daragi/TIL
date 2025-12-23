# 함수 기초
print('== 함수 사용 전 ==')

number1 = 5
number2 = 10

if number1 > number2:
    answer = number1
else:
    answer = number2
print(answer)

### 숫자가 바뀔 때마다 변수를 재할당 해야함
number3 =7
number4 = 10
# 함수 정의 (define)
print('=== 함수 사용 후 ===')
def get_bigger(num1, num2):
    if num1 > num2:
        answer = num1
    else:
        answer = num2
    return answer

# 박스만 만들었기에 아무일도 일어나지 않음.
# 함수 호출 (call)
print(get_bigger(number1, number2))
print(get_bigger(number3, number4))
