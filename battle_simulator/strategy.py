from random import randint


class Strategy:
    def weakest_strategy(self, target):
        min_health = min([
            squad.health()
            for squad in target.squads
        ])
        weak_squad = target.squads[0]
        for squad in target.squads:
            if squad.health() <= min_health:
                if squad.health() > 0:
                    min_health = squad.health()
                    weak_squad = squad
        return weak_squad

    def strongest_strategy(self, target):
        max_health = max([
            squad.health()
            for squad in target.squads
        ])
        strong_squad = target.squads[0]
        for squad in target.squads:
            if squad.health() >= max_health:
                max_health = squad.health()
                strong_squad = squad
        return strong_squad

    def random_strategy(self, target):
        strategy = randint(0, 1)
        if strategy == 0:
            return self.weakest_strategy(target)
        elif strategy == 1:
            return self.strongest_strategy(target)