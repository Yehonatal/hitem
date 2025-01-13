import unittest
from unittest.mock import MagicMock
from target import Target  # Import directly since we're in the game directory
from constants import WINDOW_WIDTH, TARGET_WIDTH


class TestTarget(unittest.TestCase):
    def setUp(self):
        self.canvas = MagicMock()  # Create a mock canvas to simulate Tkinter's canvas
        self.target = Target(self.canvas)

    def test_initial_position(self):
        """Test if the target is initialized at the correct position."""
        self.assertEqual(self.target.x, WINDOW_WIDTH - TARGET_WIDTH - 50)
        self.assertEqual(self.target.y, 50)

    def test_shrink(self):
        """Test if the target shrinks correctly."""
        initial_width = self.target.width
        initial_height = self.target.height

        self.target.shrink()

        if initial_width > 20:
            self.assertLess(self.target.width, initial_width)
        else:
            self.assertEqual(self.target.width, initial_width)

        if initial_height > 10:
            self.assertLess(self.target.height, initial_height)
        else:
            self.assertEqual(self.target.height, initial_height)


if __name__ == '__main__':
    unittest.main()
