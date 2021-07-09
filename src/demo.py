import chess
import chess.svg

from src.mcts import MCTS
from src.state import ChessState

players = ["Black", "White"]


def play_game():
    """
    Play a sample game between two UCT players where each player gets a different number of UCT iterations.
    """
    board = chess.Board()
    board.reset()
    print(chess.svg.board(board))
    state = ChessState(board=board, side_to_move=board.turn)

    while state.get_moves():
        print(str(state))
        if state.player_just_moved == chess.BLACK:
            m = MCTS.search(root_state=state, max_iteration=1000, verbose=False)  # White
        else:
            m = MCTS.search(root_state=state, max_iteration=1, verbose=False)  # Black

        print("Best Move: " + str(m) + "\n")
        state.do_move(m)

    if state.get_result(state.player_just_moved) == 1.0:
        print("Player " + players[int(state.player_just_moved)] + " wins!")
    elif state.get_result(state.player_just_moved) == 0.0:
        print("Player " + players[int(not state.player_just_moved)] + "wins!")
    else:
        print("Nobody wins!")


play_game()
