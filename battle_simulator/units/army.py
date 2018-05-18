class Army:
    def __init__(self, name, squads):
        self.name = name
        self.squads = squads

    def select_strategy(self, strategy, target):
        if strategy == 'weakest':
            min_health = target.squads[0].total_health()
            weak_squad = target.squads[0]
            for squad in target.squads:
                if squad.total_health() < min_health:
                    min_health = squad.total_health()
                    weak_squad = squad
            return weak_squad
        elif strategy == 'strongest':
            max_health = target.squads[0].total_health()
            strong_squad = target.squads[0]
            for squad in target.squads:
                if squad.total_health() > max_health:
                    max_health = squad.total_health()
                    strong_squad = squad
            return strong_squad

    def random_strategy(self, target):
        strategy = randint(0, 1)
        if strategy == 0:
            self.select_strategy('weakest', target)
        elif strategy == 1:
            self.select_strategy('strongest', target)

    def alive(self):
        alive_squads = 0
        for squad in self.squads:
            if squad.alive():
                alive_squads += 1
        if alive_squads == 0:
            return False
        elif alive_squads > 0:
            return True