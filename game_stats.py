class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        with open('ai_high_score.txt') as file_object:
            contents = file_object.read()
            score = contents[0:6]
            
        score = int(score)
        self.high_score = score
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit 
        self.score = 0
        self.level = 1

