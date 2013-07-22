import os
import unittest
import sys
sys.path.append('../src')
sys.path.append('../src/algorithms')
from results import Results
from norvig_algorithm import NorvigAlgorithm


class TestResults(unittest.TestCase):

    def setUp(self):
        self.route_to_save = 'F:/sudoku/game_results/saved1'
        self.save = Results(self.route_to_save)
        self.norvig = NorvigAlgorithm()
        self.grid1 = '003020600900305001001806400008102900700000008006708200' \
                     '002609500800203009005010300'

    def test_save_sudoku_to_txt_file(self):
        info = self.norvig.parse_sudoku_to_string(self.norvig.solve(self.grid1))
        self.save.save_to_file(info, self.route_to_save)
        self.assertTrue(os.path.isfile(self.route_to_save + '.txt'))

if __name__ == '__main__':
    unittest.main()
