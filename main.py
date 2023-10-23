import tkinter as tk
from sudoku import SudokuBoard

sudokuboard = SudokuBoard()

root = tk.Tk()
root.title('Sudoku Solver')
root.geometry('500x500')
button = tk.Button(root, text='Solve', font=('Arial', 20), command=lambda: solve())
button.pack()
clear_button = tk.Button(root, text='Clear', font=('Arial', 20), command=lambda: clear())
clear_button.pack()
tk.Label(root, text='Sudoku Solver', font=('Arial', 20)).pack()
frame = tk.Frame(root)
frame.pack()
for row in range(9):
    for col in range(9):
        tk.Entry(frame, width=2, font=('Arial', 20)).grid(row=row, column=col)

def clear():
    global sudokuboard, frame
    sudokuboard = SudokuBoard()
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack()
    for row in range(9):
        for col in range(9):
            tk.Entry(frame, width=2, font=('Arial', 20)).grid(row=row, column=col)
    button['state'] = 'normal'

def solve():
    for row in range(9):
        for col in range(9):
            value = frame.grid_slaves(row=row, column=col)[0].get()
            if value != '':
                sudokuboard.edit_board(row, col, int(value))
    print(sudokuboard)

    empty_cells = sudokuboard.get_all_empty()
    tried_values = {}
    index = 0

    while index < len(empty_cells):
        row, col = empty_cells[index]
        if (row, col) not in tried_values:
            tried_values[(row, col)] = []
        possible_values = sudokuboard.get_all_possible_values(row, col)
        if len(possible_values) == 0:
            sudokuboard.edit_board(row, col, 0)
            index -= 1
            continue
        if len(tried_values[(row, col)]) == len(possible_values):
            sudokuboard.edit_board(row, col, 0)
            tried_values[(row, col)] = []
            index -= 1
            continue
        value = possible_values[len(tried_values[(row, col)])]
        sudokuboard.edit_board(row, col, value)
        tried_values[(row, col)].append(value)
        index += 1
        
    # def solve_per_cell(row, col):
    #     if (row, col) in sudokuboard.board:
    #         return solve_per_cell(row, col+1)
    #     if row == 9:
    #         return True
    #     possible_values = sudokuboard.get_all_possible_values(row, col)
    #     for value in possible_values:
    #         sudokuboard.edit_board(row, col, value)
    #         if solve_per_cell(row, col+1):
    #             return True
    #         sudokuboard.edit_board(row, col, 0)
    #     return False
    
    # solve_per_cell(0, 0)
    print(sudokuboard)
    for i in range(9):
        for j in range(9):
            frame.grid_slaves(row=i, column=j)[0].destroy()
            label = tk.Label(frame, text=sudokuboard.get(i, j), font=('Arial', 20)).grid(row=i, column=j)
    button['state'] = 'disabled'
root.mainloop()