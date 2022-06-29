import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        ### Pygame initialization
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        ### Change to fullscreen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        ### Add support for USB controllers
        # pygame.joystick.init()
        # joysticks = [ pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count()) ]

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__=='__main__':
    game = Game()
    game.run()