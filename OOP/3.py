class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, target):
        print(f"{self.name}이 {target.name}을(를) 공격했다! (데미지 {self.power})")
        target.take_damage(self.power) # 타 객체가 자신의 데이터를 수정하도록 위임

    def take_damage(self, damage):
        if damage < 0: # 데이터 보호 -유효성 검사 (캡슐화) 
            print("음수 공격력은 적용되지 않습니다.")
            return
        self.hp -= damage
        print(f"{self.name}이 {damage}의 데미지를 입었다. 체력이 {self.hp}이 남았다.")

# 용사 캐릭터
hero = Character("용사", 100, 10)

# 슬라임 캐릭터
monster = Character("슬라임", 30, 5)

# 공격 함수
print("==== Step 1. 딕셔너리 이용 실행 ====")
hero.attack(monster)

hero.power = -50
print("잘못된 공격")
hero.attack(monster)

'''
캡슐화로 데이터 보호
'''