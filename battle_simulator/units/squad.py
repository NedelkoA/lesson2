class Squad:
    def __init__(self, name, unts):
        self.name = name
        self.units = unts
        #self.clock = Clock()
        #self.set_rech = 100

    def attack_power(self):
        damage = 0
        multiplication = 1
        for unit in self.units:
            multiplication *= unit.chance_attack()
            damage += unit.damage()
        chance_attack = multiplication ** (1 / len(self.units))
        return round(chance_attack * damage, 3)

    def take_damage(self, dmg):
        for unit in self.units:
            unit.take_damage((dmg / len(self.units)))

    def attack(self, target):
        target.take_damage(self.attack_power())
        #self.set_rech += self.clock.time()

    def total_health(self):
        hp = 0
        for unit in self.units:
            hp += unit.health()
        return hp

    def alive(self):
        unit_alive = 0
        for unit in self.units:
            if unit.health() > 0:
                unit_alive += 1
        if unit_alive > 0:
            return True
        elif unit_alive == 0:
            return False