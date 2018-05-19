from .unit import Unit
from random import randint


class Vehicles(Unit):
    def __init__(self, hp, name, operators, clock):
        self.hp = hp
        self.name = name
        self.operators = operators
        self.clock = clock

    def health(self):
        return round(self.hp, 2)

    def chance_attack(self):
        multiplication = 1
        for operator in self.operators:
            multiplication *= operator.chance_attack()
        gavg = multiplication ** (1 / 3)
        return 0.5 * (1 + self.health() / 100) * gavg

    def damage(self):
        exp_soldrs = 0
        for operator in self.operators:
            exp_soldrs += operator.experience
        sum_exp = exp_soldrs / 100
        return 0.1 + sum_exp

    def attack_power(self):
        return round(self.chance_attack() * self.damage(), 2)

    def alive(self):
        operator_alive = 0
        for operator in self.operators:
            if operator.alive():
                operator_alive += 1
        if self.health() > 0 and operator_alive > 0:
            return True
        elif operator_alive == 0:
            self.hp = 0
            return False
        elif self.health() <= 0:
            for operator in self.operators:
                operator.hp = 0
            self.hp = 0
            return False

    def take_damage(self, dmg):
        unlucky_operator = randint(0, 2)
        self.hp = self.health() - (dmg * 0.6)
        count = 0
        for operator in self.operators:
            if count == unlucky_operator:
                operator.hp = operator.hp - (dmg * 0.2)
            else:
                operator.hp = operator.hp - (dmg * 0.1)
            count += 1

    def attack(self, target, clock):
        target.take_damage(self.attack_power())
        self.clock = clock

    def up_exp(self):
        for unit in self.operators:
            unit.up_exp()