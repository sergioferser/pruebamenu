import pygame, sys

mainClock= pygame.time.Clock()
from pygame.locals import *
pygame.init()
username=""
pygame.display.set_caption('gamebase')
screen= pygame.display.set_mode((1920,1080),pygame.RESIZABLE)
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

        mx,my= pygame.mouse.get_pos()
        button_1=font.render("Play",False,(101,56,25))
        button_1_rect=button_1.get_rect(center=(960,450))
        button_2=font.render("Options",False,(101,56,25))
        button_2_rect=button_2.get_rect(center=(960,550))
        button_3=font.render("Salir",False,(101,56,25))
        button_3_rect=button_3.get_rect(center=(960,650))
        if button_1_rect.collidepoint((mx,my)):
            if click:
                introducir_nombre()
        if button_2_rect.collidepoint((mx,my)):
            if click:
                options()
        if button_3_rect.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()
        screen.blit(button_1,button_1_rect)
        screen.blit(button_2,button_2_rect)
        screen.blit(button_3,button_3_rect)


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
def introducir_nombre():
    running=True
    username=""
    while running:
        screen.fill((192,157,86))
        draw_text('INSERT NAME',font,(101,56,25),screen,700,200)
        draw_text(username,font,(101,56,25),screen,750,500)
        input_rect = pygame.Rect(700,500,450,70)
        color=pygame.Color(101,56,25)
        pygame.draw.rect(screen,color,input_rect,2)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    running=False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif(len(username)>=9):
                    pass
                else:
                    username+= event.unicode
                if event.key == K_ESCAPE:
                    running=False
        pygame.display.update()
        mainClock.tick(60)

def options():
    running=True
    click=False
    while running:
        screen.blit(fondo,(0,0))

        mx,my= pygame.mouse.get_pos()
        button_1_1 = font.render("Skins",False,(101,56,25))
        button_1_1_rect = button_1_1.get_rect(center=(960,450))
        button_1_2 = font.render("Salir",False,(101,56,25))
        button_1_2_rect = button_1_2.get_rect(center=(960,550))

        if button_1_1_rect.collidepoint((mx,my)):
            if click:
                skin()
        if button_1_2_rect.collidepoint((mx,my)):
            if click:
                running=False
        screen.blit(button_1_1,button_1_1_rect)
        screen.blit(button_1_2,button_1_2_rect)
        click = False


        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()
        mainClock.tick(60)

def skin():
    running=True
    click=False
    while running:

        screen.blit(fondo, (0, 0))

        mx,my= pygame.mouse.get_pos()

        button_1=font.render("Inverted",False,(101,56,25))
        button_1_rect=button_1.get_rect(center=(960,450))
        button_2=font.render("Salir",False,(101,56,25))
        button_2_rect=button_1.get_rect(center=(960,550))
        if button_1_rect.collidepoint((mx,my)):
            if click:
                pass
        if button_2_rect.collidepoint((mx,my)):
            if click:
                running=False

        screen.blit(button_1, button_1_rect)
        screen.blit(button_2, button_2_rect)

        click = False
        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False

            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()
        mainClock.tick(60)
main_menu()