import unittest
from gedcom import Gedcom


class TestCheckFunctionsSprint02(unittest.TestCase):
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

    # US22
    def test_check_unique_id(self):
        test_case_22_1 = Gedcom("test_example_22_1")
        test_case_22_1.check_unique_id()
        test_case_22_1_expected = []
        self.assertEqual(test_case_22_1_expected, test_case_22_1.error_list)

        test_case_22_2 = Gedcom("test_example_22_2")
        test_case_22_2.check_unique_id()
        test_case_22_2_expected = ["ANOMALY: US22: FAMILY: @F1@ is not unique.",
                                   "ANOMALY: US22: INDIVIDUAL: @I1@ is not unique."]
        self.assertEqual(test_case_22_2_expected, test_case_22_2.error_list)

    # US12
    def test_check_parents_not_too_old(self):
        test_case_12_1 = Gedcom("test_example_12_1")
        test_case_12_1.check_parents_not_too_old()
        test_case_12_1_expected = []
        self.assertEqual(test_case_12_1_expected, test_case_12_1.error_list)

        test_case_12_2 = Gedcom("test_example_12_2")
        test_case_12_2.check_parents_not_too_old()
        test_case_12_2_expected = ['ERROR: US12: FAMILY: @F1@: Mother: @I2@ is more than 60 years older than her children: @I3@',
                                   'ERROR: US12: FAMILY: @F1@: Father: @I1@ is more than 80 years older than his children: @I3@']
        self.assertEqual(test_case_12_2_expected, test_case_12_2.error_list)


if __name__ == '__main__':
    unittest.main()

