from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    @abstractmethod
    def attack(self, target, clock):
        pass

    @abstractmethod
    def take_damage(self, dmg):
        pass

    @property
    @abstractmethod
    def alive(self):
        pass

    @property
    @abstractmethod
    def health(self):
        pass

    @property
    @abstractmethod
    def attack_power(self):
        pass
