import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Background color
        self.bg_color = (220, 220, 210)

    def run_game(self):   
        "This is the main loop for the game"
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()

            
            
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):

        """respond to key  when released events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create new bullet and add to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update position of bullets and get rid of old ones"""
        self.bullets.update()

        #get rid of bullets as they leave the top of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
        
        
    def _update_screen(self):
        """Redraw screen during each pass trhough loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        self.aliens.draw(self.screen) 

        #The most recently drawn screen is visible
        pygame.display.flip()

    def _create_fleet(self):
        """create a fleet of aliens"""
        #make an alien
        alien = Alien(self)
        self.aliens.add(alien)





if __name__ == '__main__':
    #Make an instance and run the game
    ai = AlienInvaders()
    ai.run_game()
