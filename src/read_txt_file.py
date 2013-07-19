class ReadTxtFile:
    """
    This class reads a TXT file containing 1 sudoku puzzle in the 9x9 format
    Keywords:
    route -- The path with the txt file to read.
    file_with_puzzle -- Saves the sudoku puzzle of the txt file.
    parsed_sudoku_puzzle -- Saves the sudoku puzzle in one string of 81 chars.
    """

    def __init__(self, route):
        self.route = route

    def read_file(self):
        try:
            self.open_file = open(self.route, 'r')
            self.file_with_puzzle = self.open_file.read()
            self.file_with_puzzle = self.file_with_puzzle.split('\n')
            self.open_file.close()
        except:
            print "Error reading " + self.route + " file"
            return ""
        res = self.read_one_sudoku_puzzle()

        return res


    def read_one_sudoku_puzzle(self):
        self.file_with_puzzle = self.delete_unneccesary_characters(self.file_with_puzzle)
        parsed_sudoku_puzzle = ''
        for line in self.file_with_puzzle:
            parsed_sudoku_puzzle += line
        return parsed_sudoku_puzzle

    def delete_unneccesary_characters(self, list_of_lines):
        rows_to_remove = []
        for line_number in range(len(list_of_lines)):
            list_of_lines[line_number] = list_of_lines[line_number].strip()
            list_of_lines[line_number] = list_of_lines[line_number].replace(' ','')
            list_of_lines[line_number] = list_of_lines[line_number].replace('-','')
            list_of_lines[line_number] = list_of_lines[line_number].replace('+','')
            list_of_lines[line_number] = list_of_lines[line_number].replace('|','')
            list_of_lines[line_number] = list_of_lines[line_number].replace('.','0')
        list_of_lines = [line for line in list_of_lines if line]
        return list_of_lines