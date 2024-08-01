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
    
    x = 1280
    y = 720
    screen = pygame.display.set_mode((x, y), pygame.FULLSCREEN)
    pygame.display.set_caption('Espinorun')

    # Background
    bg = pygame.image.load('./assets/background.png').convert_alpha()
    bg = pygame.transform.scale(bg, (x, y))
    
    # Duplicate background for continuous scrolling
    bg2 = pygame.image.load('./assets/background.png').convert_alpha()
    bg2 = pygame.transform.scale(bg2, (x, y))
    
    bg_x1 = 0
    bg_x2 = x
    
    # Ground
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

    # Player
    player_img = pygame.image.load('./assets/Player.png').convert_alpha()
    player_rect = player_img.get_rect()
    pos_player_x = 150
    pos_player_y = screen.get_height() - 430
    gravity = 0.1
    jump_height = 8
    velocity_y = 0
    on_ground = False

    # Obstacles
    obstacles = []
    last_obstacle_time = time.time()
    obstacle_interval = random.uniform(1, 3)
    obstacle_velocity = 2
    angle = 0

    # Text
    font = pygame.font.Font('./assets/Pixels.ttf', 65)
    pontos = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE and on_ground:
                    on_ground = False
                    velocity_y = -jump_height

        # Gravity
        if collisions(player_rect.move(0, velocity_y), ground_rect):
            on_ground = True
            velocity_y = 0
        else:
            velocity_y += gravity
            pos_player_y += velocity_y

        # Move and manage obstacles
        current_time = time.time()
        if current_time - last_obstacle_time > obstacle_interval:
            obstacle_img, obstacle_rect = create_obstacle(screen.get_width(), screen.get_height())
            obstacles.append((obstacle_img, obstacle_rect))
            last_obstacle_time = current_time
            obstacle_interval = random.uniform(1, 3)  # Update the interval for the next obstacle

        # Update obstacles
        for i, (obstacle_img, obstacle_rect) in enumerate(obstacles):
            obstacle_rect.x -= obstacle_velocity  # Move the obstacle to the left
            if obstacle_rect.x < -obstacle_rect.width:
                pontos += 1
                obstacles.pop(i)
        
        if obstacle_velocity < 7:
            obstacle_velocity += 0.00001

        # Update player and obstacle positions
        player_rect.x = pos_player_x
        player_rect.y = pos_player_y

        # Move background
        bg_x1 -= 1
        bg_x2 -= 1

        ground_x1 -= ground_velocity
        ground_x2 -= ground_velocity

        if bg_x1 <= -x:
            bg_x1 = x
        if bg_x2 <= -x:
            bg_x2 = x
        
        if ground_x1 <= -x:
            ground_x1 = x
        if ground_x2 <= -x:
            ground_x2 = x

        # Draw everything
        screen.blit(bg, (bg_x1, 0))
        screen.blit(bg2, (bg_x2, 0))
        #screen.blit(ground_img, (0, screen.get_height() - 128))
        screen.blit(ground_img, (ground_x1, screen.get_height() - 128))
        screen.blit(ground2_img, (ground_x2, screen.get_height() - 128))
        screen.blit(player_img, (pos_player_x, pos_player_y))
        angle += 0.5
        for obstacle_img, obstacle_rect in obstacles:
            obstacle_img = pygame.transform.rotate(obstacle_img, angle)
            screen.blit(obstacle_img, (obstacle_rect.x, obstacle_rect.y))    
        
        score = font.render(f'Pontos: {int(pontos)}', True, (95, 111, 101))
        screen.blit(score, (screen.get_width() - 200, 50))

        # GameOver
        for obstacle_img, obstacle_rect in obstacles:
            if collisions(player_rect, obstacle_rect):
                return pontos  # Retorna ao menu principal

        pygame.display.update()
    pygame.quit()
