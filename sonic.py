import pygame
from pygame import *
pygame.init()

IMG_FACE = pygame.transform.scale(pygame.image.load("assets/sonic_face.png"), (65,70))
IMG_DROITE = pygame.transform.scale(pygame.image.load("assets/sonic_side_right.png"),(65,70))
IMG_GAUCHE = pygame.transform.scale(pygame.image.load("assets/sonic_side_left.png"),(65,70))
IMG_FAST_GAUCHE = pygame.transform.scale(pygame.image.load("assets/sonic_fast_left.png"),(65,70))
IMG_FAST_DROITE = pygame.transform.scale(pygame.image.load("assets/sonic_fast_right.png"),(65,70))

class Sonic(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.velocity = 2
		self.jump_height = 10
		self.speed = 4
		self.image = IMG_FACE
		self.rect = self.image.get_rect()
		self.rect.x = 310
		self.rect.y = 230

	def move_right(self):
		if self.rect.x < 550:
			self.rect.x += self.velocity
			self.image = IMG_DROITE

	def move_left(self):
		if self.rect.x > 0:
			self.rect.x -= self.velocity
			self.image = IMG_GAUCHE

	def move_stop(self):
		self.image = IMG_FACE

	def move_fast_right(self):
		if self.rect.x < 550:
			self.rect.x += self.speed
			self.image = IMG_FAST_DROITE

	def move_fast_left(self):
		if self.rect.x > 0:
			self.rect.x -= self.speed
			self.image = IMG_FAST_GAUCHE

	def jump(self):
		self.rect.y += self.jump_height
