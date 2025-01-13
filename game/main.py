import tkinter as tk
from ball import Ball
from game_logic import GameLogic
from constants import COLORS, FONT_FAMILY, WINDOW_WIDTH, WINDOW_HEIGHT, MAX_BALLS


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python GUI Game")

        self.canvas = tk.Canvas(
            self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="white")
        self.canvas.pack()

        self.score_label = tk.Label(
            self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack()

        self.ball_label = tk.Label(self.root, text=f"Balls Left: {
                                   MAX_BALLS}", font=("Arial", 14))
        self.ball_label.pack()

        self.level_label = tk.Label(
            self.root, text="Level: 1", font=("Arial", 14))
        self.level_label.pack()

        self.logic = GameLogic(self.canvas, self.score_label,
                               self.ball_label, self.level_label)

        self.canvas.bind("<Button-1>", self.shoot_ball)

        self.restart_button = tk.Button(
            self.root,
            text="Restart",
            font=("Arial", 14),
            command=self.restart_game
        )

        self.update_game()
        self.root.mainloop()

    def shoot_ball(self, event):
        """Shoot a ball towards the clicked position."""
        if self.logic.remaining_balls > 0:
            player_x = self.logic.player.x
            player_y = self.logic.player.y

            ball = Ball(self.canvas, player_x, player_y, event.x, event.y)
            self.logic.balls.append(ball)

    def update_game(self):
        """Update the game state."""
        if self.logic.update_game():
            self.root.after(50, self.update_game)
        else:
            self.display_game_over()

    def display_game_over(self):
        """Display the game over message and show the restart button."""
        self.canvas.delete("all")

        self.canvas.create_text(
            WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20,
            text=f"Game Over! Final Score: {self.logic.score}",
            font=(FONT_FAMILY, 24),
            fill=COLORS["text"]
        )

        self.restart_button.pack()  # Pack the button to make it visible

    def restart_game(self):
        """Restart the game by resetting logic and UI elements."""
        self.canvas.delete("all")

        self.score_label.config(text="Score: 0")
        self.ball_label.config(text=f"Balls Left: {MAX_BALLS}")

        self.level_label.config(text="Level: 1")

        self.logic = GameLogic(self.canvas, self.score_label,
                               self.ball_label, self.level_label)

        self.restart_button.pack_forget()

        self.update_game()


if __name__ == "__main__":
    Game()
