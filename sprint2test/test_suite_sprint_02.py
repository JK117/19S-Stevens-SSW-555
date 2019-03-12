import unittest
from sprint2test.test_gedcom_sprint_02 import TestCheckFunctionsSprint02

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCheckFunctionsSprint02("test_check_birth_b4_death_of_parents"),
             TestCheckFunctionsSprint02("test_check_marriage_after_14")]
    suite.addTests(tests)

    with open('Sprint2_Unit_Test_Report.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
