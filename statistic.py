class Game_stats():
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_activ = False
        
    def reset_stats(self):
        self.ship_left = self.settings.ship_limit