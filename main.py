def game():

    import pygame
    import random

    pygame.init()
    pygame.display.set_caption('Espinorun')

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    obstacles = []

    # Posições
    player_pos = [(100, screen.get_height() -100), (50, 50)]
    ground_pos = [(0, screen.get_height()-45), (screen.get_width(), screen.get_height()-45)]
    obstacle_pos = [(screen.get_width(), screen.get_height() -95), (50, 50)]

    ground_colisor = pygame.Rect(ground_pos)
    player_colisor = pygame.Rect(player_pos)
    obstacle_colisor = pygame.Rect(obstacle_pos)

    velocity_y = 0.2
    velocity_obstacle = -0.5

    MOVEEMENT, t = pygame.USEREVENT+1, 250
    pygame.time.set_timer(MOVEEMENT, t)

    running = True
    while running:

        # Configs gerais
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOVEEMENT:
                    MOVEEMENT, t = pygame.USEREVENT+1, random.randrange(1000, 2000)
                    pygame.time.set_timer(MOVEEMENT, t)
                    obstacle_width = 50
                    obstacle_height = 50
                    x = screen.get_width()  # Posição inicial no lado direito da tela
                    y = screen.get_height() - 95  # Altura padrão do obstáculo em relação ao solo
                    obstacle = pygame.Rect(x, y, obstacle_width, obstacle_height)
                    obstacles.append(obstacle)
                    velocity_obstacle -= 0.05
        
        screen.fill('black')

        # Variaveis
        keys = pygame.key.get_pressed()
        dt = clock.tick(60)

        # Gravidade
        player_colisor.move_ip(0, velocity_y * dt)

        # Mov. obstáculo
        for obstacle in obstacles[:]:  # Percorre uma cópia da lista para evitar problemas de modificação durante a iteração
            obstacle.x += velocity_obstacle * dt
            if obstacle.right < 0:  # Remover obstáculos que saíram da tela
                obstacles.remove(obstacle)

        # Pulo
        if player_colisor.collidelist([ground_colisor]) >= 0:
            velocity_y = 0
            cont = 0
            if keys[pygame.K_SPACE]:
                velocity_y = -0.15
                while cont <= 100:
                    cont += 1
                    player_colisor.move_ip(0, velocity_y * dt)
                    pygame.draw.rect(screen, 'red', player_colisor)
                velocity_y = 0.2

        # Desenhar na tela
        pygame.draw.rect(screen, 'white', ground_colisor)
        pygame.draw.rect(screen, 'red', player_colisor)
        for obstacle in obstacles:
            pygame.draw.rect(screen, 'purple', obstacle)

        pygame.display.flip()

    pygame.quit()