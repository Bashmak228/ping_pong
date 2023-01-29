from pygame import*
import pygame
from time import sleep
from pygame import Surface
pygame.init()

speed_x = -1
speed_y = 1
speed_run = 1
menu = True
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = sprite.Sprite()
ball.image = image.load("ball.png")
ball.rect = ball.image.get_rect(center = (300,300)) 

player = sprite.Sprite()
player.image = image.load("p1.png")
player.rect = player.image.get_rect(center = (25,300))

player2 = sprite.Sprite()
player2.image = image.load("p2.png")   
player2.rect = player2.image.get_rect(center = (575,300))       

screen = display.set_mode((600,400))
screen.fill((255,150,101))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

fon = image.load("6206870741.jpg ")  

win_width = 600
win_height = 500
display.set_caption("p1.png")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("6206870741.jpg"), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 300

racket1 = Player("p1.png", 30, 200, 4, 50, 150)
racket2 = Player("p2.png", 520, 200, 4, 50, 150)
ball = GameSprite("Ball34.png", 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        
        racket1.update_l()
        racket2.update_r()


        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        if ball.rect.y<=0 or ball.rect.y>=380:        
            speed_y *= -1

        if ball.rect.colliderect(player.rect): 
            #y_speed *= -1
            speed_x -= speed_run
            speed_x *= -1
            s.play()

        if ball.rect.colliderect(player2.rect):     
            speed_x += speed_run
            speed_x *= -1
            s.play()


        if ball.rect.x<=0 :#гол влево
            score2 +=1
            ball.rect.x = 290
            ball.rect.y = 190
            speed_x = 1
        if ball.rect.x>=580: #гол вправо
            speed_x = 1
            score1 +=1
            ball.rect.x = 290
            ball.rect.y = 190

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        screen.fill((255,150,101))
        screen.blit(fon,(0,0))
        screen.blit(player.image,player.rect)
        screen.blit(player2.image,player2.rect)

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)

