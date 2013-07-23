import unittest
import sys
sys.path.append("..\src")
from menu import Menu
from settings import Settings

class TestMenu(unittest.TestCase):
    def setUp(self):
        pass


############################ Method: display_modify_setting_options #################################
    def test_display_modify_setting_options_should_have_level_options_when_setting_is_Level(self):
        sudoku_menu = Menu()
        expected_string = "\n\nModify Level options:\n" + \
                          "==========================\n" + \
                          "1. Modify Level by default\n" + \
                          "2. Modify Level attributes\n" + \
                          "m. Go to main menu\n" + \
                          "x. Exit"
        sudoku_menu.display_modify_setting_options("Level")

        self.assertEqual(expected_string, sudoku_menu.menu_string)

    def test_display_modify_setting_should_display_options_for_settings(self):
        sudoku_menu = Menu()
        expected_string = "\n\nModifying Settings\n" + \
                           "==================\n" + \
                           "1. Algorithm\n" + \
                           "2. Level\n" + \
                           "3. Input games\n" + \
                           "4. Results\n" + \
                           "m. Back to main menu\n" + \
                           "x. Exit"
        sudoku_menu.display_modify_settings()
        self.assertEqual(expected_string, sudoku_menu.menu_string)

    def test_display_modify_setting_should_display_main_menu(self):
        sudoku_menu = Menu()
        expected_string = "\n\n" + \
                          "SUDOKU Menu\n" + \
                          "------------------------\n" + \
                          "1. Play\n" + \
                          "2. Display settings\n" + \
                          "3. Modify settings\n" + \
                          "4. Generate sudoku game\n" + \
                          "x. Exit\n"
        sudoku_menu.display_main_menu()
        self.assertEqual(expected_string, sudoku_menu.menu_string)

    def test_display_modify_setting_should_display_current_settings(self):
        sudoku_menu = Menu()
        sudoku_setting = Settings()
        sudoku_setting.set_config_attributes("Level", "Easy","max", 35)
        sudoku_setting.set_config_attributes("Level", "Easy","min", 30)
        sudoku_setting.set_config_attributes("Level", "Medium","max", 50)
        sudoku_setting.set_config_attributes("Level", "Medium","min", 40)
        sudoku_setting.set_config_attributes("Level", "Hard","max", 70)
        sudoku_setting.set_config_attributes("Level", "Hard","min", 60)
        expected_string = "========================\n" + \
                          "\tAlgorithm:\n" + \
                          "\t\t-Peter Norvig (Default)\n" + \
                          "\t\t-Backtracking\n" + \
                          "\t\t-Brute Force\n" + \
                          "\tLevel:\n" + \
                          "\t\t-Easy\n" + \
                          "\t\t\tmax = 35\n" + \
                          "\t\t\tmin = 30\n" + \
                          "\t\t-Medium\n" + \
                          "\t\t\tmax = 50\n" + \
                          "\t\t\tmin = 40\n" + \
                          "\t\t-Hard (Default)\n" + \
                          "\t\t\tmax = 70\n" + \
                          "\t\t\tmin = 60\n" + \
                          "\tInput:\n" + \
                          "\t\t-Console\n" + \
                          "\t\t\tpath = \n" + \
                          "\t\t-TXT\n" + \
                          "\t\t\tpath = ../custom_games\n" + \
                          "\t\t-CSV (Default)\n" + \
                          "\t\t\tpath = ../custom_games\n" + \
                          "\tOutput:\n" + \
                          "\t\t-TXT (Default)\n" + \
                          "\t\t\tpath = ../game_results\n" + \
                          "========================="
        sudoku_menu.display_settings()
        self.assertEqual(expected_string, sudoku_menu.menu_string)

    def test_display_modify_default_setting_should_display_options(self):
        sudoku_menu = Menu()
        expected_string = "\n\nSet default Algorithm\n" + \
                          "1. Peter Norvig\n" + \
                          "2. Backtracking\n" + \
                          "3. Brute Force\n" + \
                          "m. Go to main menu\n" + \
                          "x. Exit"
        sudoku_menu.display_modify_default_setting("Algorithm")
        self.assertEqual(expected_string, sudoku_menu.menu_string)
    def test_display_select_setting_name_modify_attributes_should_update_attribute_for_level(self):
        sudoku_menu = Menu()
        sudoku_setting = Settings()
        old_value = sudoku_setting.get_attribute_value_for_setting("Level", "Easy","max")
        sudoku_menu.display_select_setting_name_to_modify_attributes("Level")
        new_value = sudoku_setting.get_attribute_value_for_setting("Level", "Easy","max")
        self.assertEqual(old_value, new_value)

if __name__ == '__main__':
    unittest.main()
