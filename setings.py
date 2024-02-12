class Settings():
    def __init__(self):
        #Размер монитора#
        self.screen_width = 1200
        self.screen_height = 900
        #Цвет фона#
        self.bg_color = (128, 130, 152)
        #Персонаж#
        self.ship_speed = 1.25
        self.ship_limit = 3
        #Пуля#
        self.bullet_allow = 5
        self.bullet_speed = 2
        self.bullet_width= 15
        self.bullet_height = 2
        self.bullet_color = (255, 255, 0)
        #Враги
        self.enemy_speed = 0.45
        self.enemy_closespeed = 15
        self.flee_direction = 1