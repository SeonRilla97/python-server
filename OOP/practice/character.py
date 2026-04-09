import time
# 1. 상속
class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp =hp
        self.max_hp = hp
        self.power = power

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격합니다.")
        damage = self.power
        target.take_damage(damage)

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name}이(가) 쓰러졌습니다.")

        print(f'{self.name}은 {amount}의 피해를 입고 {self.hp}의 체력이 남았습니다. : {self.hp} / {self.max_hp}')

    def show_status(self):
        print(f'이름: {self.name}, 체력: {self.hp} / {self.max_hp}, 공격력: {self.power}')

    def is_alive(self):
        return self.hp > 0

class Hero(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

        self.level=1
        self.inventory=[]
        print(f'{self.name}이(가) 모험을 시작합니다.')

    def get_item(self, item):
            print(f' [가방]: {self.name}은 {item.name}을(를) 획득했습니다.')
            self.inventory.append(item)

    def show_status(self):
        print(f'[영웅] 이름: {self.name}, 체력: {self.hp} / {self.max_hp}, 공격력: {self.power}')
        item_names = [item.name for item in self.inventory] # List Comprehension
        print(f' [가방]: {item_names}')

    def use_potion(self):
        found_potion = None
        for item in self.inventory:
            if item.name == "빨간포션":
                found_potion = item
                break

        if found_potion:
            heal_amount = found_potion.recovery_amount
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f'{self.name}은 {heal_amount}의 체력을 회복했습니다. : {self.hp} / {self.max_hp}')
            self.inventory.remove(found_potion)

            return True
        else:
            print("포션이 없습니다.")
            return False


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.drop_item = None
        print(f'몬스터 {self.name}이(가) 나타났습니다.')
class Slime(Monster):
    def attack(self, target):
        print(f'{self.name}의 몸통박치기!')
        damage = self.power
        target.take_damage(damage)

class Dragon(Monster):
    def attack(self, target):
        print(f'{self.name}의 화염구! ')
        damage = int(self.power * 1.5)
        target.take_damage(damage)


class Item:
    def __init__(self, name, recovery_amount):
        self.name = name
        self.recovery_amount = recovery_amount
# 전투 시스템
def battle(hero, monster):
    print(f"{monster.name}이 나타났다!")
    print(f"(HP: {monster.hp}, 공격력: {monster.power})")
    while hero.is_alive() and monster.is_alive():
        print("-" * 30 )

        print("선택!")
        print("1. 공격")
        print("2. 도망")
        print("3. 포션 사용")
        choice = input("행동을 선택하세요: ")

        turn_ended = False

        if choice == "1":
            hero.attack(monster)
            turn_ended = True

        elif choice == "2":
            if hero.use_potion():
                turn_ended = True
            else:
                turn_ended = False
                print("도망칠 수 없습니다!")
        elif choice == "3":
            if hero.use_potion():
                turn_ended = True
            else:
                turn_ended = False
                print("포션이 없습니다.")
        else:
            print("잘못된 선택입니다.")
            continue

        if not monster.is_alive():
            print(f"{monster.name}을(를) 물리쳤습니다!")
            if monster.drop_item:
                hero.get_item(monster.drop_item)
            break

        if turn_ended and monster.is_alive():
            time.sleep(1)
            print( "몬스터의 반격!")
            monster.attack(hero)

            if not hero.is_alive():
                print(f"{hero.name}이(가) 쓰러졌습니다.")
                break

# 게임 실행
if __name__ == "__main__":
    print("=== 게임 시작 ===")
    hero = Hero("주인공", 100, 30)
    slime = Slime("슬라임", 50, 5)
    dragon = Dragon("드래곤", 200, 20)

    slime.drop_item = Item("빨간포션", 30)


    battle(hero, slime)
    # battle(hero, dragon)

    if hero.is_alive():
        print("승리!")
        print("드래곤 등장!!")
        battle(hero, dragon)
    else:
        print("패배...")