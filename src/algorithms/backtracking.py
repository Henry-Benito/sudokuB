from copy import deepcopy, copy
from algorithm import Algorithm


class Backtracking(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.rows = 'ABCDEFGHI'
        self.cols = '123456789'
        self.squares = self.cross(self.rows, self.cols)

    def parse_board(self, data):
        """
        Takes a string with values for initial sudoku status.
        Parses the data into a 2d list of integers to be processed as Sudoku board.
        Returns the board with a list of empty squares.

        Keyword arguments:
        data -- string with values for initial status of a sudoku
        """
        data_in_lines = []
        line = ""
        for dig in range(len(data)):
            line += data[dig]
            if (dig + 1) % 9 == 0:
                data_in_lines.append(line)
                line = ""
        board = [[int(value) for value in line.strip()] for line in data_in_lines]
        empty_squares = list((row, column) for row in range(9) for column in range(9) \
                             if board[row][column] == 0)
        return (board, empty_squares)

    def possible_values(self, board, position):
        """
        Returns a generator of valid values of the square on the board
        at position (row,col).

        Keyword arguments:
        board -- list of values for sudoku
        position -- tuple of row and column
        """

        row, col = position
        adjacent = tuple(board[row][y] for y in range(9)) + \
                   tuple(board[x][col] for x in range(9)) + \
                   tuple(board[x][y] for x in range(int(row / 3) * 3, int(row / 3) * 3 + 3) \
                                     for y in range(int(col / 3) * 3, int(col / 3) * 3 + 3))

        for value in range(1, 10):
            if value not in adjacent:
                yield value

    def least_constraining_value(self, board, cell, value):
        """
        Function used in calculating least constraining value heuristic.
        Keyword arguments:
        board -- list of values for sudoku
        cell -- tuple of row and column
        value -- integer to validate in a cell into board
        """

        row, col = cell
        adjacent = {(row, y) for y in range(9)} | \
                   {(x, col) for x in range(9)} | \
                   {(x, y) for x in range(int(row / 3) * 3, int(row / 3) * 3 + 3) \
                          for y in range(int(col / 3) * 3, int(col / 3) * 3 + 3)}
        adjacent.discard(cell)
        res = sum(1 for near in adjacent if value in self.possible_values(board, near))
        return res

    def resolve(self, board, empty_cells):
        """
        Returns a solved version of the initial Sudoku board.
        Board must be 9 * 9 grid of integers

        Keyword arguments:
        board -- list of values for sudoku
        empty_cells -- list of squares in the board with empty values
        """

        empty_cells.sort(key=lambda cell: len(list(self.possible_values(board, cell))))

        if len(empty_cells) == 0:
            return board
        else:
            row, col = empty_cells.pop(0)

        sorted_possible_values = sorted(self.possible_values(board, (row, col)), \
              key = lambda value: self.least_constraining_value(board, (row, col), value))

        for value in sorted_possible_values:
            new_board = deepcopy(board)
            new_board[row][col] = value
            new_board = self.resolve(new_board, copy(empty_cells))
            if new_board:
                return new_board

        return False

    def solve(self, grid):
        """
        Returns a dictionary with solved sudoku values.
        
        Keyword arguments:
        grid -- string with values for initial status of a sudoku
        """
        board, empty_squares_to_fill = self.parse_board(grid)
        board = self.resolve(board, empty_squares_to_fill)
        return self.board_to_dict(board)

    def board_to_dict(self, board):
        """
        Returns a dictionary from a list of values.
        
        Keyword arguments:
        board -- list of values for sudoku
        """
        dict_res = {}
        index = 0
        for row in board:
            for dig in row:
                dict_res[self.squares[index]] = str(dig)
                index += 1
        return dict_res
