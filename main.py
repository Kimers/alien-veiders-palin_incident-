import sys
import pygame
from time import sleep
from setings import Settings
from ship import Ship
from enemy import Enemy
from bullet import Bullet
from statistic import Game_stats
from button import Button

class Game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Атака пришельцев")
        self.stats = Game_stats(self)
        self.ship = Ship(self)
        self.enemy = pygame.sprite.Group()
        self.bullet = pygame.sprite.Group()
        
        self._create_enemy()
        
        
        #self.bg_color = (41, 179, 217)
        #Полный экран#
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height    
        
        self.play_button = Button(self,"Играть")
        
    def run_game(self):
        while True:
            self._check_event()
            
            if self.stats.game_activ:
            
                self.ship.update()
                self._update_bullet()
                self._update_enemy()
            self._update_screen()

        
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
                
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
                                
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
                
                
    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_activ = True
                
     
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
        elif event.key == pygame.K_SPACE:
            self._fire()
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
            
            
    def _create_enemy(self):
        enemy = Enemy(self)
        enemy_width , enemy_height = enemy.rect.size
        
        ship_width = self.ship.rect.width
        avalible_space_x = ((self.settings.screen_width) - (2*enemy_width) - ship_width)        
        
        avalible_space_y = self.settings.screen_height - (2*enemy_height)
        avalible_enemy_y = avalible_space_y // (2*enemy_height)
        #self.enemy.add(enemy)
        
        print(avalible_space_x)
        print(avalible_space_y)
        
        number_ruw = avalible_space_x // (2*enemy_width)
        
        
        for ruw_number in range(number_ruw):
            for enemy_number in range(avalible_enemy_y):
                self._create_enemys(enemy_number,ruw_number)
            #print(len(self.enemy))
            
    
    def _create_enemys(self,enemy_number,ruw_number):
        enemy = Enemy(self)
        enemy_width , enemy_height = enemy.rect.size
        enemy.y = enemy_height + 2 * enemy_height * enemy_number
        enemy.rect.y = enemy.y
        enemy.rect.x = self.settings.screen_width - (enemy.rect.width + 2 * enemy.rect.width * ruw_number)
        #print(enemy.rect.x)
        #print(enemy.rect.y)

        self.enemy.add(enemy)
        
        
    def _check_flee_edge(self):
        for enemy in self.enemy.sprites():
            if enemy.check_gran():
                self.change_direct()
                break
            
    def change_direct(self):
        for enemy in self.enemy.sprites():
            enemy.rect.x -= self.settings.enemy_closespeed
        self.settings.flee_direction *= -1
        
        
        
    def _update_enemy(self):
        self._check_flee_edge()
        self.enemy.update()
        
        if pygame.sprite.spritecollideany(self.ship , self.enemy):
            #print ("Попали")
            self._ship_hit()
    

        
        
        
            
    def _fire(self):
        if len(self.bullet) <= self.settings.bullet_allow:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)
            
    def _update_bullet(self):
        self.bullet.update()
        for bullet in self.bullet.copy():
            if bullet.rect.right>=self.settings.screen_width:
                self.bullet.remove(bullet)
        #print(len(self.bullet))
        
        self._chek_col()
        
        
    

     
    def _chek_col(self):
        collision = pygame.sprite.groupcollide(self.bullet , self.enemy , True , True)
        if not self.enemy:
            self.bullet.empty()
            self._create_enemy()
            
            
    def _ship_hit(self):
        if self.stats.ship_left>0:
            self.stats.ship_left -= 1
        
            self.enemy.empty()
            self.bullet.empty()
            self._create_enemy()
            self.ship.center_ship()
        
            sleep(0.5)
            print(self.stats.game_activ)
            
        else:
            self.stats.game_activ = False
            print(self.stats.game_activ)
        
        
        
                    

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draft_bullet()
        self.enemy.draw(self.screen)
        
        if not self.stats.game_activ:
            self.play_button.draw_button()
        
        pygame.display.flip()        
        

if __name__ == '__main__':
    ai = Game()
    ai.run_game()