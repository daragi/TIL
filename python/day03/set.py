# 집합(set)
# 순서가 존재x, 가변 자료형

numbers = {1,2,3,4,5}
print(type(numbers))

# 추가
numbers.add(6)
print(numbers)
numbers.add('10')
print(numbers)
# numbers.add(['hello!']) => 해싱이 가능해야 들어갈 수 있음

# 삭제
numbers.remove('10')
# numbers.remove('10') => remove는 2번 삭제 불가
print(numbers)
numbers.discard('10') # 존재하지 않는 것을 삭제 해도 오류 x
print(numbers)

# !수학적 집합의 특성을 그대로 따름 - 연산이 가능(교,차,합 집합 등)
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

# 1) 합집합
print(set1|set2) # 중복은 제거
# print(set1 + set2) 더하기는 불가
print(set1.union(set2))

# 2) 교집합
print(set1 & set2)
print(set1.intersection(set2))

# 3) 차집합
print(set1 - set2)
print(set1.difference(set2))