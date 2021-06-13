class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (210, 1, 46)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.05
        self.fleet_drop_speed = 100
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

