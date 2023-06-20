# PythonSnake_game
This is a classic Snake game implemented in Python using the Pygame library.
# Snake Game

This is a simple Snake Game implemented in Python using the Pygame library.

## Getting Started

### Prerequisites

Make sure you have Python and Pygame installed on your system.

- Python: [Download Python](https://www.python.org/downloads/)
- Pygame: Install Pygame by running
  ```bash
pip install pygame`
  ```
### Running the Game

To run the game, execute the following command in your terminal:

```bash
python snake_game.py
```
### Game Overview
The game window has a grid-based layout where the snake moves around. The objective of the game is to eat the apples and grow the snake without colliding with the boundaries or its own body.

### Controls
Use the arrow keys to control the direction of the snake.
Press 'Q' to quit the game when prompted.
Press 'C' to restart the game when prompted.
### Code Structure
The code is structured into the following parts:

Initialization: The Pygame library is initialized, and variables for game settings and colors are defined.

Game Window: The game window dimensions are set, and the Pygame window is created.

Fonts: Different font sizes are defined for displaying text on the screen.

Helper Functions: The draw_text() function is defined to display text on the game window.

Game Loop: The main game loop is implemented, which handles user input, updates the game state, and redraws the game window.

Game Over: The game over screen is displayed when the snake collides with the boundaries or its own body. The user can choose to quit or play again.

Snake Movement: The snake's movement is controlled based on user input and updated in each iteration of the game loop. The snake's body segments are stored in a list.

Apple Generation: The apples are randomly generated on the game grid, and the snake's length is increased when it collides with an apple.

Collision Detection: The game checks for collisions between the snake's head and its body segments or the boundaries of the game window.

Drawing: The game window is cleared, and the snake, apples, and score are drawn on the screen.

Game Speed: The game clock is used to control the speed of the game.

## Acknowledgments
This Snake Game implementation is based on the tutorial by Clear Code: Snake Game using Python and Pygame
