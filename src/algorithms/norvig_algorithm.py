"""Solve Every Sudoku Puzzle
Throughout this program we have:
row is a row of the 9x9 matrix, e.g. 'A'
col is a column of the 9x9 matrix, e.g. '3'
square is a position or interception between a column and a row, e.g. 'A3'
dig is a digit, e.g. '9'
un is a unit, e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
grid is a string of 81 non-blank chars e.g. 81 non-blank chars, e.g. starting with '.18...7...
values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}
"""
import sys
sys.path.append("../")
from algorithm import Algorithm
from algorithm import time_decorator
import time

class NorvigAlgorithm(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.cols = self.digits
        self.squares = self.cross(self.rows, self.cols)
        self.unitlist = ([self.cross(self.rows, col) for col in self.cols] +
                         [self.cross(row, self.cols) for row in self.rows] +
                         [self.cross(row_square, col_square) for row_square in ('ABC','DEF','GHI')
                         for col_square in ('123','456','789')])
        self.units = dict((square, [un for un in self.unitlist if square in un])
                          for square in self.squares)
        self.peers = dict((square, set(sum(self.units[square],[]))-set([square]))
                          for square in self.squares)


    def parse_grid(self, grid):
        """Convert grid to a dict of possible values, or return False if a contradiction is detected.
        Keywords:
        grid -- A sudoku grid e.g. '010020670, etc'
        """
        values = dict((square, self.digits) for square in self.squares)
        for square, dig in self.grid_values(grid).items():
            if dig in self.digits and not self.assign(values, square, dig):
                return False
        return values

    def grid_values(self, grid):
        """Convert a sudoku grid into a dict with '0' or '.' chars for empty values.
        Keywords:
        grid -- A sudoku grid e.g. '010020670, etc'
        """
        chars = [col for col in grid if col in self.digits or col in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def assign(self, values, square, dig):
        """Return a list of values, if a contradiction is detected it return a boolean value False.
        Keywords:
        values -- Is a list of possible values for a grid e.g. [2, 4, 5, 8, 1, etc]
        square -- Is the possition of a sudoku grid 'A1'
        dig -- Is a integer value between 1 and 9.
        """
        other_values = values[square].replace(dig, '')
        if all(self.eliminate(values, square, other_digit) for other_digit in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square, dig):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return a list of values, if a contradiction is detected it return a boolean value False.
        (1) If a square is reduced to one value dig2, then eliminate dig2 from the peers.
        (2) If a unit un is reduced to only one place for a value dig, then put it there.
        Keywords:
        values -- Is a list of possible values for a grid e.g. [2, 4, 5, 8, 1, etc]
        square -- Is the possition of a sudoku grid 'A1'
        dig -- Is a integer value between 1 and 9.
        """
        if dig not in values[square]:
            return values
        values[square] = values[square].replace(dig, '')
        if len(values[square]) == 0:
            return False
        elif len(values[square]) == 1:
            other_digit = values[square]
            if not all(self.eliminate(values, other_square, other_digit) \
                       for other_square in self.peers[square]):
                return False

        return values

    def digit_places_func(self, values, square, dig):
        """Add numbers (digits) to a list of squares (square)
        Keywords:
        values -- Is a list of possible values for a grid e.g. [2, 4, 5, 8, 1, etc]
        square -- Is the possition of a sudoku grid 'A1'
        dig -- Is a integer value between 1 and 9.
        """
        for un in self.units[square]:
            digit_places = [square for square in un if dig in values[square]]
            if len(digit_places) == 0:
                return False
            elif len(digit_places) == 1:
                if not self.assign(values, digit_places[0], dig):
                    return False
        return values

    @time_decorator
    def solve(self, grid):
        """Solve a suoku puzzle that already have some possible values in each of the blank
        spaces.
        Keywords:
        grid is a string of 81 non-blank chars e.g. 81 non-blank chars, e.g. starting with
         '.18...7...
        """
        return self.search(self.parse_grid(grid))

    def search(self, values):
        """Using depth-first search and propagation, try and return all possible values.
        Keywords:
        values -- Is a list of possible values for a grid e.g. [2, 4, 5, 8, 1, etc]
        """
        if values is False:
            return False
        if all(len(values[square]) == 1 for square in self.squares):
            return values
        n, square = min((len(values[square]), square)
                        for square in self.squares if len(values[square]) > 1)

        return self.possible_values(self.search(self.assign(values.copy(), square, dig))
                                    for dig in values[square])

    def possible_values(self, seq):
        """Return an element of a list that is true.
        Keywords:
        seq -- list of values e.g. [2, 4, 5, 8, 1, etc]
        """
        for element in seq:
            if element:
                return element
        return False
