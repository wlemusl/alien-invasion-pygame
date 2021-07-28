# Import required libraries
import sys
from time import sleep
import pygame
import pygame.font
from bullet import Bullet
from random import randrange
from alien import Alien

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, help_button):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, 
                              bullets, mouse_x, mouse_y)
            check_help_button(ai_settings, screen, stats, sb, help_button, ship, aliens, 
                              bullets, mouse_x, mouse_y)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Move the ship up:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move the ship down:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()
    elif event.key == pygame.K_p:
        pause(screen, ai_settings)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, 
                      bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked == True and stats.game_active == False:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens, stats)
        ship.center_ship()

def check_help_button(ai_settings, screen, stats, sb, help_button, ship, aliens, 
                      bullets, mouse_x, mouse_y):
    """Show the instructions of the game when the player clicks Help."""
    button_clicked = help_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked == True and stats.game_active == False:
        instructions = True
        while instructions:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        instructions = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
            screen.fill((230, 230, 230))

            pygame.font.init()
            screen_rect = screen.get_rect()

            myfont = pygame.font.SysFont('Consola', 80)
            text = myfont.render('Welcome to Alien Invasion!', True, (0, 185, 0), ai_settings.bg_color)
            text1_rect = text.get_rect()
            text1_rect.centerx = screen_rect.centerx
            text1_rect.centery = screen_rect.centery - 300
            screen.blit(text, text1_rect)
            
            line0 = 'The objective of this game is to destroy the fleet of aliens BEFORE it reaches earth or YOUR spaceship.' 
            line1 = 'The key facts that you must know:' 
            line2 = '  1. You have 4 spaceships, but if an alien crashes against your spaceship or against earth, then your' 
            line3 = '     current spaceship will be destroyed.' 
            line4 = '  2. Every time you lose a spaceship, the level which you are will restart and a new fleet will appear.'
            line5 = '  3. It is GAME OVER when you lose all your 4 spaceships.'
            line6 = '  4. The spaceship can shoot only 3 bullets at a time and it requieres one bullet to destroy an alien.'
            line7 = '  5. Every time you destroy an alien, you accumulate points. GO and try to beat the current high score!'
            line8 = '  6. Every time you kill a fleet of aliens, you go to the next level, where the speed of aliens boosts and/or'
            line9 = '     the number or aliens increases.'
            line10 = '  7. Move your spaceship with the Left, Right, Up, and Down arrow, and make it shoot with the spacebar.'
            line11 = '  8. While playing, press P to pause the game, C to continue playing, or Q to quit and exit the game.'
            messages = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11]
            
            count = 0
            for message in messages:
                myfont = pygame.font.SysFont('Consola', 30)
                text = myfont.render(message, True, (0, 0, 0), ai_settings.bg_color)
                text2_rect = text.get_rect()
                text2_rect.left = 80
                text2_rect.top = 180 + count*38
                count += 1
                screen.blit(text, text2_rect)
            
            myfont = pygame.font.SysFont('Consola', 32)
            text = myfont.render('Press C to continue back to the menu or Q to quit.', True, (185, 0, 0), 
                                 ai_settings.bg_color)
            text1_rect = text.get_rect()
            text1_rect.centerx = screen_rect.centerx
            text1_rect.centery = screen_rect.centery + 275
            screen.blit(text, text1_rect)
            
            pygame.display.flip()

