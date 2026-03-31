
# 커피 자판기 

coffee_stock = 5
inputs =[300,200,300,400,500,600]
while True:
    # 현재 재고 확인
    print(f"커피 재고: {coffee_stock}")

    # 돈 입력
    money = inputs.pop(0)
    
    # 돈 부족
    if money < 300:
        print(f"돈이 부족합니다. {money}원을 반환합니다. ")
        continue
    
    # 정상 판매 (300원 이상)
    print(f"커피가 나왔습니다. 거스름돈: {money - 300}원")
    coffee_stock -= 1

    # 재고 소진
    if coffee_stock == 0:
        print("품절되었습니다.")
        break

print("-- 영업 종료--")