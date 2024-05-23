# Import packages
import pygame
from sys import exit
import random
from pygame import mixer 


# Making main function
def Playfunc():

	# Initializes the window and sets the size of it
	pygame.init()
	screen = pygame.display.set_mode((1200,900))


	# Making the title/caption
	pygame.display.set_caption("Space Dodgers")
	Icon = pygame.image.load('Graphics/Playership.png')
	pygame.display.set_icon(Icon)


	# Setting fps
	clock = pygame.time.Clock()


	# Setting text style
	Mainmenu_font = pygame.font.Font(None, 50)


	# Setting the main variables
	score = 0
	player_grav = 0
	placingbulle = 485
	Highscore = 0


	# Setting the background
	space = pygame.image.load("Graphics/space.png").convert_alpha()


	# Setting Highscore
	Highscore_surf = Mainmenu_font.render(f'Highscore: {Highscore}', True, (255, 255, 255))
	Highscore_rect = Highscore_surf.get_rect(center = (450, 50))


	# Setting the Score
	score_surf = Mainmenu_font.render(f'Score: {score}', True, (255, 255, 255))
	score_rect = Highscore_surf.get_rect(center = (450, 150))


	# Setting the player image
	player_surf = pygame.image.load("Graphics/Playership.png").convert_alpha()
	player_rect = player_surf.get_rect(midbottom = (150, 470))


	# Setting the bullet image
	Bullet_surface = pygame.image.load('Graphics/Bullet.png').convert_alpha()
	Bullet_rect = Bullet_surface.get_rect(midbottom = (960, placingbulle))

	while True:

		# Quiting game function
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()


		# Setting Highscore
		Highscore_surf = Mainmenu_font.render(f'Highscore: {Highscore}', True, (255, 255, 255))
		Highscore_rect = Highscore_surf.get_rect(center = (450, 50))


		# Showing the games name
		screen.blit(space, (0,0))	
		pygame.draw.rect(screen,(0,0,0),Highscore_rect)
		pygame.draw.rect(screen,(255,255,255),Highscore_rect,2)
		screen.blit(Highscore_surf, Highscore_rect)


		# Renders the score
		score_surf = Mainmenu_font.render(f'Score: {score}', True, (255, 255, 255))
		score_rect = Highscore_surf.get_rect(center = (450, 150))


		# Showing your score
		pygame.draw.rect(screen,(0,0,0),score_rect)
		pygame.draw.rect(screen,(255,255,255),score_rect,2)
		screen.blit(score_surf, score_rect)
		screen.blit(Bullet_surface, Bullet_rect)



		# Bullet y movement
		placinglist = ["1", "2", "3"]
		placinglit = random.choice(placinglist)
		if placinglit == "1":
			placingbullet = 340
		elif placinglit == "2":
			placingbullet = 485
		elif placinglit == "3":
			placingbullet = 600

		# Bullet x movement
		Bullet_rect.x -= 6
		if Bullet_rect.right <= 0:
			Bullet_rect.left = 960
			score += 1
			placingbulle = placingbullet
			Bullet_surface = pygame.image.load('Graphics/Bullet.png').convert_alpha()
			Bullet_rect = Bullet_surface.get_rect(midbottom = (960, placingbulle))


		if score > Highscore:
			Highscore += 1



		# Player
		player_grav += 1
		player_rect.y += player_grav
		screen.blit(player_surf,player_rect)


		# Controls
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			player_grav = -20


		# Collision
		Collod = player_rect.colliderect(Bullet_rect)
		if Collod == True:
			score = 0


		# fps/clock speed
		pygame.display.update()
		clock.tick(60)