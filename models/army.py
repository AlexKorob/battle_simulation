from random import choice
from .squad import Squad


class Army:
    def __init__(self, name=None, squad=1, units=None):
        self.squads = [Squad(units, i + 1) for i in range(squad)]
        self.name = name

    def choose_targets(self, list_with_armies):
        target_squads = []
        for army in list_with_armies:
            if army != self:
                for squad in army.squads:
                    if squad.alive:
                        target_squads.append(squad)
        return target_squads

    def update(self):
        accum = []
        for squad in self.squads:
            if squad.alive:
                accum.append(squad)
        self.squads = accum

    @property
    def alive(self):
        if self.squads == []:
            return False
        return True

    @staticmethod
    def weakest_squad(enemy_squads):
        ''' squad with minimum health the most weakest '''
        weak = enemy_squads[0]
        for squad in enemy_squads:
            if squad.health < weak.health:
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

    def choose_target(self, all_armies):
        enemy_squads = self.choose_targets(all_armies)
        if enemy_squads == []:
            return None
        choose_list = choice(['random', 'weakest', 'stronger'])

        if choose_list == 'random':
            return choice(enemy_squads)
        elif choose_list == 'weakest':
            return self.weakest_squad(enemy_squads)
        elif choose_list == 'stronger':
            return self.stronger_squad(enemy_squads)

    def attack(self, all_armies):
        '''Army choose random one own squad
            and one enemy squad from method 'choose_targets'''
        squad = choice(self.squads)
        target_squad = self.choose_target(all_armies)
        target_army = None
        for army in all_armies:
            if target_squad in army.squads:
                target_army = army
        if squad.attack() > target_squad.attack():
            return {"attack": True,
                    "self_squad": squad,
                    "enemy_squad": target_squad,
                    "enemy_army": target_army}
        return {"attack": False}

    def __str__(self):
        return str(self.name)
