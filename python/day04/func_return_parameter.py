# 반환값과 매개변수 유무

# 반환값 x, 매개변수 o
def hello(name):
    print('함수 안에서 출력')
    print(f'안녕하세요! {name}님')

print('함수 밖에서 출력')
print(hello('김하비')) 
# print와 함수를 같이 쓰면 None이 출력 why?
# 함수 밖에서는 hello라는 함수가 없기에 함수 호출을 못함 = None

# 반환값 x, 매개변수 x

## 문제 1. 별 찍기
star = int(input('별 개수를 입력하세요.'))

def print_starts():
    for i in range(1, star + 1):
        print('*' * i, end = '\n')
    
print_starts()

# 반환값 o, 매개변수 o
## 문제 2. 최고 최저 매출 파악하기

# new_sales = list(input('새로운 매출 리스트를 넣어주세요.'))
new_sales = [400, 1000, 10, 100, 554, 340, 300, 2040, 1060]

def sales_min_value_max_value(new_sales):
    max_value = 0
    min_value = 10000
    
    for high in new_sales:
        if high > max_value:
            max_value = high
    print(f'최고매출은 {new_sales.index(max_value)}일차이고 해당 금액은 {max_value} 입니다.')
            
    for low in new_sales:     
        if low < min_value:
            min_value = low
    print(f'최저매출은 {new_sales.index(min_value)}일차이고 해당 금액은 {min_value} 입니다.')
    
sales_min_value_max_value(new_sales)