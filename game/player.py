from constants import PLAYER_START_X, PLAYER_START_Y, COLORS, WINDOW_HEIGHT


class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.width = 40
        self.height = 20
        self.id = canvas.create_rectangle(
            self.x - self.width // 2, self.y - self.height // 2,
            self.x + self.width // 2, self.y + self.height // 2,
            fill=COLORS["player"]
        )
