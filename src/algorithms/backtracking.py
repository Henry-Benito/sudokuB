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
        Takes a string with string elements.
        Parses the data into a 2d list of integers to be processed as Sudoku board.
        Returns the board with a list of empty squares.
        """
        data_in_lines = []
        line = ""
        for dig in range(len(data)):
            line += data[dig]
            if (dig + 1) % 9 == 0:
                data_in_lines.append(line)
                line = ""
        #board = [[int(value) for value in line.strip()] for line in data]
        board = [[int(value) for value in line.strip()] for line in data_in_lines]
        empty_squares = list((row, column) for row in range(9) for column in range(9) \
                             if board[row][column] == 0)
        return (board, empty_squares)

    def possible_values(self, board, position):
        """
        Returns a generator of valid values of the square on the board
        at position (row,col).
        """

        row, col = position
        adjacent = tuple(board[row][y] for y in range(9)) + \
                   tuple(board[x][col] for x in range(9)) + \
                   tuple(board[x][y] for x in range(int(row / 3) * 3, int(row/3) * 3 + 3) \
                                     for y in range(int(col / 3) * 3, int(col/3) * 3 + 3))

        for value in range(1, 10):
            if value not in adjacent:
                yield value

    def least_constraining_value(self, board, cell, value):
        """
        Function used in calculating least constraining value heuristic.
        """

        row, col = cell
        adjacent = {(row, y) for y in range(9)} | \
                   {(x, col) for x in range(9)} | \
                   {(x, y) for x in range(int(row / 3) * 3, int(row / 3) * 3 + 3) \
                          for y in range(int(col / 3) * 3, int(col / 3) * 3 + 3)}
        adjacent.discard(cell)

        return sum(1 for near in adjacent if value in self.possible_values(board, near))

    def resolve(self, board, emptyCells):
        """
        Returns a solved version of the initial Sudoku board.
        Board must be 9*9 grid of integers
        """

        emptyCells.sort(key=lambda cell: len(list(self.possible_values(board, cell))))

        if len(emptyCells) == 0:
            return board
        else:
            row, col = emptyCells.pop(0)

        sorted_possible_values = sorted(self.possible_values(board, (row, col)), \
              key = lambda value: self.least_constraining_value(board, (row, col), value))

        for value in sorted_possible_values:
            newBoard = deepcopy(board)
            newBoard[row][col] = value
            newBoard = self.resolve(newBoard, copy(emptyCells))
            if newBoard:
                return newBoard

        return False

    def solve(self, grid):
        board, empty_squares_to_fill = self.parse_board(grid)
        board = self.resolve(board, empty_squares_to_fill)
        return self.board_to_dict(board)

    def board_to_dict(self, board):
        dict_res = {}
        index = 0
        for row in board:
            for dig in row:
                dict_res[self.squares[index]] = str(dig)
                index += 1
        return dict_res

"""
#Used for testing algorithm.
grid = '000000801700200000000506000000700050010000300080000000500000020040080000600030000'
grid1 = '000006000059000008200008000045000000003000000006003054000325006000000000000000000'
b = Backtracking()
result = b.solve(grid1)
#b.display(result)
"""
