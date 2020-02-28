import pygame

class Ship:
    """This class will manage the ship"""

    def __init__(self, ai_game):
        """init the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Starts each ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #This is a flag for ship movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """The ships position is updated depending on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """draws ship at current location"""
        self.screen.blit(self.image, self.rect)