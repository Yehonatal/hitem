# Python GUI Game with Tkinter

## Project Overview
This project is a single-player Python game developed using Tkinter and John Zelle's simple object-oriented graphics library. The game provides an interactive graphical interface where the player shoots moving balls at a vertically moving target. The target and balls shrink upon hits, progressively increasing the difficulty.

---

## Features

### Core Components
- **Playing Box**: A canvas serves as the game area.
- **Player**: A fixed position from where balls are launched.
- **Target Object**: A moving object that the player aims to hit.
- **Ball (Projectile)**: The object shot by the player to hit the target.

### Game Logic
- The player starts with 3 balls.
- **On Target Hit**:
  - The target shrinks, increasing difficulty.
  - The ball shrinks.
  - Score increases (optional multiplier).
  - Level increases (optional).
- **On Target Miss**:
  - The player loses one ball.
  - Game continues with the remaining balls.
- **Game Over**:
  - Occurs when all balls are used.
  - Displays high score (optional).
  - Offers the option to start a new game (optional).

---

## Optional Features
- **Score Counter**: Displays the current score.
- **Level Counter**: Tracks the player's progression.
- **Ball Counter**: Shows the remaining balls.
- **Multiplier Rule**: Increases score multiplier with each level.
- **High Score**: Stores and displays the highest score.
- **New Game Window**: Provides an option to restart after game over.

---

## Folder Structure
```
project_root/
├── game/
│   ├── __init__.py           # Package initializer
│   ├── main.py               # Entry point of the game
│   ├── player.py             # Player-related classes and logic
│   ├── target.py             # Target-related classes and logic
│   ├── ball.py               # Ball-related classes and logic
│   ├── game_logic.py         # Core game logic and utility functions
│   ├── constants.py          # Global constants
│   └── assets/
│       ├── sounds/           # Sound files (optional)
│       ├── images/           # Images or icons (optional)
│       └── fonts/            # Custom fonts (optional)
├── tests/
│   ├── __init__.py           # Package initializer for tests
│   ├── test_game_logic.py    # Unit tests for game logic
│   ├── test_player.py        # Unit tests for player logic
│   ├── test_target.py        # Unit tests for target logic
│   └── test_ball.py          # Unit tests for ball logic
├── requirements.txt          # Python dependencies (if needed)
├── README.md                 # Project description and setup instructions
└── LICENSE                   # License file (optional)
```

---

## How to Run the Game
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project_root
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python game/main.py
   ```

---

## Future Improvements
- Add sound effects for hits and misses.
- Include more complex target movements (e.g., diagonal or random patterns).
- Introduce power-ups or bonus balls.
- Implement a pause/resume feature.
- Enhance UI with custom graphics and animations.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **Tkinter**: For the GUI framework.
- **John Zelle's Graphics Library**: For object-oriented graphics capabilities.


