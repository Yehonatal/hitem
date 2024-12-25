import tkinter as tk
from game_logic import GameLogic
from player import Player
from target import Target
from ball import Ball
from constants import CANVAS_WIDTH, CANVAS_HEIGHT, COLORS

class Game:
    def __init__(self, root):
        self.root = root 
        self.root.title("HITEM GAME")


        self.canvas = tk.Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=COLORS["background"])
        self.canvas.pack()
    
    def setup_game(self):
        ...
    
    def shoot_ball(self, event):
        ...

    def update_game(self):
        ...

    def run(self):
        self.update_game()
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    game.run()