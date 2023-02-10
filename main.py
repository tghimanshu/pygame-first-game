import sys
import pygame

# initialize PyGame
pygame.init()
clock = pygame.time.Clock()

# Base Variables
width, height = 480, 360
x, y = 150, 5
velocity = 2
jumpVelocity = 6
black = 0, 0, 0
white = 255, 255, 255
pipeX = width
score = 0
font = pygame.font.SysFont('Serif', 2)
text = font.render(str("yo"), True, white, black)
textRect = text.get_rect()
textRect.x = 0
textRect.y = 0

# creating the basic screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("First PyGame")


# game loop
running = True
while running:
    # For closing the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # User Input
    key = pygame.key.get_pressed()
    # Basic 4 Directional Movements
    if key[pygame.K_UP]:
        y -= velocity
        # ball.move(x, y)
    if key[pygame.K_DOWN]:
        y += velocity
        # ball.move(x, y)
    if key[pygame.K_LEFT]:
        x -= velocity
        # ball.move(x, y)
    if key[pygame.K_RIGHT]:
        x += velocity
        # ball.move(x, y)
    if key[pygame.K_SPACE]:
        y -= jumpVelocity

    y += velocity
    # Scene creation
    # fill screen
    screen.fill(black)
    # obstacles
    pipe_1 = pygame.draw.rect(screen, white, pygame.Rect(pipeX, 0, 40, 100))
    pipe_2 = pygame.draw.rect(screen, white, pygame.Rect(pipeX, 250, 40, 100))
    pipeX -= 2
    if pipeX < -40:
        pipeX = width

    # player
    ball = pygame.draw.circle(screen, white, (x, y), 5)
    if ball.collidelistall([pipe_1, pipe_2]):
        pipeX = width
        score = 0
        y = 5
    if pipe_1.x == 100:
        print(score)
        score += 1

    # update
    pygame.display.update()

    clock.tick(60)
