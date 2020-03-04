import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
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

        #store game stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Make play button
        self.play_button = Button(self, "Play")

        #Background color
        self.bg_color = (220, 220, 210)

    def run_game(self):   
        "This is the main loop for the game"
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()

            
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    
    def _check_play_button(self, mouse_pos):
        #starts game as click mouse
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True

            #get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create new fleet and centre the ship
            self._create_fleet()
            self.ship.center_ship()
            #Hide mouse
            pygame.mouse.set_visible(False)

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

        self._check_bullet_alien_collision()

        

    def _check_bullet_alien_collision(self):
        """Respond to alien bullet collisions"""
        #remove alien and bullets that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            #detroy existing bullets and create new fleets
            self.bullets.empty()
            self._create_fleet()

        
        
    def _update_screen(self):
        """Redraw screen during each pass trhough loop"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        self.aliens.draw(self.screen) 

        #Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        #The most recently drawn screen is visible
        pygame.display.flip()

    def _create_fleet(self):
        """create a fleet of aliens"""
        #make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # The available space for teh aliens is calculated as double the width of an alien is taken away from the screen length 
        available_space_x = self.settings.screen_width - (2 * alien_width)
        #The spacing between aliens. So double alien width divided by the available space.
        number_aliens_x = available_space_x // (2 * alien_width)

        #Number of rows aliens will fit inside
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #create fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """create alien in row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Check if aliens are at the edge then Update the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        #look for alien ship collision

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #look for aliens hitting the bottomof the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if aliens have reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """respond to ship being hit by the alien"""
        if self.stats.ships_left > 0:
            #decrement ships left
            self.stats.ships_left -= 1

            #get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create new fleet and centre the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            

        

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat like if ship is hit
                self._ship_hit()
                break

            
            





if __name__ == '__main__':
    #Make an instance and run the game
    ai = AlienInvaders()
    ai.run_game()
