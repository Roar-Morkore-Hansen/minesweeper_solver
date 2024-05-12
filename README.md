# Minesweeper Solver

run: python minesweeper_solver.py

## Overview
This is a Python program designed to solve Minesweeper puzzles. Minesweeper is a game where the player has to flag all the mines on a blank grid. When a blank cell is clicked, it can be a mine or a number. The number tells the player the number of mines in the adjacent cells.

## Design
The program offers two main actions: flagging and clicking.

- **Flagging**: A blank cell is flagged if the number of bombs in the adjacent cells minus the number of flagged cells is equal to the number of blank cells.
  
- **Clicking**: All the blank adjacent cells are clicked if the number of bombs is equal to the number of flagged cells. This indicates that there can be no bombs in the remaining cells.

## Implementation
The program uses Selenium to interact with the Minesweeper game at minesweeperonline.com. It iterates through every cell from top left to bottom right and checks the adjacent cells of all numbered cells, using the flag or click algorithm to determin if what action should be taken.

## Evaluation
This implementation serves as a good first iteration, but it has certain limitations. One issue is the potential for deadlock. Future implementations should address this issue by:

- Implementing a recursive depth-first solving algorithm instead of the brute-force method of iterating through the grid.
- Implement deadlock detection and a way to break deadlock by clicking on a onsertain tile.
- Optimizing the algorithm to skip checking cells that don't have any adjacent blank spaces.

Testing procedures should also be added to ensure the robustness of the program. Additionally, there is a known issue where the program crashes when the Minesweeper game is completed, which needs to be addressed in future updates. 

## Future Improvements
- Handle deadlocks by clicking random cells.
- Implement a recursive depth-first solving algorithm.
- Optimize the algorithm to skip checking cells without adjacent blank spaces.
- Add testing procedures to ensure robustness.
- Address the issue causing the program to crash upon completing the Minesweeper game.
