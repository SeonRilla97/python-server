import time
import random
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
            self.inventory.remove(found_potion)
            print(f'{found_potion.name}을(를) 사용했습니다.')
            heal_amount = found_potion.recovery_amount
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f'체력을 회복했습니다. : {self.hp} / {self.max_hp}')


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

class GameManager:
    def __init__(self):
        self.hero = None
    

    def start_game(self):
        print("\n 텍스트 RPG : 전설의 시작")
        name = input("영웅의 이름을 입력하세요 : ")
        self.hero = Hero(name, 100, 30)

        while True:
            print ("\n" + "=" * 30)
            print(" [ 메 인 메 뉴 ] ")
            print ("1. 모험을 떠난다 (랜덤 이벤트)")
            print ("2. 상태 보기")
            print ("3. 종료")   
            print ("=" * 30)
            choice = input(">>> ")

            if choice == "1":
                self.explore()
            elif choice == "2":
                self.hero.show_status()
            elif choice == "3":
                print("게임을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")

            if not self.hero.is_alive():
                print("게임 오버")
                break
    def explore(self):
        print("숲속을 탐험하는중....")
        time.sleep(1)

        dice = random.randint(1, 10)

        if dice <= 3:
            print ("아무 일도 일어나지 않았습니다.")
        elif dice <= 8:
            print ("덤불 속에서 무언가 튀어나왔습니다.")

            if random.random() < 0.8:
                monster = Slime("슬라임", 30, 10)
                monster.drop_item=Item ("빨간포션", 30)
            else:
                monster = Dragon("드래곤", 100, 30)
            self.battle(monster)
        else:
            print("길가에서 반짝이는 것을 발견했습니다.")
            potion = Item("빨간포션", 30)
            self.hero.get_item(potion)

    def battle(self, monster):
        print(f"{monster.name}이 나타났다!")
        print(f"[VS {monster.name} (HP: {monster.hp})]")
        while self.hero.is_alive() and monster.is_alive():
            print("-" * 30 )

            print("선택! : 1. 공격, 2. 포션 사용, 3. 도망")
            choice = input(">>> ")

            turn_ended = False

            if choice == "1":
                self.hero.attack(monster)
                turn_ended = True

            elif choice == "2":
                if self.hero.use_potion():
                    turn_ended = True
                else:
                    turn_ended = False
                    print("도망칠 수 없습니다!")
            elif choice == "3":
                if self.hero.use_potion():
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
                    self.hero.get_item(monster.drop_item)
                break

            if turn_ended and monster.is_alive():
                time.sleep(0.3)
                print( "몬스터의 반격!")
                monster.attack(self.hero)

                if not self.hero.is_alive():
                    print(f"{self.hero.name}이(가) 쓰러졌습니다.")
                    break

# 게임 실행
if __name__ == "__main__":
    game = GameManager()
    game.start_game()