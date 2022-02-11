# Jason Chen
# Chess AI

'''
Alpha Beta with special openings
'''

import chess
import math
import random
import Openings

class AlphaBetaAI():
    def __init__(self, depth_limit):
        self.depth_limit = depth_limit
        self.num_calls = 0

        self.special_opening = True


        self.opening_num = random.randint(0, len(Openings.openings)-1)
        self.opening = Openings.openings[self.opening_num]  # opening list
        self.opening_name = Openings.openings_dict[self.opening_num]
        self.opening_index = 0


    # returns optimal move
    def choose_move(self, board):
        self.max_player = board.turn

        tup = (None, None)

        if self.special_opening:
            # special opening for white player
            if self.max_player and self.opening_index < len(self.opening):

                print("Playing: ", self.opening_name, "opening")

                opening_move = chess.Move.from_uci(self.opening[self.opening_index])
                self.opening_index += 2
                tup = (0, opening_move)            
                    
            elif not self.max_player and self.opening_index+1 < len(self.opening):  # black player
                
                print("Playing: ", self.opening_name, "opening")

                opening_move = chess.Move.from_uci(self.opening[self.opening_index+1])
                self.opening_index += 2
                tup = (0, opening_move)
            
            else:   # special opening done

                tup = self.max_value(board, 0, -math.inf, math.inf)

        else:

            tup = self.max_value(board, 0, -math.inf, math.inf)

        

        move = tup[1]
        print("move", move)

        #print("Value: " + str(value))
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
