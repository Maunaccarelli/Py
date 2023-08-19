import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dragon Ball Z Game")

# Carga de imágenes y efectos de sonido
background = pygame.image.load("background.png")
goku_image = pygame.image.load("goku.png")
enemy_images = [pygame.image.load("freezer.png"), pygame.image.load("cell.png")]
kamehameha_sound = pygame.mixer.Sound("kamehameha.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")

# Posición inicial de Goku
goku_x = 100
goku_y = screen_height - goku_image.get_height() - 10
goku_speed = 5

# Listas para almacenar enemigos, disparos y explosiones
enemies = []
shots = []
explosions = []

# Función para crear una explosión
def create_explosion(x, y):
    explosions.append((x, y))

# Función para crear un enemigo
def create_enemy():
    enemy_image = random.choice(enemy_images)
    enemy_x = screen_width
    enemy_y = random.randint(100, screen_height - enemy_image.get_height() - 10)
    enemies.append((enemy_image, enemy_x, enemy_y))

# Bucle principal del juego
running = True
level = 1
enemies_per_level = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        goku_x -= goku_speed
    if keys[pygame.K_RIGHT]:
        goku_x += goku_speed
    if keys[pygame.K_SPACE]:
        kamehameha_sound.play()
        shots.append((goku_x + goku_image.get_width() // 2, goku_y))

    # Creación de enemigos
    if len(enemies) < enemies_per_level:
        create_enemy()

    # Movimiento de enemigos
    for enemy_image, enemy_x, enemy_y in enemies:
        enemy_x -= level * 2
        if enemy_x < -enemy_image.get_width():
            enemies.remove((enemy_image, enemy_x, enemy_y))
        
        # Detección de colisión con Goku
        if pygame.Rect(enemy_x, enemy_y, enemy_image.get_width(), enemy_image.get_height()).colliderect(
            pygame.Rect(goku_x, goku_y, goku_image.get_width(), goku_image.get_height())):
            create_explosion(goku_x, goku_y)
            explosion_sound.play()
            running = False
        
        for shot in shots:
            shot_x, shot_y = shot
            if pygame.Rect(enemy_x, enemy_y, enemy_image.get_width(), enemy_image.get_height()).colliderect(
                pygame.Rect(shot_x, shot_y, 10, 10)):
                create_explosion(enemy_x, enemy_y)
                explosion_sound.play()
                shots.remove(shot)
                enemies.remove((enemy_image, enemy_x, enemy_y))
        
        enemy_x = enemy_x
        enemies.append((enemy_image, enemy_x, enemy_y))

    # Movimiento de disparos y detección de colisiones
    for shot in shots:
        shot_x, shot_y = shot
        shot_y -= 10
        if shot_y < 0:
            shots.remove(shot)
        for explosion in explosions:
            exp_x, exp_y = explosion
            if pygame.Rect(shot_x, shot_y, 10, 10).colliderect(pygame.Rect(exp_x, exp_y, 64, 64)):
                shots.remove(shot)
        shot = (shot_x, shot_y)
    
    # Dibuja en la pantalla
    screen.blit(background, (0, 0))
    screen.blit(goku_image, (goku_x, goku_y))
    for enemy_image, enemy_x, enemy_y in enemies:
        screen.blit(enemy_image, (enemy_x, enemy_y))
    for shot in shots:
        pygame.draw.circle(screen, (255, 0, 0), shot, 5)
    for explosion in explosions:
        exp_x, exp_y = explosion
        screen.blit(pygame.image.load("explosion.png"), (exp_x, exp_y))
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()