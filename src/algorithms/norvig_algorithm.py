"""Solve Every Sudoku Puzzle
Throughout this program we have:
row is a row of the 9x9 matrix, e.g. 'A'
col is a column of the 9x9 matrix, e.g. '3'
square is a position or interception between a column and a row, e.g. 'A3'
dig is a digit, e.g. '9'
un is a unit, e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}
"""
import sys
sys.path.append("../")
from algorithm import Algorithm
import time

class Norvig(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        #self.route = route
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.cols = self.digits
        self.squares = self.cross(self.rows, self.cols)
        self.unitlist = ([self.cross(self.rows, col) for col in self.cols] +
                         [self.cross(row, self.cols) for row in self.rows] +
                         [self.cross(row_square, col_square) for row_square in ('ABC', 'DEF', 'GHI')
                         for col_square in ('123', '456', '789')])
        self.units = dict((square, [un for un in self.unitlist if square in un])
                          for square in self.squares)
        self.peers = dict((square, set(sum(self.units[square], []))-set([square]))
                          for square in self.squares)

    def time_decorator(func):
        def wrapper(*arg):
            t = time.clock()
            res = func(*arg)
            time_result = time.clock()-t
            #res = ('%02d:%02d.%d'%(time_result.minute,time_result.second,time_result.microsecond))[:-4]
            print "Sudoku solved in: " + str(time_result) + " seconds"
            return res
        return wrapper

    def parse_grid(self, grid):
        """Convert grid to a dict of possible values,
        or return False if a contradiction is detected.

        Keywords:
        grid -- A sudoku grid
        values -- Return a dictionary of possible values for the grid as dictionary.
        """
        values = dict((square, self.digits) for square in self.squares)
        for square, dig in self.grid_values(grid).items():
            if dig in self.digits and not self.assign(values, square, dig):
                return False
        return values

    def grid_values(self, grid):
        """Convert a sudoku grid into a dict of with '0' or '.' chars for empty values
        and return a dictionary.

        Keywords:
        grid -- A sudoku grid
        chars -- a list of values for columns with '0' or '.'
        squares -- the position of the matrix for example 'A1', 'C5', etc.
        """
        chars = [col for col in grid if col in self.digits or col in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def assign(self, values, square, dig):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return a list of values, if a contradiction is detected we return a boolean value False."""
        other_values = values[square].replace(dig, '')
        if all(self.eliminate(values, square, other_digit) for other_digit in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square, dig):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return a list of values, if a contradiction is detected we return a boolean value False.
        (1) If a square is reduced to one value dig2, then eliminate dig2 from the peers.
        (2) If a unit un is reduced to only one place for a value dig, then put it there.
        """
        if dig not in values[square]:
            return values
        values[square] = values[square].replace(dig, '')
        if len(values[square]) == 0:
            return False
        elif len(values[square]) == 1:
            other_digit = values[square]
            if not all(self.eliminate(values, other_square, other_digit) for other_square in self.peers[square]):
                return False

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
        """
        return self.search(self.parse_grid(grid))

    def search(self, values):
        """Using depth-first search and propagation, try all possible values."""
        if values is False:
            return False
        if all(len(values[square]) == 1 for square in self.squares):
            return values
        n, square = min((len(values[square]), square)
                        for square in self.squares if len(values[square]) > 1)

        return self.some(self.search(self.assign(values.copy(), square, dig))
                         for dig in values[square])

    def some(self, seq):
        """Return some element of seq that is true."""
        for element in seq:
            if element:
                return element
        return False
