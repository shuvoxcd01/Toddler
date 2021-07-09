from copy import deepcopy

import chess


class ChessState:
    def __init__(self, board: chess.Board, side_to_move: bool, max_depth=15):
        self.player_just_moved = not side_to_move
        self.board = board
        self.max_depth = max_depth
        self.num_move = 0
        self.piece_value_map = {"p": -1, "n": -3, "b": -3, "r": -5, "q": -9, "k": 0,
                                "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0}

    def clone(self):
        return deepcopy(self)

    def do_move(self, move):
        assert move in list(self.board.legal_moves)
        self.board.push(move)
        self.player_just_moved = not self.player_just_moved
        self.num_move += 1

    def get_moves(self):
        if self.board.is_game_over() or (self.num_move >= 2 * self.max_depth):
            return []
        return list(self.board.legal_moves)

    def _evaluate_position(self, player_just_moved: bool):
        assert not self.board.is_game_over()

        value = 0
        for piece in self.board.piece_map().values():
            value += self.piece_value_map[piece.symbol()]

        if not player_just_moved:
            value = - value

        return value / 1000

    def get_result(self, player_just_moved: bool):
        possible_results = ["1-0", "0-1", "1/2-1/2", "*"]
        result = self.board.result()
        index = possible_results.index(result)

        if index == 3:
            return self._evaluate_position(player_just_moved)

        if index == 2:
            return 0.5

        return 1.0 if bool(index) != player_just_moved else -1.0

    def __repr__(self):
        return str(self.board)
