from random import randint


class Unit:
    def __init__(self):
        self.health = 1
        self.recharge = randint(100, 1000)
