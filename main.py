import sys
import pygame
from setings import Settings

class Game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Атака пришельцев")
        #self.bg_color = (41, 179, 217)
        
    def run_game(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            self.screen.fill(self.settings.bg_color)
        
            pygame.display.flip()
        


if __name__ == '__main__':
    ai = Game()
    ai.run_game()