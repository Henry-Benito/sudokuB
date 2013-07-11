
class Algorithm:
    def __init__(self):
        self.rows = 'ABCDEFGHI'
        self.cols = '123456789'
        self.squares  = self.cross(self.rows,self.cols)

    def solve(self, grid):
        """Returns a dictionary with values for sudoku solved.

        Keyword arguments:
        grid -- string with values for initial status of a sudoku
        """
        raise error("This method 'solve' should be implemented")
        return "Not implemented"

    def display(self, values):
        """Display these values as a 2-D grid.

        Keyword arguments:
        values -- dictionary with values for sudoku solved
        """
        width = 1+max(len(values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)
        for r in self.rows:
            print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                          for c in self.cols)
            if r in 'CF': print line
        print

    def cross(self, A, B):
        """Cross product of elements in A and elements in B.
        """
        return [a+b for a in A for b in B]