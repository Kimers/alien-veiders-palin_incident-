import pygame

class Ship():
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #self.setting = ai_game.setting
        
        self.image = pygame.image.load("image\MC4.png")
        self.rect = self.image.get_rect()
        self.moving_up = False
        self.moving_down = False
        
        self.rect.midleft = self.screen_rect.midleft
        
    def update(self):
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1
        
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)