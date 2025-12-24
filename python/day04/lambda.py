# 익명함수
# lambda input 요소: output 요소
# 익명함수를 이용한 방식
result = (lambda x, y: x + y)(1, 4)
print(result)

numbers = [1,5,3,7,10,4]
print(sorted(numbers, key=lambda x: -x))

# 리스트 형태
example = [(0,2),(3,5),(1,4),(0,-1)]
back = sorted(example, key = lambda element: element[1]) # 뒤에 요소를 기준으로 정렬
front = sorted(example, key = lambda element: element[0]) # 앞에 요소를 기준으로 정렬

print(back)
print(front)

# 문제 1. 수 정렬
# 주어진 2차원 리스트를 기준에 따라서 정렬하시오.
# (1) [앞쪽, 뒤쪽] 이라고 할 때, 뒤 쪽이 '작은' 순서로 정렬하되 
# (2) 만약 같다면 앞쪽이 '큰' 순서대로 정렬하시오.
nums = [[70, 30], 
        [70, 10], 
        [20, 30], 
        [50, 90], 
        [40, 80], 
        [80, 90], 
        [10, 60]]

back = sorted(nums, key=lambda x: (x[1], -x[0]))
print(back)