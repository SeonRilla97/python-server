'''
패키지 <- 모듈 <- 함수 

[실습 목표]
1. import 구문으로 표준 라이브러리 가져오기 (상자째)
2. from ... import 구문으로 특정 함수만 꺼내오기 (도구만)
3. random, math, datetime 모듈의 핵심 기능 사용해보기
'''

# -------------------------------------------------
# 1. 상자째 가져오기 (import 모듈명)
# -------------------------------------------------
import random 

print("--- 🎲 랜덤 모듈 (random) ---")

# random 상자 안에 있는 randint 도구를 꺼내 씁니다.
# 점(.)은 "~의" 라고 생각하면 됩니다. (random의 randint)
dice = random.randint(1, 6)
print(f"주사위 결과: {dice}")

# 리스트에서 하나를 무작위로 뽑기 (choice)
menus = ["김치찌개", "돈까스", "짜장면", "초밥"]
lunch = random.choice(menus)
print(f"오늘 점심 추천: {lunch}")

print("-" * 30)

# -------------------------------------------------
# 2. 도구만 꺼내오기 (from 모듈명 import 함수명)
# -------------------------------------------------
# math 상자에서 pi와 sqrt(제곱근)만 꺼내옵니다.
from math import pi, sqrt

print("--- 🧮 수학 모듈 (math) ---")

# math.pi 라고 안 해도 됩니다. 그냥 pi라고 부르세요.
print(f"원주율(pi): {pi}")
print(f"25의 제곱근(sqrt): {sqrt(25)}") # 5.0

print("-" * 30)

# -------------------------------------------------
# 3. 날짜와 시간 (datetime)
# -------------------------------------------------
import datetime

print("--- 📅 날짜/시간 모듈 (datetime) ---")

# 현재 시각 가져오기
now = datetime.datetime.now()
print(f"지금 시각: {now}")

# 보기 좋게 포맷팅 (년-월-일)
print(f"오늘은: {now.year}년 {now.month}월 {now.day}일")