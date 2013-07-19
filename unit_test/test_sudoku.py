import unittest
import sys
sys.path.append("../src")
from sudoku import Sudoku
from settings import Settings


class Test_Sudoku(unittest.TestCase):

    def setUp(self):
        pass

    def test_sudoku_should_resolve_an_easy_sudoku_with_norvig_from_CSV_to_result(self):
        sudoku_test = Sudoku()
        settings_test = Settings()
        expected_result= ["4 8 3 |9 2 1 |6 5 7 \n", \
                          "9 6 7 |3 4 5 |8 2 1 \n", \
                          "2 5 1 |8 7 6 |4 9 3 \n", \
                          "------+------+------\n", \
                          "5 4 8 |1 3 2 |9 7 6 \n", \
                          "7 2 9 |5 6 4 |1 3 8 \n", \
                          "1 3 6 |7 9 8 |2 4 5 \n", \
                          "------+------+------\n", \
                          "3 7 2 |6 8 9 |5 1 4 \n", \
                          "8 1 4 |2 5 3 |7 6 9 \n", \
                          "6 9 5 |4 1 7 |3 8 2 \n"]
        settings_test.set_config("Algorithm", "Peter Norvig")
        settings_test.set_config("Input", "CSV")
        settings_test.write_settings()
        sudoku_test.start_game()
        file_result = open("../game_results/default.txt", 'r')
        result = file_result.readlines()
        file_result.close()
        self.assertEqual(expected_result, result)

    def test_sudoku_should_resolve_an_easy_sudoku_with_backtracking_from_TXT_to_result(self):
        sudoku_test = Sudoku()
        settings_test = Settings()
        expected_result= ["4 8 3 |9 2 1 |6 5 7 \n", \
                          "9 6 7 |3 4 5 |8 2 1 \n", \
                          "2 5 1 |8 7 6 |4 9 3 \n", \
                          "------+------+------\n", \
                          "5 4 8 |1 3 2 |9 7 6 \n", \
                          "7 2 9 |5 6 4 |1 3 8 \n", \
                          "1 3 6 |7 9 8 |2 4 5 \n", \
                          "------+------+------\n", \
                          "3 7 2 |6 8 9 |5 1 4 \n", \
                          "8 1 4 |2 5 3 |7 6 9 \n", \
                          "6 9 5 |4 1 7 |3 8 2 \n"]
        settings_test.set_config("Algorithm", "Backtracking")
        settings_test.set_config("Input", "TXT")
        settings_test.write_settings()
        sudoku_test.start_game()
        file_result = open("../game_results/default.txt", 'r')
        result = file_result.readlines()
        file_result.close()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()