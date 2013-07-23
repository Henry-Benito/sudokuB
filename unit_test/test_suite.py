from coverage import coverage

cov = coverage()
cov.start()

import unittest
from test_norvig import TestNorvig
from test_menu import TestMenu
from test_read_from_csv import TestReadFromCsv
from test_read_from_txt import TestReadFromTxt
from test_settings import TestSettings
from test_results import TestResults
from test_generator import TestGenerator
from test_sudoku import TestSudoku
from test_backtracking import TestBacktracking


suite = unittest.TestSuite()


suite_norvig = unittest.TestLoader().loadTestsFromTestCase(TestNorvig)
suite_read_from_csv = unittest.TestLoader().loadTestsFromTestCase(TestReadFromCsv)
suite_read_from_txt = unittest.TestLoader().loadTestsFromTestCase(TestReadFromTxt)
suite_results = unittest.TestLoader().loadTestsFromTestCase(TestResults)
suite_generator = unittest.TestLoader().loadTestsFromTestCase(TestGenerator)
suite_menu = unittest.TestLoader().loadTestsFromTestCase(TestMenu)
suite_back = unittest.TestLoader().loadTestsFromTestCase(TestBacktracking)
suite_settings = unittest.TestLoader().loadTestsFromTestCase(TestSettings)
suite_sudoku = unittest.TestLoader().loadTestsFromTestCase(TestSudoku)

unittest.TextTestRunner(verbosity=2).run(suite_norvig)
unittest.TextTestRunner(verbosity=2).run(suite_read_from_csv)
unittest.TextTestRunner(verbosity=2).run(suite_read_from_txt)
unittest.TextTestRunner(verbosity=2).run(suite_results)
unittest.TextTestRunner(verbosity=2).run(suite_generator)
unittest.TextTestRunner(verbosity=2).run(suite_menu)
unittest.TextTestRunner(verbosity=2).run(suite_back)
unittest.TextTestRunner(verbosity=2).run(suite_settings)
unittest.TextTestRunner(verbosity=2).run(suite_sudoku)

cov.stop()
cov.html_report(directory='covhtml')
