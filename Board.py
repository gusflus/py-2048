import random

class Board:
    def __init__(self):
        self.state = [[0 for _ in range(4)] for _ in range(4)]
        self.score = 0
        self.game_over = False
        self.won = False

    def reset(self):
        self.state = [[0 for _ in range(4)] for _ in range(4)]
        self.score = 0
        self.game_over = False
        self.won = False


    # can you make a function that slides the 2048 board up?


    def slide_up(self):
        move_occurred = False
        for col in range(4):
            for row in range(1, 4):
                if self.state[row][col]:
                    r = row
                    while r > 0:
                        if self.state[r - 1][col] == 0:
                            self.state[r - 1][col] = self.state[r][col]
                            self.state[r][col] = 0
                            r -= 1
                            move_occurred = True
                        elif self.state[r - 1][col] == self.state[r][col]:
                            self.state[r - 1][col] *= 2
                            self.score += self.state[r - 1][col]
                            self.state[r][col] = 0
                            move_occurred = True
                            break
                        else:
                            break
        return move_occurred

    def slide_left(self):
        move_occurred = False
        for row in range(4):
            for col in range(1, 4):
                if self.state[row][col]:
                    c = col
                    while c > 0:
                        if self.state[row][c - 1] == 0:
                            self.state[row][c - 1] = self.state[row][c]
                            self.state[row][c] = 0
                            c -= 1
                            move_occurred = True
                        elif self.state[row][c - 1] == self.state[row][c]:
                            self.state[row][c - 1] *= 2
                            self.score += self.state[row][c - 1]
                            self.state[row][c] = 0
                            move_occurred = True
                            break
                        else:
                            break
        return move_occurred

    def slide_right(self):
        move_occurred = False
        for row in range(4):
            for col in range(2, -1, -1):
                if self.state[row][col]:
                    c = col
                    while c < 3:
                        if self.state[row][c + 1] == 0:
                            self.state[row][c + 1] = self.state[row][c]
                            self.state[row][c] = 0
                            c += 1
                            move_occurred = True
                        elif self.state[row][c + 1] == self.state[row][c]:
                            self.state[row][c + 1] *= 2
                            self.score += self.state[row][c + 1]
                            self.state[row][c] = 0
                            move_occurred = True
                            break
                        else:
                            break
        return move_occurred

    def slide_down(self):
        move_occurred = False
        for col in range(4):
            for row in range(2, -1, -1):
                if self.state[row][col]:
                    r = row
                    while r < 3:
                        if self.state[r + 1][col] == 0:
                            self.state[r + 1][col] = self.state[r][col]
                            self.state[r][col] = 0
                            r += 1
                            move_occurred = True
                        elif self.state[r + 1][col] == self.state[r][col]:
                            self.state[r + 1][col] *= 2
                            self.score += self.state[r + 1][col]
                            self.state[r][col] = 0
                            move_occurred = True
                            break
                        else:
                            break
        return move_occurred

    def _generate_new_tile(self):
        empty_cells = [(i, j) for i in range(len(self.state)) for j in range(len(self.state[i])) if self.state[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.state[i][j] = 2 if random.random() < 0.9 else 4