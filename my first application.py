import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('julius.mp3')
pygame.mixer.music.play()

screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("money")
bg = pygame.image.load('backdrop.jpg')
bg = pygame.transform.scale(bg, (1000, 650)).convert_alpha()

me = pygame.image.load("me.jpg")
me = pygame.transform.scale(me, (200, 200)).convert_alpha()

bird = pygame.image.load("flappy.png")
bird = pygame.transform.scale(bird, (200, 200)).convert_alpha()

PUBG = pygame.image.load("PUBG.jpg")
PUBG = pygame.transform.scale(PUBG, (200, 200)).convert_alpha()

free = pygame.image.load("free fire.jpg")
free = pygame.transform.scale(free, (300, 300)).convert_alpha()

among_us = pygame.image.load("among us.jpg")
among_us = pygame.transform.scale(among_us, (100, 100)).convert_alpha()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

game_over = False

font = pygame.font.SysFont(None, 72)
font2 = pygame.font.SysFont(None, 25)
font3 = pygame.font.SysFont(None, 35)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])

def text_screen2(text, color, x, y):
    screen_text = font2.render(text, True, color)
    screen.blit(screen_text, [x,y])

def text_screen3(text, color, x, y):
    screen_text = font3.render(text, True, color)
    screen.blit(screen_text, [x,y])

def exit_screen():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        screen.blit(bg, (0, 0))
        text_screen("OH NO! you lost!", green, 400, 400)
        pygame.display.update()

def q_2():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()    

        screen.blit(bg, (0, 0))
        text_screen("Congratulations! you won $10", blue, 200, 200)
        text_screen2("press ESC to exit!", blue, 200, 550)
        text_screen3("#jao aur jakar ash karo!!", black, 200, 500)
        pygame.display.update()

def q_1():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    q_2()
                else:
                    exit_screen()

        screen.blit(bg, (0, 0))
        text_screen3("you know about the folowing games", red, 30, 200)
        text_screen3("these are the world famous games, which are made by very famous programmers.", red, 30, 220)
        text_screen("Question 1-", black, 30, 350)
        text_screen("Who made PUBG", black, 30, 400)
        pygame.draw.rect(screen, black, (30, 500, 150, 100))
        text_screen2("1: Brandon green", red, 35, 540)
        pygame.draw.rect(screen, black, (300, 500, 190, 100))
        text_screen2("2: Amitabh bachchan", red,  305, 540)
        pygame.draw.rect(screen, black, (700, 500, 190, 100))
        text_screen2("3: Mark zukerberg", red, 705, 540)
        pygame.display.update()

def askdesk():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    q_1()
            

        screen.blit(bg, (0, 0))
        screen.blit(bird, (100, 50))
        screen.blit(PUBG, (750, 400))
        screen.blit(free, (150, 400))
        screen.blit(among_us, (850, 100))
        text_screen("press 1--", black, 500, 325)
        pygame.display.update()

def start_screen():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    askdesk()

        screen.blit(bg, (0, 0))
        screen.blit(me, (100, 50))
        text_screen("About the doveloper-", red, 300, 50)
        text_screen3("i am a 12 years old boy who loves programing.please access my github page!!", 
        black, 100, 300)
        pygame.draw.rect(screen, black, (850, 50, 100, 100))
        text_screen2("press p--", red, 860, 90)
        pygame.display.update()
        
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                exit()
        
            if event.key == pygame.K_s:
                start_screen()
    
    screen.blit(bg, (0, 0))
    
    text_screen("Welcome to my software!", (255, 0, 0), 250, 100)
    pygame.draw.rect(screen, black, (50, 500, 150, 100))
    text_screen2("press S to start!", red, 60, 540)
    pygame.draw.rect(screen, black, (800, 490, 150, 100))
    text_screen2("press E to exit", red, 810, 530)
    
    pygame.display.update()
