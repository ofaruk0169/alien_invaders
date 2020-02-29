import pygame

class Ship:
    """This class will manage the ship"""

    def __init__(self, ai_game):
        """init the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Starts each ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # stores decimal value for ships horizontal position
        self.x = float(self.rect.x)

        #This is a flag for ship movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """The ships position is updated depending on the movement flag"""
        #update ships x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draws ship at current location"""
        self.screen.blit(self.image, self.rect)