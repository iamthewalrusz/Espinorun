import pygame, sys
from main import game

pygame.init()
screen = pygame.display.set_mode((1280, 720))
from pygame.locals import *
clock = pygame.time.Clock()

running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

font = pygame.font.Font("./assets/Pixels.ttf", 50)
font_titulo = pygame.font.Font("./assets/Pixels.ttf", 150)

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
    pontos = 0
    record = 0
    pygame.display.set_caption('Espinorun')
    music_img = pygame.image.load('./assets/NotaMusical.png').convert_alpha()
    while True:

        screen.fill([201, 218, 191])
        draw_text("ESPINORUN", font_titulo, (255, 255, 255), screen, 435, 200)
        draw_text("Corra, Espinossauro!", font, (255, 255, 255), screen, 490, 300)
        music_pause = 0 # Variável para pausar e despausar a música

        score = font.render(f'Recorde: {int(record)}', True, (95, 111, 101))
        screen.blit(score, (screen.get_width() - 200, 50))
        
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(525, 500, 200, 50)
        button_music = pygame.Rect(25, 650, 60, 60)
        
        pygame.draw.rect(screen, (156, 169, 134), button_1)
        pygame.draw.rect(screen, (156, 169, 134), button_music)
        draw_text("Iniciar", font, (255, 255, 255), screen, 580, 500)

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (128, 141, 124), button_1)
            draw_text("Iniciar", font, (255, 255, 255), screen, 580, 500)
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

        screen.blit(music_img, (screen.get_width() - 1245, 655))
        
        pygame.display.update()
        clock.tick(60)

main_menu()