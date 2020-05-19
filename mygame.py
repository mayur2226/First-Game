import pygame
import random
WIDTH=500
HEIGHT=500
FPS=40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
isJump = False
jumpCount=10
score=0
lives=3

clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
font_name=pygame.font.match_font("arial")
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font('Stabillo Medium.ttf',32)
    text_surface=font.render(text,True,BLACK)
    text_rect=text_surface.get_rect()
    text_rect.center=(x,y)
    surf.blit(text_surface,text_rect)
class backg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('back.png').convert()
        self.image.set_colorkey((0,0,0),pygame.RLEACCEL)
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=450

    def update(self):
        self.rect.x-=10


class backg1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('back.png').convert()
        self.image.set_colorkey((135,205,250),pygame.RLEACCEL)
        self.rect=self.image.get_rect()
        self.rect.x=500
        self.rect.y=450

    def update(self):
        self.rect.x-=10


class Mobs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sss.png').convert()
        self.image.set_colorkey((135,205,250),pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y= random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y= random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('L2E.png').convert()
        self.image.set_colorkey((0,0,0),pygame.RLEACCEL)
        self.rect = self.image.get_rect(center=(random.randint(500 + 20, 500 + 100),
                random.randint(0, 500),
                )
            )
        self.rect.centerx = ((HEIGHT / 2)+(225))
        self.rect.bottom =(HEIGHT - 50)    
        self.speed = random.randint(5, 6)
       
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
           

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.image.load('cc.png').convert()
        self.image.set_colorkey((0,0,0),pygame.RLEACCEL)
        self.rect = self.image.get_rect(center=(random.randint(500 + 20, 500 + 100),
                random.randint(0, 500),
                )
            )
        self.rect.centerx = ((HEIGHT / 2)+200)
        self.rect.bottom =(HEIGHT - 180)    
        self.speed = random.randint(5, 6)
        
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('R12.png').convert()
        self.image.set_colorkey((0,0,0),pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.img=[]
        self.img.append(pygame.image.load('R2.png'))
        self.img.append(pygame.image.load('R3.png'))
        self.img.append(pygame.image.load('R4.png'))
        self.img.append(pygame.image.load('R5.png'))
        self.index=0
        self.im=self.img[self.index]
        self.lives= lives
 
        self.isJump=isJump
        self.score=score

        self.rect.centery = WIDTH / 2
        self.rect.bottom = HEIGHT - 50
        self.jumpCount=jumpCount
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
         

        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def update1(self):        
        self.index += 1
        if self.index > len(self.img):
            self.index = 0
        self.im=self.img[self.index]




all_sprites = pygame.sprite.Group()
player = Player()
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,2500)
ADDCOIN = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCOIN,2500)
enemy=Enemy()
coins=Coins()
backg=backg()
backg1=backg1()
mob=Mobs()
all_sprites.add(player,enemy,coins,backg,backg1,mob)
enemies= pygame.sprite.Group(enemy)
players= pygame.sprite.Group(player)
coin=pygame.sprite.Group(coins)
backgs=pygame.sprite.Group(backg)
backg1s=pygame.sprite.Group(backg1)
mobs=pygame.sprite.Group()
for i in range(8):
    m=Mobs()
    all_sprites.add(m)
    mobs.add(m)
for i in range(8):
    c=Coins()
    all_sprites.add(c)
    coin.add(c)




running = True
while running:
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False    
        elif event.type == ADDENEMY:
            new_enemy=Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCOIN:
            new_coin=Coins()
            coin.add(new_coin)
            all_sprites.add(new_coin)    
        
   
    keystate = pygame.key.get_pressed()
    if not(player.isJump):
        if keystate[pygame.K_UP]:
            player.isJump = True
    if player.isJump:
        if player.jumpCount >= -10:
            player.rect.y -= ((player.jumpCount * abs(player.jumpCount)) * 0.5)
            player.jumpCount -= 1
        else: 
            player.rect.y = HEIGHT -115
            player.jumpCount=10
            player.isJump = False
    hits = pygame.sprite.spritecollide(player, enemies, False)
    
    if hits:
        running=False
    
    hits1 = pygame.sprite.spritecollide(player, coin, True)
    if hits1:
        player.score += 1
        print(player.score)
        running = True    
    if backg.rect.right<=0:
        backg.rect.x=500
    if backg1.rect.right<=0:
        backg1.rect.x=500
    all_sprites.update()
    screen.fill((135,205,250))
    
    all_sprites.draw(screen)
    draw_text(screen, "Score"+":"+str(player.score), 28, 70, 20)
    pygame.display.flip()

pygame.quit()    