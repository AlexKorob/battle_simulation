from random import randint, choices
from time import time
from .unit import Unit
from .soldier import Soldier


@Unit.register('Vehicle')
class Vehicle(Unit):
    def __init__(self, operators):
        self._health = 3
        self._recharge = randint(1000, 2000)
        self.operators = operators if 0 < operators <= 3 else 1
        self.operators = [Soldier() for i in range(operators)]
        self.saved_time = 0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    @property
    def recharge(self):
        return self._recharge

    def attack(self):
        attacks = [oper.attack() for oper in self.operators]
        gavg = 1
        for oper_attack in attacks:
            gavg *= oper_attack
        gavg = gavg**(1/len(attacks))

        calc = 0.5 * (1 + self.health / 100) * gavg
        return round(calc, 2)

    def total_health(self):
        '''return health in % '''
        tot_health = sum([oper.health for oper in self.operators]) + self.health
        return int((tot_health / (len(self.operators) + self.health)) * 100)

    def up_level(self):
        for oper in self.operators:
            oper.up()

    def damage(self):
        if self.is_recharged():
            oper_exp = [oper.experience/100 for oper in self.operators]
            self.up_level()
            self.saved_time = time()
            return 0.1 + sum(oper_exp)
        return 0

    def is_recharged(self):
        current_time = time()
        if (current_time - self.saved_time)*1000 > self.recharge:
            return True
        return False

    def alive(self):
        if (self.operators != []) and (self.health > 0):
            return True
        else:
            return False

    def update(self):
        accum = []
        for oper in self.operators:
            if oper.health <= 0:
                continue
            accum.append(oper)

        self.operators = accum

    def get_damage(self, dmg):
        tot_dmg = 10
        self.health -= round(dmg*0.6, 2)
        rand_oper = choices(self.operators)[0]
        rand_oper.health -= round(dmg*0.1, 2)
        tot_dmg -= 7
        while tot_dmg > 0:
            for oper in self.operators:
                oper.health -= dmg*0.1
                oper.health = round(oper.health, 2)
                tot_dmg -= 1
                if tot_dmg <= 0:
                    break
        self.update()

    def __str__(self):
        string = 'Vehicle Total health: ' + str(self.total_health()) + '\n'
        for num, oper in enumerate(self.operators):
            string += 'operator ' + str(num+1) + ' health: ' + str(int(round(oper.health, 2)*100)) +\
                      ' exp:' + str(oper.experience) + '\n'
        return string
