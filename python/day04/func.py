# 함수 (function)
# 코드 재사용을 위한 블랙박스적인 블럭이다.
# 입력하면, 처리하고, 반환합니다.

# 내장 함수
numbers = [1,2,3,4,5,6]
print(len(numbers)) # 컨테이너의 길이를 반환하는 내장함수
print(sum(numbers)) # 컨테이너의 합계를 반환하는 내장함수 
print(abs(-100)) # 주어진 수치형 값의 절댓값을 반환하는 내장함수

print('== 사용자 정의 함수 ==')
# 1단계 : 정의 (define)
# 함수를 만들었기 때문
def abs_num(n): 
    if n > 0:
        answer = n
    else:
        answer = -1 * n
    return answer

# 똑같은 함수이다!
def abs_num(n): 
    if n > 0:
        return n
    else:
        return -1 * n
# return 이라는 키워드 만나게 되면, 함수 종료


# 2단계 : 호출 (call)
i = -123 # -123은 인자
result = abs_num(i) # 함수 내에서 매개변수 (n = -123)으로 사용
print(result)

numbers = [1,2,3,4,5]
print(len(numbers))

word = 'Hello Python!'
print(len(word))

is_male = True
# print(len(is_male)) bool은 len으로 셀수 없음

# 사용자 정의함수 len_func 작성
numeric = [2,45,6,8,2543,8,32,6,2,6,8]

# 1단계 정의
def len_func(container):
    conut = 0
    for _ in container:
        count += 1
    
    return count

# 최대값
print(max(numeric))

# 최소값
print(min(numeric))
    