import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """this class represents an alien in the fleet"""

    def __init__(self, ai_game):
        """init the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #each new alien starts at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store horizontal position 
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Check true if alien has hit edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True