# Jason Chen
# CS76 Fall 21
# PA3

from MinimaxAI import MinimaxAI
import math


class IDS_MinimaxAI:

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit
        self.num_calls = 0

    # iterative deepening search
    def choose_move(self, board):

        depth = 0
        best_value = -math.inf
        best_move = None

        # while depth limit is not exceeded, call dfs
        while depth <= self.depth_limit:
            player = MinimaxAI(depth)

            move = player.choose_move(board)
            # print("depth", depth, move, player.get_value())
            if (player.get_value() >= best_value):
                self.num_calls += player.num_calls
                best_value = player.get_value()
                if (move != None):
                    best_move = move    

            depth += 1
        
        # print("best move", best_move, best_value)
        return best_move
