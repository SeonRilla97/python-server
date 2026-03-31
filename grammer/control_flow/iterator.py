'''
[중심 내용]
for 변수 in 컨테이너 : 순차적으로 하나씩 꺼내기
enumerate(컨테이너) : 인덱스 + 값
'''
# 리스트 순회
basket = ['사과','바나나','오렌지']
for fruit in basket:
    print(fruit)

# 문자열 순회
for char in "안녕하세요":
    print(char)

# enumerate 사용
for index, fruit in enumerate(basket):
    print(f'{index + 1}번째 과일: {fruit}')

# 점수 분석기
# 60점 이상 학생만 '합격' 출력하기
score = [80, 55, 92, 45, 70]
for s in score:
    if s >= 60:
        print(f'{s}점 합격')
    else:
        print(f'{s}점 불합격')