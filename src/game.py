import sys
import pygame
from src.farm import Farm

class Game:
	def __init__(self, screen, clock):
		self.screen = screen
		self.clock = clock
		self.farm = Farm()
		
	def run(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			
			dt = self.clock.tick(60) / 1000
			self.farm.run(dt)
			pygame.display.update()
		pygame.quit()
		sys.exit()