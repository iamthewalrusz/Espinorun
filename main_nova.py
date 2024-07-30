import pygame

def colisions(a, b):
    if a.colliderect(b):
        return True
    else:
        return False

def game():
    x = 1280
    y = 720
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption('Estegorun')

    bg = pygame.image.load('./assets/background.png').convert_alpha()
    bg = pygame.transform.scale(bg, (x, y))

    groundImg = pygame.image.load('./assets/ground.png').convert_alpha()
    ground_rect = groundImg.get_rect()
    pos_ground_y = screen.get_height()-128
    ground_rect.y = pos_ground_y

    playerImg = pygame.image.load('./assets/Player.png').convert_alpha()
    player_rect = playerImg.get_rect()
    pos_player_x = 150
    pos_player_y = screen.get_height()-430
    gravity = 0.5
    jump_height = 16
    velocity_y = 0
    on_ground = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Teclas
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and on_ground:
            on_ground = False
            velocity_y = -jump_height
        

        # Gravidade
        if colisions(player_rect.move(0, velocity_y), ground_rect):
            on_ground = True
            velocity_y = 0
        else:
            velocity_y += gravity
            pos_player_y += velocity_y

            
        # Colisão seguir sprite
        player_rect.x = pos_player_x
        player_rect.y = pos_player_y
        

        # Desenhar sprites
        screen.blit(bg, (0, 0))
        screen.blit(groundImg, (0, screen.get_height()-128))
        screen.blit(playerImg, (pos_player_x, pos_player_y))

        # Desenhar colisão
        #pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
        #pygame.draw.rect(screen, (255, 0, 0), ground_rect, 4)
    
        pygame.display.update()

game()