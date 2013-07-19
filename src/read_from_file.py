from read_txt_file import ReadTxtFile
from read_csv_file import ReadCsvFile


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

    def inbound_sudoku_has_good_format(self, inbound_sudoku):
        """
        Return True when the string only contains numbers from 0 to 9 or '.' character and
        its length is 81.

        Keyword arguments:
        inbound_sudoku -- string with values for sudoku game from user i.e.:
        400000805030000000000700000020000060000080400000010000
        """
        if re.match("^(\.|[0-9])+$", inbound_sudoku) and len(inbound_sudoku) == 81:
            return True
        else:
            return False