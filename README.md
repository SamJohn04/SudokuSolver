# SUDOKU SOLVER

### Python implementation of Sudoku Solver.

Insert the Sudoku contents via the GUI app and solve!
Use clear button to solve another sudoku.

### Implementation details

The board itself is represented by a class for the same, within which it is stored as a dictionary. GUI app implemented using tkinter.

The original implementation was to use recursion, which fell short due to exceeding maximum depth of recursion   
**Current Solution:** Maintain an index to traverse through all the empty cells. The index is built to traverse in both directions.