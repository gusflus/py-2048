import pygame
from Board import Board
from enum import Enum

pygame.init()
titleFont = pygame.font.Font('freesansbold.ttf', 46)
font = pygame.font.Font('freesansbold.ttf', 28)

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

TILE_COLORS = {
    0: (199, 199, 199),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

TICKRATE = 40

class Game2048AI:
    
    def __init__(self):
        self.display = pygame.display.set_mode((500, 600))
        pygame.display.set_caption("2048 AI")
        self.clock = pygame.time.Clock()

        self.board = Board()
        self.reset()

    def reset(self):
        self.board.reset()

    def play_step(self, action):
        
        prevScore = self.board.score
        prevBoard = self.board.state

        # 1. handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 2. move
        self._move(action)

        # 3. check if game over
        reward = 0
        game_over = False
        if self.board.is_deadlocked():
            game_over = True
            reward = -10
            return reward, game_over, self.board.score
        
        # 4. check if won
        if self.board.is_won():
            game_over = True
            reward = 10
        
        # 5. check if score increased
        if self.board.score > prevScore:
            reward = 1
        
        # 6. check if board was moved
        if self.board.state != prevBoard:
            reward = 0.05
            self.board._generate_new_tile()

        # 7. update ui and time

        self._update_ui()
        self.clock.tick(TICKRATE)

        return reward, game_over, self.board.score

    def _update_ui(self):
        
        self.display.fill((199, 199, 199))
        title = titleFont.render("2048", True, (0, 0, 0))
        titleRect = title.get_rect()
        titleRect.center = (self.display.get_width() / 2, 55)
        self.display.blit(title, titleRect)

        text = font.render("Score: " + str(self.board.score), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (3 * self.display.get_width() / 4 + 10, 60)
        self.display.blit(text, textRect)

        pygame.draw.rect(self.display, (148, 148, 148), pygame.Rect(25, 125, 450, 450))
        for i in range(4):
            for j in range(4):
                self._draw_tile(i, j, self.board.state[i][j])

        pygame.display.flip()

    def _draw_tile(self, y, x, value):
        pygame.draw.rect(self.display, (199, 199, 199), pygame.Rect(35 + 110 * x, 135 + 110 * y, 100, 100))
        if value != 0:
            pygame.draw.rect(self.display, TILE_COLORS[value], pygame.Rect(35 + 110 * x, 135 + 110 * y, 100, 100))
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(str(value), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (35 + 110 * x + 50, 135 + 110 * y + 50)
            self.display.blit(text, textRect)

    def _move(self, action):
        if action == Direction.UP:
            self.board.slide_up()
        elif action == Direction.DOWN:
            self.board.slide_down()
        elif action == Direction.LEFT:
            self.board.slide_left()
        elif action == Direction.RIGHT:
            self.board.slide_right()
        

        

    