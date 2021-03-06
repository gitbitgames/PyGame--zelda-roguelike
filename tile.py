import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((tilesize, tilesize))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = ( pos[0], pos[1]-tilesize ))
        else:
            self.rect = self.image.get_rect(topleft = pos)

        if self.rect.height == 128:
            if self.rect.width == 128:
                self.hitbox = self.rect.inflate(-20, -60)
            else:
                self.hitbox = self.rect.inflate(-15, -80)
        else:
            self.hitbox = self.rect.inflate(-15, -30)
            self.rect.y += 20