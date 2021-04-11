import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

font2 = pygame.font.SysFont('Verdana', 60)
game_over = font2.render("GAME OVER", True, (255, 0, 0))

image = pygame.image.load('road.png')
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play()

SCORE = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coinenemy.png')
        self.surf = pygame.Surface((90, 90))
        self.rect = self.surf.get_rect(center = (random.randint(90, 510), 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0, 5)
        if(self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(90, 510), 0) 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coinplayer.png')
        self.surf = pygame.Surface((90, 90))
        self.rect = self.surf.get_rect(center = (210, 510))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 600:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 =  Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED = random.randint(1, 5)

    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    scores = font2.render(str(SCORE), True, (255, 255, 0))
    screen.blit(scores, (500, 20))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          screen.fill((255, 255, 255))
          screen.blit(game_over, (130,240))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit() 

    pygame.display.update()
    clock.tick(60)

pygame.quit()