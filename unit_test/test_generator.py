import unittest
import re
import sys
sys.path.append('../src')
from sudoku_generator import SudokuGenerator

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.minimum_limit = 30
        self.maximum_limit = 40
        self.generator = SudokuGenerator(self.minimum_limit, self.maximum_limit)
        self.generator.fill_board()
        self.generator.fill_puzzle_with_dots()

    def test_generate_empty_board(self):
        expected_easy_puzzle = None
        self.assertEqual(expected_easy_puzzle, self.generator.clean_board())

    def test_parsed_puzzle(self):
        expected_result = self.generator.create_board_to_txt()
        self.assertTrue(re.match('0123456789+-_|', expected_result))

if __name__ == '__main__':
    unittest.main()
