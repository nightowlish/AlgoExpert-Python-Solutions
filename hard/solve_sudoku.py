class Sudoku:
    def __init__(self, board, dimension=3):
        self.board = board
        self.dimension = dimension
        self.board_size = self.dimension * self.dimension
        
    def solve(self):
        for row_index in range(self.board_size):
            for column_index in range(self.board_size):
                if self.board[row_index][column_index]:
                    continue
                fillings = self.get_valid_fillings(row_index, column_index)
                if not fillings:
                    return False
                for filling in fillings:
                    self.board[row_index][column_index] = filling
                    result = self.solve()
                    if result:
                        return True
                else:
                    self.board[row_index][column_index] = 0
                    return False
        return True
                
    def get_valid_fillings(self, row_index, column_index):
        good_row = self.get_valid_row_fillings(row_index)
        good_column = self.get_valid_column_fillings(column_index)
        good_cell = self.get_valid_cell_fillings(row_index, column_index)
        return good_row & good_column & good_cell
    
    def get_valid_row_fillings(self, row_index):
        used_fillings = {element for element in self.board[row_index] if element}
        return {value for value in range(1, 10) if not value in used_fillings}
    
    def get_valid_column_fillings(self, column_index):
        used_fillings = {row[column_index] for row in self.board if row[column_index]}
        return {value for value in range(1, 10) if not value in used_fillings}
        
    def get_valid_cell_fillings(self, row_index, column_index):
        used_values = set()
        row_offset = row_index // self.dimension
        row_remainder = row_index % self.dimension
        column_offset = column_index // self.dimension
        column_remainder = column_index % self.dimension
        for current_row_index in range(row_offset * self.dimension, (row_offset + 1) * self.dimension):
            for current_column_index in range(column_offset * self.dimension, (column_offset + 1) * self.dimension):
                if self.board[current_row_index][current_column_index]:
                    used_values.add(self.board[current_row_index][current_column_index])
        return {value for value in range(1, 10) if not value in used_values}


def solveSudoku(board):
    board = Sudoku(board)
    result = board.solve()
    if not result:
        return None
    return board.board
