from random import randint
import pygame
from particles import AnimationPlayer
from settings import *

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player


    def flame(self, player, cost, group):
        if player.energy >= cost:
            player.energy -= cost

            ### Detect what direction the fireball should shoot
            dir = player.status.split('_')[0]
            if dir == 'right': direction = pygame.math.Vector2(1,0)
            elif dir == 'left': direction = pygame.math.Vector2(-1,0)
            elif dir == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)

            for i in range(1, 6):
                if direction.x:
                    offset_x = (direction.x * i) * tilesize
                    x = player.rect.centerx + offset_x + randint(-tilesize // 3, tilesize // 3)
                    y = player.rect.centery
                    self.animation_player.create_particles('flame', (x, y), group)
                else:
                    offset_y = (direction.y * i) * tilesize
                    x = player.rect.centerx
                    y = player.rect.centery + offset_y + randint(-tilesize // 3, tilesize // 3)
                    self.animation_player.create_particles('flame', (x, y), group)



    def heal(self, player, strength, cost, group):
        if player.energy >= cost:
            player.health += strength

            if player.health > player.stats['health']:
                player.health = player.stats['health']

            player.energy -= cost
            self.animation_player.create_particles('heal', player.rect.center, group)
            self.animation_player.create_particles('aura', player.rect.center, group)
