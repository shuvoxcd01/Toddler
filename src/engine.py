import chess
import chess.svg

from mcts import MCTS
from state import ChessState


class Engine:
    def __init__(self):
        self.name = "Toddler"
        self.author = "Falguni Das Shuvo"
        self.board = chess.Board()

    def set_position(self, fen, moves: list):
        print(fen, moves)
        self.board = chess.Board(fen=fen) if fen else chess.Board()
        for move in moves:
            self.board.push(chess.Move.from_uci(move))

    def find_best_move(self, max_iteration=10000):
        root_state = ChessState(self.board, self.board.turn)
        best_move = chess.Move.uci(MCTS.search(root_state, max_iteration))
        return best_move
