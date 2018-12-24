from random import randint
from time import time
from .unit import Unit


class Soldier(Unit):
    def __init__(self):
        self.recharge = randint(100, 1000)
        self.health = 1
        self.experience = 0
        self.saved_time = 0

    def up(self):
        self.experience += 1

    def attack(self):
        exp = self.experience if self.experience <= 50 else 50
        calc = 0.5 * (1 + self.health/100) * randint(50 + exp, 100) / 100
        return calc

    def damage(self):
        if self.is_recharged():     # if soldier recharged return damage
            dmg = 0.05 + self.experience / 100
            self.up()
            self.saved_time = time()
            return round(dmg, 2)
        return 0    # else return damage == 0

    def get_damage(self, dmg):
        self.health -= dmg

    def is_recharged(self):
        current_time = time()
        if (current_time - self.saved_time)*1000 > self.recharge:
            return True
        return False

    def alive(self):
        if self.health <= 0:
            return False
        return True

    def __str__(self):
        return 'Soldier health: ' + str(int(round(self.health, 2) * 100)) + \
               ' exp: ' + str(self.experience) + '\n'
