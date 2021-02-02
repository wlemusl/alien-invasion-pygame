#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Settings():
    """A class to store all settings for Alien Invasion Game."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings.
        self.ship_limit = 3
        self.ship_speed_factor = 0.8
        
        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullet_speed_factor = 0.6
        self.bullets_allowed = 3
        
        # Alien settings.
        self.fleet_drop_speed = 12
        
        # How quickly the game speeds up.
        self.speedup_scale = 1.07
        # How quickly the alien point values increase.
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.alien_speed_factor = 0.15
        
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Scoring.
        self.alien_points = 10
        
    def increase_speed_bef_12(self):
        """Increase speed settings and alien point values up to level 10."""
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        
    def increase_speed_bef_20(self):
        """Increase speed settings and alien point values after level 10."""
        # 0.9533 so the speedup_scale goes from 7% to 2%.
        self.alien_speed_factor *= self.speedup_scale*0.9533
        
        self.alien_points = int(self.alien_points * self.score_scale)




