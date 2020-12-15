import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('bcimage.jpg')
pygame.display.set_caption('Egg Catcher')

playerImg = pygame.image.load('basket.png')
playerx = 100
playery = 430
playery_change = 0
playerx_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))
    
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

def egg(x, y, i):
    screen.blit(eggImg[i], (x, y))
    
def eggCollison():
    if egg_y[i] >= 450:
        return True
    else:
        return False
    
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 50


def showscore(x, y):
    score_value = font.render('Score : ' + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))

game_font = pygame.font.Font('freesansbold.ttf', 40)
reason_font = pygame.font.Font('freesansbold.ttf', 20)


def game_over_text():
    text = game_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(text, (300, 230))
    text1 = reason_font.render('Do not catch black eggs', True, (255, 0, 0))
    screen.blit(text1, (300, 280))


victory_font = pygame.font.Font('freesansbold.ttf', 45)


def game_over2():
    score_value = victory_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(score_value, (300, 230))
    text1 = reason_font.render('Time limit exceeded', True, (255, 0, 0))
    screen.blit(text1, (350, 280))


def victory():
    score_value = victory_font.render('YOU WON', True, (255, 255, 255))
    screen.blit(score_value, (300, 230))

pause_font = pygame.font.Font('freesansbold.ttf', 40)


def pause_text():
    text = pause_font.render('GAME PAUSED', True, (255, 255, 255))
    screen.blit(text, (300, 230))


time_font = pygame.font.Font('freesansbold.ttf', 32)

sec = 30

def showtimer():
    score_value = time_font.render('Time Left : ' + str(int(sec)), True, (255, 255, 255))
    screen.blit(score_value, (700, 20))


def showlevel():
    score_value = font.render('Level :', True, (255, 255, 255))
    screen.blit(score_value, (700, 60))
    score_value = font.render('             Easy', True, (0, 255, 0))
    screen.blit(score_value, (700, 60))
    score_value = font.render('Target : 35', True, (255, 255, 255))
    screen.blit(score_value, (700, 100))
    
running = True
pause = False
Exit = False
target = 35

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change -= 10
            if event.key == pygame.K_RIGHT:
                playerx_change += 10

            if event.key == pygame.K_SPACE:
                Exit = False
                score = 0
                for j in range(3):
                    egg_x[j] = random.randint(0, 570)
                    egg_y[j] = random.randint(0, 100)
            
            if event.key == pygame.K_UP:
                if pause:
                    pause = False
                else:
                    pause = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    
    if playerx <= -30:
        playerx = -30
    elif playerx > 700:
        playerx = 700

    for i in range(number_of_eggs):
        if egg_y[i] >= 600:
            egg_x[i] = random.randint(0, 570)
            egg_y[i] = random.randint(0, 100)

        egg_y[i] += eggy_y_change[i]
        if egg_y[i] <= 450:
            egg(egg_x[i], egg_y[i], i)
                
