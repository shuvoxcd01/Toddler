import random

from src.node import Node


class MCTS:
    @staticmethod
    def search(root_state, max_iteration, verbose=False):
        """
        Conduct a UCT search for max_iteration iterations starting from root_state.
        Return the best move from the root_state.
        Assumes 2 alternating players (player 1 starts), with game results in the range [-1.0, 1.0]
        """
        root_node = Node(state=root_state)

        for i in range(max_iteration):
            node = root_node
            state = root_state.clone()

            # Select
            while node.untried_moves == [] and node.childNodes != []:  # node is fully expanded and non-terminal
                node = node.select_child()
                state.do_move(node.move)

            # Expand
            if node.untried_moves:
                m = random.choice(node.untried_moves)
                state.do_move(m)
                node = node.add_child(m, state)  # add child and descend tree

            # Rollout
            while state.get_moves():  # while state is non-terminal
                state.do_move(random.choice(state.get_moves()))

            # Back-propagate
            while node is not None:  # back-propagate from the expanded node and work back to the root node
                node.update(state.get_result(node.player_just_moved))
                node = node.parentNode

        # Output some information about the tree -- can be omitted.
        # if verbose:
        #     print(root_node.tree_to_string(0))
        # else:
        #     print(root_node.children_to_string())

        return sorted(root_node.childNodes, key=lambda c: c.visits)[-1].move
