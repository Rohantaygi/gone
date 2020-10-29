import pygame
import random
import time

pygame.init()

#screen-
height = 500
width = 500
game_screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Flyer")

#colors-
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

#game variables-
ground_x = 0
ground_y = 450
man_x = 0
man_y = 100
velocity_x = 0
velocity_y = 1
enemy_x = 450
enemy_y = random.randint(0, 200)
enemy_velocity_x = -0.2
time = 0


game_over = False

font = pygame.font.SysFont(None, 45)
font2 = pygame.font.SysFont(None, 25)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_screen.blit(screen_text, [x,y])

def text_screen2(text, color, x, y):
    screen_text = font2.render(text, True, color)
    game_screen.blit(screen_text, [x,y])

def exit_screen():
    game_over = False
    while not game_over:
        game_screen.fill(green)
        text_screen("OPS! you lost", red, 190, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
        pygame.display.update()

def help_desk():
    game_over = False
    while not game_over:
        game_screen.fill(green)
        text_screen2("you have to fly and don't touch the acid and wall!!", black, 50, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
        pygame.display.update()


while not game_over:
    time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x =   0.5
                velocity_y = 0
            
            if event.key == pygame.K_LEFT:
                velocity_x =   -0.5
                velocity_y = 0
            
            if event.key == pygame.K_UP:
                velocity_y =  -0.2

            if event.key == pygame.K_DOWN:
                velocity_y =  0.2   
            
            if event.key == pygame.K_F1:
                help_desk()
    
    man_x = man_x+ velocity_x
    man_y = man_y+ velocity_y
    enemy_x = enemy_x + enemy_velocity_x
    
    if abs(man_x - ground_x)<1000 and abs(man_y - ground_y)<55:
        exit_screen()

    if abs(man_x) > abs(width):
        exit_screen()
    
    if abs(man_y) > abs(height):
        exit_screen()

    game_screen.fill(blue)
    pygame.draw.rect(game_screen, green, (ground_x, ground_y, 1000, 60))
    pygame.draw.rect(game_screen, black, (man_x, man_y, 30, 30))
    pygame.draw.rect(game_screen, red, (enemy_x, enemy_y, 40, 40))
    text_screen("Fly for your life", white, 10, 0)
    text_screen("press F1 for help", black, 0, 450)
    pygame.display.update()


    
