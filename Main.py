import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Tutorial")

clock = pygame.time.Clock()
Mainmenu_font = pygame.font.Font(None, 50)

score = 0
player_grav = 0

sky = pygame.image.load("Graphics/sky.png").convert_alpha()
floor = pygame.image.load("Graphics/floor.png").convert_alpha()

name_surf = Mainmenu_font.render('Space Dodgers', True, (255, 255, 255))
name_rect = name_surf.get_rect(center = (450, 50))

score_surf = Mainmenu_font.render(f'Score: {score}', True, (255, 255, 255))
score_rect = name_surf.get_rect(center = (450, 150))

Bullet_surface = pygame.image.load('Graphics/Bullet.png').convert_alpha()
Bullet_rect = Bullet_surface.get_rect(midbottom = (900, 350))

player_surf = pygame.image.load("Graphics/Playership.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (150, 350))

while True:

	score_surf = Mainmenu_font.render(f'Score: {score}', True, (255, 255, 255))
	score_rect = name_surf.get_rect(center = (450, 150))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky, (0,0))
	screen.blit(floor, (0,350))
	pygame.draw.rect(screen,(155,0,22),name_rect)
	pygame.draw.rect(screen,(155,0,22),name_rect,10)
	screen.blit(name_surf, name_rect)

	pygame.draw.rect(screen,(155,0,22),score_rect)
	pygame.draw.rect(screen,(155,0,22),score_rect,10)
	screen.blit(score_surf, score_rect)

	#Bullet
	Bullet_rect.x -= 6
	if Bullet_rect.right <= 0:
		Bullet_rect.left = 900
		score += 1
	screen.blit(Bullet_surface,Bullet_rect)

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