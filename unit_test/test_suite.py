from coverage import coverage

cov = coverage()
cov.start()

import unittest
from test_norvig import TestNorvig
from test_menu import Test_menu


suite = unittest.TestSuite()

# adding all the tests from a unittest class
suite_norvig = unittest.TestLoader().loadTestsFromTestCase(TestNorvig)
suite_menu = unittest.TestLoader().loadTestsFromTestCase(Test_menu)

unittest.TextTestRunner(verbosity=2).run(suite_norvig)
unittest.TextTestRunner(verbosity=2).run(suite_menu)

cov.stop()
cov.html_report(directory='covhtml')
