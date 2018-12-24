from random import choices
from .squad import Squad


class Army:
    def __init__(self, name=None, squad=1, units=None):
        self.squads = [Squad(units) for i in range(squad)]
        self.name = name

    def all_enemy_squads(self, list_with_armies):
        target_squads = []
        for army in list_with_armies:
            if army != self:
                for squad in army.squads:
                    if squad.alive():
                        target_squads.append(squad)
        return target_squads

    def update(self, all_armies):
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

    def choose_target(self, all_armies):
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

    def attack(self, all_armies):
        '''Army choose random one own squad
            and one enemy squad from method 'all_enemy_squads'''
        self.update(all_armies)
        if (self in all_armies):
            squad = choices(self.squads)[0]
            target = self.choose_target(all_armies)
            if squad.attack() > target.attack():
                damage = squad.damage()
                target.get_damage(damage)

    def __str__(self):
        return self.name
