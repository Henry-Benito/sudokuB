import random
from results import Results


class SudokuGenerator(object):
    def __init__(self, minimum_limit, maximum_limit):
        """
        Keywords:
        difficulty -- is the difficult level of a sudoku game
        minimum_limit -- Is the minimum value of a difficult level
        maximum_limit -- Is the maximum value of a difficult level
        solution -- is an empty solution list
        puzzle -- is an empty puzzle list
        """
        self.clean_board()
        self.difficulty = random.randint(minimum_limit, maximum_limit)
        self.solution = []
        self.puzzle = []
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def clean_board(self):
        """Create a 9x9 clean matrix with None values in each position of the matrix
        """
        self.board = []
        for row in xrange(9):
            self.board.append([None for i in xrange(9)])

    def create_board_to_txt(self):
        """
        This function prints a board row by row and without brackets
        Keywords:
        puzzle_line -- returns a sudoku puzzle as a string separated by
        line with a sudoku game format.
        """
        puzzle_line = ''
        cont = 0
        for row in self.puzzle:
            cont += 1
            if cont == 4 or cont == 7:
                puzzle_line += '------+-------+-------\n'
            item_cont = 0
            for item in row:
                item_cont += 1
                if item_cont == 4 or item_cont == 7:
                    puzzle_line += '| '
                puzzle_line += str(item) + " "
            puzzle_line += '\n'
        return puzzle_line

    def is_number_in_row(self, board, row, number):
        """Verifies if a number is present in a row
        Keywords:
        board -- Is a 9x9 matrix
        row -- Is a row value between 1 and 9
        number -- is a number to be verified
        If the number is not present in the row, then return False
        """
        result = False
        if number in board[row] and number != None:
            result = True
        else:
            reult = False
        return result

    def is_number_in_column(self, board, col, number):
        """Verifies if a number is present in a column
        Keywords:
        board -- Is a 9x9 matrix
        col -- Is a column value between 1 and 9
        number -- is a number to be verified
        If the number is not present in the column, then return False
        """
        result = False
        for row in xrange(9):
            if board[row][col] == number and number != None:
                result = True
        return result

    def is_number_in_square(self, board, square_row, square_col, number):
        """Verifies if a number is present in a square [square_row, square_col]
        Keywords:
        board -- is a 9x9 matrix
        square_row -- a position of a peer [A1]
        square_col -- a position of a peer [A1]
        number -- is a number to be verified
        If the number is not present in the column, then return False
        """
        for row in range(3 * square_row, 3 * square_row + 3):
            for col in range(3 * square_col, 3 * square_col + 3):
                if board[row][col] == number and number != None:
                    return True
        return False

    def fill_board(self):
        """Fills a sudoku board with values in each square [4, 2, 3, etc]
        Keywords:
        possible_values -- a matrix with values that a square can contain
        try_value -- is a delimiter to assign possible values to a row until 200 times, if in 200
        times the value was wrong, then we clean the board and try again.
        row -- is the row of a board
        stop -- a flag that help us to stop or continue trying values for a square
        wrong -- is a flag that help us to verify if there were wrong values for a square, if wrong
        is the same number of possible values, then we restart the board
        number -- is not present in any of the squares, then we assign that number to a square and
        removes that number from possible_values
        """
        random.seed()
        col = 0
        while col < 9:
            maximum_tries = 200
            random.shuffle(self.possible_values)
            row = 0
            try_value = 0
            res = self.try_values_in_row(try_value, row, col, maximum_tries)
            col += 1

            if try_value == maximum_tries:
                self.clean_board()
                col = 0

    def try_values_in_row(self, try_value, row, col, maximum_tries):
        """Verifies if a value is present in a row and tries to add it in another row and returns
        the row number incremented.
        Keywords:
        try_value -- integer value that count the tries to add a value to a row
        row -- Integer value that represents a row
        col -- Integer value that represents a column
        maximum_tries -- Is a variable that counts the times that a value was tried to be added
        in a row.
        """
        while row < 9 and try_value < maximum_tries:
            wrong = 0
            stop = 0
            res = self.element_in_range(wrong, row, col)
            if res == len(self.possible_values):
                for row_t in xrange(9):
                    self.board[row_t][col] = None
                self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                stop = 1
                row = 0
                try_value += 1
            if stop == 0:
                found_number = self.number_in_range(row, col)
                self.board[row][col] = found_number
                self.possible_values.remove(found_number)
                row += 1
        return row

    def number_in_range(self, row, col):
        """Verifies if a number is present in a row of the puzzle
        Keywords:
        row -- is the row position of the puzzle
        col -- is the col position of the puzzle
        number -- is a randomic number between 1 and 9
        """
        number = random.randint(1, 9)
        while (self.is_number_in_column(self.board, col, number)
                or self.is_number_in_row(self.board, row, number)
                or self.is_number_in_square(self.board, int(round(row / 3)),
                int(round(col / 3)), number)):
            random.seed()
            number = random.randint(1, 9)
        return number

    def element_in_range(self, wrong, row, col):
        """Verifies if a number is present in a square of the puzzle and return a number that
        represents the wrong tries did for that element.
        """
        for elem in range(0, len(self.possible_values)):
                    if (self.is_number_in_column(self.board, col, self.possible_values[elem])
                        or self.is_number_in_row(self.board, row, self.possible_values[elem])
                        or self.is_number_in_square(self.board, int(round(row / 3)),
                        int(round(col / 3)), self.possible_values[elem])):
                        wrong += 1
        return wrong

    def fill_puzzle_with_dots(self):
        """After fill a board a puzzle is generated emptying squares randomly, using as delimiter
        the difficulty level of the sudoku game.
        """

        self.puzzle = self.board
        self.puzzle_zeros = self.board
        i = 0
        pos = 0
        while (i < self.difficulty):
            pos = int(random.randint(0, 80))
            row, col = divmod(pos, 9)
            if self.puzzle[row][col] != ".":
                self.puzzle[row][col] = "."
                i += 1
    def generate_sudoku(self):
        sudoku_generated = "None"
        while "None" in sudoku_generated:

            self.fill_board()
            self.fill_puzzle_with_dots()
            sudoku_generated = self.create_board_to_txt()
        print sudoku_generated
        return sudoku_generated
