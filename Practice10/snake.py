import pygame
import random
from pygame.locals import *

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
GREEN = (50, 200, 50)
RED = (255, 0, 0)
FRUIT_COLOR = (200, 120, 0)

# Snake setup (list of segments)
segments = [[50,50],[60,50],[70,50],[80,50]]
direction = "r"

# Grid size (important for alignment)
STEP = 10

# Score & level
score = 0
level = 1

# Speed (will increase)
speed = 5

# Wall (simple rectangular obstacle)
wall_rect = pygame.Rect(200, 200, 100, 20)

# Image cache
image_lib = {}
def load_image(path):
    if path not in image_lib:
        image_lib[path] = pygame.image.load(path)
    return image_lib[path]

# Sound cache
sfx_lib = {}
def load_sfx(path):
    if path not in sfx_lib:
        sfx_lib[path] = pygame.mixer.Sound(path)
    return sfx_lib[path]

# Music
#pygame.mixer.music.load("open-source-lab-dreamy-times-358804.mp3")
#pygame.mixer.music.play(-1)

# Function to generate safe fruit
def spawn_fruit():
    while True:
        x = random.randrange(0, WIDTH, STEP)
        y = random.randrange(0, HEIGHT, STEP)

        # Check not on snake
        if [x, y] in segments:
            continue

        # Check not on wall
        if wall_rect.collidepoint(x, y):
            continue

        return [x, y]

fruit = spawn_fruit()

running = True
clock = pygame.time.Clock()

while running:

    # -------- EVENTS --------
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # -------- INPUT --------
    keys = pygame.key.get_pressed()

    if keys[K_UP] and direction != "d":
        direction = "u"
    elif keys[K_DOWN] and direction != "u":
        direction = "d"
    elif keys[K_LEFT] and direction != "r":
        direction = "l"
    elif keys[K_RIGHT] and direction != "l":
        direction = "r"

    # -------- MOVE SNAKE --------
    head_x, head_y = segments[-1]

    if direction == "r":
        head_x += STEP
    elif direction == "l":
        head_x -= STEP
    elif direction == "u":
        head_y -= STEP
    elif direction == "d":
        head_y += STEP

    new_head = [head_x, head_y]

    # -------- COLLISIONS --------

    # Border collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False

    # Self collision
    if new_head in segments:
        running = False

    # Wall collision
    if wall_rect.collidepoint(head_x, head_y):
        running = False

    segments.append(new_head)

    # -------- FOOD --------
    if new_head == fruit:
        score += 1
        #load_sfx("gc.wav").play()

        # Level up every 3 foods
        if score % 3 == 0:
            level += 1
            speed += 1  # increase speed

        fruit = spawn_fruit()
    else:
        segments.pop(0)  # remove tail if not eating

    # -------- DRAW --------
    screen.fill(WHITE)

    # Draw wall
    pygame.draw.rect(screen, (100,100,100), wall_rect)

    # Draw snake
    for segment in segments:
        pygame.draw.rect(screen, GREEN, (*segment, STEP-1, STEP-1))

    # Draw fruit
    pygame.draw.rect(screen, FRUIT_COLOR, (*fruit, STEP-1, STEP-1))

    # -------- UI --------
    font = pygame.font.SysFont("times new roman", 20)

    score_text = font.render(f"Score: {score}", True, (0,0,0))
    level_text = font.render(f"Level: {level}", True, (0,0,0))

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.flip()

    # -------- SPEED CONTROL --------
    clock.tick(speed)

pygame.quit()
