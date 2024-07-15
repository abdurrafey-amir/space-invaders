import pygame
import sys
import random
import time


# functions
def ship_ani():
    ship.x += ship_speed
    if ship.right >= screen_width:
        ship.right = screen_width
    if ship.left <= 0:
        ship.left = 0

    

def enemy_ani():
    global enemy_speed
    enemy.x += enemy_speed
    if enemy.right >= screen_width:
        enemy.right = screen_width
        enemy_speed *= -1
        # new_proj = pygame.Rect(enemy.left, enemy.bottom + 30, 15, 15)
        # projectiles.append(new_proj)
    if enemy.left <= 0:
        enemy.left = 0
        enemy_speed *= -1
        # new_proj2 = pygame.Rect(enemy.left, enemy.bottom + 30, 15, 15)
        # projectiles.append(new_proj2)

def proj_ani():
    new_proj = pygame.Rect(enemy.left, enemy.bottom + 30, 15, 15)
    projectiles.append(new_proj)


# general setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# main window
screen_width = 1280
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

# game recs

ship = pygame.Rect(screen_width/2 - 15, screen_height - 50, 30, 30)
enemy = pygame.Rect(screen_width/2 - 30, 50, 60, 30)
bullet = pygame.Rect(ship.left, ship.top - 30, 15, 15)
bullets = []  
projectile = pygame.Rect(enemy.left, enemy.bottom + 30, 15, 15)
projectiles = []


bg_color = pygame.Color('grey12')
bg = pygame.image.load('background.png')
light_grey = (200, 200, 200)
font = pygame.font.Font("freesansbold.ttf", 32)
shoot_sound = pygame.mixer.Sound('shoot.wav')

# speed
ship_speed = 0
enemy_speed = 7 * random.choice((1, -1))
proj_speed_y = 7
bullet_speed_y = 7
proj_time = 0
score = 0

# main loop
while True:
    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship_speed += 7
            if event.key == pygame.K_LEFT:
                ship_speed -= 7
            if event.key == pygame.K_SPACE:
                new_bullet = pygame.Rect(ship.left, ship.top - 30, 15, 15)
                bullets.append(new_bullet)
                pygame.mixer.Sound.play(shoot_sound)
                # proj_time = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship_speed -= 7
            if event.key == pygame.K_LEFT:
                ship_speed += 7
                
    
    


    # functions
    ship_ani()
    enemy_ani()    
    
    
    
    
    # visuals
    screen.fill(bg_color)
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, light_grey, ship)
    pygame.draw.rect(screen, light_grey, enemy)


    # score
    score_text = font.render(f'{score}', False, light_grey)
    screen.blit(score_text, (screen_width/2, 20))




    # Spawn projectile once every second
    
    # current_time = pygame.time.get_ticks()
    # if current_time - proj_time >= 1000:  # 1000 ms = 1 second
    #     proj_time = current_time
    #     proj_ani()  # spawn a new projectile
    
    
    # # current_time = pygame.time.get_ticks()
    # # if current_time - proj_time > 700:
    #     for proj in projectiles:
    #         print(proj.y)
    #         proj.y += proj_speed_y
    #         pygame.draw.ellipse(screen, light_grey, proj)
    #         if proj.bottom >= screen_height:
    #             projectiles.remove(proj)
    
    
    
    # bullets
    for bullet in bullets:
            bullet.y -= bullet_speed_y
            pygame.draw.ellipse(screen, light_grey, bullet)
            if bullet.top <= 0:
                bullets.remove(bullet)
            if bullet.colliderect(enemy):
                score += 1
                bullets.remove(bullet)
    
        
    # updating the window
    pygame.display.flip()
    clock.tick(60)