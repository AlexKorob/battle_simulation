from .units.soldier import Soldier
from .units.vehicle import Vehicle
from .units.unit import Unit

class Squad:
    def __init__(self, units):
        self.members = []
        for unit, numbers in units.items():
            dictionary = numbers
            if not "numbers" in dictionary:
                raise AttributeError("Did not define a numbers in configuration file")
            num_units = dictionary["numbers"]
            dictionary.pop("numbers")

            for i in range(num_units):
                self.members.append(Unit.new(unit, **dictionary))

            dictionary['numbers'] = num_units


    def attack(self):
        total_number = len(self.members)
        accum = 1

        for member in self.members:
            accum *= member.attack()

        return round(accum**(1/total_number), 2)

    def update(self):
        accum = []
        for member in self.members:
            if member.alive() is False:
                continue
            accum.append(member)

        self.members = accum

    def damage(self):
        total = 0
        for member in self.members:
            total += member.damage()

        return round(total, 2)

    def get_damage(self, dmg):
        dmg = dmg/len(self.members)
        for member in self.members:
            member.get_damage(dmg)
        self.update()

    def health(self):
        health = 0
        for mem in self.members:
            health += mem.health
        return health

    def alive(self):
        if self.members:
            return True
        return False
