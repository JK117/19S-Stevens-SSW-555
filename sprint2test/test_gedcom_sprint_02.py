import unittest
from gedcom import Gedcom


class TestCheckFunctionsSprint02(unittest.TestCase):
    # US09
    def test_check_birth_b4_death_of_parents(self):
        test_case_09_1 = Gedcom("test_example_09_1")
        test_case_09_1.check_birth_b4_death_of_parents()
        test_case_09_1_expected = []
        self.assertEqual(test_case_09_1_expected, test_case_09_1.error_list)

        test_case_09_2 = Gedcom("test_example_09_2")
        test_case_09_2.check_birth_b4_death_of_parents()
        test_case_09_2_expected = ["ERROR: US09: FAMILY: @F1@: Child: @I5@: Birthday: 2009-05-14: "
                                   "After father: @I1@: Death: 2008-01-01: 9 months later"]
        self.assertEqual(test_case_09_2_expected, test_case_09_2.error_list)

    # US10
    def test_check_marriage_after_14(self):
        test_case_10_1 = Gedcom("test_example_10_1")
        test_case_10_1.check_marriage_after_14()
        test_case_10_1_expected = []
        self.assertEqual(test_case_10_1_expected, test_case_10_1.error_list)

        test_case_10_2 = Gedcom("test_example_10_2")
        test_case_10_2.check_marriage_after_14()
        test_case_10_2_expected = ["ANOMALY: US10: FAMILY: @F1@: Wife: @I2@: Married at age: 12: On: 1945-06-08"]
        self.assertEqual(test_case_10_2_expected, test_case_10_2.error_list)


if __name__ == '__main__':
    # unittest.main()
    test_case_10_1 = Gedcom("test_example_12_1")
    print(test_case_10_1.check_parents_not_too_old())


