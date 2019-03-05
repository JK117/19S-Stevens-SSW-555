import unittest
from test.test_gedcom import TestCheckFunctions

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCheckFunctions("test_check_birth_b4_marr"), TestCheckFunctions("test_check_marr_b4_div"),
             TestCheckFunctions("test_check_birth_b4_death"), TestCheckFunctions("test_check_marr_b4_death")]
    suite.addTests(tests)

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    with open('Sprint1_Unit_Test_Report.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
