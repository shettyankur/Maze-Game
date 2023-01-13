import pygame
from pygame import *

pygame.init()

size = (450, 450)

select1 = pygame.image.load("resources/select1.png")
select2 = pygame.image.load("resources/select2.png")
select1b = pygame.image.load("resources/select1b.png")
select2b = pygame.image.load("resources/select2b.png")

cadown = pygame.image.load("resources/ca-sprites/ca_down.png")
caleft = pygame.image.load("resources/ca-sprites/ca_left.png")
caright = pygame.image.load("resources/ca-sprites/ca_right.png")
caup = pygame.image.load("resources/ca-sprites/ca_up.png")
cawin1 = pygame.image.load("resources/ca-sprites/ca_win1.png")
cawin2 = pygame.image.load("resources/ca-sprites/ca_win2.png")
cawin3 = pygame.image.load("resources/ca-sprites/ca_win3.png")
cawin4 = pygame.image.load("resources/ca-sprites/ca_win4.png")

start = pygame.image.load("resources/start.png")
brick = pygame.image.load("resources/brick.png")
end = pygame.image.load("resources/end.png")

home = pygame.image.load("resources/home.png")
background = pygame.image.load("resources/background.jpg")

success = pygame.image.load("resources/success.png")

icon = pygame.image.load("resources/icon.png")

confirmsound = pygame.mixer.Sound("resources/sounds/confirm.wav")
wonsound = pygame.mixer.Sound("resources/sounds/won.wav")