import pygame
from random import choice
from support import import_folder



    ### Let's create an animation player since we're importing many effects. We don't want the effects to be imported every time we summon a particle effect, it could cause slowdown
class AnimationPlayer:
    def __init__(self):
        self.frames = {
            'flame': import_folder('./img/particles/flame/frames'),
            'aura': import_folder('./img/particles/aura'),
            'heal': import_folder('./img/particles/heal/frames'),

            'claw': import_folder('./img/particles/claw'),
            'slash': import_folder('./img/particles/slash'),
            'sparkle': import_folder('./img/particles/sparkle'),
            'leaf_attack': import_folder('./img/particles/leaf_attack'),
            'thunder': import_folder('./img/particles/thunder'),

            'squid': import_folder('./img/particles/smoke_orange'),
            'raccoon': import_folder('./img/particles/raccoon'),
            'spirit': import_folder('./img/particles/nova'),
            'bamboo': import_folder('./img/particles/bamboo'),

            'leaf': (
                import_folder('./img/particles/leaf1'),
                import_folder('./img/particles/leaf2'),
                import_folder('./img/particles/leaf3'),
                import_folder('./img/particles/leaf4'),
                import_folder('./img/particles/leaf5'),
                import_folder('./img/particles/leaf6'),
                self.reflect_images(import_folder('./img/particles/leaf1')),
                self.reflect_images(import_folder('./img/particles/leaf2')),
                self.reflect_images(import_folder('./img/particles/leaf3')),
                self.reflect_images(import_folder('./img/particles/leaf4')),
                self.reflect_images(import_folder('./img/particles/leaf5')),
                self.reflect_images(import_folder('./img/particles/leaf6'))
            )
        }

        ### Allows us to flip the frame
    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames
        
    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, attack_type, pos, groups):
        animation_frames = self.frames[attack_type]
        ParticleEffect(pos, animation_frames, groups)



    ### Creates particle effects for all of the player/enemy attacks
class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()