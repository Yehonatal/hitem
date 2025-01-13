import unittest
from unittest.mock import MagicMock
from player import Player
from constants import PLAYER_START_X, PLAYER_START_Y, WINDOW_HEIGHT


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.canvas = MagicMock()
        self.player = Player(self.canvas)

    def test_initial_position(self):
        """Test if the player is initialized at the correct position."""
        self.assertEqual(self.player.x, PLAYER_START_X)
        self.assertEqual(self.player.y, PLAYER_START_Y)


if __name__ == '__main__':
    unittest.main()
