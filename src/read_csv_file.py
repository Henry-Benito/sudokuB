class ReadCsvFile:
    def __init__(self, route_file):
        """This class reads a CSV file containing 1 or several sudoku puzzles.
        Keywords:
        route_file -- the path were the csv file is found as string e.g. '../custom_games'
        """
        self.route_file = route_file
        self.open_sudoku_file(self.route_file)

    def open_sudoku_file(self, route_file):
        """Open a file and save the contain in a variable and returns a variable that contains
        all the sudoku puzzles to be solved in a list
        Keywords:
        route_file -- the path were the file is found as string e.g. '../custom_games'
        """
        try:
            self.open_file = open(self.route_file, 'r')
            self.file_with_puzzle = self.open_file.read().strip().split('\n')
            self.open_file.close()
        except:
            raise "Error when opening the file: " + self.route_file

    def read_file(self):
        """This function verify if a csv file contains one or more than one sudoku puzzles
        and calls the respective function about that.
        """
        if len(self.file_with_puzzle) > 0:
            res = self.read_several_sudoku_puzzles()
        return res

    def read_one_sudoku_puzzle(self, string_puzzle):
        """ Read one sudoku puzzle from any csv file
        Keywords:
        string_puzzle -- Is a sudoku puzzle in 1 string of 81 chars if the puzzle contains dots (.)
        are replaced by zeros (0) for empty spots.
        """
        string_puzzle = string_puzzle.replace(',', '')
        string_puzzle = string_puzzle.replace('.', '0')
        return string_puzzle

    def read_several_sudoku_puzzles(self):
        """ Reads several sudoku puzzles from a csv file and returns a variable that contains a list
        with several sudoku puzzles like string in each position of that list.
        """
        for pos_list in range(len(self.file_with_puzzle)):
            self.file_with_puzzle[pos_list] = self.read_one_sudoku_puzzle(self.file_with_puzzle[pos_list])
        return self.file_with_puzzle
