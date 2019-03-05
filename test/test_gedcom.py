# Project for SSW-555
# Author: Jiakuan Fan

import unittest
from gedcom import Gedcom


class TestCheckFunctions(unittest.TestCase):
    # def test_check_date_b4_current(self):
    #     # Test check_date_b4_current() function

    def test_check_birth_b4_marr(self):
        # Test check_birth_b4_marr() function
        test_case_01_1 = Gedcom("test_example_01_1")
        test_case_01_2 = Gedcom("test_example_01_2")
        test_case_01_3 = Gedcom("test_example_01_3")
        test_case_01_4 = Gedcom("test_example_01_4")
        test_case_01_5 = Gedcom("test_example_01_5")
        self.assertTrue(test_case_01_1.check_birth_b4_marr())
        self.assertFalse(test_case_01_2.check_birth_b4_marr())
        self.assertFalse(test_case_01_3.check_birth_b4_marr())
        self.assertFalse(test_case_01_4.check_birth_b4_marr())
        self.assertTrue(test_case_01_5.check_birth_b4_marr())

    # def test_check_birth_b4_death(self):
    #     # Test check_birth_b4_death() function

    def test_check_marr_b4_div(self):
        # Test check_marr_b4_div() function
        test_case_02_1 = Gedcom("test_example_02_1")
        test_case_02_2 = Gedcom("test_example_02_2")
        test_case_02_3 = Gedcom("test_example_02_3")
        test_case_02_4 = Gedcom("test_example_02_4")
        self.assertTrue(test_case_02_1.check_marr_b4_div())
        self.assertTrue(test_case_02_2.check_marr_b4_div())
        self.assertFalse(test_case_02_3.check_marr_b4_div())
        self.assertTrue(test_case_02_4.check_marr_b4_div())

    # def test_check_marr_b4_death(self):
    #     # Test check_marr_b4_death() function

    # def test_check_div_b4_death(self):
    #     # Test check_div_b4_death() function


if __name__ == '__main__':
    unittest.main(verbosity=2)
