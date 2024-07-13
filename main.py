import pygame
import sys
import random


# functions
def ship_ani():
    ship.x += ship_speed
    if ship.right >= screen_width:
        ship.right = screen_width
    if ship.left <= 0:
        ship.left = 0

def proj_ani():
    proj.y += proj_speed_y

# general setup
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
proj = pygame.Rect(enemy.left + 23, enemy.bottom + 5, 10, 50)

# colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# speed
ship_speed = 0
proj_speed_y = 7

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship_speed -= 7
            if event.key == pygame.K_LEFT:
                ship_speed += 7

    # functions
    ship_ani()
    proj_ani()

    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, ship)
    pygame.draw.rect(screen, light_grey, enemy)
    pygame.draw.rect(screen, light_grey, proj)

    # updating the window
    pygame.display.flip()
    clock.tick(60)