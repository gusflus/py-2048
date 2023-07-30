import pygame
from Board import Board
from AITools import AITools

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
running = True
dt = 0

pressed_up = False
pressed_down = False
pressed_left = False
pressed_right = False
pressed_r = False

board = Board()
board._generate_new_tile()

totalScore = 0
resets = 0

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

moveMaker = AITools()

games = 15

while running and resets < games:

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

    directions = ["Up", "Down", "Left", "Right", "Reset"]
    suggestion = directions[moveMaker.getMove(board)]

    suggestionText = font.render("Suggestion: " + suggestion, True, (0, 0, 0))
    suggestionRect = suggestionText.get_rect()
    suggestionRect.center = (3*screen.get_width() / 4, 100)
    screen.blit(suggestionText, suggestionRect)

    gameText = font.render("Game: " + str(resets + 1) + "/" + str(games), True, (0, 0, 0))
    gameRect = gameText.get_rect()
    gameRect.center = ((screen.get_width() / 4) - 40, 60)
    screen.blit(gameText, gameRect)

    # pygame.draw.text(screen, "Score: 0", (25, 25))
    pygame.draw.rect(screen, (148, 148, 148), pygame.Rect(25, 125, 450, 450))
    for i in range(4):
        for j in range(4):
            draw_tile(i, j, board.state[i][j])
            # print('[' + str(i) + '][' + str(j) + ']: ' + str(board.state[i][j]))

    keys = pygame.key.get_pressed()

    if suggestion == "Up":
        board.slide_up() and board._generate_new_tile()
    elif suggestion == "Down":
        board.slide_down() and board._generate_new_tile()
    elif suggestion == "Left":
        board.slide_left() and board._generate_new_tile()
    elif suggestion == "Right":
        board.slide_right() and board._generate_new_tile()
    elif suggestion == "Reset":
        resets += 1
        totalScore += board.score
        board.reset()
        board._generate_new_tile()


    if not pressed_r and keys[pygame.K_r]:
        board.reset()
        board._generate_new_tile()
        pressed_r = True
    elif not keys[pygame.K_r]:
        pressed_r = False

    pygame.display.flip()

    dt = clock.tick(60) / 1000

print(str(games) + " Game Average Score: " + str(totalScore / resets))

pygame.quit()