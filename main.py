from random import randint, choices


class Unit:
    def __init__(self):
        self.health = 1
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
        dmg = 0.05 + self.experience / 100
        self.up()
        return round(dmg, 2)

    def get_damage(self, dmg):
        self.health -= dmg

    def alive(self):
        if self.health <= 0:
            return False
        return True

    def __str__(self):
        return 'Soldier health: ' + str(int(round(self.health, 2) * 100)) + \
               ' exp: ' + str(self.experience) + '\n'


class Vehicle(Unit):
    def __init__(self, operators):
        super().__init__()
        self.health_coeff = 3   # указывает коефиц. здоровья
        self.health *= 3
        self.recharge = randint(1000, 2000)
        self.operators = operators if 0 < operators <= 3 else 1
        self.operators = [Soldier() for i in range(operators)]

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
        return int((tot_health / (len(self.operators) + self.health_coeff)) * 100)

    def up_level(self):
        for oper in self.operators:
            oper.up()

    def damage(self):
        oper_exp = [oper.experience/100 for oper in self.operators]
        self.up_level()
        return 0.1 + sum(oper_exp)

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


class Squad:
    def __init__(self, num_soldiers, num_vehicle):
        self.soldiers = [Soldier() for i in range(num_soldiers)]
        self.vehicles = [Vehicle(randint(2, 3)) for i in range(num_vehicle)]
        self.members = self.soldiers + self.vehicles

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


class Army:
    global all_armies

    def __init__(self, squad=1, soldier=5, vehicle=3, name=None):
        soldier = 5 if 3 >= soldier >= 7 else soldier
        vehicle = 3 if 1 >= vehicle >= 6 else vehicle
        self.squads = [Squad(soldier, vehicle) for i in range(squad)]
        self.name = name
        self.status = 'Active'

    def all_enemy_squads(self, list_with_armies):
        target_squads = []
        for army in list_with_armies:
            if army != self:
                for squad in army.squads:
                    if squad.alive():
                        target_squads.append(squad)
        self.ts = target_squads
        return target_squads

    def update(self):
        accum = []
        for squad in self.squads:
            if squad.alive():
                accum.append(squad)
        self.squads = accum
        if self.squads == []:
            all_armies.remove(self)

    @staticmethod
    def weakest_squad(enemy_squads):
        ''' squad with minimum health the most weakest '''
        weak = enemy_squads[0]
        for squad in enemy_squads:
            if squad.health() < weak.health():
                weak = squad

        return weak

    @staticmethod
    def stronger_squad(enemy_squads):
        ''' squad with maximum units the most stonger '''
        power = enemy_squads[0]
        for squad in enemy_squads:
            if len(squad.members) > len(power.members):
                power = squad

        return power

    def choose_target(self):
        enemy_squads = self.all_enemy_squads(all_armies)
        if enemy_squads == []:
            return None
        choose_list = choices(['random', 'weakest', 'stronger'])[0]

        if choose_list == 'random':
            return choices(enemy_squads)[0]
        elif choose_list == 'weakest':
            return self.weakest_squad(enemy_squads)
        elif choose_list == 'stronger':
            return self.stronger_squad(enemy_squads)

    def attack(self):
        '''Army choose random one own squad
            and one enemy squad from method 'all_enemy_squads'''
        self.update()
        if (self in all_armies):
            squad = choices(self.squads)[0]
            target = self.choose_target()
            if squad.attack() > target.attack():
                damage = squad.damage()
                target.get_damage(damage)

    def __str__(self):
        return self.name


def battle():
    print('Fight Armies: ')
    for army in all_armies:
        print('--' + str(army) + '--')
    print()

    while len(all_armies) != 1:
        for army in all_armies:
            army.attack()

    winner = all_armies[0]
    print('Winner: ', winner)

    # uncommet below for details
    '''
    print()
    print('Status', str(winner) + ':')
    print('Squads:', len(winner.squads))
    for i, squad in enumerate(winner.squads):
        print(i+1, "SQUAD")
        print()
        print('Number of members', len(squad.members))
        for member in squad.members:
            print(member)
    '''


if __name__ == '__main__':
    all_armies = [
        Army(squad=2, soldier=2, vehicle=2, name='ARMY_1'),
        Army(squad=3, soldier=6, vehicle=4, name='ARMY_2'),
        Army(squad=3, soldier=6, vehicle=4, name='ARMY_3'),
        Army(squad=3, soldier=6, vehicle=4, name='ARMY_4'),
        ]
    battle()
