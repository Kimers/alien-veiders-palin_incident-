import sys
import pygame
from setings import Settings
from ship import Ship

class Game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Атака пришельцев")
        self.ship = Ship(self.screen)
        #self.bg_color = (41, 179, 217)
        
    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()

        
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()        
        

if __name__ == '__main__':
    ai = Game()
    ai.run_game()