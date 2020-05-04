import pygame
from pygame import *
from game import Game
pygame.init()

IMG_FACE2 = pygame.transform.scale(pygame.image.load("assets/sonic_face.png"), (65,70))
fenetre = pygame.display.set_mode((620,318))
pygame.display.set_caption("Mon super sonic !")

background = pygame.image.load("assets/background.png")

game = Game()

continuer = 1

while continuer:

	fenetre.blit(background,(0,0))

	fenetre.blit(game.sonic.image, game.sonic.rect)


	if game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_SPACE):
		game.sonic.move_fast_right()
	elif game.pressed.get(pygame.K_LEFT) and game.pressed.get(pygame.K_SPACE):
		game.sonic.move_fast_left()
	elif game.pressed.get(pygame.K_RIGHT):
		game.sonic.move_right()
	#	game.sonic.image = game.sonic.img_droite
	elif game.pressed.get(pygame.K_LEFT):
		game.sonic.move_left()
	#	game.sonic.image = game.sonic.img_gauche
	elif game.pressed.get(pygame.K_DOWN):
		game.sonic.move_stop()


	#if not(game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_LEFT)):
		#game.sonic.image = IMG_FACE2

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True
		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False

pygame.quit()