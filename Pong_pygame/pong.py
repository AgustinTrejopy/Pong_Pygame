import pygame
import time

pygame.init()

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED = ( 255,   0,   0)
BLUE = (   0,   0, 255)

screen_size = (800, 600)
player_width = 15
player_height = 90

puntos_player_1 = 0
puntos_player_2 = 0

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

# Coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

# Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_y_speed = -5
            if event.key == pygame.K_s:
                player1_y_speed = 5
            if event.key == pygame.K_UP:
                player2_y_speed = -5
            if event.key == pygame.K_DOWN:
                player2_y_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1

    # Revisa si la pelota sale del lado derecho
    if pelota_x > 800:
        puntos_player_1 += 1
        pelota_x = 400
        pelota_y = 300
        # Si sale de la pantalla, invierte direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        time.sleep(1)
    # Revisa si la pelota sale del lado izquierdo
    if pelota_x < 0:
        puntos_player_2 += 1
        pelota_x = 400
        pelota_y = 300
        # Si sale de la pantalla, invierte direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        time.sleep(1)
    
    # Modifica las coordenadas para dar mov. a los jugadores/pelota

    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    # Movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    if player1_y_coor > 510:
        player1_y_coor = 510

    if player1_y_coor < 0:
        player1_y_coor = 0

    if player2_y_coor > 510:
        player2_y_coor = 510

    if player2_y_coor < 0:
        player2_y_coor = 0

    screen.fill(BLACK)

    fuente = pygame.font.SysFont("arial black", 60)
    fuente_2 = pygame.font.SysFont("arial", 30)
    texto = fuente.render (str(puntos_player_1), True, WHITE)
    texto_2 = fuente.render(str(puntos_player_2), True, WHITE)

    # Zona de dibujo
    jugador1 = pygame.draw.rect(screen, WHITE, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, WHITE, (player2_x_coor, player2_y_coor, player_width, player_height))
    pelota = pygame.draw.circle(screen, WHITE, (pelota_x, pelota_y), 10)
    screen.blit(texto, (200, 5))
    screen.blit(texto_2, (600, 5))
    linea_vertical = pygame.draw.line(screen, WHITE, (400, 600), (400, 0), 5)
    # Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    # Zona de dibujo
    pygame.display.flip()
    clock.tick(60)
pygame.quit()