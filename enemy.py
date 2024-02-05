import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('image/enemy1.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.screen.get_rect().width - self.rect.width
        self.rect.y = self.rect.height
        
        self.y = float(self.rect.y)
        
        
    def check_gran(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or screen_rect.top>self.rect.top:
            print("True")
            return True
        else:
            return False
        print (self.screen.get_rect())
        
        
    def update(self):
        self.y += (self.settings.enemy_speed * self.settings.flee_direction)
        self.rect.y = self.y