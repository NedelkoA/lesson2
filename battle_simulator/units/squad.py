class Squad:
    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.hp = 0

    def attack_power(self):
        damage = 0
        multiplication = 1
        for unit in self.units:
            multiplication *= unit.chance_attack()
            damage += unit.damage()
        chance_attack = multiplication ** (1 / len(self.units))
        return round(chance_attack * damage, 2)

    def take_damage(self, dmg):
        for unit in self.units:
            unit.take_damage((dmg / len(self.units)))

    def attack(self, target, clock):
        target.take_damage(self.attack_power())
        for unit in self.units:
            unit.clock = clock

    def health(self):
        return round(sum([
            unit.health()
            for unit in self.units
        ]), 2)

    def alive(self):
        unit_alive = 0
        for unit in self.units:
            if unit.alive():
                unit_alive += 1
        return unit_alive > 0