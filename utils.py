from model.parameters import Parameters
from model.state import State
from model.teams import Teams


def update_state(game_map, game_params, game_teams):
    state = State(input(), game_teams, game_params)
    my_buildings = state.my_buildings()
    my_squads = state.my_squads()
    my_squads.sort(key=lambda c: c.way.left, reverse=False)
    enemy_buildings = state.enemy_buildings()
    enemy_squads = state.enemy_squads()
    neutral_buildings = state.neutral_buildings()
    forges_buildings = state.forges_buildings()

    return state, my_buildings, my_squads, enemy_buildings, enemy_squads, neutral_buildings, forges_buildings
