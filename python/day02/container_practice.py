# 문자열 포맷과 시간 변화

minutes = int(input('시간을 입력해 주세요: '))

time = minutes // 60
minute = minutes % 60

if time == 0 and minute ==0:
    False
else:
    print(f'{time}시간{minute}분')