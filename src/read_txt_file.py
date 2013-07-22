class ReadTxtFile:
    def __init__(self, route_file):
        """This class reads a TXT file containing 1 sudoku puzzle in the 9x9 format
        Keywords:
        route -- The path with the txt file to read.
        """
        self.route_file = route_file
        self.open_sudoku_file(self.route_file)

    def open_sudoku_file(self, route_file):
        """Open a file and save the contain in a variable
        Keywords:
        route_file -- the path were the file is found as string e.g. '../custom_games'
        """
        try:
            self.open_file = open(self.route_file, 'r')
            self.file_with_puzzle = self.open_file.read()
            self.file_with_puzzle = self.file_with_puzzle.split('\n')
            self.open_file.close()
        except:
            raise "Error when opening the file: " + self.route_file

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
        for line_number in range(len(list_of_lines)):
            list_of_lines[line_number] = list_of_lines[line_number].strip()
            list_of_lines[line_number] = list_of_lines[line_number].replace('.','0')
            list_of_lines[line_number] = list_of_lines[line_number].translate(None, ' -+|')
        list_of_lines = [line for line in list_of_lines if line]
        return list_of_lines
