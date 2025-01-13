from constants import COLORS, MAX_BALLS, WINDOW_WIDTH, WINDOW_HEIGHT, TARGET_SPEED
from ball import Ball
from target import Target
from player import Player


class GameLogic:
    def __init__(self, canvas, score_label, ball_label, level_label):
        self.canvas = canvas
        self.player = Player(canvas)  # Initialize the player
        self.target = Target(canvas)   # Initialize the target
        self.balls = []
        self.remaining_balls = MAX_BALLS
        self.score = 0
        self.level = 1
        self.score_label = score_label
        self.ball_label = ball_label
        self.level_label = level_label

    def shoot_ball(self):
        """Shoot a ball from the player's position."""
        if self.remaining_balls > 0:
            player_x = self.player.x
            player_y = self.player.y

            target_x = self.target.x + \
                (self.target.width // 2)
            target_y = self.target.y + \
                (self.target.height // 2)

            ball = Ball(self.canvas, player_x, player_y, target_x, target_y)
            self.balls.append(ball)

    def update_game(self):
        """Update game state: move target, move balls, check for hits."""
        self.target.move()  # Move the target

        for ball in list(self.balls):
            ball.move()

            if ball.is_off_screen():
                self.canvas.delete(ball.id)
                self.balls.remove(ball)
                self.remaining_balls -= 1
                self.ball_label.config(text=f"Balls Left: {
                                       self.remaining_balls}")

                if self.remaining_balls == 0:
                    return False  # Game over condition

                continue

            if self.target.is_hit(ball):
                self.score += 10
                self.score_label.config(text=f"Score: {self.score}")
                self.target.shrink()  # Shrink the target on hit
                self.canvas.delete(ball.id)
                self.balls.remove(ball)

                # Level up logic
                if self.score >= (100 * self.level):
                    self.level += 1  # Increase level
                    self.target.increase_speed(4)

                    if hasattr(self.level_label, 'config'):
                        self.level_label.config(text=f"Level: {self.level}")

        return True

    def reset_game(self):
        """Reset game state for a new game."""
        self.remaining_balls = MAX_BALLS
        self.score = 0
        self.level = 1
        self.balls.clear()

        if self.ball_label:
            self.ball_label.config(text=f"Balls Left: {self.remaining_balls}")

        if self.score_label:
            self.score_label.config(text=f"Score: {self.score}")

        if hasattr(self.level_label, 'config'):
            self.level_label.config(text=f"Level: {self.level}")
