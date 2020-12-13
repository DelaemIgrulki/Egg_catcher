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
    
def eggCollison():
    if egg_y[i] >= 450:
        return True
    else:
        return False
    
# score display
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 50


# Score display function
def showscore(x, y):
    score_value = font.render('Score : ' + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))

# Game over text
game_font = pygame.font.Font('freesansbold.ttf', 40)
reason_font = pygame.font.Font('freesansbold.ttf', 20)


# function to display game over text
def game_over_text():
    text = game_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(text, (300, 230))
    text1 = reason_font.render('Do not catch black eggs', True, (255, 0, 0))
    screen.blit(text1, (300, 280))


# victory_font
victory_font = pygame.font.Font('freesansbold.ttf', 45)


def game_over2():
    score_value = victory_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(score_value, (300, 230))
    text1 = reason_font.render('Time limit exceeded', True, (255, 0, 0))
    screen.blit(text1, (350, 280))


def victory():
    score_value = victory_font.render('YOU WON', True, (255, 255, 255))
    screen.blit(score_value, (300, 230))


    
