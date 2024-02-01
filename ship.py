import pygame

class Ship():
    def __init__(self,ai_game):
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()
        
        self.image = pygame.image.load("image\MC4.png")
        self.rect = self.image.get_rect()
        
        self.rect.midleft = self.screen_rect.midleft
        
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)