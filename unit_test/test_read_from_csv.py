import unittest
import os
import sys
sys.path.append("../src/")

from read_csv_file import ReadCsvFile

class TestReadFromCsv(unittest.TestCase):

    def setUp(self):
        self.route_one_sudoku = '../custom_games/easy1.csv'
        self.route_several_sudokus = '../custom_games/easy2.csv'
        self.read_csv_one_sudoku = ReadCsvFile(self.route_one_sudoku)
        self.read_csv_several_sudokus = ReadCsvFile(self.route_several_sudokus)

    def test_verify_if_file_exist_for_one_sudoku(self):
        self.assertTrue(os.path.isfile(self.route_one_sudoku))

    def test_verify_if_file_exist_for_several_sudokua(self):
        self.assertTrue(os.path.isfile(self.route_several_sudokus))

    def test_read_a_csv_file_with_one_sudoku_puzzle(self):
        expected_one_sudoku = ['00302060090030500100180640000810290070000000800' \
                              '6708200002609500800203009005010300']
        one_sudoku = self.read_csv_one_sudoku.read_file()
        self.assertEqual(expected_one_sudoku, one_sudoku)

    def test_read_a_csv_file_with_several_sudoku_puzzle(self):
        expected_several_sudokus = ['002003000003410008004097000040500001605030029' \
                                    '000000004050600000000009070000001030',
                                    '530029006002810000010000900006000000400090002' \
                                    '000052000065000000000700310190000700',
                                    '120000000578400000000000100009060004006040020' \
                                    '000190700000050200060801970000300000']
        several_sudokus = self.read_csv_several_sudokus.read_file()
        self.assertEqual(expected_several_sudokus, several_sudokus)

if __name__ == '__main__':
    unittest.main()
