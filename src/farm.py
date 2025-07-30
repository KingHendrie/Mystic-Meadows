import pygame
from data.config.settings import *
from src.player import Player
from src.ui import UI
from src.sprites import Generic

class Farm:
	def __init__(self):
		# Get the display surface
		self.display_surface = pygame.display.get_surface()

		# Sprite groups
		self.all_sprites = CameraGroup()

		self.setup()
		self.ui = UI(self.player)

	def setup(self):
		Generic(
			pos = (0,0),
			surf = pygame.image.load('assets/sprites/world/ground.png').convert_alpha(),
			groups = self.all_sprites,
			z = LAYERS['ground'])
		
		self.player = Player((640, 360), self.all_sprites)

	def run(self, dt):
		self.display_surface.fill('black')
		# self.all_sprites.draw(self.display_surface)
		self.all_sprites.custom_draw(self.player)
		self.all_sprites.update(dt)

		self.ui.display()

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player):
		self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
		self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

		for layer in LAYERS.values():
			for sprite in self.sprites():
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -= self.offset
					self.display_surface.blit(sprite.image, offset_rect)