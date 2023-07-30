class Board:
    def __init__(self):
        self.state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.game_over = False
        self.won = False
