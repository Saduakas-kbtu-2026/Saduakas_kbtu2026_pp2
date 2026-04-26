import pygame
import random
from pygame.locals import *

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))

# Colors
WHITE = (255, 255, 255)
GREEN = (50, 200, 50)
RED = (255, 0, 0)
FRUIT_COLOR = (200, 120, 0)

# Snake setup (list of segments)
segments = [[50,50],[60,50],[70,50],[80,50]]
direction = "r"


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
        x = random.randrange(0, 600, 10)
        y = random.randrange(0, 400, 10)

        # Check not on snake
        if [x, y] in segments:
            continue

        # Check not on wall
        if wall_rect.collidepoint(x, y):
            continue

        return [x, y]

fruit = spawn_fruit()
max_fruit_weight = 3# varies from 1 to 3 | different weight
max_food_timer = 120
food_timer = 1

running = True
clock = pygame.time.Clock()

while running:

    #quit func
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    #player input
    keys = pygame.key.get_pressed()

    if keys[K_UP] and direction != "d":
        direction = "u"
    elif keys[K_DOWN] and direction != "u":
        direction = "d"
    elif keys[K_LEFT] and direction != "r":
        direction = "l"
    elif keys[K_RIGHT] and direction != "l":
        direction = "r"

    #snake movement
    head_x, head_y = segments[-1]

    if direction == "r":
        head_x += 10
    elif direction == "l":
        head_x -= 10
    elif direction == "u":
        head_y -= 10
    elif direction == "d":
        head_y += 10

    new_head = [head_x, head_y]

    #collisions

    # Border collision
    if head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 400:
        running = False

    # Self collision
    if new_head in segments:
        running = False

    # Wall collision
    if wall_rect.collidepoint(head_x, head_y):
        running = False

    segments.append(new_head)

    #fruit logic
    if new_head == fruit:
        score += random.randint(1, max_fruit_weight) # from 1 to 3
        #load_sfx("gc.wav").play()
        food_timer = max_food_timer

        # Level up every 3 foods
        if score % 3 == 0:
            level += 1
            speed += 1  # increase speed

        fruit = spawn_fruit()
    else:
        food_timer -= 1
        segments.pop(0)  # remove tail if not eating

    if food_timer ==0:
        fruit = spawn_fruit() 

    #rendering/ drawing
    screen.fill(WHITE)

    #draws the timer bar
    pygame.draw.rect(screen, (0,0,0),(0,0, food_timer*5,10))

    # Draw wall
    pygame.draw.rect(screen, (100,100,100), wall_rect)

    # Draw snake
    for segment in segments:
        pygame.draw.rect(screen, GREEN, (*segment, 9, 9))

    # Draw fruit
    pygame.draw.rect(screen, FRUIT_COLOR, (*fruit, 9, 9))

    #draw text
    font = pygame.font.SysFont("times new roman", 20)

    
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    level_text = font.render(f"Level: {level}", True, (0,0,0))

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.flip()

    #snake speed
    clock.tick(speed)

pygame.quit()
