import pygame
from data.config.settings import *
from src.utils import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)

		self.import_assets()
		self.status = 'down_idle'
		self.frame_index = 0

		# General Setup
		self.image = self.animations[self.status][self.frame_index]
		self.rect = self.image.get_rect(center = pos)

		# Movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 200

	def import_assets(self):
		self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
									'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
									'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
									'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
									'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}
		
		for animation in self.animations.keys():
			full_path = 'assets/sprites/character/' + animation
			self.animations[animation] = import_folder(full_path)

	def animate(self, dt):
		self.frame_index += 4 * dt
		if self.frame_index >= len(self.animations[self.status]):
			self.frame_index = 0
		self.image = self.animations[self.status][int(self.frame_index)]

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_d]:
			self.direction.x = 1
		elif keys[pygame.K_a]:
			self.direction.x = -1
		else:
			self.direction.x = 0

	def move(self, dt):

		# Normalizing a vector
		if self.direction.magnitude() > 1:
			self.direction = self.direction.normalize()

		# Horizontal movement
		self.pos.x += self.direction.x * self.speed * dt
		self.rect.centerx = self.pos.x

		#Vertical movement
		self.pos.y += self.direction.y * self.speed * dt
		self.rect.centery = self.pos.y

	def update(self, dt):
		self.input()
		self.move(dt)