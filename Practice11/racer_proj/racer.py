import pygame
from pygame.locals import *
import random

pygame.init()

screen = pygame.display.set_mode((300,600))

class player_car(pygame.sprite.Sprite):
    def __init__(self,path="player_car.png"):
        super().__init__()
        imported_image = pygame.image.load(path)
        self.image = pygame.transform.scale(imported_image,(75,150))
        self.rect = self.image.get_rect()
        self.rect.center = (47,525)
    
    def move(self, move_speed):
        button = pygame.key.get_pressed()

        if button[K_a]:
            self.rect.centerx -= 3
        elif button[K_d]:
            self.rect.centerx += 3
        # boundary condition for the position of the car
        if self.rect.centerx < 47:
            self.rect.centerx = 47
        if self.rect.centerx > 253:
            self.rect.centerx = 253

    
class opposing_car(pygame.sprite.Sprite):
    def __init__(self,path = "enemy_car.png"):
        super().__init__()
        imported_image = pygame.image.load(path)
        self.image = pygame.transform.scale(imported_image,(75,150))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(47,253),75)
        self.speed = 5
        self.score = 0
    
    def move(self, move_speed):
        new_speed = self.speed + move_speed
        self.rect.centery += new_speed

        if self.rect.centery > 675:
            self.rect.centery = -75
            self.rect.centerx = random.randint(47,253)
            self.score += 10

class Coin(pygame.sprite.Sprite):
    def __init__(self, path="coin.png"):
        super().__init__()
        img = pygame.image.load(path)
        self.image = pygame.transform.scale(img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(47, 253), -40)
        self.speed = 4

    def move(self, coin_speed):
        new_speed = self.speed + coin_speed
        self.rect.centery += new_speed

        # Respawn when off screen
        if self.rect.centery > 650:
            self.rect.centery = -40
            self.rect.centerx = random.randint(47, 253)
            



class background_loading:# loads background
    def __init__(self, path = "road2.png"):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(300,300))
        self.image = pygame.transform.rotate(self.image, 90)
        rect1 = self.image.get_rect()
        rect2 = self.image.get_rect()
        rect2.centery += 300
        rect3 = self.image.get_rect()
        rect3.centery += 600
        self.rectangles = []
        self.rectangles.append(rect1)
        self.rectangles.append(rect2)
        self.rectangles.append(rect3)
        
    
    def draw(self):
        for rectangle in self.rectangles:
            screen.blit(self.image,rectangle)
    
    def move(self, speed):
        for rectangle in self.rectangles:
            rectangle.centery+=(2+speed)
            if rectangle.centery>750:
                rectangle.centery = -150


#loads entinties
player = player_car()
opponent = opposing_car()
coins = pygame.sprite.Group()

# spawn a few coins
for _ in range(3):
    coins.add(Coin())

coin_count = 0
font = pygame.font.SysFont("arial", 24)

cars = pygame.sprite.Group()
cars.add(player)
cars.add(opponent)

opponents = pygame.sprite.Group()
opponents.add(opponent)

honk_sound = pygame.mixer.Sound("honk.mp3")

running = True



background = background_loading()

coin_counter = 0
speed = 1

while running: #main gameloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    background.move(speed)
    background.draw()

    
    #initiates all car entities/objects
    for car in cars:
        screen.blit(car.image,car.rect)
        car.move(speed) #gives scaling speed to cars

    #init all coins obj
    for coin in coins:
        screen.blit(coin.image, coin.rect)
        coin.move(random.randint(-1,1)+speed) #random speed (weight)

    #check collision between player and enemies
    if pygame.sprite.spritecollideany(player,opponents):
        screen.fill((125,50,50))
        font = pygame.font.SysFont("open dyslexic",18)
        text = font.render("Your final score is: " + str(opponent.score),True,(0,255,255))
        rect = text.get_rect()
        rect.center = (150,300)
        
        #gameover
        honk_sound.play()
        screen.blit(text,rect)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    
    #check collision between player and coins
    collected = pygame.sprite.spritecollide(player, coins, False)

    for coin in collected:
        coin_count += 1
        coin.rect.centery = -40
        coin.rect.centerx = random.randint(47, 253)

        if coin_count % 3 == 0:
            speed += 1  # increase speed
        
    
    #coin counter
    text = font.render(f"Coins: {coin_count}", True, (255, 255, 0))
    text_rect = text.get_rect(topright=(290, 10))
    screen.blit(text, text_rect)
    
    pygame.time.Clock().tick(60)
    pygame.display.flip()
 
