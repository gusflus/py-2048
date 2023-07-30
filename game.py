import pygame
from Board import Board

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
running = True
dt = 0

pressed_up = False
pressed_down = False
pressed_left = False
pressed_right = False

board = Board()
board._generate_new_tile()

tile_colors = {
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

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def draw_tile(y, x, value):
    pygame.draw.rect(screen, (199, 199, 199), pygame.Rect(35 + 110 * x, 135 + 110 * y, 100, 100))
    if value != 0:
        pygame.draw.rect(screen, tile_colors[value], pygame.Rect(35 + 110 * x, 135 + 110 * y, 100, 100))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(value), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (35 + 110 * x + 50, 135 + 110 * y + 50)
        screen.blit(text, textRect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((199, 199, 199))

    titleFont = pygame.font.Font('freesansbold.ttf', 46)
    title = titleFont.render("2048", True, (0, 0, 0))
    titleRect = title.get_rect()
    titleRect.center = (screen.get_width() / 2, 55)
    screen.blit(title, titleRect)
    
    font = pygame.font.Font('freesansbold.ttf', 28)
    text = font.render("Score: " + str(board.score), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (3 * screen.get_width() / 4 + 10, 60)
    screen.blit(text, textRect)

    # pygame.draw.text(screen, "Score: 0", (25, 25))
    pygame.draw.rect(screen, (148, 148, 148), pygame.Rect(25, 125, 450, 450))
    for i in range(4):
        for j in range(4):
            draw_tile(i, j, board.state[i][j])
            # print('[' + str(i) + '][' + str(j) + ']: ' + str(board.state[i][j]))

    keys = pygame.key.get_pressed()

    if not pressed_up and keys[pygame.K_w]:
        board.slide_up() and board._generate_new_tile()
        pressed_up = True
    elif not keys[pygame.K_w]:
        pressed_up = False

    if not pressed_down and keys[pygame.K_s]:
        board.slide_down() and board._generate_new_tile()
        pressed_down = True
    elif not keys[pygame.K_s]:
        pressed_down = False

    if not pressed_left and keys[pygame.K_a]:
        board.slide_left() and board._generate_new_tile()
        pressed_left = True
    elif not keys[pygame.K_a]:
        pressed_left = False

    if not pressed_right and keys[pygame.K_d]:
        board.slide_right() and board._generate_new_tile()
        pressed_right = True
    elif not keys[pygame.K_d]:
        pressed_right = False

    if keys[pygame.K_r]:
        board.reset()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()