import pygame
from pygame.locals import *

pygame.init()

screen_width = 564
screen_height = 736

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#load images
bg = pygame.image.load('')

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            
           
pygame.quit()      