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
        self.moving_left = False
        self.moving_right = False
        
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):       
        
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed
            
        if self.moving_right and self.rect.left<self.setting.screen_width/4:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -= self.setting.ship_speed  
        self.rect.x = self.x    
        self.rect.y = self.y       
            
        

        
        
    def blitme(self):
        self.screen.blit(self.image,(self.x,self.y))