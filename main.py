from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")
        return 50

class Bow(Weapon):
    def attack(self):
        print("Боец выпускает стрелу из лука.")
        return 30

class Fighter:
    def __init__(self, health=100):
        self.weapon = None
        self.health = health

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            print("Боец не выбрал оружие.")
            return 0

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Боец побежден!")
        else:
            print(f"Боец получил урон {damage} и остался с {self.health} здоровья.")

class Monster:
    def __init__(self, health=100):
        self.health = health

    def attack(self):
        print("Монстр наносит удар.")
        return 40

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"Монстр получил урон {damage} и остался с {self.health} здоровья. Монстр побежден!")
        else:
            print(f"Монстр получил урон {damage} и остался с {self.health} здоровья.")



fighter = Fighter()  # Создаем бойца
monster = Monster()  # Создаем монстра

print("Боец выбирает меч.")
fighter.change_weapon(Sword())  # Боец выбирает меч
damage = fighter.attack()  # Боец наносит удар мечом
monster.defend(damage)

print("\nБоец выбирает лук.")
fighter.change_weapon(Bow())  # Боец выбирает лук
damage = fighter.attack()  # Боец выпускает стрелу из лука
monster.defend(damage)

print("\n")
damage = monster.attack()  # Монстр наносит удар
fighter.defend(damage)

print("\nБоец выбирает меч.")
fighter.change_weapon(Sword())  # Боец выбирает меч
damage = fighter.attack()  # Боец наносит удар мечом
monster.defend(damage)



