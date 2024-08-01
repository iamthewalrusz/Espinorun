import pygame, sys
from main import game
from credits import credits
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
clock = pygame.time.Clock()

font = pygame.font.Font("./assets/Pixels.ttf", 50)
font_pontos = pygame.font.Font("./assets/Pixels.ttf", 65)
font_titulo = pygame.font.Font("./assets/Pixels.ttf", 150)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pygame.mixer.init()
pygame.mixer.music.load("./assets/teste.wav")
pygame.mixer.music.play(loops=-1)

def main_menu():
    button_size_x, button_size_y = 45, 45
    pontos = 0
    record = 0
    pygame.display.set_caption('Espinorun')
    music_img = pygame.image.load('./assets/NotaMusical.png').convert_alpha()
    music_img = pygame.transform.scale(music_img, (button_size_x-15, button_size_y-15))
    music_pause = 0 # Variável para pausar e despausar a música
    bg = pygame.image.load('./assets/background.png').convert_alpha()
    bg = pygame.transform.scale(bg, (1280, 720))
    screen.fill([201, 218, 191])

    while True:
        
        screen.blit(bg, (0,0))
        draw_text("ESPINORUN", font_titulo, (255, 255, 255), screen, 435, 200)
        draw_text("Corra, Espinossauro!", font, (255, 255, 255), screen, 490, 300)

        score = font_pontos.render(f'Recorde: {int(record)}', True, (95, 111, 101))
        screen.blit(score, (screen.get_width() - 200, 50))
        
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(525, 500, 200, 50)
        button_music = pygame.Rect(25, 650, button_size_x, button_size_y)
        button_credits = pygame.Rect(525, 562.5, 200, 50)
        button_quit = pygame.Rect(525, 625, 200, 50)
        
        pygame.draw.rect(screen, (156, 169, 134), button_1)
        pygame.draw.rect(screen, (156, 169, 134), button_music)
        pygame.draw.rect(screen, (156, 169, 134), button_credits)
        pygame.draw.rect(screen, (156, 169, 134), button_quit)

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (128, 141, 124), button_1)
            if click:
                pontos = game()
                if pontos >= record:
                    record = pontos

        if button_music.collidepoint((mx, my)):
            pygame.draw.rect(screen, (128, 141, 124), button_music)
            if click:
                if music_pause == 0:
                    pygame.mixer_music.pause()
                    music_pause = 1
                else:
                    pygame.mixer_music.unpause()
                    music_pause = 0

        if button_credits.collidepoint((mx, my)):
            pygame.draw.rect(screen, (128, 141, 124), button_credits)
            if click:
                credits()

        if button_quit.collidepoint((mx, my)):
            pygame.draw.rect(screen, (128, 141, 124), button_quit)
            if click:
                pygame.quit()
                sys.exit()

        draw_text("Iniciar", font, (255, 255, 255), screen, 580, 500)
        draw_text("Creditos", font, (255, 255, 255), screen, 575, 562.5)
        draw_text("Sair", font, (255, 255, 255), screen, 600, 625)
        screen.blit(music_img, (screen.get_width() - 1245, 655))

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