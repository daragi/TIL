# 컨테이너 자료형

# 문자열(String)
# 0 개 이상의 문자를 순서가 있게 저장하는 컨테이너 자료형

# 특징 1: 순서가 존재한다.
# 순서가 존재하기에 인덱스로 값에 접근하는 것이 가능함.
subject = 'python'
word = 'hello'
print(subject[0])

# 덧셈 연산
print(subject + word) 
# 문자열끼리 바로 이어 붙인다. => concat

# 곱셈 연산
print(subject * 3)

# 특징 2 : 불변 자료형
# 변경하는 것처럼 보이는 케이스
print(subject[1:])
subject = 'P' + subject[1:]
print(subject) # => 변경한 것 처럼 보이지만 변수가 재할당 되면서 기존의 subject 변수가 변경됨

# 컨테이너 자료형과 기초 자료형과의 차이
print(len(subject))
print(len([1,2,3,4,5]))
print(len('True'))
# print(len(3.14)) float는 len이 불가
