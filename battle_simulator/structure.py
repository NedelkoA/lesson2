from random import randint


class Soldier:
    def __init__(self):
        self.name = 'Vasiya'
        self.health = 100
        self.recharge = 500
        self.experience = 0
        self.level = 0
        self.damage = 0.05

    def up_exp(self, exp):
        if self.experience < 50:
            self.experience = self.experience + exp
            if self.experience >= 50:
                self.level = self.level + (self.experience // 50)
                self.experience = self.experience % 50
        return self.experience

    def up_dmg(self):
        exp = self.experience
        if self.level > 0:
            exp += self.level * 50
        self.damage = 0.05 + exp / 100
        return self.damage

    def up_recharge(self):
        self.recharge = self.recharge - (5 * self.level)
        return self.recharge

    def attack(self):
        chance_attack = 0.5 * (1 + self.health/100) * randint(50 + self.experience, 100) / 100
        return chance_attack

    def is_alive(self):
        if self.health > 0:
            return True
        if self.health <= 0:
            return False


class Vahicles:
    def __init__(self, *args):
        self.health = 100
        self.recharge = 1000
        self.damage = 0.1
        self.operators = [
            unit
            for unit in args
        ]

    def attack(self):
        multiplication = 1
        for i in self.operators:
            multiplication *= i.attack()
        gavg = multiplication ** (1/3)
        return round(0.5 * (1 + self.health / 100) * gavg, 2)

    def up_dmg(self):
        exp_soldrs = 0
        for i in self.operators:
            exp_soldrs += i.experience
            if i.level > 0:
                exp_soldrs += i.level * 50
        sum_exp = exp_soldrs / 100
        self.damage = 0.1 + sum_exp
        return self.damage

    def get_dmg(self, damage):
        count = 0
        wich = randint(0,2)
        self.health = self.health - (damage * 0.6)
        for i in self.operators:
            if count == wich:
                i.health = i.health - (damage * 0.2)
            else:
                i.health = i.health - (damage * 0.1)
            count += 1

    def is_alive(self):
        for i in self.operators:
            if self.health > 0 and i.health > 0:
                return True
            elif self.health > 0 and i.health < 0:
                return False
        if self.health <= 0:
            for i in self.operators:
                i.health = 0
            return False


class Squad:
    def __init__(self, *args):
        self.units = [
            unit
            for unit in args
        ]

    def attack(self):
        multiplication = 1
        for i in self.units:
            multiplication *= i.attack()
        gavg = multiplication ** (1 / len(self.units))
        return round(gavg, 2)

    def take_dmg(self):
        damage = 0
        for i in self.units:
            damage += i.damage
        return damage

    def get_dmged(self, damage):
        for i in self.units:
            i.health = i.health - (damage / len(self.units))

    def total_health(self):
        health = 0
        for i in self.units:
            health += i.health
        return health

class Army:
    def __init__(self, *args):
        self.squads = [
            squad
            for squad in args
        ]

    def attack(self):
        multiplication = 1
        for i in self.squads:
            multiplication *= i.attack()
        gavg = multiplication ** (1 / len(self.squads))
        return round(gavg, 2)

    def take_dmg(self):
        damage = 0
        for i in self.squads:
            damage += i.take_dmg()
        return damage

    def get_dmged(self, damage):
        for i in self.squads:
            i.get_dmged(damage)

class Strategy:
    def select_strategy(self, wich, target):
        if wich == 'weakest':
            min_health = target.squads[0].total_health()
            weak_squad = target.squads[0]
            for i in target.squads:
                if i.total_health() < min_health:
                    min_health = i.total_health()
                    weak_squad = i
            return weak_squad
        elif wich == 'strongest':
            max_health = target.squads[0].total_health()
            strong_squad = target.squads[0]
            for i in target.squads:
                if i.total_health() > max_health:
                    max_health = i.total_health()
                    strong_squad = i
            return strong_squad

    def random_strategy(self, target):
        wich = randint(0,1)
        if wich == 0:
            self.select_strategy('weakest', target)
        elif wich == 1:
            self.select_strategy('strongest', target)