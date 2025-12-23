# (1) 데이터를 딕셔너리 형태로
student = {
    '국어' : 85,
    '영어' : 90,
    '수학' : 78
}

# (2) 파이썬 과목 100점 추가
student['파이썬'] = 100

# (3) 국어 점수는 85점입니다 형태로 출력
for k, v in student.items():
    print(f'{k} 점수는 {v}점입니다')
    
print('---------------------------------------')    
    
python_class ={'철수','영희','민수'}
data_class ={'영희','지현','민수'}


# (1) 두 강좌를 모두 수강하는 학생
print(python_class.intersection(data_class))
# (2) 파이썬 강좌만 수강하는 학생
print(python_class - data_class)
# (3) 두 강좌 중 하나라도 수강하는 학생
print(python_class|data_class)