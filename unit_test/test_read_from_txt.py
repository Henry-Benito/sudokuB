import unittest
import os
import sys
sys.path.append("../src/")

from read_txt_file import ReadTxtFile

class TestReadFromTxt(unittest.TestCase):

    def setUp(self):
        self.route_one_sudoku = "../custom_games/easy.txt"
        self.route_bad_format = "../custom_games/bad_format.txt"
        self.read_txt_one_sudoku = ReadTxtFile(self.route_one_sudoku)
        self.read_bad_format = ReadTxtFile(self.route_bad_format)

    def test_verify_if_file_exist_for_one_sudoku(self):
        self.assertTrue(os.path.isfile(self.route_one_sudoku))

    def test_sudoku_puzzle_not_in_9x9_format(self):
        expected_one_sudoku = '4000008050300000000007000000200000600000804' \
                              '00000010000000603070500200000104000000'
        one_sudoku = self.read_txt_one_sudoku.read_one_sudoku_puzzle()
        self.assertEqual(expected_one_sudoku, one_sudoku)

    def test_read_a_csv_file_with_one_sudoku_puzzle(self):
        one_bad_sudoku = self.read_bad_format.read_one_sudoku_puzzle()
        self.assertFalse(one_bad_sudoku)

if __name__ == '__main__':
    unittest.main()
