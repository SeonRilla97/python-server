
# 용사 캐릭터
hero = {
    "name": "용사",
    "hp": 100,
    "power": 10
}

# 슬라임 캐릭터
monster = {
    "name": "슬라임",
    "hp": 30,
    "power": 5
}

# 공격 함수
def attack_dict(attacker, target):
    print(f"{attacker['name']}이 {target['name']}을(를) 공격했다! (데미지 {attacker['power']})")
    target['hp'] -= attacker['power']
    print(f"{target['name']}의 체력이 {target['hp']}이 남았다.")
    return target['hp']

print("==== Step 1. 딕셔너리 이용 실행 ====")
monster["hp"] = attack_dict(hero, monster)

'''
기능과 데이터 분리
여전히 공격함수의 -공격 가능
'''