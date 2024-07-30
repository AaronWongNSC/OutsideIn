'''
Greedy algorithm: Pick the larger of the two available cards. If both cards have the
same value, pick one at random.
'''

def strategy(Game):
    import random

    L0 = Game.left(0)
    R0 = Game.right(0)
    
    if L0 > R0:
        return 'L'
    
    if R0 > L0:
        return 'R'
    
    return random.choice(['L', 'R'])