import sys

from engine import Engine

engine = Engine()


def reply_uci():
    sys.stdout.write("id name " + engine.name + " \n")
    sys.stdout.write("id author " + engine.author + " \n")
    sys.stdout.write("uciok \n")


def reply_isready():
    sys.stdout.write("readyok \n")


def reply_quit():
    sys.exit()


def reply_position(arg: list):
    pos_type = arg[0]

    if pos_type == "startpos":
        fen_string = None
        moves = []
        if len(arg) > 2:
            moves = arg[2:]
        engine.set_position(fen_string, moves)
    elif pos_type == "fen":
        fen_string = arg[1]
        moves = []
        for i in range(2, len(arg)):
            if arg[i] == "moves":
                moves = arg[i + 1:]
                break
            fen_string += " " + arg[i]
        engine.set_position(fen_string, moves)
    else:
        raise Exception("Error!")


def reply_go(arg):
    best_move = engine.find_best_move(1000)
    sys.stdout.write("bestmove " + best_move + " \n")


def reply_ucinewgame():
    sys.stdout.write("new game \n")


def reply_stop():
    sys.stdout.write("stopped \n")


commands = {'uci': reply_uci,
            'isready': reply_isready,
            'ucinewgame': reply_ucinewgame,
            'position': reply_position,
            'go': reply_go,
            'stop': reply_stop,
            'quit': reply_quit}

while True:
    command = input()
    tokens = command.split()
    token_head = tokens[0]
    token_rest = tokens[1:]
    if token_head in commands:
        commands[token_head]() if not token_rest else commands[token_head](token_rest)
    else:
        sys.stdout.write("Command not recognized \n")
