class ReadCsvFile:
    def __init__(self, route_file):
        """
        This class reads a CSV file containing 1 or several sudoku puzzles.
        Keywords:
        route -- The path with the txt file to read.
        """
        try:
            self.route_file = route_file
            self.open_file = open(self.route_file, 'r')
            self.file_with_puzzle = self.open_file.read().strip().split('\n')
            self.open_file.close()
        except:
            print "Error reading " + self.route_file + " file"

    def read_file(self):
        """This function verify if a csv file contains one or more than one sudoku puzzles
        and calls the respective function about that.
        """
        if len(self.file_with_puzzle) > 1:
            res = self.read_several_sudoku_puzzles()
        else:
            res = self.read_one_sudoku_puzzle()
        return res

    def read_one_sudoku_puzzle(self):
        """ After read the csv file a first time in the previous function we need to restart the
        reading of the file.
        """
        string_puzzle = ''.join(self.file_with_puzzle)
        string_puzzle = string_puzzle.replace(',', '')
        string_puzzle = string_puzzle.replace('.', '0')
        return string_puzzle

    def read_several_sudoku_puzzles(self):
        """ After read the csv file a first time in the previous function we need to restart the
        reading of the file.
        """
        for pos_list in range(len(self.file_with_puzzle)):
            self.file_with_puzzle[pos_list] = self.file_with_puzzle[pos_list].replace(',', '')
            self.file_with_puzzle[pos_list] = self.file_with_puzzle[pos_list].replace('.', '0')
        return self.file_with_puzzle
