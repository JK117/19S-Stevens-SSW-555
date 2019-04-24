import unittest
from sprint4test.test_gedcom_sprint_04 import TestCheckFunctionsSprint04

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCheckFunctionsSprint04("test_list_individual_ages"),
             TestCheckFunctionsSprint04("test_list_multiple_births"),
             TestCheckFunctionsSprint04("test_correct_gender_for_role"),
             TestCheckFunctionsSprint04("test_unique_first_names_in_families"),
             TestCheckFunctionsSprint04("test_check_unique_name_and_birth_date"),
             TestCheckFunctionsSprint04("test_check_unique_families_by_spouses")]
    suite.addTests(tests)

    with open('Sprint4_Unit_Test_Report.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)