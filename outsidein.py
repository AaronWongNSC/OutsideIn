class OutsideIn:
    def __init__(self, lower = 1, upper = 10, num_tiles = 10):
        import random

        self.board = [ random.randint(lower, upper) for _ in range(num_tiles)]
        self.initboard = self.board
        self.turn = 'P1'
        self.P1_tiles = []
        self.P1_decisions = []
        self.P2_tiles = []
        self.P2_decisions = []

    def left(self, layer):
        if layer > len(self.board):
            return 0
        return self.board[layer]
    
    def right(self, layer):
        if layer > len(self.board):
            return 0
        return self.board[-(layer + 1)]
    
    def take(self, choice):
        if self.turn == 'P1':
            if choice == 'L':
                self.P1_tiles.append(self.left(0))
                self.board = self.board[1:]
            elif choice == 'R':
                self.P1_tiles.append(self.right(0))
                self.board = self.board[:-1]
            self.P1_decisions.append(choice)
            self.turn = 'P2'
        elif self.turn == 'P2':
            if choice == 'L':
                self.P2_tiles.append(self.left(0))
                self.board = self.board[1:]
            elif choice == 'R':
                self.P2_tiles.append(self.right(0))
                self.board = self.board[:-1]
            self.P2_decisions.append(choice)
            self.turn = 'P1'

    def display(self):
        status = self.status()

        print('--------------------')
        if status['Winner'] is not None:
            print('Initial board: {}'.format(status['Initial']))
            print()
            print('P1 Final Score: {}'.format(status['P1_Score']))
            print('P1 Decisions: {}'.format(status['P1_Decisions']))
            print('P1 Tiles: {}'.format(status['P1_Tiles']))
            print()
            print('P2 Final Score: {}'.format(status['P2_Score']))
            print('P2 Decisions: {}'.format(status['P2_Decisions']))
            print('P2 Tiles: {}'.format(status['P2_Tiles']))
            print()
            print('Winner: {}'.format(status['Winner']))

        else:
            print('Current board: {}'.format(status['Current']))
            print('Current Turn: {}'.format(status['Turn']))
            print('P1: {} -- {}'.format(status['P1_Score'], status['P1_Tiles']))
            print('P2: {} -- {}'.format(status['P2_Score'], status['P2_Tiles']))
    
    def status(self):
        if len(self.board) > 0:
            winner = None
        else:
            if sum(self.P1_tiles) > sum(self.P2_tiles):
                winner = 'P1'
            elif sum(self.P1_tiles) < sum(self.P2_tiles):
                winner = 'P2'
            else:
                winner = 'Tie'

        return {
            'Initial': self.initboard,
            'Current': self.board,
            'Turn': self.turn,
            'P1_Score': sum(self.P1_tiles),
            'P1_Tiles': self.P1_tiles,
            'P1_Decisions': self.P1_decisions,
            'P2_Score': sum(self.P2_tiles),
            'P2_Tiles': self.P2_tiles,
            'P2_Decisions': self.P2_decisions,
            'Winner': winner,
        }

def play(Game, strat1, strat2, show = True):
    if show:
        Game.display()
    while len(Game.board) > 0:
        if Game.turn == 'P1':
            Game.take(strat1.strategy(Game))
        elif Game.turn == 'P2':
            Game.take(strat2.strategy(Game))
        if show:
            Game.display()