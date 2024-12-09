class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1600
        self.screen_height = 1100
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 15
        self.ship_limit = 5

        # Bullet Settings
        self.bullet_speed = 30
        self.bullet_width = 60
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

