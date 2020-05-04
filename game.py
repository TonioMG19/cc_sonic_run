import pygame
from sonic import Sonic
from pygame import *

pygame.init()

class Game:

	def __init__(self):

		self.sonic = Sonic()
		self.pressed = {}