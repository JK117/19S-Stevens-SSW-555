import unittest
from sprint4test.test_gedcom_sprint_04 import TestCheckFunctionsSprint04

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # tests = [TestCheckFunctionsSprint03("test_siblings_spacing"),
    #          TestCheckFunctionsSprint03("test_multiple_births_less_than_5"),
    #          TestCheckFunctionsSprint03("test_fewer_than_15_siblings"),
    #          TestCheckFunctionsSprint03("test_male_last_names"),
    #          TestCheckFunctionsSprint03("test_check_no_marriages_to_descendants"),
    #          TestCheckFunctionsSprint03("test_check_siblings_should_not_marry")]
    # suite.addTests(tests)

    with open('Sprint4_Unit_Test_Report.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)