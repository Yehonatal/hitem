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

        self.direction_x = target_x - x
        self.direction_y = target_y - y
        distance = math.sqrt(self.direction_x ** 2 + self.direction_y ** 2)

        if distance != 0:
            self.direction_x /= distance
            self.direction_y /= distance

        self.id = canvas.create_oval(
            x - BALL_RADIUS, y - BALL_RADIUS,
            x + BALL_RADIUS, y + BALL_RADIUS,
            fill=COLORS["ball"]
        )

    def move(self):
        """Move the ball in a straight line towards its target."""
        self.canvas.move(self.id, self.direction_x *
                         BALL_SPEED, self.direction_y * BALL_SPEED)

        self.x += self.direction_x * BALL_SPEED
        self.y += self.direction_y * BALL_SPEED

    def is_off_screen(self):
        return (self.x < 0 or self.x > WINDOW_WIDTH or
                self.y < 0 or self.y > WINDOW_HEIGHT)
