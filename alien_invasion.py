#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import required libraries
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from play_button import PlayButton
from help_button import HelpButton
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from random import randrange


# In[2]:


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play button.
    play_button = PlayButton(ai_settings, screen, "Play")
    
    # Make the Help button.
    help_button = HelpButton(ai_settings, screen, "Help")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens, stats)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, help_button)
        
        if stats.game_active == True:
            ship.update()
            gf.update_bullets(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
                         play_button, help_button)


# In[3]:


run_game()