def pause(screen, ai_settings):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        screen.fill((230, 230, 230))
        
        pygame.font.init()
        screen_rect = screen.get_rect()
        
        myfont = pygame.font.SysFont('Consola', 80)
        text = myfont.render('Paused Game!', True, (0, 185, 0), ai_settings.bg_color)
        text1_rect = text.get_rect()
        text1_rect.center = screen_rect.center
        screen.blit(text, text1_rect)
        
        myfont = pygame.font.SysFont('Consola', 32)
        text = myfont.render('Press C to continue playing or Q to quit.', True, (185, 0, 0))
        text2_rect = text.get_rect()
        text2_rect.centerx = screen_rect.centerx
        text2_rect.centery = screen_rect.centery + 70
        screen.blit(text, text2_rect)
        
        pygame.display.flip()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
                  play_button, help_button):
    """Update images on the screen and flip to the new screen."""
    
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)
    
    # Draw the score information.
    sb.show_score()
    
    # Draw the play button if the game is inactive.
    if stats.game_active == False:
        play_button.draw_button()
        help_button.draw_button()
        if stats.ships_left == 0:
            
            image = pygame.image.load('images/boom.png').convert_alpha()
            image_rect = image.get_rect()
            screen_rect = screen.get_rect()
            
            if ship.rect.bottom >= screen_rect.bottom:
                image_rect.centerx = ship.centerx
                image_rect.centery = ship.bottom - 40
                screen.blit(image, image_rect) 
            else:
                image_rect.centerx = ship.centerx
                image_rect.centery = ship.bottom
                screen.blit(image, image_rect)
            
            pygame.font.init()
            screen_rect = screen.get_rect()
            myfont = pygame.font.SysFont('arialblack', 130)
            text = myfont.render('GAME OVER', True, (210, 0, 0), None)
            text1_rect = text.get_rect()
            text1_rect.centerx = screen_rect.centerx
            text1_rect.centery = screen_rect.centery - 150
            screen.blit(text, text1_rect)
            
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    
    # Update bullet positions.
    bullets.update()
    
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
                                  aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
                                  aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
        
    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        
        if stats.level < 12:
            ai_settings.increase_speed_bef_12()
        elif stats.level >= 12 and stats.level < 20:
            ai_settings.increase_speed_bef_20()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens, stats)  

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        with open('ai_high_score.txt', 'r+') as file_object:
            file_object.truncate(0)
        with open('ai_high_score.txt', 'w') as file_object:
            file_object.write("{}".format(stats.score))
        sb.prep_high_score()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
     # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge, and then update 
    the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
        
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges() == True:
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    # Decrement ships_left.
    if stats.ships_left > 0:
        
        image = pygame.image.load('images/boom.png').convert_alpha()
        image_rect = image.get_rect()
        screen_rect = screen.get_rect()
        
        if ship.rect.bottom >= screen_rect.bottom:
            image_rect.centerx = ship.centerx
            image_rect.centery = ship.bottom - 40
            screen.blit(image, image_rect) 
        else:
            image_rect.centerx = ship.centerx
            image_rect.centery = ship.bottom
            screen.blit(image, image_rect)
        
        pygame.display.flip()
        
        # Decrement ships_left.
        stats.ships_left -= 1
        
        # Update scoreboard.
        sb.prep_ships()
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens, stats)
        ship.center_ship()

        # Pause.
        sleep(2)
    
    else:
        stats.game_active = False        
        pygame.mouse.set_visible(True)

def create_fleet(ai_settings, screen, ship, aliens, stats):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    if stats.level < 12:
        number_aliens = 32
    elif stats.level >= 12 and stats.level < 20:
        number_aliens = 46
    else:
        number_aliens = 60
    
    # Create the fleet of aliens.
    for alien in range(number_aliens):
        create_alien(ai_settings, screen, aliens, stats)

def create_alien(ai_settings, screen, aliens, stats):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    if stats.level < 12:
        alien.x = randrange(90, (ai_settings.screen_width - 90), (90))
        alien.rect.x = alien.x
        alien.rect.y = randrange(60, (ai_settings.screen_height - (alien_height * 6)), (60))  
    elif stats.level >= 12 and stats.level < 20:
        alien.x = randrange(90, (ai_settings.screen_width - 90), (90))
        alien.rect.x = alien.x
        alien.rect.y = randrange(60, (ai_settings.screen_height - (alien_height * 5)), (60))  
    else:
        alien.x = randrange(90, (ai_settings.screen_width - 90), (90))
        alien.rect.x = alien.x
        alien.rect.y = randrange(60, (ai_settings.screen_height - (alien_height * 4)), (60)) 
        
    aliens.add(alien)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

