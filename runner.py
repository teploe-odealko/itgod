import argparse
from subprocess import Popen, PIPE
from model.game import Game

server_ip = "wss://gameapi.it-god.ru"
user_id = "9efeda32-d4de-4c41-ad6e-5e7c5f2fa56f"
bot_id = "b8750899-93fa-4c87-a85b-1ad40b38c5bc"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Runner for ITGod')

    parser.add_argument('-i', '--ip', type=str, nargs='?', help='Server IP', default=server_ip)
    parser.add_argument('-b', '--bot', type=str, nargs='?', help='Bot Id', default=bot_id)
    parser.add_argument('-u', '--user', type=str, nargs='?', help='User Id', default=user_id)
    parser.add_argument('-g', '--game', type=str, nargs='?', help='Game Id')
    parser.add_argument('-s', '--srv', action='store_true', help='Service argument')

    args = parser.parse_args()

    process = Popen(["python", "-u", "bot.py"], stdout=PIPE, stdin=PIPE)

    if args.srv:
        Game(process, "{}/game".format(args.ip), None, args.bot, args.game)
    else:
        Game(process, "{}/game".format(args.ip), args.user, args.bot, None)
