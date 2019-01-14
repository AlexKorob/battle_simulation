import json
from models.army import Army
from intro import draw_py_battle
from logs import create_logs


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
                attack = army.attack(all_armies)
                if attack['attack']:
                    squad = attack["self_squad"]
                    enemy_squad = attack["enemy_squad"]
                    enemy_army = attack["enemy_army"]
                    enemy_sq_health_bf_attack = enemy_squad.repr_health
                    damage = squad.damage()
                    enemy_squad.get_damage(damage)
                    if show_log and enemy_sq_health_bf_attack != enemy_squad.repr_health:
                        log_fight.info("squad: %s from army: %s attack squad: %s from army: %s"
                                       ";  squad health: (%6s | %5s)", squad, army, enemy_squad, enemy_army,
                                       enemy_sq_health_bf_attack, enemy_squad.repr_health)
                        if enemy_squad.health <= 0:
                            log_fight.info("squad: %s from army: %s was destroyed", enemy_squad, enemy_army)
                            log_info.info("squad: %s from army: %s was destroyed", enemy_squad, enemy_army)
            else:
                all_armies.remove(army)
                if show_log:
                    log_fight.info("army: %s falled in this battle", army)
                    log_info.info("army: %s falled in this battle", army)

    winner = all_armies[0]
    print(space, "WINNER:", winner)

    if show_log:
        log_info.info("END FIGHT")
        log_info.info('WINNER: %s', winner)
        log_info.info('Status %s:', winner)
        log_info.info('Squads: %s', len(winner.squads))
        for i, squad in enumerate(winner.squads):
            log_info.info("  %s SQUAD", i+1)
            log_info.info("")
            log_info.info('  Number of members %s', len(squad.members))
            for member in squad.members:
                log_info.info("    %s", member)
        print('More details about fight in "fight_logs.txt" file...')


if __name__ == '__main__':
    all_armies = read_json()
    draw_py_battle()
    print()
    show_log = True if input("Show logs? (y/n) ") == 'y' else False
    if show_log:
        log_fight, log_info = create_logs(all_armies)

    battle()
