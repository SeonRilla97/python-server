# 용사 캐릭터 
hero_name="용사"
hero_hp=100
hero_power=10


# 슬라임 캐릭터 
monster_name="슬라임"
monster_hp=30
monster_power=5

# 공격 함수
def attack(attacker, attacker_power, target, target_hp):
    print(f"{attacker}이 {target}을(를) 공격했다! (데미지 {attacker_power})")
    target_hp -= attacker_power
    print(f"{target}의 체력이 {target_hp}이 남았다.")
    return target_hp

print("==== Step 1. 전역 변수 이용 실행 ====")
monster_hp = attack(hero_name, hero_power, monster_name, monster_hp)

print("\n==== Step 2. 마이너스 공격력으로 공격 ====")
monster_hp = attack(hero_name, -50, monster_name, monster_hp)


'''
몬스터 100마리면 변수 100개 만들어야함
함수 호출 시 매개변수 순서가 바뀌면 잘못된 로직 실행

'''