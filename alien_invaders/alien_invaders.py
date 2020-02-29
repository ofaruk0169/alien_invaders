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

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
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
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    

    def _check_keydown_events(self, event):

        """respond to key events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):

        """respond to key  when released events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        
        
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
