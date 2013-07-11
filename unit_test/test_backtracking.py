import unittest
import sys
sys.path.append("..\src\\algorithms")
from backtracking import Backtracking


class Test_Backtracking(unittest.TestCase):

    def setUp(self):
        self.easy = "003020600900305001001806400008102900700000008006708200" + \
                    "002609500800203009005010300"
        self.normal = "400000805030000000000700000020000060000080400000010000" + \
                        "000603070500200000104000000"
        self.hard =  "000006000059000008200008000045000000003000000006003054" + \
                        "000325006000000000000000000"
        self.back = Backtracking()

    def test_verify_solution_for_easy_grid(self):
        expected_result_easy = '48392165796734582125187649354813297672956413' \
                                '8136798245372689514814253769695417382'
        unsort_list = self.back.solve(self.easy)
        nums = ''
        for key in sorted(unsort_list.iterkeys()):
            nums = nums + str(unsort_list[key])
        self.assertEqual(expected_result_easy, nums)

    def test_verify_solution_for_normal_grid(self):
        expected_result_normal = '41736982563215894795872431682543716979158643' \
                                '2346912758289643571573291684164875293'
        unsort_list = self.back.solve(self.normal)
        nums = ''
        for key in sorted(unsort_list.iterkeys()):
            nums = nums + str(unsort_list[key])
        self.assertEqual(expected_result_normal, nums)
    
if __name__ == '__main__':
    unittest.main()
