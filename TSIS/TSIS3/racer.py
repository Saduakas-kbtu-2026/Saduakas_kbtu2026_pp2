import pygame
import random
import json
import os
from datetime import datetime

pygame.init()

# ---------------- SCREEN ----------------
WIDTH, HEIGHT = 300, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ---------------- FILES ----------------
SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

default_settings = {
    "sound": True,
    "difficulty": 1,
    "car_color": [0, 200, 255]
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return default_settings.copy()

def save_settings():
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    try:
        with open(LEADERBOARD_FILE, "r") as f:
            data = f.read().strip()
            if not data:
                return []
            return json.loads(data)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_score(name, score):
    board = load_leaderboard()

    board.append({"name": name, "score": score})
    board = sorted(board, key=lambda x: x["score"], reverse=True)[:10]

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(board, f, indent=2)

settings = load_settings()

# ---------------- SOUNDS ----------------
#coin_snd = pygame.mixer.Sound("coin.wav") if settings["sound"] else None
crash_snd = pygame.mixer.Sound("honk.mp3")
#power_snd = pygame.mixer.Sound("powerup.wav") if settings["sound"] else None

# ---------------- COLORS ----------------
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (200,50,50)
WINDSHIELD = (180,220,255)
BLACK = (0,0,0)

LANES = [47, 150, 253]

# ---------------- CAR ----------------
def draw_car(x, y, color):
    pygame.draw.rect(screen, BLACK, (x+3, y+20, 7, 30))
    pygame.draw.rect(screen, BLACK, (x+65, y+20, 7, 30))
    pygame.draw.rect(screen, BLACK, (x+3, y+105, 7, 30))
    pygame.draw.rect(screen, BLACK, (x+65, y+105, 7, 30))

    pygame.draw.rect(screen, color, (x+10, y+10, 55, 130))
    pygame.draw.rect(screen, WINDSHIELD, (x+20, y+50, 35, 20))
    pygame.draw.rect(screen, WINDSHIELD, (x+20, y+100, 35, 15))

# ---------------- BACKGROUND ----------------
class Background:
    def __init__(self):
        self.img = pygame.image.load("road3.png")
        self.img = pygame.transform.scale(self.img, (300,300))
        self.y1 = 300
        self.y2 = 0
        self.y3 = -300

    def move(self, speed):
        self.y1 += speed
        self.y2 += speed
        self.y3 += speed
        if self.y1 >= 600: self.y1 = -300
        if self.y2 >= 600: self.y2 = -300
        if self.y3 >= 600: self.y3 = -300

    def draw(self):
        screen.blit(self.img, (0,self.y1))
        screen.blit(self.img, (0,self.y2))
        screen.blit(self.img, (0,self.y3))

# ---------------- PLAYER ----------------
class Player:
    def __init__(self):
        self.x = 150
        self.y = 450
        self.rect = pygame.Rect(self.x,self.y,70,140)
        self.shield = False
        self.lives = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.x -= 4
        if keys[pygame.K_d]: self.x += 4
        self.x = max(0, min(WIDTH-70, self.x))
        self.rect.topleft = (self.x,self.y)

    def draw(self):
        draw_car(self.x,self.y,settings["car_color"])

# ---------------- ENEMY ----------------
class Enemy:
    go_right = False
    def __init__(self, speed):
        self.x = random.choice(LANES)
        if self.x > WIDTH/2: self.go_right = True
        else: self.go_right = False

        self.y = -150
        self.speed = speed + settings["difficulty"]
        self.rect = pygame.Rect(self.x,self.y,70,140)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = -150
            self.x = random.choice(LANES)
        self.rect.topleft = (self.x,self.y)

        if random.randint(-1,1)>= 0:
            if self.go_right:
                self.x += (1-level)
            else:
                self.x -= (1-level)

    def draw(self):
        draw_car(self.x,self.y,RED)
    
    def destroy(self): 
        self.y = -150

# ---------------- COIN ----------------
class Coin:
    def __init__(self):
        self.reset()
        self.rect = pygame.Rect(self.x,self.y,20,20)

    def reset(self):
        self.x = random.choice(LANES)
        self.y = random.randint(-600,0)

    def update(self,speed):
        self.y += speed
        if self.y > HEIGHT:
            self.reset()
        self.rect.topleft = (self.x,self.y)

    def draw(self):
        pygame.draw.circle(screen,YELLOW,(self.x+10,self.y+10),8)

# ---------------- POWERUPS ----------------
class PowerUp:
    def __init__(self):
        self.type = random.choice(["shield","nitro","repair"])
        self.x = random.choice(LANES)
        self.y = random.randint(-800,-200)
        self.rect = pygame.Rect(self.x,self.y,25,25)
        

    def reset(self):
        self.y = random.randint(-600,0)
        self.type = random.choice(["shield","nitro","repair"])

    def update(self,speed):
        self.y += speed
        if self.y > HEIGHT:
            self.y = -800
        self.rect.topleft = (self.x,self.y)

    def draw(self):
        if self.type == "shield":
            color = (0,255,0)
        elif self.type=="repair":
            color = (255,0,0)
        else: color = (0,200,255)
        pygame.draw.rect(screen,color,self.rect)

# ---------------- GAME STATE ----------------
state = "MENU"
menu_index = 0
settings_index = 0

menu = ["Play","Leaderboard","Settings","Quit"]

player_name = ""
typing = False

# ---------------- INIT ----------------
bg = Background()
font = pygame.font.SysFont("arial",20)

def reset_game():
    global player,enemies,coins,powerups,score,speed,level
    player = Player()
    level = 1
    enemies = [Enemy(4)]
    coins = [Coin()]
    powerups = [PowerUp()]
    score = 0
    speed = 4
    

# ---------------- MAIN LOOP ----------------
running = True

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # -------- MENU --------
        if state == "MENU":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu_index = (menu_index-1)%len(menu)
                if event.key == pygame.K_DOWN:
                    menu_index = (menu_index+1)%len(menu)

                if event.key == pygame.K_RETURN:
                    if menu[menu_index]=="Play":
                        player_name = ""
                        state="NAME"
                        typing=True
                    elif menu[menu_index]=="Leaderboard":
                        state="LEADERBOARD"
                    elif menu[menu_index]=="Settings":
                        state="SETTINGS"
                    elif menu[menu_index]=="Quit":
                        running=False

        # --------- leaderboard ----------
        if state == "LEADERBOARD":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    state = "MENU"

        # -------- NAME INPUT --------
        elif state == "NAME":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(player_name.strip()) > 0:
                        reset_game()
                        state = "GAME"
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        # -------- SETTINGS --------
        elif state == "SETTINGS":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    settings_index = (settings_index - 1) % 3

                if event.key == pygame.K_DOWN:
                    settings_index = (settings_index + 1) % 3

                if event.key == pygame.K_RETURN:

                    # TOGGLE SOUND
                    if settings_index == 0:
                        settings["sound"] = not settings["sound"]

                    # CHANGE DIFFICULTY
                    elif settings_index == 1:
                        settings["difficulty"] = (settings["difficulty"] % 3) + 1

                    # RANDOM CAR COLOR
                    elif settings_index == 2:
                        settings["car_color"] = [
                            random.randint(0,255),
                            random.randint(0,255),
                            random.randint(0,255)
                        ]

                if event.key == pygame.K_ESCAPE:
                    save_settings()
                    state = "MENU"

    # ---------------- MENU ----------------
    if state == "MENU":
        for i,m in enumerate(menu):
            c = YELLOW if i==menu_index else WHITE
            screen.blit(font.render(m,True,c),(100,200+i*40))

    # ---------------- NAME ----------------
    elif state == "NAME":
        screen.blit(font.render("Enter Name:",True,WHITE),(80,250))
        screen.blit(font.render(player_name,True,YELLOW),(100,300))

    # ---------------- GAME ----------------
    elif state == "GAME":
        bg.move(speed)
        bg.draw()

        player.update()
        player.draw()
        for e in enemies:
            e.update()
            e.draw()
            if player.rect.colliderect(e.rect):
                if not player.shield:
                    if player.lives > 0:
                        player.lives-=1
                        e.destroy()
                    else:
                        if settings["sound"]:
                            crash_snd.play()
                        save_score(player_name,score)
                        state="MENU"
                else:
                    player.shield = False
        
        for c in coins:
            c.update(speed)
            c.draw()
            if player.rect.colliderect(c.rect):
                #coin_snd and coin_snd.play()
                score += 100
                c.reset()

        for p in powerups:
            p.update(speed)
            p.draw()
            if player.rect.colliderect(p.rect):
                #power_snd and power_snd.play()
                if p.type=="nitro":
                    speed+=2
                elif p.type=="shield":
                    player.shield=True
                elif p.type=="repair":
                    player.lives+=1
                
                p.reset()

        score += 1
        if score // 1000 > level - 1: 
            level +=1
            speed +=1 #add speed for 
            enemies.append(Enemy(4 + level))
        screen.blit(font.render(f"{player_name} Score:{score}",True,WHITE),(10,10))
        screen.blit(font.render(f"{player_name}`s car durablitiy:{player.lives}",True,WHITE),(10,30))
        if player.shield:
            screen.blit(font.render(f"{player_name}`s car is shielded",True,WHITE),(10,50))

    # ---------------- LEADERBOARD ----------------
    elif state=="LEADERBOARD":
        board = load_leaderboard()
        screen.blit(font.render("TOP SCORES",True,YELLOW),(80,50))
        for i,b in enumerate(board):
            t = f"{i+1}. {b['name']} - {b['score']}"
            screen.blit(font.render(t,True,WHITE),(40,120+i*30))

    # ---------------- SETTINGS ----------------
    elif state=="SETTINGS":
        items = [
            f"Sound: {settings['sound']}",
            f"Difficulty: {settings['difficulty']}",
            f"Car Color",
        ]

        for i,it in enumerate(items):
            color = YELLOW if i == settings_index else WHITE
            screen.blit(font.render(it,True,color),(60,200+i*40))

        screen.blit(font.render("ENTER to change | ESC to save", True, WHITE), (20, 450))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()