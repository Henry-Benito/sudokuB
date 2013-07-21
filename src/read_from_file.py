from read_txt_file import ReadTxtFile
from read_csv_file import ReadCsvFile
import re

class ReadFromFile:
    """
    This class is used to read sudokus from a txt or csv files.
    keywords:
    route -- Is the path where the sudoku files will be read
    sep -- This variable is used to separate all the sudoku puzzles between lines
    """
    def __init__(self):
        pass
    def read_file(self, route):
        self.route = route
        if self.route[-3:] == 'csv':
            self.csv = ReadCsvFile(route)
            res = self.csv.read_file()
        elif self.route[-3:] == 'txt':
            self.txt = ReadTxtFile(route)
            res = self.txt.read_file()
        else:
            print ("There is no file in the directory")
        return res

    def get_sudoku_from_console(self):
        """
        Return a string from user that contains a sudoku to solve.
        """
        sudoku_from_console = ""
        for row in range(9):
            try:
                console_row = str(raw_input("Enter the 9 digits for %s row of sudoku:" % str(row)))
                sudoku_from_console += console_row
            except:
                sudoku_from_console = None
        return sudoku_from_console

