class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1600
        self.screen_height = 1100
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 5

        # Bullet Settings
        self.bullet_width = 60
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50

        # How quickly the game speeds up
        self.speedup_scale = 1.2

        # How quickly the score increases
        self.score_scale = 2.0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Change is speed per level"""
        self.ship_speed = 20
        self.bullet_speed = 5.0
        self.alien_speed = 1.0

        # Score settings
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        
