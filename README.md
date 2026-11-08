# Snake Game in Python (Tkinter)
---

A classic implementation of the Snake game developed in Python using the `tkinter` graphical user interface library. This project demonstrates core game development concepts, including architecture, real-time canvas updates, collision detection, and dynamic canvas rendering.

---

## Features

- **Architecture:** The game board utilizes a coordinate-mapped grid scaled via a constant tile size.
- **Dynamic Growth Mechanics:** The snake increases in length upon consuming food, and new food items are generated randomly across the grid.
- **Collision Detection Systems:** 
  - Boundary collision detection prevents the snake from exiting the playable area.
  - Self-collision detection triggers the termination sequence if the snake intersects its own body.
- **Responsive Controls:** Arrow key inputs are handled via event binding, featuring a directional lock to prevent immediate reverse movement.
- **State Management:** Implements a clean termination state ("Game Over") with a centered overlay message.

---

## Technical Requirements

- Python 3.x (with the standard `tkinter` library included).

---

## Execution Instructions

1. Download or clone the project repository to the local machine.
2. Open a terminal or command prompt within the project directory.
3. Execute the script using the following command:

```bash
python snake_game.py