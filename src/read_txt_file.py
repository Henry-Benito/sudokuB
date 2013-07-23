class ReadTxtFile:
 
    def __init__(self, route):
        """
        This class reads a TXT file containing 1 sudoku puzzle in the 9x9 format
        Keywords:
        route -- The path with the txt file to read.        
        """
        self.route = route

    def read_file(self):
        """Open a file and save the contain in a variable
        """
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
        """Reads a sudoku file in any format, even the parsed one that contains '- + ? |' chars
        """
        self.file_with_puzzle = self.delete_unneccesary_characters(self.file_with_puzzle)
        parsed_sudoku_puzzle = ''
        for line in self.file_with_puzzle:
            parsed_sudoku_puzzle += line
        if len(parsed_sudoku_puzzle) == 81:
            return parsed_sudoku_puzzle
        else:
            return False

    def delete_unneccesary_characters(self, list_of_lines):
        """Removes from a string the special characters added when a sudoku puzzle is parsed with
        the following special chars: '- + ? .' and returns a list of sudoku puzzle as a string.
        """
        rows_to_remove = []
        for line_number in range(len(list_of_lines)):
            list_of_lines[line_number] = list_of_lines[line_number].strip()
            list_of_lines[line_number] = list_of_lines[line_number].translate(None, ' -+|')
            list_of_lines[line_number] = list_of_lines[line_number].replace('.','0')
        list_of_lines = [line for line in list_of_lines if line]
        return list_of_lines