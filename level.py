import pygame
from player import Player
from settings import *
from tile import Tile
from debug import debug
from weapons import Weapon
from support import *
import random


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('./img/map_FloorBlocks.csv'),
            'grass': import_csv_layout('./img/map_Grass.csv'),
            'object': import_csv_layout('./img/map_Objects.csv')
        }

        graphics = {
            'grass': import_folder('./img/Terrain/Grass'),
            'objects': import_folder('./img/Terrain/Objects')
        }
        # print(list(graphics['objects']))
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * tilesize
                        y = row_index * tilesize

                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')

                        if style == 'grass':
                            new_choice = random.choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', new_choice)

                        if style == 'object':
                            new_choice = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', new_choice)

        self.player = Player((2000, 1430), [self.visible_sprites], self.obstacle_sprites)

    def create_attack(self):
        new_weapon = Weapon(self.player, [self.visible_sprites])

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.status)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # create the floor
        self.floor_surf = pygame.image.load('./img/Terrain/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

            ### This loop fixes the hitbox issues with overlapping sprites
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)