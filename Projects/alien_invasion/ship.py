import pygame
from Projects.alien_invasion.settings import  Settings


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.rect = self.image.get_rect()
        # Start each new ship at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def match_image_background(self):
        self.image.set_colorkey((230, 230, 230))  # Set background's image transparent
