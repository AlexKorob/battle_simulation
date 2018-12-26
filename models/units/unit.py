from abc import abstractmethod, abstractproperty, ABC


class Unit(ABC):
    UNIT = {}

    @abstractproperty
    def recharge(self):
        pass

    @abstractproperty
    def health(self):
        pass

    def register(self, cls, name):
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

    @classmethod
    def register(cls, name):
        def dec(unit_cls):
            cls.UNIT[name] = unit_cls
            return unit_cls
        return dec

    @classmethod
    def new(cls, name, **kwargs):
        return cls.UNIT[name](**kwargs)
