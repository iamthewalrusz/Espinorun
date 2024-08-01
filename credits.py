import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
clock = pygame.time.Clock()

font = pygame.font.Font("./assets/Pixels.ttf", 50)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def credits():
    pygame.display.set_caption('Espinorun')
    bg = pygame.image.load('./assets/background.png').convert_alpha()
    bg = pygame.transform.scale(bg, (1280, 720))
    screen.fill([201, 218, 191])
    click = False

    while True:
        screen.blit(bg, (0,0))

        button_credits = pygame.Rect(270, 180, 740, 360)
        pygame.draw.rect(screen, (156, 169, 134), button_credits)

        draw_text("Desenvolvedores:", font, (255, 255, 255), screen, 535, 200)
        draw_text("-Nathan Guimaraes: Programador e Arte Visual", font, (255, 255, 255), screen, 300, 250)
        draw_text("-Joao Vitor Gimenes: Programador e Sound Design", font, (255, 255, 255), screen, 300, 300)
        draw_text("-Lucas Bicudo: Redator de Artigo", font, (255, 255, 255), screen, 300, 350)
        draw_text("*Jogo feito para a disciplina JCRALGO em conjunto", font, (255, 255, 255), screen, 300, 450)
        draw_text("a um relatorio, disponivel no CONICT", font, (255, 255, 255), screen, 300, 475)

        button_voltar = pygame.Rect(525, 562.5, 200, 50)
        pygame.draw.rect(screen, (156, 169, 134), button_voltar)

        mx, my = pygame.mouse.get_pos()

        if button_voltar.collidepoint((mx, my)):
            pygame.draw.rect(screen, (128, 141, 124), button_voltar)
            if click:
                return
        draw_text("Voltar", font, (255, 255, 255), screen, 587, 562.5)
            
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True 

        pygame.display.update()
        clock.tick(60)