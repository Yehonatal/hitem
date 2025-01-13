from constants import TARGET_SPEED, COLORS, TARGET_HEIGHT, TARGET_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH


class Target:
    def __init__(self, canvas):
        self.canvas = canvas
        self.speed = TARGET_SPEED
        self.x = WINDOW_WIDTH - TARGET_WIDTH - 50  # Position on right side
        self.y = 50
        self.width = TARGET_WIDTH
        self.height = TARGET_HEIGHT
        self.id = canvas.create_rectangle(
            self.x, self.y,
            self.x + self.width, self.y + self.height,
            fill=COLORS["target"]
        )
        self.direction = 1

    def move(self):
        """Move the target vertically and reverse direction upon hitting window edges."""
        self.canvas.move(self.id, 0, self.speed * self.direction)
        self.y += self.speed * self.direction

        if self.y <= 0 or self.y + self.height >= WINDOW_HEIGHT:
            self.direction *= -1

    def increase_speed(self, increment):
        """Increase the target's speed."""
        self.speed += increment

    def shrink(self):
        """Shrink the target's dimensions when hit."""
        new_width = max(20, self.width - 10)
        new_height = max(10, self.height - 5)

        if new_width != self.width or new_height != self.height:
            self.width = new_width
            self.height = new_height

            self.canvas.coords(
                self.id,
                self.x, self.y,
                self.x + self.width, self.y + self.height
            )

    def is_hit(self, ball):
        """Check if the ball has hit the target."""
        ball_coords = self.canvas.coords(ball.id)
        target_coords = self.canvas.coords(self.id)

        return (
            ball_coords[2] > target_coords[0] and
            ball_coords[0] < target_coords[2] and
            ball_coords[3] > target_coords[1] and
            ball_coords[1] < target_coords[3]
        )

    def reset(self):
        """Reset the target's position and size."""
        self.x = (WINDOW_WIDTH - TARGET_WIDTH) // 2
        self.y = 50

        self.width = TARGET_WIDTH
        self.height = TARGET_HEIGHT

        self.canvas.coords(
            self.id,
            self.x, self.y,
            self.x + self.width, self.y + self.height
        )
