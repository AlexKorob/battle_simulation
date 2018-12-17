from random import randint
from math import sqrt
from time import time
'''
get current ms
int(round(time.time()*1000)) % 1000

'''


class Unit:
    def __init__(self):
        self.health =  100
        self.recharge = randint(100, 1000)


class Soldier(Unit):
    def __init__(self):
        super().__init__()
        self.experience = 0

    def up(self):
        self.experience += 1

    def attack(self):
        exp = self.experience if self.experience <= 50 else 50
        calc = 0.5 * (1 + self.health/100) * randint(50 + exp, 100) / 100
        return calc

    def damage(self):
        return int((0.05 + self.experience / 100)*100)


class Vehicle(Unit):
    def __init__(self, operators):
        super().__init__()
        self.recharge = randint(1000, 2000)
        self.operators = operators if operators <= 3 else 1
        self.operators = [Soldier() for i in range(operators)]

    def attack(self):
        attacks = [oper.attack() for oper in self.operators]
        gavg = 1
        for oper_attack in attacks:
            gavg *= oper_attack
        gavg = gavg**(1/len(attacks))
        
        calc = 0.5 * (1 + self.health / 100) * gavg
        return calc
        
s = Soldier()
tank = Vehicle(3)
