# Jason Chen
# CS76 Fall 21
# PA3

import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IDS_MinimaxAI import IDS_MinimaxAI

import time
import sys


# player1 = HumanPlayer()
player1 = MinimaxAI(2)

player2 = AlphaBetaAI(2)
# player1 = IDS_MinimaxAI(1)
# player2 = IDS_MinimaxAI(2)
# player1 = RandomAI()

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()
    print(player2.num_calls)
    # time.sleep(1)

print(game)
print(player2.num_calls)
print(game.board.outcome())


#print(hash(str(game.board)))
