import json
from models.army import Army


def read_json():
    with open('config_armies.json', 'r') as file:
        json_obj = json.load(file)
    parameters = list(json_obj.values())
    all_armies = []
    for parameter in parameters:
        all_armies.append(Army(**parameter))
    return all_armies


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
    all_armies = read_json()
    battle()
