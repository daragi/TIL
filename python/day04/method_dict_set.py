# 메서드
# 딕셔너리
    # 순서 없음
    # 수정 가능
    # 중복 불가 (key 값)

students = {'jun' : 40,
            'alex' : 20,
            'kyle' : 30,
            'ken' : 22}
print(students)

# 조회
print(students['jun'])

# 값 조회: get
# key를 기준으로 value를 가지고 옴
print(students.get('ken'))
print(students.get('chelsea')) # 없는 경우, 에러를 발생 시키지 않음

# 수정
students.update({'jun' : 300})
print(students)

# 삭제
students.pop('alex')
print(students)

# 집합
    # 순서 없음
    # 수정 가능
    # 중복 불가

num1 = {1,3,5,6,7}
num2 = {1,2,3,4,5}

# 연산
print(num1.intersection(num2))
print(num1.difference(num2))
print(num1.union(num2))

# 추가
num1.add(1999)
print(num1)
num1.add(1)
print(num1) # 집합은 중복을 허용하지 않기에 이미 존재하는 값은 추가 
# update 여러 값 추가
num1.update([10,20,30]) # 값이 add와 다르게 맨 뒤가 아닌 무작위로 들어감?
print(num1)

# 삭제
num1.remove(1999)
print(num1)

num1.add(1999)
print(num1)
num1.discard(1999)
print(num1)