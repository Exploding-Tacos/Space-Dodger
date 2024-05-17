import pygame
from sys import exit
import random
from pygame import mixer 

pygame.init()
screen = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Space Dodgers")
Icon = pygame.image.load('Graphics/Playership.png')
pygame.display.set_icon(Icon)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
button_surface = pygame.Surface((150, 50))
text = font.render("Play", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
button_rect = pygame.Rect(125, 125, 150, 50)  # Adjust the position as needed

while True:

    clock.tick(60)
 
    screen.fill((155, 255, 155))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if button_rect.collidepoint(event.pos):
            print("Button clicked!")

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
  


    button_surface.blit(text, text_rect)

    screen.blit(button_surface, (button_rect.x, button_rect.y))

    pygame.display.update()