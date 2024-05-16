import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1200,900))
pygame.display.set_caption("Tutorial")

clock = pygame.time.Clock()
Mainmenu_font = pygame.font.Font(None, 50)

score = 0
player_grav = 0

sky = pygame.image.load("Graphics/space.png").convert_alpha()

name_surf = Mainmenu_font.render('Space Dodgers', True, (255, 255, 255))
name_rect = name_surf.get_rect(center = (450, 50))

score_surf = Mainmenu_font.render(f'Score: {score}', True, (255, 255, 255))
score_rect = name_surf.get_rect(center = (450, 150))

player_surf = pygame.image.load("Graphics/Playership.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (150, 350))

Bullet_surface = pygame.image.load('Graphics/Bullet.png').convert_alpha()
Bullet_rect = Bullet_surface.get_rect(midbottom = (900, 350))

while True:

	score_surf = Mainmenu_font.render(f'Score: {score}', True, (255, 255, 255))
	score_rect = name_surf.get_rect(center = (450, 150))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky, (0,0))	
	pygame.draw.rect(screen,(155,0,22),name_rect)
	pygame.draw.rect(screen,(155,0,22),name_rect,10)
	screen.blit(name_surf, name_rect)

	pygame.draw.rect(screen,(155,0,22),score_rect)
	pygame.draw.rect(screen,(155,0,22),score_rect,10)
	screen.blit(score_surf, score_rect)
	screen.blit(Bullet_surface, Bullet_rect)

	'''placinglist = ["1", "2", "3"]
	placinglit = random.choice(placinglist)
	if placinglit == "1":
		placingbullet = 350
	elif placinglit == "2":
		placingbullet = 450
	elif placinglit == "3":
		placingbullet = 550

	Bullet_surface = pygame.image.load('Graphics/Bullet.png').convert_alpha()
	Bullet_rect = Bullet_surface.get_rect(midbottom = (900, placingbullet))'''

	Bullet_rect.x -= 6
	if Bullet_rect.right <= 0:
		Bullet_rect.left = 900
		score += 1
		print("bol")

	#Player
	player_grav += 1
	player_rect.y += player_grav
	screen.blit(player_surf,player_rect)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		player_grav = -20

	Collod = player_rect.colliderect(Bullet_rect)
	if Collod == True:
		score = 0
		#print("Collision")

	pygame.display.update()
	clock.tick(60)

score_run = False