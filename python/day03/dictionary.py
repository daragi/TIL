# 기초 자료 구조와 로직 설계
# 순서가 있는 자료 구조
# 순서(위치)로 값을 관리

user = ['alex', 3, True]

# 딕셔너리
# '순서'가 없는 컨테이너 - index로 접근 불가
# key - value 한 쌍의 구조
user = {
    'name':'alex',
    'age' : 30,
    'license' : True,
    'city' : 'seoul'}

# key 값은 unhashable 이어야 함 => 불변  <> key는 유일해야 함. 중복 불가
# value 값은 상관 없음
print(user)
print(type(user))
print(user['age'])
print(len(user))
# print(user[0]) => 위치로 불러올 수 없음 KeyError: 0

# 가변 자료형
# 1) 수정
user['age'] = 32
print(user)

# 2) 추가
user['nationality'] = 'korea'
print(user)

# 3) 삭제
user.pop('city')
print(user)

# 딕셔너리 메서드
print(user.keys())
print(type (user.keys()))
print(user.values())
print(list(user.values()))

# key-value를 무시하고, 튜플로 반환
print(user.items())

# 딕셔너리에 조건 검사
for k in user.keys():
    if k == 'nationality' or k =='city':
        print(f'{user[k]} 출신')

# 딕셔너리 풀어 헤치기
for k, v in user.items():
    print(k)
    print(v)
for k, v in user.items():
    print(f'{k}는 {v}입니다.')