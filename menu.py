import pygame, sys

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

def main_menu():
    while True:

        screen.fill([48, 100, 184])
        draw_text("Jogo do Dinossauro", font_titulo, (255, 255, 255), screen, 325, 200)
        

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(525, 500, 200, 50)
        button_music = pygame.Rect(25, 650, 50, 50)
        
        pygame.draw.rect(screen, (27, 59, 110), button_1)
        pygame.draw.rect(screen, (27, 59, 110), button_music)
        draw_text("Iniciar", font, (255, 255, 255), screen, 605, 517)

        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (17, 39, 74), button_1)
            draw_text("Iniciar", font, (204, 204, 204), screen, 605, 517)
            if click:
                game()

        if button_music.collidepoint((mx, my)):
            pygame.draw.rect(screen, (17, 39, 74), button_music)
            if click:
                print()

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

def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        screen.fill([66, 135, 245])

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_pos.y -= 300 * dt
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

main_menu()