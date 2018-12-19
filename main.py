from random import randint
from random import choices
from models.army import Army


def battle():
    print('Fight Armies: ')
    for army in all_armies:
        print('--' + str(army) + '--')
    print()

    while len(all_armies) != 1:
        for army in all_armies:
            army.attack(all_armies)

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
