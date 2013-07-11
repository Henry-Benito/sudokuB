import unittest
import sys
sys.path.append("..\src\\algorithms")
from norvig_algorithm import Norvig

class TestNorvig(unittest.TestCase):
    def setUp(self):
        self.grid1 = '003020600900305001001806400008102900700000008006708200' \
                     '002609500800203009005010300'
        self.grid2 = '4.....8.5.3..........7......2.....6.....8.4......1....' \
                     '...6.3.7.5..2.....1.4......'
        self.hard1 = '.....6....59.....82....8....45........3........6..3.54' \
                     '...325..6..................'
        self.norvig = Norvig()
        self.filename1 = 'hardest'
        self.filename2 = 'top95'
        self.path = "..\\custom_games"

    def test_verify_solution_for_easy_grid(self):
        expected_result_grid1 = '48392165796734582125187649354813297672956413' \
                                '8136798245372689514814253769695417382'
        unsort_list = self.norvig.parse_grid(self.grid1)
        nums = ''
        for key in sorted(unsort_list.iterkeys()):
            nums = nums + str(unsort_list[key])
        self.assertEqual(expected_result_grid1, nums)

    def test_verify_solution_for_normal_grid(self):
        expected_result_grid2 = '41736982563215894795872431682543716979158643' \
                                '2346912758289643571573291684164875293'
        unsort_list = self.norvig.solve(self.grid2)
        nums = ''
        for key in sorted(unsort_list.iterkeys()):
            nums = nums + str(unsort_list[key])
        self.assertEqual(expected_result_grid2, nums)

    '''def test_verify_solution_for_hard_grid(self):
        import time
        expected_result_hard1 = '43879621565913247827145869384521936771356482' \
                                '9926873154194325786362987541587641932'
        unsort_list = self.norvig.solve(self.hard1)
        nums = ''
        for key in sorted(unsort_list.iterkeys()):
            nums = nums + str(unsort_list[key])
        self.assertEqual(expected_result_hard1, nums[-81:])

    def test_verify_that_the_cross_method_generate_the_peers(self):
        self.cols = '123456789'
        self.rows = 'ABCDEFGHI'
        expected_peers = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
                          'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
                          'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                          'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
                          'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
                          'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
                          'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
                          'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
                          'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        self.assertEqual(expected_peers, self.norvig.cross(self.rows, self.cols))

    def test_verify_that_parse_grid_generate_a_grid_of_posible_values(self):
        expected_grid = {'I6': '5789', 'H9': '4689', 'I2': '6789', 'E8': '12359',
                         'H3': '3', 'H7': '69', 'I7': '23569', 'I4': '589',
                         'H5': '479', 'F9': '23789', 'G7': '1259', 'G6': '3',
                         'G5': '459', 'E1': '3679', 'G3': '289', 'G2': '89',
                         'G1': '289', 'I1': '1', 'C8': '12349', 'I3': '4',
                         'E5': '8', 'I5': '579', 'C9': '123469', 'G9': '12489',
                         'G8': '7', 'A1': '4', 'A3': '12679', 'A2': '1679',
                         'A5': '2369', 'A4': '139', 'A7': '8', 'A6': '269',
                         'C3': '125689', 'C2': '15689', 'C1': '2689',
                         'E6': '25679', 'C7': '12369', 'C6': '245689',
                         'C5': '234569', 'C4': '7', 'I9': '23689', 'D8': '6',
                         'I8': '23589', 'E4': '359', 'D9': '13789', 'H8': '489',
                         'F6': '25679', 'A9': '5', 'G4': '6', 'A8': '1239',
                         'E7': '4', 'E3': '15679', 'F1': '36789', 'F2': '4',
                         'F3': '56789', 'F4': '359', 'F5': '1', 'E2': '15679',
                         'F7': '23579', 'F8': '23589', 'D2': '2', 'H1': '5',
                         'H6': '1', 'H2': '6789', 'H4': '2', 'D3': '15789',
                         'B4': '14589', 'B5': '24569', 'B6': '245689',
                         'B7': '12679', 'E9': '12379', 'B1': '26789', 'B2': '3',
                         'B3': '1256789', 'D6': '4579', 'D7': '13579',
                         'D4': '3459', 'D5': '34579', 'B8': '1249',
                         'B9': '124679', 'D1': '3789'}
        self.assertEqual(expected_grid, self.norvig.parse_grid(self.grid2))

    def test_verify_that_grid_values_generate_a_grid_with_zeros(self):
        expected_zeros_grid = {'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0',
                               'H3': '0', 'H7': '0', 'I7': '3', 'I4': '0',
                               'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9',
                               'G5': '0', 'E1': '7', 'G3': '2', 'G2': '0',
                               'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5',
                               'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0',
                               'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0',
                               'A5': '2', 'A4': '0', 'A7': '6', 'A6': '0',
                               'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0',
                               'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8',
                               'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0',
                               'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0',
                               'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0',
                               'F1': '0', 'F2': '0', 'F3': '6', 'F4': '7',
                               'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0',
                               'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0',
                               'H4': '2', 'D3': '8', 'B4': '3', 'B5': '0',
                               'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9',
                               'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9',
                               'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1',
                               'D1': '0'}
        self.assertEqual(expected_zeros_grid, self.norvig.grid_values(self.grid1))'''

    def test_sudoku_games_from_file(self):
        self.norvig.read_from_file(self.path)

    def test_verify_directory_of_sudoku_games_exist(self):
        import os.path
        if os.path.isdir(self.path):
          res = True
        else:
          res = False
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
