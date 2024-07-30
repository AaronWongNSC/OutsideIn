'''
Challenge match between strategies:
* Increased board length
* 1000 matches with each strategy going first
* Displays final result

'''
board_length = 1000
matches = 1000

import outsidein as OI

import greedy_strat as strat1
import random_strat as strat2

strat1_first = {
    'Wins': 0,
    'Losses': 0,
    'Ties': 0
}

strat2_first = {
    'Wins': 0,
    'Losses': 0,
    'Ties': 0
}

# Strat1 plays first
for _ in range(matches):
    Game = OI.OutsideIn()
    play = OI.play(Game, strat1, strat2, show = False)
    result = Game.status()['Winner']

    if result == 'P1':
        strat1_first['Wins'] += 1
    elif result == 'P2':
        strat1_first['Losses'] += 1
    else:
        strat1_first['Ties'] += 1

# Strat2 plays first
for _ in range(matches):
    Game = OI.OutsideIn()
    play = OI.play(Game, strat2, strat1, show = False)
    result = Game.status()['Winner']

    if result == 'P1':
        strat2_first['Wins'] += 1
    elif result == 'P2':
        strat2_first['Losses'] += 1
    else:
        strat2_first['Ties'] += 1

print('Final Results:')
print('Strat1 First: {Wins} wins, {Losses} losses, {Ties} ties'.format(**strat1_first))
print('Strat2 First: {Wins} wins, {Losses} losses, {Ties} ties'.format(**strat2_first))