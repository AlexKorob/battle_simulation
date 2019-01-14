from .units.soldier import Soldier  # noqa
from .units.vehicle import Vehicle  # noqa
from .units.unit import Unit


class Squad:
    def __init__(self, units, name):
        self.members = []
        total_units = 0
        self.name = name
        for unit, parameters in units.items():
            if "numbers" not in parameters:
                raise AttributeError("Did not define a numbers in configuration file")
            num_units = parameters["numbers"]
            total_units += num_units
            if total_units > 10:
                raise AssertionError("Units in Squad > 10")
            parameters.pop("numbers")

            for i in range(num_units):
                self.members.append(Unit.new(unit, **parameters))

            parameters['numbers'] = num_units
        self.full_hp = self.health

    def attack(self):
        total_number = len(self.members)
        accum = 1

        for member in self.members:
            accum *= member.attack()

        return round(accum**(1/total_number), 2)

    def update(self):
        accum = []
        for member in self.members:
            if member.alive:
                accum.append(member)

        self.members = accum

    def damage(self):
        total = 0
        for member in self.members:
            total += member.damage()

        return total

    def get_damage(self, dmg):
        dmg = dmg/len(self.members)
        for member in self.members:
            member.get_damage(dmg)
        self.update()

    @property
    def health(self):
        health = 0
        for mem in self.members:
            health += mem.health
        return health

    @property
    def alive(self):
        if self.members:
            return True
        return False

    @property
    def repr_health(self):
        return "%.2f" %(self.health * 100 / self.full_hp)

    def __str__(self):
        return str(self.name)
