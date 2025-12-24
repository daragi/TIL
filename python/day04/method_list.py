# 메서드 (Method)

# 특정 자료형에 딸려 있는 함수
# 리스트
    # 순서 있음
    # 변경 가능
    # 중복 가능

numbers = [10,20,30,40,50]

# 추가
# append
numbers.append(60) # 원형의 자료를 변경, 반환값이 없음
numbers.append([70,80,90]) # 원형의 자료를 변경, 반환값이 없음
print(numbers)

# extend
numbers.extend([70,80,90])
# numbers.extend(70,80,90) 하나의 인자만 와야함 지금 3개 왔음
print(numbers)

# insert
numbers.insert(0, 0)
print(numbers)

# 삭제

# pop : 위치를 기준으로 삭제
del_val = numbers.pop(1)
print(del_val) # 삭제된 것을 반환
print(numbers)

# remove : 값을 기준으로 삭제
numbers.remove(80)
print(numbers)

# 정렬

# sort
# sorted : 전달받은 컨테이너를 정렬하여, '새로운 리스트를' 반환
# sort : 기존의 리스트 자체를 변경

# numbers.sort(key=lambda x:-x)
# numbers.sort(key=lambda x:(x%3, -x))

# reverse : 리스트를 뒤집는다.
a = numbers.reverse()
print(a)
print(numbers)

# etc

# count : 값의 개수 세기
cnt1 = numbers.count([70])
cnt2 = numbers.count(70)
print(cnt1)
print(cnt2)
