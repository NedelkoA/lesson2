from .unit import Unit
from random import randint


class Soldier(Unit):
    def __init__(self, hp, name):
        self.hp = hp
        self.name = name
        self.experience = 0

    def health(self):
        return round(self.hp, 3)

    def chance_attack(self):
        return 0.5 * (1 + self.health()/100) * randint(50 + self.experience, 100) / 100

    def damage(self):
        return 0.05 + self.experience / 100

    def attack_power(self):
        return round(self.chance_attack() * self.damage(), 3)

    def alive(self):
        if self.health() > 0:
            return True
        elif self.health() <= 0:
            return False

    def recharge(self):
        pass

    def attack(self, target):
        target.take_damage(self.attack_power())

    def take_damage(self, dmg):
        self.hp = self.health() - dmg

    def up_exp(self):
        if self.experience < 50:
            self.experience = self.experience + 50
        return self.experience