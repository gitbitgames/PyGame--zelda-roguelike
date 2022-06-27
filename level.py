import pygame
from settings import *
from tile import Tile

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(world_map):
            for col_index, col in enumerate(row):
                x = col_index * tilesize
                y = row_index * tilesize
                if col == 'x':
                    Tile((x, y),[self.visible_sprites])

    def run(self):
        pass