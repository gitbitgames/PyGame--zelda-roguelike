import sys
from numpy import full
import pygame
from settings import *
from support import *
from weapons import Weapon
from magic import Magic

class Player(pygame.sprite.Sprite):
    def __init__(self,
                pos,
                groups,
                obstacle_sprites,
                create_attack,
                destroy_attack,
                create_magic,
                destroy_magic
                ):

        super().__init__(groups)

        ### Player rectangle
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)

        ### Movement
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites

        ### Attacks
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = 0
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        
        ### Weapon selection
        self.weapon_index = 0
        self.weapon = list( weapon_data.keys() )[self.weapon_index]
        self.change_weapon = False
        self.change_timer = 0
        self.change_cooldown = 180

        ### Magic attacks
        self.magicking = False
        self.magic_cooldown = 1000
        self.magic_time = 0
        self.create_magic = create_magic
        self.destroy_magic = destroy_magic
        

        ### Magic selection
        self.magic_index = 0
        self.style = list( magic_data.keys() )[self.magic_index]
        self.change_magic = False
        self.change_mag_timer = 0
        self.change_mag_cooldown = 180
        self.magic_cost = magic_data[self.style]['cost']
        self.magic_strength = magic_data[self.style]['strength']

        ### Stats
        self.stats = {
            'health': 100,
            'energy': 60,
            'attack': 10,
            'magic': 4,
            'speed': 6
            }
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 123
        self.speed = self.stats['speed'] + weapon_data[self.weapon]['speed']
        self.magic_power = self.stats['magic'] + self.magic_strength

        ### Animations
        self.animations = self.import_player_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        self.animation_speed = 0.15

        ### Import all assets related to the player character's movement
    def import_player_assets(self):
        character_path = './img/player/'
        animations = {
            'up': [],
            'down': [],
            'left': [],
            'right': [],
            'right_idle': [],
            'left_idle': [],
            'up_idle': [],
            'down_idle': [],
            'right_attack': [],
            'left_attack': [],
            'up_attack': [],
            'down_attack': [],
        }
        for animation in animations.keys():
            full_path = character_path + animation
            animations[animation] = import_folder(full_path)
        return animations

        ### Detect keyboard events
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

        if keys[pygame.K_ESCAPE]:
            sys.exit()

        if keys[pygame.K_z] and not self.change_weapon:
            self._change_weapon('down')
            self.change_weapon = True
            self.change_timer = pygame.time.get_ticks()

        if keys[pygame.K_x] and not self.change_weapon:
            self._change_weapon('up')
            self.change_weapon = True
            self.change_timer = pygame.time.get_ticks()

        if keys[pygame.K_END] and not self.change_magic:
            self._change_magic()
            self.change_magic = True
            self.change_mag_timer = pygame.time.get_ticks()

        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.create_attack()

        if keys[pygame.K_LCTRL] and not self.magicking:
            self.magicking = True
            self.magic_time = pygame.time.get_ticks()
            self.create_magic(self.style, self.magic_power, self.magic_cost)

        ### Retrieves a status on what the player sprite is currently doing
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking or self.magicking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status[:-5]
                self.status = self.status + '_attack'
        elif 'attack' in self.status:
            self.status = self.status[:-7]

        ### Governs basic foot movement
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

        ### Collisions detection
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

        ### Changes the weapon and updates player stats
    def _change_weapon(self, type):
        if type == 'down':
            self.weapon_index -= 1
        elif type == 'up':
            self.weapon_index += 1

        length = len(weapon_data.keys())
        if self.weapon_index < 0:
            self.weapon_index = length-1
        if self.weapon_index > length-1:
            self.weapon_index = 0
        self.weapon = list( weapon_data.keys() )[self.weapon_index]
        self.stats['attack'] = weapon_data[self.weapon]['damage']
        self.stats['speed'] = weapon_data[self.weapon]['speed']
        self.attack_cooldown = weapon_data[self.weapon]['cooldown']

    def _change_magic(self):
        self.magic_index += 1

        length = len(magic_data.keys())
        if self.magic_index > length-1:
            self.magic_index = 0
        self.style = list( magic_data.keys() )[self.magic_index]
        self.magic_power = magic_data[self.style]['strength']
        self.magic_cost = magic_data[self.style]['cost']


        ### Governs player cooldowns for both switching weapons/magic, using weapons/magic
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

        if self.change_weapon:
            if current_time - self.change_timer >= self.change_cooldown:
                self.change_weapon = False

        if self.magicking:
            if current_time - self.magic_time >= self.magic_cooldown:
                self.magicking = False
                self.destroy_magic()

        if self.change_magic:
            if current_time - self.change_mag_timer >= self.change_mag_cooldown:
                self.change_magic = False

        ### Animate the player
    def animate(self):
        animation = self.animations[self.status]

        # Loop our frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # Round the index and set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        ### Continuously runs the 'always-on' player functions
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)