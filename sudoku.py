class SudokuBoard:
    def __init__(self, board = None):
        if board is None:
            self.board = {}
        else:
            self.board = board
    def edit_board(self, row, col, value):
        self.board[(row, col)] = value
    def __str__(self):
        board_str = ''
        for x in range(9):
            for y in range(9):
                if (x, y) in self.board:
                    board_str += str(self.board[(x, y)])+'\t'
                else:
                    board_str += '0\t'
            board_str += '\n'
        return board_str
    def get(self, row, col):
        return self.board[(row, col)]
    def get_all_affected(self, row, col):
        affected = []
        for x in range(9):
            if x != row:
                affected.append((x, col))
        for y in range(9):
            if y != col:
                affected.append((row, y))
        for x in range(3):
            for y in range(3):
                if x != row % 3 or y != col % 3:
                    affected.append((row - row % 3 + x, col - col % 3 + y))
        return affected
    def get_all_values(self, cells):
        cell_values = [self.board[cell] for cell in cells if cell in self.board]
        return cell_values
    def get_all_possible_values(self, row, col):
        affected = self.get_all_affected(row, col)
        cell_values = self.get_all_values(affected)
        possible_values = [x for x in range(1, 10) if x not in cell_values]
        return possible_values
    def get_all_empty(self):
        empty = []
        for x in range(9):
            for y in range(9):
                if (x, y) not in self.board:
                    empty.append((x, y))
        return empty