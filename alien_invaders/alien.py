import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """this class represents an alien in the fleet"""

    def __init__(self, ai_game):
        """init the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #each new alien starts at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store horizontal position 
        self.x = float(self.rect.x)