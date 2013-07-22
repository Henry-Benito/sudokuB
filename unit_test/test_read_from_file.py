import unittest
import sys
sys.path.append("../src/")

from read_from_file import ReadFromFile
from read_csv_file import ReadCsvFile
from read_txt_file import ReadTxtFile

class TestReadFromFile(unittest.TestCase):

    def setUp(self):
        self.route_csv_file = '../custom_games/easy1.csv'
        self.route_txt_file = '../custom_games/easy.txt'
        self.read = ReadFromFile()
        self.csv = ReadCsvFile(self.route_csv_file)
        self.txt = ReadTxtFile(self.route_txt_file)

    def test_read_csv_file_function(self):
        expected_read = self.read.read_file(self.route_csv_file)
        self.assertEqual(expected_read, self.csv.read_file())

    def test_read_txt_file_function(self):
        expected_read = self.read.read_file(self.route_txt_file)
        self.assertEqual(expected_read, self.txt.read_one_sudoku_puzzle())

if __name__ == '__main__':
    unittest.main()
