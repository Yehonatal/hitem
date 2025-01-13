import unittest
from unittest.mock import MagicMock
from ball import Ball  # Import directly since we're in the game directory
from constants import WINDOW_WIDTH


class TestBall(unittest.TestCase):
    def setUp(self):
        self.canvas = MagicMock()  # Mock canvas to avoid Tkinter dependency
        # Initialize with example coordinates
        self.ball = Ball(self.canvas, 100, 100, 200, 200)

    def test_initial_position(self):
        """Test if the ball is initialized at the correct position."""
        self.assertEqual(self.ball.x, 100)
        self.assertEqual(self.ball.y, 100)

    def test_is_off_screen(self):
        """Test if the ball correctly identifies when it is off screen."""
        self.ball.x = WINDOW_WIDTH + 10  # Move it off screen
        self.assertTrue(self.ball.is_off_screen())


if __name__ == '__main__':
    unittest.main()
