import unittest
from sprint1test.test_gedcom_sprint_01 import TestCheckFunctionsSprint01


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCheckFunctionsSprint01("test_check_date_b4_current"),
             TestCheckFunctionsSprint01("test_check_birth_b4_marr"),
             TestCheckFunctionsSprint01("test_check_birth_b4_death"),
             TestCheckFunctionsSprint01("test_check_marr_b4_div"),
             TestCheckFunctionsSprint01("test_check_marr_b4_death"),
             TestCheckFunctionsSprint01("test_check_div_b4_death")]
    suite.addTests(tests)

    with open('Sprint1_Unit_Test_Report.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
