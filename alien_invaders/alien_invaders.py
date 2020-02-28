import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvaders:
    """This class manages the assests and behaviour in the game"""

    def __init__(self):
        """Init the game and the resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #Background color
        self.bg_color = (220, 220, 210)

    def run_game(self):
        "This is the main loop for the game"
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    def _check_events(self):
        """#This watches keyboard and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    #move ship right
                    

    def _update_screen(self):
        """Redraw screen during each pass trhough loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #The most recently drawn screen is visible
        pygame.display.flip()





if __name__ == '__main__':
    #Make an instance and run the game
    ai = AlienInvaders()
    ai.run_game()
