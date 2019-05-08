# Project for SSW-555
# Author: Hangbo Li

import unittest
from gedcom import Gedcom
import us01
import us02
import us03
import us04
import us05
import us06


class TestCheckFunctions(unittest.TestCase):
    def test_check_date_b4_current(self):
        # Test check_date_b4_current() function
        test_case_01_1 = Gedcom("test_example_01_1")
        us01.check_date_b4_current(test_case_01_1)
        test_case_01_1_expected = ['ERROR: FAMILY: US01: @F2@: Divorced Date 2020-06-22 occurs before today: 2019-05-08']
        self.assertEqual(test_case_01_1_expected, test_case_01_1.error_list)

        test_case_01_2 = Gedcom("test_example_01_2")
        us01.check_date_b4_current(test_case_01_2)
        test_case_01_2_expected = []
        self.assertEqual(test_case_01_2_expected, test_case_01_2.error_list)

    def test_check_birth_b4_marr(self):
        # Test check_birth_b4_marr() function
        test_case_02_1 = Gedcom("test_example_02_1")
        us02.check_birth_b4_marr(test_case_02_1)
        test_case_02_1_expected = []
        self.assertEqual(test_case_02_1_expected, test_case_02_1.error_list)

        test_case_02_2 = Gedcom("test_example_02_2")
        us02.check_birth_b4_marr(test_case_02_2)
        test_case_02_2_expected = ['ERROR: FAMILY: US02: @F1@: @I1@: Marriage date 1925-06-08 occurs before birthday 1930-09-05',
                                   'ERROR: FAMILY: US02: @F1@: @I2@: Marriage date 1925-06-08 occurs before birthday 1932-07-01']
        self.assertEqual(test_case_02_2_expected, test_case_02_2.error_list)

        test_case_02_3 = Gedcom("test_example_02_3")
        us02.check_birth_b4_marr(test_case_02_3)
        test_case_02_3_expected = ['ERROR: FAMILY: US02: @F1@: @I1@: Marriage date 1931-06-08 occurs before birthday 1932-09-05']
        self.assertEqual(test_case_02_3_expected, test_case_02_3.error_list)

        test_case_02_4 = Gedcom("test_example_02_4")
        us02.check_birth_b4_marr(test_case_02_4)
        test_case_02_4_expected = ['ERROR: FAMILY: US02: @F1@: @I2@: Marriage date 1931-06-08 occurs before birthday 1932-07-01']
        self.assertEqual(test_case_02_4_expected, test_case_02_4.error_list)

        test_case_02_5 = Gedcom("test_example_02_5")
        us02.check_birth_b4_marr(test_case_02_5)
        test_case_02_5_expected = []
        self.assertEqual(test_case_02_5_expected, test_case_02_5.error_list)

    def test_check_birth_b4_death(self):
        # Test check_birth_b4_death() function
        test_case_03_1 = Gedcom("test_example_03_1")
        us03.check_birth_b4_death(test_case_03_1)
        test_case_03_1_expected = []
        self.assertEqual(test_case_03_1_expected, test_case_03_1.error_list)

        test_case_03_2 = Gedcom("test_example_03_2")
        us03.check_birth_b4_death(test_case_03_2)
        test_case_03_2_expected = ['ERROR: INDIVIDUAL: US03: @I1@: Death date 1930-09-05 occurs before Birthday 2008-01-01']
        self.assertEqual(test_case_03_2_expected, test_case_03_2.error_list)

        test_case_03_3 = Gedcom("test_example_03_3")
        us03.check_birth_b4_death(test_case_03_3)
        test_case_03_3_expected = ['ERROR: INDIVIDUAL: US03: @I2@: Death date 1932-07-01 occurs before Birthday 2015-05-05']
        self.assertEqual(test_case_03_3_expected, test_case_03_3.error_list)

        test_case_03_4 = Gedcom("test_example_03_4")
        us03.check_birth_b4_death(test_case_03_4)
        test_case_03_4_expected = []
        self.assertEqual(test_case_03_4_expected, test_case_03_4.error_list)

        test_case_03_5 = Gedcom("test_example_03_5")
        us03.check_birth_b4_death(test_case_03_5)
        test_case_03_5_expected = []
        self.assertEqual(test_case_03_5_expected, test_case_03_5.error_list)

    def test_check_marr_b4_div(self):
        # Test check_marr_b4_div() function
        test_case_04_1 = Gedcom("test_example_04_1")
        us04.check_marr_b4_div(test_case_04_1)
        test_case_04_1_expected = []
        self.assertEqual(test_case_04_1_expected, test_case_04_1.error_list)

        test_case_04_2 = Gedcom("test_example_04_2")
        us04.check_marr_b4_div(test_case_04_2)
        test_case_04_2_expected = []
        self.assertEqual(test_case_04_2_expected, test_case_04_2.error_list)

        test_case_04_3 = Gedcom("test_example_04_3")
        us04.check_marr_b4_div(test_case_04_3)
        test_case_04_3_expected = ['ERROR: FAMILY: US04: @F2@: Divorce date 1952-05-15 occurs before marriage date 1962-06-22']
        self.assertEqual(test_case_04_3_expected, test_case_04_3.error_list)

        test_case_04_4 = Gedcom("test_example_04_4")
        us04.check_marr_b4_div(test_case_04_4)
        test_case_04_4_expected = []
        self.assertEqual(test_case_04_4_expected, test_case_04_4.error_list)

    def test_check_marr_b4_death(self):
        # Test check_marr_b4_death() function
        test_case_05_1 = Gedcom("test_example_05_1")
        us05.check_marr_b4_death(test_case_05_1)
        test_case_05_1_expected = []
        self.assertEqual(test_case_05_1_expected, test_case_05_1.error_list)

        test_case_05_2 = Gedcom("test_example_05_2")
        us05.check_marr_b4_death(test_case_05_2)
        test_case_05_2_expected = ['ERROR: FAMILY: US03: @F1@: @I1@: Death date 2008-01-01 occurs before marriage date 2018-06-08',
                                   'ERROR: FAMILY: US03: @F1@: @I2@: Death date 2015-05-05 occurs before marriage date 2018-06-08']
        self.assertEqual(test_case_05_2_expected, test_case_05_2.error_list)

    def test_check_div_b4_death(self):
        # Test check_div_b4_death() function
        test_case_06_1 = Gedcom("test_example_06_1")
        us06.check_div_b4_death(test_case_06_1)
        test_case_06_1_expected = []
        self.assertEqual(test_case_06_1_expected, test_case_06_1.error_list)

        test_case_06_2 = Gedcom("test_example_06_2")
        us06.check_div_b4_death(test_case_06_2)
        test_case_06_2_expected = ['ERROR: FAMILY: US06: @F2@: Divorced date 2000-06-22 occurs before @I3@ Death date: 1998-01-01']
        self.assertEqual(test_case_06_2_expected, test_case_06_2.error_list)


if __name__ == '__main__':
    unittest.main()
