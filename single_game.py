'''
Run a single game of Outside In with the indicated strategies
'''

import outsidein as OI

import greedy_strat as strat1
import random_strat as strat2

Game = OI.OutsideIn()
play = OI.play(Game, strat1, strat2)