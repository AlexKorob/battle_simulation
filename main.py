import json
from models.army import Army
from intro import draw_py_battle


def read_json():
    with open('config_armies.json', 'r') as file:
        json_obj = json.load(file)
    parameters = list(json_obj.values())
    all_armies = []
    for parameter in parameters:
        all_armies.append(Army(**parameter))
    return all_armies


def battle():
    space = ' ' * 56
    print("\n" * 2)
    print(space, 'Fight Armies', end="\n" * 2)
    for army in all_armies:
        print(space, ' --' + str(army) + '--')
    print()

    while len(all_armies) != 1:
        for army in all_armies:
            army.update()
            if army.alive:
                army.attack(all_armies)
            else:
                all_armies.remove(army)

    winner = all_armies[0]
    print(space, 'Winner:', winner)

    print("Show details? (y/n): ", end='')
    inpt = input()
    if inpt == 'y' or inpt == 'д':
        print()
        print('Status', str(winner) + ':')
        print('Squads:', len(winner.squads))
        for i, squad in enumerate(winner.squads):
            print(i+1, "SQUAD")
            print()
            print('Number of members', len(squad.members))
            for member in squad.members:
                print(member)


if __name__ == '__main__':
    all_armies = read_json()
    draw_py_battle()
    battle()
