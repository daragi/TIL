# 문자열
    # 순서 있음
    # 변경 불가
    # 중복 가능
word = 'Merry Christmas!!'

# 문자열 분할 : split()
word_list = word.split(' ') # 자기 자신을 바꾸지 않고, 리스트 반환
print(word_list)

# students = input('학생의 이름 명단을 입력해 주세요.')
# stu_lst = students.split(',')
# print(stu_lst)

# 문자열 합치기 : join()
string_list = ['merry', 'christmas', '!!', 'happy', 'holiday', '!!']
print(len(string_list))
string_join = '^'.join(string_list)
print(string_join)