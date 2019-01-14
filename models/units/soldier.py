from random import randint
from time import time
from .unit import Unit


@Unit.register('Soldier')
class Soldier(Unit):
    def __init__(self):
        self._recharge = randint(100, 1000)
        self._health = 1
        self._experience = 0
        self.saved_time = 0
        self.name = "Soldier"

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    @property
    def recharge(self):
        return self._recharge

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value if value <= 50 else 50

    @property
    def alive(self):
        if self.health == 0:
            return False
        return True

    @property
    def recharged(self):
        current_time = time()
        if (current_time - self.saved_time)*1000 > self.recharge:
            return True
        return False

    def up_level(self):
        self.experience += 1

    def attack(self):
        calc = 0.5 * (1 + self.health/100) * randint(50 + self.experience, 100) / 100
        return calc

    def damage(self):
        if self.recharged:     # if soldier recharged return damage
            dmg = 0.05 + self.experience / 100
            self.up_level()
            self.saved_time = time()
            return round(dmg, 2)
        return 0    # else return damage == 0

    def get_damage(self, dmg):
        self.health -= dmg

    def __str__(self):
        return 'Soldier health: ' + str(int(round(self.health, 2) * 100)) + \
               ' exp: ' + str(self.experience) + '\n'
