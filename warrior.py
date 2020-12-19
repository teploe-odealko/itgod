from utils import update_state
from model.abilites import AbilityType
from threading import Thread
from model.map import Map
from model.parameters import Parameters
from model.teams import Teams


def start_strategy(enemy_squads, state, my_buildings, enemy_buildings, game):
    game_map = Map(game)  # карта игрового мира
    game_teams = Teams(game)  # моя команда
    while len(enemy_squads) == 0:
        state, my_buildings, my_squads, enemy_buildings, \
            enemy_squads, neutral_buildings, forges_buildings = update_state(game)
        continue
    if state.ability_ready(AbilityType.Area_damage):
        location = game_map.get_tower_location(enemy_buildings[0].id)
        print(game_teams.my_her.area_damage(location))
    # while my_buildings[0].creeps_count < 16:
    #     state, my_buildings, my_squads, enemy_buildings, \
    #         enemy_squads, neutral_buildings, forges_buildings = update_state()

    print(game_teams.my_her.move(my_buildings[0].id, enemy_buildings[0].id, 1))


def warrior(game):

    while True:
        try:
            state, my_buildings, my_squads, enemy_buildings, \
                enemy_squads, neutral_buildings, forges_buildings = update_state(game)

            # invisible_ability_th = Thread(target=start_strategy, args=(enemy_squads, state, my_buildings, enemy_buildings))
            x = Thread(target=start_strategy, args=(enemy_squads, state, my_buildings, enemy_buildings, game))
            x.start()

            # if state.ability_ready(AbilityType.Armor):
            #     print(game_teams.my_her.armor(my_buildings[0].id))
            # # Проверяем доступность абилки Разрушение
            # # if len(enemy_squads) > 4:

            #
            # # Upgrade башни
            # if my_buildings[0].level.id < len(game_params.tower_levels) - 1:
            #     # Если хватает стоимости на upgrade
            #     update_coast = game_params.get_tower_level(my_buildings[0].level.id + 1).update_coast
            #     if update_coast < my_buildings[0].creeps_count:
            #         print(game_teams.my_her.upgrade_tower(my_buildings[0].id))
            #         my_buildings[0].creeps_count -= update_coast
            #
            # # Атакуем башню противника
            # # определяем расстояние между башнями
            # distance = game_map.towers_distance(my_buildings[0].id, enemy_buildings[0].id)
            # # определяем сколько тиков идти до нее со стандартной скоростью
            # ticks = distance / game_params.creep.speed
            # # определяем прирост башни в соответствии с ее уровнем
            # enemy_creeps = 0
            # if enemy_buildings[0].creeps_count >= enemy_buildings[0].level.player_max_count:
            #     # если текущее количество крипов больше чем положено по уровню
            #     enemy_creeps = enemy_buildings[0].creeps_count
            # else:
            #     # если меньше - будет прирост
            #     grow_creeps = ticks / enemy_buildings[0].level.creep_creation_time
            #     enemy_creeps = enemy_buildings[0].creeps_count + grow_creeps
            #     if enemy_creeps >= enemy_buildings[0].level.player_max_count:
            #         enemy_creeps = enemy_buildings[0].level.player_max_count
            # # определяем количество крипов с учетом бонуса защиты
            # enemy_defence = enemy_creeps * (1 + enemy_buildings[0].DefenseBonus)
            # # если получается в моей башне крипов больше + 10 на червя - идем на врага всей толпой
            # if enemy_defence + 10 < my_buildings[0].creeps_count:
            #     print(game_teams.my_her.move(my_buildings[0].id, enemy_buildings[0].id, 1))
            #
            # # Применение абилки ускорение
            # if len(my_squads) > 4:
            #     if state.ability_ready(AbilityType.Speed_up):
            #         location = game_map.get_squad_center_position(my_squads[2])
            #         print(game_teams.my_her.speed_up(location))

        except Exception as e:
            print(str(e))
        finally:
            """ Требуется для получения нового состояния игры  """
            print("end")
