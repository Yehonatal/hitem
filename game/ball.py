# ball.py
import math
from constants import BALL_RADIUS, COLORS, BALL_SPEED, WINDOW_HEIGHT, WINDOW_WIDTH


class Ball:
    def __init__(self, canvas, x, y, target_x, target_y):
        """Initialize a ball at the specified position."""
        self.canvas = canvas
        self.x = x
        self.y = y
        self.target_x = target_x   # Target coordinates will be set during shooting
        self.target_y = target_y

        # Calculate direction vector
        self.direction_x = target_x - x
        self.direction_y = target_y - y
        distance = math.sqrt(self.direction_x ** 2 + self.direction_y ** 2)

        # Normalize direction vector
        if distance != 0:
            self.direction_x /= distance
            self.direction_y /= distance

        # Create visual representation of the ball
        self.id = canvas.create_oval(
            x - BALL_RADIUS, y - BALL_RADIUS,
            x + BALL_RADIUS, y + BALL_RADIUS,
            fill=COLORS["ball"]
        )

    def move(self):
        """Move the ball in a straight line towards its target."""
        # Move based on normalized direction vector
        self.canvas.move(self.id, self.direction_x *
                         BALL_SPEED, self.direction_y * BALL_SPEED)

        # Update internal position for collision detection
        self.x += self.direction_x * BALL_SPEED
        self.y += self.direction_y * BALL_SPEED

    def is_off_screen(self):
        """Check if the ball has moved off-screen to the right."""
        return self.x > WINDOW_WIDTH + BALL_RADIUS  # Consider off-screen if x exceeds window width.
