from constants import COLORS, MAX_BALLS, WINDOW_WIDTH, WINDOW_HEIGHT
from target import Target
from ball import Ball
from player import Player


class GameLogic:
    def __init__(self, canvas, score_label, ball_label):
        self.canvas = canvas
        self.player = Player(canvas)  # Initialize the player
        self.target = Target(canvas)   # Initialize the target
        self.balls = []
        self.remaining_balls = MAX_BALLS
        self.score = 0
        self.score_label = score_label
        self.ball_label = ball_label
        self.level = 1

    def shoot_ball(self):
        """Shoot a ball from the player's position."""
        if self.remaining_balls > 0:
            player_x = self.player.x
            player_y = self.player.y

            target_x = self.target.x + \
                (self.target.width // 2)  # Center of target
            target_y = self.target.y + \
                (self.target.height // 2)  # Center of target

            # Create and append a new Ball instance without decrementing remaining_balls
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
                                       self.remaining_balls}")  # Update UI

                if self.remaining_balls == 0:
                    return False

                continue

            if self.target.is_hit(ball):
                self.score += 10
                self.score_label.config(text=f"Score: {self.score}")
                self.target.shrink()
                self.canvas.delete(ball.id)
                self.balls.remove(ball)

        return True  # Return true if game continues

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
