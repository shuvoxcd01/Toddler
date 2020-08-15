from copy import deepcopy

import chess


class ChessState:
    def __init__(self, board: chess.Board, side_to_move: bool):
        self.player_just_moved = not side_to_move
        self.board = board

    def clone(self):
        return deepcopy(self)

    def do_move(self, move):
        assert move in list(self.board.legal_moves)
        self.board.push(move)
        self.player_just_moved = not self.player_just_moved

    def get_moves(self):
        if self.board.is_game_over():
            return []
        return list(self.board.legal_moves)

    def get_result(self, player_just_moved: bool):
        possible_results = ["1-0", "0-1", "1/2-1/2", "*"]
        result = self.board.result()
        index = possible_results.index(result)

        assert index != 3

        if index == 2: return 0.5

        return float(bool(index) != player_just_moved)

    def __repr__(self):
        return str(self.board)
