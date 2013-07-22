from menu import Menu
from settings import Settings
from algorithms.norvig_algorithm import NorvigAlgorithm
from algorithms.backtracking import Backtracking
from read_from_file import ReadFromFile
from results import Results
from sudoku_generator import SudokuGenerator
import re
class Sudoku:

    def __init__(self):
        self.menu = Menu()
        self.sudoku_settings = Settings()
        self.reader = ReadFromFile()
        self.writer = Results()


        self.settings = ["Algorithm", "Level", "Input", "Output"]
        self.current_settings = self.sudoku_settings.get_current_settings()
        self.go_main_menu_option = "m"
        self.exit_game_option = "x"
        self.list_of_char_options = [self.go_main_menu_option, self.exit_game_option]
        self.menu_options = {self.exit_game_option: [self.menu.exit],
                             self.go_main_menu_option: [self.menu.go_to_main_menu],
                             "1": [self.start_game],
                             "2": [self.menu.display_settings],
                             "3": [self.menu.display_modify_settings],
                             "3.1": [self.menu.display_modify_setting_options, self.settings[0]],
                             "3.1.1": [self.menu.display_modify_default_setting,
                                       self.settings[0]],
                             "3.2": [self.menu.display_modify_setting_options, self.settings[1]],
                             "3.2.1": [self.menu.display_modify_default_setting, self.settings[1]],
                             "3.2.2": [self.menu.display_select_setting_name_to_modify_attributes,
                                       self.settings[1]],
                             "3.3": [self.menu.display_modify_setting_options, self.settings[2]],
                             "3.3.1": [self.menu.display_modify_default_setting, self.settings[2]],
                             "3.3.2": [self.menu.display_select_setting_name_to_modify_attributes,
                                       self.settings[2]],
                             "3.4": [self.menu.display_modify_setting_options, self.settings[3]],
                             "3.4.1": [self.menu.display_modify_default_setting, self.settings[3]],
                             "3.4.2": [self.menu.display_select_setting_name_to_modify_attributes,
                                       self.settings[3]],
                             "4": [self.generate_sudoku]}
    def run_application(self):
        """
        Initiates the application launching or displaying on console the main menu
        the main menu.
        """
        while self.menu.status != self.menu.exit_game_option:
            if self.menu.status == self.menu.go_main_menu_option or self.menu.status == "":
                self.menu.display_main_menu()
            self.get_option_value_from_user()
            self.validate_user_option()
            self.run_method_according_option()

    def start_game(self):
        """
        Get inbound sudoku, solve it, and save it in a file.
        """
        algorithm = self.create_instance_of_algorithm_from_setting()
        inbound_sudoku = self.inbound_sudoku_according_of_setting()
        solved_sudoku = algorithm.solve(inbound_sudoku)
        algorithm.display(solved_sudoku)
        solved_sudoku_as_string = algorithm.parse_sudoku_to_string(solved_sudoku)
        output_path = self.current_settings["output_path"] + "/" + "default"
        self.writer.save_to_file(solved_sudoku_as_string, output_path)
        self.menu.status = self.go_main_menu_option

    def create_instance_of_algorithm_from_setting(self):
        """
        Create an instance according the value for default algorithm
        """
        algorithm_list = {"Peter Norvig" : NorvigAlgorithm,"Backtracking" : Backtracking}
        algorithm_instance = algorithm_list[self.current_settings["Algorithm"]]()
        return algorithm_instance

    def inbound_sudoku_according_of_setting(self):
        """
        get inbound sudoku according to Input in settings and return a string with initial status
        of a sudoku game.
        """
        inbound_sudoku = ""
        if self.current_settings["Input"] == "CSV" or self.current_settings["Input"] == "TXT":
            try:
                file_name = str(raw_input("Please enter the file name to read:"))
                input_path = self.current_settings["input_path"] + "/" + file_name + \
                             "." + (self.current_settings["Input"].lower())
                inbound_sudoku = self.reader.read_file(input_path)
            except:
                print "Error reading sudoku from file at:" + input_path
                inbound_sudoku = ""
        else:
            inbound_sudoku = self.reader.get_sudoku_from_console()
        return inbound_sudoku

    def generate_sudoku(self):
        """make a sudoku game, according to Level in settings, and save it in a file"""
        minimum_limit_of_dots = int(self.current_settings["min"])
        maximum_limit_of_dots = int(self.current_settings["max"])
        generator = SudokuGenerator(minimum_limit_of_dots, maximum_limit_of_dots)
        sudoku_generated = generator.generate_sudoku()
        self.writer.save_to_file(sudoku_generated, "../custom_games/sudoku_generated")
        self.menu.status = self.go_main_menu_option

    def get_option_value_from_user(self):
        """Get and update the value for user_option from user input"""
        try:
            self.menu.user_option = str(raw_input("Please enter an option:"))
        except:
            self.menu.user_option = "m"

    def validate_user_option(self):
        """Validate input from user and return None if it is a non valid key
        """
        good_input_values = "^(" + self.exit_game_option + "|" + self.go_main_menu_option \
                            + "|\d){1}$"
        if re.match(good_input_values, self.menu.user_option):
            self.menu.user_option = self.menu.status + self.menu.user_option
            last_character = self.menu.user_option[-1]
            if self.__is_a_char_option(last_character) is True:
                self.menu.user_option = last_character
            if not self.menu_options.has_key(self.menu.user_option):
                self.menu.user_option = None
        else:
            self.menu.user_option = "m"

    def __is_a_char_option(self, last_character):
        """Return True if the character belongs to list_of_char_options

        Keyword arguments:
        last_character -- a character value i.e.: x
        """
        for char_options in self.list_of_char_options:
            if self.menu_options.has_key(last_character) and char_options == last_character:
                return True
        return False

    def run_method_according_option(self):
        """Execute the method according to user_option value

        Keyword arguments:
        user_option -- value of option according to menu
        """
        if self.menu.user_option is not None:
            list_execute = self.menu_options[self.menu.user_option]
            function_execute = list_execute[0]
            if len(list_execute) > 1:
                function_execute(list_execute[1])
            else:
                function_execute()
        else:
            self.menu.status = self.go_main_menu_option


if __name__ == '__main__':
    s = Sudoku()
    s.run_application()