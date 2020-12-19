# coding=utf-8
# from utils import update_state
from model.abilites import AbilityType
from model.state import State
import numpy as np

from threading import Thread


# def update_state(game_map, game_params, game_teams):
#     state = State(input(), game_teams, game_params)
#     my_buildings = state.my_buildings()
#     my_squads = state.my_squads()
#     my_squads.sort(key=lambda c: c.way.left, reverse=False)
#     enemy_buildings = state.enemy_buildings()
#     enemy_squads = state.enemy_squads()
#     neutral_buildings = state.neutral_buildings()
#     forges_buildings = state.forges_buildings()
#
#     return state, my_buildings, my_squads, enemy_buildings, enemy_squads, neutral_buildings, forges_buildings


def move_units(enemy_buildings, my_buildings, enemy_squads, game_map, game_teams):
    if len(enemy_squads) == 4:
        enemy_plan_towers = set([squad.to_id for squad in enemy_squads])
        if len(enemy_plan_towers) == 4:
            print(game_teams.my_her.move(my_buildings[0].id, game_map.get_nearest_tower_id(my_buildings[0].id, list(enemy_plan_towers)), 1))


def cast_aoe(enemy_squads, enemy_buildings, game_map, game_teams):
    global is_first_units
    if len(enemy_squads) == 0:
        return
    if is_first_units == 1:
        location = game_map.get_tower_location(enemy_buildings[0].id)
        print(game_teams.my_her.area_damage(location))
        is_first_units = 0
    else:
        creeps = np.array(enemy_squad.CreepsCount for enemy_squad in enemy_squads)
        location = game_map.get_squad_center_position(enemy_squads[np.argmax(creeps)])
        print(game_teams.my_her.area_damage(location))


    # while my_buildings[0].creeps_count < 16:
    #     state, my_buildings, my_squads, enemy_buildings, \
    #         enemy_squads, neutral_buildings, forges_buildings = update_state()

    # print(game_teams.my_her.move(my_buildings[0].id, enemy_buildings[0].id, 1))


start = 1
ticks = 0
is_first_units = 1


def warrior(game_map, game_params, game_teams):
    global start
    global ticks

    while True:
        state = State(input(), game_teams, game_params)

        my_buildings = state.my_buildings()
        my_squads = state.my_squads()
        # сортируем по остаточному пути
        my_squads.sort(key=lambda c: c.way.left, reverse=False)

        enemy_buildings = state.enemy_buildings()
        enemy_squads = state.enemy_squads()

        neutral_buildings = state.neutral_buildings()

        forges_buildings = state.forges_buildings()

        if state.ability_ready(AbilityType.Area_damage):
            cast_aoe(enemy_squads, enemy_buildings, game_map, game_teams)
        move_units(enemy_buildings, my_buildings, enemy_squads, game_map, game_teams)
        ticks += 1
        print("end")
