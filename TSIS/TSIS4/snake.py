import pygame
import random
import json
import psycopg2
from pygame.locals import *

pygame.init()

# ---------------- SCREEN ----------------
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ---------------- DATABASE ----------------
conn = psycopg2.connect(
    dbname="snake_game",
    user="postgres",
    password="admin123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def save_score(username, score, level):
    cursor.execute(
        "INSERT INTO leaderboard (username, score, level) VALUES (%s, %s, %s)",
        (username, score, level)
    )
    conn.commit()

def get_top_scores():
    cursor.execute(
        "SELECT username, score, level, created_at FROM leaderboard ORDER BY score DESC LIMIT 10"
    )
    return cursor.fetchall()

def get_personal_best(username):
    cursor.execute(
        "SELECT MAX(score) FROM leaderboard WHERE username = %s",
        (username,)
    )
    result = cursor.fetchone()[0]
    return result if result else 0

# ---------------- SETTINGS ----------------
def load_settings():
    try:
        with open("settings.json") as f:
            return json.load(f)
    except:
        return {"snake_color":[50,200,50], "grid":True, "sound":True}

def save_settings(settings):
    with open("settings.json","w") as f:
        json.dump(settings,f)

settings = load_settings()

# ---------------- COLORS ----------------
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
POISON_COLOR = (139,0,0)

# ---------------- GLOBAL ----------------
font = pygame.font.SysFont("arial", 20)
state = "menu"
username = ""

# ---------------- UTIL ----------------
def draw_text(text, x, y):
    screen.blit(font.render(text, True, BLACK), (x,y))

def spawn_item(blocked):
    while True:
        x = random.randrange(0, WIDTH, 10)
        y = random.randrange(0, HEIGHT, 10)
        if [x,y] not in blocked:
            return [x,y]

# ---------------- USERNAME INPUT ----------------
def get_username():
    name = ""
    while True:
        screen.fill(WHITE)
        draw_text("Enter Username: " + name, 150, 200)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return ""
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    return name
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

# ---------------- MENU ----------------
def menu_screen():
    global username

    while True:
        screen.fill(WHITE)

        draw_text("SNAKE GAME", 230, 50)
        draw_text("1. Play", 250, 150)
        draw_text("2. Leaderboard", 250, 180)
        draw_text("3. Settings", 250, 210)
        draw_text("4. Quit", 250, 240)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return "quit"

            if event.type == KEYDOWN:
                if event.key == K_1:
                    username = get_username()
                    return "game"
                if event.key == K_2:
                    return "leaderboard"
                if event.key == K_3:
                    return "settings"
                if event.key == K_4:
                    return "quit"

# ---------------- GAME ----------------
def game_loop():
    global state

    segments = [[50,50],[60,50],[70,50]]
    direction = "r"

    score = 0
    level = 1
    speed = 5

    fruit = spawn_item(segments)
    poison = None

    powerup = None
    power_type = None
    power_time = 0
    active_power = None
    shield = False

    obstacles = []

    personal_best = get_personal_best(username)

    food_timer = 120

    running = True

    while running:
        screen.fill(WHITE)

        # grid
        if settings["grid"]:
            for x in range(0, WIDTH, 10):
                pygame.draw.line(screen, (220,220,220), (x,0),(x,HEIGHT))
            for y in range(0, HEIGHT, 10):
                pygame.draw.line(screen, (220,220,220), (0,y),(WIDTH,y))

        # input
        for event in pygame.event.get():
            if event.type == QUIT:
                return "quit"

        keys = pygame.key.get_pressed()
        if keys[K_UP] and direction!="d": direction="u"
        if keys[K_DOWN] and direction!="u": direction="d"
        if keys[K_LEFT] and direction!="r": direction="l"
        if keys[K_RIGHT] and direction!="l": direction="r"

        # move
        x,y = segments[-1]
        if direction=="r": x+=10
        if direction=="l": x-=10
        if direction=="u": y-=10
        if direction=="d": y+=10

        new_head = [x,y]

        # collision
        if x<0 or x>=WIDTH or y<0 or y>=HEIGHT:
            if shield:
                shield=False
            else:
                running=False

        if new_head in segments:
            if shield:
                shield=False
            else:
                running=False

        for o in obstacles:
            if o.collidepoint(x,y):
                running=False

        segments.append(new_head)

        # fruit
        if new_head == fruit:
            score += random.randint(1,3)
            food_timer = 120

            if score % 3 == 0:
                level += 1
                speed += 1

                if level >= 3:
                    obstacles = []
                    for _ in range(level*2):
                        ox,oy = spawn_item(segments)
                        obstacles.append(pygame.Rect(ox,oy,10,10))

            fruit = spawn_item(segments)

        else:
            segments.pop(0)
            food_timer -= 1

        if food_timer <= 0:
            fruit = spawn_item(segments)
            food_timer = 120

        # poison
        if poison is None and random.random()<0.01:
            poison = spawn_item(segments)

        if poison and new_head == poison:
            segments = segments[2:]
            poison = None
            if len(segments)<=1:
                running=False

        # powerup spawn
        if powerup is None and random.random()<0.005:
            powerup = spawn_item(segments)
            power_type = random.choice(["speed","slow","shield"])
            power_time = pygame.time.get_ticks()

        # power pickup
        if powerup and new_head == powerup:
            active_power = power_type
            power_time = pygame.time.get_ticks()
            if active_power=="shield":
                shield=True
            powerup = None

        # power duration
        now = pygame.time.get_ticks()
        current_speed = speed

        if active_power=="speed" and now-power_time<5000:
            current_speed = speed+3
        elif active_power=="slow" and now-power_time<5000:
            current_speed = max(2,speed-2)
        else:
            active_power=None

        # draw snake
        for s in segments:
            pygame.draw.rect(screen, settings["snake_color"], (*s,9,9))

        pygame.draw.rect(screen, (200,120,0), (*fruit,9,9))

        if poison:
            pygame.draw.rect(screen, POISON_COLOR, (*poison,9,9))

        if powerup:
            color = RED if power_type=="speed" else (0,0,255) if power_type=="slow" else (255,215,0)
            pygame.draw.rect(screen, color, (*powerup,9,9))

        for o in obstacles:
            pygame.draw.rect(screen, (100,100,100), o)

        # UI
        draw_text(f"Score: {score}",10,10)
        draw_text(f"Level: {level}",10,30)
        draw_text(f"Best: {personal_best}",10,50)

        pygame.display.flip()
        clock.tick(current_speed)

    save_score(username, score, level)
    return "game_over"

# ---------------- GAME OVER ----------------
def game_over_screen():
    while True:
        screen.fill(WHITE)

        draw_text("GAME OVER", 250,150)
        draw_text("Press R to Retry", 220,200)
        draw_text("Press M for Menu", 220,230)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return "quit"
            if event.type == KEYDOWN:
                if event.key == K_r:
                    return "game"
                if event.key == K_m:
                    return "menu"

# ---------------- LEADERBOARD ----------------
def leaderboard_screen():
    data = get_top_scores()

    while True:
        screen.fill(WHITE)

        draw_text("LEADERBOARD", 220,30)

        y = 80
        for i,row in enumerate(data):
            text = f"{i+1}. {row[0]} - {row[1]} (Lv {row[2]})"
            draw_text(text, 150, y)
            y += 30

        draw_text("Press ESC to return", 180,350)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return "quit"
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "menu"

# ---------------- SETTINGS ----------------
def settings_screen():
    while True:
        screen.fill(WHITE)

        draw_text("SETTINGS", 250,50)
        draw_text("1. Toggle Grid", 200,150)
        draw_text("2. Toggle Sound", 200,180)
        draw_text("3. Random Snake Color", 200,210)
        draw_text("ESC to save & back", 180,300)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return "quit"
            if event.type == KEYDOWN:
                if event.key == K_1:
                    settings["grid"] = not settings["grid"]
                if event.key == K_2:
                    settings["sound"] = not settings["sound"]
                if event.key == K_3:
                    settings["snake_color"] = [random.randint(0,255) for _ in range(3)]
                if event.key == K_ESCAPE:
                    save_settings(settings)
                    return "menu"

# ---------------- MAIN LOOP ----------------
running = True

while running:
    if state == "menu":
        state = menu_screen()
    elif state == "game":
        state = game_loop()
    elif state == "game_over":
        state = game_over_screen()
    elif state == "leaderboard":
        state = leaderboard_screen()
    elif state == "settings":
        state = settings_screen()
    elif state == "quit":
        running = False

pygame.quit()
