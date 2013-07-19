from menu import Menu
from settings import Settings
from algorithms.norvig_algorithm import Norvig
from algorithms.backtracking import Backtracking
from read_from_file import ReadFromFile
from results import Results
from sudoku_generator import SudokuGenerator
class Sudoku:

    def __init__(self):
        self.sudoku_menu = Menu()
        self.sudoku_settings = Settings()
        self.reader = ReadFromFile()
        self.writer = Results()
        self.current_settings = self.sudoku_settings.get_current_settings()
    def run_application(self):
        """
        Initiates the application launching or displaying on console the main menu
        the main menu.
        """
        while self.sudoku_menu.status != self.sudoku_menu.exit_game_option:
            if self.sudoku_menu.status == self.sudoku_menu.go_main_menu_option or self.sudoku_menu.status == "":
                self.sudoku_menu.display_main_menu()
            self.sudoku_menu.get_option_value_from_user()
            self.sudoku_menu.validate_user_option()
            self.sudoku_menu.run_method_according_option()

    def start_game(self):
        algorithm = self.create_instance_of_algorithm_from_setting()
        inbound_sudoku = self.inbound_sudoku_according_of_setting()
        solved_sudoku = algorithm.solve(inbound_sudoku)
        algorithm.display(solved_sudoku)
        solved_sudoku_as_string = algorithm.parse_sudoku_to_string(solved_sudoku)
        #output_path = self.current_settings["output_path"] + "/" + "default.txt"
        output_path = "../game_results/default"
        self.writer.save_to_file(solved_sudoku_as_string, output_path)

    def create_instance_of_algorithm_from_setting(self):
        algorithm_list = {"Peter Norvig" : Norvig,"Backtracking" : Backtracking}
        algorithm_instance = algorithm_list[self.current_settings["Algorithm"]]()
        return algorithm_instance

    def inbound_sudoku_according_of_setting(self):
        inbound_sudoku = ""
        if self.current_settings["Input"] == "CSV" or self.current_settings["Input"] == "TXT":
            try:
                #file_name = str(raw_input("Please enter the file name to read:"))
                file_name = "file01"
                input_path = self.current_settings["input_path"] + "/" + file_name + \
                             "." + (self.current_settings["Input"].lower())
                inbound_sudoku = self.reader.read_file(input_path)
            except:
                print "Error reading sudoku from file at:" + input_path
        else:
            inbound_sudoku = self.reader.get_sudoku_from_console()
        return inbound_sudoku

    def generate_sudoku(self):
        minimum_limit_of_dots = int(self.current_settings["min"])
        maximum_limit_of_dots = int(self.current_settings["max"])
        generator = SudokuGenerator(minimum_limit_of_dots, maximum_limit_of_dots)
        sudoku_generated = generator.generate_sudoku()
        self.writer.save_to_file(sudoku_generated, "../custom_games/sudoku_generated")




if __name__ == '__main__':
    s = Sudoku()
    #s.generate_sudoku()
    s.start_game()
    #s.run_application()