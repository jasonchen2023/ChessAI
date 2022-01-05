# Jason Chen
# CS76 Fall 21
# PA3

import chess
import math
import random

class MinimaxAI():
    def __init__(self, depth_limit):
        self.depth_limit = depth_limit  # max depth
        self.num_calls = 0


    # returns optimal move
    def choose_move(self, board):

        self.max_player = board.turn
        (self.value, move) = self.max_value(board, 0)
        
        print("move", move)
        print("Value: " + str(self.value))

        return move


    def get_value(self):
        return self.value

    # returns move with highest value
    def max_value(self, board, depth):

        self.num_calls += 1

        # print(depth)
        # game over
        if board.is_game_over():
            return (self.eval(board), None)

        # cutoff limit reached
        if depth >= self.depth_limit:
            return (self.eval(board), None)
  
        v = -math.inf

        actions = list(board.legal_moves)   # all possible children nodes
        random.shuffle(actions)

        for a in actions:   
            board.push(a)

            (v2, a2) = self.min_value(board, depth + 1)
            if v2 > v:  # store move with highest value
                (v, move) = (v2, a)

            board.pop()
        
        return (v, move)


    # returns move with min value
    def min_value(self, board, depth):

        self.num_calls += 1
        # print(depth)

        if board.is_game_over():
            return (self.eval(board), None)
        
        # cutoff limit reached
        if depth >= self.depth_limit:
            return (self.eval(board), None)
    
        v = math.inf

        # loop through all possible legal next moves
        actions = list(board.legal_moves)
        random.shuffle(actions)
        # print(actions)
        for a in actions:

            board.push(a)
            (v2, a2) = self.max_value(board, depth + 1)

            if v2 < v:
                (v, move) = (v2, a) # store move with min value
            board.pop()
        return (v, move)



    # evaluation function for status of chess game
    def eval(self, board):

        if board.is_checkmate():    # checkmate
            
            if board.turn == self.max_player:   # opponent won
                return -100
            else:
                return 100  # opponent lost
        
        elif board.is_stalemate():  # stalemate
            return 0

        elif board.is_insufficient_material() :
            return 0
        else:
            score = 0

            # loop through all chess pieces
            for i in range(1, 7):
                score += i * len(board.pieces(i, self.max_player))   # add your pieces
                score -= i * len(board.pieces(i, not self.max_player))    # subtract opponent pieces
        
            return score
    
    