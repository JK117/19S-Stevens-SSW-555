import unittest
from gedcom import Gedcom


class TestCheckFunctionsSprint03(unittest.TestCase):
    # US07
    def test_check_less_then_150_years_old(self):
        test_case_07_1 = Gedcom("test_example_07_1")
        test_case_07_1.check_less_then_150_years_old()
        test_case_07_1_expected = ["ERROR: US07: INDIVIDUAL: " + "@I3@" + " is more than or equals to 150 years old."]
        self.assertEqual(test_case_07_1_expected, test_case_07_1.error_list)

        test_case_07_2 = Gedcom("test_example_07_2")
        test_case_07_2.check_less_then_150_years_old()
        test_case_07_2_expected = []
        self.assertEqual(test_case_07_2_expected, test_case_07_2.error_list)

    # US08
    def test_check_birth_b4_marriage_of_parents(self):
        test_case_08_1 = Gedcom("test_example_08_1")
        test_case_08_1.check_birth_b4_marriage_of_parents()
        test_case_08_1_expected = ["ERROR: US08: FAMILY: " + "@F2@" + ": Child: " + "@I8@" +
                                   ": Birthday: " + "1945-04-16" +
                                   ": Before his/her parents' Married: " + "1982-05-15"]
        self.assertEqual(test_case_08_1_expected, test_case_08_1.error_list)

        test_case_08_2 = Gedcom("test_example_08_2")
        test_case_08_2.check_birth_b4_marriage_of_parents()
        test_case_08_2_expected = []
        self.assertEqual(test_case_08_2_expected, test_case_08_2.error_list)

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

    # US17
    def test_check_no_marriages_to_descendants(self):
        test_case_17_1 = Gedcom("test_example_17_1")
        test_case_17_1.check_no_marriages_to_descendants()
        test_case_17_1_expected = ['ERROR: US17: FAMILY: @F2@, there is marriage between parents and descendants.']
        self.assertEqual(test_case_17_1_expected, test_case_17_1.error_list)

        test_case_17_2 = Gedcom("test_example_17_2")
        test_case_17_2.check_no_marriages_to_descendants()
        test_case_17_2_expected = []
        self.assertEqual(test_case_17_2_expected, test_case_17_2.error_list)

    # US18
    def test_check_siblings_should_not_marry(self):
        test_case_18_1 = Gedcom("test_example_18_1")
        test_case_18_1.check_siblings_should_not_marry()
        test_case_18_1_expected = ['ERROR: US18: FAMILY: @F2@, there is marriage between siblings.']
        self.assertEqual(test_case_18_1_expected, test_case_18_1.error_list)

        test_case_18_2 = Gedcom("test_example_18_2")
        test_case_18_2.check_siblings_should_not_marry()
        test_case_18_2_expected = []
        self.assertEqual(test_case_18_2_expected, test_case_18_2.error_list)


if __name__ == '__main__':
    unittest.main()
