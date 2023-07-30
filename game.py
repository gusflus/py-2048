import pygame
import Board

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
running = True
dt = 0

board = Board()

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

def draw_tile(x, y, value):
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

    # pygame.draw.text(screen, "Score: 0", (25, 25))
    pygame.draw.rect(screen, (148, 148, 148), pygame.Rect(25, 125, 450, 450))
    for i in range(4):
        for j in range(4):
            draw_tile(i, j, board.state[i][j])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()