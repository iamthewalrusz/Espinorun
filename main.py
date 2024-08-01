import pygame, sys, random, time
from pygame.locals import *

def collisions(a, b):
    return a.colliderect(b)

def create_obstacle(screen_width, screen_height):
    obstacle_img = pygame.image.load(f'./assets/pedra-{random.randint(1, 2)}.png').convert_alpha()
    obstacle_rect = obstacle_img.get_rect()
    obstacle_rect.x = screen_width
    obstacle_rect.y = screen_height - 200
    return obstacle_img, obstacle_rect

def game():
    pygame.init()
    
    # Configs tela
    x = 1280
    y = 720
    screen = pygame.display.set_mode((x, y), pygame.FULLSCREEN)
    pygame.display.set_caption('Espinorun')

    # Background 1 e 2
    bg = pygame.image.load('./assets/background.png').convert_alpha()
    bg = pygame.transform.scale(bg, (x, y))
    bg2 = pygame.image.load('./assets/background.png').convert_alpha()
    bg2 = pygame.transform.scale(bg2, (x, y))
    bg_x1 = 0
    bg_x2 = x
    
    # Configs Chão 1 e 2
    ground_img = pygame.image.load('./assets/ground.png').convert_alpha()
    ground_rect = ground_img.get_rect()
    pos_ground_y = screen.get_height() - 128
    ground_rect.y = pos_ground_y

    ground2_img = pygame.image.load('./assets/ground.png').convert_alpha()
    ground2_rect = ground2_img.get_rect()
    pos_ground2_y = screen.get_height() - 128
    ground2_rect.y = pos_ground2_y

    ground_x1 = 0
    ground_x2 = x
    ground_velocity = 2

    # Configs Player (sprite)
    player_jumping = pygame.image.load('./assets/player_jumping.png').convert_alpha()
    player_frames = [pygame.image.load('./assets/player_0.png').convert_alpha(),
                     pygame.image.load('./assets/player_1.png').convert_alpha(),
                     pygame.image.load('./assets/player_2.png').convert_alpha(),
                     pygame.image.load('./assets/player_3.png').convert_alpha()]
    frame_player_anim = 0
    frame_rate = 0.125
    last_frame_time = time.time()

    # Configs Player (física)
    player_rect = player_frames[1].get_rect()
    pos_player_x = 150
    pos_player_y = screen.get_height() - 430
    gravity = 0.1
    jump_height = 8
    velocity_y = 0
    on_ground = False

    # Configs Obstáculos
    obstacles = []
    last_obstacle_time = time.time()
    obstacle_interval = random.uniform(1, 3)
    obstacle_velocity = 2
    angle = 0

    # Configs Texto
    font = pygame.font.Font('./assets/Pixels.ttf', 65)
    pontos = 0

    running = True
    while running:
        # Detectar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Sair do jogo
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Sair do jogo 2
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE and on_ground: # Pular
                    on_ground = False
                    velocity_y = -jump_height

        # Gravidade
        if collisions(player_rect.move(0, velocity_y), ground_rect):
            on_ground = True
            velocity_y = 0
        else:
            velocity_y += gravity
            pos_player_y += velocity_y

        # Mover e controlar obstáculos
        current_time = time.time()
        if current_time - last_obstacle_time > obstacle_interval:
            obstacle_img, obstacle_rect = create_obstacle(screen.get_width(), screen.get_height())
            obstacles.append((obstacle_img, obstacle_rect))
            last_obstacle_time = current_time
            obstacle_interval = random.uniform(1, 3)  # Atualizar intervalo obstáculos

        # Atualizar Obstáculos
        for i, (obstacle_img, obstacle_rect) in enumerate(obstacles):
            obstacle_rect.x -= obstacle_velocity  # Mover p/ esquerda
            if obstacle_rect.x < -obstacle_rect.width:
                pontos += 1
                obstacles.pop(i)
        
        if obstacle_velocity < 7:
            obstacle_velocity += 0.0001

        # Mover colisores player
        player_rect.x = pos_player_x
        player_rect.y = pos_player_y

        # Animação player
        if time.time() - last_frame_time > frame_rate:
            frame_player_anim += 1
            last_frame_time = time.time()
        if frame_player_anim > 3: frame_player_anim = 0

        # Mover background
        bg_x1 -= 1
        bg_x2 -= 1
        if bg_x1 <= -x:
            bg_x1 = x
        if bg_x2 <= -x:
            bg_x2 = x
        
        # Mover chão
        ground_x1 -= ground_velocity
        ground_x2 -= ground_velocity
        if ground_x1 <= -x:
            ground_x1 = x
        if ground_x2 <= -x:
            ground_x2 = x

        # Desenhar Background/Chão
        screen.blit(bg, (bg_x1, 0))
        screen.blit(bg2, (bg_x2, 0))
        screen.blit(ground_img, (ground_x1, screen.get_height() - 128))
        screen.blit(ground2_img, (ground_x2, screen.get_height() - 128))

        # Desenhar player
        if on_ground:
            screen.blit(player_frames[frame_player_anim], (pos_player_x, pos_player_y))
        else:
            screen.blit(player_jumping, (pos_player_x, pos_player_y))

        # Desenhar obstáculos
        angle += 0.5
        for obstacle_img, obstacle_rect in obstacles:
            obstacle_img = pygame.transform.rotate(obstacle_img, angle)
            screen.blit(obstacle_img, (obstacle_rect.x, obstacle_rect.y))    
        
        # Escrever pontuação
        score = font.render(f'Pontos: {int(pontos)}', True, (95, 111, 101))
        screen.blit(score, (screen.get_width() - 200, 50))

        # GameOver
        for obstacle_img, obstacle_rect in obstacles:
            if collisions(player_rect, obstacle_rect):
                return pontos  # Retorna ao menu principal

        pygame.display.update()
    pygame.quit()
