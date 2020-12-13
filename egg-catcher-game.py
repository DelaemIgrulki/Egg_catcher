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
playery = 430
playery_change = 0
playerx_change = 0

#player function
def player(x, y):
    screen.blit(playerImg, (x, y))
    
#eggs
crackImg = pygame.image.load('yellow crack.png')
crackImg = pygame.image.load('white crack.png')
crackImg = pygame.image.load('black crack.png')

eggImg = [
    pygame.image.load('yellow egg.png'),
    pygame.image.load('white egg.png'),
    pygame.image.load('yellow egg.png'),
    pygame.image.load('black egg.png')
]

egg_x = []
egg_y = []
eggy_y_change = []
number_of_eggs = 4

for i in range(number_of_eggs):
    egg_x.append(random.randint(0, 570))
    egg_y.append(random.randint(0, 100))
    eggy_y_change.append(4)

# Egg function
def egg(x, y, i):
    screen.blit(eggImg[i], (x, y))
    
