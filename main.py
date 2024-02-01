import sys
import pygame

class Game():
    def __init__(self):
        pygame.init()
        
        self.window = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Атака пришельцев")
        self.bg_color = (41, 179, 217)
        
    def ran_game(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
        self.window.fill(self.bg_color)
                    
        pygame.display.flip()
        


if __name__ == '__main__':
    ai = Game()
    ai.ran_game()