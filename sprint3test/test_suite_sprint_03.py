import unittest
from sprint3test.test_gedcom_sprint_03 import TestCheckFunctionsSprint03

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCheckFunctionsSprint03("test_check_less_then_150_years_old"),
             TestCheckFunctionsSprint03("test_check_birth_b4_marriage_of_parents"),
             TestCheckFunctionsSprint03("test_check_birth_b4_death_of_parents"),
             TestCheckFunctionsSprint03("test_check_marriage_after_14"),
             TestCheckFunctionsSprint03("test_check_no_marriages_to_descendants"),
             TestCheckFunctionsSprint03("test_check_siblings_should_not_marry")]
    suite.addTests(tests)

    with open('Sprint3_Unit_Test_Report.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
