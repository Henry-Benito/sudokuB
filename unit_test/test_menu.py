import unittest
import sys
sys.path.append("..\src")
from menu import Menu

class Test_menu(unittest.TestCase):
    def setUp(self):
        pass

############################ Method: validate_user_option ######################################
    def test_validate_user_option_should_be_x_when_user_option_is_x(self):
        m = Menu()
        m.user_option = "x"
        m.validate_user_option()
        self.assertEqual("x",m.user_option)
    def test_validate_user_option_should_be_x_when_user_option_is_x_and_status_3_dot_2(self):
        m = Menu()
        m.status = "3.2."
        m.user_option = "x"
        m.validate_user_option()
        self.assertEqual("x",m.user_option)
    def test_validate_user_option_should_be_a_3_dot_1_when_user_option_is_1_and_status_3_dot(self):
        m = Menu()
        m.status = "3."
        m.user_option = "1"
        m.validate_user_option()
        self.assertEqual("3.1",m.user_option)

    def test_validate_user_option_should_be_None_when_user_option_is_a_non_key_valid(self):
        m = Menu()
        m.status = "3."
        m.user_option = "7"
        m.validate_user_option()
        self.assertEqual(None,m.user_option)

    def test_validate_user_option_should_be_m_when_user_option_is_enter_an_invalid_option(self):
        m = Menu()
        m.status = "3."
        m.user_option = "7asdasds"
        m.validate_user_option()
        self.assertEqual("m",m.user_option)

############################ Method: __run_method_according_option #################################
    def test_run_method_according_option_should_have_start_game_when_user_option_is_1(self):
        m = Menu()
        m.status = ""
        m.user_option = "1"
        list_aux = m.menu_options[m.user_option]
        list_aux[0].__name__
        #self.assertEqual("start_game",m.user_option)

############################ Method: display_modify_setting_options #################################
    def test_display_modify_setting_options_should_have_level_options_when_setting_is_Level(self):
        m = Menu()
        expected_string = "\n\nModify Level options:\n" + \
                          "==========================\n" + \
                          "1. Modify Level by default\n" + \
                          "2. Modify Level attributes\n" + \
                          "m. Go to main menu\n" + \
                          "x. Exit"
        m.display_modify_setting_options("Level")

        self.assertEqual(expected_string, m.menu_string)

    def test_inbound_sudoku_has_good_format_should_return_true_for_valid_sudoku_format(self):
        m = Menu()
        sudoku_input = "223...456023...456026...456023...456023...456023...456023...456023...456023...456"
        result = m.inbound_sudoku_has_good_format(sudoku_input)
        self.assertTrue(result)

    def test_inbound_sudoku_has_good_format_should_return_true_for_invalid_sudoku_format(self):
        m = Menu()
        sudoku_input = "223...456023sa...456026...456023...456023...456023...456023...456023...456023...456"
        result = m.inbound_sudoku_has_good_format(sudoku_input)
        self.assertFalse(result)
        sudoku_input = "+/223...456023...456026...456023...456023...456023...456023...456023...456023...456"
        result = m.inbound_sudoku_has_good_format(sudoku_input)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
