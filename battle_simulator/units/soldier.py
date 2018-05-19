from .unit import Unit
from random import uniform


class Soldier(Unit):
    def __init__(self, hp, name, clock):
        self.hp = hp
        self.name = name
        self.experience = 0
        self.clock = clock

    def health(self):
        return round(self.hp, 2)

    def chance_attack(self):
        return 0.5 * (1 + self.health()/100) * uniform(50 + self.experience, 100) / 100

    def damage(self):
        return 0.05 + self.experience / 100

    def attack_power(self):
        return round(self.chance_attack() * self.damage(), 2)

    def alive(self):
        if self.health() > 0:
            return True
        elif self.health() <= 0:
            self.hp = 0
            return False

    def attack(self, target, clock):
        target.take_damage(self.attack_power())
        self.clock = clock

    def take_damage(self, dmg):
        self.hp = self.health() - dmg

    def up_exp(self):
        if self.experience < 50:
            self.experience = self.experience + 0.1
        return self.experience
