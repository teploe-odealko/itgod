from model.hero import *
from model.map import Map
from model.parameters import Parameters
from model.state import State
from model.abilites import AbilityType
from model.teams import Teams
from warrior import *
import json
import random
import time

game = json.loads(input())
game_map = Map(game)  # карта игрового мира
game_params = Parameters(game)  # параметры игры
game_teams = Teams(game)  # моя команда

def main():
    # state = State(input(), game_teams, game_params)
    # if game_teams.enemy_team[0].hero_type == HeroType.Warrior:
    warrior(game_map, game_params, game_teams)


main()
