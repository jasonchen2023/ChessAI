# Jason Chen
# CS76 Fall 21
# PA3

import chess
import math
import random

class AlphaBetaAI():
    def __init__(self, depth_limit):
        self.depth_limit = depth_limit
        self.num_calls = 0

    # returns optimal move
    def choose_move(self, board):
        
        self.max_player = board.turn
        (value, move) = self.max_value(board, 0, -math.inf, math.inf)
        print("move", move)
        print("Value: " + str(value))
        return move

    # returns move with highest value
    def max_value(self, board, depth, alpha, beta):
        self.num_calls += 1

        if board.is_game_over():
            return (self.eval(board), None)

        # cutoff limit reached
        if depth >= self.depth_limit:
            return (self.eval(board), None)
  
        v = -math.inf

        actions = list(board.legal_moves)
        random.shuffle(actions)

        for a in actions:
            board.push(a)
            (v2, a2) = self.min_value(board, depth + 1, alpha, beta)

            if v2 > v:
                (v, move) = (v2, a)
                alpha = max(alpha, v)
            
            board.pop()
            
            if v >= beta:   # prune this branch
                return (v, move)
        
        # print("max", move)
        return (v, move)


    # returns move with min value
    def min_value(self, board, depth, alpha, beta):

        self.num_calls += 1

        if board.is_game_over():    # game over
            return (self.eval(board), None)

        # cutoff limit reached
        if depth >= self.depth_limit:
            return (self.eval(board), None)
    
        v = math.inf
        actions = list(board.legal_moves)
        random.shuffle(actions)
       
       # loop through all possible next states
        for a in actions:
            board.push(a)
            (v2, a2) = self.max_value(board, depth + 1, alpha, beta)

            if v2 < v:
                (v, move) = (v2, a)
                beta = min(beta, v)

            board.pop()
            
            if v <= alpha:  # prune this branch
                return (v, move)
        
        return (v, move)


    # evaluation for status of chess game
    def eval(self, board):

        # returns 100 for a win, -100 for a loss
        if board.is_checkmate():
            if board.turn == self.max_player:
                return -100
            else:
                return 100
        
        elif board.is_stalemate():
            return 0

        elif board.is_insufficient_material():
            return 0

        else:
            score = 0

            # loop through all pieces
            for i in range(1, 7):
                score += i * len(board.pieces(i, self.max_player))   # add number of your pieces to score
                score -= i * len(board.pieces(i, not self.max_player))    # subtract number of opponents pieces to score
        
            return score