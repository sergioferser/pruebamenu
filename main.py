import pygame, sys

mainClock= pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('gamebase')
screen= pygame.display.set_mode((1280,720),0,32)
font=pygame.font.Font("font/fuente.TTF",50)
fondo=pygame.image.load("menu.png").convert()
def draw_text(text,font,color,surface,x,y):
    textobj= font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

click= False

def main_menu():
    while True:
        screen.blit(fondo,(0,0))
        draw_text('main menu',font,(255,255,255),screen,20,20)

        mx,my= pygame.mouse.get_pos()
        button_1=font.render("Play",False,(101,56,25))
        button_1_rect=button_1.get_rect(center=(960,450))
        button_2=font.render("Options",False,(101,56,25))
        button_2_rect=button_1.get_rect(center=(960,550))
        if button_1_rect.collidepoint((mx,my)):
            if click:
                game()
        if button_2_rect.collidepoint((mx,my)):
            if click:
                options()
        screen.blit(button_1,button_1_rect)
        screen.blit(button_2,button_2_rect)

        click= False
        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()
        mainClock.tick(60)
def game():
    running=True
    while running:
        screen.fill((0,0,0))
        draw_text('GAME',font,(255,255,255),screen,20,20)

        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
        pygame.display.update()
        mainClock.tick(60)

def options():
    running=True
    while running:
        screen.blit(fondo,(0,0))

        draw_text('OPTIONS',font,(255,255,255),screen,20,20)
        mx,my= pygame.mouse.get_pos()
        button_1=font.render("Pantalla",False,(101,56,25))
        button_1_rect=button_1.get_rect(center=(960,450))
        button_2=font.render("Salir",False,(101,56,25))
        button_2_rect=button_1.get_rect(center=(960,550))
        if button_1_rect.collidepoint((mx,my)):
            if click:
                pantalla()
        if button_2_rect.collidepoint((mx,my)):
            if click:
                running=False
        screen.blit(button_1,button_1_rect)
        screen.blit(button_2,button_2_rect)



        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
        pygame.display.update()
        mainClock.tick(60)

def pantalla():
    running=True
    while running:
        mx,my= pygame.mouse.get_pos()

        button_1=font.render("1280*720",False,(101,56,25))
        button_1_rect=button_1.get_rect(center=(960,450))
        button_2=font.render("Salir",False,(101,56,25))
        button_2_rect=button_1.get_rect(center=(960,550))
        if button_1_rect.collidepoint((mx,my)):
            if click:
                running=False
        if button_2_rect.collidepoint((mx,my)):
            if click:
                running=False
        screen.blit(button_1, button_1_rect)
        screen.blit(button_2, button_2_rect)
        screen.blit(fondo, (0, 0))
        draw_text('Pantalla',font,(255,255,255),screen,20,20)

        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
        pygame.display.update()
        mainClock.tick(60)
main_menu()