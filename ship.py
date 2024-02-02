import pygame

class Ship():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings
        
        
        self.image = pygame.image.load("image\MC4.png")
        self.rect = self.image.get_rect()
        
        self.moving_up = False
        self.moving_down = False
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        
    def update(self):
        if self.moving_up:
            self.y -= self.setting.ship_speed
        if self.moving_down:
            self.y += self.setting.ship_speed
        self.rect.y = self.y
        
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)