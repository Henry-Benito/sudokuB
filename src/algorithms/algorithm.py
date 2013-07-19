

class Algorithm:
    def __init__(self):
        self.rows = 'ABCDEFGHI'
        self.cols = '123456789'
        self.squares = self.cross(self.rows, self.cols)

    def solve(self, grid):
        """Return a dictionary with values for sudoku solved.

        Keyword arguments:
        grid -- string with values for initial status of a sudoku
        """
        raise Exception("This method solve should be implemented")

    def display(self, values):
        """Display these values as a 2-D grid.

        Keyword arguments:
        values -- dictionary with values for sudoku solved
        """
        width = 1 + max(len(values[s]) for s in self.squares)
        line = '+'.join(['-' * (width * 3)] * 3)
        for r in self.rows:
            print ''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                          for c in self.cols)
            if r in 'CF':
                print line
        print

    def cross(self, first_list, second_list):
        """Do a scalar product of elements in first_list and elements in second_list
        and return a list.
        Keyword arguments:
        first_list -- a iterable with elements to combine with other.
        second_list -- a iterable with elements to combine with other.
        """
        scalar_product = [element_first_list + element_sec_list \
                          for element_first_list in first_list \
                          for element_sec_list in second_list]
        return scalar_product

    def dict_to_string(self, dictionary):
        string_result = ""
        for key in sorted(dictionary.iterkeys()):
            string_result = string_result + str(dictionary[key])
        return string_result

    def parse_sudoku_to_string(self, values):
        """Saves a sudoku puzzle solved as a 2-D grid in order to save it into a TXT file."""
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
        return pr_line

