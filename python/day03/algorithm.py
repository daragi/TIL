# 다양한 설계 방식에 대해 알아보자
# 1등급 광물의 존재 여부
gems= [3,3,1,2,3,2,2,3,3,1]

# 방법 1
print(1 in gems)

# 방법 2
grade_1 = False
for gem in gems:
    if gem == 1:
       grade_1 = True
       break

print(grade_1)

# 등급별 광물의 갯수

# 방법 1
grade_list = [0] * 3 # 등급별 위치에 개수 기록
print(grade_list)

for gem in gems:
    grade_list[gem - 1] += 1
print(grade_list)

# 방법 2
grade_dict = {}

for gem in gems:
    if gem not in grade_dict:
        grade_dict[gem] = 1
    else:
        grade_dict[gem] += 1
print(grade_dict)