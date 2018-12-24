from abc import abstractmethod, abstractproperty, ABC


class Unit(ABC):
    def __init__(self):
        @abstractproperty
        def recharge(self):
            pass

        @abstractproperty
        def health(self):
            pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def alive(self):
        pass
