class Army:
    def __init__(self, name, squads, strategy):
        self.name = name
        self.squads = squads
        self.strategy = strategy

    def select_strategy(self, strategy, target):
        if self.strategy == 'weakest':
            return strategy.weakest_strategy(target)
        elif self.strategy == 'strongest':
            return strategy.strongest_strategy(target)
        elif self.strategy == 'random':
            return strategy.random_strategy(target)

    def alive(self):
        return self.health() > 0

    def health(self):
        return round(sum([
            squad.health()
            for squad in self.squads
        ]), 2)

    def damage(self):
        return round(sum([
            squad.attack_power()
            for squad in self.squads
        ]), 2)