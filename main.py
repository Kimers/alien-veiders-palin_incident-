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
        self.ship = Ship(self)
        #self.bg_color = (41, 179, 217)
        #Полный экран#
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height        
        
    def run_game(self):
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()

        
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
                                
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
                
     
    def _check_keydown(self,event):
        if event.key == pygame.K_UP:
            #self.ship.rect.y -= 1
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True                
        elif event.key == pygame.K_LSHIFT:
            self.settings.ship_speed +=0.5
        elif event.key == pygame.K_q:
            sys.exit()
     
     
    def _check_keyup(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False                 
        elif event.key == pygame.K_LSHIFT:
            self.settings.ship_speed -=0.5             
     
                    

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()        
        

if __name__ == '__main__':
    ai = Game()
    ai.run_game()