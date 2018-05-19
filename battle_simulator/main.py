from read_data import data_armies
from strategy import Strategy
from clock import Clock
import logging


def main():
    logging.basicConfig(filename="battle_recap.log", level=logging.INFO)
    clock = Clock()
    armies = data_armies(clock.time())
    strategy = Strategy()
    logging.info("Battle begin")

    while True:
        clock.tick()
        for army in armies:
            for squad in army.squads:
                print(squad.name, squad.health())

        for army_a in armies:
            for army_b in armies:
                if army_a is not army_b:
                    if army_a.alive() and army_b.alive():
                        logging.info("{} health: {} --> {} health: {}".format(
                            army_a.name,
                            army_a.health(),
                            army_b.name,
                            army_b.health()
                        ))
                        target_squad = army_a.select_strategy(strategy, army_b)
                        for squad in army_a.squads:
                            if squad.alive():
                                for unit in squad.units:
                                    if unit.clock <= clock.time():
                                        squad.attack(target_squad, clock.time())
                                        unit.up_exp()
        army_alive = 0
        army_name = ""
        for army in armies:
            if army.alive():
                army_alive += 1
                army_name = army.name
        if army_alive == 1:
            for army in armies:
                for squad in army.squads:
                    print(squad.name, squad.health())
            logging.info("{} win!".format(army_name))
            print(army_name, "win!")
            return


if __name__ == '__main__':
    main()
