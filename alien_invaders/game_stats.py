class GameStats:
    """track teh stats of the game"""

    def __init__(self, ai_game):
        """init the stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        #start invasion game in an active state
        self.game_active = False

    def reset_stats(self):
        """Init stats that can change during the game"""
        self.ships_left = self.settings.ship_limit