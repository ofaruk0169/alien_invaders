import sys
import pygame

from settings import Settings

class AlienInvaders:
    """This class manages the assests and behaviour in the game"""

    def __init__(self):
        """Init the game and the resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Background color
        self.bg_color = (220, 220, 210)

    def run_game(self):
        "This is the main loop for the game"
        while True:
            #This watches keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw screen during each pass trhough loop
            self.screen.fill(self.settings.bg_color)

            #The most recently drawn screen is visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make an instance and run the game
    ai = AlienInvaders()
    ai.run_game()
