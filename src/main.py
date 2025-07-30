import pygame
from data.config.settings import *
from src.game import Game

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Mystic Meadows')
	clock = pygame.time.Clock()
	game = Game(screen, clock)
	game.run()