from math import *


class Node:
    """
    A node in the game tree. Note that win is always from the viewpoint of playerJustMoved.
    Crashes if state not specified.
    """

    def __init__(self, move=None, parent=None, state=None):
        self.move = move  # the move that got us to this node - "None" for the root node
        self.parentNode = parent  # "None" for the root node.
        self.childNodes = []
        self.value = 0
        self.visits = 0
        self.untried_moves = state.get_moves()  # future child nodes
        self.player_just_moved = state.player_just_moved  # the only part of the state that Node needs later

    def select_child(self):
        """
        Use the UCB1 formula to select a child node.
        Often a constant UCTK is applied so we have
        lambda c : c.wins/c.visits + UCTK * sqrt(2 * log(self.visits)/c.visits) to vary the amount of
        exploration versus exploitation.
        """
        s = sorted(self.childNodes, key=lambda c: c.value / c.visits + sqrt(2 * log(self.visits) / c.visits))[-1]
        return s

    def add_child(self, m, s):
        """
        Remove m from untriedMoves and add a new child node for this move.
        Return the added child node.
        """
        n = Node(move=m, parent=self, state=s)
        self.untried_moves.remove(m)
        self.childNodes.append(n)
        return n

    def update(self, result):
        """
        Update this node.
        One additional visit and result additional wins.
        Result must be from the viewpoint of playerJustMoved.
        """
        self.visits += 1
        self.value += result

    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.value) + "/" + str(self.visits) + " U:" + str(
            self.untried_moves) + "]"

    def tree_to_string(self, indent):
        s = self.indent_string(indent) + str(self)
        for c in self.childNodes:
            s += c.tree_to_string(indent + 1)
        return s

    @staticmethod
    def indent_string(indent):
        s = "\n"
        for i in range(1, indent + 1):
            s += "| "
        return s

    def children_to_string(self):
        s = ""
        for c in self.childNodes:
            s += str(c) + "\n"
        return s
