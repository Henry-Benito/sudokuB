## Solve Every Sudoku Puzzle
## Throughout this program we have:
## row is a row of the 9x9 matrix, e.g. 'A'
## col is a column of the 9x9 matrix, e.g. '3'
## square is a position or interception between a column and a row, e.g. 'A3'
## dig is a digit, e.g. '9'
## un is a unit, e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
## grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
## values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}

from algorithm import Algorithm

class Norvig(Algorithm):
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

    def cross(self,A, B):
        "Cross product of elements in A and elements in B."
        return [a+b for a in A for b in B]

    ################ Parse a Grid ################

    def parse_grid(self, grid):
        """Convert grid to a dict of possible values, {square: self.digits}, or
        return False if a contradiction is detected."""
        ## To start, every square can be any digit; then assign values from the grid.
        values = dict((square, self.digits) for square in self.squares)
        for square, dig in self.grid_values(grid).items():
            if dig in self.digits and not self.assign(values, square, dig):
                return False ## (Fail if we can't assign d to square s.)
        return values

    def grid_values(self, grid):
        "Convert grid into a dict of {square: char} with '0' or '.' for empties."
        chars = [col for col in grid if col in self.digits or col in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    ################ Constraint Propagation ################

    def assign(self, values, square, dig):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = values[square].replace(dig, '')
        if all(self.eliminate(values, square, dig2) for dig2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square, dig):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if dig not in values[square]:
            return values ## Already eliminated
        values[square] = values[square].replace(dig,'')
        ## (1) If a square is reduced to one value dig2, then eliminate dig2 from the peers.
        if len(values[square]) == 0:
            return False ## Contradiction: removed last value
        elif len(values[square]) == 1:
            dig2 = values[square]
            if not all(self.eliminate(values, square2, dig2) for square2 in self.peers[square]):
                return False
        ## (2) If a unit un is reduced to only one place for a value dig, then put it there.
        for un in self.units[square]:
            dplaces = [square for square in un if dig in values[square]]
            if len(dplaces) == 0:
                return False ## Contradiction: no place for this value
            elif len(dplaces) == 1:
                # dig can only be in one place in unit; assign it there
                if not self.assign(values, dplaces[0], dig):
                    return False
        return values

    ################ Display as 2-D grid ################

    def parse_sudoku_to_string(self, values):
        "Display these values as a 2-D grid."
        self.values = values
        width = 1 + max(len(self.values[squares]) for squares in self.squares)
        line = '+'.join(['-' * (width * 3)] * 3)
        pr_line = ""
        for row in self.rows:
            pr_line += ''.join(self.values[row+col].center(width) + ('|' if col in '36' else '')
                          for col in self.cols)
            pr_line += '\n'
            if row in 'CF':
                pr_line += (line + '\n')
        return pr_line+'\n'

    ################ Search ################

    def solve(self, grid): return self.search(self.parse_grid(grid))

    def search(self, values):
        "Using depth-first search and propagation, try all possible values."
        if values is False:
            return False ## Failed earlier
        if all(len(values[square]) == 1 for square in self.squares):
            return values ## Solved!
        ## Chose the unfilled square s with the fewest possibilities
        n, square = min((len(values[square]), square)
                    for square in self.squares if len(values[square]) > 1)

        return self.some(self.search(self.assign(values.copy(), square, dig))
                    for dig in values[square])

    ################ Utilities ################

    def some(self, seq):
        "Return some element of seq that is true."
        for e in seq:
            if e: return e
        return False

    def read_from_file(self, route, sep = '\n'):
        """
        Read the sudoku puzzles from a file and resolve them.
        First we validate that the extension of a file is CSV or TXT to solve it,
        in other case we display a message.
        Then we save the results in another file.
        """
        import os
        self.route = route
        list_files = [f for f in os.listdir(self.route)\
                    if os.path.isfile(os.path.join(self.route, f))]
        for ext_file in list_files:
            if ext_file[-3:] == 'txt':
                f = open(self.route+'\\'+ext_file, 'r')
                sudoku_file = f.read().strip().split()
                for i in range(len(sudoku_file)):
                    if len(sudoku_file[i]) == 81:
                        self.save_to_file("..\Game_Results\\Res_Generated",
                        self.parse_sudoku_to_string(self.solve(sudoku_file[i])))
                    else:
                        print 'Not a valid sudoku puzzle'
                f.close()
            elif ext_file[-3:] == 'csv':
                f = open(self.route+'\\'+ext_file, 'r')
                sudoku_file = f.read().strip().split()
                csv_str = [[]] * len(sudoku_file)
                for u in range(len(sudoku_file)):
                    i = sudoku_file[u]
                    csv_str[u] = i.replace(',', '')

                for i in range(len(csv_str)):
                    if len(csv_str[i]) == 81:
                        self.save_to_file("..\game_results\\res_generated",
                        self.parse_sudoku_to_string(self.solve(csv_str[i])))
                    else:
                        print 'Not a valid sudoku puzzle'
                f.close()
            else:
                print 'The file is not a TXT or CSV file with sudoku puzzles to solve'


    def save_to_file(self, saved_route, info):
        """This function save a solved sudoku puzzle in a TXT file
        """
        self.saved_route = saved_route
        self.info = str(info)
        f = open(self.saved_route+'.txt', 'a')
        f.write(self.info)
        f.close()


    def shuffled(self, seq):
        """Return a randomly shuffled copy of the input sequence."""
        seq = list(seq)
        random.shuffle(seq)
        return seq
