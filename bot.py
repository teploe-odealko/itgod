# coding=utf-8
from model.hero import *

from model.abilites import AbilityType
from model.teams import Teams
import json
import random
import time
from warrior import warrior


# start_strategy = 1



def main():
    game = json.loads(input())
    # game_map = Map(game)  # карта игрового мира
    # game_params = Parameters(game)  # параметры игры
    game_teams = Teams(game)  # моя команда
    if game_teams.enemy_team[0].hero_type == HeroType.Warrior:
        warrior(game)


main()