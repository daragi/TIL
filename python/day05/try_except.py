# 예외 처리

# try:
    # 일단 해 봐
# except:
    # ~를 제외하고

# 정상 : 숫자 입력 시
# 비정상 : 숫자 입력하지 않았을때, 에러가 발생하면 무조건 프로그램 종료

# n = input('숫자를 입력해 주세요: ') # str
# n = int(n) # str -> int
# answer = 10 / n 

# print(answer)

# n = input('숫자를 입력해 주세요.')

# # 예외처리를 통해, 프로그램이 정상종료되도록 처리할 수 있다.
# try:
#     n = int(n)
#     answer = 10 / n
#     print(answer)
# except Exception as e:
#     print(f'에러발생 : {e}')
#     # try 문에는 except 또는 finally 절이 하나 이상 있어야 합니다


numbers = [10,20,30,40,50]
# print(numbers[10])

try:
    print(numbers[10]) # 에러 발생
except Exception:
    pass

print('프로그램이 종료되지 않고 끝났습니다.')