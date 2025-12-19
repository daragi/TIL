print('======= 입력 =======')
# 사용자 입력

# 내장함수 input을 통해 사용자에게 입력받습니다.
name = input('이름을 입력해 주세요 : ')
print(name)
print(type(name)) # <class 'str'>

age = int(input('나이를 입력해 주세요 : '))
print(age)
print(type(age))  # <class 'int'>

print(f"약 10일 후면, {name}의 나이는 {age+1}살이 됩니다.")

print("===== 출력 =====")
# 터미널 상에서 보여주기 위함입니다.
# print 내장함수를 사용합니다.

word1 = 'Hello'
word2 = 'Python'
word3 = 'yeah!'

# 컴마를 기준으로 여러 변수 출력 가능
# 공백(default가 공백)을 기준으로 연결되어 한 줄 출력
print(word1, word2, word3)
print(word1, word2, word3, sep='~') # 구분문자 sep, 입력안할시 공백으로 구분

# 출력 시, 개행하여 출력
print()
print(word1, word2, end="!") # 문장 끝 개행의 여부 조절
print(word3)

# 정리
# 입력 = input() -> 터미널에서 받는다.
# 출력 = print() -> 터미널에서 출력된다.