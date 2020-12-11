import random
from pygame import mixer
import pygame

#initialize game
pygame.init()

#initial setup
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('bcimage.jpg')
pygame.display.set_caption('Egg Catcher')

#player
playerImg = pygame.image.load('basket.png')
playerx = 100
playery = 380
playery_change = 0
playerx_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))
