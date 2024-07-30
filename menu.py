import pygame, sys
from main_nova import game

pygame.init()
screen = pygame.display.set_mode((1280, 720))
from pygame.locals import *
clock = pygame.time.Clock()

running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

font = pygame.font.SysFont(None, 20)
font_titulo = pygame.font.SysFont(None, 100)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

pygame.mixer.init()
pygame.mixer.music.load("./assets/teste.wav")
pygame.mixer.music.play(loops=-1)

def main_menu():
    while True:

        screen.fill([201, 218, 191])
        draw_text("ESPINORUN", font_titulo, (255, 255, 255), screen, 425, 200)
        music_pause = 0 # Variável para pausar e despausar a música
        
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(525, 500, 200, 50)
        button_music = pygame.Rect(25, 650, 50, 50)
        
        pygame.draw.rect(screen, (156, 169, 134), button_1)
        pygame.draw.rect(screen, (156, 169, 134), button_music)
        draw_text("Iniciar", font, (255, 255, 255), screen, 605, 517)

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (128, 141, 124), button_1)
            draw_text("Iniciar", font, (204, 204, 204), screen, 605, 517)
            if click:
                game()

        if button_music.collidepoint((mx, my)):
            pygame.draw.rect(screen, (128, 141, 124), button_music)
            if click:
                if music_pause == 0:
                    pygame.mixer_music.pause()
                    music_pause = 1
                else:
                    pygame.mixer_music.unpause()
                    music_pause = 0

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

main_menu()