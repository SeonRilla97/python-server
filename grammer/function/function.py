# 함수 정의
count = 0 

def increase_count():
    global count
    count += 1
    print(f'현재 햄버거 개수: {count}개')

# 인자, 반환 값 추가
def make_burger(name):
    print(f'{name} 햄버거 만들기')
    print('1. 빵 굽기')
    print('2. 패티 굽기')

    print('완성!')
    return name

# 함수 호출
make_burger("치즈버거")
increase_count()