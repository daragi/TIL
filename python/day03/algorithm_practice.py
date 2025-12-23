# 떡잎마을 반장선거
# 후보가 없는 반장선거
# 표가 발생하면, 자동 입후보 되는 구조

# 누가 반장이 될까요?
print('---1번 문제---')
votes = ['짱구','짱구','수지','짱구','훈이','맹구','짱구',
        '수지','수지','수지','짱구','유리','철수']

vote_dict = {}

# dict 형태로 변환
for vote in votes:
    if vote not in vote_dict:
        vote_dict[vote] = 1
    else:
        vote_dict[vote] += 1
print(vote_dict)

# 최다 득표의 value 구하기


# 동점이 있을 경우에

max_votes = 0
max_name = []
for k,v in vote_dict.items():
    if v >= max_votes:
        max_counts = v
        max_name.append(k)

# 동점이 없을 경우에

max_votes = 0
max_name = ''
for k, v in vote_dict.items():
    if v > max_votes:
        max_votes = v
        max_name = k
print(f'반장은 {max_votes}표 득표한 {max_name}이 되었습니다.')
       
# max, min 구하기
print('---2번 문제---') 
nums = [7,1,2,4,6,8,3]
max_num = 0

for num in nums:
    if max_num < num:
        max_num = num
print(f'최대값은 {max_num}')

min_num = 10
for num in nums:
    if min_num > num:
        min_num = num
print(f'최소값은 {min_num}')

# python_len 내장 함수 만들기
def len_func(container):
    count = 0
    for _ in container: # _는 변수이다. 반복은 하겠지만 추출한 값을 쓰진 않겠다는 의미
        count += 1
    return count